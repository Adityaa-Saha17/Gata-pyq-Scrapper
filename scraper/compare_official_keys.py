"""Compare the site's answer keys with the official GATE answer-key PDFs.

Usage:
    python scraper/compare_official_keys.py

Reads cache/official_keys/<paper_id>.pdf (official final keys, downloaded from
the GATE 2027 site's archive at gate2027.iitm.ac.in/download) and the matching
papers/<paper_id>.json.

Official numbering puts General Aptitude first (Q1-10) and the CS questions
after (Q11-65). The site lists CS questions first and GA last, so questions are
paired in order within each section; type and marks must match for every pair
or the paper is reported as misaligned and skipped.

Writes reports/official_key_check.json. Does not modify papers/.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

import pdfplumber

ROOT = pathlib.Path(__file__).resolve().parent.parent
KEYS_DIR = ROOT / "cache" / "official_keys"
PAPERS_DIR = ROOT / "papers"
REPORTS_DIR = ROOT / "reports"

ROW_RE = re.compile(r"^(\d+)\s+(\d+)\s+(MCQ|MSQ|NAT)\s+(GA|CS(?:-\d)?)\s+(.+?)\s+([12])$")
RANGE_RE = re.compile(r"(-?\d+(?:\.\d+)?)\s*to\s*(-?\d+(?:\.\d+)?)", re.IGNORECASE)


def parse_official(path: pathlib.Path) -> list[dict]:
    with pdfplumber.open(path) as pdf:
        lines = [ln.strip() for page in pdf.pages for ln in (page.extract_text() or "").splitlines()]
    rows = []
    for line in lines:
        m = ROW_RE.match(line)
        if m:
            number, _session, qtype, section, key, marks = m.groups()
            rows.append({"number": int(number), "type": qtype, "section": "GA" if section == "GA" else "CS",
                         "key": key.strip(), "marks": int(marks)})
    return rows


def parse_key(qtype: str, raw: str) -> dict:
    """Return {'mta': bool, 'alternatives': [...]} where each alternative is a letter list or [lo, hi]."""
    if raw.upper() == "MTA":
        return {"mta": True, "alternatives": []}
    parts = re.split(r"\s+or\s+", raw, flags=re.IGNORECASE)
    alternatives = []
    for part in parts:
        if qtype == "NAT":
            m = RANGE_RE.search(part)
            if not m:
                raise ValueError(f"unparseable NAT key {raw!r}")
            alternatives.append([float(m.group(1)), float(m.group(2))])
        else:
            letters = sorted(set(re.findall(r"[A-E]", part.upper())))
            if not letters:
                raise ValueError(f"unparseable choice key {raw!r}")
            alternatives.append(letters)
    return {"mta": False, "alternatives": alternatives}


def pair_questions(site_qs: list[dict], official: list[dict]) -> list[tuple[dict, dict]] | str:
    site_ga = [q for q in site_qs if q["section"] == "General Aptitude"]
    site_cs = [q for q in site_qs if q["section"] == "Technical"]
    off_ga = sorted((r for r in official if r["section"] == "GA"), key=lambda r: r["number"])
    off_cs = sorted((r for r in official if r["section"] == "CS"), key=lambda r: r["number"])
    if len(site_ga) != len(off_ga) or len(site_cs) != len(off_cs):
        return f"section sizes differ: site GA/CS {len(site_ga)}/{len(site_cs)}, official {len(off_ga)}/{len(off_cs)}"
    pairs = list(zip(site_ga, off_ga)) + list(zip(site_cs, off_cs))
    mismatched = [(q["number"], r["number"]) for q, r in pairs if q["type"] != r["type"] or q["marks"] != r["marks"]]
    if mismatched:
        return f"type/marks differ for {len(mismatched)} pairs (site Q, official Q): {mismatched[:6]}"
    return pairs


def compare(question: dict, official_key: dict) -> tuple[str, str]:
    if official_key["mta"]:
        if question.get("marks_to_all"):
            return "match", "marks to all, applied"
        return "mta", "official key: marks to all (question dropped)"
    alts = official_key["alternatives"]
    if question["type"] == "NAT":
        site_alts = [question["nat_range"], *question.get("accepted", [])]
        norm = lambda rs: sorted((round(float(lo), 9), round(float(hi), 9)) for lo, hi in rs)
        if norm(site_alts) == norm(alts):
            return "match", f"site {site_alts} vs official {alts}"
        site = question["nat_range"]
        if any(abs(site[0] - lo) < 1e-9 and abs(site[1] - hi) < 1e-9 for lo, hi in alts):
            return "partial", f"site {site_alts} vs official {alts}"
        overlap = any(site[0] <= hi and lo <= site[1] for lo, hi in alts)
        return ("range_differs" if overlap else "mismatch"), f"site {site_alts} vs official {alts}"
    site_alts = [sorted(question["correct"]), *(sorted(a) for a in question.get("accepted", []))]
    if sorted(site_alts) == sorted(alts):
        return "match", f"site {site_alts} vs official {alts}"
    if sorted(question["correct"]) in alts:
        return "partial", f"site {site_alts} vs official {alts}"
    return "mismatch", f"site {site_alts} vs official {alts}"


def main() -> int:
    rows_out = []
    summary = {}
    for pdf_path in sorted(KEYS_DIR.glob("*.pdf")):
        pid = pdf_path.stem
        paper_path = PAPERS_DIR / f"{pid}.json"
        if not paper_path.exists():
            print(f"{pid}: no matching paper, skipped")
            continue
        official = parse_official(pdf_path)
        if len(official) == 0:
            print(f"{pid}: no text rows in the PDF (scanned image?), skipped")
            summary[pid] = "unreadable"
            continue
        paper = json.loads(paper_path.read_text())
        pairs = pair_questions(paper["questions"], official)
        if isinstance(pairs, str):
            print(f"{pid}: misaligned, skipped ({pairs})")
            summary[pid] = f"misaligned: {pairs}"
            continue
        counts: dict[str, int] = {}
        for question, row in sorted(pairs, key=lambda p: p[0]["number"]):
            verdict, detail = compare(question, parse_key(row["type"], row["key"]))
            counts[verdict] = counts.get(verdict, 0) + 1
            rows_out.append({"question_id": question["id"], "official_number": row["number"], "type": question["type"],
                             "official_key": row["key"], "verdict": verdict, "detail": detail})
        summary[pid] = counts
        print(f"{pid}: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))

    issues = [r for r in rows_out if r["verdict"] != "match"]
    if issues:
        print("\nNeeds attention (site key differs from, or is narrower than, the official key):")
        for r in issues:
            print(f"  {r['question_id']:<13} (official Q{r['official_number']}) {r['type']}  {r['verdict']:<13} {r['detail']}")

    REPORTS_DIR.mkdir(exist_ok=True)
    out = REPORTS_DIR / "official_key_check.json"
    out.write_text(json.dumps({"summary": summary, "questions": rows_out}, indent=2) + "\n")
    print(f"\nWrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
