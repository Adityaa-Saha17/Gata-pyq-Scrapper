# GATE simulator: always-on local server

Once started, open <http://localhost:8765/simulator/exam.html>.

The server starts again by itself after a restart or login, until you run the killer.

The server is `simulator/server.py`. It serves the project folder and, every time you submit a test:

- saves the attempt into `results/` as `<attempt_id>.json`
- rewrites `reports/performance.json` (the same report as `python3 tools/performance.py`)
- writes the review page `reviews/<attempt_id>.html` (site solutions only; for Claude's explanations run `tools/reviewer.py <result file> --llm` yourself)

Each question in a review has a **Study material** line. Its links open the books in `Study Materials/` at the notes for that question's subtopic and at the past questions on it (exact position in Chrome; other browsers may only jump to the page). If the books have no notes for the subtopic, it links the topic's chapter and says so; if they do not cover the topic at all, it says that instead. The page positions are indexed in `cache/study_index.json`, rebuilt by itself when a PDF changes. Subtopics the index cannot place by itself are mapped by hand in `schema/study_map.json`; check that file with `python tools/study_index.py --check`. Reviews written before the PDFs were added do not have the line: run `tools/reviewer.py <result file>` again.

The start page lists all past attempts with these numbers and a link to each review. It checks the three folders again on every load, so a result file moved into `results/` by hand shows up too.

If the page is opened from any other server, the result is downloaded to the Downloads folder instead and nothing else updates.

To run it by hand instead: `python3 simulator/server.py` (add `--port N` for another port).

## Runner

Paste into Terminal once:

```bash
cat > ~/Library/LaunchAgents/local.gate-simulator.plist <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>local.gate-simulator</string>
    <key>ProgramArguments</key>
    <array>
        <string>/opt/homebrew/bin/python3</string>
        <string>/Users/adityaasaha/Documents/Gata pyq Scrapper/simulator/server.py</string>
        <string>--port</string>
        <string>8765</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardErrorPath</key>
    <string>/Users/adityaasaha/Library/Logs/gate-simulator.log</string>
</dict>
</plist>
EOF
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/local.gate-simulator.plist
```

## Killer

Stops it for good:

```bash
launchctl bootout gui/$(id -u)/local.gate-simulator
rm ~/Library/LaunchAgents/local.gate-simulator.plist
```

## If it does not load

- macOS may ask whether python3 can access the Documents folder. Click **Allow**.
- Check the log: `cat ~/Library/Logs/gate-simulator.log`
- If the project folder is moved or renamed, run the killer, fix the folder path in the runner above, and run the runner again.
- After changing the runner (for example the port), run the killer and then the runner again.
