"""Build topic-wise mock tests from the scraped papers.

Usage:
    python tools/make_topic_mocks.py [--size 30] [--minutes 90] [--seed 2026] [--dry-run]

Reads:
    papers/*.json                 every scraped question

Writes:
    mocks/<topic-slug>-<nn>.json  one mock per file, same question shape as a paper
    mocks/index.json              the list the simulator shows on its start page

How the sets are made:
    * Each topic gets as many sets as fit (questions // size). No question is
      used twice within a topic; the oldest leftover questions are left out.
    * Questions are grouped by subtopic, marks and type, then dealt out one at a
      time across the sets, so every set gets its share of every subtopic.
    * Inside a set, 1-mark questions come first and 2-mark questions after, as in
      the real paper. The order within each group is shuffled.
    * A question that refers to "the previous question" stays in the same set as
      that question and directly after it.

Questions keep their original id (for example 2014-S2-Q23), so results from a
topic mock join the performance tracker and reviewer exactly like a full paper.
The same seed always gives the same sets, as long as papers/ has not changed.
Re-run this after editing papers/ or the override files.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import random
import re
import sys
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPERS_DIR = ROOT / "papers"
MOCKS_DIR = ROOT / "mocks"
SCHEMA_DIR = ROOT / "schema"

PREVIOUS_RE = re.compile(r"previous\s+question", re.IGNORECASE)


def slugify(topic: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", topic.lower()).strip("-")


def subtopic_key(subtopic: str | None) -> str:
    """Fold spelling variants ('OSI layer', 'Verbal Ability ') into one group."""
    if not subtopic or not subtopic.strip():
        return "(none)"
    key = re.sub(r"\s+", " ", subtopic.strip().lower())
    return {"transactions": "transaction"}.get(key, key)


def load_by_topic() -> dict[str, list[dict]]:
    by_topic: dict[str, list[dict]] = defaultdict(list)
    for path in sorted(PAPERS_DIR.glob("*.json")):
        paper = json.loads(path.read_text())
        for q in paper["questions"]:
            item = dict(q)
            item["source_paper_id"] = paper["paper_id"]
            item["source_number"] = q["number"]
            item["_year"] = paper["year"]
            item["_set"] = paper.get("set") or 0
            by_topic[q["topic"]].append(item)
    return by_topic


def find_links(questions: list[dict]) -> dict[str, str]:
    """Map follower id -> leader id for questions that need the one before them."""
    by_position = {(q["source_paper_id"], q["source_number"]): q for q in questions}
    links = {}
    for q in questions:
        if not PREVIOUS_RE.search(q["question"]):
            continue
        leader = by_position.get((q["source_paper_id"], q["source_number"] - 1))
        if leader is not None:
            links[q["id"]] = leader["id"]
    return links


def deal(questions: list[dict], size: int, rng: random.Random) -> tuple[list[list[dict]], list[dict]]:
    """Split one topic's questions into equal sets. Returns (sets, left_out)."""
    n_sets = len(questions) // size
    links = find_links(questions)
    linked_ids = set(links) | set(links.values())

    # Leave out the oldest questions, but never half of a linked pair.
    oldest_first = sorted(questions, key=lambda q: (q["_year"], q["_set"], q["source_number"]))
    spare = len(questions) - n_sets * size
    left_out = [q for q in oldest_first if q["id"] not in linked_ids][:spare]
    left_out_ids = {q["id"] for q in left_out}
    pool = [q for q in oldest_first if q["id"] not in left_out_ids]

    rng.shuffle(pool)
    pool.sort(key=lambda q: (subtopic_key(q["subtopic"]), q["marks"], q["type"]))
    sets: list[list[dict]] = [[] for _ in range(n_sets)]
    for i, q in enumerate(pool):
        sets[i % n_sets].append(q)

    # Bring each follower into its leader's set by swapping it with a similar question.
    where = {q["id"]: s for s, group in enumerate(sets) for q in group}
    for follower_id, leader_id in sorted(links.items()):
        src, dst = where[follower_id], where[leader_id]
        if src == dst:
            continue
        follower = next(q for q in sets[src] if q["id"] == follower_id)
        candidates = [q for q in sets[dst] if q["id"] not in linked_ids and q["marks"] == follower["marks"]]
        candidates.sort(key=lambda q: (subtopic_key(q["subtopic"]) != subtopic_key(follower["subtopic"]),
                                       q["type"] != follower["type"], q["id"]))
        if not candidates:
            raise SystemExit(f"cannot keep {follower_id} with {leader_id}: no question to swap")
        swap = candidates[0]
        sets[src][sets[src].index(follower)] = swap
        sets[dst][sets[dst].index(swap)] = follower
        where[follower_id], where[swap["id"]] = dst, src

    # Exam order: 1-mark first, then 2-mark, shuffled; followers right after leaders.
    for group in sets:
        rng.shuffle(group)
        group.sort(key=lambda q: q["marks"])
        for follower_id, leader_id in links.items():
            follower = next((q for q in group if q["id"] == follower_id), None)
            if follower is None:
                continue
            group.remove(follower)
            leader_at = next(i for i, q in enumerate(group) if q["id"] == leader_id)
            group.insert(leader_at + 1, follower)
    return sets, left_out


def build_mock(topic: str, set_no: int, group: list[dict], minutes: int, seed: int, stamp: str) -> dict:
    questions = []
    for position, q in enumerate(group, start=1):
        item = {k: v for k, v in q.items() if not k.startswith("_")}
        item["number"] = position
        questions.append(item)
    return {
        "paper_id": f"{slugify(topic)}-{set_no:02d}",
        "paper": f"{topic}: Topic Mock {set_no}",
        "kind": "topic_mock",
        "topic": topic,
        "set": set_no,
        "duration_min": minutes,
        "total_marks": sum(q["marks"] for q in questions),
        "seed": seed,
        "generated_at": stamp,
        "questions": questions,
    }


def make_validator():
    """Validator for mock files, or None when jsonschema is not installed."""
    try:
        from jsonschema import Draft202012Validator
        from referencing import Registry, Resource
    except ImportError:
        return None
    paper_schema = json.loads((SCHEMA_DIR / "paper.schema.json").read_text())
    mock_schema = json.loads((SCHEMA_DIR / "mock.schema.json").read_text())
    registry = Registry().with_resources([
        (paper_schema["$id"], Resource.from_contents(paper_schema)),
        (mock_schema["$id"], Resource.from_contents(mock_schema)),
    ])
    return Draft202012Validator(mock_schema, registry=registry)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=30, help="questions per mock (default 30)")
    parser.add_argument("--minutes", type=int, default=90, help="time limit per mock (default 90)")
    parser.add_argument("--seed", type=int, default=2026, help="shuffle seed; same seed gives the same sets")
    parser.add_argument("--dry-run", action="store_true", help="print the plan without writing files")
    args = parser.parse_args(argv[1:])

    by_topic = load_by_topic()
    canonical = json.loads((SCHEMA_DIR / "topics.json").read_text())["canonical_topics"]
    stamp = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    validator = make_validator()
    if validator is None:
        print("warning: jsonschema not installed, mocks are not schema-checked", file=sys.stderr)

    mocks: list[dict] = []
    index_topics = []
    print(f"{'Topic':<40}{'Qs':>5}{'Sets':>6}{'Left out':>10}{'Marks':>12}{'Subtopics':>11}")
    for topic in canonical:
        questions = by_topic.get(topic, [])
        if len(questions) < args.size:
            print(f"{topic:<40}{len(questions):>5}{'-':>6}{'(too few)':>10}")
            continue
        rng = random.Random(f"{args.seed}:{topic}")
        sets, left_out = deal(questions, args.size, rng)
        topic_mocks = [build_mock(topic, n, group, args.minutes, args.seed, stamp)
                       for n, group in enumerate(sets, start=1)]
        marks = [m["total_marks"] for m in topic_mocks]
        spread = [len({subtopic_key(q["subtopic"]) for q in m["questions"]}) for m in topic_mocks]
        print(f"{topic:<40}{len(questions):>5}{len(sets):>6}{len(left_out):>10}"
              f"{f'{min(marks)}-{max(marks)}':>12}{f'{min(spread)}-{max(spread)}':>11}")
        mocks.extend(topic_mocks)
        index_topics.append({
            "topic": topic,
            "slug": slugify(topic),
            "sets": [{
                "paper_id": m["paper_id"],
                "set": m["set"],
                "questions": len(m["questions"]),
                "total_marks": m["total_marks"],
            } for m in topic_mocks],
        })

    # Checks: right size, no question twice within a topic, schema-valid.
    problems = []
    seen: dict[str, Counter] = defaultdict(Counter)
    for m in mocks:
        if len(m["questions"]) != args.size:
            problems.append(f"{m['paper_id']}: {len(m['questions'])} questions")
        for q in m["questions"]:
            seen[m["topic"]][q["id"]] += 1
            if q["topic"] != m["topic"]:
                problems.append(f"{m['paper_id']}: {q['id']} is {q['topic']}")
        if validator is not None:
            for error in validator.iter_errors(m):
                problems.append(f"{m['paper_id']}: {error.message[:160]}")
    for topic, counts in seen.items():
        for qid, n in counts.items():
            if n > 1:
                problems.append(f"{topic}: {qid} used {n} times")
    if problems:
        print("\nProblems found, nothing written:", file=sys.stderr)
        for line in problems[:30]:
            print(f"  {line}", file=sys.stderr)
        return 1

    print(f"\n{len(mocks)} mocks, {args.size} questions and {args.minutes} minutes each.")
    if args.dry_run:
        print("Dry run: no files written.")
        return 0

    MOCKS_DIR.mkdir(exist_ok=True)
    for old in MOCKS_DIR.glob("*.json"):
        old.unlink()
    for m in mocks:
        (MOCKS_DIR / f"{m['paper_id']}.json").write_text(json.dumps(m, indent=2, ensure_ascii=False) + "\n")
    index = {
        "generated_at": stamp,
        "seed": args.seed,
        "questions_per_mock": args.size,
        "duration_min": args.minutes,
        "topics": index_topics,
    }
    (MOCKS_DIR / "index.json").write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote {len(mocks)} files and index.json to {MOCKS_DIR.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
