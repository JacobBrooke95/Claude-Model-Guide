# Capability model: methods

Model version `cap-v2.2`, as of 2026-11-16. Every number here is written by `python3 capability/run.py` from `capability/output/capability_forecast.json`; do not edit by hand.

**v1 was withdrawn.** An independent adversarial review of cap-v1.0 (`research/04-adversarial-review-v1.md`) found two blockers and eight major problems: the headline backtest left out its worst fold and compared against weak baselines; several benchmark predictions contradicted scores already observed; and the long-range band was an untested prior. v1's output is kept, unedited, at `history/capability_forecast_v1.0_withdrawn.json`, and its predictions stay on file marked withdrawn. Section 14 lists each finding and what changed.

## 1. What is forecast, and how far to trust each part

| Output | Status |
|---|---|
| Public ECI of the next Opus, Sonnet, Fable/Mythos (1-3 months out) | Tested on all past releases; about 2.5-3 ECI points RMSE; no better than a two-line baseline, which is its core |
| Public ECI of the next Haiku (about 8 months out) | Outside anything tested |
| Benchmark scores of the next models | Anchored on each family's last score; thinly tested (2-16 folds per benchmark) |
| AECI as printed in the model's own card | Judgement-heavy estimate from eight cards; wide band |
| Frontier to 2027-09-30 | The uncorrected code was backtested at this horizon and under-predicted; the published, corrected configuration is tested only to six months |
| Frontier beyond that, to 2030 | Scenario projection driven by stated priors |

**Primary scale.** Public ECI is the modelling scale (256 models, four years, posterior draws, refittable inputs). AECI is reported two ways: (1) 'own card', the value Anthropic will print in the model's own system card, which is what gets graded and is modelled directly; (2) the November 6 2026 scale, secondary, through a mapping.

## 2. Data

`build_data.py` writes the canonical tables under `capability/data/` and logs every rename, date conflict, merge and dropped row in `build_log.csv` (v2: every non-exact name match is logged, and dated variants of a model no longer merge into a sibling). Nothing is interpolated. Models: 256 with a public ECI plus the Claude releases Epoch does not score. Index values: public ECI with 90% credible intervals and Epoch's 500 joint posterior draws; every AECI value Anthropic has printed, by card. Benchmark scores: one row per benchmark and model in one stated configuration. Release dates for the next models come from `forecast/output/forecast.json`.

## 3. The level process

One process produces the record line for both layers of the model.

- **Fit.** Record-setting releases since Claude 3 Opus. Level now and recent slope are drawn with equal weight from three recent-trend forms: trailing-12-month line, trailing-24-month line, and the last segment of a piecewise line with unknown changepoint. v1's stacking over seven forms is gone: its weights were corner solutions that flipped between forms, and the all-history forms under-predicted in every fold.
- **Uncertainty.** Subsample bootstrap: each replicate keeps the distinct members of a with-replacement resample of models (about 63%) and one of Epoch's 500 joint posterior draws; record sets are recomputed per replicate. Slope draws outside 4-60 (recent) or 4-40 (pre-break) ECI/yr are clipped to the bound; the share is reported.
- **Paths.** From today, pace(t) = kappa x log10(compute growth) + a0 x m(t), with a scenario for m(t) drawn per path (section 10), plus a random walk whose annual sd is the sd of past 12-month frontier gains.
- **Correction.** On the 'hold' and faster scenarios only, beta x g(h) is added to the Anthropic line, with beta pooled across both frontier series and g tapering in from zero and out by 1.5 years (section 7.2).
- **Frontier.** The running maximum held at T is max(leader's own value drawn from Epoch's posterior, line level lagged by the standing record's age + scatter).

Anthropic today: level 171.6 (168.1 to 174.9), recent slope 20.6 (16.9 to 27.2) ECI/yr, pre-break slope 15.0 (12.3 to 18.3), total slope ratio 1.37 (1.00 to 1.98). The total slope ratio above (recent / pre-break, public ECI, Anthropic) is the quantity comparable to METR's 1.9x and the card's 1.88x, which are total-slope ratios on AECI. The algorithmic multiplier m used inside the scenarios is a different quantity (it excludes the compute term) and is larger. All labs: recent slope 16.4 (13.2 to 19.8). Fitted to the other labs' records; no step-up is found, so 'pre-break' pace is at most the recent pace and 'reversion' nearly coincides with 'hold' for this series. No under-prediction correction is applied to it. A sizeable share of its slope draws hit the clipping bounds (reported above).

### Was there a break?

| Series | n | BIC wt linear | hinge | jump | quadratic | Slope before | after | Ratio |
|---|---|---|---|---|---|---|---|---|
| Anthropic, public ECI | 16 | 0.00 | 0.30 | 0.01 | 0.69 | 14.41 | 23.64 | 1.64 |
| All labs, public ECI | 24 | 0.44 | 0.19 | 0.22 | 0.14 | 22.89 | 16.47 | 0.72 |
| AECI Nov 6 fit, public dates | 14 | 0.00 | 0.17 | 0.82 | 0.01 | 15.49 | 26.34 | 1.70 |
| AECI Nov 6 fit, internal dates + internal model | 15 | 0.00 | 0.94 | 0.02 | 0.04 | 15.43 | 29.19 | 1.89 |

Anthropic's public-ECI records bend upward; the all-lab frontier does not; the card's 1.88x on AECI is reproduced only with internal dates and the unreleased internal model. The other labs' line is fitted on non-Anthropic records only; 35% of its slope draws hit the clipping bounds.

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
forecast as a level: an equal blend of the last card's gap and the mean of the last
three (v2.0 used the mean of three alone, which scored worse than the last gap in the
rolling test). The predictive sd is the larger of the rolling out-of-sample RMSE of
the blend and the sd of the last four gaps,
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

Predicted gap +3.80, sd 3.94. Rolling test (each card predicted from the three before it):

| Card | Predicted gap (blend) | Actual | Error | Error of 'last gap' rule |
|---|---|---|---|---|
| Claude Mythos 5.1 | -2.93 | -5.01 | -2.08 | -2.43 |
| Claude Opus 5.5 | -4.24 | 0.82 | 5.06 | 5.83 |
| Claude Sonnet 5.5 | -0.72 | 1.37 | 2.09 | 0.55 |
| Claude Haiku 5.5 | 0.22 | 6.68 | 6.47 | 5.31 |
| Claude Mythos 5.2 | 4.82 | 3.68 | -1.14 | -3.00 |

RMSE 3.94, mean error +2.08 (mean-of-three alone: 4.32; last gap alone: 3.93). Judgement-heavy estimate with a wide band. The rolling test (five cards) has RMSE 3.9 AECI points; the Haiku 5.5 card missed by 6.5. Sonnet and Haiku own-card predictions are conditional on Anthropic printing one: the Sonnet 5 card printed no AECI. They expire unresolved if the card has none.

### November 6 scale (secondary)

A level mapping fitted on 13 Claude models (hinge above a knee, or a one-time level shift; the forecast mixes them 0.4/0.6). Leave-one-out RMSE 1.4; residual sd used 1.6. Caveats: The gap between AECI and public ECI tracks how recent the model and the fit are, not the model's level: Haiku 5.5 (ECI 160.4) printed 167.11 in its own card. A mapping in level alone under-states Sonnet- and Haiku-tier AECI by roughly 2-4 points; the residual sd is set from leave-one-out and held-out errors to cover that. The level-shift threshold is not identified between ECI 156.3 and 164.1 (no model in between). Thirteen models on one fit. Secondary quantity.

### Refits

Descriptive only in v2 (the own-card forecast no longer sums refit steps). Three of the seven card-to-card transitions are observed for Opus 5.5 alone, read from cards that state no fit; over those three refits combined, the other models moved +3.8 to +4.5 and Opus 5.5 +5.4. The two large steps coincide with basket changes, so steps are not exchangeable draws.

## 6. Benchmarks

Bounded scores follow p = (score - floor)/(ceiling - floor) = sigmoid(a (ability - D)); the ceiling is estimated (with a bootstrap interval) wherever at least four scores lie above 75% of the nominal range, otherwise the nominal ceiling is kept. Predictions are ANCHORED: the family's own last score, moved along the link by the predicted ability gain (on the logit scale for bounded scores, under a ceiling drawn from its bootstrap and never below the last score), plus step noise estimated from past within-family steps. A benchmark is published only if it is not stale (a model scored in the last six months), not saturated (best score below 90% of the ceiling), not too thin; whether it is graded or only indicative is decided by the admission rule below.

| Benchmark | Link | Models | Ceiling | Estimated | Best observed | Backtest folds | MAE anchored | MAE v1 curve level | MAE previous-in-family | Bias | 80% coverage | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SWE-bench Pro | bounded | 13 | 100.00 | yes | 93.00 | 4 | 5.89 | 5.30 | 10.45 | 3.46 | 0.50 | indicative |
| Terminal-Bench 2.1 | bounded | 10 | 100.00 | yes | 87.60 | 2 | 0.78 | 2.89 | 5.80 | 0.07 | 1.00 | indicative |
| OSWorld | bounded | 16 | 89.50 | yes | 89.30 | 10 | 5.61 | 4.92 | 10.40 | -4.55 | 0.70 | indicative |
| GDPval-AA v2.1 | elo | 46 | - | no | 1866.00 | 12 | 74.53 | 115.56 | 378.50 | -37.85 | 1.00 | no |
| Remote Labor Index | bounded | 17 | 100.00 | no | 41.30 | 2 | 7.48 | 6.75 | 18.15 | 5.14 | 1.00 | indicative |
| ARC-AGI-2 | bounded | 90 | 95.20 | yes | 95.00 | 16 | 11.66 | 14.38 | 26.40 | -2.70 | 1.00 | indicative |
| Humanity's Last Exam (no tools) | bounded | 15 | 100.00 | no | 73.20 | 8 | 3.90 | 5.16 | 15.63 | -0.88 | 1.00 | graded |
| ForecastBench (baseline) | linear | 16 | - | no | 60.30 | 11 | 1.35 | 1.75 | 1.30 | -0.67 | 0.64 | no |
| Vending-Bench 2 | linear | 61 | - | no | 16484.21 | 14 | 3159.28 | 3070.80 | 2951.29 | -1342.11 | 0.79 | no |
| METR 50% time horizon (TH1.1) | loghorizon | 20 | - | no | 718.81 | 9 | 74.01 | 73.06 | 131.10 | 61.00 | 1.00 | no |
| GPQA Diamond | bounded | 176 | 96.67 | yes | 96.53 | 31 | 4.23 | 3.22 | 11.38 | -0.17 | 0.90 | no |
| FrontierMath Tiers 1-3 | bounded | 90 | 95.09 | yes | 95.09 | 12 | 5.67 | 5.67 | 17.92 | 3.86 | 0.83 | indicative |
| Terminal-Bench 2.0 | bounded | 32 | 100.00 | yes | 84.72 | 6 | 10.43 | 11.32 | 13.53 | -2.46 | 1.00 | no |
| WebDev Arena | elo | 80 | - | no | 1820.31 | 12 | 60.21 | 50.79 | 93.20 | 16.78 | 0.67 | indicative |
| LMArena text | elo | 104 | - | no | 1538.38 | 30 | 41.20 | 41.02 | 47.84 | -14.67 | 0.67 | indicative |
| AA Intelligence Index v5 | bounded | 31 | 100.00 | no | 64.56 | 3 | 3.49 | 3.54 | 19.51 | 3.08 | 1.00 | indicative |
| Vals Index v2.2 | bounded | 23 | 100.00 | no | 71.31 | - | - | - | - | - | - | indicative |

**Admission rule.** A benchmark with a fitted link is dropped if it is stale (no model scored in six months), withdrawn, shows no skill against 'previous in family' on 4 or more folds, or every family is saturated. Otherwise it is GRADED only if it has at least 4 backtest folds, 80% coverage of at least 0.7, |bias| no more than half its RMSE, a resolvable source (a site chart still reporting the family), and an estimated ceiling that does not merely hug the record; every other benchmark is INDICATIVE: shown, not graded. Per family, no number is published if the family's latest score or its predicted median is at or above 90% of the ceiling (a saturation statement is given instead), or if the family's latest model has no score to anchor on.

Why each indicative benchmark is not graded:

- **SWE-bench Pro**: 80% coverage 0.5 (needs 0.7); bias 3.46 is more than half the RMSE 5.94.
- **Terminal-Bench 2.1**: 2 backtest folds (needs 4).
- **OSWorld**: bias -4.55 is more than half the RMSE 7.53; estimated ceiling 89.5 merely hugs the best observed score 89.3.
- **Remote Labor Index**: 2 backtest folds (needs 4).
- **ARC-AGI-2**: estimated ceiling 95.2 merely hugs the best observed score 95.0.
- **FrontierMath Tiers 1-3**: no resolvable source (not a site chart; arena ratings and outside indices are read at mixed snapshots); estimated ceiling 95.1 merely hugs the best observed score 95.1.
- **WebDev Arena**: 80% coverage 0.67 (needs 0.7); no resolvable source (not a site chart; arena ratings and outside indices are read at mixed snapshots).
- **LMArena text**: 80% coverage 0.67 (needs 0.7); no resolvable source (not a site chart; arena ratings and outside indices are read at mixed snapshots).
- **AA Intelligence Index v5**: 3 backtest folds (needs 4); no resolvable source (not a site chart; arena ratings and outside indices are read at mixed snapshots).
- **Vals Index v2.2**: 0 backtest folds (needs 4); no resolvable source (not a site chart; arena ratings and outside indices are read at mixed snapshots).

Not published at all:

- **GDPval-AA v2.1**: withdrawn: the linear Elo link over-extrapolates (the six highest-ECI models sit about 250 Elo below it; the backtest over-predicted in 10 of 12 folds; v2.0's 80% lower bounds exceeded the best score ever recorded).
- **ARC-AGI-3**: too thin: only 7 models with both a public ECI and a score (minimum 8).
- **ForecastBench (baseline)**: no skill: anchored MAE 1.35 vs previous-in-family 1.3 on 11 folds.
- **Vending-Bench 2**: no skill: anchored MAE 3159.28 vs previous-in-family 2951.29 on 14 folds.
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

Pooled over benchmarks, anchored intervals cover 46% / 83% / 96% at nominal 50 / 80 / 95% (182 fold-benchmarks); the 50% intervals are stretched by 1.072; the 80% and 95% factors are 1 (no-op).

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
| Model, date given | 10 | 1.23 | 2.07 | 2.60 | 1.79 | 0.70 | 1.00 | 1.00 |
| **Model, date not given** | 9 | 0.41 | 2.04 | 2.47 | 1.85 | 1.00 | 1.00 | 1.00 |
| Baseline: previous + 12-month Anthropic slope x elapsed (date given) | 10 | 0.67 | 2.00 | 2.20 | - | - | - | - |
| Baseline: same, date not given | 9 | 0.06 | 2.33 | 2.61 | - | - | - | - |
| Baseline: previous model in family | 9 | 9.56 | 9.56 | 11.20 | - | - | - | - |
| Baseline: previous + family's mean step | 9 | 1.69 | 4.26 | 5.83 | - | - | - | - |
| Baseline: trailing-12-month all-lab line | 10 | -4.66 | 4.95 | 6.02 | - | - | - | - |
| Baseline: all-history all-lab line | 10 | -1.36 | 4.11 | 4.71 | - | - | - | - |

**6 months ahead**

| Method | n | Bias (actual - predicted) | MAE | RMSE | CRPS | Cov 50% | Cov 80% | Cov 95% |
|---|---|---|---|---|---|---|---|---|
| Model, date given | 4 | 3.19 | 3.19 | 3.54 | 2.60 | 0.75 | 1.00 | 1.00 |
| **Model, date not given** | 3 | 5.77 | 5.77 | 5.94 | 3.55 | 0.33 | 1.00 | 1.00 |
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
| 0.25 | given | prev_plus_slope | 10 | 2.07 | 2.00 | 0.07 | -0.63 | 0.87 | 6 |
| 0.25 | given | prev_in_family | 9 | 1.86 | 9.56 | -7.70 | -10.82 | -4.72 | 9 |
| 0.25 | given | family_mean_step | 9 | 1.86 | 4.26 | -2.40 | -4.61 | -0.30 | 4 |
| 0.25 | given | trailing_12m_linear | 10 | 2.07 | 4.95 | -2.87 | -4.68 | -1.05 | 8 |
| 0.25 | given | all_history_linear | 10 | 2.07 | 4.11 | -2.03 | -3.29 | -0.72 | 8 |
| 0.25 | not given | prev_plus_slope_date_unknown | 9 | 2.04 | 2.33 | -0.29 | -0.97 | 0.54 | 7 |
| 0.50 | given | prev_plus_slope | 4 | 3.19 | 3.18 | 0.01 | -0.86 | 1.07 | 3 |
| 0.50 | given | prev_in_family | 3 | 2.63 | 17.63 | -14.99 | -16.01 | -13.98 | 3 |
| 0.50 | given | family_mean_step | 3 | 2.63 | 8.67 | -6.04 | -7.45 | -4.62 | 3 |
| 0.50 | given | trailing_12m_linear | 4 | 3.19 | 6.60 | -3.41 | -6.18 | -0.57 | 3 |
| 0.50 | given | all_history_linear | 4 | 3.19 | 5.24 | -2.05 | -4.27 | 0.13 | 3 |
| 0.50 | not given | prev_plus_slope_date_unknown | 3 | 5.77 | 4.64 | 1.13 | 0.24 | 2.02 | 1 |

**Verdict.** On all folds the model's point forecast is not distinguishable from 'previous-in-family + trailing-12-month Anthropic record slope x elapsed time' at any lead (every paired interval spans zero, or favours the baseline). That baseline is therefore the core of the model: next = predecessor + recent record-line gain. What the model adds is a predictive distribution with tested coverage, a positive-step constraint, and consistency with the long-range paths. It does clearly beat 'previous model in family', 'family mean step' and the two all-lab trend lines.

**What the sample supports.** Lead 0 (n=21) supports an error of roughly 2.5 ECI points RMSE with the date known. Three months ahead (n=10, 9 with the date unknown) supports 'about the same, perhaps 3'. Six months ahead (n=4, 3 date-unknown) supports nothing firmer than 'errors of 4-6 points happened and every one was an under-prediction'. No fold has a lead beyond six months: the Haiku forecast (median lead about eight months) is outside anything tested.

Within-family steps: 21 observed, 0 negative, smallest +0.86. Variants tested on the same folds (no bias term; no step ratio; record line + pooled family offset; a stacked mix of the two) are in the JSON; none is better beyond noise. Monte Carlo noise: a second seed gives RMSE 2.46 vs 2.47 at 0.0 yr, 2.67 vs 2.6 at 0.25 yr, 3.32 vs 3.54 at 0.5 yr.

### 7.2 The projection code itself

The projection code itself (level.LevelProcess.paths, central scenario weights) run at monthly historical origins and scored on the running-max public ECI 0.5, 1.0 and 1.5 years later. 'raw' has no correction. 'published_config' is the configuration the live forecast uses: the pooled correction, learned only from folds (of either series) whose target precedes the origin, added on trend-continuation paths. Calibration factors are fitted on 'published_config'. Folds overlap heavily; origins span 2024-07 to 2026-05, one regime of rising pace. The scenario weights are today's prior, so this is not a test of the weights.

**Anthropic frontier** (30 folds, 16 origins, 10 distinct outcomes)

| Horizon (yr) | Variant | n | Folds with a correction | Bias | MAE | RMSE | CRPS | Cov 50% | Cov 80% | Cov 95% |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.50 | raw | 16 | 9 | 3.74 | 3.74 | 4.04 | 2.35 | 0.31 | 1.00 | 1.00 |
| 0.50 | published_config | 16 | 9 | 3.29 | 3.29 | 3.53 | 2.06 | 0.44 | 1.00 | 1.00 |
| 1.00 | raw | 10 | 3 | 6.30 | 6.30 | 6.55 | 3.91 | 0.30 | 1.00 | 1.00 |
| 1.00 | published_config | 10 | 3 | 5.50 | 5.50 | 5.66 | 3.39 | 0.40 | 1.00 | 1.00 |
| 1.50 | raw | 4 | 0 | 8.43 | 8.43 | 8.81 | 5.26 | 0.25 | 1.00 | 1.00 |
| 1.50 | published_config | 4 | 0 | 8.43 | 8.43 | 8.81 | 5.26 | 0.25 | 1.00 | 1.00 |

Calibration factors (50/80/95%), fitted on 'published_config': 0.5 yr: 1.038/1.0/1.0; 1.0 yr: 1.197/1.0/1.0; 1.5 yr: 1.0/1.0/1.0.

**All-lab frontier** (51 folds, 23 origins, 14 distinct outcomes)

| Horizon (yr) | Variant | n | Folds with a correction | Bias | MAE | RMSE | CRPS | Cov 50% | Cov 80% | Cov 95% |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.50 | raw | 23 | 9 | 2.51 | 3.41 | 4.34 | 2.32 | 0.83 | 1.00 | 1.00 |
| 0.50 | published_config | 23 | 9 | 2.20 | 3.34 | 4.30 | 2.29 | 0.87 | 1.00 | 1.00 |
| 1.00 | raw | 17 | 3 | 2.91 | 4.95 | 5.85 | 3.83 | 0.88 | 1.00 | 1.00 |
| 1.00 | published_config | 17 | 3 | 2.49 | 5.35 | 6.08 | 3.99 | 0.82 | 1.00 | 1.00 |
| 1.50 | raw | 11 | 0 | 7.39 | 8.90 | 9.80 | 6.68 | 0.82 | 1.00 | 1.00 |
| 1.50 | published_config | 11 | 0 | 7.39 | 8.90 | 9.80 | 6.68 | 0.82 | 1.00 | 1.00 |

Calibration factors (50/80/95%), fitted on 'published_config': 0.5 yr: 1.0/1.0/1.0; 1.0 yr: 1.0/1.0/1.0; 1.5 yr: 1.0/1.0/1.0.

**The correction.** The uncorrected process under-predicted both frontiers in this window. Block by block (half-years of origin), the slope of error on horizon was:

| Series | Origins in | Folds | Slope (ECI/yr) | se |
|---|---|---|---|---|
| all | 2024H2 | 21 | 8.11 | 0.60 |
| all | 2025H1 | 16 | 0.27 | 0.95 |
| all | 2025H2 | 10 | -1.02 | 0.88 |
| all | 2026H1 | 4 | 2.88 | 1.17 |
| anthropic | 2025H1 | 16 | 5.47 | 0.88 |
| anthropic | 2025H2 | 10 | 8.00 | 0.60 |
| anthropic | 2026H1 | 4 | 9.24 | 1.29 |

| Estimate | ECI/yr |
|---|---|
| Anthropic series alone (unshrunk; v2.0 used this x 0.8) | 6.24 |
| All-lab series alone | 4.22 |
| Random-effects pooled mean (used) | 4.71 (se 1.51) |
| Between-block sd | 3.87 |
| Predictive sd for a new block (used as the term's sd) | 4.15 |

Trend fits ran low on both frontiers over 2024-26, but block slopes range from -1.0 to 9.2 and the series disagree; a random-effects mean across all blocks is used instead of the Anthropic-only estimate, with the between-block spread carried as its uncertainty. Shape: level adjustment = beta x g(h): g = h^2 up to 0.5 yr, 0.25 + (h-0.5) - (h-0.5)^2/2 up to 1.5 yr, 0.75 after (the correction rate tapers in from zero, peaks at 0.5 yr, and is zero from 1.5 yr). Applied to: hold, compounding, explosive. Not applied to: slowdown, reversion, non-Anthropic frontier (slowdown and reversion are the claim that the recent pace does not persist; the other labs' backtest rejected a correction). Size: 3.2 ECI on those paths at end-2027, 3.53 from mid-2028 on. A rolling (out-of-sample) correction exists for only 12 Anthropic folds with 6 distinct outcomes, at horizons [0.5, 1.0] yr (mostly six months). On those it lowered MAE from 5.55 to 4.3; on the all-lab series the same correction changed MAE from 1.77 to 2.21 over 12 folds. Nothing at 1.5 years has been scored with a correction, and at one year only three overlapping folds have. 80% and 95% bands covered throughout; the 50% band was too narrow around a biased median, which the 50% factor repairs where it is above 1. Factors equal to 1 are a no-op.

### 7.3 Leave-future-out IRT refit

Own least-squares 2PL refit of Epoch's benchmark-level inputs, refitted at every fold origin on models released on or before that date, mapped to ECI units by a monotone alignment to the published ECI of those same models. The release backtest is rerun with history from a strict-origin vintage (models released before the origin; in v2.0 the lead-0 vintage included the target) and the target's actual from the release date's vintage. The fit is deterministic; the vintages are stored in data/irt_vintages.csv.gz, which is committed and covered by the input hash (run.py --full rebuilds it; a test recomputes two vintages and compares). In v1 a date-rounding slip excluded the target from its own vintage on a clean cache, which is why the reviewer's clean run found 18 folds instead of 33. Fixed (tolerance on 'on or before'); numbers below are from a clean rebuild.

Reproduction on all data: correlation 0.9973 with Epoch's ECI, RMSE 0.67 above ECI 140. Target shift, vintage vs published: mean absolute 0.8, max 2.59 over 35 folds.

| Lead (yr) | Method | n | RMSE vintage | RMSE published | Bias vintage | Bias published |
|---|---|---|---|---|---|---|
| 0.0 | model | 21 | 2.80 | 2.47 | 0.53 | 0.40 |
| 0.0 | prev_plus_slope | 21 | 3.46 | 2.52 | 0.59 | 0.35 |
| 0.25 | model | 10 | 2.29 | 2.60 | 0.92 | 1.23 |
| 0.25 | prev_plus_slope | 10 | 3.14 | 2.20 | 1.10 | 0.67 |
| 0.5 | model | 4 | 4.08 | 3.54 | 3.53 | 3.19 |
| 0.5 | prev_plus_slope | 4 | 4.64 | 3.63 | 3.23 | 2.39 |

Scores in Epoch's input file are today's collection; a score measured after the origin for a model released before it cannot be removed (no timestamps).

## 8. Calibration

Conformal-style: per nominal level, the factor by which an interval must be stretched about its median to cover the stated share of backtest outcomes, learned from earlier folds when scoring and from all folds for the live forecast; floored at 1.

| Set | Folds | Raw 50% | Raw 80% | Raw 95% | Factor 50% | 80% | 95% | 80% factor before floor |
|---|---|---|---|---|---|---|---|---|
| Ability, date given, lead 0 | 21 | 0.52 | 0.86 | 1.00 | 1.00 | 1.00 | 1.00 | 0.81 |
| Ability, date not given, 3-6 months | 12 | 0.83 | 1.00 | 1.00 | 1.00 | 1.00 | 1.00 | 0.51 |
| Benchmarks, anchored, pooled | 182 | 0.46 | 0.83 | 0.96 | 1.07 | 1.00 | 1.00 | 0.95 |

For ability the raw intervals already cover at or above nominal on all folds, so the factors are 1 and calibration changes nothing there. That is a statement about the folds we have, not about longer leads. The frontier bands use the factors in 7.2.

## 9. Next-model predictions

Each draw takes a release date from the release forecaster, the record-line gain from the shared level paths (scenario mixture, central weights, bias term included), a positive step and measurement noise. Anthropic's Fable 5.2 card prints an unreleased internal model at AECI 178.78 (15 benchmarks); it is not used in the fit.

| Next model | Release (median, 10-90%) | Predecessor ECI | Public ECI (80%) | 95% | AECI own card (80%) | AECI Nov 6 scale (80%) | P(below predecessor) | Lead within tested range |
|---|---|---|---|---|---|---|---|---|
| Claude Opus 5.6 | 2026-12-14 (2026-11-20 to 2027-02-22) | 168.54 | 173.9 (169.9 to 181.1) | 168.2 to 188.8 | 177.9 (171.6 to 186.8) | 179.7 (173.7 to 189.4) | 3.5% | yes |
| Claude Sonnet 5.6 | 2027-01-21 (2026-12-01 to 2027-04-02) | 166.56 | 173.1 (168.5 to 182.3) | 166.6 to 192.2 | 177.3 (170.3 to 188.0) | 178.9 (172.3 to 190.4) | 2.4% | yes |
| Claude Haiku 6 | 2027-07-13 (2027-02-03 to 2027-11-23) | 160.43 | 175.2 (165.3 to 198.7) | 162.3 to 224.5 | 179.4 (167.2 to 203.9) | 181.1 (169.4 to 208.2) | 0.6% | no |
| Claude Fable / Mythos 5.3 | 2027-02-02 (2026-12-14 to 2027-04-13) | 173.44 | 178.4 (174.1 to 186.4) | 172.4 to 195.1 | 182.5 (175.6 to 192.2) | 184.6 (178.2 to 195.6) | 6.2% | yes |

Benchmarks (median, 80% interval; 'saturated' = statement only; '-' = the family's latest model has no score to anchor on). Only graded rows enter the scorecard:

| Benchmark | Status | Opus | Sonnet | Haiku | Fable / Mythos |
|---|---|---|---|---|---|
| SWE-bench Pro | indicative | saturated | 89.8 (83.0 to 96.1) | 89.6 (74.3 to 99.0) | saturated |
| Terminal-Bench 2.1 | indicative | saturated | 89.0 (83.7 to 94.9) | - | - |
| OSWorld | indicative | saturated | saturated | saturated | saturated |
| Remote Labor Index | indicative | 39.1 (21.8 to 69.5) | - | - | 61.1 (39.9 to 85.9) |
| ARC-AGI-2 | indicative | saturated | saturated | saturated | saturated |
| Humanity's Last Exam (no tools) | graded | 74.5 (66.0 to 85.2) | 70.4 (60.0 to 84.7) | 75.8 (56.0 to 96.2) | 81.0 (73.6 to 89.9) |
| FrontierMath Tiers 1-3 | indicative | saturated | saturated | saturated | saturated |
| WebDev Arena | indicative | 1920 (1817 to 2071) | 1908 (1796 to 2088) | - | - |
| LMArena text | indicative | 1549 (1501 to 1611) | 1514 (1462 to 1584) | 1493 (1416 to 1645) | - |
| AA Intelligence Index v5 | indicative | 71.9 (53.8 to 87.4) | 70.8 (51.1 to 88.3) | 72.3 (43.0 to 96.7) | 75.7 (57.8 to 90.1) |
| Vals Index v2.2 | indicative | 77.6 (62.5 to 88.8) | 79.6 (64.7 to 90.7) | 79.8 (59.6 to 95.5) | 78.1 (63.2 to 89.5) |

## 10. Projection to 2030

'Backtested through 2027-09-30' means only this: the UNCORRECTED code was run at a 1.0-year horizon from 10 overlapping monthly origins (7 distinct outcomes) in one regime, and under-predicted in 10 of them (mean error +6.3 ECI; 50% coverage 0.40). The corrected configuration that is published has been scored out of sample on only 12 overlapping folds with 6 distinct outcomes, nine of them at six months and none beyond one year. Beyond 2027-09-30 the bands are a scenario projection driven by the stated priors: read each scenario path separately and treat the mixture as a summary of the prior.

### Scenarios

| Scenario | Definition | Record-line gain in 2027, correction included (80%) | Same, without correction | 2028 | 2030 | Share of paths below pre-break pace, 2027 | Frontier, end-2030 (median) |
|---|---|---|---|---|---|---|---|
| slowdown | Below pre-break pace. Training-compute growth follows the 'low' driver path (2.5x, 2x, 1.5x, 1.5x per year 2027-30) and the algorithmic multiplier falls to 0.4-0.9 of its pre-break value within a year. | 12.1 (8.0 to 16.6) | 12.10 | 8.30 | 7.30 | 0.82 | 209.30 |
| reversion | The 2025-26 step-up was one-off. Pace returns within six months to 0.85-1.15x the pre-break slope (centred on it, so about half these paths run below pre-break pace), then follows the 'central' compute path down. | 15.5 (10.9 to 20.3) | 15.50 | 14.10 | 12.30 | 0.43 | 228.30 |
| hold | The recent trend holds: the algorithmic multiplier stays where the recent slope puts it; compute follows the 'central' driver path (5x, 4x, 3x, 2.5x). | 24.0 (17.4 to 32.2) | 20.70 | 20.10 | 18.20 | 0.05 | 253.50 |
| compounding | AI R&D feedback: the algorithmic multiplier doubles every 6-12 months until it reaches 4-7.5x, then stays; 60-100% of the excess over 'hold' is realised; compute on the 'central' or 'high' path. | 34.7 (25.3 to 47.1) | 31.60 | 45.40 | 46.90 | 0.00 | 344.50 |
| explosive | Bounded explosive tail: the multiplier doubles every 3-6 months to a peak of 8-30x, holds 1-2 years, then settles at 3-6x; same 60-100% realisation haircut. | 59.0 (39.8 to 92.1) | 55.30 | 109.60 | 42.90 | 0.00 | 478.80 |

Mixture: 21.3 ECI gained in 2027 (19.3 without the correction); pre-break pace 15.0, recent pace 20.6.

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

| Date | Anthropic frontier, public ECI (80%) | 95% | Other labs' frontier (80%) | All-lab frontier = larger of the two (80%) | Anthropic leads in | AECI Nov 6 scale, secondary (80%) | Median beyond measured scale | Share of paths beyond it |
|---|---|---|---|---|---|---|---|---|
| 2026-12-31 | 174.7 (171.7 to 178.4) | 170 to 181 | 172.1 (169.2 to 176.0) | 175.2 (172.4 to 178.9) | 75% | 180.3 (177.1 to 187.0) | no | 0% |
| 2027-12-31 | 194.7 (184.1 to 215.2) | 180 to 237 | 188.6 (179.7 to 200.8) | 196.2 (186.9 to 216.6) | 73% | 202.7 (189.4 to 228.9) | no | 47% |
| 2028-12-31 | 212.8 (194.6 to 264.3) | 188 to 345 | 205.2 (190.7 to 248.6) | 215.3 (199.1 to 270.5) | 67% | 222.9 (200.8 to 285.3) | yes | 88% |
| 2029-12-31 | 229.6 (203.7 to 318.0) | 194 to 456 | 220.1 (200.2 to 308.7) | 232.9 (210.1 to 335.0) | 64% | 241.3 (210.8 to 345.6) | yes | 97% |
| 2030-12-31 | 245.9 (212.1 to 370.6) | 200 to 516 | 234.3 (209.2 to 366.9) | 250.2 (220.5 to 401.4) | 62% | 259.5 (220.0 to 403.9) | yes | 99% |

Layer agreement: the frontier median is never below the median implied by the next-model layer's own draws (largest shortfall -0.022 ECI across quarters).


**Measured scale.** For each benchmark in Epoch's basket, the ECI at which it is 90% solved is difficulty + 2.2/slope (Epoch's item parameters; all benchmarks, no slope cut-off). The range reported runs from the level where 80% of the basket is that far solved to the level where 90% is; the upper end is the one value the page shades from (the lower end is already close to today's frontier because the basket still holds many old, solved benchmarks). Above the upper end only about one benchmark in ten still separates models, so ECI values are extrapolations of the scale itself. Bands above it are kept in the data and flagged. Range: 182.8 to 195.6; shaded from 195.6; display cap 230. At today's frontier 60% of the basket is already 90% solved.

### Sensitivity to the prior

| Weighting | Date | Median | 80% low | 80% high |
|---|---|---|---|---|
| central | 2027-12-31 | 195 | 184 | 215 |
| central | 2028-12-31 | 213 | 194 | 264 |
| central | 2030-12-31 | 246 | 212 | 371 |
| sceptic | 2027-12-31 | 191 | 182 | 206 |
| sceptic | 2028-12-31 | 205 | 191 | 231 |
| sceptic | 2030-12-31 | 230 | 205 | 280 |
| accelerationist | 2027-12-31 | 202 | 188 | 230 |
| accelerationist | 2028-12-31 | 232 | 202 | 332 |
| accelerationist | 2030-12-31 | 289 | 229 | 484 |
| unweighted_evidence_average | 2027-12-31 | 195 | 185 | 212 |
| unweighted_evidence_average | 2028-12-31 | 214 | 198 | 252 |
| unweighted_evidence_average | 2030-12-31 | 248 | 220 | 344 |

### Research note 1's central path

Research note 1's central path (17, 17, 16, 15 ECI/yr) is the all-lab frontier continuing at Epoch's reasoning-era slope. For the all-lab series that is our 'hold' and 'reversion' scenarios, which land near it. Our medians are higher for three reasons, in order of size: the Anthropic series has a steeper recent slope than the all-lab series, and Anthropic currently holds the frontier; some prior weight sits on accelerating scenarios; and an explicit under-prediction term is carried where it helped out of sample. Note 1: +65, about 235 by end-2030. Ours, all-lab: slowdown 215, reversion 237, hold 255, compounding 368, explosive 577; mixture median 250.

### Time horizon

No hours series is published. METR's last measurement is 17.4 hours (Claude Mythos Preview, April 2026) and METR calls estimates above 16 hours unreliable; the fitted link (about 4.75 ECI points per doubling) has no model above public ECI 157.8. Every released frontier model since then, and every projected value, lies beyond that range, so any hours figure would be extrapolation. Qualitatively: if the link held, each further 5 ECI points would double the horizon.

### Against external forecasts

| Source | Quantity | Theirs | Ours | Why they differ |
|---|---|---|---|---|
| FutureSearch (2026-11-14) | Rise in the highest public ECI held by OpenAI/Anthropic/GDM during 2029 | p10 11.7, p25 18.5, p50 27.3, p75 42.7, p90 74 | p10 9.2, p25 13.4, p50 18.4, p75 28.6, p90 66.0 | Same right-skewed shape. Ours is lower in the middle because the central compute path slows by 2029. |
| Ho et al., Rosetta Stone naive extrapolation (2025-10; conversion approximate) | All-lab public ECI frontier, Oct 2028 | ~189 (182-196) | median 210.6 (80% 196.1 to 255.5) at 2028-09-30 | Rosetta extrapolates the 2023-25 slope; the frontier is already about 8 ECI above that line. |
| Epoch AI trend (not a forecast), Nov 2026 | All-lab frontier at 16.6 ECI/yr (14.6-18.7) | straight line reaches 238 at end-2030 | all-lab median 250.2 at 2030-12-31 | See the reconciliation with research note 1. |
| AI Futures Project milestones (Automated Coder mid-2028 / mid-2030; SAR 2027 under a held 1.7-1.9x trend) | Capability milestones from a takeoff model | dates of qualitative milestones | no equivalent output | v1 translated ECI into METR-style hours to compare; that translation extrapolated two orders of magnitude beyond METR's measurements and has been withdrawn. The 'compounding' and 'explosive' scenarios are the nearest analogue. |

## 11. Assumptions that are not estimated

| Assumption | Value | Source |
|---|---|---|
| Residual distribution | Student-t, 4 df | robustness choice |
| Floor on trend residual scale | 0.75 ECI | Epoch posterior sd at the frontier is 1-2 points |
| Recent-trend forms and their weights | three forms, equal | review decision; all-history forms under-predict |
| Correction: which scenarios, and its taper | hold and faster; in from 0, peak at 0.5 yr, out by 1.5 yr | second-review decision |
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
- Above the measured-scale threshold (see scale) today's benchmark basket no longer identifies the scale; values there are flagged, not meaningful measurements.
- Frontier paths on the 'hold' and faster scenarios carry a pooled under-prediction correction whose out-of-sample test is thin (see projection.bias_term).
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

## 14. What the reviews changed

### First review (v1 -> v2.0)

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

### Second review (v2.0 -> v2.1)

Verdict: no blockers; publishable after targeted fixes (`research/05-adversarial-review-v2.md`). v2.0's output is archived at `history/capability_forecast_v2.0_superseded.json`.

| Finding | Issue | Disposition | What was done |
|---|---|---|---|
| N1 | Bias term added to every scenario and hidden from the scenario table | fixed | The correction is pooled across both series by random effects, applied only to 'hold' and faster scenarios on the Anthropic line, tapered in from zero and out by 1.5 years. Scenario paces are published as realised gains with the correction included; 'slowdown' runs below the pre-break pace in 2027. |
| N2 | 'The correction helped' rested on four folds | partly | The thinness of the test is stated wherever the correction is mentioned (METHODS 7.2, headline.notes, projection.bias_term). The pooled estimate replaces the Anthropic-only one. It remains a correction estimated in one regime and untested beyond six months. |
| N3 | 'Validated through' too strong | fixed | Renamed backtested_through (alias kept one version), derived without the 0.13-year allowance, with a caveat attached. |
| N4 | GDPval-AA over-extrapolates | fixed | Withdrawn. No concave link was fitted: with 12 folds and a board that re-anchors, there is nothing to validate one against. |
| N5 | All-lab frontier was mostly Anthropic's and inherited its correction | fixed | The non-Anthropic frontier is fitted on its own records, carries no correction and is published; the all-lab frontier is the larger of the two; the share of paths in which Anthropic leads is reported per year-end. |
| minor | Fable/Mythos Terminal-Bench 2.1 anchored on Fable 5.1 | fixed | A prediction now needs a score from the family's latest model; this one is withdrawn. |
| minor | Admission rule text disagreed with code; inconsistent saturation | fixed | One rule in code and text: graded needs 4+ folds, 80% coverage >= 0.7, |bias| <= RMSE/2, a resolvable source and a ceiling that does not hug the record; everything else with a link is indicative. A family gets no number if its latest score or predicted median is in the top tenth. |
| minor | Arena scores at mixed snapshots | fixed | Indicative, not graded. |
| minor | Layers agreed to ~1 ECI, not Monte Carlo noise | fixed | The frontier is built from the next-model layer's own draws until both frontier families have shipped; projection.layer_agreement reports the shortfall per quarter and a test bounds it. |
| minor | Lead-0 vintage included the target | fixed | History now comes from a strict-origin vintage. |
| minor | Grading matched chart rows by exact date | fixed | Matches on model name. |
| minor | Measured-scale threshold lenient | fixed | Reported as a range from the whole basket; the page shades from its upper end. |
| minor | Calibration factors fitted on a different configuration | fixed | Fitted on the published configuration; METHODS says where they are a no-op. |
| nit | Own-card rule scored worse than 'last gap' | fixed | Equal blend of the two rules. |
| nit | Claude 3.5 Haiku entered vintages 13 days early | fixed | Vintages use canonical release dates. |
| nit | All-lab slope draws clipped 19.8% | noted | Reported in trend.level_process; the other labs' record series is short and noisy and the clipping bounds are wide (4-60 ECI/yr). |

What moved:

- Frontier, end-2027 median: 197.5 -> 194.7; end-2030: 251.2 -> 245.9. The under-prediction correction is now pooled across both series (4.7 instead of 5.0 ECI/yr), applied only to 'hold' and faster scenarios, and tapered to zero by 1.5 years instead of being added to every path permanently.
- Claude Opus 5.6 public ECI median: 174.2 -> 173.9.
- Claude Sonnet 5.6 public ECI median: 173.8 -> 173.1.
- Claude Haiku 6 public ECI median: 177.4 -> 175.2.
- Claude Fable / Mythos 5.3 public ECI median: 179.2 -> 178.4.
- 'Slowdown' and 'reversion' no longer carry the correction; slowdown now runs below the pre-break pace in 2027. Scenario paces are published as realised gains, correction included.
- validated_through renamed backtested_through (2027-09-30; the old key is kept as an alias for this version) and now carries a caveat.
- Benchmarks split into graded and indicative. GDPval-AA predictions and the Fable/Mythos Terminal-Bench 2.1 prediction are withdrawn; one saturation rule (latest score or predicted median in the top tenth) replaces per-family inconsistencies. Graded: hle.
- All-lab frontier: the non-Anthropic line is now fitted separately and published; the share of paths in which Anthropic leads is reported.
- Own-card AECI: gap rule changed to an equal blend of the last gap and the mean of the last three (rolling RMSE 3.9).
- Measured-scale threshold is now a range derived from the whole basket (183-196); the page shades from 196 (was 207.6).
- cap-v2.2 adds a what-if variant, variants.with_model_4, alongside the default. The default forecast and its open predictions are numerically unchanged from cap-v2.1.

## 15. Anthropic's unreleased internal model (METR's Model 4)

**What is known.** The Fable 5.2 / Mythos 5.2 card prints 'a separate, unreleased internal research model that is somewhat more capable than Claude Mythos 5.2': AECI 178.78 on the November 6 fit (global 95% 173.75 to 185.18; local 177.08 to 180.59), scored on 15 benchmarks, plotted at an internal date of about 2026-09-26. METR's November 5 assessment describes 'Model 4' (finished training September-October 2026; AECI 178.6, or 179.7 dropping three suspect benchmarks; above 50% on all 15 benchmarks it was tested on, which makes METR 'somewhat nervous about our ability to measure AECI'). METR's Model 4 and the card's Internal Model are very probably the same model (author's confidence about 90%): both are Anthropic's most capable internal model in autumn 2026, both were scored on exactly 15 AECI benchmarks, the values are 178.6 (METR, fit before Nov 5) and 178.78 (card, Nov 6 fit), and the card's internal date (~Sept 26) falls in METR's 'finished training September-October 2026'. Neither source names the other's label, so it is an inference, not a statement. METR gives only training-completion dates (Model 2: July 2026; Model 3: August-September 2026) and no AECI values, public dates or mapping to released names; they are not used. (METR also lists an 'Unreleased 2022' model.)

**Why the default excludes it.** It is unreleased and has no public ECI; its score rests on 15 of Anthropic's internal benchmarks, all above 50%; its date is an internal-availability date while every other point in the model is at its public date; and it is already 51 days past that date with no release. In the default it appears only as a comparison (`p_aeci_nov6_at_or_above_internal_model`). The default's numbers and open predictions are identical to cap-v2.1.

**What the variant assumes** (`variants.with_model_4`; a what-if, not graded). It re-weights the default's own simulated paths by three separately switchable pieces of evidence.

- *Level.* Model 4's public-ECI equivalent is 175.1 (80% 171.6 to 178.7): Fable 5.2's public ECI (173.44) + the same-fit AECI difference to its twin Mythos 5.2 (+1.66); sd combines the two local AECI intervals (1.13), 1.0 for model-specific scatter of the AECI-ECI gap, and Fable 5.2's own ECI posterior sd (2.33; 19 benchmarks so far). The model has no public date. It is not placed on the record line at its internal date (that would steepen the slope artificially, because every other point is at its public date). It enters as a pseudo-observation at a public-date-equivalent of today + a remaining lag; observed lags have lengthened (25 and 47 days for the last two Mythos) and this one is censored at 51 days. Remaining lag: exponential, mean 45 days. The record line at that date is weighted by how well it matches (sd 1.74, the scatter of record-setters about the line).
- *Next release.* With probability p = 0.7 the next Fable/Mythos is Model 4 or at least as capable, so its draws are truncated below at Model 4's level (77% of the default's draws already are). Judgement. For: the one earlier internally reported frontier model (Mythos Preview, internal use from 2026-02-24) shipped within weeks, and every frontier Claude with an internal date has shipped 3-47 days later. Against: the card calls this one a 'research model', it is evaluated nowhere else in the card, and it is already 51 days past its internal date, longer than any earlier lag. Sensitivity at 0.5 and 0.9 is reported.
- *Trend.* Only the scenario weights move, and only between 'reversion' and 'hold'; the recent-slope fit is untouched. The shift is the ratio of the four-line evidence average with and without the internal model on the AECI series, capped so that at most half the reversion weight moves. BIC weight on 'jump or no change' for the AECI series: 0.82 without the internal model, 0.018 with it; four-line average 0.471 to 0.271; reversion weight 0.28 to 0.1609, hold 0.38 to 0.4991. This is the component most open to criticism: the point rests on Anthropic's internal benchmarks, on 15 of them, with the model above 50% on every one (METR is 'somewhat nervous' about measuring it), so the index may be saturating exactly where this point sits.

**Results (median, 80% interval).**

| Public ECI | Default | With Model 4 | Median shift |
|---|---|---|---|
| Claude Opus 5.6 | 173.9 (169.9 to 181.1) | 174.0 (170.1 to 181.3) | +0.1 |
| Claude Sonnet 5.6 | 173.1 (168.5 to 182.3) | 173.4 (168.6 to 182.5) | +0.2 |
| Claude Haiku 6 | 175.2 (165.3 to 198.7) | 176.0 (165.6 to 200.1) | +0.8 |
| Claude Fable / Mythos 5.3 | 178.4 (174.1 to 186.4) | 179.2 (175.1 to 187.6) | +0.8 |
| Anthropic frontier, 2026-12-31 | 174.7 (171.7 to 178.4) | 174.7 (171.7 to 178.4) | +0.0 |
| Anthropic frontier, 2027-12-31 | 194.7 (184.1 to 215.2) | 196.8 (186.1 to 215.4) | +2.1 |
| Anthropic frontier, 2028-12-31 | 212.8 (194.6 to 264.3) | 216.8 (196.8 to 264.1) | +4.0 |
| Anthropic frontier, 2029-12-31 | 229.6 (203.7 to 318.0) | 235.3 (205.9 to 317.2) | +5.7 |
| Anthropic frontier, 2030-12-31 | 245.9 (212.1 to 370.6) | 253.3 (214.5 to 369.6) | +7.4 |

By component (shift in the median):

| Components on | Fable/Mythos 5.3 | Opus 5.6 | Frontier end-2027 | end-2028 | end-2030 | Effective paths |
|---|---|---|---|---|---|---|
| level_only | +0.14 | +0.17 | +0.61 | +1.13 | +2.10 | 17979 |
| next_release_only | +0.88 | +0.05 | +0.59 | +0.93 | +1.59 | 34986 |
| trend_only | +0.06 | +0.03 | +1.40 | +2.89 | +5.47 | 36757 |
| level_and_next_release | +0.70 | +0.11 | +0.73 | +1.37 | +2.50 | 16308 |
| all | +0.82 | +0.14 | +2.14 | +3.99 | +7.38 | 14973 |

Sensitivity to p (all components on): p=0.5: Fable/Mythos 179.0, frontier end-2027 196.8; p=0.7: Fable/Mythos 179.2, frontier end-2027 196.8; p=0.9: Fable/Mythos 179.3, frontier end-2027 196.8. Differences of a tenth or two between rows are Monte Carlo noise. Reading: Model 4 moves the next Fable/Mythos by under a point, because the default already expects the next release to be about that good; nearly all of the long-range shift comes from the trend component, which is the weakest of the three.
