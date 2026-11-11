# Handshake: GATE CSE PYQ Scraper + Mock Test System

This is the context handoff from a planning chat. Read it fully before doing anything.

## Ground rules (do these first, every time)
1. **Confirm the OS before starting any work.** Preference is macOS; Linux only if the project needs it. Ask even though this folder is on a Mac.
2. **Share the plan for the session and wait for a go-ahead.** Don't dive straight in.
3. Language for this project: **Python** for scraping and tooling, plus HTML/JS for the exam simulator. (C++ is my usual default, but it doesn't apply here.)
4. Use standard, meaningful variable names (`n`, `i`, `j`, `ans`, `question`, `paper`). No quirky names.
5. Show code in inline code blocks when explaining it, and write the real files into this folder.
6. Be polite to the site: slow requests (a few seconds apart), cache raw HTML, personal use only, and check robots.txt and the terms first.

## The goal
Scrape GATE CSE previous-year papers into **one JSON file per paper**. That JSON is the single source of truth, and everything else is generated from it:

```
scraper ──▶ papers/*.json ──┬──▶ PDF generator
                            ├──▶ exam simulator (exam.html) ──▶ results/*.json ──▶ performance tracker
                            └──▶ reviewer (correct answer + why, via LLM)
```

- **Source index:** https://practicepaper.in/gate-cse/gate-cse-year-wise-questions
  - It links to one page per paper; each page shows the questions and options.
- **Simulator:** a single generic `exam.html` that loads any paper JSON. It needs a 180-minute timer, a GATE-style question palette (answered / marked for review / not visited), KaTeX for math, and GATE scoring. It outputs a results JSON.
- **Performance tracker:** combines all results files into per-topic accuracy and average time per question across tests.
- **Reviewer:** takes a results file plus the paper JSON and explains the correct answers, starting with the ones I got wrong.

## Known facts and risks
- **practicepaper.in blocked an automated fetch (bot detection).** A plain `requests` call will probably fail, so expect to need `playwright` (a real browser). Verify this during recon.
- GATE has three question types:
  - **MCQ:** one correct option, negative marking (1/3 of the marks).
  - **MSQ:** one or more correct options, no negative marking, no partial credit.
  - **NAT:** a numerical answer, no options, scored correct if within a range.
- Questions contain **LaTeX** (keep it raw), **C code blocks** (preserve whitespace) and **images** (automata, circuits, ER diagrams: save their URLs and download them).
- **Fallback sources** if the site is too hostile: gateoverflow.in (has topic tags) and questions.examside.com (year-wise, shows question type and marks).
- **Answer keys must come from the site or official GATE keys, never from an LLM.** Wrong keys would silently corrupt performance data. The LLM only writes explanations.
- **Topics must exist before any test is taken.** Use a fixed topic list (the official GATE CSE syllabus subjects) plus a free-form `subtopic`. Scrape the topic tags if the site has them; otherwise an LLM tags questions, but only against that fixed list.

## Draft paper schema (`papers/<id>.json`)
```json
{
  "paper_id": "2024-S1",
  "paper": "GATE CSE 2024 Set 1",
  "year": 2024,
  "set": 1,
  "source_url": "...",
  "scraped_at": "ISO-8601",
  "questions": [
    {
      "id": "2024-S1-Q23",
      "number": 23,
      "section": "General Aptitude | Technical",
      "type": "MCQ | MSQ | NAT",
      "marks": 1,
      "negative_marks": 0.33,
      "question": "text with $LaTeX$ kept raw",
      "code": null,
      "images": [],
      "options": { "A": "...", "B": "...", "C": "...", "D": "..." },
      "correct": ["B"],
      "nat_range": null,
      "topic": "Databases",
      "subtopic": "B-tree",
      "explanation": null
    }
  ]
}
```
- `id` is permanent and is the join key for results, the performance tracker and the reviewer.
- For NAT questions, `options` is null and `nat_range` is `[low, high]`.
- `explanation` stays null until the reviewer stage.

## Draft results schema (`results/<paper_id>_<timestamp>.json`)
Per attempt: `paper_id`, start/end time, total score, and for each question: `question_id`, `response`, `is_correct`, `marks_earned`, `time_spent_sec`, `marked_for_review`.

## Planned folder layout
```
Gata pyq Scrapper/
├── handshake.md
├── scraper/        # RECON.md, scrape_paper.py, crawl_all.py
├── cache/html/     # raw HTML cache
├── papers/         # one JSON per paper
├── mocks/          # topic-wise mocks + index.json (generated)
├── schema/         # paper.schema.json, results.schema.json, topics.json
├── simulator/      # exam.html
├── results/        # one JSON per attempt
└── tools/          # make_pdf.py, performance.py, reviewer.py, make_topic_mocks.py
```

## Session plan
1. **Recon + schemas:** inspect the index page and one paper page (plain HTML or JS-rendered? where are the questions, options, answer key and topic tags?). Write `scraper/RECON.md`, the schema files and `topics.json`, and set up a venv.
2. **Single-paper scraper:** one paper to one JSON file, handling MCQ/MSQ/NAT, LaTeX, code and images. Validate: 65 questions, 4 options per MCQ/MSQ, every question has a `correct` answer.
3. **Full crawl:** all papers from the index, with delays, retries and the cache. Fill in topics and check the answer keys.
4. **Simulator:** `exam.html` that outputs a results JSON.
5. **Performance tracker + PDF generator.**
6. **Reviewer:** LLM explanations.

## Status (2026-11-07)
All six sessions are built and the simulator has been tested end to end in a browser. Details of the site's format are in `scraper/RECON.md`.

- **Data:** 49 papers (1987–2026) in `papers/`, 2,798 questions, all valid against `schema/paper.schema.json`. 413 images in `cache/images/`. Raw HTML cached in `cache/html/` (re-scrapes need no network).
- **Scraper:** `scraper/scrape_paper.py`, `scraper/crawl_all.py` (`--only`, `--force`), `scraper/download_images.py`.
- **Key check:** `scraper/check_keys.py` compares each key with the "Answer:" line in the site's own solution (offline). 1,301 agree, 0 disagree; pre-2009 papers can't be checked this way.
- **Official keys:** `scraper/compare_official_keys.py` checks 2022–2026 (8 papers, 520 questions) against the official final-key PDFs in `cache/official_keys/` (from gate2027.iitm.ac.in/download). The 2021 key is a scanned PDF, so both 2021 sets (130 questions) were compared by eye on 2026-11-07. Corrections live in `schema/key_overrides.json` (2021-S1-Q23 also accepts 819–820, 2021-S1-Q64 also accepts C, 2023-Q17, 2023-Q20, 2023-Q57 marks-to-all, 2025-S1-Q55). The simulator and tools handle `accepted` alternatives and `marks_to_all`.
- **Marks fix (2003–2007):** `schema/marks_overrides.json` sets the real 1-/2-mark split (150 marks per paper), taken from scans of the papers in `cache/question_papers/` and the GATE Forum 2007 reprint. Negative marks keep the 1/3 rule (0.33 / 0.67); the originals reportedly used 0.25 / 0.5, but no primary source was found.
- **Simulator:** `simulator/exam.html` (serve the project root with `python3 -m http.server`). Browser-tested with Playwright on 2026-11-07: scoring, palette, resume after reload, time-out auto-submit, KaTeX, images, phone width. A time-out now downloads the results JSON automatically, as a manual submit does.
- **Tools:** `tools/performance.py`, `tools/make_pdf.py`, `tools/reviewer.py` (`--llm` needs `ANTHROPIC_API_KEY`). The tracker counts a question as attempted only when it has a response.
- **Topics:** `schema/topics.json` (canonical list + aliases, incl. legacy Software Engineering / Web Technologies); `schema/topic_overrides.json` for 9 questions the site left untagged.

## Additions (2026-11-11)
- **Calculator:** `simulator/exam.html` has a "Calculator" button in the exam top bar. It opens a draggable, mouse-operated scientific calculator (trig with Deg/Rad, ln, log, log₂, powers, roots, n!, mod, %, EXP, Ans, memory keys). Expressions go through a small parser in the page, not `eval()`. It works in full papers and topic mocks, and its memory is cleared at the start of each exam.
- **Topic-wise mocks:** `tools/make_topic_mocks.py` builds `mocks/<topic-slug>-<nn>.json` plus `mocks/index.json` from `papers/`. 87 mocks across 12 topics, 30 questions and 90 minutes each (`--size`, `--minutes`, `--seed`, `--dry-run`).
  - No question repeats within a topic. The oldest leftover questions are left out (0 to 27 per topic).
  - Questions are dealt across subtopic, marks and type, so every set mixes subtopics. Subtopics are not shown before or during a test, only in the results table afterwards.
  - Each set has 1-mark questions first, then 2-mark. Total marks vary by set (40 to 50).
  - The three questions that refer to "the previous question" (2010-Q55, 2011-Q53, 2011-Q55) stay directly after that question.
  - Software Engineering (25 questions) and Web Technologies (4) have too few questions for a set.
  - Mock questions keep their original `id`, with `source_paper_id` and `source_number` added; `number` is the position in the mock. Format: `schema/mock.schema.json`.
  - **Re-run the generator after editing `papers/` or an override file**, because mocks hold copies of the questions. The same seed gives the same sets as long as the question pool is unchanged.
- **Simulator:** the start page lists full papers and topic mocks. The timer comes from the mock's `duration_min` (180 for full papers). Any id that is not `YYYY` or `YYYY-S<n>` is loaded from `mocks/`.
- **Tools:** `tools/make_pdf.py` and `tools/reviewer.py` accept mock ids; `tools/performance.py` needs no mock data because results join on the original question ids. `schema/results.schema.json` allows mock ids in `paper_id`.
- **Testing:** browser-tested with Playwright on 2026-11-11 (calculator arithmetic, drag, a full topic mock with scoring, resume, time-out, a full paper, phone width). Playwright's bundled Chromium build was missing, so the test used the installed Chrome: `pw.chromium.launch(channel="chrome")`.

Known data issues (not fixed, need a decision or an official source):
1. **2003–2007 negative marks and linked answers:** negative marks use the 1/3 rule rather than the reported 0.25 / 0.5. Linked-answer pairs (2005–2007) are scored as independent questions.
2. **Papers before 2003 are partial:** the site has only the objective part of each paper (1 to 55 questions), so they are practice sets, not full mocks.
3. **2008 is missing** from the site's index.
4. **1991 and 1993 use five options (A–E).** 1991 says "more than one may be correct", but the site stores one answer per question.
5. **No official keys before 2021** in the IIT Madras archive; 2020 and earlier rely on the site. gateoverflow.in and questions.examside.com block AI agents in robots.txt, so they were not used.
