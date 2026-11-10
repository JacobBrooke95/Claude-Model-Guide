# Learning log

What the forecaster has got wrong, what the evidence was, and what follows. Every daily run reads this first (`DAILY_RUNBOOK.md` §2). Add an entry only when it will change what a future run does. Entries are dated and never rewritten; if a lesson turns out wrong, add a new entry that says so.

A lesson is not a model change. A lesson that implies one becomes a backlog entry in `EXPERIMENTS.md` and goes through the protocol there.

## Standing rules (distilled from the entries below)

1. **The model runs low and slow.** It under-predicted through the 2025–26 holdout and on the one release graded forward. When model and market disagree and the market is higher, the record so far favours the market. Say this next to any number that is below the market's.
2. **A late signal is not a dead signal.** Sightings that go unfulfilled for weeks have, so far, been followed by the release anyway. Do not read ageing sightings as evidence against a release.
3. **Artifacts are good on existence, poor on timing, and unreliable on the name.** Version strings in catalogs, commit trailers and page headings can be working names.
4. **Dated calls miss late.** Never move toward a called date.
5. **Count release cycles, not rows.** Two blocks is two observations however many snapshots they contain.
6. **Open the primary source and record when.** A disputed sighting with no fetch time cannot be settled later.
7. **A release-day run takes the next day as its origin.** `daily.py` does this; do not override it.
8. **An unmapped target is invisible to the model.** A new `UNRELEASED …` row must be added to `LIVE` in `tools/build_signals.py`.

## 2026-11-10 — A voice-model forecast was added; what it rests on

Jacob asked for an estimate of when Anthropic ships a speech model of its own. The family engine cannot give one (no gaps to fit), so `voice.py` is a separate small model; `DAILY_RUNBOOK.md` §12 says how to run it. What a future run should know:

- **Nothing shipped so far counts.** Voice mode (2025-05-27), dictation, the July 2026 upgrade and Claude Code dictation were never announced as running on an Anthropic speech model; a spokesperson called voice mode turn-based in July 2026. The question is about the next thing, and it needs Anthropic to say the model is its own.
- **The evidence on 2026-11-10** was a research-team job posting (listed January to July 2026, gone by November), a voice-recording opt-in that reversed a no-training line (Oct 4), and a hidden "Voice / Preview" item in the web app (Oct 10, screenshot only). No first-party page, API doc, catalog row, partner test or market mentioned an audio model.
- **Every signal weight is an assumption** (`EXPERIMENTS.md` V1–V6). The honest output is the range, about one third to two thirds by the end of 2027, not the point value.
- **The standing rules apply here too**: a late signal is not a dead signal; dated tipster calls miss late; open the primary. And the family lesson about the market applies in advance: if a market on this opens, it gets most of the weight until this model has a record.
- **Could not be opened on 2026-11-10:** openai.com launch pages (403), the FT's Krieger interview (paywall), Wayback captures of the job posting (connection reset; only the availability index answered), the Metaculus API (login), Anthropic's subprocessor list (script-rendered). Rows that depend on them are marked RELAYED or APPROXIMATE.

## 2026-11-10 — Post-mortem: Claude Fable 5.2 and Mythos 5.2 (shipped 2026-11-09)

**What the forecast said.** Four snapshots were frozen before the release (Oct 30, Nov 1, Nov 2, Nov 8; versions v3c, v3d, v3e, v3e).

| Snapshot | Fable P(by Nov 9): model / market | Fable P(by Nov 30): model / market | Fable median | Nov 9 inside 80% window |
|---|---|---|---|---|
| Oct 30 | 16% / 50% | 38% / 88.5% | Dec 15 (+36 d) | yes |
| Nov 1 | 26% / 41% | 49% / 82.5% | Dec 1 (+22 d) | yes |
| Nov 2 | 20% / 41% (Nov 1 prices) | 45% / 82.5% | Dec 7 (+28 d) | yes |
| Nov 8 | 6% / 11.5% | 45% / 89% | Dec 4 (+25 d) | no (window opened Nov 10) |

The day before launch the model gave 6% for the next day; Polymarket gave 11.5%. The model never gave Fable more than 49% by Nov 30; the market was at 82–89% throughout. The market's "by Nov 9" price is the isotonic-cleaned ladder value stored in each snapshot. Mythos was the same story (8% by Nov 9 on Nov 8, median Nov 24).

**Score.** On the ten dated questions where both had a number: model Brier 0.185, market 0.010 (row counts, as the weekly note reported them). Clustered by release cycle (`SCORECARD.md`): 0.077 against 0.005 over two blocks; on the Fable/Mythos block alone 0.155 against 0.008. The Opus block is a wash. The model does beat the base rate (0.026 against 0.037 over four blocks), which is a much lower bar.

**Other calls.** Name: missed. "Claude Fable 5.5" had 85% and "5.2" 13% in every snapshot; 5.2 shipped. Co-launch with Mythos: 83%, happened. Price: 50% unchanged, 25% cut; it was cut ($10/$50 → $8/$40). SWE-bench Pro: projected 88.4 (80% range 79.3–93.9), reported 93.0, inside the range near the top.

**Which signals led, and by how long** (grade A/B rows mapped to the release): Azure catalog row `claude-fable-5-5` 27 days; `claude-onigiri-eap` 25; TestingCatalog "next week" 23; commit trailer 21; The Information (unnamed model) 20; first-party Mythos page heading 8; `claude-donut-eap` 2. Every EAP string left the Devin CLI on Nov 8, the day before launch.

**Which were noise or wrong.** Three dated calls, all late: "end of September or early October" (5–6 weeks), "next week" on Oct 17 (3 weeks), "Nov 3 or 4" (5–6 days). The name "5.5" on three artifacts. Polymarket's 79–88% on "Fable by Oct 24" two weeks earlier.

**Lessons.**

1. *The model treated ageing sightings as evidence against a release.* Each week without a launch moved the October sightings further out on a lead-time curve whose median is 5–12 days, so their weight fell and the forecast drifted down (49% → 45% by Nov 30 in the last week) while the launch got closer. The leads for this release were 20–27 days. The lead-time tail is too thin, or the model lacks the idea that a model with catalog rows and partner strings exists and will ship. The adversarial review said this on Oct 30 (finding 10): 16 of 17 releases with a named catalog, EAP or partner signal shipped within about 75 days, yet the model implied a 20–24% chance that Fable would not ship in 62. → `EXPERIMENTS.md` E2, E4.
2. *The market was closer, by a lot, in the direction the backtest predicted.* The holdout calibration intercept was +0.74 (model too low) and the README called the live Fable number "probably low" before the release. A known bias that is not corrected is a choice. → E1 (blend), E5 (pool weight).
3. *The named-version rule failed its only forward test.* 85% is a fixed weight, not a fitted one, and it was applied on the strength of a catalog row, a commit trailer and a page heading. None of those is a first-party API identifier. → E3. Until then `named_versions.json` takes a name only under the stricter rule in `DAILY_RUNBOOK.md` §3 (hygiene rule 7).
4. *EAP strings vanishing preceded the launch by a day,* as on the day Fable 5.1 shipped. But five ids were also pruned on Oct 23 with nothing for 17 days. Two hits and one miss is not a rule; it is a reason to log removals. → E6.
5. *Dated tipster calls were late three more times.* → standing rule 4, E7.
6. *The day-before forecast was structurally unable to be high.* With a Monday launch and a forecast made Sunday, 6% for "by tomorrow" is what a smooth hazard gives. Short-range sharpness needs same-day evidence (first-party page changes, EAP removals), which is what the daily sweep is for.
7. *Release-day mechanics.* The engine counts releases dated before its origin, so the post-release run had to be dated Nov 10. Done by hand then; `daily.py` now does it.
8. *One disputed grade-A row.* The Nov 1 Mythos page sighting was logged without a saved copy; a desk re-fetch on Nov 2 found no "5.5", and another site put the reversion before the logged fetch time. It was kept as logged. Every grade-A row now records its fetch time, and `tools/sweep.py` keeps the name set it saw each day.

**What the model could not have known.** The exact day. Nothing public pointed at Nov 9 over Nov 10–12; the market had 11.5% on it.

## 2026-11-08 — Fetch failures hide first-party evidence

The weekly run could not fetch the models overview, the support release notes or the Mythos page from the cloud session (permission timeouts), in the week a first-party page was the freshest evidence. A weekly look is also too coarse for artifacts that live for hours: the Azure row lasted about 28 hours and `claude-onigiri-eap` sat in the Artificial Analysis frontend for three. Consequence: the daily sweep, with every check logged including failures (`data/raw/sweep_log.csv`). On 2026-11-10 all tier-1 URLs fetched cleanly with `curl` through the session proxy.

## 2026-11-02 — The weekday profile needs calendar sense (v3e)

Before v3e the model rated Tuesday Nov 3, a US election day, as Fable's single likeliest day, because Tuesday is Anthropic's most common launch day. Polymarket's daily ladder had already priced Nov 3 well below Nov 4. Fixed as an a-priori low-hazard day. The general point: when the market's shape differs from the model's on a specific day, look for a calendar fact the model does not have (holidays, the IPO date, a competitor's event) before assuming the market is noise.

## 2026-11-01 — One class clock masked a fresh sighting (v3d)

Each signal class's clock ran from its earliest sighting, so the Oct 13 Azure row masked the Nov 1 first-party page, and live runs could not see a sighting first seen on the run date. Fixed in v3d (most recent grade A/B sighting; same-day sightings in live runs). Tested and not adopted: a separate first-party signal class, which scored slightly worse in both periods.

## 2026-10-30 — Adversarial review of the backtest (`data/raw/adversarial_review.md`)

Twelve findings; the ones that should shape daily work:

- **The only clean out-of-sample result is v1 on the lockbox, and it lost to the old EWMA model at 30 and 90 days.** Everything since was designed after seeing the lockbox. The final model ties the EWMA over the full period and loses to it in the holdout at 90 days (p = 0.006). Do not describe the model as validated.
- **Calibration has opposite signs in the two periods**: too high in 2024–25 (intercept −0.46), too low in 2025–26 (+0.74, slope 1.26). An overall slope near 1 hid this. Always look at calibration by period.
- **Signal data is hindsight.** Sightings for 2023–25 were collected after the fact, so detection rates are too high and false-alarm counts too low (one false row before 2026). That is why the absence term hurt and is off, and why the false-alarm rate has a floor. The fix is prospective logging, which the sweep log now does.
- **A single curation decision moved the headline by 7 points** (dropping one EAP row during the review). Signal mapping decisions are forecasts in disguise; record who decided what and why, in the row's note.
- **Effective sample size is 13–16 events.** Pooled significance tests overstated it. Hence blocks.
- **Config selection was mostly noise**: probability of backtest overfitting 0.83 across the 27 stage-1 configs. The gains that hold are structural (cadence over base rate, signals over none, pooling over either part). Prefer structural changes with a mechanism to parameter tuning.
- **Haiku is a known hole.** The model gives Haiku 4–5% by Dec 31 from three long gaps and has no mechanism for a lineup-wide refresh; the market says about 20%. → E9.
- **`live.py` appended duplicate log rows when run twice.** Fixed then (it refuses a second block for the same date and version); `daily.py` and `weekly.py` now also refuse to recompute a frozen origin.

## What the signal record says (from `data/raw/signals_notes.md`; current counts in `data/source_ledger.csv`)

- Specific client and partner strings are late: 0–5 days. Codenamed EAP strings run 1–29 days, and about half of codenames never map to a release.
- First-party "coming weeks" has meant 6–18 days (five cases). "Later this year" meant 124 days once and never once.
- Red-team planet codenames lead by 4–32 days: good evidence that something is coming, weak on which tier.
- Cloud catalog rows are bimodal: 0–1 day, or 16–149 days. Useless for timing alone.
- Public model IDs have never pre-staged in the SDK, the docs, Claude Code or OpenRouter (0 of 4). A null there says almost nothing.
- No Anthropic model has been documented as an anonymous arena entry.
- Launch weekdays in 2026: Tuesday dominates (6 of 12); Opus 5 was the only Friday.
- Six releases in 2023–25 have no logged signal at all. That reflects how little monitoring existed, not how Anthropic behaved.

## Post-mortem template (use on a release day)

```
## YYYY-MM-DD — Post-mortem: <model> (shipped YYYY-MM-DD)
**What the forecast said.** Table: each frozen snapshot of the cycle: P(by release day), P(by next checkpoint), median and its error, inside 80% window, market beside each.
**Score.** From SCORECARD.md: this block's Brier, model vs market vs base rate; the running totals and the number of blocks.
**Other calls.** Name, co-launch, price, SWE-bench Pro: forecast vs outcome.
**Which signals led, and by how long.** Grade A/B rows mapped to the release, with lead in days. Say which mappings are inferences.
**Which were noise or wrong.**
**Lessons.** Numbered. Each one that implies a change names its EXPERIMENTS.md entry.
**What the model could not have known.**
```
