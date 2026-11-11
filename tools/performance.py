"""Performance tracker: combine every attempt in results/ into per-topic stats.

Usage:
    python tools/performance.py [--results-dir DIR] [--min-attempts N]

Reads:
    papers/*.json            question metadata (topic, subtopic, type, marks)
    results/*.json           one file per attempt (from simulator/exam.html)

Attempts at topic mocks (mocks/*.json) count too: their questions keep the
original ids, so they join on papers/ like any full paper.

Writes:
    reports/performance.json  the same numbers as the printed tables

Accuracy is correct / attempted. Average time uses attempted questions only,
since time spent on a question you skipped says little about speed.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import sys
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "papers"
RESULTS_DIR = ROOT / "results"
REPORTS_DIR = ROOT / "reports"


def load_questions() -> dict[str, dict]:
    questions: dict[str, dict] = {}
    for path in sorted(PAPERS_DIR.glob("*.json")):
        paper = json.loads(path.read_text())
        for q in paper["questions"]:
            questions[q["id"]] = q
    return questions


def load_attempts(results_dir: pathlib.Path) -> list[dict]:
    attempts = []
    for path in sorted(results_dir.glob("*.json")):
        try:
            data = json.loads(path.read_text())
        except json.JSONDecodeError as e:
            print(f"warning: skipping {path.name}: invalid JSON ({e})", file=sys.stderr)
            continue
        if not isinstance(data, dict) or "answers" not in data or "paper_id" not in data:
            print(f"warning: skipping {path.name}: not an attempt file", file=sys.stderr)
            continue
        attempts.append(data)
    attempts.sort(key=lambda a: a["started_at"])
    return attempts


class Bucket:
    def __init__(self) -> None:
        self.total = 0
        self.attempted = 0
        self.correct = 0
        self.wrong = 0
        self.marks_earned = 0.0
        self.marks_possible = 0.0
        self.time_attempted_sec = 0

    def add(self, question: dict, answer: dict) -> None:
        self.total += 1
        self.marks_possible += question["marks"]
        self.marks_earned += answer["marks_earned"]
        # A dropped question ("marks to all") left blank earns marks but isn't an attempt.
        if answer["is_correct"] is None or answer["response"] is None:
            return
        self.attempted += 1
        self.time_attempted_sec += answer["time_spent_sec"]
        if answer["is_correct"]:
            self.correct += 1
        else:
            self.wrong += 1

    def summary(self) -> dict:
        return {
            "questions": self.total,
            "attempted": self.attempted,
            "correct": self.correct,
            "wrong": self.wrong,
            "unattempted": self.total - self.attempted,
            "accuracy": round(self.correct / self.attempted, 3) if self.attempted else None,
            "avg_time_sec": round(self.time_attempted_sec / self.attempted, 1) if self.attempted else None,
            "marks_earned": round(self.marks_earned, 2),
            "marks_possible": round(self.marks_possible, 2),
        }


def aggregate(attempts: list[dict], questions: dict[str, dict]) -> dict:
    by_topic: dict[str, Bucket] = defaultdict(Bucket)
    by_subtopic: dict[tuple[str, str], Bucket] = defaultdict(Bucket)
    by_type: dict[str, Bucket] = defaultdict(Bucket)
    by_marks: dict[str, Bucket] = defaultdict(Bucket)
    by_section: dict[str, Bucket] = defaultdict(Bucket)
    overall = Bucket()
    trend = []
    missing = 0

    for attempt in attempts:
        attempt_bucket = Bucket()
        for answer in attempt["answers"]:
            question = questions.get(answer["question_id"])
            if question is None:
                missing += 1
                continue
            for bucket in (
                by_topic[question["topic"]],
                by_subtopic[(question["topic"], question["subtopic"] or "(none)")],
                by_type[question["type"]],
                by_marks[f"{question['marks']}-mark"],
                by_section[question["section"]],
                overall,
                attempt_bucket,
            ):
                bucket.add(question, answer)
        stats = attempt_bucket.summary()
        trend.append({
            "attempt_id": attempt.get("attempt_id"),
            "paper_id": attempt["paper_id"],
            "date": attempt["started_at"][:10],
            "score": attempt.get("score"),
            "total_marks": attempt.get("total_marks"),
            "general_aptitude": (attempt.get("score_breakdown") or {}).get("general_aptitude"),
            "technical": (attempt.get("score_breakdown") or {}).get("technical"),
            "accuracy": stats["accuracy"],
            "attempted": stats["attempted"],
            "duration_min": round(attempt.get("duration_sec", 0) / 60, 1),
        })

    def table(buckets: dict) -> dict:
        return {key if isinstance(key, str) else " / ".join(key): b.summary() for key, b in buckets.items()}

    return {
        "generated_at": dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z"),
        "attempts": len(attempts),
        "unknown_question_ids": missing,
        "overall": overall.summary(),
        "trend": trend,
        "by_section": table(by_section),
        "by_topic": table(by_topic),
        "by_type": table(by_type),
        "by_marks": table(by_marks),
        "by_subtopic": table(by_subtopic),
    }


def fmt_pct(x: float | None) -> str:
    return "-" if x is None else f"{x * 100:5.1f}%"


def fmt_num(x: float | None) -> str:
    return "-" if x is None else f"{x:.0f}"


def print_table(title: str, rows: dict, sort_by_accuracy: bool = False) -> None:
    print(f"\n{title}")
    header = f"  {'':<42}{'Qs':>5}{'Att':>5}{'Right':>6}{'Wrong':>6}{'Acc':>8}{'Avg s':>7}{'Marks':>14}"
    print(header)
    print("  " + "-" * (len(header) - 2))
    items = list(rows.items())
    if sort_by_accuracy:
        items.sort(key=lambda kv: (kv[1]["accuracy"] is None, kv[1]["accuracy"] or 0))
    else:
        items.sort(key=lambda kv: kv[0])
    for name, s in items:
        marks = f"{s['marks_earned']:.2f}/{s['marks_possible']:.0f}"
        print(
            f"  {name[:42]:<42}{s['questions']:>5}{s['attempted']:>5}{s['correct']:>6}{s['wrong']:>6}"
            f"{fmt_pct(s['accuracy']):>8}{fmt_num(s['avg_time_sec']):>7}{marks:>14}"
        )


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--results-dir", type=pathlib.Path, default=RESULTS_DIR)
    parser.add_argument("--min-attempts", type=int, default=3,
                        help="minimum attempted questions before a subtopic counts as weak (default 3)")
    args = parser.parse_args(argv[1:])

    questions = load_questions()
    attempts = load_attempts(args.results_dir)
    if not attempts:
        print(f"No attempt files found in {args.results_dir}. Take a test in simulator/exam.html first.")
        return 1

    report = aggregate(attempts, questions)

    print(f"Attempts: {report['attempts']}")
    if report["unknown_question_ids"]:
        print(f"warning: {report['unknown_question_ids']} answers reference questions not in papers/")
    o = report["overall"]
    print(f"Overall: {o['correct']}/{o['attempted']} attempted correct ({fmt_pct(o['accuracy']).strip()}), "
          f"{o['marks_earned']:.2f}/{o['marks_possible']:.0f} marks, avg {fmt_num(o['avg_time_sec'])}s per attempted question")

    print("\nScore trend")
    for t in report["trend"]:
        print(f"  {t['date']}  {t['paper_id']:<28}  {t['score']:>6}/{t['total_marks']}  "
              f"GA {t['general_aptitude']}  Tech {t['technical']}  acc {fmt_pct(t['accuracy']).strip()}  "
              f"{t['attempted']} attempted in {t['duration_min']} min")

    print_table("By section", report["by_section"])
    print_table("By topic (weakest first)", report["by_topic"], sort_by_accuracy=True)
    print_table("By question type", report["by_type"])
    print_table("By marks", report["by_marks"])

    weak = {k: v for k, v in report["by_subtopic"].items()
            if v["attempted"] >= args.min_attempts and v["accuracy"] is not None}
    weakest = dict(sorted(weak.items(), key=lambda kv: kv[1]["accuracy"])[:10])
    report["weakest_subtopics"] = weakest
    if weakest:
        print_table(f"Weakest subtopics (>= {args.min_attempts} attempted)", weakest, sort_by_accuracy=True)
    else:
        print(f"\nNo subtopic has {args.min_attempts}+ attempted questions yet; weak-subtopic list needs more attempts.")

    REPORTS_DIR.mkdir(exist_ok=True)
    out = REPORTS_DIR / "performance.json"
    out.write_text(json.dumps(report, indent=2) + "\n")
    print(f"\nWrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
