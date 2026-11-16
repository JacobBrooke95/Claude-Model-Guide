# Capability model: methods

Model version `cap-v2.0`, as of 2026-11-16. Every number here is written by `python3 capability/run.py` from `capability/output/capability_forecast.json`; do not edit by hand.

**v1 was withdrawn.** An independent adversarial review of cap-v1.0 (`research/04-adversarial-review-v1.md`) found two blockers and eight major problems: the headline backtest left out its worst fold and compared against weak baselines; several benchmark predictions contradicted scores already observed; and the long-range band was an untested prior. v1's output is kept, unedited, at `history/capability_forecast_v1.0_withdrawn.json`, and its predictions stay on file marked withdrawn. Section 14 lists each finding and what changed.

## 1. What is forecast, and how far to trust each part

| Output | Status |
|---|---|
| Public ECI of the next Opus, Sonnet, Fable/Mythos (1-3 months out) | Tested on all past releases; about 2.5-3 ECI points RMSE; no better than a two-line baseline, which is its core |
| Public ECI of the next Haiku (about 8 months out) | Outside anything tested |
| Benchmark scores of the next models | Anchored on each family's last score; thinly tested (2-16 folds per benchmark) |
| AECI as printed in the model's own card | Judgement-heavy estimate from eight cards; wide band |
| Frontier to 2027-12-31 | Same code backtested at 0.5-1.5 years; one regime; few independent folds |
| Frontier beyond that, to 2030 | Scenario projection driven by stated priors |

**Primary scale.** Public ECI is the modelling scale (256 models, four years, posterior draws, refittable inputs). AECI is reported two ways: (1) 'own card', the value Anthropic will print in the model's own system card, which is what gets graded and is modelled directly; (2) the November 6 2026 scale, secondary, through a mapping.

## 2. Data

`build_data.py` writes the canonical tables under `capability/data/` and logs every rename, date conflict, merge and dropped row in `build_log.csv` (v2: every non-exact name match is logged, and dated variants of a model no longer merge into a sibling). Nothing is interpolated. Models: 256 with a public ECI plus the Claude releases Epoch does not score. Index values: public ECI with 90% credible intervals and Epoch's 500 joint posterior draws; every AECI value Anthropic has printed, by card. Benchmark scores: one row per benchmark and model in one stated configuration. Release dates for the next models come from `forecast/output/forecast.json`.

## 3. The level process

One process produces the record line for both layers of the model.

- **Fit.** Record-setting releases since Claude 3 Opus. Level now and recent slope are drawn with equal weight from three recent-trend forms: trailing-12-month line, trailing-24-month line, and the last segment of a piecewise line with unknown changepoint. v1's stacking over seven forms is gone: its weights were corner solutions that flipped between forms, and the all-history forms under-predicted in every fold.
- **Uncertainty.** Subsample bootstrap: each replicate keeps the distinct members of a with-replacement resample of models (about 63%) and one of Epoch's 500 joint posterior draws; record sets are recomputed per replicate. Slope draws outside 4-60 (recent) or 4-40 (pre-break) ECI/yr are clipped to the bound; the share is reported.
- **Paths.** From today, pace(t) = kappa x log10(compute growth) + a0 x m(t), with a scenario for m(t) drawn per path (section 10), plus a random walk whose annual sd is the sd of past 12-month frontier gains.
- **Bias term.** beta x min(h, 1.5) is added to every path, with beta estimated out of sample (section 7.2).
- **Frontier.** The running maximum held at T is max(leader's own value drawn from Epoch's posterior, line level lagged by the standing record's age + scatter).

Anthropic today: level 171.5 (168.0 to 174.9), recent slope 20.5 (16.9 to 27.4) ECI/yr, pre-break slope 15.0 (12.3 to 18.2), total slope ratio 1.37 (1.00 to 1.98). The total slope ratio above (recent / pre-break, public ECI, Anthropic) is the quantity comparable to METR's 1.9x and the card's 1.88x, which are total-slope ratios on AECI. The algorithmic multiplier m used inside the scenarios is a different quantity (it excludes the compute term) and is larger. All labs: recent slope 17.1 (14.5 to 21.0). Fitted to all-lab records; no step-up is found, so 'pre-break' pace equals the recent pace and the 'reversion' scenario coincides with 'hold' for this series.

### Was there a break?

| Series | n | BIC wt linear | hinge | jump | quadratic | Slope before | after | Ratio |
|---|---|---|---|---|---|---|---|---|
| Anthropic, public ECI | 16 | 0.00 | 0.30 | 0.01 | 0.69 | 14.41 | 23.64 | 1.64 |
| All labs, public ECI | 24 | 0.44 | 0.19 | 0.22 | 0.14 | 22.89 | 16.47 | 0.72 |
| AECI Nov 6 fit, public dates | 14 | 0.00 | 0.17 | 0.82 | 0.01 | 15.49 | 26.34 | 1.70 |
| AECI Nov 6 fit, internal dates + internal model | 15 | 0.00 | 0.94 | 0.02 | 0.04 | 15.43 | 29.19 | 1.89 |

Anthropic's public-ECI records bend upward; the all-lab frontier does not; the card's 1.88x on AECI is reproduced only with internal dates and the unreleased internal model.

## 4. Next model in a family

Next = predecessor + max(line gain, 0.3) x exp(c + s z) + measurement noise. The latent step is positive by construction (0 of 21 historical within-family steps were negative); the published score can still fall below the predecessor through measurement noise alone.

The line gain is the recent slope times the time already elapsed since the predecessor, plus the simulated path from today to the release date (drawn from the release forecaster). c and s are the median and robust sd of log(actual step / line gain) over the 21 past within-family steps: c = -0.01, s = 0.487. Measurement sd 1.88 ECI (Epoch's posterior sd for recent Anthropic models). This is the reviewer's two-line baseline with a distribution around it. Fable and Mythos are one underlying model. They are forecast as one entity, 'fable_mythos': one release-date distribution (the forecaster's Fable distribution), one ability draw, one set of benchmark predictions. Public ECI attaches to the Fable label, AECI to the Mythos label.

Offsets from the record line (pooled across families by empirical Bayes) are used only for the family paths after 2027; the next-model forecast uses the gain model. A 'record line + pooled offset' predictor was tested on all folds and is not better (see variants in the release backtest).

## 5. AECI

### Own card (primary AECI output)

gap_i = own-card AECI_i - public ECI_i (today's Epoch fit; vintage ECI is not available),
one per card that printed an own value, in card order. The gap is a property of the
card's fit (it rose from about -4 to about +4 between May and November 2026, with two
large steps that coincided with basket changes), not of the model's level, so it is
forecast as a level: the mean of the last three cards' gaps. The predictive sd is the
larger of the rolling out-of-sample RMSE of that rule and the sd of the last four gaps,
widened by sqrt(1 + 0.25 (K-1)) for K card refits before the model's own card. Steps are
not treated as iid and no upward drift is extrapolated. Eight cards: a judgement-heavy
estimate, not a tested forecast.

| Card | Model | Own-card AECI | Public ECI (today's fit) | Gap |
|---|---|---|---|---|
| opus4.8 | Claude Opus 4.8 | 155.50 | 159.94 | -4.44 |
| fable5 | Claude Mythos 5 | 161.29 | 164.13 | -2.84 |
| opus5 | Claude Opus 5 | 162.10 | 164.68 | -2.58 |
| fable5.1 | Claude Mythos 5.1 | 161.98 | 166.99 | -5.01 |
| opus5.5 | Claude Opus 5.5 | 169.36 | 168.54 | 0.82 |
| sonnet5.5 | Claude Sonnet 5.5 | 167.93 | 166.56 | 1.37 |
| haiku5.5 | Claude Haiku 5.5 | 167.11 | 160.43 | 6.68 |
| fable5.2 | Claude Mythos 5.2 | 177.12 | 173.44 | 3.68 |

Predicted gap +3.91, sd 4.32. Rolling test (each card predicted from the three before it):

| Card | Predicted gap | Actual | Error | Error of 'last gap' rule |
|---|---|---|---|---|
| Claude Mythos 5.1 | -3.29 | -5.01 | -1.72 | -2.43 |
| Claude Opus 5.5 | -3.48 | 0.82 | 4.30 | 5.83 |
| Claude Sonnet 5.5 | -2.26 | 1.37 | 3.63 | 0.55 |
| Claude Haiku 5.5 | -0.94 | 6.68 | 7.62 | 5.31 |
| Claude Mythos 5.2 | 2.96 | 3.68 | 0.72 | -3.00 |

RMSE 4.32 ('last gap' rule: 3.93). Judgement-heavy estimate with a wide band. The rolling test (five cards) has RMSE 4.3 AECI points; the Haiku 5.5 card missed by 7.6. Sonnet and Haiku own-card predictions are conditional on Anthropic printing one: the Sonnet 5 card printed no AECI. They expire unresolved if the card has none.

### November 6 scale (secondary)

A level mapping fitted on 13 Claude models (hinge above a knee, or a one-time level shift; the forecast mixes them 0.4/0.6). Leave-one-out RMSE 1.4; residual sd used 1.6. Caveats: The gap between AECI and public ECI tracks how recent the model and the fit are, not the model's level: Haiku 5.5 (ECI 160.4) printed 167.11 in its own card. A mapping in level alone under-states Sonnet- and Haiku-tier AECI by roughly 2-4 points; the residual sd is set from leave-one-out and held-out errors to cover that. The level-shift threshold is not identified between ECI 156.3 and 164.1 (no model in between). Thirteen models on one fit. Secondary quantity.

### Refits

Descriptive only in v2 (the own-card forecast no longer sums refit steps). Three of the seven card-to-card transitions are observed for Opus 5.5 alone, read from cards that state no fit; over those three refits combined, the other models moved +3.8 to +4.5 and Opus 5.5 +5.4. The two large steps coincide with basket changes, so steps are not exchangeable draws.

## 6. Benchmarks

Bounded scores follow p = (score - floor)/(ceiling - floor) = sigmoid(a (ability - D)); the ceiling is estimated (with a bootstrap interval) wherever at least four scores lie above 75% of the nominal range, otherwise the nominal ceiling is kept. Predictions are ANCHORED: the family's own last score, moved along the link by the predicted ability gain (on the logit scale for bounded scores, under a ceiling drawn from its bootstrap and never below the last score), plus step noise estimated from past within-family steps. A benchmark is published only if it is not stale (a model scored in the last six months), not saturated (best score below 90% of the ceiling), not too thin, and the anchored method is no worse than 'previous in family' in backtest.

| Benchmark | Link | Models | Ceiling | Estimated | Best observed | Backtest folds | MAE anchored | MAE v1 curve level | MAE previous-in-family | 80% coverage | Published |
|---|---|---|---|---|---|---|---|---|---|---|---|
| SWE-bench Pro | bounded | 13 | 100.00 | yes | 93.00 | 4 | 5.89 | 5.30 | 10.45 | 0.50 | yes |
| Terminal-Bench 2.1 | bounded | 10 | 100.00 | yes | 87.60 | 2 | 0.78 | 2.89 | 5.80 | 1.00 | yes |
| OSWorld | bounded | 16 | 89.50 | yes | 89.30 | 10 | 6.07 | 5.50 | 10.40 | 0.60 | yes |
| GDPval-AA v2.1 | elo | 46 | - | no | 1866.00 | 12 | 95.91 | 117.65 | 378.50 | 1.00 | yes |
| Remote Labor Index | bounded | 17 | 100.00 | no | 41.30 | 2 | 7.48 | 6.75 | 18.15 | 1.00 | yes |
| ARC-AGI-2 | bounded | 90 | 95.20 | yes | 95.00 | 16 | 12.04 | 14.99 | 26.40 | 1.00 | yes |
| Humanity's Last Exam (no tools) | bounded | 15 | 100.00 | no | 73.20 | 8 | 4.36 | 5.62 | 15.63 | 1.00 | yes |
| ForecastBench (baseline) | linear | 16 | - | no | 60.30 | 11 | 1.35 | 1.75 | 1.30 | 0.64 | no |
| Vending-Bench 2 | linear | 61 | - | no | 16484.21 | 14 | 3292.42 | 3202.24 | 2951.29 | 0.79 | no |
| METR 50% time horizon (TH1.1) | loghorizon | 20 | - | no | 718.81 | 9 | 74.74 | 73.67 | 131.10 | 1.00 | no |
| GPQA Diamond | bounded | 176 | 96.67 | yes | 96.53 | 31 | 4.30 | 3.27 | 11.38 | 0.90 | no |
| FrontierMath Tiers 1-3 | bounded | 90 | 95.09 | yes | 95.09 | 12 | 6.06 | 5.79 | 17.92 | 0.83 | yes |
| Terminal-Bench 2.0 | bounded | 32 | 100.00 | yes | 84.72 | 6 | 10.49 | 11.38 | 13.53 | 1.00 | no |
| WebDev Arena | elo | 80 | - | no | 1820.31 | 12 | 62.02 | 52.60 | 93.20 | 0.67 | yes |
| LMArena text | elo | 104 | - | no | 1538.38 | 30 | 42.28 | 42.15 | 47.84 | 0.67 | yes |
| AA Intelligence Index v5 | bounded | 31 | 100.00 | no | 64.56 | 3 | 3.49 | 3.54 | 19.51 | 1.00 | yes |
| Vals Index v2.2 | bounded | 23 | 100.00 | no | 71.31 | - | - | - | - | - | yes |

Not published:

- **ARC-AGI-3**: too thin: only 7 models with both a public ECI and a score (minimum 8).
- **ForecastBench (baseline)**: not validated: 11 folds, anchored MAE 1.35 vs previous-in-family 1.3, 80% coverage 0.64.
- **Vending-Bench 2**: not validated: 14 folds, anchored MAE 3292.42 vs previous-in-family 2951.29, 80% coverage 0.79.
- **METR 50% time horizon (TH1.1)**: stale: newest scored model was released 2026-04-07 (223 days before 2026-11-16).
- **GPQA Diamond**: saturated: every family's latest score is at or above 90% of the estimated ceiling (best 96.5, ceiling 96.7).
- **Terminal-Bench 2.0**: stale: newest scored model was released 2026-04-23 (207 days before 2026-11-16).
- **Terminal-Bench 4.0**: too thin: scores for five Claude models only, all released Sept-Nov 2026.

Saturation statements (published instead of numbers for families at the ceiling):

- SWE-bench Pro is saturating: the best score so far is 93.0 against an estimated ceiling of about 100.0. A family already within a tenth of that ceiling gets no numeric prediction: expect its next model at or just below the ceiling, with differences inside the noise. Families at or above 90%: fable.
- OSWorld is saturating: the best score so far is 89.3 against an estimated ceiling of about 89.5. A family already within a tenth of that ceiling gets no numeric prediction: expect its next model at or just below the ceiling, with differences inside the noise. Families at or above 90%: fable, opus, sonnet.
- ARC-AGI-2 is saturating: the best score so far is 95.0 against an estimated ceiling of about 95.2. A family already within a tenth of that ceiling gets no numeric prediction: expect its next model at or just below the ceiling, with differences inside the noise. Families at or above 90%: fable, opus.
- GPQA Diamond is saturating: the best score so far is 96.5 against an estimated ceiling of about 96.7. A family already within a tenth of that ceiling gets no numeric prediction: expect its next model at or just below the ceiling, with differences inside the noise. Families at or above 90%: fable, haiku, opus, sonnet.
- FrontierMath Tiers 1-3 is saturating: the best score so far is 95.1 against an estimated ceiling of about 95.1. A family already within a tenth of that ceiling gets no numeric prediction: expect its next model at or just below the ceiling, with differences inside the noise. Families at or above 90%: fable, opus, sonnet.

Pooled over benchmarks, anchored intervals cover 44% / 82% / 96% at nominal 50 / 80 / 95% (182 fold-benchmarks); the 50% intervals are stretched by 1.089. Site-chart benchmarks have few folds each: treat them as thinly tested.

## 7. Backtests

### 7.1 Claude releases, all folds

Folds are (Claude release, lead) for leads of 0, 3 and 6 months; origin = release date minus lead; everything is refitted on models released strictly before the origin. ALL folds are reported, including the first release of a family (Fable 5), which the model places on the record line. 'model' is told the release date; 'model_date_unknown' is given only the family's cadence up to the origin and is the relevant test of the live forecasts at leads above zero. A baseline is scored on every fold where it is defined (n is shown per row).

**Day-of (lead 0)**

| Method | n | Bias (actual - predicted) | MAE | RMSE | CRPS | Cov 50% | Cov 80% | Cov 95% |
|---|---|---|---|---|---|---|---|---|
| Model, date given | 21 | 0.40 | 2.12 | 2.47 | 1.53 | 0.52 | 0.86 | 1.00 |
| Baseline: previous + 12-month Anthropic slope x elapsed (date given) | 21 | 0.35 | 2.19 | 2.52 | - | - | - | - |
| Baseline: previous model in family | 20 | 6.58 | 6.58 | 8.34 | - | - | - | - |
| Baseline: previous + family's mean step | 20 | -0.99 | 4.46 | 5.94 | - | - | - | - |
| Baseline: trailing-12-month all-lab line | 21 | -3.95 | 4.22 | 5.28 | - | - | - | - |
| Baseline: all-history all-lab line | 21 | -1.91 | 2.99 | 3.88 | - | - | - | - |

**3 months ahead**

| Method | n | Bias (actual - predicted) | MAE | RMSE | CRPS | Cov 50% | Cov 80% | Cov 95% |
|---|---|---|---|---|---|---|---|---|
| Model, date given | 10 | 0.90 | 2.22 | 2.70 | 1.86 | 0.80 | 0.90 | 1.00 |
| **Model, date not given** | 9 | 0.30 | 2.15 | 2.67 | 1.91 | 0.89 | 1.00 | 1.00 |
| Baseline: previous + 12-month Anthropic slope x elapsed (date given) | 10 | 0.67 | 2.00 | 2.20 | - | - | - | - |
| Baseline: same, date not given | 9 | 0.06 | 2.33 | 2.61 | - | - | - | - |
| Baseline: previous model in family | 9 | 9.56 | 9.56 | 11.20 | - | - | - | - |
| Baseline: previous + family's mean step | 9 | 1.69 | 4.26 | 5.83 | - | - | - | - |
| Baseline: trailing-12-month all-lab line | 10 | -4.66 | 4.95 | 6.02 | - | - | - | - |
| Baseline: all-history all-lab line | 10 | -1.36 | 4.11 | 4.71 | - | - | - | - |

**6 months ahead**

| Method | n | Bias (actual - predicted) | MAE | RMSE | CRPS | Cov 50% | Cov 80% | Cov 95% |
|---|---|---|---|---|---|---|---|---|
| Model, date given | 4 | 2.85 | 3.30 | 3.78 | 2.76 | 0.75 | 1.00 | 1.00 |
| **Model, date not given** | 3 | 5.34 | 5.34 | 5.71 | 3.52 | 0.33 | 1.00 | 1.00 |
| Baseline: previous + 12-month Anthropic slope x elapsed (date given) | 4 | 2.39 | 3.18 | 3.63 | - | - | - | - |
| Baseline: same, date not given | 3 | 4.64 | 4.64 | 5.25 | - | - | - | - |
| Baseline: previous model in family | 3 | 17.63 | 17.63 | 17.63 | - | - | - | - |
| Baseline: previous + family's mean step | 3 | 8.67 | 8.67 | 9.05 | - | - | - | - |
| Baseline: trailing-12-month all-lab line | 4 | -4.61 | 6.60 | 7.51 | - | - | - | - |
| Baseline: all-history all-lab line | 4 | -0.39 | 5.24 | 5.36 | - | - | - | - |

Paired differences in absolute error (model minus baseline; negative = model better), bootstrap 90% interval over folds:

| Lead (yr) | Date | Baseline | n | MAE model | MAE baseline | Difference | 90% low | 90% high | Folds model better |
|---|---|---|---|---|---|---|---|---|---|
| 0.00 | given | prev_plus_slope | 21 | 2.12 | 2.19 | -0.08 | -0.32 | 0.17 | 14 |
| 0.00 | given | prev_in_family | 20 | 2.03 | 6.58 | -4.55 | -6.43 | -2.91 | 18 |
| 0.00 | given | family_mean_step | 20 | 2.03 | 4.46 | -2.43 | -4.00 | -1.07 | 13 |
| 0.00 | given | trailing_12m_linear | 21 | 2.12 | 4.22 | -2.11 | -3.33 | -1.02 | 15 |
| 0.00 | given | all_history_linear | 21 | 2.12 | 2.99 | -0.88 | -1.75 | -0.05 | 13 |
| 0.25 | given | prev_plus_slope | 10 | 2.22 | 2.00 | 0.22 | -0.41 | 0.90 | 4 |
| 0.25 | given | prev_in_family | 9 | 2.15 | 9.56 | -7.41 | -10.45 | -4.43 | 9 |
| 0.25 | given | family_mean_step | 9 | 2.15 | 4.26 | -2.11 | -4.39 | 0.06 | 5 |
| 0.25 | given | trailing_12m_linear | 10 | 2.22 | 4.95 | -2.73 | -4.32 | -1.14 | 7 |
| 0.25 | given | all_history_linear | 10 | 2.22 | 4.11 | -1.88 | -2.90 | -0.74 | 8 |
| 0.25 | not given | prev_plus_slope_date_unknown | 9 | 2.15 | 2.33 | -0.17 | -0.94 | 0.67 | 5 |
| 0.50 | given | prev_plus_slope | 4 | 3.30 | 3.18 | 0.12 | -0.61 | 1.23 | 3 |
| 0.50 | given | prev_in_family | 3 | 2.54 | 17.63 | -15.09 | -16.20 | -13.98 | 3 |
| 0.50 | given | family_mean_step | 3 | 2.54 | 8.67 | -6.13 | -7.45 | -4.81 | 3 |
| 0.50 | given | trailing_12m_linear | 4 | 3.30 | 6.60 | -3.30 | -6.37 | -0.26 | 3 |
| 0.50 | given | all_history_linear | 4 | 3.30 | 5.24 | -1.94 | -4.34 | 0.53 | 3 |
| 0.50 | not given | prev_plus_slope_date_unknown | 3 | 5.34 | 4.64 | 0.70 | 0.24 | 1.17 | 1 |

**Verdict.** On all folds the model's point forecast is not distinguishable from 'previous-in-family + trailing-12-month Anthropic record slope x elapsed time' at any lead (every paired interval spans zero, or favours the baseline). That baseline is therefore the core of the model: next = predecessor + recent record-line gain. What the model adds is a predictive distribution with tested coverage, a positive-step constraint, and consistency with the long-range paths. It does clearly beat 'previous model in family', 'family mean step' and the two all-lab trend lines.

**What the sample supports.** Lead 0 (n=21) supports an error of roughly 2.5 ECI points RMSE with the date known. Three months ahead (n=10, 9 with the date unknown) supports 'about the same, perhaps 3'. Six months ahead (n=4, 3 date-unknown) supports nothing firmer than 'errors of 4-6 points happened and every one was an under-prediction'. No fold has a lead beyond six months: the Haiku forecast (median lead about eight months) is outside anything tested.

Within-family steps: 21 observed, 0 negative, smallest +0.86. Variants tested on the same folds (no bias term; no step ratio; record line + pooled family offset; a stacked mix of the two) are in the JSON; none is better beyond noise. Monte Carlo noise: a second seed gives RMSE 2.46 vs 2.47 at 0.0 yr, 2.83 vs 2.7 at 0.25 yr, 3.59 vs 3.78 at 0.5 yr.

### 7.2 The projection code itself

The projection code itself (level.LevelProcess.paths, central scenario weights) run at monthly historical origins and scored on the running-max public ECI 0.5, 1.0 and 1.5 years later. 'bias_corrected' adds beta*h with beta learned only from folds whose target precedes the origin. Calibration factors are learned the same way and applied to the published bands. Folds overlap heavily; origins span 2024-07 to 2026-05, one regime of rising pace. The scenario weights are today's prior, so this is not a test of the weights.

**Anthropic frontier** (30 folds from 16 origins)

| Horizon (yr) | Variant | n | Bias | MAE | RMSE | CRPS | Cov 50% | Cov 80% | Cov 95% |
|---|---|---|---|---|---|---|---|---|---|
| 0.50 | raw | 16 | 3.74 | 3.74 | 4.04 | 2.35 | 0.31 | 1.00 | 1.00 |
| 0.50 | bias_corrected | 16 | 3.07 | 3.07 | 3.46 | 2.03 | 0.56 | 1.00 | 1.00 |
| 1.00 | raw | 10 | 6.30 | 6.30 | 6.55 | 3.91 | 0.30 | 1.00 | 1.00 |
| 1.00 | bias_corrected | 10 | 6.30 | 6.30 | 6.55 | 3.91 | 0.30 | 1.00 | 1.00 |
| 1.50 | raw | 4 | 8.43 | 8.43 | 8.81 | 5.26 | 0.25 | 1.00 | 1.00 |
| 1.50 | bias_corrected | 4 | 8.43 | 8.43 | 8.81 | 5.26 | 0.25 | 1.00 | 1.00 |

Bias slope beta = 6.24 ECI/yr (block-bootstrap se 1.14 over 3 half-year blocks; se used 3.12). Rolling test on folds with at least six earlier folds: MAE 4.62 raw, 1.95 corrected. The term beta*min(h, 1.5) is applied with mean = shrunk estimate only where the rolling (out-of-sample) correction lowered MAE; otherwise its mean is 0 and only its uncertainty is carried. Used: mean 4.99, sd 3.12. Calibration factors (50/80/95%) by horizon: 0.5 yr: 1.0/1.0/1.0; 1.0 yr: 1.381/1.0/1.0; 1.5 yr: 1.0/1.0/1.0.

**All-lab frontier** (51 folds from 23 origins)

| Horizon (yr) | Variant | n | Bias | MAE | RMSE | CRPS | Cov 50% | Cov 80% | Cov 95% |
|---|---|---|---|---|---|---|---|---|---|
| 0.50 | raw | 23 | 2.51 | 3.41 | 4.34 | 2.32 | 0.83 | 1.00 | 1.00 |
| 0.50 | bias_corrected | 23 | 0.33 | 4.47 | 5.13 | 2.83 | 0.65 | 0.91 | 1.00 |
| 1.00 | raw | 17 | 2.91 | 4.95 | 5.85 | 3.83 | 0.88 | 1.00 | 1.00 |
| 1.00 | bias_corrected | 17 | -0.35 | 8.19 | 9.28 | 5.89 | 0.59 | 0.76 | 0.94 |
| 1.50 | raw | 11 | 7.39 | 8.90 | 9.80 | 6.68 | 0.82 | 1.00 | 1.00 |
| 1.50 | bias_corrected | 11 | 7.39 | 8.90 | 9.80 | 6.68 | 0.82 | 1.00 | 1.00 |

Bias slope beta = 4.22 ECI/yr (block-bootstrap se 2.63 over 4 half-year blocks; se used 2.63). Rolling test on folds with at least six earlier folds: MAE 1.66 raw, 6.63 corrected. The term beta*min(h, 1.5) is applied with mean = shrunk estimate only where the rolling (out-of-sample) correction lowered MAE; otherwise its mean is 0 and only its uncertainty is carried. Used: mean 0.0, sd 2.63. Calibration factors (50/80/95%) by horizon: 0.5 yr: 1.0/1.0/1.0; 1.0 yr: 1.0/1.225/1.01; 1.5 yr: 1.0/1.0/1.0.

The process under-predicted both frontiers in this window. For Anthropic the out-of-sample correction helped and is applied; for all labs it made things worse, so only its uncertainty is carried. 80% and 95% bands covered; the 50% band was too narrow around a biased median, which is what the 50% factor at one year repairs. 'bias_corrected' equals 'raw' at 1.0 and 1.5 years because no fold at those horizons has six earlier resolved folds: the correction is untested there.

### 7.3 Leave-future-out IRT refit

Own least-squares 2PL refit of Epoch's benchmark-level inputs, refitted at every fold origin on models released on or before that date, mapped to ECI units by a monotone alignment to the published ECI of those same models. The release backtest is rerun with history from the origin's vintage and the target's actual from the release date's vintage. The fit is deterministic; the vintages are stored in data/irt_vintages.csv.gz, which is committed and covered by the input hash (run.py --full rebuilds it; a test recomputes two vintages and compares). In v1 a date-rounding slip excluded the target from its own vintage on a clean cache, which is why the reviewer's clean run found 18 folds instead of 33. Fixed (tolerance on 'on or before'); numbers below are from a clean rebuild.

Reproduction on all data: correlation 0.9973 with Epoch's ECI, RMSE 0.67 above ECI 140. Target shift, vintage vs published: mean absolute 0.84, max 2.59 over 35 folds.

| Lead (yr) | Method | n | RMSE vintage | RMSE published | Bias vintage | Bias published |
|---|---|---|---|---|---|---|
| 0.0 | model | 21 | 2.72 | 2.47 | 0.58 | 0.40 |
| 0.0 | prev_plus_slope | 21 | 3.32 | 2.52 | 0.72 | 0.35 |
| 0.25 | model | 10 | 2.43 | 2.70 | 0.53 | 0.90 |
| 0.25 | prev_plus_slope | 10 | 3.19 | 2.20 | 1.03 | 0.67 |
| 0.5 | model | 4 | 4.08 | 3.78 | 2.77 | 2.85 |
| 0.5 | prev_plus_slope | 4 | 4.32 | 3.63 | 2.75 | 2.39 |

Scores in Epoch's input file are today's collection; a score measured after the origin for a model released before it cannot be removed (no timestamps).

## 8. Calibration

Conformal-style: per nominal level, the factor by which an interval must be stretched about its median to cover the stated share of backtest outcomes, learned from earlier folds when scoring and from all folds for the live forecast; floored at 1.

| Set | Folds | Raw 50% | Raw 80% | Raw 95% | Factor 50% | 80% | 95% | 80% factor before floor |
|---|---|---|---|---|---|---|---|---|
| Ability, date given, lead 0 | 21 | 0.52 | 0.86 | 1.00 | 1.00 | 1.00 | 1.00 | 0.81 |
| Ability, date not given, 3-6 months | 12 | 0.75 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.51 |
| Benchmarks, anchored, pooled | 182 | 0.44 | 0.82 | 0.96 | 1.09 | 1.00 | 1.00 | 0.97 |

For ability the raw intervals already cover at or above nominal on all folds, so the factors are 1 and calibration changes nothing there. That is a statement about the folds we have, not about longer leads. The frontier bands use the factors in 7.2.

## 9. Next-model predictions

Each draw takes a release date from the release forecaster, the record-line gain from the shared level paths (scenario mixture, central weights, bias term included), a positive step and measurement noise. Anthropic's Fable 5.2 card prints an unreleased internal model at AECI 178.78 (15 benchmarks); it is not used in the fit.

| Next model | Release (median, 10-90%) | Predecessor ECI | Public ECI (80%) | 95% | AECI own card (80%) | AECI Nov 6 scale (80%) | P(below predecessor) | Lead within tested range |
|---|---|---|---|---|---|---|---|---|
| Claude Opus 5.6 | 2026-12-14 (2026-11-20 to 2027-02-22) | 168.54 | 174.2 (170.1 to 182.3) | 168.3 to 190.8 | 178.5 (171.6 to 188.2) | 180.1 (173.9 to 190.7) | 3.0% | yes |
| Claude Sonnet 5.6 | 2027-01-21 (2026-12-01 to 2027-04-02) | 166.56 | 173.8 (168.8 to 184.2) | 166.9 to 195.2 | 178.2 (170.5 to 190.1) | 179.7 (172.7 to 192.4) | 1.9% | yes |
| Claude Haiku 6 | 2027-07-13 (2027-02-03 to 2027-11-23) | 160.43 | 177.4 (166.1 to 202.9) | 162.8 to 230.1 | 181.8 (168.1 to 208.4) | 183.5 (170.4 to 213.1) | 0.4% | no |
| Claude Fable / Mythos 5.3 | 2027-02-02 (2026-12-14 to 2027-04-13) | 173.44 | 179.2 (174.5 to 188.4) | 172.7 to 198.1 | 183.5 (175.9 to 194.5) | 185.6 (178.7 to 197.8) | 4.7% | yes |

Benchmarks (median, 80% interval; 'saturated' = statement only; '-' = no current anchor):

| Benchmark | Opus | Sonnet | Haiku | Fable / Mythos |
|---|---|---|---|---|
| SWE-bench Pro | 94.3 (90.5 to 97.6) | 90.4 (83.4 to 96.7) | 91.6 (76.0 to 99.4) | saturated |
| Terminal-Bench 2.1 | 91.4 (87.6 to 95.9) | 89.5 (84.0 to 95.5) | - | 93.6 (88.0 to 97.3) |
| OSWorld | saturated | saturated | 87.7 (80.2 to 89.4) | saturated |
| GDPval-AA v2.1 | 2127 (1917 to 2499) | 2168 (1921 to 2638) | 2395 (1877 to 3559) | 2094 (1863 to 2519) |
| Remote Labor Index | 40.6 (22.4 to 73.1) | - | - | 64.2 (41.6 to 89.4) |
| ARC-AGI-2 | saturated | 93.7 (86.9 to 95.1) | 94.7 (84.7 to 95.2) | saturated |
| Humanity's Last Exam (no tools) | 75.1 (66.4 to 86.4) | 71.7 (60.8 to 86.6) | 79.2 (57.9 to 97.3) | 82.1 (74.3 to 91.4) |
| FrontierMath Tiers 1-3 | saturated | saturated | 93.6 (85.7 to 95.0) | saturated |
| WebDev Arena | 1927 (1821 to 2087) | 1922 (1801 to 2119) | - | 1982 (1866 to 2162) |
| LMArena text | 1552 (1503 to 1617) | 1518 (1465 to 1595) | 1506 (1422 to 1670) | 1591 (1539 to 1662) |
| AA Intelligence Index v5 | 72.8 (54.2 to 88.7) | 72.3 (52.5 to 90.0) | 76.4 (45.6 to 97.8) | 77.3 (59.5 to 91.5) |
| Vals Index v2.2 | 78.0 (62.8 to 89.4) | 80.3 (65.4 to 91.6) | 81.9 (61.5 to 96.5) | 79.1 (64.0 to 90.4) |

## 10. Projection to 2030

Up to 2027-12-31 the bands rest on a backtest of this same code (Anthropic frontier: 16 folds at 0.5 yr, 10 at 1.0, 4 at 1.5, from 16 monthly origins in one regime). Beyond it they are a scenario projection driven by the stated priors: read each scenario path separately and treat the mixture as a summary of the prior.

### Scenarios

| Scenario | Definition | Anthropic ECI pts/yr 2027 (80%) | 2028 | 2030 | Share of paths below pre-break pace, 2027 | Frontier, end-2030 (median) |
|---|---|---|---|---|---|---|
| slowdown | Below pre-break pace. Training-compute growth follows the 'low' driver path (2.5x, 2x, 1.5x, 1.5x per year 2027-30) and the algorithmic multiplier falls to 0.4-0.9 of its pre-break value within a year. | 12.7 (10.4 to 15.8) | 8.20 | 7.10 | 0.85 | 216.70 |
| reversion | The 2025-26 step-up was one-off. Pace returns within six months to 0.85-1.15x the pre-break slope (centred on it, so about half these paths run below pre-break pace), then follows the 'central' compute path down. | 15.9 (13.0 to 19.3) | 14.10 | 12.30 | 0.28 | 235.70 |
| hold | The recent trend holds: the algorithmic multiplier stays where the recent slope puts it; compute follows the 'central' driver path (5x, 4x, 3x, 2.5x). | 20.6 (16.8 to 27.3) | 19.70 | 17.90 | 0.00 | 257.50 |
| compounding | AI R&D feedback: the algorithmic multiplier doubles every 6-12 months until it reaches 4-7.5x, then stays; 60-100% of the excess over 'hold' is realised; compute on the 'central' or 'high' path. | 30.1 (22.8 to 41.1) | 44.40 | 46.80 | 0.00 | 348.60 |
| explosive | Bounded explosive tail: the multiplier doubles every 3-6 months to a peak of 8-30x, holds 1-2 years, then settles at 3-6x; same 60-100% realisation haircut. | 50.1 (33.7 to 78.9) | 107.90 | 44.10 | 0.00 | 482.00 |

### Weights

priors. 'central' is the author's judgement; 'sceptic' and 'accelerationist' bracket it; 'unweighted_evidence_average' is an unweighted average of three unlike data-based numbers, shown for transparency, not an estimate.

| Weighting | Slowdown | Reversion | Hold | Compounding | Explosive |
|---|---|---|---|---|---|
| central | 0.12 | 0.28 | 0.38 | 0.16 | 0.06 |
| sceptic | 0.25 | 0.42 | 0.26 | 0.06 | 0.01 |
| accelerationist | 0.00 | 0.15 | 0.35 | 0.30 | 0.20 |
| unweighted_evidence_average | 0.00 | 0.35 | 0.46 | 0.19 | 0.00 |

Why the central prior looks as it does. For reversion or slower (40%): the all-lab frontier shows no break; the AECI result depends on the link function and on unreleased models; compute growth cannot stay at 5x/yr; scenario-style forecasts have run at 60-75% of predicted pace. For hold (38%): Anthropic's public-ECI records do bend, and the two earlier breaks in the reference class both persisted for a year or more. For compounding and explosive (22%): Anthropic's S-1/A says the AI R&D threshold is met on the 'expect' prong; point forecasters have under-predicted benchmark progress. The unweighted evidence average: Three numbers that span 0.01 to 0.86 are averaged with equal weight; slowdown and explosive are zero only because the sample contains no such episode. Not an estimate.

### Results (central weights; mixture bands calibrated)

| Date | Anthropic frontier, public ECI (80%) | 95% | All-lab frontier (80%) | AECI Nov 6 scale, secondary (80%) | Median beyond measured scale | Share of paths beyond it |
|---|---|---|---|---|---|---|
| 2026-12-31 | 174.6 (171.8 to 178.1) | 170 to 180 | 175.8 (173.3 to 178.9) | 180.3 (177.1 to 186.5) | no | 0% |
| 2027-12-31 | 197.5 (187.2 to 214.9) | 182 to 234 | 198.7 (188.0 to 219.4) | 205.5 (192.5 to 229.2) | no | 19% |
| 2028-12-31 | 218.2 (200.6 to 268.1) | 193 to 349 | 219.8 (203.8 to 274.3) | 228.8 (207.0 to 290.0) | yes | 76% |
| 2029-12-31 | 235.1 (210.3 to 322.0) | 200 to 460 | 237.5 (215.0 to 339.2) | 247.4 (217.5 to 350.7) | yes | 93% |
| 2030-12-31 | 251.2 (218.9 to 374.5) | 206 to 520 | 254.7 (225.5 to 405.2) | 265.5 (227.1 to 408.6) | yes | 97% |

**Measured scale.** Public ECI at which the second-hardest discriminating benchmark (slope >= 0.04) in Epoch's current basket is 90% solved (difficulty + 2.2/slope from Epoch's item parameters). Above it at most one benchmark still separates models, so ECI values are extrapolations of the scale itself, not measurements. Bands above this line are kept in the data and flagged; the page should shade them and need not draw above display_cap_eci. Threshold: 207.6; display cap 230.

### Sensitivity to the prior

| Weighting | Date | Median | 80% low | 80% high |
|---|---|---|---|---|
| central | 2027-12-31 | 198 | 187 | 215 |
| central | 2028-12-31 | 218 | 201 | 268 |
| central | 2030-12-31 | 251 | 219 | 374 |
| sceptic | 2027-12-31 | 195 | 186 | 207 |
| sceptic | 2028-12-31 | 212 | 197 | 236 |
| sceptic | 2030-12-31 | 238 | 212 | 284 |
| accelerationist | 2027-12-31 | 203 | 190 | 229 |
| accelerationist | 2028-12-31 | 236 | 208 | 336 |
| accelerationist | 2030-12-31 | 293 | 234 | 488 |
| unweighted_evidence_average | 2027-12-31 | 198 | 188 | 212 |
| unweighted_evidence_average | 2028-12-31 | 219 | 203 | 255 |
| unweighted_evidence_average | 2030-12-31 | 253 | 227 | 348 |

### Research note 1's central path

Research note 1's central path (17, 17, 16, 15 ECI/yr) is the all-lab frontier continuing at Epoch's reasoning-era slope. For the all-lab series that is our 'hold' and 'reversion' scenarios, which land near it. Our medians are higher for three reasons, in order of size: the Anthropic series has a steeper recent slope than the all-lab series, and Anthropic currently holds the frontier; some prior weight sits on accelerating scenarios; and an explicit under-prediction term is carried where it helped out of sample. Note 1: +65, about 238 by end-2030. Ours, all-lab: slowdown 220, reversion 242, hold 259, compounding 374, explosive 589; mixture median 255.

### Time horizon

No hours series is published. METR's last measurement is 17.4 hours (Claude Mythos Preview, April 2026) and METR calls estimates above 16 hours unreliable; the fitted link (about 4.75 ECI points per doubling) has no model above public ECI 157.8. Every released frontier model since then, and every projected value, lies beyond that range, so any hours figure would be extrapolation. Qualitatively: if the link held, each further 5 ECI points would double the horizon.

### Against external forecasts

| Source | Quantity | Theirs | Ours | Why they differ |
|---|---|---|---|---|
| FutureSearch (2026-11-14) | Rise in the highest public ECI held by OpenAI/Anthropic/GDM during 2029 | p10 11.7, p25 18.5, p50 27.3, p75 42.7, p90 74 | p10 9.3, p25 13.5, p50 18.5, p75 29.1, p90 66.7 | Same right-skewed shape. Ours is lower in the middle because the central compute path slows by 2029. |
| Ho et al., Rosetta Stone naive extrapolation (2025-10; conversion approximate) | All-lab public ECI frontier, Oct 2028 | ~189 (182-196) | median 215.1 (80% 200.6 to 259.1) at 2028-09-30 | Rosetta extrapolates the 2023-25 slope; the frontier is already about 8 ECI above that line. |
| Epoch AI trend (not a forecast), Nov 2026 | All-lab frontier at 16.6 ECI/yr (14.6-18.7) | straight line reaches 242 at end-2030 | all-lab median 254.7 at 2030-12-31 | See the reconciliation with research note 1. |
| AI Futures Project milestones (Automated Coder mid-2028 / mid-2030; SAR 2027 under a held 1.7-1.9x trend) | Capability milestones from a takeoff model | dates of qualitative milestones | no equivalent output | v1 translated ECI into METR-style hours to compare; that translation extrapolated two orders of magnitude beyond METR's measurements and has been withdrawn. The 'compounding' and 'explosive' scenarios are the nearest analogue. |

## 11. Assumptions that are not estimated

| Assumption | Value | Source |
|---|---|---|
| Residual distribution | Student-t, 4 df | robustness choice |
| Floor on trend residual scale | 0.75 ECI | Epoch posterior sd at the frontier is 1-2 points |
| Recent-trend forms and their weights | three forms, equal | review decision; all-history forms under-predict |
| Bias term cap | 1.5 years | longest backtested horizon |
| Bias se floor | half the estimate | 3-4 independent blocks |
| Gain floor; log-ratio sd floor | 0.3 ECI; 0.25 | keep the multiplicative step defined |
| ECI per 10x compute | 9 +/- 2 | research note 1 |
| Compute growth paths | low / central / high | `driver_scenarios_2026_2030.csv` |
| Multiplier ranges per scenario; 60-100% realisation haircut | scenario table | research note 3; AI 2027 ran at 58-75% of pace |
| Scenario weights | table above | prior |
| Own-card gap rule and its widening with refits | mean of last three; sqrt(1 + 0.25(K-1)) | judgement |
| Mapping-form probability clip | 0.2 to 0.8 | 13 points cannot exclude either form |
| Saturation and staleness thresholds | 90% of ceiling; six months | review decision |
| Family offset drift (post-2027 family paths) | 1.5 ECI per sqrt(year) | judgement |
| Fable = Mythos | identical | Anthropic |

## 12. Limitations

- Small samples: 25 Claude models with a public ECI, 21 within-family steps, 8 own-card AECI values, 13 models linking AECI to ECI.
- The next-model point forecast is, in effect, 'predecessor + recent record-line slope x elapsed time'. Nothing more elaborate tested better.
- Backtest evidence stops at six months ahead (4 folds; 3 with the date unknown, all under-predictions). Haiku's forecast is beyond it.
- All backtest folds lie in 2024-26, one regime of rising pace. Every method under-predicted in it.
- Beyond about 1.5 years the bands are a scenario projection driven by stated priors, not a validated forecast.
- Above public ECI ~208 today's benchmark basket no longer identifies the scale; values there are flagged, not meaningful measurements.
- Both indices are re-estimated on every update. AECI rests on first-party internal benchmarks; own-card predictions are judgement with a wide band.
- Benchmark predictions are anchored on each family's last score; families near a ceiling get a saturation statement instead.
- Release dates come from the site's release forecaster; its errors pass straight through.
- The model cannot see regime changes it has no data on (new architectures, export controls, a compute shock, a pause).
- Machine-backtest folds overlap (monthly origins, horizons up to 1.5 years): 30 Anthropic folds are about three independent half-years.
- The scenario weights used in the backtest are today's prior; the backtest tests the code and the bias, not the weights.
- Links use ability point estimates and, for site charts, Claude models only. OSWorld mixes three eval versions; HLE and SWE-bench Pro are first-party.
- Public ECI for past models is today's fit (the vintage check suggests this matters little).

## 13. What would change the forecast

- The next two Anthropic record-setters: near the 20-25 ECI/yr line supports 'hold'; two near 15 shifts weight to reversion.
- Epoch scoring more of Fable 5.2 (19 benchmarks so far): it anchors the level and every Fable/Mythos prediction.
- The next card's own-card gap: it is the whole basis of the AECI forecast.
- Other labs' frontier bending upward would weaken the 'no industry-wide break' evidence.
- New, harder benchmarks entering Epoch's basket would raise the measured-scale ceiling.
- Delivered compute against the S-1 commitments; export restrictions.

## 14. What the review changed

| Finding | Issue | Disposition | What was done |
|---|---|---|---|
| B1 | Headline backtest omitted the worst fold; strawman baselines | fixed | Every table is on all folds (Fable 5 included; a first-of-family release is placed on the record line). The reviewer's baseline is a named baseline with paired differences and bootstrap intervals. 'Beats every baseline' is withdrawn: the model is not distinguishable from previous-in-family + trailing-12-month slope, which is now its core. |
| B2 | Benchmark predictions contradicted observed scores | fixed | Ceilings are estimated where the data allow; predictions are anchored on the family's own last score; saturated, stale and thin benchmarks are dropped with reasons; a family already within a tenth of the ceiling gets a saturation statement instead of a number; tests check every open prediction against observed scores. |
| M1 | Corner-solution stacking; the two layers disagreed | fixed | Stacking is gone. One level process (equal weights over three recent-trend forms; no all-history forms) feeds both the next-model layer and the projection from the same simulated paths. |
| M2 | The 2027-30 band was an untested prior | partly | The projection code is now backtested at 0.5, 1.0 and 1.5 years on both frontiers, its bias term is estimated out of sample and carried with uncertainty, and its calibration factors are applied. The all-lab frontier is fitted to all-lab data. A below-pre-break scenario exists. Beyond 1.5 years nothing can be tested: those bands remain a prior and are labelled as such; values above the measured scale are flagged. |
| M3 | Implied METR horizon was false precision | fixed | The hours series and the work-month / work-year probabilities are removed; a qualitative statement replaces them. |
| M4 | AECI layer | partly | Own-card AECI is modelled directly from the eight own-card values and labelled a judgement-heavy estimate; refit steps are no longer summed as iid draws; Sonnet/Haiku predictions are marked conditional. It is still eight cards: the rolling test is poor and is reported. |
| M5 | Twins and grading | fixed | Fable and Mythos are one entity. Unresolvable predictions are pruned; grade.py has an expiry rule and grades against the first published value. |
| M6 | Regression odds contradicted the record | fixed | Positive-step model; implied P(regression) is reported per entity and is a few percent, from measurement noise only. |
| M7 | Section 7.4 not reproducible | fixed | Root cause was a date-rounding bug that dropped the target from its own vintage on a clean cache. Fixed; vintages are committed, hashed and tested. |
| M8 | Live leads untested; calibration a no-op | partly | The date-unknown variant is the headline for leads above zero and the limits of n are stated. Ability calibration factors are still 1: raw coverage on all folds is at or above nominal, so there is nothing to widen. That is a finding, not an omission; the frontier bands do get non-trivial factors. Haiku's eight-month lead remains untested and is flagged in the output. |
| minor | Name-matcher merges | fixed | Dated variants no longer merge into siblings; explicit aliases for Claude 3.5 Sonnet (Oct/Jun); every non-exact match is logged. |
| minor | Bootstrap was a subsample; slope draws truncated | fixed | Called a subsample bootstrap; draws are clipped (not discarded) and the clipped share is reported. |
| minor | Tests asserted what the code wrote | fixed | Leak tests perturb future data and require unchanged predictions; the mapping test is leave-one-out. |
| minor | Monte Carlo noise comparable to differences | fixed | Draws raised; a second-seed rerun is reported; candidate differences inside that noise are no longer interpreted. |
| minor | m compared with METR's total-slope ratio | fixed | The total slope ratio is reported for the like-for-like comparison. |
| minor | Degenerate frontier floor | fixed | The standing leader's value is drawn from Epoch's posterior. |
| minor | Full-sample tuning choices (df, floors, half-life) | rejected | Left as stated assumptions (METHODS section 11). The reviewer measured their effect at RMSE 2.36-2.83, inside fold noise; tuning them by nested cross-validation on ~20 folds would add machinery without changing any number that matters. |
