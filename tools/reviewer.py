"""Review an attempt: what you got wrong, the official answer, and why.

Usage:
    python tools/reviewer.py <results/attempt.json> [--include-correct]
                             [--llm] [--max-llm N] [--show-prompt] [--out PATH]

Without --llm the review uses the site's own worked solutions only (free, offline).

--llm asks Claude (claude-opus-5-5) for a tutor-style explanation of each
wrong or skipped question that also addresses the specific option you picked.
Needs ANTHROPIC_API_KEY (or another Anthropic credential) and costs money per
question; answers are cached in cache/llm/ so re-runs are free.
The official answer key is never changed: Claude is told the key and asked to
explain it. If it believes the key is wrong it says so, and the review shows a
"key dispute" warning for you to check by hand.

--show-prompt prints the request for the first question and exits, without
calling the API.

Output: reviews/<attempt_id>.html (open it in a browser).
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from make_pdf import KATEX, answer_text, find_paper, image_folder, rich  # noqa: E402

REVIEWS_DIR = ROOT / "reviews"
LLM_CACHE_DIR = ROOT / "cache" / "llm"
MODEL = "claude-opus-5-5"

SYSTEM_PROMPT = """You are a GATE Computer Science tutor reviewing one question a student attempted in a mock exam.

The official answer key is authoritative and is given to you. Explain why the official answer is correct, step by step, at the level of a strong final-year CS undergraduate. Keep it focused: the key idea, the working, and the result.

If the student gave an answer, explain the specific mistake that most likely led to it (the misconception, the trap in the question, or the arithmetic slip) and how to avoid it. If the student skipped the question, describe the fastest reliable way to solve it in exam conditions instead.

Write math between [latex] and [/latex] tags, for example [latex]O(n \\log n)[/latex]. Do not use $ delimiters. Plain text otherwise; you may use <b> for emphasis and <br> for line breaks.

If, after working the problem carefully, you believe the official answer key is wrong, set key_check to "disagree" and explain why in key_check_note, but still explain the official answer as given. Otherwise set key_check to "agree" and leave key_check_note empty."""

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "key_check": {"type": "string", "enum": ["agree", "disagree"]},
        "key_check_note": {"type": "string"},
        "explanation": {"type": "string"},
        "mistake": {"type": "string"},
    },
    "required": ["key_check", "key_check_note", "explanation", "mistake"],
    "additionalProperties": False,
}


# ---------------------------------------------------------------- loading

def load_attempt(path: pathlib.Path) -> tuple[dict, dict]:
    attempt = json.loads(path.read_text())
    paper_path = find_paper(attempt["paper_id"])
    if paper_path is None:
        raise SystemExit(f"Paper or topic mock {attempt['paper_id']} not found in papers/ or mocks/")
    return attempt, json.loads(paper_path.read_text())


def build_items(attempt: dict, paper: dict, include_correct: bool) -> list[dict]:
    questions = {q["id"]: q for q in paper["questions"]}
    items = []
    for answer in attempt["answers"]:
        question = questions.get(answer["question_id"])
        if question is None:
            continue
        if answer["is_correct"] is True and not include_correct:
            continue
        status = {True: "correct", False: "wrong", None: "skipped"}[answer["is_correct"]]
        items.append({"question": question, "answer": answer, "status": status})
    order = {"wrong": 0, "skipped": 1, "correct": 2}
    items.sort(key=lambda it: (order[it["status"]], -it["question"]["marks"], it["question"]["number"]))
    return items


# ---------------------------------------------------------------- LLM

def fmt_response(response) -> str:
    if response is None:
        return "(skipped)"
    if isinstance(response, list):
        return ", ".join(response) if response else "(none selected)"
    return str(response)


def build_request(question: dict, answer: dict) -> dict:
    lines = [
        f"Question {question['number']} ({question['type']}, {question['marks']} mark{'s' if question['marks'] > 1 else ''}), "
        f"topic: {question['topic']}" + (f" / {question['subtopic']}" if question["subtopic"] else ""),
        "",
        "Question text (may contain HTML and [latex] tags):",
        question["question"],
    ]
    if question["options"]:
        lines += ["", "Options:"] + [f"({k}) {v}" for k, v in question["options"].items()]
    type_note = {
        "MCQ": "Exactly one option is correct.",
        "MSQ": "One or more options are correct; the student must select exactly the correct set.",
        "NAT": "Numerical answer; any value inside the official range is accepted.",
    }[question["type"]]
    lines += [
        "",
        type_note,
        f"Official answer: {answer_text(question)}",
        f"Student's answer: {fmt_response(answer['response'])}",
    ]
    content: list[dict] = [{"type": "image", "source": {"type": "url", "url": url}} for url in question["images"]]
    content.append({"type": "text", "text": "\n".join(lines)})
    return {
        "model": MODEL,
        "max_tokens": 16000,
        "betas": ["server-side-fallback-2026-07-01"],
        "fallbacks": "default",
        "system": SYSTEM_PROMPT,
        "output_config": {"effort": "high", "format": {"type": "json_schema", "schema": OUTPUT_SCHEMA}},
        "messages": [{"role": "user", "content": content}],
    }


def cache_path(question: dict, answer: dict) -> pathlib.Path:
    key = json.dumps(answer["response"], sort_keys=True)
    digest = hashlib.sha1(key.encode()).hexdigest()[:10]
    return LLM_CACHE_DIR / f"{question['id']}__{digest}.json"


def ask_claude(client, question: dict, answer: dict) -> dict:
    path = cache_path(question, answer)
    if path.exists():
        return json.loads(path.read_text())

    response = client.beta.messages.create(**build_request(question, answer))
    if response.stop_reason == "refusal":
        category = response.stop_details.category if response.stop_details else None
        return {"error": f"Claude declined this question (category: {category})."}
    if response.stop_reason == "max_tokens":
        return {"error": "Claude's answer was cut off at the token limit."}

    text = next((b.text for b in response.content if b.type == "text"), "")
    data = json.loads(text)
    data["model"] = response.model
    data["generated_at"] = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n")
    return data


def run_llm(items: list[dict], max_calls: int) -> None:
    import anthropic

    client = anthropic.Anthropic()
    calls = 0
    for item in items:
        if item["status"] == "correct":
            continue
        question, answer = item["question"], item["answer"]
        if not cache_path(question, answer).exists():
            if calls >= max_calls:
                continue
            calls += 1
        print(f"  Claude: Q{question['number']} ({item['status']})", flush=True)
        try:
            item["llm"] = ask_claude(client, question, answer)
        except anthropic.AuthenticationError:
            print("Anthropic credentials invalid; check ANTHROPIC_API_KEY. Continuing with site solutions only.")
            return
        except TypeError as e:
            # The SDK raises TypeError when no credential source resolves at all.
            if "authentication method" not in str(e):
                raise
            print("No Anthropic credentials found; set ANTHROPIC_API_KEY. Continuing with site solutions only.")
            return
        except anthropic.PermissionDeniedError as e:
            print(f"API key lacks permission ({e.message}). Continuing with site solutions only.")
            return
        except anthropic.RateLimitError:
            print("Rate limited after retries; stopping LLM calls. Re-run later; finished answers are cached.")
            return
        except anthropic.BadRequestError as e:
            item["llm"] = {"error": f"Request rejected: {e.message}"}
        except anthropic.APIStatusError as e:
            print(f"API error {e.status_code}; stopping LLM calls. Re-run later; finished answers are cached.")
            return
        except anthropic.APIConnectionError:
            print("Network error reaching the API; stopping LLM calls. Re-run later; finished answers are cached.")
            return
        except json.JSONDecodeError:
            item["llm"] = {"error": "Claude returned malformed JSON."}
    skipped = sum(1 for it in items if it["status"] != "correct" and "llm" not in it)
    if skipped:
        print(f"  {skipped} question(s) left without a Claude explanation (--max-llm {max_calls}).")


# ---------------------------------------------------------------- HTML

def option_rows(question: dict, answer: dict, pid: str) -> str:
    if not question["options"]:
        return (f'<p class="nat">Your answer: <b>{html.escape(fmt_response(answer["response"]))}</b> · '
                f'Accepted: <b>{html.escape(answer_text(question))}</b></p>')
    picked = answer["response"] if isinstance(answer["response"], list) else [answer["response"]]
    rows = []
    for letter, text in question["options"].items():
        classes = []
        tags = []
        if letter in question["correct"]:
            classes.append("right")
            tags.append("correct")
        if letter in picked:
            classes.append("picked")
            tags.append("your pick")
        tag_html = f'<span class="otag">{" · ".join(tags)}</span>' if tags else ""
        rows.append(f'<li class="{" ".join(classes)}"><b>({letter})</b> <div class="rich">{rich(text, pid)}</div>{tag_html}</li>')
    return '<ol class="opts">' + "".join(rows) + "</ol>"


def llm_block(llm: dict | None, pid: str) -> str:
    if not llm:
        return ""
    if "error" in llm:
        return f'<div class="llm err">Claude: {html.escape(llm["error"])}</div>'
    parts = ['<div class="llm"><h4>Claude\'s explanation</h4>']
    if llm.get("key_check") == "disagree":
        parts.append(f'<div class="dispute"><b>Key dispute:</b> Claude thinks the official key may be wrong. '
                     f'Check this by hand before trusting your score.<div class="rich">{rich(llm.get("key_check_note", ""), pid)}</div></div>')
    if llm.get("mistake"):
        parts.append(f'<p><b>Where it went wrong:</b></p><div class="rich">{rich(llm["mistake"], pid)}</div>')
    parts.append(f'<p><b>Solution:</b></p><div class="rich">{rich(llm.get("explanation", ""), pid)}</div></div>')
    return "".join(parts)


def build_html(attempt: dict, paper: dict, items: list[dict]) -> str:
    cards = []
    for item in items:
        q, a = item["question"], item["answer"]
        pid = image_folder(q, paper)
        badge = {"wrong": "Wrong", "skipped": "Skipped", "correct": "Correct"}[item["status"]]
        lost = q["marks"] - a["marks_earned"]
        topic = html.escape(q["topic"] + (f" / {q['subtopic']}" if q["subtopic"] else ""))
        site = ""
        if q["explanation"]:
            site = f'<details><summary>Site solution</summary><div class="rich">{rich(q["explanation"], pid)}</div></details>'
        cards.append(
            f'<section class="card {item["status"]}">'
            f'<div class="head"><span class="badge">{badge}</span> <b>Q{q["number"]}</b> · {q["type"]} · '
            f'{q["marks"]} mark{"s" if q["marks"] > 1 else ""} · {topic} · {a["time_spent_sec"]}s spent'
            f'{f" · {lost:g} marks lost" if lost else ""}</div>'
            f'<div class="rich">{rich(q["question"], pid)}</div>'
            f'{option_rows(q, a, pid)}{llm_block(item.get("llm"), pid)}{site}</section>'
        )
    wrong = sum(it["status"] == "wrong" for it in items)
    skipped = sum(it["status"] == "skipped" for it in items)
    disputes = sum(1 for it in items if (it.get("llm") or {}).get("key_check") == "disagree")
    title = html.escape(f"Review: {paper['paper']}")
    dispute_line = f" · <b>{disputes} key dispute(s) flagged</b>" if disputes else ""
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{KATEX}/katex.min.css">
<script src="{KATEX}/katex.min.js"></script>
<style>
  body {{ margin: 0; background: #f4f6f9; color: #1d2330; font: 15px/1.55 -apple-system, "Segoe UI", Roboto, sans-serif; }}
  main {{ max-width: 900px; margin: 0 auto; padding: 24px 16px 60px; }}
  h1 {{ font-size: 22px; margin: 0 0 4px; }}
  .sub {{ color: #5d6677; margin: 0 0 18px; }}
  .card {{ background: #fff; border: 1px solid #d5dae3; border-left: 5px solid #999; border-radius: 8px; padding: 14px 16px; margin-bottom: 14px; }}
  .card.wrong {{ border-left-color: #d64545; }}
  .card.skipped {{ border-left-color: #c9a227; }}
  .card.correct {{ border-left-color: #2e9d57; }}
  .head {{ color: #5d6677; font-size: 13px; margin-bottom: 8px; }}
  .head b {{ color: #1d2330; }}
  .badge {{ display: inline-block; font-weight: 600; font-size: 12px; padding: 1px 8px; border-radius: 10px; background: #eceff4; color: #1d2330; }}
  .wrong .badge {{ background: #fbe3e3; color: #a62d2d; }}
  .skipped .badge {{ background: #fbf2d5; color: #7d6514; }}
  .correct .badge {{ background: #def3e6; color: #1f6e3d; }}
  .rich {{ white-space: pre-wrap; overflow-wrap: anywhere; }}
  .rich pre {{ white-space: pre; background: #f1f3f7; border: 1px solid #d5dae3; border-radius: 6px; padding: 8px 10px; overflow-x: auto; font: 13px/1.45 ui-monospace, Menlo, monospace; }}
  .rich img {{ max-width: 100%; height: auto; display: block; margin: 6px 0; }}
  .rich table {{ border-collapse: collapse; white-space: normal; }}
  .rich td, .rich th {{ border: 1px solid #d5dae3; padding: 2px 6px; }}
  .opts {{ list-style: none; padding: 0; margin: 10px 0; }}
  .opts li {{ display: flex; gap: 8px; align-items: flex-start; border: 1px solid #e3e6ec; border-radius: 6px; padding: 6px 10px; margin: 5px 0; }}
  .opts li.right {{ border-color: #2e9d57; background: #f0faf3; }}
  .opts li.picked:not(.right) {{ border-color: #d64545; background: #fdf1f1; }}
  .otag {{ margin-left: auto; font-size: 12px; color: #5d6677; white-space: nowrap; }}
  .llm {{ border-top: 1px dashed #d5dae3; margin-top: 10px; padding-top: 8px; }}
  .llm h4 {{ margin: 0 0 6px; font-size: 14px; }}
  .llm.err {{ color: #a62d2d; }}
  .dispute {{ background: #fff4e5; border: 1px solid #e0a040; border-radius: 6px; padding: 8px 10px; margin-bottom: 8px; }}
  details {{ margin-top: 10px; }}
  summary {{ cursor: pointer; color: #1f5fae; }}
</style></head>
<body><main>
<h1>{title}</h1>
<p class="sub">Score {attempt.get('score')} / {attempt.get('total_marks')} · {wrong} wrong · {skipped} skipped{dispute_line} ·
attempt {html.escape(attempt.get('attempt_id', ''))}. Wrong answers first, highest marks first.</p>
{''.join(cards) or '<p>Nothing to review: every question was answered correctly.</p>'}
</main>
<script>
  document.querySelectorAll(".math").forEach(function (el) {{
    if (window.katex) katex.render(el.textContent, el, {{ throwOnError: false }});
  }});
</script>
</body></html>
"""


# ---------------------------------------------------------------- main

def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("results_file", type=pathlib.Path)
    parser.add_argument("--include-correct", action="store_true")
    parser.add_argument("--llm", action="store_true")
    parser.add_argument("--max-llm", type=int, default=30, help="cap on new Claude calls per run (default 30)")
    parser.add_argument("--show-prompt", action="store_true")
    parser.add_argument("--out", type=pathlib.Path)
    args = parser.parse_args(argv[1:])

    attempt, paper = load_attempt(args.results_file)
    items = build_items(attempt, paper, args.include_correct)
    print(f"{paper['paper']}: {sum(i['status'] == 'wrong' for i in items)} wrong, "
          f"{sum(i['status'] == 'skipped' for i in items)} skipped")

    if args.show_prompt:
        first = next((i for i in items if i["status"] != "correct"), None)
        if first is None:
            print("No wrong or skipped questions.")
            return 0
        print(json.dumps(build_request(first["question"], first["answer"]), indent=2, ensure_ascii=False))
        return 0

    if args.llm:
        run_llm(items, args.max_llm)

    out = args.out or REVIEWS_DIR / f"{attempt.get('attempt_id', attempt['paper_id'])}.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build_html(attempt, paper, items), encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT) if out.resolve().is_relative_to(ROOT) else out}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
