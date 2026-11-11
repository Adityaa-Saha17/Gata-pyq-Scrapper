"""Download referenced images for every scraped paper.

Usage:
    python scraper/download_images.py [--only <paper_id> ...]

Reads papers/*.json, pulls each URL in question["images"] into
cache/images/<paper_id>/<basename>. Skips files that already exist.
Sleeps 1 second between network downloads.

Paper JSON is not rewritten; the simulator maps '/wp-content/...' paths to
the local cache at render time.
"""

from __future__ import annotations

import argparse
import json
import pathlib
import sys
import time
import urllib.parse

import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scraper"))

from scrape_paper import USER_AGENT  # noqa: E402

PAPERS_DIR = ROOT / "papers"
IMAGES_DIR = ROOT / "cache" / "images"
IMG_DELAY_SEC = 1


def download_one(url: str, dest: pathlib.Path) -> int:
    resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    resp.raise_for_status()
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(resp.content)
    return len(resp.content)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", nargs="+", default=None)
    args = parser.parse_args(argv[1:])

    only_set = set(args.only) if args.only else None

    papers = sorted(PAPERS_DIR.glob("*.json"))
    if not papers:
        print("No papers found in papers/.")
        return 1

    total_downloaded = 0
    total_skipped = 0
    total_failed = 0

    for p in papers:
        paper = json.loads(p.read_text())
        pid = paper["paper_id"]
        if only_set and pid not in only_set:
            continue
        paper_img_dir = IMAGES_DIR / pid

        urls: list[str] = []
        for q in paper["questions"]:
            for u in q.get("images", []):
                if u not in urls:
                    urls.append(u)
        if not urls:
            continue

        print(f"[{pid}] {len(urls)} image(s)")
        for url in urls:
            name = pathlib.Path(urllib.parse.urlparse(url).path).name
            if not name:
                print(f"  SKIP (no filename in URL): {url}")
                total_failed += 1
                continue
            dest = paper_img_dir / name
            if dest.exists():
                total_skipped += 1
                continue
            time.sleep(IMG_DELAY_SEC)
            try:
                nbytes = download_one(url, dest)
                total_downloaded += 1
                print(f"  got {dest.relative_to(ROOT)} ({nbytes} bytes)")
            except Exception as e:  # noqa: BLE001
                total_failed += 1
                print(f"  FAIL {url}: {type(e).__name__}: {e}")

    print(
        f"\nDone: downloaded={total_downloaded}, "
        f"cached_already={total_skipped}, failed={total_failed}"
    )
    return 0 if total_failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
