"""Single-paper scraper for practicepaper.in GATE CSE pages.

Usage:
    python scraper/scrape_paper.py <slug> <paper_id>

Example:
    python scraper/scrape_paper.py gate-cse-2024-set-1 2024-S1

The slug is what appears after '/gate-cse/' in the URL. The paper_id is the
stable identifier used in file names and question ids (e.g. 2024-S1, 2020,
2015-S3).

Behaviour:
    - Fetches page 1 and every subsequent page listed in meta.totalPages.
    - Uses cache/html/<paper_id>_p<N>.html as a cache; only misses are fetched.
    - Sleeps 3 seconds between network fetches.
    - Writes papers/<paper_id>.json in the canonical schema.
"""

from __future__ import annotations

import datetime as dt
import json
import pathlib
import re
import sys
import time
import urllib.parse

import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / "cache" / "html"
PAPERS_DIR = ROOT / "papers"
SCHEMA_DIR = ROOT / "schema"

SITE_BASE = "https://practicepaper.in"
PATH_PREFIX = "/gate-cse/"
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
)
REQUEST_DELAY_SEC = 3

QUIZ_DATA_RE = re.compile(
    r"<script id='pp-quiz-data' type='application/json'>(.*?)</script>",
    re.DOTALL,
)
IMG_SRC_RE = re.compile(r"""<img[^>]+src=['"]([^'"]+)['"]""", re.IGNORECASE)
LETTERS = ["A", "B", "C", "D", "E"]


def load_topic_map() -> dict[str, str]:
    data = json.loads((SCHEMA_DIR / "topics.json").read_text())
    return data["aliases"]


def cache_path(paper_id: str, page: int) -> pathlib.Path:
    return CACHE_DIR / f"{paper_id}_p{page}.html"


def fetch_page(slug: str, paper_id: str, page: int) -> str:
    """Return the HTML for the given page, cache-first."""
    path = cache_path(paper_id, page)
    if path.exists():
        return path.read_text(encoding="utf-8")
    url = f"{SITE_BASE}{PATH_PREFIX}{slug}"
    if page > 1:
        url += f"?page_no={page}"
    print(f"  fetch page {page}: {url}", flush=True)
    time.sleep(REQUEST_DELAY_SEC)
    resp = requests.get(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        },
        timeout=30,
    )
    resp.raise_for_status()
    path.write_text(resp.text, encoding="utf-8")
    return resp.text


def parse_blob(html: str) -> dict:
    m = QUIZ_DATA_RE.search(html)
    if not m:
        raise RuntimeError("pp-quiz-data script tag not found on page")
    return json.loads(m.group(1))


def extract_images(*texts: str | None) -> list[str]:
    out: list[str] = []
    for t in texts:
        if not t:
            continue
        for src in IMG_SRC_RE.findall(t):
            url = urllib.parse.urljoin(SITE_BASE, src)
            if url not in out:
                out.append(url)
    return out


def canonical_topic(tag: str | None, aliases: dict[str, str]) -> str:
    tag = (tag or "").strip()
    if not tag:
        raise RuntimeError("question has no topic tag")
    folded = {k.casefold(): v for k, v in aliases.items()}
    if tag.casefold() in folded:
        return folded[tag.casefold()]
    raise RuntimeError(
        f"unknown topic tag {tag!r}; add it to schema/topics.json aliases"
    )


def load_topic_overrides() -> dict[str, dict]:
    path = SCHEMA_DIR / "topic_overrides.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text())
    canonical = set(json.loads((SCHEMA_DIR / "topics.json").read_text())["canonical_topics"])
    for qid, entry in data["overrides"].items():
        if entry["topic"] not in canonical:
            raise RuntimeError(f"topic_overrides.json: {qid} uses non-canonical topic {entry['topic']!r}")
    return data["overrides"]


def normalize_question(raw: dict, paper_id: str, aliases: dict[str, str]) -> dict:
    qtype = raw["type"]
    number = int(raw["number"])
    marks = int(raw["marks"])
    subtopic = (raw.get("tag2") or "").strip() or None
    override = load_topic_overrides().get(f"{paper_id}-Q{number}")
    if not (raw.get("tag1") or "").strip() and override:
        topic = override["topic"]
        subtopic = subtopic or override.get("subtopic")
    else:
        topic = canonical_topic(raw.get("tag1"), aliases)
    section = "General Aptitude" if topic == "General Aptitude" else "Technical"

    options: dict[str, str] | None = None
    correct: list[str] | None = None
    nat_range: list[float] | None = None
    negative_marks: float = 0.0

    if qtype == "MCQ":
        opts = raw.get("options") or []
        if len(opts) not in (4, 5):
            raise RuntimeError(f"Q{number}: MCQ with {len(opts)} options")
        options = {LETTERS[i]: opts[i] for i in range(len(opts))}
        idx = raw.get("correct")
        if not isinstance(idx, int) or not (0 <= idx < len(opts)):
            raise RuntimeError(f"Q{number}: MCQ 'correct' not an option index: {idx!r}")
        correct = [LETTERS[idx]]
        negative_marks = round(marks / 3, 2)
    elif qtype == "MSQ":
        opts = raw.get("options") or []
        if len(opts) not in (4, 5):
            raise RuntimeError(f"Q{number}: MSQ with {len(opts)} options")
        options = {LETTERS[i]: opts[i] for i in range(len(opts))}
        idxs = raw.get("correctSet")
        if not isinstance(idxs, list) or not idxs or not all(
            isinstance(i, int) and 0 <= i < len(opts) for i in idxs
        ):
            raise RuntimeError(f"Q{number}: MSQ 'correctSet' invalid: {idxs!r}")
        correct = [LETTERS[i] for i in sorted(set(idxs))]
    elif qtype == "NAT":
        if raw.get("options"):
            raise RuntimeError(f"Q{number}: NAT unexpectedly has options")
        lo = raw.get("ansMin")
        hi = raw.get("ansMax")
        if not isinstance(lo, (int, float)) or not isinstance(hi, (int, float)):
            raise RuntimeError(f"Q{number}: NAT missing ansMin/ansMax: {lo!r},{hi!r}")
        if lo > hi:
            raise RuntimeError(f"Q{number}: NAT ansMin > ansMax ({lo}>{hi})")
        nat_range = [float(lo), float(hi)]
    else:
        raise RuntimeError(f"Q{number}: unknown type {qtype!r}")

    solution = raw.get("solution")
    explanation_source = "site" if solution else "none"

    return {
        "id": f"{paper_id}-Q{number}",
        "source_id": int(raw["id"]),
        "number": number,
        "section": section,
        "type": qtype,
        "marks": marks,
        "negative_marks": negative_marks,
        "question": raw.get("text", ""),
        "code": None,
        "images": extract_images(raw.get("text"), raw.get("solution")),
        "options": options,
        "correct": correct,
        "nat_range": nat_range,
        "topic": topic,
        "subtopic": subtopic,
        "explanation": solution or None,
        "explanation_source": explanation_source,
    }


def apply_key_overrides(questions: list[dict]) -> None:
    path = SCHEMA_DIR / "key_overrides.json"
    if not path.exists():
        return
    overrides = json.loads(path.read_text())["overrides"]
    for q in questions:
        entry = overrides.get(q["id"])
        if not entry:
            continue
        if "nat_range" in entry:
            if q["type"] != "NAT":
                raise RuntimeError(f"key_overrides.json: {q['id']} is {q['type']}, not NAT")
            q["nat_range"] = [float(x) for x in entry["nat_range"]]
        if "accepted" in entry:
            q["accepted"] = entry["accepted"]
        if entry.get("marks_to_all"):
            q["marks_to_all"] = True
        q["key_source"] = entry["source"]


def apply_marks_overrides(paper_id: str, questions: list[dict], total_marks: int) -> int:
    """Fix per-question marks for papers where the site lists everything as 1 mark.

    Returns the paper's total marks (corrected if an override exists).
    """
    path = SCHEMA_DIR / "marks_overrides.json"
    if not path.exists():
        return total_marks
    entry = json.loads(path.read_text())["papers"].get(paper_id)
    if not entry:
        return total_marks
    for q in questions:
        q["marks"] = 1 if q["number"] <= entry["one_mark_up_to"] else 2
        if q["type"] == "MCQ":
            q["negative_marks"] = round(q["marks"] / 3, 2)
    total = sum(q["marks"] for q in questions)
    if total != entry["total_marks"]:
        raise RuntimeError(f"marks_overrides.json: {paper_id} sums to {total}, expected {entry['total_marks']}")
    return total


def parse_paper_id(paper_id: str) -> tuple[int, int | None]:
    m = re.fullmatch(r"(\d{4})(?:-S([1-9]))?", paper_id)
    if not m:
        raise SystemExit(f"bad paper_id {paper_id!r}, expected YYYY or YYYY-S<n>")
    year = int(m.group(1))
    set_num = int(m.group(2)) if m.group(2) else None
    return year, set_num


def scrape(slug: str, paper_id: str) -> dict:
    aliases = load_topic_map()
    year, set_num = parse_paper_id(paper_id)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    html1 = fetch_page(slug, paper_id, 1)
    blob1 = parse_blob(html1)
    meta = blob1["meta"]
    total_pages = int(meta["totalPages"])
    total_questions_meta = int(meta["totalQuestions"])
    print(
        f"  meta: quiz={meta['quizName']!r}, totalPages={total_pages}, "
        f"totalQuestions={total_questions_meta}, totalMarks={meta['totalMarks']}",
        flush=True,
    )

    raw_questions: list[dict] = list(blob1["questions"])
    for p in range(2, total_pages + 1):
        html = fetch_page(slug, paper_id, p)
        blob = parse_blob(html)
        raw_questions.extend(blob["questions"])

    # Deduplicate by source id, then sort by number.
    by_source_id: dict[int, dict] = {}
    for q in raw_questions:
        by_source_id[int(q["id"])] = q
    raw_sorted = sorted(by_source_id.values(), key=lambda q: int(q["number"]))

    questions = [normalize_question(q, paper_id, aliases) for q in raw_sorted]
    apply_key_overrides(questions)
    total_marks = apply_marks_overrides(paper_id, questions, int(meta["totalMarks"]))

    # Sanity.
    numbers = [q["number"] for q in questions]
    if numbers != list(range(1, len(questions) + 1)):
        gaps = [n for n in range(1, len(questions) + 1) if n not in set(numbers)]
        extras = [n for n in numbers if numbers.count(n) > 1]
        raise RuntimeError(
            f"question numbering gaps or duplicates: gaps={gaps}, extras={extras}"
        )
    if len(questions) != total_questions_meta:
        raise RuntimeError(
            f"got {len(questions)} questions but meta.totalQuestions={total_questions_meta}"
        )

    paper = {
        "paper_id": paper_id,
        "paper": meta["quizName"],
        "year": year,
        "set": set_num,
        "source_url": urllib.parse.urljoin(SITE_BASE + PATH_PREFIX, slug),
        "source_id": int(meta.get("quizId", 0)) or None,
        "total_marks": total_marks,
        "scraped_at": dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "questions": questions,
    }
    return paper


def main(argv: list[str]) -> int:
    if len(argv) != 3:
        print(__doc__, file=sys.stderr)
        return 2
    slug, paper_id = argv[1], argv[2]
    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Scraping {slug} as paper_id={paper_id}", flush=True)
    paper = scrape(slug, paper_id)
    out_path = PAPERS_DIR / f"{paper_id}.json"
    out_path.write_text(json.dumps(paper, ensure_ascii=False, indent=2) + "\n")

    # Summary
    counts = {"MCQ": 0, "MSQ": 0, "NAT": 0}
    sec = {"General Aptitude": 0, "Technical": 0}
    for q in paper["questions"]:
        counts[q["type"]] += 1
        sec[q["section"]] += 1
    print(f"Wrote {out_path.relative_to(ROOT)}")
    print(
        f"  {len(paper['questions'])} questions: "
        f"MCQ={counts['MCQ']}, MSQ={counts['MSQ']}, NAT={counts['NAT']}; "
        f"GA={sec['General Aptitude']}, Technical={sec['Technical']}; "
        f"total_marks={paper['total_marks']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
