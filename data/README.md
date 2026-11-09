# data/

The site's numbers live here. `scripts/build-site-data.py` writes them into the
places that use them:

| Source | Generates |
|---|---|
| `models.json` | `modelData` and the pricing chart rows in `claude-models.html`; all of `forecast/data/anthropic_releases.csv` |
| `benchmarks.json` | every benchmark chart's data in `claude-models.html` (SWE-bench Pro, Terminal-Bench 2.1, OSWorld, Vending-Bench 2, Vending-Bench Arena, GDPval-AA, RLI, ARC-AGI-2/3, Capability Profile) |
| `board-checks.json` | the Board Coverage section of `claude-models.html` |

```
python3 scripts/build-site-data.py            # rebuild
python3 scripts/build-site-data.py --check    # exit 1 if anything is stale
python3 scripts/build-site-data.py --list     # what is generated from what
```

In the page, generated blocks sit between `// >>> generated:NAME` and
`// <<< generated:NAME`. Don't edit inside them: the next build overwrites the
edit, and the pre-commit hook (`.githooks/pre-commit`, wired by
`scripts/install-hooks.sh`) refuses a commit while `--check` fails. The data is
written into the HTML rather than fetched at runtime because
`scripts/predict-releases.js` and `forecast/engine/backtest.py` read the release
block straight out of the page.

## To add a model

1. **`models.json`**: append one object to `releases` (two for a co-launch,
   sharing a `colaunch_group`). Copy the previous release in the family and
   change `id`, `date`, `model`, `version`, prices, `url`, `note`. Keep the list
   in date order.
   That one entry puts the model on the family card, the release calendar,
   timeline and shipping-pace charts, into the cadence forecast and
   `predict-releases.js`, and into the forecast engine's CSV. It also moves the
   pricing chart: the bars follow the newest generally available release in each
   family, and the dashed "previous price" mark is derived from the family's
   price history. And it queues the model as *pending, never checked* on every
   tracked board in Board Coverage.
2. **`benchmarks.json`**: add a row to each chart you have a figure for, with
   `source`, `as_of` and, where a reader needs it, a `note`. Append a line to
   the chart's `history` saying what you read and when. A row's `date` must be
   the model's release date; the build checks it against `models.json`.
3. **`board-checks.json`**: for each board you looked at, add a check for the
   model (`listed` with a `value`, or `pending`) and set the board's
   `last_checked` to today. See below.
4. Run `python3 scripts/build-site-data.py`, then look at the page.

## To record a board re-check

- Looked and found nothing new: set that board's `last_checked` to today. Every
  pending row of the board picks it up.
- The model is now listed: change its check to `"status": "listed"`, add
  `value`, and add the chart row in `benchmarks.json`. For the date:
  - `first_listed` only when the listing date is really known: the board states
    it, or you read the board on release day and the entry was there. Say which
    in `first_listed_basis`.
  - otherwise `first_seen_by_site`: the day of your read. It is an upper bound
    on the listing date and is shown as "≤Nd". It never feeds the typical-lag
    median, which needs three known dates per board.
  - `not_listed_as_of` is the last read that found nothing, if there was one.
- Never put a guessed date in `first_listed`.

Then rebuild. `matrix.since` in `board-checks.json` sets which releases get a
column in the table; move it forward when the table gets too wide for a phone.

## Still manual

- **Prose.** The notes under each chart, the section sub-heads and the intro
  lines in `claude-models.html` are hand-written. That includes sentences that
  hard-code a check date ("board checked November 9, 2026", "has no run yet"):
  Board Coverage updates from the JSON, those sentences do not.
- **The `lastUpdated.textContent` stamp** in `claude-models.html`.
- **Chart furniture**: legends (a family's first appearance on a chart needs a
  legend entry), axis ranges and headroom constants such as `maxPrice`, the
  "Announcement" link rows, and which models the Capability Profile plots
  (`models` in `benchmarks.json` is data, but the swap is a decision).
- **A price change without a new model.** The pricing chart is derived from
  launch prices; a mid-life change has no place in `models.json` yet.
- **The forecast runbook's other steps** (`forecast/WEEKLY_RUNBOOK.md`):
  `named_versions.json`, `raw/signals_research.csv`, the `MAP` in
  `tools/build_signals.py`, markets, `weekly.py`, the narrative.
- **System cards** (`system-cards/`, `scripts/build-system-cards.py`) are a
  separate pipeline.

## Fields

Each file opens with `_about` and `_fields`. Briefly: anything on a benchmark
row named `source`, `source_url`, `as_of`, `note` or `caveats` is provenance and
stays in the JSON; every other key is chart data and is copied into the page
exactly as written. The pull logs that used to sit in code comments above each
array are each chart's `history`.
