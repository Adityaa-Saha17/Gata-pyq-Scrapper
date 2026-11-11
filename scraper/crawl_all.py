"""Full crawl of every GATE CSE paper listed on practicepaper.in.

Usage:
    python scraper/crawl_all.py [--force] [--only <paper_id> ...]

Flags:
    --force             Re-scrape even if papers/<paper_id>.json already exists.
    --only <paper_id>   Restrict to the listed paper_ids (may be given multiple
                        times). Useful for retrying a few papers after fixing
                        topic aliases.

Behaviour:
    - Reuses cache/html/index.html if present; otherwise fetches it.
    - Enumerates every /gate-cse/gate-cse-YYYY(-set-N)? link.
    - For each paper, delegates to scrape_paper.scrape(). Per-paper exceptions
      are caught, logged and summarised; the crawl continues.
    - Prints a final summary (done, skipped, failed).
"""

from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import time

import bs4
import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scraper"))

from scrape_paper import (  # noqa: E402
    CACHE_DIR,
    PAPERS_DIR,
    PATH_PREFIX,
    REQUEST_DELAY_SEC,
    SITE_BASE,
    USER_AGENT,
    scrape,
)

INDEX_URL = f"{SITE_BASE}{PATH_PREFIX}gate-cse-year-wise-questions"
INDEX_CACHE = CACHE_DIR / "index.html"

SLUG_RE = re.compile(r"^gate-cse-(\d{4})(?:-set-([1-9]))?$")


def fetch_index() -> str:
    if INDEX_CACHE.exists():
        return INDEX_CACHE.read_text(encoding="utf-8")
    print(f"Fetching index: {INDEX_URL}", flush=True)
    time.sleep(REQUEST_DELAY_SEC)
    resp = requests.get(INDEX_URL, headers={"User-Agent": USER_AGENT}, timeout=30)
    resp.raise_for_status()
    INDEX_CACHE.parent.mkdir(parents=True, exist_ok=True)
    INDEX_CACHE.write_text(resp.text, encoding="utf-8")
    return resp.text


def slug_to_paper_id(slug: str) -> str | None:
    m = SLUG_RE.match(slug)
    if not m:
        return None
    year, set_num = m.group(1), m.group(2)
    return f"{year}-S{set_num}" if set_num else year


def papers_from_index(html: str) -> list[tuple[str, str]]:
    soup = bs4.BeautifulSoup(html, "lxml")
    seen: set[str] = set()
    out: list[tuple[str, str]] = []
    for a in soup.find_all("a", href=True):
        href = a["href"].rstrip("/")
        m = re.search(r"/gate-cse/(gate-cse-\d{4}(?:-set-\d+)?)$", href)
        if not m:
            continue
        slug = m.group(1)
        if slug in seen:
            continue
        seen.add(slug)
        pid = slug_to_paper_id(slug)
        if pid is None:
            continue
        out.append((slug, pid))

    def sort_key(entry: tuple[str, str]) -> tuple[int, int]:
        pid = entry[1]
        year = int(pid[:4])
        set_num = int(pid.split("-S")[1]) if "-S" in pid else 0
        return (year, set_num)

    out.sort(key=sort_key, reverse=True)
    return out


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--only", nargs="+", default=None)
    args = parser.parse_args(argv[1:])

    PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    index_html = fetch_index()
    papers = papers_from_index(index_html)
    print(f"Index has {len(papers)} papers", flush=True)

    only_set = set(args.only) if args.only else None

    done: list[tuple[str, int]] = []
    skipped: list[str] = []
    failed: list[tuple[str, str]] = []

    for slug, pid in papers:
        if only_set and pid not in only_set:
            continue
        out_path = PAPERS_DIR / f"{pid}.json"
        if out_path.exists() and not args.force:
            skipped.append(pid)
            print(f"[skip] {pid}: already scraped", flush=True)
            continue
        print(f"[work] {pid} ({slug})", flush=True)
        try:
            paper = scrape(slug, pid)
            out_path.write_text(
                json.dumps(paper, ensure_ascii=False, indent=2) + "\n"
            )
            done.append((pid, len(paper["questions"])))
            print(
                f"[done] {pid}: {len(paper['questions'])} questions, "
                f"{paper['total_marks']} marks",
                flush=True,
            )
        except Exception as e:  # noqa: BLE001
            failed.append((pid, f"{type(e).__name__}: {e}"))
            print(f"[FAIL] {pid}: {type(e).__name__}: {e}", flush=True)

    print("\n=========== Summary ===========")
    print(f"done:    {len(done)}")
    for pid, n in done:
        print(f"  {pid:<10}  {n} questions")
    print(f"skipped: {len(skipped)}")
    if skipped:
        print(f"  {', '.join(skipped)}")
    print(f"failed:  {len(failed)}")
    for pid, err in failed:
        print(f"  {pid:<10}  {err}")
    return 0 if not failed else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
