# data/

The site's numbers live here. `scripts/build-site-data.py` writes them into the
places that use them:

| Source | Generates |
|---|---|
| `models.json` | `modelData` and the pricing chart rows in `claude-models.html`; all of `forecast/data/anthropic_releases.csv` |
| `benchmarks.json` | every benchmark chart's data in `claude-models.html` (Anthropic ECI, SWE-bench Pro, Terminal-Bench 2.1, OSWorld, Vending-Bench 2, Vending-Bench Arena, GDPval-AA, RLI, ARC-AGI-2, ARC-AGI-3, Humanity's Last Exam, Capability Profile) |
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

## Charts with their own rules

- **Anthropic ECI (`aeci`) is one fit, never a splice.** Each system card refits
  the whole scale, and the card says values from different fits are not
  comparable. When a new card publishes a new table, **replace** `points` whole
  with that card's fit; never append a row from a newer or older card. Earlier
  cards' values live in `earlier_fits` and are not plotted. Rows flagged
  `figure_read` were measured off the card's figure; rows flagged `estimated`
  are this site's own one-hop rescaling of an earlier card's value (their
  `derivation` shows the arithmetic). Drop or re-derive both when the fit
  changes.
  The second panel (`aeci.drift`) is the opposite case: it is append-only.
  When a card prints AECI values, add a column to `drift.fits` and one
  `drift.values` row per value printed, with `"own": true` on the card's own
  model. Only printed values go in; a model shown as an unlabelled dot in a
  figure gets no cell. The estimates' overlap pairs must be cells of this
  matrix, and the two panels and the note must agree on every number.
- **Humanity's Last Exam (`hle`) plots Anthropic's no-tools figures only.**
  With-tools runs, per-effort runs and the two outside boards (Artificial
  Analysis, Scale/CAIS) are recorded under the rows' notes and `other_sources`
  and are never joined to the line. If a later card restates an earlier model
  under the newer setup, plot the restated figure and keep the own-card figure
  in the row note.
- **ARC-AGI-3 (`arc_agi_3`)**: `series` is each model's best Standard-harness
  score, `adapter` its best Provider Adapter score (hollow, never joined), and
  `configurations` every Claude run on the board.
- **A first-party figure on a board-sourced chart** gets `"reported_by":
  "anthropic"` on its row (today: Fable 5.2 on `rli`). The chart draws it hollow
  on a dashed segment. When the board lists the model, switch `score` and
  `source` to the board's and delete the flag; the point turns solid. Its
  Board Coverage row stays `pending` until then.

## Still manual

- **Prose.** The notes under each chart, the section sub-heads and the intro
  lines in `claude-models.html` are hand-written. That includes sentences that
  hard-code a check date ("board checked November 9, 2026", "has no run yet"):
  Board Coverage updates from the JSON, those sentences do not.
- **The `lastUpdated.textContent` stamp** in `claude-models.html`.
- **Dated captions in sub-heads** ("read November 9, 2026" under ARC-AGI-3,
  "a single fit, dated November 6, 2026" under Anthropic ECI).
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
