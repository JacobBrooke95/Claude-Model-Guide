# Capability model: methods

Model version `cap-v1.0`, as of 2026-11-16. Every number in this file is written by `python3 capability/run.py` from `capability/output/capability_forecast.json`; do not edit it by hand.

## 1. What is forecast

1. The capability of the next model in each Anthropic family (Opus, Sonnet, Haiku, Fable, Mythos): public ECI, AECI on the November 6 2026 scale, AECI as it will be printed in the model's own system card, and its score on each tracked benchmark.
2. The Anthropic frontier, each family, and the all-lab frontier by quarter to the end of 2030.

**Primary scale.** Public ECI is the modelling scale: 256 models from all labs over four years, published posterior draws, and benchmark-level inputs that let the scale be refitted. AECI has 14 released models on one fit, is built on first-party internal benchmarks and is re-estimated by every card. AECI is the headline *reporting* scale: every prediction is carried to it through the mapping below.

## 2. Data

`build_data.py` writes four tables under `capability/data/` and logs every rename, date conflict, merge and dropped row in `build_log.csv`. Nothing is interpolated.

- **Models** (`models.csv`): 256 models with a public ECI plus the Claude releases Epoch does not score (the four Mythos models, Claude 2.1, Claude 1). Claude release dates are the repo's (`data/models.json`, first public availability); four differ from Epoch's by 4 to 13 days.
- **Index values** (`index_values.csv`): public ECI with 90% credible intervals; every AECI value Anthropic has printed, keyed by the card fit it belongs to. Epoch's 500 joint posterior draws per model are in `raw/eci_posterior_draws.csv.gz`.
- **Benchmark scores** (`benchmark_scores.csv`): one row per benchmark and model in one stated configuration. Site-chart benchmarks use the site's series (`data/benchmarks.json`); other labs are added from Epoch's hub or Artificial Analysis where the same board is the source.
- **Release dates** for the next model in each family come from `forecast/output/forecast.json` and are not re-modelled here.

## 3. Trend model

A frontier series is the set of record-setting releases (running maximum of public ECI by release date). Seven candidate forms are fitted to Anthropic's records, each a regression with Student-t errors (4 degrees of freedom, fitted by IRLS):

| Candidate | Form |
|---|---|
| `lin_all` | one slope, all history |
| `lin_24`, `lin_12` | one slope, trailing 24 or 12 months |
| `hinge` | piecewise linear, changepoint date unknown (profile likelihood over a monthly grid) |
| `jump` | one slope plus a one-time level shift at an unknown date |
| `quad` | quadratic over the trailing 36 months (smooth acceleration) |
| `pool_all` | the all-lab trailing-24-month line plus a mean-reverting Anthropic gap |

Uncertainty: each fit is repeated on bootstrap replicates that resample models and take one of Epoch's 500 joint posterior draws, recomputing the record set each time (this carries the winner's-curse selection of noisy records); coefficients are drawn from a multivariate t; the changepoint is drawn from its profile likelihood.

Two estimands are kept apart. The **level** L(T) is the height of the record line at T: what a record-setter released at T is expected to score. The **frontier** F(T) is the running maximum actually held at T, a step function at or below the line: F(T) = max(F(now), L(T - A) + e), with A the age of the standing record drawn from the observed record gaps.

### Was there a break?

Record-setting releases since Claude 3 Opus (March 2024). 'hinge' = piecewise linear with unknown changepoint; 'jump' = constant slope with a one-time level shift. BIC weights compare the four forms on the published point estimates; the slope-ratio interval is from the bootstrap over models and Epoch posterior draws.

| Series | n | BIC wt linear | hinge | jump | quadratic | Slope before | after | Ratio | Changepoint |
|---|---|---|---|---|---|---|---|---|---|
| Anthropic, public ECI | 16 | 0.00 | 0.30 | 0.01 | 0.69 | 14.41 | 23.64 | 1.64 | 2025.92 |
| All labs, public ECI | 24 | 0.44 | 0.19 | 0.22 | 0.14 | 22.89 | 16.47 | 0.72 | 2024.97 |
| AECI Nov 6 fit, public dates | 14 | 0.00 | 0.17 | 0.82 | 0.01 | 15.49 | 26.34 | 1.70 | 2025.81 |
| AECI Nov 6 fit, internal dates + internal model | 15 | 0.00 | 0.94 | 0.02 | 0.04 | 15.43 | 29.19 | 1.89 | 2025.83 |

With bootstrap uncertainty, the public-ECI slope ratio for Anthropic is 1.57 (1.07 to 2.17) (median, 80% interval): 14.9 points/yr before and 22.4 after. The probability that it reaches the card's 1.88x is 23%. The all-lab public frontier shows no break. So the acceleration Anthropic reports on AECI is partly replicated on the public scale for Anthropic alone, and not at all for the industry frontier.

### Combination

The four combination rules and the seven single candidates score within noise of each other on release folds (the lead is short, so the candidates barely differ at the target date). The frontier folds, with longer horizons, favour the pooled candidate. The live forecast therefore uses the 'blend' rule: the average of the frontier-fold stacking weights, the release-fold stacking weights and equal weights.

| Candidate | Stacking on frontier folds | Stacking on release folds | Equal | Live weight (average) |
|---|---|---|---|---|
| lin_all | 0.05 | 0.05 | 0.14 | 0.08 |
| lin_24 | 0.05 | 0.05 | 0.14 | 0.08 |
| lin_12 | 0.05 | 0.44 | 0.14 | 0.21 |
| hinge | 0.05 | 0.05 | 0.14 | 0.08 |
| jump | 0.05 | 0.05 | 0.14 | 0.08 |
| quad | 0.05 | 0.05 | 0.14 | 0.08 |
| pool_all | 0.70 | 0.31 | 0.14 | 0.38 |

Stacking minimises the mean CRPS of the mixture over folds, with a 5% floor per candidate. All-lab frontier weights: lin_all 0.05, lin_24 0.55, lin_12 0.25, hinge 0.05, jump 0.05, quad 0.05.

## 4. Families

Offsets are ECI minus the piecewise reference line through Anthropic's record-setters, weighted toward recent releases (half-life 1.5 years). 'pooled' is the empirical-Bayes estimate used by the 'mean' predictor; 'last' is the family's most recent offset, used by the 'last' predictor.

| Family | n | Effective n | Unpooled mean | Pooled mean | SE | Shrinkage | Last offset |
|---|---|---|---|---|---|---|---|
| fable | 3 | 2.98 | 1.01 | 0.58 | 1.04 | 0.14 | 1.69 |
| haiku | 4 | 3.32 | -8.48 | -7.67 | 0.99 | 0.13 | -9.27 |
| opus | 9 | 8.33 | -0.33 | -0.42 | 0.65 | 0.06 | -0.23 |
| sonnet | 9 | 7.83 | -2.44 | -2.42 | 0.67 | 0.06 | -2.59 |

Within-family sd 1.93, between-family sd 2.77. The next offset is a mixture: weight 0.66 on the family's last offset and the rest on its pooled mean (weight set by CRPS stacking over backtest folds), plus Student-t scatter. A version-type effect (new generation / x.5 / minor) was estimated (gen -0.33, half +0.23, minor +0.13 ECI points) and tested: CRPS 1.775 with it, 1.741 without. It is not used. Mythos is the restricted twin of Fable (same underlying model per Anthropic). Public ECI scores Fable only, so on the ECI scale Mythos uses Fable's history; AECI is printed for Mythos only.

## 5. AECI: mapping and drift

Below public ECI ~157 (through Opus 4.6) the two scales agree within about 1 point. For every model released since June 2026 AECI is 3.7-6.2 points higher. A one-time level shift fits that better than a steadily widening gap, but five points cannot separate the two, so both forms are carried.

| Model | Public ECI | AECI (Nov 6) | Hinge fit | Level-shift fit | AECI source |
|---|---|---|---|---|---|
| Claude 3 Opus | 125.52 | 124.70 | 125.80 | 125.88 | figure_read |
| Claude 3.5 Sonnet | 130.00 | 130.00 | 130.28 | 130.36 | anchor_by_definition |
| Claude 3.5 Sonnet (October 2024) | 133.43 | 133.70 | 133.71 | 133.79 | figure_read |
| Claude 3.7 Sonnet | 141.00 | 141.30 | 141.28 | 141.36 | figure_read |
| Claude Opus 4 | 142.90 | 144.70 | 143.18 | 143.26 | figure_read |
| Claude Sonnet 4.5 | 147.63 | 147.70 | 147.91 | 147.99 | figure_read |
| Claude Opus 4.5 | 151.92 | 152.20 | 152.68 | 152.28 | figure_read |
| Claude Opus 4.6 | 156.34 | 157.30 | 158.21 | 156.70 | figure_read |
| Claude Mythos 5 | 164.13 | 168.68 | 167.95 | 169.09 | printed |
| Claude Opus 5 | 164.68 | 169.40 | 168.64 | 169.64 | printed |
| Claude Mythos 5.1 | 166.99 | 172.62 | 171.53 | 171.95 | printed |
| Claude Opus 5.5 | 168.54 | 174.78 | 173.46 | 173.50 | printed |
| Claude Mythos 5.2 | 173.44 | 177.12 | 179.59 | 178.40 | printed |

Hinge: knee 150.0, slope above it 1.25. Level shift: +4.61 above 156.5. Overlap RMSE: hinge 1.07, level shift 0.78. In the bootstrap the level-shift form fits better in 60% of replicates; the forecast uses it with probability 0.60 (clipped to 0.2-0.8 so neither form is ruled out on 13 points). Residual sd used: 1.21 AECI points, which includes the miss on the two site-rescaled values (Sonnet 5.5, Haiku 5.5) that were not used in the fit: Claude Sonnet 5.5 site estimate 173.6, mapped 171.52 / 170.99; Claude Haiku 5.5 site estimate 167.3, mapped 165.39 / 163.32.

**Drift.** Per-refit change in printed AECI of frontier models between consecutive card fits. Seven transitions: five near zero, two near +5 (the Sept 18 fit and the Haiku 5.5 card fit).

| Refit (card) | Mean change of models in both fits | Models |
|---|---|---|
| fable5 | 0.61 | 1 |
| opus5 | 0.01 | 1 |
| fable5.1 | -1.60 | 2 |
| opus5.5 | 5.21 | 3 |
| sonnet5.5 | -0.24 | 1 |
| haiku5.5 | 5.44 | 1 |
| fable5.2 | 0.22 | 1 |

Mean 1.38 per refit, sd 2.78. The own-card prediction adds, for each refit expected before the model's card (one per card; other families' releases counted from the release forecaster), a step resampled from these seven, plus sd 0.7 for the own-card measurement. Leave-one-out check of the step distribution: 71% of the seven inside the 80% interval. n = 7; this is the least-tested part of the model.

## 6. Benchmark links

Bounded scores: p = (score - floor)/(ceiling - floor) = sigmoid(a(ability - D)), noise Student-t on the logit scale so draws respect the bounds. Elo and other unbounded scores: linear in ability. METR horizon: log2(minutes) linear in ability. Own fit for every benchmark. Where the benchmark is in public ECI, Epoch's item parameters are shown beside the fit and the fit's RMSE under Epoch's parameters is reported; they agree closely wherever the data are the same (GPQA, FrontierMath, ARC-AGI-2, RLI, Terminal-Bench 2.0).

| Benchmark | Link | n | Slope | Difficulty (ECI at 50%) | ECI from 50% to 90% | Fit RMSE | Epoch slope | Epoch difficulty | Configuration |
|---|---|---|---|---|---|---|---|---|---|
| SWE-bench Pro | bounded | 13 | 0.103 | 151.93 | 21.20 | 3.65 | - | - | Anthropic system cards, mean of five trials (first-party) |
| Terminal-Bench 2.1 | bounded | 10 | 0.084 | 146.95 | 26.20 | 2.78 | - | - | Vals AI harness snapshot |
| OSWorld | bounded | 16 | 0.103 | 145.57 | 21.40 | 5.72 | 0.150 | 146.75 | Anthropic-reported; three eval versions on one series (original, Verified, 2.1 partial credit) |
| GDPval-AA v2.1 | elo | 46 | 44.714 | - | - | - | - | - | Artificial Analysis v2.1, strongest (max-effort) config per release |
| Remote Labor Index | bounded | 17 | 0.162 | 176.16 | 13.60 | 1.46 | 0.152 | 176.75 | Scale AI / CAIS leaderboard; Fable 5.2 Anthropic-reported |
| ARC-AGI-2 | bounded | 90 | 0.262 | 154.21 | 8.40 | 8.13 | 0.218 | 154.63 | ARC Prize leaderboard, strongest listed config per model |
| Humanity's Last Exam (no tools) | bounded | 15 | 0.088 | 161.44 | 24.90 | 3.12 | - | - | Anthropic system cards, no-tools, max effort / adaptive thinking (first-party) |
| ForecastBench (baseline) | linear | 16 | 0.098 | - | - | - | - | - | ForecastBench baseline board, best config per model; prompt set-ups differ by model |
| Vending-Bench 2 | linear | 61 | 438.386 | - | - | - | - | - | Andon Labs leaderboard, mean final balance |
| METR 50% time horizon (TH1.1) | loghorizon | 20 | 0.210 | - | - | - | - | - | METR-Horizon-v1.1 YAML; coverage ends with Mythos Preview (May 2026) |
| GPQA Diamond | bounded | 176 | 0.117 | 133.70 | 18.70 | 2.91 | 0.116 | 133.91 | Epoch hub, best score across configs; chance 25%, ceiling 97% per Epoch |
| FrontierMath Tiers 1-3 | bounded | 90 | 0.165 | 150.80 | 13.30 | 5.84 | 0.166 | 150.71 | Epoch hub (v2 private set), best config; ceiling 95% per Epoch |
| Terminal-Bench 2.0 | bounded | 32 | 0.160 | 149.38 | 13.80 | 5.91 | 0.164 | 149.42 | Epoch hub 'Terminal Bench', best accuracy per model; coverage ends April 2026 |
| WebDev Arena | elo | 80 | 17.852 | - | - | - | - | - | Epoch hub copy of LMArena WebDev scores, best per model |
| LMArena text | elo | 114 | 6.134 | - | - | - | - | - | LMArena text 'overall', latest snapshot per model (style-controlled era) |
| AA Intelligence Index v5 | bounded | 31 | 0.098 | 165.93 | 22.30 | 3.26 | - | - | Artificial Analysis v5.0.1, strongest config per release |
| Vals Index v2.2 | bounded | 23 | 0.065 | 155.71 | 33.80 | 5.45 | - | - | Vals Index v2.2 overall, best config per model |

METR: 4.75 ECI points per doubling of the 50% horizon (90% interval 4.47 to 5.07; Epoch says about 5).

Dropped: ARC-AGI-3 (only 7 models with both a public ECI and a score (minimum 8)); Terminal-Bench 4.0 (scores exist for five Claude models only (Artificial Analysis), all released Sept-Nov 2026).

## 7. Backtest

### 7.1 Claude releases

Folds are (Claude release, lead) for leads of 0, 3 and 6 months. The origin is the release date minus the lead; everything is refitted on models released strictly before the origin; the model is given the release's actual date and version type. A fold exists only if the release is the next one in its family as seen from the origin, which is why few folds exist at 3 and 6 months (families ship every ~3 months). Lead 0 is a day-of nowcast. Baseline intervals are a normal centred on the baseline with the sd of its own earlier errors at that lead (from its 5th fold). Tables use the folds on which every baseline exists.

**Day-of nowcast (lead 0)**

| Method | n | Bias (actual - predicted) | MAE | RMSE | CRPS | Cov 50% | Cov 80% | Cov 95% |
|---|---|---|---|---|---|---|---|---|
| Model | 19 | 0.51 | 1.94 | 2.35 | 1.42 | 0.63 | 0.89 | 1.00 |
| Baseline: trailing-12-month all-lab trend at the date | 19 | -4.22 | 4.50 | 5.53 | 2.83 | 0.33 | 0.67 | 0.80 |
| Baseline: all-history all-lab linear trend at the date | 19 | -3.67 | 4.28 | 5.09 | 2.95 | 0.40 | 0.60 | 0.80 |
| Baseline: previous + family's mean step | 19 | -0.66 | 4.32 | 5.88 | 3.24 | 0.67 | 0.93 | 0.93 |
| Baseline: previous model in family | 19 | 6.75 | 6.75 | 8.52 | 4.58 | 0.27 | 0.80 | 0.80 |

**3 months ahead**

| Method | n | Bias (actual - predicted) | MAE | RMSE | CRPS | Cov 50% | Cov 80% | Cov 95% |
|---|---|---|---|---|---|---|---|---|
| Model | 8 | 1.37 | 1.48 | 1.98 | 1.37 | 0.88 | 1.00 | 1.00 |
| Baseline: trailing-12-month all-lab trend at the date | 8 | -5.91 | 5.91 | 6.69 | 4.01 | 0.00 | 0.50 | 0.75 |
| Baseline: all-history all-lab linear trend at the date | 8 | -4.18 | 6.56 | 7.07 | 4.27 | 0.25 | 0.75 | 1.00 |
| Baseline: previous + family's mean step | 8 | 2.79 | 3.90 | 5.64 | 1.95 | 0.75 | 1.00 | 1.00 |
| Baseline: previous model in family | 8 | 10.33 | 10.33 | 11.82 | 6.10 | 0.00 | 0.75 | 0.75 |
| Model, release date not given (cadence reconstruction) | 8 | 0.56 | 2.20 | 2.62 | 1.77 | 0.88 | 1.00 | 1.00 |

**6 months ahead**

| Method | n | Bias (actual - predicted) | MAE | RMSE | CRPS | Cov 50% | Cov 80% | Cov 95% |
|---|---|---|---|---|---|---|---|---|
| Model | 3 | 2.89 | 2.89 | 2.93 | 1.93 | 1.00 | 1.00 | 1.00 |
| Baseline: trailing-12-month all-lab trend at the date | 3 | -7.31 | 7.31 | 8.22 | - | - | - | - |
| Baseline: all-history all-lab linear trend at the date | 3 | -3.36 | 8.23 | 8.26 | - | - | - | - |
| Baseline: previous + family's mean step | 3 | 8.67 | 8.67 | 9.05 | - | - | - | - |
| Baseline: previous model in family | 3 | 17.63 | 17.63 | 17.63 | - | - | - | - |
| Model, release date not given (cadence reconstruction) | 3 | 5.74 | 5.74 | 5.90 | 3.57 | 0.33 | 1.00 | 1.00 |

Errors are in public-ECI points. The model beats every baseline at every lead on RMSE and CRPS. It under-predicts on average (positive bias, growing with lead). The model under-predicted on average (positive bias). Subtracting the rolling mean of earlier errors did not reduce out-of-sample error, so no correction is applied. Not knowing the release date roughly doubles the error at 6 months.

Combination rules and single candidates, same folds:

| Lead (yr) | Variant | n | RMSE | CRPS | Cov 80% |
|---|---|---|---|---|---|
| 0.00 | rule_blend | 19 | 2.42 | 1.45 | 0.89 |
| 0.00 | rule_stack_frontier | 19 | 2.39 | 1.44 | 0.89 |
| 0.00 | rule_equal | 19 | 2.42 | 1.44 | 0.89 |
| 0.00 | rule_stack_release | 19 | 2.46 | 1.46 | 0.95 |
| 0.00 | cand_lin_all | 19 | 2.83 | 1.61 | 0.84 |
| 0.00 | cand_lin_24 | 19 | 2.42 | 1.43 | 0.89 |
| 0.00 | cand_lin_12 | 19 | 2.36 | 1.44 | 0.95 |
| 0.00 | cand_hinge | 19 | 2.38 | 1.45 | 0.95 |
| 0.00 | cand_jump | 19 | 2.61 | 1.53 | 0.89 |
| 0.00 | cand_quad | 19 | 2.42 | 1.49 | 0.95 |
| 0.00 | cand_pool_all | 19 | 2.66 | 1.55 | 0.89 |
| 0.00 | type_effect_on | 19 | 2.43 | 1.45 | 0.95 |
| 0.00 | type_effect_off | 19 | 2.40 | 1.44 | 0.89 |
| 0.25 | rule_blend | 8 | 1.95 | 1.39 | 1.00 |
| 0.25 | rule_stack_frontier | 8 | 1.98 | 1.38 | 1.00 |
| 0.25 | rule_equal | 8 | 2.00 | 1.38 | 1.00 |
| 0.25 | rule_stack_release | 8 | 2.01 | 1.39 | 1.00 |
| 0.25 | cand_lin_all | 8 | 2.16 | 1.37 | 1.00 |
| 0.25 | cand_lin_24 | 8 | 2.04 | 1.32 | 1.00 |
| 0.25 | cand_lin_12 | 8 | 2.18 | 1.45 | 1.00 |
| 0.25 | cand_hinge | 8 | 2.19 | 1.47 | 1.00 |
| 0.25 | cand_jump | 8 | 2.30 | 1.45 | 1.00 |
| 0.25 | cand_quad | 8 | 2.11 | 1.53 | 1.00 |
| 0.25 | cand_pool_all | 8 | 1.88 | 1.54 | 1.00 |
| 0.25 | type_effect_on | 8 | 2.08 | 1.42 | 1.00 |
| 0.25 | type_effect_off | 8 | 2.00 | 1.39 | 1.00 |

### 7.2 Frontier at fixed horizons

Monthly origins; target = running-max public ECI held at origin + h. Candidates are refitted on models released before each origin (bootstrap B=20). 'stacked' uses weights learned only from folds whose target date precedes the origin (equal weights until 10 such folds exist).

| Series | Horizon (yr) | Method | n | Bias | MAE | RMSE | CRPS | Cov 50% | Cov 80% | Cov 95% |
|---|---|---|---|---|---|---|---|---|---|---|
| all | 0.50 | lin_all | 23 | 4.62 | 4.62 | 5.43 | 3.21 | 0.70 | 1.00 | 1.00 |
| all | 0.50 | lin_12 | 23 | 3.29 | 3.41 | 4.16 | 2.41 | 0.52 | 1.00 | 1.00 |
| all | 0.50 | hinge | 23 | 2.99 | 3.42 | 4.93 | 2.46 | 0.70 | 0.91 | 1.00 |
| all | 0.50 | persistence | 23 | 8.65 | 8.65 | 8.92 | 8.65 | 0.00 | 0.00 | 0.00 |
| all | 0.50 | stacked | 23 | 4.11 | 4.11 | 5.15 | 2.68 | 0.70 | 1.00 | 1.00 |
| all | 1.00 | lin_all | 17 | 6.54 | 7.70 | 8.53 | 5.64 | 0.82 | 1.00 | 1.00 |
| all | 1.00 | lin_12 | 17 | 3.42 | 3.56 | 4.81 | 3.35 | 0.88 | 1.00 | 1.00 |
| all | 1.00 | hinge | 17 | 4.10 | 4.81 | 6.85 | 3.75 | 0.71 | 1.00 | 1.00 |
| all | 1.00 | persistence | 17 | 16.78 | 16.78 | 16.84 | 16.78 | 0.00 | 0.00 | 0.00 |
| all | 1.00 | stacked | 17 | 5.79 | 5.91 | 7.16 | 4.33 | 0.94 | 1.00 | 1.00 |
| all | 1.50 | lin_all | 11 | 9.72 | 12.84 | 13.74 | 9.54 | 0.73 | 1.00 | 1.00 |
| all | 1.50 | lin_12 | 11 | 4.35 | 5.59 | 7.09 | 5.05 | 0.91 | 1.00 | 1.00 |
| all | 1.50 | hinge | 11 | 8.99 | 9.47 | 12.17 | 6.71 | 0.55 | 1.00 | 1.00 |
| all | 1.50 | persistence | 11 | 25.39 | 25.39 | 25.46 | 25.39 | 0.00 | 0.00 | 0.00 |
| all | 1.50 | stacked | 11 | 10.57 | 10.57 | 12.06 | 7.64 | 0.91 | 1.00 | 1.00 |
| anth | 0.50 | lin_all | 16 | 4.23 | 4.23 | 4.76 | 2.93 | 0.31 | 0.75 | 0.94 |
| anth | 0.50 | lin_12 | 16 | 3.78 | 3.78 | 4.36 | 2.52 | 0.38 | 0.88 | 1.00 |
| anth | 0.50 | hinge | 16 | 3.70 | 3.70 | 4.21 | 2.44 | 0.38 | 0.94 | 1.00 |
| anth | 0.50 | pool_all | 16 | 2.64 | 2.94 | 3.45 | 2.22 | 0.50 | 0.81 | 1.00 |
| anth | 0.50 | persistence | 16 | 9.27 | 9.27 | 9.55 | 9.27 | 0.00 | 0.00 | 0.00 |
| anth | 0.50 | stacked | 16 | 3.59 | 3.59 | 4.11 | 2.43 | 0.44 | 0.81 | 1.00 |
| anth | 1.00 | lin_all | 10 | 6.05 | 6.05 | 6.43 | 4.06 | 0.30 | 0.70 | 1.00 |
| anth | 1.00 | lin_12 | 10 | 5.83 | 5.83 | 6.18 | 3.77 | 0.40 | 0.80 | 1.00 |
| anth | 1.00 | hinge | 10 | 6.14 | 6.14 | 6.51 | 3.95 | 0.30 | 0.80 | 1.00 |
| anth | 1.00 | pool_all | 10 | 3.30 | 3.82 | 4.42 | 2.81 | 0.70 | 1.00 | 1.00 |
| anth | 1.00 | persistence | 10 | 18.73 | 18.73 | 18.88 | 18.73 | 0.00 | 0.00 | 0.00 |
| anth | 1.00 | stacked | 10 | 5.57 | 5.57 | 5.93 | 3.57 | 0.40 | 0.80 | 1.00 |
| anth | 1.50 | lin_all | 4 | 7.68 | 7.68 | 7.72 | 4.62 | 0.00 | 1.00 | 1.00 |
| anth | 1.50 | lin_12 | 4 | 7.91 | 7.91 | 8.00 | 4.84 | 0.00 | 1.00 | 1.00 |
| anth | 1.50 | hinge | 4 | 7.65 | 7.65 | 7.72 | 4.66 | 0.00 | 1.00 | 1.00 |
| anth | 1.50 | pool_all | 4 | 6.16 | 6.16 | 8.69 | 5.41 | 0.75 | 1.00 | 1.00 |
| anth | 1.50 | persistence | 4 | 27.50 | 27.50 | 27.63 | 27.50 | 0.00 | 0.00 | 0.00 |
| anth | 1.50 | stacked | 4 | 7.24 | 7.24 | 7.35 | 4.39 | 0.25 | 1.00 | 1.00 |

Every trend form under-predicted the frontier over 2024-26, by about 6 ECI points at one year for the stacked model: the pace rose during the test window. Folds overlap heavily (monthly origins), so the effective sample is far below n.

### 7.3 Benchmark scores

Same folds as the release backtest. Each benchmark's link is refitted on models released before the origin (and must pass the inclusion rule at that date); the release's score is predicted from (a) its predicted ability ('model') and (b) its true ability ('link_given_true_ability', isolating link error). Baseline: the previous model in the family on the same benchmark.

| Benchmark | n | MAE model | MAE previous-in-family | Model better |
|---|---|---|---|---|
| aa_index | 3 | 4.07 | 19.51 | True |
| arc_agi_2 | 16 | 14.48 | 26.40 | True |
| forecastbench | 11 | 1.64 | 1.30 | False |
| frontiermath_t13 | 12 | 5.56 | 17.92 | True |
| gdpval_aa | 12 | 104.21 | 378.50 | True |
| gpqa_diamond | 29 | 3.40 | 12.08 | True |
| hle | 8 | 4.21 | 15.63 | True |
| lmarena_text | 29 | 36.52 | 48.91 | True |
| metr_h50 | 9 | 81.06 | 131.10 | True |
| osworld | 10 | 5.29 | 10.40 | True |
| rli | 2 | 7.99 | 18.15 | True |
| swe_bench_pro | 4 | 5.25 | 10.45 | True |
| terminal_bench_2 | 6 | 11.23 | 13.53 | True |
| terminal_bench_2_1 | 2 | 3.75 | 5.80 | True |
| vending_bench_2 | 14 | 2994.66 | 2951.29 | False |
| webdev_arena | 12 | 56.99 | 93.20 | True |

With the true ability known, link error on bounded benchmarks is RMSE 0.093 and MAE 0.063 of the score range (held-out RMSE 0.092, MAE 0.067 with ability known (research note 1)). The model loses to 'previous in family' on ForecastBench and Vending-Bench 2, where scores barely track ability; treat those two predictions as weak.

### 7.4 Leave-future-out IRT refit

Own least-squares 2PL refit of Epoch's benchmark-level inputs. For every fold origin, the IRT is refitted on models released on or before that date only and mapped to ECI units by a monotone alignment to the published ECI of those same models; the release backtest is rerun with history from the origin's vintage and the target's 'actual' from the release date's vintage.

Reproduction on all data: correlation 0.9973 with Epoch's published ECI, RMSE 0.67 above ECI 140 (1.98 overall). Vintage versus published ability of the target: mean shift 0.08, mean absolute 0.82, maximum 2.59 ECI points over 33 folds.

| Lead (yr) | n | RMSE vintage | RMSE published | Bias vintage | Bias published | Cov 80% vintage | Cov 80% published |
|---|---|---|---|---|---|---|---|
| 0.0 | 20 | 2.88 | 2.64 | 1.30 | 0.78 | 0.95 | 0.85 |
| 0.25 | 9 | 3.37 | 2.85 | 2.41 | 1.93 | 0.89 | 0.89 |
| 0.5 | 4 | 5.30 | 4.70 | 4.50 | 4.15 | 0.75 | 1.00 |

Using today's abilities for past models (the look-ahead in the scale) flatters the backtest slightly: errors are about 10-20% larger on vintage abilities. Scores in Epoch's input file are today's collection; a score measured after the origin for a model released before it cannot be removed (no timestamps).

## 8. Calibration

Conformal-style: per nominal level, the factor by which the interval must be stretched about the median to cover the stated share of backtest outcomes; learned on earlier folds only when scoring (rolling), and on all folds for the live forecast; floored at 1.

| Set | Folds | Raw 50% | Raw 80% | Raw 95% | Folds scored rolling | Calibrated 50% | 80% | 95% | Factor 50% | 80% | 95% | 80% factor before floor |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ability, day-of | 20 | 0.60 | 0.85 | 1.00 | 12 | 0.58 | 0.83 | 1.00 | 1.00 | 1.00 | 1.00 | 0.69 |
| Ability, 3-6 months ahead | 13 | 0.77 | 0.92 | 1.00 | 6 | 0.67 | 0.83 | 1.00 | 1.00 | 1.00 | 1.00 | 0.99 |
| Benchmark scores, pooled | 221 | 0.48 | 0.81 | 0.98 | 207 | 0.49 | 0.80 | 0.98 | 1.05 | 1.00 | 1.00 | 0.96 |

Raw intervals already cover at or above nominal for ability, so the factors sit at or near 1 and calibration changes little; the unfloored factors below 1 say the raw intervals are, if anything, slightly wide. They are not narrowed. AECI intervals use the ability factors; there is no AECI backtest beyond the drift check.

## 9. Next-model predictions

Each draw samples a release date from the forecaster's distribution, then the trend level at that date, the family offset and the version type. Anthropic's Fable 5.2 card prints an unreleased internal model at AECI 178.78 (15 benchmarks, internal date ~2026-09-26). It is not used in the fit; p_aeci_at_or_above_internal_model compares the prediction with it.

| Family | Likeliest name | Release (median, 10-90%) | Previous ECI | Public ECI (80%) | AECI Nov 6 scale (80%) | AECI own card (80%) | P(AECI >= internal model) |
|---|---|---|---|---|---|---|---|
| opus | Claude Opus 5.6 | 2026-12-14 (2026-11-20 to 2027-02-22) | 168.54 | 172.7 (168.0 to 178.2) | 178.2 (172.1 to 185.9) | 180.2 (172.8 to 190.0) | 0.45 |
| sonnet | Claude Sonnet 5.6 | 2027-01-21 (2026-12-01 to 2027-04-02) | 166.56 | 171.8 (166.7 to 178.2) | 177.3 (170.6 to 185.8) | 180.3 (171.8 to 192.0) | 0.40 |
| haiku | Claude Haiku 6 | 2027-07-13 (2027-02-03 to 2027-11-23) | 160.43 | 173.1 (164.2 to 184.8) | 178.6 (168.3 to 192.4) | 188.4 (171.8 to 210.3) | 0.49 |
| fable | Claude Fable 5.3 | 2027-02-02 (2026-12-14 to 2027-04-13) | 173.44 | 176.3 (170.9 to 182.6) | 182.1 (175.1 to 191.1) | 185.6 (176.5 to 197.7) | 0.72 |
| mythos | Claude Mythos 5.3 | 2027-01-26 (2026-12-10 to 2027-03-30) | 173.44 | 175.9 (170.7 to 182.1) | 181.6 (174.8 to 190.4) | 185.0 (176.2 to 196.5) | 0.69 |

Benchmarks, median with 80% interval:

| Benchmark | Opus | Sonnet | Haiku | Fable / Mythos |
|---|---|---|---|---|
| SWE-bench Pro | 89.8 (83.4 to 94.5) | 88.9 (81.5 to 94.4) | 90.1 (77.8 to 97.1) | 92.7 (87.1 to 96.5) |
| Terminal-Bench 2.1 | 90.1 (84.9 to 94.1) | 89.4 (83.5 to 94.1) | 90.3 (80.8 to 96.4) | 92.5 (87.9 to 95.9) |
| OSWorld | 94.2 (88.2 to 97.4) | 93.7 (86.9 to 97.3) | 94.3 (85.0 to 98.5) | 95.8 (90.8 to 98.4) |
| GDPval-AA v2.1 | 2088 (1794 to 2415) | 2047 (1734 to 2406) | 2101 (1664 to 2673) | 2246 (1920 to 2605) |
| Remote Labor Index | 35.6 (20.5 to 57.5) | 32.4 (17.2 to 57.3) | 36.8 (12.5 to 78.5) | 49.1 (28.6 to 73.4) |
| ARC-AGI-2 | 99.2 (95.9 to 99.9) | 99.0 (94.2 to 99.9) | 99.3 (88.5 to 100.0) | 99.7 (97.9 to 100.0) |
| Humanity's Last Exam (no tools) | 73.2 (63.3 to 82.4) | 71.6 (60.6 to 82.1) | 73.8 (55.7 to 89.0) | 78.8 (68.8 to 87.2) |
| ForecastBench (baseline) | 61.3 (58.6 to 64.0) | 61.2 (58.6 to 64.0) | 61.3 (58.6 to 64.3) | 61.7 (58.8 to 64.5) |
| Vending-Bench 2 | 13551 (9818 to 17608) | 13230 (9306 to 17502) | 13800 (8731 to 19860) | 15123 (11097 to 19468) |
| METR 50% time horizon (TH1.1) | 5068 (2247 to 12811) | 4471 (1888 to 12317) | 5338 (1368 to 30597) | 8504 (3416 to 24116) |
| GPQA Diamond | 96.3 (95.6 to 96.7) | 96.2 (95.3 to 96.7) | 96.3 (94.8 to 96.8) | 96.5 (96.0 to 96.8) |
| FrontierMath Tiers 1-3 | 92.5 (89.2 to 94.1) | 92.2 (87.9 to 94.1) | 92.7 (84.8 to 94.7) | 93.6 (91.3 to 94.6) |
| Terminal-Bench 2.0 | 97.6 (94.5 to 99.1) | 97.3 (93.3 to 99.1) | 97.8 (90.9 to 99.7) | 98.6 (96.5 to 99.6) |
| WebDev Arena | 1846 (1731 to 1974) | 1830 (1710 to 1970) | 1853 (1676 to 2075) | 1908 (1784 to 2049) |
| LMArena text | 1563 (1514 to 1617) | 1558 (1506 to 1615) | 1565 (1498 to 1650) | 1584 (1532 to 1643) |
| AA Intelligence Index v5 | 66.3 (54.0 to 78.2) | 64.5 (51.0 to 78.0) | 67.1 (45.4 to 86.9) | 73.8 (61.3 to 84.6) |
| Vals Index v2.2 | 75.2 (67.4 to 82.8) | 74.1 (65.5 to 82.5) | 75.6 (63.0 to 87.6) | 79.1 (70.9 to 86.6) |

Mythos shares Fable's ability; its release window differs slightly, so its numbers in the JSON differ by a few tenths.

## 10. Projection, 2026-2030

Pace on the public-ECI scale is decomposed with the driver tables: pace(t) = kappa x log10(compute growth in year t) + a0 x m(t), with kappa = 9.0 +/- 2.0 ECI per 10x training compute (research note 1), a0 the algorithmic share at the pre-break pace (pre-break slope minus kappa x log10(5), 5x/yr being Epoch's compute trend), and m(t) a multiplier on algorithmic progress. The post-break public slope implies m = 2.01 (80% 1.1 to 3.38); METR and the AI Futures Project attribute 1.7-1.9x to AI assistance. Scenarios differ only in the compute path and m(t):

| Scenario | Definition | ECI pts/yr 2027 (80%) | 2028 | 2030 | AECI pts/yr 2027 | x pre-break pace, 2027 |
|---|---|---|---|---|---|---|
| slowdown | Compute/supply-limited: training-compute growth falls on the 'low' driver path (2.5x, 2x, 1.5x, 1.5x per year 2027-30) and algorithmic progress falls back to 0.6-1.0x its pre-break rate within a year. | 14.2 (11.6 to 18.2) | 9.50 | 8.40 | 15.60 | 0.96 |
| reversion | One-time jump: the 2025-26 step up was a level shift. Pace returns within six months to 1.0-1.4x the pre-break slope (at 5x/yr compute), then follows the 'central' compute path down. | 18.8 (15.1 to 23.5) | 17.00 | 15.20 | 20.60 | 1.26 |
| hold | New trend holds: algorithmic progress stays at the multiplier implied by the post-break slope; compute follows the 'central' driver path (5x, 4x, 3x, 2.5x). | 22.5 (18.0 to 31.2) | 21.60 | 19.80 | 24.90 | 1.57 |
| compounding | AI R&D feedback: the algorithmic multiplier doubles every 6-12 months until it reaches 4-7.5x (total pace ~3-5x pre-break, as in research note 3), then stays there; 60-100% of the excess over 'hold' is realised; compute on the 'central' or 'high' path. | 32.7 (24.9 to 45.4) | 45.50 | 47.00 | 36.10 | 2.29 |
| explosive | Bounded explosive tail: the multiplier doubles every 3-6 months to a peak of 8-30x (Forethought's 'won't be 30X' cap), holds 1-2 years, then settles at 3-6x; same 60-100% realisation haircut. | 54.6 (37.0 to 84.5) | 109.50 | 42.70 | 60.10 | 3.76 |

On top of each path: a random walk with annual sd 4.34 ECI points (the spread of one-year frontier errors in backtest), trend-parameter draws for the starting level, record-age and residual noise for the step-function frontier. The all-lab frontier is the larger of Anthropic's and a rival frontier whose gap to Anthropic mean-reverts to its 2024-26 average (+2.6 ECI, sd 2.93; today -3.7). Families sit at the record line lagged by their release cadence plus their pooled offset, which is allowed to drift.

### Weights

The data cannot set these weights alone, so they are an explicit prior built in two steps.

*Step 1, data only.* Three lines of evidence on whether the step-up reverts, averaged: (a) the reference class of earlier apparent accelerations in the ECI frontier and METR horizons, Laplace-smoothed: 0.2; (b) BIC weight on 'jump or no change' for Anthropic's public-ECI records: 0.009; (c) BIC weight on 'no slope increase' for the all-lab frontier: 0.856. Combined P(revert) = 0.355. The remainder is split between 'hold' and 'compounding' by the reference class (share that accelerated again: 0.292). The reference class is two independent episodes (the 2024 break in ECI and in METR horizons); both persisted for 12 months or more, one accelerated again. Slowdown and explosive have no precedent in the sample and get zero by construction.

*Step 2, central prior.* Data-only weights scaled to 84%, plus 10% slowdown and 6% explosive. Reasons for the tails: compute growth cannot stay at 5x/yr (lead times, capital, possible export restrictions; research note 1), which argues for a slowdown tail; Anthropic's S-1/A says the AI R&D threshold is met on the 'expect' prong and takeoff models put large mass on rapid acceleration, which argues for an explosive tail; scenario-style forecasts have run at 60-75% of predicted pace, which is why that tail is small and why accelerating scenarios carry a realisation haircut. The orchestrator's note in research note 3 is followed: the collecting worker's 15/35/30/20 is kept only as the 'accelerationist' alternative.

| Weighting | Slowdown | Reversion | Hold | Compounding | Explosive |
|---|---|---|---|---|---|
| central | 0.10 | 0.30 | 0.38 | 0.16 | 0.06 |
| sceptic | 0.20 | 0.45 | 0.28 | 0.06 | 0.01 |
| accelerationist | 0.00 | 0.15 | 0.35 | 0.30 | 0.20 |
| data_only | 0.00 | 0.35 | 0.46 | 0.19 | 0.00 |

### Results (central weights)

| Date | Anthropic frontier, public ECI (80%) | 95% | AECI Nov 6 scale (80%) | 95% | All-lab public ECI (80%) | Implied 50% horizon, hours (median) |
|---|---|---|---|---|---|---|
| 2026-12-31 | 173.4 (173.4 to 176.9) | 173.4 to 179.5 | 177.1 (177.1 to 184.1) | 177.1 to 188.9 | 174.3 (173.4 to 178.2) | 101 |
| 2027-12-31 | 194.8 (184.9 to 212.1) | 180.1 to 231.2 | 202.6 (190.2 to 226.1) | 184.8 to 249.7 | 198.1 (187.9 to 215.4) | 2,128 |
| 2028-12-31 | 215.9 (198.0 to 264.4) | 190.1 to 348.0 | 226.2 (204.6 to 285.6) | 195.8 to 381.2 | 219.2 (201.3 to 267.4) | 45,968 |
| 2029-12-31 | 235.3 (209.5 to 319.1) | 198.0 to 456.8 | 248.1 (217.1 to 346.5) | 204.5 to 509.2 | 238.4 (213.0 to 322.1) | 100,000+ |
| 2030-12-31 | 254.1 (220.3 to 372.7) | 205.3 to 513.5 | 269.4 (228.8 to 404.6) | 212.2 to 580.8 | 257.5 (223.7 to 375.4) | 100,000+ |

Implied METR-style 50% time horizon from the fitted link (4.75 ECI points per doubling; METR's own measurements stop at 17.4 hours, Mythos Preview, and METR calls anything above 16 hours unreliable). Everything here is extrapolation; values are capped at 100000 hours (about 50 work-years), beyond which the number has no operational meaning.

### Sensitivity to the prior

| Weighting | Series | Date | Median | 80% low | 80% high |
|---|---|---|---|---|---|
| central | anthropic_frontier_eci | 2028-12-31 | 216 | 198 | 264 |
| central | anthropic_frontier_eci | 2030-12-31 | 254 | 220 | 373 |
| central | anthropic_frontier_aeci | 2028-12-31 | 226 | 205 | 286 |
| central | anthropic_frontier_aeci | 2030-12-31 | 269 | 229 | 405 |
| sceptic | anthropic_frontier_eci | 2028-12-31 | 210 | 194 | 234 |
| sceptic | anthropic_frontier_eci | 2030-12-31 | 242 | 212 | 292 |
| sceptic | anthropic_frontier_aeci | 2028-12-31 | 219 | 201 | 253 |
| sceptic | anthropic_frontier_aeci | 2030-12-31 | 255 | 220 | 322 |
| accelerationist | anthropic_frontier_eci | 2028-12-31 | 233 | 205 | 335 |
| accelerationist | anthropic_frontier_eci | 2030-12-31 | 294 | 236 | 485 |
| accelerationist | anthropic_frontier_aeci | 2028-12-31 | 246 | 212 | 361 |
| accelerationist | anthropic_frontier_aeci | 2030-12-31 | 316 | 246 | 539 |
| data_only | anthropic_frontier_eci | 2028-12-31 | 217 | 201 | 252 |
| data_only | anthropic_frontier_eci | 2030-12-31 | 256 | 229 | 346 |
| data_only | anthropic_frontier_aeci | 2028-12-31 | 227 | 208 | 269 |
| data_only | anthropic_frontier_aeci | 2030-12-31 | 272 | 237 | 375 |

The median at end-2030 moves by tens of points across weightings and the upper 80% bound by far more: the long-range answer is mostly the prior.

### Interval widths against the track record

| Date | Horizon (yr) | Ours, 80% below median | above | Research note 1, below | above | At least as wide |
|---|---|---|---|---|---|---|
| 2027-12-31 | 1.10 | -10 | +17 | -5 | +5 | True |
| 2028-12-31 | 2.10 | -18 | +48 | -8 | +14 | True |
| 2030-12-31 | 4.10 | -34 | +119 | -20 | +45 | True |

### Saturation

Date at which Anthropic's record line reaches 90% and 95% of each bounded benchmark's ceiling-rescaled range. After that the benchmark no longer separates models.

| Benchmark | Fitted frontier score now | Best observed | Crosses 90% (median, 10-90%) | Crosses 95% |
|---|---|---|---|---|
| SWE-bench Pro | 90.20 | 93.00 | 2026-12-12 (already to 2027-03-03) | 2027-04-03 (2027-01-15 to 2027-08-12) |
| Terminal-Bench 2.1 | 90.20 | 87.60 | 2026-12-07 (already to 2027-02-23) | 2027-04-22 (2027-01-30 to 2027-09-08) |
| OSWorld | 94.60 | 89.30 | already (already to 2026-11-22) | 2027-01-04 (already to 2027-04-28) |
| Remote Labor Index | 39.20 | 41.30 | 2027-09-21 (2027-05-21 to 2028-05-07) | 2027-12-09 (2027-07-08 to 2028-09-21) |
| ARC-AGI-2 | 99.40 | 95.00 | already (already to already) | already (already to already) |
| Humanity's Last Exam (no tools) | 74.30 | 73.20 | 2027-07-13 (2027-04-05 to 2028-01-10) | 2027-11-30 (2027-07-03 to 2028-09-08) |
| GPQA Diamond | 96.30 | 96.50 | already (already to already) | already (already to already) |
| FrontierMath Tiers 1-3 | 92.80 | 95.10 | already (already to already) | already (already to 2026-11-30) |
| Terminal-Bench 2.0 | 97.90 | 84.70 | already (already to already) | already (already to 2026-11-21) |
| AA Intelligence Index v5 | 67.70 | 64.60 | 2027-08-11 (2027-04-28 to 2028-02-20) | 2027-12-15 (2027-07-14 to 2028-09-24) |
| Vals Index v2.2 | 76.00 | 71.30 | 2027-09-08 (2027-04-27 to 2028-05-29) | 2028-03-21 (2027-08-19 to 2029-05-31) |

### Against external forecasts

| Source | Quantity | Theirs | Ours | Why they differ |
|---|---|---|---|---|
| FutureSearch (2026-11-14) | Rise in the highest public ECI held by OpenAI/Anthropic/GDM during 2029 | p10 11.7, p25 18.5, p50 27.3, p75 42.7, p90 74 | p10 8.6, p25 13.9, p50 20.6, p75 31.3, p90 54.9 | Same shape (right-skewed). Ours is built from a scenario mixture whose 'hold' pace decays with the central compute path. |
| Ho et al., Rosetta Stone naive extrapolation (2025-10; conversion approximate) | All-lab public ECI frontier, Oct 2028 | ~189 (182-196) | median 214.0 (80% 198.2-253.8) at 2028-09-30 | Rosetta extrapolates the 2023-25 slope; the frontier is already ~8 ECI above that line (research note 1). |
| Epoch AI trend (not a forecast), Nov 2026 | All-lab frontier slope | 16.6 ECI/yr (14.6-18.7); straight-line value at end-2030: 242 | median 257.5 at 2030-12-31 | Our median sits above Epoch's straight line because 25% of the weight is on accelerating scenarios; our 'reversion' scenario is close to Epoch's line. |
| METR-style horizon milestones (for AI Futures comparison) | Implied 50% time horizon of Anthropic's frontier reaches 1 work-week (40 h) | AI Futures: Automated Coder median mid-2028 (Kokotajlo) / mid-2030 (Lifland); Superhuman AI Researcher medians 2027 under a held 1.7-1.9x trend | median 2026-12-31 (10-90%: 2026-12-31 to 2026-12-31); P(by end-2030) 1.0 | Not the same quantity: ours is an extrapolated METR 50% horizon from the ECI link (4.75 ECI per doubling), far outside the measured range (max 17 h); theirs are capability milestones from a takeoff model. Read as an order-of-magnitude cross-check only. |
| METR-style horizon milestones (for AI Futures comparison) | Implied 50% time horizon of Anthropic's frontier reaches 1 work-month (167 h) | AI Futures: Automated Coder median mid-2028 (Kokotajlo) / mid-2030 (Lifland); Superhuman AI Researcher medians 2027 under a held 1.7-1.9x trend | median 2027-03-31 (10-90%: 2027-03-31 to 2027-09-30); P(by end-2030) 1.0 | Not the same quantity: ours is an extrapolated METR 50% horizon from the ECI link (4.75 ECI per doubling), far outside the measured range (max 17 h); theirs are capability milestones from a takeoff model. Read as an order-of-magnitude cross-check only. |
| METR-style horizon milestones (for AI Futures comparison) | Implied 50% time horizon of Anthropic's frontier reaches 1 work-year (2,000 h) | AI Futures: Automated Coder median mid-2028 (Kokotajlo) / mid-2030 (Lifland); Superhuman AI Researcher medians 2027 under a held 1.7-1.9x trend | median 2027-12-31 (10-90%: 2027-09-30 to 2028-09-30); P(by end-2030) 0.995 | Not the same quantity: ours is an extrapolated METR 50% horizon from the ECI link (4.75 ECI per doubling), far outside the measured range (max 17 h); theirs are capability milestones from a takeoff model. Read as an order-of-magnitude cross-check only. |

## 11. Assumptions that are not estimated

| Assumption | Value | Source |
|---|---|---|
| Residual distribution | Student-t, 4 df | robustness choice |
| Floor on trend residual scale | 0.75 ECI | Epoch posterior sd at the frontier is 1-2 points |
| Recency half-life for family offsets | 1.5 years | judgement; families re-rank over time |
| Stacking floor | 5% per candidate | hedge against overfitting ~45 overlapping folds |
| Mapping-form probability clip | 0.2 to 0.8 | 13 overlap points cannot exclude either form |
| ECI per 10x compute | 9 +/- 2 | research note 1 (worker's derivation from Rosetta) |
| Compute growth paths | low / central / high | `driver_scenarios_2026_2030.csv` |
| Algorithmic multiplier ranges per scenario | see scenario table | research note 3 bands |
| Realisation haircut on accelerating scenarios | 60-100% | AI 2027 ran at 58-75% of pace |
| Scenario weights | see table | section 10; prior |
| Family offset drift | 1.5 ECI per sqrt(year) | judgement from Sonnet's 2024-26 slide |
| Rival-frontier gap is stationary | mean-reverting to 2024-26 average | judgement; METR finds 1.4x if all labs are included |
| Fable = Mythos in ability | identical | Anthropic's statement that they are one model |

## 12. Limitations

- Small samples: 25 Claude models with a public ECI, 3 Fable releases, 4 Haiku releases, 13 models linking AECI to ECI, 7 AECI refit transitions.
- Both indices are re-estimated on every update. Predictions on the ECI scale are in today's units; AECI own-card predictions include an empirical drift model built on seven refits.
- AECI rests on first-party internal benchmarks that cannot be inspected; the mapping from public ECI may shift.
- A frontier is a running maximum of selected, best-configuration results; record-setters are noisy winners.
- Benchmark scores stop carrying information near their ceiling; the index scale itself is anchored on today's benchmark basket, so values far above ~200 have no direct empirical meaning.
- Scenario weights for 2027-2030 are a documented prior, not an estimate. The sensitivity table shows how much the answer moves.
- The model cannot see regime changes it has no data on (new architectures, export controls, a compute shock, a pause).
- Release dates come from the site's release forecaster; its errors pass straight through.
- Backtest folds at 3 and 6 months are few (see the tables) because families ship every ~3 months; the long-lead evidence is thin.
- All backtest folds fall in 2024-26, a period of rising pace. Every method under-predicted; the model may still be doing so.
- The trend candidates cannot be told apart on release folds; the combination weights are a hedge, not a finding.
- Links are fitted on ability point estimates (no errors-in-variables) and, for site charts, on Claude models only (10-17 points).
- OSWorld mixes three eval versions; HLE and SWE-bench Pro are first-party; ForecastBench set-ups differ by model.
- Family projections assume today's cadence and a slowly drifting offset; a tier could be repositioned or retired.
- The implied METR horizon is extrapolated two or more orders of magnitude beyond anything METR measured.

## 13. What would change the forecast

- The next two Anthropic record-setters: on the hold path they land near the 22-24 ECI/yr line; two in a row near 15-17/yr would shift weight to reversion.
- Epoch scoring more of Fable 5.2 (19 benchmarks so far; 90% interval 169.9 to 177.5): it anchors the current level.
- The next card's refit: another +5 step in printed AECI would confirm upward drift; a stable scale would tighten own-card intervals.
- A released model matching the internal model's 178.8 AECI, and its public ECI: a sixth point on the divergence above 157.
- Other labs' frontier: if it also bends upward, the 'no industry-wide break' evidence weakens.
- A new METR horizon for any post-Mythos-Preview model.
- Compute: delivered capacity against the S-1 commitments; export restrictions.
