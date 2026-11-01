# Weekly forecast run: runbook

A scheduled task runs this every week. It updates the release forecast, grades it if Anthropic shipped a model, refreshes the Claude Model Guide, and writes a weekly summary. It's written so a fresh session with no memory of past runs can follow it start to finish.

## Ground rules

- **Current model: v3d** (adopted 2026-11-01 with Jacob's approval; see README).
- **The model is frozen.** Don't change `engine/`, `live.py`, the config, or the pool weight during a weekly run. Forward grading is only honest if the model stays fixed. If something looks wrong with the model, write it up under "Proposed changes" in the summary for Jacob to decide.
- **Never edit or delete** `history/*.json`, existing rows of `forecast_log.csv`, or past `weekly/*.md` files. Add new ones only.
- **No fabrication.** Every new release, signal, market price or competitor row needs a URL you actually opened, or a vault path. If a source won't load, say so in the summary and leave the data out.
- **External actions allowed:** pushing to `JacobBrooke95/Claude-Model-Guide` (`main`) and writing one note to Jacob's vault. Nothing else.
- **Dates:** use America/Chicago, and write YYYY-MM-DD in the data files.

## 1. Set up

1. Attach the repo with push access (`add_repo` owner `JacobBrooke95`, repo `Claude-Model-Guide`, access `push`), then clone it.
2. `cd forecast`.
3. Check that `python3 -c "import numpy, scipy, pandas"` works. If it doesn't, run `pip install --break-system-packages numpy scipy pandas`.
4. Read the newest `weekly/*.md` and the current `output/forecast.json` so you know last week's state.

## 2. Did Anthropic ship a model since the last run?

Check these first-party sources:
- https://platform.claude.com/docs/en/release-notes/overview
- https://www.anthropic.com/news
- https://platform.claude.com/docs/en/about-claude/models/overview
- https://support.claude.com/en/articles/12138966-release-notes

A **release** is the first day the model is usable by the public, through the API or the apps. For restricted models (Mythos), it's the day of the official announcement.

For each new model:

1. **Release table.** Append a row to `data/anthropic_releases.csv`:
   - Columns: `release_id, date, family, model, version, generation, access, price_in, price_out, colaunch_group, source_url, note`.
   - Prices come from the official pricing page.
   - A co-launch (two families on one day) shares a `colaunch_group`.
2. **Claude Model Guide page** (`../claude-models.html`):
   - Add the release to `modelData` inside the `// ===== release-data:begin =====` sentinels: `{ version, date, url }`, plus `restricted: true` or `notReleased: true` where they apply. Follow the existing entries.
   - Update the `lastUpdated.textContent` line to say what was added and when.
   - Don't touch the `forecast` block.
   - Then run `node ../scripts/predict-releases.js --backtest` from `forecast/` and check that it runs without errors.
   - Update the pricing or benchmark charts only if you can verify the numbers on an official page. Otherwise note "charts not yet updated" in the summary.
3. **Named versions.** Remove that family's entry from `data/named_versions.json`. If artifacts already name the next version, put that name in its place.
4. **Signals.** In `data/raw/signals_research.csv`:
   - Rows that pointed at this model (for example `UNRELEASED Fable 5.5 (aka 5.2)`) get the real `release_id` and `release_date`.
   - Add a mapping for the new name in `MAP` in `tools/build_signals.py`.
   - Run `python3 tools/build_signals.py`.

The grading itself happens automatically in `weekly.py`: every frozen snapshot made between the family's previous release and this one is scored.

## 3. New inputs this week

Look for anything from the last 7–10 days.

**Signals.** Pre-release sightings of unreleased Claude models:
- Cloud catalog rows (Bedrock, Vertex, Azure).
- Model IDs or codenames in clients (Cursor, Devin, Copilot, LiteLLM, OpenRouter).
- Press reports, partner early-access reports, red-team rounds, A/B routing, exec hints, tipster claims.

Where to look:
- **Jacob's vault**, via the "Jacob's Vault" connector if it's available: `2-Areas/Claude-Rumors/claude-rumors-hub.md` (Live board), `2-Areas/Claude-Rumors/Tracker/instrument-runs/`, `2-Areas/Claude-Rumors/Sightings/`. These are first-hand desk checks and the best source.
- **Web search:** TestingCatalog, The Information, Reuters, Bloomberg, The Verge, and "Claude" plus "Anthropic next model".

How to log them:
- Add each sighting as a row in `data/raw/signals_research.csv` with the existing columns and codes: `CLOUD_CATALOG, FIRST_PARTY_DOC, CLIENT_STRING, ARENA_CODENAME, EAP_PARTNER, PRESS_REPORT, EXEC_TEASE, TIPSTER, OTHER` (OTHER notes start with `RED_TEAM_CODENAME:` or `AB_ROUTING:`). Grade A, B or C, with a URL.
- An unreleased target uses `release_id` "UNRELEASED <name>". If the target is new, add it to `LIVE` in `tools/build_signals.py`, listing the families it points at.
- A dated call that has passed without a release gets "missed" in its note.
- When you're done, run `python3 tools/build_signals.py`.

**Markets.** Write today's prices to `data/raw/markets_<YYYY-MM-DD>.csv` with the columns `platform, question, prob, volume, close_date, url, retrieved_at`.
- Polymarket: `https://gamma-api.polymarket.com/public-search?q=claude` and the event pages.
- Manifold: `https://api.manifold.markets/v0/search-markets?term=claude`.
- Keep Polymarket's question wording exactly. `engine/market.py` (`LADDERS`) parses "Next Fable Model (5.2+) released by <date>?", "Next Claude Opus (5.6+) released by <date>?" and so on.
- If the wording changes after a release (for example a new "5.6+" ladder), update the regexes in `LADDERS`. That is data parsing, not a model change.

**Competitors** (logged, not used in the final model). Append new frontier releases to `data/competitor_releases.csv`.

**Corporate.** Note IPO milestones, S-1/A filings and safety-gating news for the summary narrative only.

## 4. Run the forecast

```
python3 weekly.py
```

This writes `output/forecast.json`, `history/forecast_<date>.json`, new rows in `forecast_log.csv`, `output/grades.json` and `weekly/<date>.md`, and rebuilds `../release-forecast.html`.

## 5. Narrative

1. In `weekly/<date>.md`, replace the `<!-- NARRATIVE … -->` line with a short write-up. Plain prose, no hype. Cover:
   - What shipped, and how the forecast did on it, in plain terms: "it gave X% by that day; the market gave Y%".
   - The new inputs that moved the numbers, with links.
   - The biggest model-versus-market gap and the reason for it.
   - Anything that should make Jacob trust this week's numbers less.
   - "Proposed changes", if any.
2. In `page_text.json`:
   - Set `watch_family` to the family most worth watching.
   - Rewrite `watch_html` for that family: the facts behind the current call, with model and market numbers. Keep the existing tone.
   - Update or clear `watch_band`: `[start, end, label]`, or remove the key.
3. Run `python3 tools/build_page.py` again.

## 6. Verify before pushing

- Render `../release-forecast.html` with Playwright at 1200px and 400px. There should be no console errors and no horizontal overflow.
- Check the forecast: each CDF in `output/forecast.json` is non-decreasing, and every probability is between 0 and 1.
- The Claude Guide's Release Calendar (`claude-models.html`) and its "Statistical forecast" box read `forecast/output/forecast.json` straight from the site, so they update with no edits. Leave the family cards and the EWMA cadence list alone; Jacob wants that cycle information kept. After the Pages deploy finishes, load https://jacobbrooke95.github.io/Claude-Model-Guide/claude-models.html and check that the calendar footer reads "statistical forecast, as of <this run's date>".
- `git diff --stat`: only the expected files changed, `history/` only added files, and `forecast_log.csv` only appended rows.

## 7. Publish

- Commit to `main` with a message like `Weekly forecast <date>` plus the summary's first line, and push.
- Confirm the GitHub Pages deploy succeeded (`gh run list -R JacobBrooke95/Claude-Model-Guide -L 1`).
- Then write the weekly summary to Jacob's vault at `2-Areas/Claude-Rumors/Tracker/forecast-weekly/<date>.md`, using the "Jacob's Vault" connector, with frontmatter `type: forecast-weekly`. If the connector isn't available, skip this step and say so.

## 8. Report

End the run with the weekly summary: the table, what was graded, what changed, and the link to the page. Send a push notification only when a model shipped, or when a family's probability for the next checkpoint moved 20 points or more.
