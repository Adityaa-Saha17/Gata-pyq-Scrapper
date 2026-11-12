"""Index of the study material PDFs, and the lookup that ties a question to them.

Usage:
    python tools/study_index.py            build cache/study_index.json if it is stale
    python tools/study_index.py --rebuild  build it even if it looks fresh
    python tools/study_index.py --check    also check schema/study_map.json and report coverage

The three books in "Study Materials/" (filter1_volume1..3.pdf) each hold chapters made of

    Topic-wise Key Concepts     revision notes, one heading per subtopic
    numbered sections           "5.8 Disk Scheduling (16)": the past questions on a subtopic,
                                each with a link to its gateoverflow.in page

The index records where every chapter, notes heading and numbered section starts (page and
distance from the top of the page), and which numbered section each past question is in.

lookup() then answers, for one question from papers/ or mocks/, where to read about it:

    1. The question itself is in a book (matched by the gateoverflow id in its solution link):
       the notes for the subtopic the book files it under.
    2. Otherwise the question's own topic/subtopic, through schema/study_map.json.
    3. Subtopic not in the books: the notes of the topic's chapter(s).
    4. Topic not in the books: nothing to link, and the result says so.

The index is rebuilt by itself when a PDF changes (size or modification time).
"""
from __future__ import annotations

import argparse
import collections
import glob
import json
import pathlib
import re
import sys
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
STUDY_DIR = ROOT / "Study Materials"
INDEX_PATH = ROOT / "cache" / "study_index.json"
MAP_PATH = ROOT / "schema" / "study_map.json"
VOLUMES = (1, 2, 3)
INDEX_VERSION = 1

GO_ID = re.compile(r"https?://gateoverflow\.in/(\d+)")
GO_QUESTION = re.compile(r"https?://gateoverflow\.in/(\d+)/[^#]+$")  # the question's title link
CHAPTER = re.compile(r"(\d+) (.+?) \((\d+)\)$")                      # "5 Operating System (343)"
SECTION = re.compile(r"(\d+\.\d+) (.+?) \((\d+)\)$")                 # "5.8 Disk Scheduling (16)"
NOTES_START = "Topic-wise Key Concepts"
NOTES_END = ("Quick Formula Reference", "Important Tips for GATE")
ANSWER_KEYS = "Answer Keys"
# Chrome's PDF viewer measures '#zoom=100,left,top' in CSS pixels from the top of the page.
PX_PER_PT = 96 / 72
TOP_MARGIN_PT = 8  # leave a little space above the heading


def pdf_path(vol: int) -> pathlib.Path:
    return STUDY_DIR / f"filter1_volume{vol}.pdf"


def norm(name: str) -> str:
    """'Dijkstra's Algorithm' and 'Dijkstras Algorithm' compare equal."""
    name = re.sub(r"^\d+\.\s+", "", name)  # '6. Image Rotation'
    name = re.sub(r"\(.*?\)", " ", name).lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "", name)


def name_keys(name: str) -> list[str]:
    """The heading itself first, then what it has in brackets or around a slash.

    'SRTF (Shortest Remaining Time First)' -> srtf, shortestremainingtimefirst
    'Tables / Tabular Data'                -> tablestabulardata, tables, tabulardata
    """
    keys = [norm(name)]
    for inner in re.findall(r"\((.*?)\)", name):
        keys.append(norm(re.sub(r"^for ", "", inner)))
    if "/" in name:
        keys += [norm(part) for part in re.sub(r"\(.*?\)", " ", name).split("/")]
    return [k for k in dict.fromkeys(keys) if k]


# ---------------------------------------------------------------- building

def source_stamp() -> dict | None:
    """Size and mtime of each PDF; None when a book is missing."""
    stamp = {}
    for vol in VOLUMES:
        path = pdf_path(vol)
        if not path.exists():
            return None
        stat = path.stat()
        stamp[path.name] = {"size": stat.st_size, "mtime": int(stat.st_mtime)}
    return stamp


def read_outline(pdf) -> list[tuple[int, str, int, float]]:
    """Bookmarks as (level, title, page index, points from the top of the page)."""
    heights: dict[int, float] = {}
    entries = []
    for bookmark in pdf.get_toc():
        dest = bookmark.get_dest()
        if dest is None or dest.get_index() is None:
            continue
        page = dest.get_index()
        if page not in heights:
            heights[page] = pdf[page].get_height()
        _, pos = dest.get_view()
        y = pos[1] if len(pos) > 1 else heights[page]
        entries.append((bookmark.level, (bookmark.get_title() or "").strip(), page, round(heights[page] - y, 1)))
    return entries


def text_headings(pdf, start: tuple[int, float], end: tuple[int, float]) -> list[dict]:
    """Notes headings found in the text between two (page, top) positions.

    Some chapters bookmark only the start of their notes. Their subtopic headings are
    still there as a short all-bold line at the left margin.
    """
    import ctypes

    import pypdfium2.raw as raw

    name = ctypes.create_string_buffer(128)
    flags = ctypes.c_int()

    def bold(textpage, i: int) -> bool:
        raw.FPDFText_GetFontInfo(textpage, i, name, len(name), ctypes.byref(flags))
        return b"Bold" in name.value

    found = []
    for index in range(start[0], min(end[0], len(pdf) - 1) + 1):
        page = pdf[index]
        height = page.get_height()
        textpage = page.get_textpage()
        lines: list[list[tuple[int, str]]] = [[]]
        for i in range(textpage.count_chars()):
            char = chr(raw.FPDFText_GetUnicode(textpage, i))
            if char in "\r\n":
                if lines[-1]:
                    lines.append([])
            else:
                lines[-1].append((i, char))
        for line in lines:
            inked = [i for i, char in line if char.strip()]
            text = "".join(char for _, char in line).strip()
            if not inked or not 2 < len(text) <= 70 or ":" in text:
                continue
            left, _, _, glyph_top = textpage.get_charbox(inked[0])
            top = round(max(0.0, height - glyph_top - 6.0), 1)
            if left > 41 or (index, top) <= start or (index, top) >= end:
                continue
            if text in (NOTES_START, ANSWER_KEYS, *NOTES_END):
                continue
            if all(bold(textpage, i) for i in inked):
                found.append({"title": text, "page": index, "top": top})
    return found


def build_index() -> dict:
    import pdfplumber
    import pypdfium2 as pdfium

    stamp = source_stamp()
    if stamp is None:
        raise FileNotFoundError(f"study material PDFs not found in {STUDY_DIR}")
    chapters: list[dict] = []
    questions: dict[str, list[int]] = {}

    for vol in VOLUMES:
        path = pdf_path(vol)
        fast = pdfium.PdfDocument(str(path))  # bookmarks and text; pdfplumber reads the links
        outline = read_outline(fast)
        with pdfplumber.open(path) as pdf:
            # Split the bookmarks into chapters.
            groups: list[tuple[tuple, list]] = []
            for level, title, page, top in outline:
                if level == 0:
                    groups.append(((title, page, top), []))
                elif level == 1 and groups:
                    groups[-1][1].append((title, page, top))

            vol_chapters = []
            for (title, page, top), children in groups:
                match = CHAPTER.match(title)
                if not match:
                    continue  # Table of Contents, Contributors
                chapter = {
                    "key": f"{vol}.{match.group(1)}", "vol": vol, "file": path.name,
                    "title": match.group(2), "count": int(match.group(3)),
                    "page": page, "top": top, "notes": None, "headings": [], "sections": [],
                }
                notes_end = answers = None
                for child_title, child_page, child_top in children:
                    pos = {"page": child_page, "top": child_top}
                    section = SECTION.match(child_title)
                    if child_title == NOTES_START:
                        chapter["notes"] = pos
                    elif section:
                        notes_end = notes_end or (child_page, child_top)
                        chapter["sections"].append({"num": section.group(1), "name": section.group(2),
                                                    "count": int(section.group(3)), **pos, "notes": None})
                    elif child_title in NOTES_END:
                        notes_end = notes_end or (child_page, child_top)
                    elif child_title == ANSWER_KEYS:
                        answers = (child_page, child_top)
                    elif chapter["notes"] and notes_end is None:
                        chapter["headings"].append({"title": child_title, **pos})

                # Headings that are in the text but not in the bookmarks.
                if chapter["notes"] and notes_end:
                    start = (chapter["notes"]["page"], chapter["notes"]["top"] + 6)
                    known = {norm(h["title"]) for h in chapter["headings"]}
                    for heading in text_headings(fast, start, notes_end):
                        if norm(heading["title"]) not in known:
                            known.add(norm(heading["title"]))
                            chapter["headings"].append(heading)
                    chapter["headings"].sort(key=lambda h: (h["page"], h["top"]))

                # Which notes heading belongs to each numbered section.
                by_key: dict[str, int] = {}
                for rank in (0, 1):  # full names first, bracketed alternatives second
                    for i, heading in enumerate(chapter["headings"]):
                        keys = name_keys(heading["title"])
                        for key in (keys[:1] if rank == 0 else keys[1:]):
                            by_key.setdefault(key, i)
                for section in chapter["sections"]:
                    section["notes"] = by_key.get(norm(section["name"]))
                # 'Infix Prefix' -> 'Infix, Prefix, Postfix Notations': the one unclaimed
                # heading that starts with the section's name.
                claimed = {s["notes"] for s in chapter["sections"]}
                for section in chapter["sections"]:
                    wanted = norm(section["name"])
                    if section["notes"] is None and len(wanted) >= 6:
                        starts = [i for i, h in enumerate(chapter["headings"])
                                  if i not in claimed and norm(h["title"]).startswith(wanted)]
                        if len(starts) == 1:
                            section["notes"] = starts[0]
                            claimed.add(starts[0])

                chapter["_end"] = answers or (len(pdf.pages), 0)
                vol_chapters.append(chapter)

            # Place each past question in its numbered section.
            for chapter in vol_chapters:
                if not chapter["sections"]:
                    continue
                c_index = len(chapters)
                starts = [(s["page"], s["top"]) for s in chapter["sections"]]
                for index in range(starts[0][0], min(chapter["_end"][0], len(pdf.pages) - 1) + 1):
                    for link in pdf.pages[index].hyperlinks:
                        match = GO_QUESTION.match(link.get("uri") or "")
                        if not match:
                            continue
                        pos = (index, link["top"] + 6)
                        if pos < starts[0] or pos >= chapter["_end"]:
                            continue
                        s_index = max(i for i, start in enumerate(starts) if start <= pos)
                        questions.setdefault(match.group(1), [c_index, s_index])
                del chapter["_end"]
                chapters.append(chapter)
            for chapter in vol_chapters:  # chapters without numbered sections
                if "_end" in chapter:
                    del chapter["_end"]
                    chapters.append(chapter)
        fast.close()

    return {"version": INDEX_VERSION, "source": stamp, "chapters": chapters, "questions": questions}


def load_index(rebuild: bool = False) -> dict | None:
    """The index, rebuilt first when missing or older than the PDFs. None when the books are missing."""
    stamp = source_stamp()
    if stamp is None:
        return None
    if not rebuild:
        try:
            index = json.loads(INDEX_PATH.read_text())
            if index.get("version") == INDEX_VERSION and index.get("source") == stamp:
                return index
        except (OSError, ValueError):
            pass
    index = build_index()
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text(json.dumps(index, separators=(",", ":")) + "\n")
    return index


# ---------------------------------------------------------------- lookup

class StudyGuide:
    """Finds the study material for a question. Build one per run, then call lookup()."""

    def __init__(self, index: dict, study_map: dict):
        self.index = index
        self.topics: dict[str, list[str]] = study_map.get("topics", {})
        self.subtopics: dict[str, dict[str, list[str]]] = {
            topic: {norm(name): targets for name, targets in names.items()}
            for topic, names in study_map.get("subtopics", {}).items()
        }
        self.chapters = {c["key"]: c for c in index["chapters"]}

    @classmethod
    def load(cls) -> "StudyGuide | None":
        """None when the PDFs are not there, so callers can simply leave the links out."""
        index = load_index()
        if index is None:
            return None
        return cls(index, json.loads(MAP_PATH.read_text()))

    # -- references --------------------------------------------------------

    def _place(self, chapter: dict, pos: dict | None) -> dict | None:
        if pos is None:
            return None
        return {"file": chapter["file"], "vol": chapter["vol"], "page": pos["page"] + 1, "top": pos["top"]}

    def _chapter_ref(self, chapter: dict) -> dict:
        return {"title": chapter["title"], "scope": "topic",
                "notes": self._place(chapter, chapter["notes"] or chapter), "practice": None, "count": None}

    def _section_ref(self, chapter: dict, section: dict) -> dict:
        heading = chapter["headings"][section["notes"]] if section["notes"] is not None else None
        return {"title": heading["title"] if heading else section["name"], "scope": "subtopic",
                "notes": self._place(chapter, heading), "practice": self._place(chapter, section),
                "count": section["count"]}

    def resolve(self, target: str) -> dict | None:
        """A study_map target: '3.5' is a chapter, '3.5/Disk Scheduling' a subtopic in it."""
        key, _, name = target.partition("/")
        chapter = self.chapters.get(key)
        if chapter is None:
            return None
        if not name:
            return self._chapter_ref(chapter)
        wanted = norm(name)
        for section in chapter["sections"]:
            if norm(section["name"]) == wanted:
                return self._section_ref(chapter, section)
        for i, heading in enumerate(chapter["headings"]):
            if wanted in name_keys(heading["title"]):
                # Notes without a question section of the same name.
                section = next((s for s in chapter["sections"] if s["notes"] == i), None)
                if section:
                    return self._section_ref(chapter, section)
                return {"title": heading["title"], "scope": "subtopic",
                        "notes": self._place(chapter, heading), "practice": None, "count": None}
        return None

    # -- the lookup --------------------------------------------------------

    def lookup(self, question: dict) -> dict:
        """Where to read about this question.

        Returns {"level": "subtopic" | "topic" | "none", "refs": [...], "note": str | None}.
        Each ref has a title and up to two places: "notes" and "practice" (the past
        questions on it), each {"file", "vol", "page" (1-based), "top" (points)}.
        """
        topic, subtopic = question.get("topic") or "", question.get("subtopic")
        refs: list[dict] = []
        questions_only: list[dict] = []  # a book section without notes: listed last

        # 1. The question is in a book: use the subtopic the book files it under.
        for go_id in GO_ID.findall(question.get("explanation") or ""):
            found = self.index["questions"].get(go_id)
            if found:
                chapter = self.index["chapters"][found[0]]
                ref = self._section_ref(chapter, chapter["sections"][found[1]])
                (refs if ref["notes"] else questions_only).append(ref)
                break

        # 2. The question's own subtopic, when that has not led to any notes yet.
        if not refs and subtopic:
            for target in self.subtopics.get(topic, {}).get(norm(subtopic), []):
                ref = self.resolve(target)
                if ref and ref["notes"]:
                    refs.append(ref)

        if refs:
            return {"level": "subtopic", "refs": refs + questions_only, "note": None}

        # 3. Only the topic is covered.
        chapter_refs = [ref for ref in map(self.resolve, self.topics.get(topic, [])) if ref]
        if chapter_refs:
            if subtopic:
                note = f"The subtopic “{subtopic}” has no notes of its own in the study material. Topic notes:"
            else:
                note = "This question has no subtopic tag. Topic notes:"
            return {"level": "topic", "refs": chapter_refs + questions_only, "note": note}

        # 4. Not covered at all.
        return {"level": "none", "refs": questions_only,
                "note": f"The topic “{topic or 'untagged'}” is not covered in the study material."}


def href(place: dict, base: str) -> str:
    """Link that opens the PDF at the place. 'base' is the URL of the 'Study Materials' folder."""
    top_px = max(0, round((place["top"] - TOP_MARGIN_PT) * PX_PER_PT))
    return f"{base.rstrip('/')}/{urllib.parse.quote(place['file'])}#page={place['page']}&zoom=100,0,{top_px}"


# ---------------------------------------------------------------- command line

def check(guide: StudyGuide) -> int:
    """Report study_map targets that do not resolve, and how the scraped questions fare."""
    problems = 0
    for topic, targets in guide.topics.items():
        for target in targets:
            if guide.resolve(target) is None:
                problems += 1
                print(f"  unresolved topic target: {topic} -> {target}")
    for topic, names in json.loads(MAP_PATH.read_text()).get("subtopics", {}).items():
        for name, targets in names.items():
            for target in targets:
                ref = guide.resolve(target)
                if ref is None or not ref["notes"]:
                    problems += 1
                    print(f"  unresolved subtopic target: {topic} / {name} -> {target}")

    levels: dict[str, collections.Counter] = collections.defaultdict(collections.Counter)
    unmapped = collections.Counter()
    for path in sorted(glob.glob(str(ROOT / "papers" / "*.json"))):
        for question in json.loads(pathlib.Path(path).read_text())["questions"]:
            result = guide.lookup(question)
            levels[question["topic"]][result["level"]] += 1
            if result["level"] != "subtopic":
                unmapped[(question["topic"], question["subtopic"], result["level"])] += 1
    print("\nQuestions in papers/ by what the review can link:")
    print(f"  {'topic':42} {'subtopic':>9} {'topic':>6} {'none':>5}")
    for topic in sorted(levels):
        row = levels[topic]
        print(f"  {topic:42} {row['subtopic']:9} {row['topic']:6} {row['none']:5}")
    total = sum((row for row in levels.values()), collections.Counter())
    print(f"  {'TOTAL':42} {total['subtopic']:9} {total['topic']:6} {total['none']:5}")
    if unmapped:
        print("\nNot linked to a subtopic:")
        for (topic, subtopic, level), count in sorted(unmapped.items(), key=lambda kv: (-kv[1], str(kv[0]))):
            print(f"  {count:4}  {topic} / {subtopic}  ->  {level}")
    return 1 if problems else 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--rebuild", action="store_true")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args(argv[1:])

    index = load_index(rebuild=args.rebuild)
    if index is None:
        print(f"Study material PDFs not found in {STUDY_DIR}")
        return 1
    sections = sum(len(c["sections"]) for c in index["chapters"])
    with_notes = sum(1 for c in index["chapters"] for s in c["sections"] if s["notes"] is not None)
    print(f"{INDEX_PATH.relative_to(ROOT)}: {len(index['chapters'])} chapters, {sections} question sections "
          f"({with_notes} with their own notes), {len(index['questions'])} past questions")
    if args.check:
        return check(StudyGuide(index, json.loads(MAP_PATH.read_text())))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
