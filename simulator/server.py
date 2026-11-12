"""Local server for the simulator: serves the project, saves attempts, keeps reports in step.

Usage:
    python3 simulator/server.py [--port 8765]

Then open http://localhost:8765/simulator/exam.html.

It behaves like `python3 -m http.server` for the project root, plus two endpoints:

    POST /api/results      body: the attempt JSON from exam.html
                           writes results/<attempt_id>.json, then syncs (below)
    GET  /api/performance  syncs, then returns the tools/performance.py report with
                           links to each attempt's result file and review page
                           (shown on the start page of exam.html)

A sync brings the other two folders in step with results/:

    reports/performance.json   rewritten when its numbers have changed
    reviews/<attempt>.html     written by tools/reviewer.py (site solutions only, no
                               Claude calls) when missing or older than the result;
                               each question links to its notes in "Study Materials/"

So a result file dropped into results/ by hand is picked up on the next page load.

The server only listens on 127.0.0.1. Both endpoints refuse requests that do not
come from the simulator page itself, so another website open in the browser cannot
read or write files here.
"""
from __future__ import annotations

import argparse
import functools
import http.server
import json
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import threading
import urllib.parse

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
import performance  # noqa: E402  (tools/performance.py)

RESULTS_DIR = ROOT / "results"
REPORTS_DIR = ROOT / "reports"
REVIEWS_DIR = ROOT / "reviews"
REVIEWER = ROOT / "tools" / "reviewer.py"
# The reviewer needs the project's packages (bs4), which live in the venv.
VENV_PYTHON = ROOT / ".venv" / "bin" / "python"
MAX_BODY_BYTES = 2_000_000  # a 65-question attempt is about 15 kB
REVIEW_TIMEOUT_SEC = 60

# '<paper_id>_<yyyymmddThhmmssZ>', as in schema/results.schema.json. The id becomes
# the file name, so nothing outside this pattern is accepted.
ATTEMPT_ID = re.compile(r"(\d{4}(-S[1-9])?|[a-z][a-z-]*-\d{2})_\d{8}T\d{6}Z")
REQUIRED_KEYS = ("attempt_id", "paper_id", "started_at", "ended_at", "score", "answers")

SYNC_LOCK = threading.Lock()  # one sync at a time: requests are handled on threads


def write_atomic(target: pathlib.Path, text: str) -> None:
    """Write to a temp file first so a crash never leaves half a file."""
    target.parent.mkdir(exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=target.parent, prefix=".saving-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            handle.write(text)
        os.chmod(tmp, 0o644)
        os.replace(tmp, target)
    except BaseException:
        pathlib.Path(tmp).unlink(missing_ok=True)
        raise


def write_report(report: dict) -> None:
    """Rewrite reports/performance.json unless only its timestamp would change."""
    target = REPORTS_DIR / "performance.json"
    try:
        current = json.loads(target.read_text())
    except (OSError, ValueError):
        current = None
    if isinstance(current, dict) and {**current, "generated_at": None} == {**report, "generated_at": None}:
        return
    write_atomic(target, json.dumps(report, indent=2) + "\n")


def write_review(result: pathlib.Path, review: pathlib.Path) -> str | None:
    """Run tools/reviewer.py for one attempt. Returns what went wrong, or None."""
    python = str(VENV_PYTHON) if VENV_PYTHON.exists() else sys.executable
    try:
        done = subprocess.run(
            [python, str(REVIEWER), str(result), "--out", str(review)],
            cwd=ROOT, capture_output=True, text=True, timeout=REVIEW_TIMEOUT_SEC,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        return str(error)
    if done.returncode != 0:
        lines = (done.stderr or done.stdout).strip().splitlines()
        return lines[-1] if lines else f"reviewer exited with status {done.returncode}"
    return None


def sync() -> dict:
    """Bring reports/ and reviews/ in step with results/; return the report for the page.

    The returned report has, for each attempt in "trend", "result_url" and either
    "review_url" or "review_error". Those are not written to reports/performance.json.
    """
    with SYNC_LOCK:
        report = performance.build_report(RESULTS_DIR)
        try:
            write_report(report)
        except OSError as error:
            report["report_error"] = f"could not write reports/performance.json: {error}"
        for entry in report["trend"]:
            result = RESULTS_DIR / entry["file"]
            review = REVIEWS_DIR / f"{result.stem}.html"
            entry["result_url"] = "/results/" + urllib.parse.quote(result.name)
            error = None
            if not review.exists() or review.stat().st_mtime < result.stat().st_mtime:
                error = write_review(result, review)
            if error:
                entry["review_error"] = error
            else:
                entry["review_url"] = "/reviews/" + urllib.parse.quote(review.name)
        return report


class Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        # Always revalidate, so an edited exam.html or paper is picked up on reload.
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()

    def reply(self, status: int, payload: dict) -> None:
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def local_names(self) -> set[str]:
        port = self.server.server_address[1]
        return {f"localhost:{port}", f"127.0.0.1:{port}"}

    def from_simulator(self) -> bool:
        """Same host and, when the browser says, same origin."""
        origin = self.headers.get("Origin")
        return self.headers.get("Host") in self.local_names() and (
            origin is None or origin.removeprefix("http://") in self.local_names()
        )

    def do_GET(self) -> None:
        if self.path.split("?", 1)[0] != "/api/performance":
            super().do_GET()
            return
        if not self.from_simulator():
            self.reply(403, {"error": "requests are accepted from the simulator page only"})
            return
        try:
            report = sync()
        except Exception as error:  # one malformed attempt file must not kill the server
            self.reply(500, {"error": f"could not read results/: {error!r}"})
            return
        self.reply(200, report)

    def do_POST(self) -> None:
        if self.path != "/api/results":
            self.reply(404, {"error": "unknown endpoint"})
            return
        if not self.from_simulator():
            self.reply(403, {"error": "requests are accepted from the simulator page only"})
            return
        if self.headers.get_content_type() != "application/json":
            self.reply(415, {"error": "Content-Type must be application/json"})
            return
        try:
            length = int(self.headers.get("Content-Length", ""))
        except ValueError:
            self.reply(411, {"error": "Content-Length required"})
            return
        if not 0 < length <= MAX_BODY_BYTES:
            self.reply(413, {"error": "body is empty or too large"})
            return

        try:
            attempt = json.loads(self.rfile.read(length))
        except (ValueError, UnicodeDecodeError):
            self.reply(400, {"error": "body is not valid JSON"})
            return
        if not isinstance(attempt, dict) or any(key not in attempt for key in REQUIRED_KEYS):
            self.reply(400, {"error": f"attempt must have {', '.join(REQUIRED_KEYS)}"})
            return
        attempt_id = attempt["attempt_id"]
        if not isinstance(attempt_id, str) or not ATTEMPT_ID.fullmatch(attempt_id):
            self.reply(400, {"error": "attempt_id is not '<paper_id>_<yyyymmddThhmmssZ>'"})
            return

        target = RESULTS_DIR / f"{attempt_id}.json"
        try:
            write_atomic(target, json.dumps(attempt, indent=2, ensure_ascii=False) + "\n")
        except OSError as error:
            self.reply(500, {"error": f"could not write the file: {error}"})
            return

        # The attempt is safe on disk. Whatever happens to the report and the review
        # is reported next to it, never instead of it.
        saved = {"saved": f"results/{target.name}"}
        try:
            report = sync()
        except Exception as error:
            saved["sync_error"] = f"performance and review were not updated: {error!r}"
        else:
            entry = next((e for e in report["trend"] if e["file"] == target.name), {})
            saved["performance_updated"] = "report_error" not in report
            for key in ("review_url", "review_error"):
                if key in entry:
                    saved[key] = entry[key]
        self.reply(201, saved)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    handler = functools.partial(Handler, directory=str(ROOT))
    with http.server.ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        print(f"Serving {ROOT} at http://localhost:{args.port}/simulator/exam.html")
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
