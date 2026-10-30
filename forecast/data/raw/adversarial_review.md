# Adversarial review — Claude release-date forecaster (`forecast/`, v3b-final)

Reviewed 2026-10-30 against the code and pickles as they stood at ~09:45 CT. Everything below was checked by reading the engine and by re-running pieces of it (read-only; scratch copies only). Stored backtest values reproduce exactly with the current code (checked at origins 2025-07-07, 2026-02-02, 2026-08-31, 2025-03-10), so the pickles are a fair basis for the numbers quoted here.

Housekeeping first: running `python3 live.py 2026-10-30` as instructed appended a second, duplicate block of 7 rows (as_of 2026-10-30) to `forecast/forecast_log.csv`. The README says those rows are "never edited"; the duplicate should be removed before the log is treated as a prospective record, and `live.py` should refuse to append a second block for the same `as_of`.

Severity scale: **critical** = a headline claim is wrong or unsupported; **major** = materially changes how results should be read; **minor** = should be fixed, small effect.

---

## 1. CRITICAL — The headline "beats the old EWMA at every horizon" is an in-sample artifact; on the only holdout the final model loses at 30 and 90 days

Evidence (Brier, Opus/Sonnet/Haiku rows, from `output/lockbox_scores_v2*.pkl` and `tuning_full_scores_v2*.pkl`):

| period | h | final | EWMA (as stored) | EWMA (same-day leak fixed, §4) |
|---|---|---|---|---|
| lockbox | 7 | 0.0544 | 0.0571 | 0.0548 |
| lockbox | 30 | 0.1758 | 0.1719 | 0.1639 |
| lockbox | 90 | 0.1839 | 0.1336 | 0.1272 |
| tuning | 90 | 0.2735 | 0.4266 | 0.4175 |

`page_text.json` ("test_lede_html") says: "On Opus, Sonnet and Haiku it beats the site's earlier EWMA model at every horizon." That is true only when the tuning period (where the EWMA collapsed on the 444-day Opus gap) is pooled with the lockbox. On the lockbox, the EWMA beats `final` by 0.05 Brier at 90 days (the author's own DM test, `backtest.json` tests row 53: t = 2.58, p = 0.01 in the EWMA's favour).

A pool-weight sweep (linear pool of `sig_noabsence` and `ewma`, O/S/H) shows the chosen `w_ewma = 0.3` is the argmin on the *pooled* period only (mean Brier 0.1401 at 0.3 vs 0.1404 at 0.4). On the tuning period alone the optimum is w = 0; on the lockbox alone it is **w = 1.0 (pure EWMA)**. The weight is a compromise fitted to the whole sample, as the README admits, and is optimal for neither regime.

Fix: state the lockbox result plainly ("v3 loses to the EWMA at 30/90 d out of sample"), present the 70/30 pool as a post-hoc proposal to be judged by `forecast_log.csv`, and drop "at every horizon".

## 2. CRITICAL — The EWMA baseline (and therefore the v3 pool) is tuned in-sample on the lockbox period

`claude-models.html` lines ~2560–2580 (forecast block): "Tunables, picked by sweeping them against `predict-releases.js --backtest`" — `GAP_DECAY = 0.25`, `SPREAD_FRACTION = 0.5` ("widened Aug 2026 … ±50% catches 86%"). That backtest replays *every* release through today, i.e. it includes every lockbox release. So:

* "v1 lost to the EWMA on the lockbox" compares an out-of-sample model to a baseline whose hyper-parameters were chosen on that very period.
* v3 = 0.7·model + 0.3·EWMA imports those in-sample choices; the "post-hoc" label on v3 understates it.

Fix: either re-tune the EWMA's two constants on pre-2025-07 data only and re-run the EWMA column, or label the EWMA as an in-sample reference, not a baseline.

## 3. CRITICAL — "Well calibrated: calibration slope 1.01" hides opposite-sign biases in the two periods

Logistic recalibration of `final`, main targets (my computation from the pickles):

| period | intercept | slope | mean p | observed freq |
|---|---|---|---|---|
| lockbox (n = 945) | **+1.02** | 1.28 | 0.32 | 0.43 |
| tuning (n = 855) | **−0.59** | 0.82 | 0.31 | 0.24 |
| pooled (n = 1800) | +0.15 | 0.98 | 0.31 | 0.34 |

The pooled slope of ~1 is the average of a model that over-predicted by ~0.6 logits in 2024–25 and under-predicts by ~1 logit in 2025–26. The lockbox reliability table in `backtest.json` says the same thing bin by bin (bin 0.15–0.30 → 35% observed; 0.30–0.50 → 54%; 0.50–0.70 → 84%). By family at 90 days in the lockbox: Opus observed 0.95 vs mean forecast 0.52; "any" observed 1.00 vs 0.92.

A constant +0.7 logit shift applied to `final` on the lockbox lowers Brier from 0.197→0.178 (30 d) and 0.157→0.131 (90 d) — a larger gain than the signal layer delivers. The regime bias is the dominant error. The page's "a rolling recalibration made it worse, so none is applied" needs its details shown; a period-wise reliability diagram should replace the single slope.

## 4. MAJOR (bug) — EWMA baseline sees releases dated *on* the origin day

`scripts/predict-releases.js`, `shipped()`: `.filter(r => !cutoff || r.date <= cutoff)` — inclusive. `engine/data.py:54` uses `date < asof`, and `outcome()` counts a release on the origin day as y = 1. Five weekly origins fall on release days (2024-11-04 Haiku 3.5, 2025-02-24 Sonnet 3.7, 2025-09-29 Sonnet 4.5, 2025-11-24 Opus 4.5, 2026-09-28 Sonnet 5.5). At those rows the EWMA "knows" the release happened today and gives P(release in [t, t+7)) ≈ 0.003 against y = 1 (log-loss clipped at 9.2 each). Re-reading those five origins with `--date = origin − 1` moves the EWMA from 0.003/0.02/0.25 to 0.05–0.15 / 0.24–0.58 / 0.76–0.98 and shifts the full-period EWMA Brier at 7 d from 0.0475 to 0.0450 (final: 0.0435). The pooled `final` inherits 30% of the same leak.

Fix: call the EWMA with `--date` = origin − 1 day in `ewma_baseline()` (or make the JS filter strict and document it), then re-run the EWMA and ensemble columns.

## 5. MAJOR — Signal gains rest on hindsight-collected data; the false-alarm rate is implausibly low and contradicts the author's own notes

`data/signals.csv`: 62 of 80 signal IDs were first seen in 2026, 3 in 2024, 1 in 2023; 9 "false" rows total, 1 before 2026. Six releases in 2023–25 have no signal at all. Fitted at the live origin (`forecast.json` → `signal_class_params`): λ_infra = λ_report = 0.0005 per family-day with **n_fp = 0**; λ_client = 0.0017 with n_fp = 2. `data/raw/signals_notes.md` §9 says "roughly half of the [EAP] names never map", and §7–8 list a string of missed Fable timing calls — yet the client false-alarm count in the fit is 2 and the Fable "misses" (kimmonismus 9/5 "window passed – FALSE timing", TestingCatalog 10/17 "missed", lyra 10/15 "not shipped") are labelled `is_false = 0` and enter the live Fable likelihood as *positive* evidence (`forecast.json` → `signals.fable`).

Consequences:
* With λ ≈ 0 the likelihood ratio hits the cap of 5 for every infra/report sighting (`peak_ratio = 5.0` in the output for three of four Fable classes); the lead-time density shape is irrelevant and each class acts as a fixed ~√5 ≈ 2.2× bump after tempering, 25× in total for Fable. The cap/tempering "guards" are doing all the work.
* The lockbox "signals vs base" result (pooled DM t = −3.66 at 7 d) is not significant for any single target (per-target t between −1.2 and −2.0) and is p = 0.03 / 0.02 / 0.22 at 7/30/90 d when tested on block means (16/15/13 inter-release blocks).
* The live Fable number moved from p30 = 0.55 to 0.62 between two builds of `signals.csv` during this review (the `orzata` row was dropped at 09:41). A single curation decision moves the headline by 7 points.

Fix: (a) label timing misses as false for the purpose of λ; (b) estimate λ from a denominator the researcher actually scanned (e.g. TestingCatalog article counts per month) or set an informative prior on λ of order 0.01–0.02 per family-day; (c) report the signal layer's gain only for 2026 origins, where collection was near-contemporaneous; (d) in `SignalModel.visible()` do not let the *earliest* sighting per class define the clock (`drop_duplicates("cls")` keeps the oldest; a stale weak sighting suppressed the fresh `onigiri` string) — use the most recent grade-A/B sighting or combine them.

## 6. MAJOR — The "lockbox" was looked at 23 configurations deep, and the 59 configs tried are selected within MCMC noise

Counts from the scripts and pickles: stage 1 = 27 configs; stage 1b = 18 (12 new); `lockbox_scores_main.pkl` (the very first lockbox run, 09:20) already scored **9** configs including `signals`, `sig_rho35_cap8`, `sig_rho70_cap5`, `sig_noabsence`; `lockbox_scores_v2.pkl` 11 more; then `ensemble`, `ensemble50`, `final`. Total distinct ≈ 59; scored on the lockbox ≈ 23. The README's "v1 was scored once … the only clean out-of-sample result" is true of v1 but the signal hyper-parameters (ρ, cap, absence) were compared on the lockbox from the first look, and `final` (absence off) was chosen because it "hurt in both periods".

The stage-1 ranking (`tuning_ranking.csv`) separates #1 and #2 by 0.0008 in mean log-loss. MCMC noise is an order of magnitude larger: the sampler (`cadence.py:150–170`, 5000 iterations, 500 thinned draws) has ESS ≈ 15–70 per parameter at the live origin, and re-running v1 vs `t|linear|w0.0` on a third of the tuning origins with seeds 0/1/2 gives mean log-loss 0.381/0.385/0.386 vs 0.396/0.403/0.372 — the order flips with seed 2. The author's own CSCV gives **PBO = 0.83** for stage 1 but PBO was not computed for the stage-2 choices (signals, absence, ρ/cap, w_ewma), which is where it matters.

Fix: average ≥ 4 seeds in every backtest (as `live.py` already does) or run a proper sampler; compute PBO/deflated scores over the full set of configs actually tried; report the number of lockbox looks.

## 7. MAJOR — Structural choices use hindsight: the change-point date and the "no further acceleration" assumption

`cadence.py:76`: `BREAK = pd.Timestamp("2025-06-01")` is a fixed calendar date chosen knowing the 2025–26 record; at every origin the model asserts gaps stopped shrinking in June 2025. The actual Opus gaps after the break were 111, 73, 70, 42, 57, 59 days — still shrinking — which is why the model under-predicts (§3). `holiday_mask` (Dec 20 – Jan 4) is justified by "no release in 2023–25", i.e. the full sample. These are small leaks of structure rather than of data, but they are leaks.

Related mis-labelling: `CadencePosterior.params()` reports `exp(median mu)` as `median_gap_now_days` (Opus 92.9 d). For the Weibull error family that is the scale, not the median; the implied median is exp(μ − 0.3665σ) ≈ 79 d. The realised Opus median since mid-2025 is ~70 d. Even so, the model's Opus P(by Dec 31) = 0.68 is well under an empirical renewal estimate (6 of the last 7 Opus gaps ≤ 100 d → ~0.85) and under Polymarket's 0.885.

Fix: choose the break by marginal likelihood at each origin, or drop the change-point and keep only recency weighting; relabel the parameter; add partial pooling that does not drag Opus toward Haiku's year-long gaps (family-specific σ is implemented, `fam_sigma`, but never used).

## 8. MAJOR — The cadence layer adds little over a trivial recency baseline; "climatology" is a weak straw man

Climatology (`backtest.py:50`) is an unconditional window base rate. A Poisson baseline using the target's release count in the previous 180 days ("rr180") is one line of code and, on the lockbox, scores Brier 0.0999 / 0.2427 / **0.1848** at 7/30/90 d against the hierarchical cadence model's 0.0979 / 0.2349 / **0.2045** and climatology's 0.1019 / 0.2809 / 0.2399. The MCMC renewal model loses to the 180-day rate at 90 days. Also note the "any" target at 90 d has y = 1 in all 56 lockbox rows and "frontier" 53/56: there is nothing to discriminate, and pooling them into the main table rewards any model that says "high".

Fix: add rr180 (or an empirical-gap renewal) as the reference baseline in the score table; report per-target scores; exclude or flag targets with degenerate outcomes at a horizon.

## 9. MAJOR — Effective sample size is ~13–16 events, and the pooled significance tests overstate it

Lockbox: 16 release days; by target 7 Opus, 4 Sonnet, 2 Haiku (h = 7 positives: 7, 4, 2). Weekly 90-day windows put each event into ~13 consecutive rows, and `frontier`/`any` rows re-use the same Opus events. `dm_hac()` is run on rows stacked by (target, origin) with lag = h/7 + 1, so the HAC kernel never sees the cross-target correlation at the same origin (e.g. loss-differential correlation opus–frontier = 0.67 at 30 d). `block_bootstrap_diff()` resamples inter-release intervals, but a 90-day window spans 2–4 intervals, so blocks are not exchangeable. The block-level t-tests I ran (n = 13–16) keep the final-vs-climatology result but shrink the signals result to borderline (§5).

Fix: treat the event count as n; use blocks of ≥ h days (or one block per target-event) and drop `frontier`/`any` from pooled tests, or test per target.

## 10. MAJOR — Live numbers vs. Polymarket: Haiku and Fable are not defensible as stated

`output/forecast.json` (v3b-final, 4 seeds) vs `data/raw/markets_2026-10-30.csv`:

| | by 2026-11-30 | by 2026-12-31 | by 2027-01-31 |
|---|---|---|---|
| Fable model / market | 0.57–0.63 / 0.885 | 0.76–0.81 / 0.94 | — |
| Opus model / market | 0.42 / 0.56 | 0.68 / 0.885 | — |
| Sonnet model / market | — | 0.35 / 0.395 | 0.60 / 0.535 |
| Haiku model / market | — | **0.07 / 0.41** | **0.13 / 0.70** |

* **Haiku.** The model's 0.07 by Dec 31 comes from three gaps of 236/345/356 days. It has no mechanism for the lineup-wide refresh that just happened (Opus 5.5 → Sonnet 5.5 → Haiku 5.5 in 15 days), and the wave model, which is meant to capture that, gives Haiku *less* (0.04) because its inclusion intercept (a_haiku = −4.3) is fitted to a history in which Haiku skipped 20 of 23 waves. The Haiku market is thin (~$1.7k–2k), but a 0.07 vs 0.41 gap with the direction of every recent structural change pointing the market's way is a model problem, not a market problem.
* **Fable.** By the author's own notes, 16 of 17 releases with a named catalog/EAP/partner signal shipped within ~75 days (the lone exception being Claude 3.5 Opus). The model's 0.76–0.81 by Dec 31 implies a ~20–24% chance that a model with an Azure catalog row, EAP partners and a commit trailer does not ship in 62 days. The signal layer only reshapes *timing* against a far-future reference (`ratio` floors at 1), it never raises the probability that the model exists and will ship. The 30-point gap the README describes as "the open question" is, on the record, mostly the model being too low.
* **Opus.** Under the market by 14–20 points, consistent with the lockbox under-prediction in §3 and the pooling toward long-gap families in §7.
* Sonnet is the one family where model and market agree.

The very-short end is fine: P(Fable today) = 0.012 vs market "on Oct 30" 0.0075.

## 11. MAJOR — Statements presented as findings that the data cannot support

* **Competitor response** (`page_text.json` method_html: "Nothing in the record says Anthropic ships faster after a rival does", γ ≈ −0.17 ± 0.24). The `major21` exposure variable is 1 on 67% of all days and 77% of 2026 days; the estimate rests on 13 exposed Anthropic release days; the 90% interval on the hazard ratio is ~0.6–1.3. That is a no-power test, not evidence of no effect. `sota30` has a built-in negative correlation: a competitor can only "take SOTA" when Claude has not just shipped, so exposure is mechanically low right before Anthropic releases (7 of 23 release days exposed vs 57% of days). The label "pre-registered, fixed 2026-10-30 before any backtest was run" (`modifiers.py:29`) is same-day self-declaration; `competitor_releases.csv` was last modified at 09:27, after the first lockbox run (09:20).
* **Release parameters** (`params.py`). `generation_clock` uses `GEN_STARTS[-1] = 2026-06-09` while `anthropic_releases.csv` marks Mythos Preview (2026-04-07) as generation 5; the choice moves "elapsed" from 143 to 206 days and changes P(Claude 6 by Mar 31 2027). Student-t predictive on n = 4 gaps is labelled honestly but should carry a wide band on the page. `swe_pro_projection` pools 8 within-family logit rates (which range from 0.5 to >5 per year), assumes exchangeability across tiers and time, and projects Haiku to 90.5 SWE-bench Pro (80% band 57–99) and Opus 5.6 to 93.4 — a logit-linear extrapolation of lab-reported scores on a benchmark approaching saturation, with Anthropic-reported numbers that this reviewer cannot verify. Reporting to 0.1 is false precision; `apply_named_signals` hard-codes 0.85 on "Fable 5.5" in `live.py`, fine as a rule but it is not a model output.
* **Mythos Preview** counts as a `mythos`/`frontier`/wave release in the Python model (`access = restricted`, announcement only) but is excluded from the EWMA (`notReleased: true`). The two models being compared use different definitions of "release", and the `frontier` outcome set is made easier by including an announcement.
* **"Shipped Claude models usually follow their named sightings within about a week (median 6 days, 17 releases)"** — computed from signals found after the fact; survivorship (releases without sightings have no lead) biases this short.

## 12. MINOR — Smaller bugs and inconsistencies

* `signals.py:125` absence term uses `sf(j+1) − sf(j+since_last)`; the "already seen" event is lead ∈ (j, j + since_last), i.e. `sf(j) − …`. One-day off; absence is switched off in `final` anyway.
* `wave.py:103` draws future-wave gaps at `_trend_z(asof, asof)` while `cadence.pmf` uses the interval start; under `trend="linear"` (v1) the two layers disagree on the trend level. `wave.py:102` also redraws θ for every gap on a path, mixing parameter uncertainty into per-gap noise.
* `wave.py:155–159` keeps empty waves after 50 rejection tries and still increments `n_waves`.
* `forecast.py:123,177` picks whichever of Fable/Mythos "moved more" (max over the change) — a selection on the sign of the update that biases aggregates upward.
* `live.py` docstring says it uses the stage-1 config; it reads `tuning_v2_ranking.csv` (stage 1b).
* `run_events` crashed once (`run_main.log`) on empty inclusion rows; now guarded, but the event pickle predates the final code for some configs — re-run `--part=events` once.
* `Config.fam_sigma` exists but is never exercised in any backtest.
* `estimate_gamma` uses the in-sample cadence baseline hazard on the same release days it was fitted to, which attenuates γ toward 0 by construction.

---

## What would make this defensible

1. Re-run the EWMA column with `--date = origin − 1`; re-tune the EWMA constants on pre-lockbox data or label it in-sample.
2. Replace the single calibration slope with period-wise reliability; apply (and report) a recalibration fitted on the tuning period only, then show its lockbox effect.
3. Add the 180-day-rate baseline and per-target scores; retire `any`@90 d and `frontier`@90 d from pooled tables.
4. Average 4+ seeds in backtests; compute PBO over all ~59 configs; publish the count of lockbox looks.
5. Rebuild `signals.csv` with timing misses as false alarms and a defensible λ prior; report signal skill on 2026 origins only; use the most recent strong sighting per class.
6. Rewrite the claims: "cadence beats climatology" → "any recency-aware rate beats climatology"; "beats EWMA at every horizon" → "loses to EWMA at 30/90 d out of sample"; competitor effect → "underpowered, not tested".
7. Fix the duplicated block in `forecast_log.csv` and make `live.py` idempotent per `as_of`.
