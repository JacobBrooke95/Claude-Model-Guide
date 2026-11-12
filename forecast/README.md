# Claude release forecaster

A statistical model of when Anthropic will ship its next Claude model in each family (Opus, Sonnet, Haiku, Fable, Mythos). It gives full probability distributions over release dates, release parameters (name, price, co-launch, benchmark), a categorized registry of every input, and a rolling-origin backtest against base rates and the site's earlier EWMA model.

The results page is [`release-forecast.html`](../release-forecast.html). The old cadence view on [`claude-models.html`](../claude-models.html) stays as it was and links here.

A small embeddable version for a daily note (an iframe, or a Markdown block from `tools/widget_md.py`) is described in [`WIDGET.md`](WIDGET.md).

```
python3 daily.py [DATE] [--dry-run]  # the daily run: signals, markets, forecast, snapshot, grade, scorecard, note, page (see DAILY_RUNBOOK.md)
python3 weekly.py                 # weekly-only entry point: forecast, snapshot, grade, summary, page (see WEEKLY_RUNBOOK.md)
python3 tools/sweep.py run        # fetch the fixed sources, diff model names against the last run, log every check
python3 tools/pull_markets.py     # Polymarket + Manifold → data/raw/markets_<date>.csv
python3 tools/scorecard.py        # forward scorecard → SCORECARD.md, output/scorecard.json
python3 tools/build_ledger.py     # source reliability → data/source_ledger.csv
python3 tools/experiment.py --name X --set field=value   # one model experiment against the live config (see EXPERIMENTS.md)
python3 live.py 2026-10-30        # live forecast → output/forecast.json, appends forecast_log.csv
python3 voice.py [DATE]           # voice-model forecast → output/voice_forecast.json, its own snapshot and log (see below)
python3 run_tuning.py             # stage 1: 27 configs on tuning origins (2024-06 → 2025-06)
python3 run_tuning_v2.py          # stage 1b: recency weighting × trend × wave weight
python3 run_all.py --part=lock    # lockbox origins 2025-07 → 2026-10 (also --part=tune, --part=events)
python3 run_final.py --part=lock   # post-review backtest (also --part=tune, --part=events)
python3 score_final.py            # → output/backtest.json (score_lockbox.py is the pre-review scorer)
python3 tools/build_signals.py    # data/raw/signals_research.csv → data/signals.csv
python3 tools/build_page.py       # → ../release-forecast.html
```

Requires Python 3.10+ with numpy, scipy and pandas. Node is needed for the EWMA baseline, which runs the existing `scripts/predict-releases.js`.

## How it is run, and where its memory lives

A scheduled task starts a fresh session every day and has it follow [`DAILY_RUNBOOK.md`](DAILY_RUNBOOK.md): sweep the sources, record what was found (including "checked, nothing"), run the forecast, grade what resolved, and try at most one model experiment. On Sundays the same session also does the deeper weekly work in [`WEEKLY_RUNBOOK.md`](WEEKLY_RUNBOOK.md). The sessions remember nothing, so the repo carries the memory:

| File | What it holds | Written by |
|---|---|---|
| [`LEARNINGS.md`](LEARNINGS.md) | Dated lessons and release post-mortems, with the evidence | hand, on release days and when a run learns something |
| [`EXPERIMENTS.md`](EXPERIMENTS.md) | The prioritized backlog of model changes, the adoption rules, and the log of everything tried, including rejections | hand, one entry per experiment |
| [`SCORECARD.md`](SCORECARD.md), `output/scorecard.json` | Forward Brier and log score against the market, the old EWMA model and the base rate; calibration; name calls | `tools/scorecard.py`, every run |
| `data/source_ledger.csv` | Hits, false alarms, lead times and last-checked date per signal type and per named source | `tools/build_ledger.py`, every run |
| `data/raw/sweep_log.csv`, `data/raw/sweep/state.json` | Every source check with its result, nulls included; the model names last seen on each page | `tools/sweep.py` |
| `data/voice_signals.csv`, `data/voice_resolutions.json`, `voice_forecast_log.csv`, `history/voice_forecast_<date>.json` | The voice-model question: its evidence, its resolution, its frozen forecasts | hand (signals, resolution) and `voice.py` |
| `daily/<date>.md`, `weekly/<date>.md` | What each run found, why the numbers moved, what failed, questions for the owner | `daily.py` writes the skeleton, the session fills it in |

**The bar is the market.** The scorecard counts release cycles, not rows: forecasts of one question are averaged within a week, then per question, then per block (one family within one inter-release interval; Fable and Mythos share a block). Daily snapshots therefore do not inflate the sample. As of 2026-11-10 the forward record is four blocks, two of them with a market price, and on those the model is losing (Brier 0.077 against 0.005).

**One forecast per origin date.** `history/forecast_<date>.json` is written once. A second run the same day, by either entry point, restores it and adds no log rows. On a release day the origin is the day after the release, because the engine counts only releases dated before its origin; `daily.py` applies that rule itself.

**Model changes** go through the protocol in `EXPERIMENTS.md` and `DAILY_RUNBOOK.md` §10: one pre-declared variant, selected on the tuning period, checked for harm on the holdout and the forward snapshots, logged whatever the result, version bumped and committed separately when adopted. The holdout is never used to choose between variants. Data and parsing fixes are not model changes.

## The model, layer by layer

| Layer | What it does | Fitted from |
|---|---|---|
| **Cadence** (`engine/cadence.py`) | Hierarchical Bayesian renewal model. Log-gaps are Weibull with a family level `mu_f` partially pooled across families, a change-point trend (gaps before mid-2025 were longer), recency weighting (half-life 0.75 years, a power prior), and a right-censored open interval. Fit by adaptive Metropolis at every forecast origin. | Release dates before the origin |
| **Wave** (`engine/wave.py`) | Company-level renewal on distinct release days, plus a conditional logistic model of which families ride each wave. Captures co-launches. Tested in the backtest and given **zero weight** in the final model: it lost on both tuning and lockbox. | Same |
| **Calendar** (`engine/modifiers.py`) | Proportional-hazard multipliers. A Dirichlet-smoothed weekday profile (fitted), a Dec 20 – Jan 4 freeze and Thanksgiving Thu–Fri (factor 0.25, a priori). | Releases before the origin |
| **Competitors** (`engine/modifiers.py`) | A competitor-release hazard multiplier `exp(γ·x_t)`, pre-registered with two definitions. **Tested and excluded.** It made scores worse, and γ is slightly negative. | `data/competitor_releases.csv` |
| **Signals** (`engine/signals.py`) | Bayesian update on the date distribution from pre-release sightings in four classes (infrastructure, client strings, reports, soft). For each class: detection rate, log-normal lead-time density and false-alarm rate, all estimated from signals already resolved at the origin. The false-alarm rate has a floor of 0.01 per family-day, and grade A/B sightings take precedence. Tempered by ρ = 0.5 and capped at 5× per class. The absence-of-evidence term is **switched off** in the final model, because it hurt in both periods. | `data/signals.csv` (98 true and 9 false sightings, 2023–2026) |
| **EWMA pool** (`engine/ewma.py`) | Linear pool, 70% this model and 30% the repo's EWMA model, for Opus, Sonnet and Haiku. The EWMA window is read as an 80% interval. | — |
| **Markets** (`engine/market.py`) | Polymarket ladders, cleaned with an isotonic fit, shown beside the model. A 50/50 log-odds blend is displayed but is not the model, because markets and signals share sources. The ladder's threshold version is read from the question; a ladder about a model that has already shipped is dropped. | `data/raw/markets_<date>.csv` (latest on or before the origin) |
| **Parameters** (`engine/params.py`) | Generation clock (P(Claude 6 by date)), next-name distribution, price change, co-launch rate, SWE-bench Pro projection. | Release table, repo benchmark data |

## How the configuration was chosen

The history is kept because it changes how the scores should be read.

1. **Stage 1** compared 27 configs (3 error families × 3 trend forms × 3 wave weights) on **tuning origins only** (weekly, 2024-06-03 → 2025-06-30). The winner was v1: Weibull, linear trend, half wave.
2. v1 was scored **once** on the untouched **lockbox** (weekly, 2025-07-07 → 2026-10-26). It beat climatology but lost to the old EWMA model at 30 and 90 days on Opus, Sonnet and Haiku. It was too slow to adapt when Opus moved to a 6–8 week cadence. **This is the only clean out-of-sample result.**
3. **Stage 1b** added recency weighting. The choice was again made on tuning origins only, giving v2: Weibull, change-point, no wave, half-life 0.75 years. But v2 was designed *after* seeing the lockbox, so its lockbox score is post-hoc.
4. **v3 / final**: v2 plus signals (no absence term), linear-pooled 70/30 with the EWMA. Both choices were made looking at full-period results. Over the full backtest, the pool beats both of its parts, which is the standard forecast-combination result (Clemen 1989; Claeskens et al. 2016).
5. **Adversarial review** (an independent agent, 12 findings; `data/raw/adversarial_review.md`). Fixes: the EWMA baseline was leaking same-day releases, now called as of origin − 1. A false-alarm floor and A/B precedence in signals. Four MCMC chains averaged. A 180-day recent-rate baseline. Per-family scoring, block-level significance tests, calibration by period, and claims rewritten. Re-run as `run_final.py` → `score_final.py`. Model version `v3c-post-review`.
6. The probability of backtest overfitting (CSCV, Bailey et al.) across the 27 stage-1 configs is **0.83**. Picking among near-identical configs is mostly noise. Across the 20 configs scored on every origin it is **0.20**. The gains that hold up are structural, and none of them depend on that choice: cadence over climatology, signals over none, and pooling over either part alone.

**The only fully honest test from here is prospective.** A scheduled task runs `daily.py` every day, following `DAILY_RUNBOOK.md` (until 2026-11-10 it was weekly, with `weekly.py`). Each run freezes a snapshot in `history/`, appends its calls to `forecast_log.csv` (never edited), and grades every snapshot when a release resolves it. Results are in `output/grades.json` and the page's Track record section (raw row counts), and in `SCORECARD.md` (clustered by release cycle, against the market, the EWMA and the base rate). The model does not change during a run; it changes only through the experiment protocol, and each version is graded separately.

## The voice-model question (`voice.py`, added 2026-11-10)

A sixth question that the family engine cannot answer: when will Anthropic ship a speech model of its own? There is no cadence to fit, so `voice.py` is a separate, deliberately small model. `daily.py` runs it after the family forecast as a soft step; it never blocks the family run.

| Step | What it does | From |
|---|---|---|
| Base rate | Events per lab-year among frontier labs with an assistant and no speech model of their own yet; pooled rate 0.55 a year (7 events, 13.5 lab-years), Anthropic's own record 0.14 (none in 3.7 years); the base rate is their geometric mean, 0.28 | `data/voice_reference_class.csv` (measured; the combination is assumed) |
| Signals | Program evidence (hiring, executive statements) earns the pooled rate. Preparation signals multiply the hazard per class by cap^(ρ × grade × specificity), with the family model's cap 5 and ρ 0.5, fading over a year. A first-party "coming weeks" statement starts a second clock on the measured 6–18 day lead | `data/voice_signals.csv`, `data/voice_params.json` (weights assumed; "coming weeks" leads measured) |
| Market | Log-odds blend, 0.75 on a liquid market and 0.5 on a thin one, where a market has been mapped to a rung. None exists yet | `data/raw/markets_<date>.csv`, `market.map` in the params |
| Ladder | Rung A (any first-party speech model with outside access), B (general availability), C (native speech-to-speech); B and C are derived from A | params; criteria text is in the same file |

Output: `output/voice_forecast.json`, a frozen `history/voice_forecast_<date>.json` per origin, and `voice_forecast_log.csv` (rung × horizon, with the base-rate, after-signals, market and published numbers on each row). `SCORECARD.md` scores it as one separate block. The first forecast (2026-11-10): rung A 9% by Dec 31, 2026, 25% by Mar 31, 2027, 39% by Jun 30, 2027, 56% by Dec 31, 2027 (ranges 4–14, 11–36, 17–51, 29–68), median Oct 2027. Every weight that is assumed is listed as an open item in `EXPERIMENTS.md` (V1–V6); none can be backtested, because the event has never happened. Day-to-day handling is `DAILY_RUNBOOK.md` §12.

## v3d (2026-11-01)

Approved by Jacob after a first-party sighting: anthropic.com/claude/mythos began reading "Claude Mythos 5.5" on Nov 1. Version v3c could barely register it, for two reasons. Each signal class's clock ran from its *earliest* sighting, so the Oct 13 Azure catalog row masked the new page. And live runs couldn't see a sighting first seen on the run date. v3d changes three things in the signal layer; cadence and pooling are unchanged:

1. **Most recent sighting.** The clock for each class runs from the most recent grade A/B sighting, and lead times are estimated the same way.
2. **Same-day sightings in live runs.** Live runs count sightings first seen on the run date. Backtests keep the strict before-the-origin rule.
3. **Tested but not adopted: a separate first-party class.** Giving Anthropic's own surfaces their own class (`split_fp`) made scores slightly worse in both periods, so the option stays off.

Each change was checked on the full backtest (one chain per origin) before adoption. The most-recent rule was neutral to slightly better everywhere. Opus/Sonnet/Haiku 30-day Brier was 0.1231 vs 0.1233 in tuning and 0.1821 vs 0.1832 in the holdout. Fable/Mythos 30-day holdout Brier was 0.2182 vs 0.2219. Forward grading restarts its clock at v3d; earlier v3c snapshots stay in `history/` and are graded as v3c.

## v3e (2026-11-02)

Approved by Jacob. US federal election day (the Tuesday after the first Monday of November, even years) joins Thanksgiving and the year-end freeze as a low-hazard calendar day (×0.25). It's a prior, not a fitted effect. The one relevant case on record is 2024: Claude 3.5 Haiku shipped on Nov 4, the day before the election, and nothing shipped on the day. Before this change the model rated Tue Nov 3, 2026 as Fable's single likeliest day, because Tuesday is Anthropic's most common launch day. Polymarket's daily ladder had already priced Nov 3 well below Nov 4.

## Results (post-review, Opus/Sonnet/Haiku questions)

| | 30-day Brier, full | 30-day, holdout | 90-day, full | 90-day, holdout |
|---|---|---|---|---|
| Climatology | 0.184 | 0.226 | 0.268 | 0.265 |
| Recent rate (180 d) | 0.183 | 0.220 | 0.252 | 0.246 |
| Old EWMA (in-sample constants) | 0.162 | **0.164** | 0.270 | **0.127** |
| v1 (clean holdout) | 0.168 | 0.211 | 0.257 | 0.259 |
| Final (v3c) | **0.155** | 0.184 | **0.227** | 0.191 |

- **Final vs climatology and vs the 180-day rate:** better at 30 and 90 days, with block-level p ≤ 0.05.
- **Final vs the EWMA:** tied over the full period; the EWMA wins in the holdout (90 days, p = 0.006).
- **Calibration:** the model ran high in 2024–25 (intercept −0.46) and low in 2025–26 (+0.74, slope 1.26).
- **Dating releases:** from the day after the previous release, median absolute error is 33 days, and the 80% interval caught 86% of 22 releases.

## Known weaknesses

- **Small n.** About 23 distinct release days since 2024. The lockbox holds 16 release days and only 7 Opus releases. Overlapping weekly questions are autocorrelated. Confidence intervals resample whole inter-release blocks, but they are still wide.
- **Hindsight in the signal data.** Signals were collected after the fact for 2023–25. The detection rates are probably too high, which is why the absence term hurt and is off. False-alarm counts are surely too low before 2026.
- **Outcome-conditioned event scoring.** Scoring the forecast made "7 days before each release" conditions on the outcome. It favours any model that always says "due now", as the EWMA does when a family is overdue. Only the "day after the previous release" rows give valid coverage and PIT.
- **Regime bias.** The model under-predicted throughout the 2025–26 holdout. Its live numbers for Opus and Fable are probably low.
- **The Fable call, graded.** Fable 5.2 and Mythos 5.2 shipped on Nov 9, 2026. The last forecast before that (Nov 8) gave Fable 6% by that day and 45% by Nov 30, and its 80% window opened on Nov 10, one day late. Polymarket had 11.5% and 89%. With a thin two-release cadence, the model read the October sightings as stale; they were late, not wrong, and the market was closer. On the ten dated questions where both had a number, the model's Brier score is 0.185 and the market's 0.010.
- **Named versions can be wrong.** The next-name table gave "Claude Fable 5.5" 85% because grade A/B artifacts (an Azure catalog row, a commit trailer, a page heading) used that name. The model shipped as 5.2, which had 13%. The 85% weight is a rule, not a fitted value, and its one forward test is a miss.
- **The live Fable and Mythos calls** now rest on two gaps each (84 and 69 days), with no sightings and no market ladder for the next model. They are cadence-only numbers.
- **Release-day runs.** The engine counts only releases dated before the forecast origin. A run made on a release day therefore needs the next day as its origin, or it forecasts a release that has already happened and the snapshot gets graded as if it had been made beforehand. The Nov 9 run used a Nov 10 origin for that reason. `daily.py` now moves the origin itself; `weekly.py` run directly does not.
- **Hard-coded structure.** The change-point date (2025-06-01) and the holiday freeze were chosen knowing the full record.
- **Not modelled:** the IPO calendar (no base rate exists), the S-1's safety-gating disclosures (qualitative), compute coming online.
