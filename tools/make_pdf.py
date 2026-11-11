"""Render a paper JSON to a printable PDF via headless Chrome.

Usage:
    python tools/make_pdf.py <paper_id> [--answers] [--solutions] [--topics] [--out PATH]

<paper_id> is a full paper (2024-S1) or a topic mock (digital-logic-03).

Flags:
    --answers     Append an answer-key table at the end.
    --solutions   Append the site's worked solutions (implies --answers).
    --topics      Show topic / subtopic next to each question.
    --out PATH    Output file (default: pdfs/<paper_id>[-key].pdf).

Math is rendered by KaTeX (loaded from cdnjs, so the first run needs internet).
Images come from cache/images/<source paper id>/ when downloaded, otherwise the site URL.
Question HTML is reduced to an allow-list of tags before rendering.
"""

from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import subprocess
import sys
import tempfile
import urllib.parse

from bs4 import BeautifulSoup, NavigableString, Tag

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "papers"
MOCKS_DIR = ROOT / "mocks"
IMAGES_DIR = ROOT / "cache" / "images"
PDF_DIR = ROOT / "pdfs"
SITE = "https://practicepaper.in"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
KATEX = "https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9"

ALLOWED_TAGS = {"br", "b", "strong", "i", "em", "u", "s", "sub", "sup", "p", "span", "div",
                "pre", "code", "table", "thead", "tbody", "tr", "td", "th", "ul", "ol", "li",
                "img", "a", "hr", "center"}
DROP_TAGS = {"script", "style", "iframe", "object", "embed", "link", "meta", "form",
             "input", "button", "svg", "math"}
LATEX_RE = re.compile(r"\[latex\]([\s\S]*?)\[/latex\]")
STRAY_LT_RE = re.compile(r"<(?!/?(?:" + "|".join(sorted(ALLOWED_TAGS)) + r")[\s/>])", re.IGNORECASE)
PLACEHOLDER_RE = re.compile("(\\d+)")


def find_paper(paper_id: str) -> pathlib.Path | None:
    """Path of a full paper or a topic mock, or None when neither exists."""
    for folder in (PAPERS_DIR, MOCKS_DIR):
        path = folder / f"{paper_id}.json"
        if path.exists() and path.name != "index.json":
            return path
    return None


def image_folder(question: dict, paper: dict) -> str:
    """Folder under cache/images/: a mock question's images live under its original paper."""
    return question.get("source_paper_id") or paper["paper_id"]


def image_src(src: str, paper_id: str) -> str:
    remote = src if re.match(r"https?://", src, re.I) else urllib.parse.urljoin(SITE + "/", src)
    name = pathlib.PurePosixPath(urllib.parse.urlparse(remote).path).name
    local = IMAGES_DIR / paper_id / name
    return local.as_uri() if name and local.exists() else remote


def clean(node: Tag, paper_id: str) -> None:
    for child in list(node.children):
        if isinstance(child, NavigableString):
            continue
        if not isinstance(child, Tag):
            child.extract()
            continue
        name = child.name.lower()
        if name in DROP_TAGS:
            child.decompose()
            continue
        if name not in ALLOWED_TAGS:
            clean(child, paper_id)
            child.unwrap()
            continue
        attrs = dict(child.attrs)
        child.attrs = {}
        if name == "img" and attrs.get("src"):
            child["src"] = image_src(attrs["src"], paper_id)
            child["alt"] = "figure"
        if name == "a" and re.match(r"https?://", str(attrs.get("href", "")), re.I):
            child["href"] = attrs["href"]
        for span_attr in ("colspan", "rowspan"):
            if name in ("td", "th") and str(attrs.get(span_attr, "")).isdigit():
                child[span_attr] = attrs[span_attr]
        clean(child, paper_id)


def rich(raw: str | None, paper_id: str) -> str:
    if not raw:
        return ""
    maths: list[str] = []

    def stash(m: re.Match) -> str:
        maths.append(m.group(1))
        return f"{len(maths) - 1}"

    text = LATEX_RE.sub(stash, raw)
    text = re.sub(r"<br\s*/?>[ \t]*\n", "<br>", text, flags=re.IGNORECASE)
    text = STRAY_LT_RE.sub("&lt;", text)
    soup = BeautifulSoup(f"<div>{text}</div>", "html.parser")
    root = soup.div
    clean(root, paper_id)
    body = root.decode_contents()

    def unstash(m: re.Match) -> str:
        tex = maths[int(m.group(1))]
        tex = re.sub(r"<br\s*/?>", " ", tex, flags=re.IGNORECASE)
        tex = html.unescape(re.sub(r"<[^>]*>", "", tex)).strip()
        return f'<span class="math">{html.escape(tex)}</span>'

    return PLACEHOLDER_RE.sub(unstash, body)


def answer_text(q: dict) -> str:
    if q.get("marks_to_all"):
        return "Marks to all (dropped in the official key)"

    def one(alt: list) -> str:
        if q["type"] == "NAT":
            lo, hi = float(alt[0]), float(alt[1])
            return f"{lo:g}" if lo == hi else f"{lo:g} to {hi:g}"
        return ", ".join(alt)

    primary = q["nat_range"] if q["type"] == "NAT" else q["correct"]
    return " or ".join(one(alt) for alt in [primary, *q.get("accepted", [])])


def build_html(paper: dict, answers: bool, solutions: bool, topics: bool) -> str:
    qs = paper["questions"]
    parts: list[str] = []
    for q in qs:
        pid = image_folder(q, paper)
        neg = f", −{q['negative_marks']:g}" if q["negative_marks"] else ""
        meta = f"{q['type']} · {q['marks']} mark{'s' if q['marks'] > 1 else ''}{neg}"
        if topics:
            meta += f" · {html.escape(q['topic'])}"
            if q["subtopic"]:
                meta += f" / {html.escape(q['subtopic'])}"
        block = [f'<section class="q"><div class="qhead"><b>Q{q["number"]}.</b> <span>{meta}</span></div>',
                 f'<div class="rich">{rich(q["question"], pid)}</div>']
        if q["options"]:
            block.append('<ol class="opts">')
            for letter, text in q["options"].items():
                block.append(f'<li><b>({letter})</b> <div class="rich">{rich(text, pid)}</div></li>')
            block.append("</ol>")
        else:
            block.append('<div class="nat">Answer: ____________</div>')
        block.append("</section>")
        parts.append("".join(block))

    key = ""
    if answers or solutions:
        rows = "".join(f"<tr><td>Q{q['number']}</td><td>{q['type']}</td><td>{html.escape(answer_text(q))}</td></tr>" for q in qs)
        key = f'<h2 class="break">Answer key</h2><table class="key"><tr><th>Q</th><th>Type</th><th>Answer</th></tr>{rows}</table>'
    sols = ""
    if solutions:
        items = []
        for q in qs:
            if not q["explanation"]:
                continue
            pid = image_folder(q, paper)
            items.append(f'<section class="q"><div class="qhead"><b>Q{q["number"]}.</b> '
                         f'<span>Answer: {html.escape(answer_text(q))}</span></div>'
                         f'<div class="rich">{rich(q["explanation"], pid)}</div></section>')
        sols = '<h2 class="break">Solutions</h2>' + "".join(items)

    type_counts = {t: sum(q["type"] == t for q in qs) for t in ("MCQ", "MSQ", "NAT")}
    title = html.escape(paper["paper"])
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><title>{title}</title>
<link rel="stylesheet" href="{KATEX}/katex.min.css">
<script src="{KATEX}/katex.min.js"></script>
<style>
  @page {{ size: A4; margin: 16mm 14mm; }}
  body {{ font: 10.5pt/1.5 -apple-system, "Helvetica Neue", Arial, sans-serif; color: #111; }}
  h1 {{ font-size: 17pt; margin: 0 0 2px; }}
  h2 {{ font-size: 14pt; }}
  .sub {{ color: #555; margin: 0 0 14px; }}
  .q {{ break-inside: avoid; border-top: 1px solid #ccc; padding: 8px 0 10px; }}
  .qhead {{ margin-bottom: 4px; }}
  .qhead span {{ color: #555; font-size: 9pt; margin-left: 6px; }}
  .rich {{ white-space: pre-wrap; overflow-wrap: anywhere; }}
  .rich pre {{ white-space: pre; background: #f3f3f3; padding: 6px 8px; border-radius: 4px; font: 9pt/1.4 Menlo, Consolas, monospace; }}
  .rich img {{ max-width: 85%; max-height: 90mm; display: block; margin: 6px 0; }}
  .rich table {{ border-collapse: collapse; white-space: normal; }}
  .rich td, .rich th {{ border: 1px solid #999; padding: 2px 6px; }}
  .opts {{ list-style: none; padding: 0; margin: 6px 0 0; }}
  .opts li {{ display: flex; gap: 6px; margin: 3px 0; }}
  .nat {{ margin-top: 8px; color: #333; }}
  .break {{ break-before: page; }}
  table.key {{ border-collapse: collapse; }}
  table.key td, table.key th {{ border: 1px solid #999; padding: 2px 10px; text-align: left; }}
</style></head>
<body>
<h1>{title}</h1>
<p class="sub">{len(qs)} questions · {paper['total_marks']} marks · {paper.get('duration_min', 180)} minutes ·
MCQ {type_counts['MCQ']}, MSQ {type_counts['MSQ']}, NAT {type_counts['NAT']} ·
MCQ wrong answers cost 1/3 of their marks; MSQ and NAT have no negative marking.</p>
{''.join(parts)}
{key}
{sols}
<script>
  document.querySelectorAll(".math").forEach(function (el) {{
    if (window.katex) katex.render(el.textContent, el, {{ throwOnError: false }});
  }});
</script>
</body></html>
"""


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paper_id")
    parser.add_argument("--answers", action="store_true")
    parser.add_argument("--solutions", action="store_true")
    parser.add_argument("--topics", action="store_true")
    parser.add_argument("--out", type=pathlib.Path)
    args = parser.parse_args(argv[1:])

    paper_path = find_paper(args.paper_id)
    if paper_path is None:
        print(f"No such paper or topic mock: {args.paper_id}", file=sys.stderr)
        return 1
    if not pathlib.Path(CHROME).exists():
        print(f"Google Chrome not found at {CHROME}", file=sys.stderr)
        return 1

    paper = json.loads(paper_path.read_text())
    with_key = args.answers or args.solutions
    out = args.out or PDF_DIR / f"{args.paper_id}{'-key' if with_key else ''}.pdf"
    out = out.resolve()
    out.parent.mkdir(parents=True, exist_ok=True)

    page = build_html(paper, args.answers, args.solutions, args.topics)
    with tempfile.TemporaryDirectory() as tmp:
        html_path = pathlib.Path(tmp) / f"{args.paper_id}.html"
        html_path.write_text(page, encoding="utf-8")
        cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
               "--allow-file-access-from-files", "--virtual-time-budget=20000",
               f"--print-to-pdf={out}", html_path.as_uri()]
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=180)
    if proc.returncode != 0 or not out.exists():
        print(f"Chrome failed (exit {proc.returncode}):\n{proc.stderr[-2000:]}", file=sys.stderr)
        return 1
    print(f"Wrote {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out} ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
