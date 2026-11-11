# Recon: practicepaper.in GATE CSE pages

Date: 2026-11-06. Target site: `practicepaper.in`. OS used: macOS.

## TL;DR
- **No bot wall.** Plain `curl` with a normal browser `User-Agent` returns HTTP 200 and the full HTML. `playwright` is **not needed** for this site at recon time. Re-check if the site changes.
- **Pages are server-rendered.** All question data for the current page lives in a `<script id='pp-quiz-data' type='application/json'>` blob inside the HTML. No AJAX, no client-side hydration required.
- **Each paper is paginated 5 questions per page** via `?page_no=N`. GATE 2024 S1 has `totalPages: 13`, `totalQuestions: 65`.
- **Answer keys are published by the site** (in the same blob). Solutions and topic/subtopic tags are also there. No LLM is needed to tag or score — only to enrich explanations later.
- **49 papers** listed on the year-wise index, from 1987 to 2026. Old papers (pre-2010) have different question counts (e.g., 1988 has 1 question).
- `robots.txt` only disallows `/wp-admin/`. Our pages are under `/gate-cse/…` and are allowed.

## Legal / politeness

- `robots.txt`: `User-agent: *, Disallow: /wp-admin/, Allow: /wp-admin/admin-ajax.php`. Sitemap at `https://practicepaper.in/sitemap_index.xml`. Our paths are fine.
- Terms: not reviewed in detail — personal-use scraping with a conservative rate limit. If the site adds a bot wall later, revisit.
- Rate: recon used `sleep 3-4s` between page fetches. Full crawl should keep >= 3s between requests and respect `Retry-After` / 429.

## Index page

- URL: `https://practicepaper.in/gate-cse/gate-cse-year-wise-questions`
- Shape: server-rendered HTML, links to each paper. Extraction:
  - Pattern: `<a href="/gate-cse/gate-cse-YYYY(-set-N)?">…</a>`
  - Regex: `gate-cse-\d{4}(-set-\d+)?$`
- Snapshot: 49 papers, 1987–2026.
- 2025 and 2026 are the real GATE exams (confirmed against the official answer keys, which match all 65 questions in each set).
- There is no 2008 paper on the index.

## Paper page

- URL template: `https://practicepaper.in/gate-cse/gate-cse-<year>(-set-<n>)?[?page_no=<p>]`
  - Page 1 is the bare URL; pages 2+ use `?page_no=N`.
  - Example: `https://practicepaper.in/gate-cse/gate-cse-2024-set-1?page_no=7`.
- Pagination links (also parse-able from the DOM):
  - `<a class="pp-set-tab" data-page="N" href="…?page_no=N">`
  - `<a class="pp-btn pp-btn-primary" id="ppNextBtn" rel="next" href="…?page_no=N">`
- 5 questions per page. Total = `meta.totalPages * meta.questionsPerPage`, both inside the JSON blob.

### The JSON blob (primary source of truth)

Selector: `<script id='pp-quiz-data' type='application/json'>…</script>`. The content is a clean JSON document. Example shape:

```json
{
  "meta": {
    "quizId": 11241,
    "quizName": "GATE CSE 2024 SET-1",
    "pageTitle": "GATE CSE 2024 SET-1 Question Paper with Solutions and Answer Key",
    "timeLimit": 0,
    "pageNo": 1,
    "totalPages": 13,
    "totalQuestions": 65,
    "totalMarks": 100,
    "questionsPerPage": 5,
    "pageUrl": "/gate-cse/gate-cse-2024-set-1",
    "ajaxUrl": "https://practicepaper.in/wp-admin/admin-ajax.php",
    "bookmarksUrl": "…",
    "resultsJs": "…",
    "adClient": "…",
    "ads": { "title": "…", "q2": "…", "q4": "…" }
  },
  "questions": [ { … 5 questions … } ]
}
```

### Per-question fields (all three types)

Always present:
- `id` — integer, globally unique across the site (`1124101` etc.). Our stable join key.
- `number` — 1-based index within the paper, as rendered by the site.
- `type` — `"MCQ" | "MSQ" | "NAT"`.
- `marks` — integer, 1 or 2.
- `text` — question body. Contains `[latex]…[/latex]` wrappers for math (keep raw), inline `<br>`, and `<img src="/wp-content/uploads/…">` for figures. C code snippets appear as plain text with `\n` newlines — **no `<pre>` / `<code>`**.
- `solution` — HTML-formatted explanation. May contain `[latex]…[/latex]` and `<br>`.
- `tag1`, `tag1_url` — primary topic (e.g. `"Discrete Mathematics"`).
- `tag2`, `tag2_url` — subtopic (e.g. `"Functions"`).

Type-specific answer fields:

| Type | `options`               | Answer key fields                                    |
|------|-------------------------|------------------------------------------------------|
| MCQ  | 4-element array         | `correct: <int>` (0-indexed)                         |
| MSQ  | 4-element array         | `correct: null`, `correctSet: [<int>, …]` (0-indexed)|
| NAT  | `null`                  | `ansMin: <number>`, `ansMax: <number>`               |

Verified by sampling pages 1, 4, 7, 10, 13 of GATE CSE 2024 Set 1 (25/65 questions): 13 MCQ, 7 MSQ, 5 NAT.

### Sections (General Aptitude vs Technical)

The site **does not** emit a dedicated section field. Section is reliably derivable from `tag1`:
- `tag1 == "General Aptitude"` -> section = "General Aptitude"
- otherwise -> section = "Technical"

Note: in the sampled GATE 2024 S1 the site has placed GA questions at Q61–Q65, not Q1–Q10. The site renumbers; `number` is the site's rendering order. Our stable id is `id`.

### Topic tag vocabulary (observed on GATE CSE 2024 S1 sample)

`Discrete Mathematics, Engineering Mathematics, Digital Logic, Computer Organization, Operating System, Computer Network, Theory of Computation, General Aptitude, Compiler Design, Data Structure, Algorithm, Database Management System`.

The site uses singular forms and minor name differences vs the official GATE syllabus. `schema/topics.json` holds the canonical list plus an alias map; the scraper normalizes `tag1` through the alias map.

### Images

- Appear as `<img src="/wp-content/uploads/GATE/CS/<yearset>/qNN.webp" />` (relative paths) inside `text` and `solution`.
- The scraper will:
  1. Extract all `<img src>` into a per-question `images[]` list with absolute URLs.
  2. In the full-crawl stage, download them into `cache/images/<paper_id>/qNN.webp` and rewrite `text`/`solution` to reference local paths.

### Code blocks

- Site stores C code as plain text with real newlines inside `text`. No HTML markup to key off of.
- The scraper leaves code inline; the simulator uses CSS `white-space: pre` on detected code-ish spans (heuristic: multi-line block with braces, semicolons, or `#include`).
- No separate `code` field is populated in Session 2; defer until we hit a question where that fails.

## Known risks / open questions

1. **Old papers may have different structure.** Papers before ~2010 may use a non-standard quiz plugin or different fields. Session 2 must validate against at least one paper from 2010 or earlier before declaring success.
2. **Answer-key correctness.** The site's keys appear to match official GATE keys on spot-check. Session 3 should cross-check with a second source (gateoverflow.in or examside) on a random sample.
3. **Official keys (resolved for 2022–2026).** `scraper/compare_official_keys.py` checks the site against official final keys from gate2027.iitm.ac.in/download; 4 differences were found and fixed through `schema/key_overrides.json`. The official 2021 key is a scanned PDF and is not checked.
4. **NAT exactness.** Observed `ansMin == ansMax` for integer answers (e.g., Q46 exactly 3). Some NAT answers should be a range (e.g., `2.99` to `3.01` for a two-decimal rounded answer). Session 2 should log any NAT where `ansMin != ansMax` and verify by hand.
5. **Image availability.** Observed `.webp`. CDN behavior under rapid download not yet tested — batch image fetch should also keep >= 1s delay.

## Ready-for-Session-2 scraper plan

Single-paper scraper (`scraper/scrape_paper.py`):

1. Input: paper slug (e.g. `gate-cse-2024-set-1`) and a `paper_id` (e.g. `2024-S1`).
2. Fetch page 1 (cache first, HTTP only if cache miss). Parse the JSON blob. Read `meta.totalPages`.
3. For `p` in `2..totalPages`: `sleep(3)`, fetch with same UA, parse blob.
4. Merge all `questions[]` by `id`.
5. Normalize each question into the paper-schema shape (see `schema/paper.schema.json`).
6. Validate: `len(questions) == meta.totalQuestions`; each MCQ has 4 options and a valid `correct` letter; each MSQ has 4 options and >= 1 letter in `correct`; each NAT has `nat_range` with `lo <= hi`.
7. Write `papers/<paper_id>.json`.

Topic normalization uses `schema/topics.json`.
