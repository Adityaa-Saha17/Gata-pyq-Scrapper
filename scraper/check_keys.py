"""Offline answer-key consistency check.

Usage:
    python scraper/check_keys.py [--only <paper_id> ...] [--show N]

Many site solutions end with a line like "Answer: 612.06" or "Answer: Only I is
correct". This compares that stated answer with the structured key
(correct / nat_range) for every question, without any network access:

    agree         the solution's stated answer matches the key
    disagree      it clearly points at a different option or number (check by hand)
    close         NAT number outside the range but within 2% (usually rounding)
    multiple      the solution says several values are accepted but the key range excludes some
    undetermined  no answer line, or the text could not be matched to one option

Writes reports/key_check.json.
"""

from __future__ import annotations

import argparse
import html
import json
import pathlib
import re
import sys
from collections import Counter
from difflib import SequenceMatcher

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "papers"
REPORTS_DIR = ROOT / "reports"

ANSWER_RE = re.compile(
    r"(?:answer|correct\s+(?:answer|options?)|options?)\s*(?:is|are)?\s*[:\-–]\s*(.+)$",
    re.IGNORECASE,
)
LETTERS_ONLY_RE = re.compile(r"^(?:options?\s*)?\(?([A-E])\)?(?:\s*(?:,|and|&)\s*\(?([A-E])\)?)*\.?$", re.IGNORECASE)
NUMBER_RE = re.compile(r"-?\d+(?:\.\d+)?")


def plain(text: str) -> str:
    text = re.sub(r"<a [^>]*>.*?</a>", "", text, flags=re.S | re.I)
    text = re.sub(r"\[/?latex\]", "", text)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"<[^>]+>", "", text)
    return html.unescape(text)


def norm(text: str) -> str:
    text = plain(text).lower()
    text = re.sub(r"\\(?:,|;|!|\s|quad|qquad)", "", text)
    text = re.sub(r"\\(?:text|mathrm|textbf|mathbf|left|right)\s*", "", text)
    text = re.sub(r"[\s{}()$]", "", text)
    return text.rstrip(".")


def as_number(text: str) -> float | None:
    t = norm(text).rstrip("%")
    return float(t) if re.fullmatch(r"-?\d+(?:\.\d+)?", t) else None


def best_option(options: dict[str, str], stated: str) -> tuple[str | None, str]:
    """Return the single option the stated text refers to, or None if unclear."""
    target_num = as_number(stated)
    if target_num is not None:
        hits = [k for k, v in options.items() if as_number(v) is not None and abs(as_number(v) - target_num) < 1e-9]
        return (hits[0], "numeric match") if len(hits) == 1 else (None, "numeric answer matches no single option")
    target = norm(stated)
    if not target:
        return None, "empty answer text"
    scored = sorted(((SequenceMatcher(None, target, norm(v)).ratio(), k) for k, v in options.items()), reverse=True)
    (best, letter), (second, _) = scored[0], scored[1]
    if best >= 0.8 and best - second >= 0.1:
        return letter, f"closest option {letter} ({best:.2f})"
    return None, f"no clear option match (best {best:.2f}, next {second:.2f})"


def stated_answer(explanation: str | None) -> str | None:
    if not explanation:
        return None
    lines = [ln.strip() for ln in plain(explanation).splitlines() if ln.strip()]
    for line in reversed(lines[-4:]):
        m = ANSWER_RE.search(line)
        if m:
            return m.group(1).strip()
    return None


def check_choice(question: dict, stated: str) -> tuple[str, str]:
    key = sorted(question["correct"])
    m = LETTERS_ONLY_RE.match(stated.strip())
    if m:
        letters = sorted(set(re.findall(r"[A-E]", stated.upper().replace("OPTION", ""))))
        return ("agree" if letters == key else "disagree", f"letters {letters}")
    if question["type"] == "MCQ":
        letter, detail = best_option(question["options"], stated)
        if letter is None:
            return "undetermined", detail
        return ("agree" if [letter] == key else "disagree", detail)

    parts = [p for p in re.split(r"\s*(?:,|;|\band\b|&)\s*", stated) if p.strip()]
    letters = []
    for part in parts:
        letter, detail = best_option(question["options"], part)
        if letter is None:
            return "undetermined", f"MSQ part {part[:30]!r}: {detail}"
        letters.append(letter)
    letters = sorted(set(letters))
    return ("agree" if letters == key else "disagree", f"parts match options {letters}")


def check_nat(question: dict, stated: str) -> tuple[str, str]:
    numbers = NUMBER_RE.findall(stated.replace(",", ""))
    if not numbers:
        return "undetermined", "no number in answer text"
    lo, hi = question["nat_range"]
    # Alternative ranges from schema/key_overrides.json also count as correct.
    ranges = [question["nat_range"], *question.get("accepted", [])]

    def in_key(x: float) -> bool:
        return any(a - 1e-9 <= x <= b + 1e-9 for a, b in ranges)

    if re.search(r"\bor\b|both|either", stated, re.IGNORECASE) and len(set(numbers)) > 1:
        outside = [n for n in numbers if not in_key(float(n))]
        if outside:
            return "multiple", f"solution accepts several values {numbers}; key range [{lo:g}, {hi:g}] excludes {outside}"
    value = float(numbers[0])
    if in_key(value):
        return "agree", f"{value:g} in key {ranges}"
    span = max(abs(lo), abs(hi), 1e-9)
    if min(abs(value - lo), abs(value - hi)) <= 0.02 * span:
        return "close", f"{value:g} vs [{lo:g}, {hi:g}]"
    return "disagree", f"{value:g} vs [{lo:g}, {hi:g}]"


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", nargs="+")
    parser.add_argument("--show", type=int, default=40, help="max disagreements to print")
    args = parser.parse_args(argv[1:])

    rows = []
    for path in sorted(PAPERS_DIR.glob("*.json")):
        paper = json.loads(path.read_text())
        if args.only and paper["paper_id"] not in args.only:
            continue
        for q in paper["questions"]:
            stated = stated_answer(q["explanation"])
            if stated is None:
                verdict, detail = "undetermined", "no answer line in solution"
            elif q["type"] == "NAT":
                verdict, detail = check_nat(q, stated)
            else:
                verdict, detail = check_choice(q, stated)
            key = q["correct"] if q["type"] != "NAT" else q["nat_range"]
            rows.append({"question_id": q["id"], "paper_id": paper["paper_id"], "type": q["type"],
                         "key": key, "stated": stated, "verdict": verdict, "detail": detail})

    overall = Counter(r["verdict"] for r in rows)
    print(f"Checked {len(rows)} questions: " + ", ".join(f"{k}={overall[k]}" for k in ("agree", "close", "disagree", "multiple", "undetermined")))
    per_paper: dict[str, Counter] = {}
    for r in rows:
        per_paper.setdefault(r["paper_id"], Counter())[r["verdict"]] += 1
    print(f"\n  {'paper':<9}{'agree':>7}{'close':>7}{'disagree':>10}{'undet.':>8}")
    for pid in sorted(per_paper, reverse=True):
        c = per_paper[pid]
        print(f"  {pid:<9}{c['agree']:>7}{c['close']:>7}{c['disagree']:>10}{c['undetermined']:>8}")

    flagged = [r for r in rows if r["verdict"] in ("disagree", "multiple")]
    if flagged:
        print(f"\nFlagged (key vs the solution's own answer line) - check these by hand:")
        for r in flagged[: args.show]:
            stated = (r["stated"] or "")[:70]
            print(f"  {r['question_id']:<13} {r['type']}  key={r['key']}  solution says: {stated!r}  ({r['detail']})")
        if len(flagged) > args.show:
            print(f"  ... {len(flagged) - args.show} more in reports/key_check.json")

    REPORTS_DIR.mkdir(exist_ok=True)
    out = REPORTS_DIR / "key_check.json"
    out.write_text(json.dumps({"summary": dict(overall), "questions": rows}, indent=2, ensure_ascii=False) + "\n")
    print(f"\nWrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
