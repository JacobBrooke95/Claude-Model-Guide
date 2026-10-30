# Claude release forecaster

A statistical model of when Anthropic will ship its next Claude model in each family (Opus, Sonnet, Haiku, Fable, Mythos). It gives full probability distributions over release dates, release parameters (name, price, co-launch, benchmark), a categorized registry of every input, and a rolling-origin backtest against base rates and the site's earlier EWMA model.

The results page is [`release-forecast.html`](../release-forecast.html). The old cadence view on [`claude-models.html`](../claude-models.html) stays as it was and links here.

```
python3 live.py 2026-10-30        # live forecast → output/forecast.json, appends forecast_log.csv
python3 run_tuning.py             # stage 1: 27 configs on tuning origins (2024-06 → 2025-06)
python3 run_tuning_v2.py          # stage 1b: recency weighting × trend × wave weight
python3 run_all.py --part=lock    # lockbox origins 2025-07 → 2026-10 (also --part=tune, --part=events)
python3 run_final.py --part=lock   # post-review backtest (also --part=tune, --part=events)
python3 score_final.py            # → output/backtest.json (score_lockbox.py is the pre-review scorer)
python3 tools/build_signals.py    # data/raw/signals_research.csv → data/signals.csv
python3 tools/build_page.py       # → ../release-forecast.html
```

Requires Python 3.10+ with numpy, scipy and pandas. Node is needed for the EWMA baseline, which runs the existing `scripts/predict-releases.js`.

## The model, layer by layer

| Layer | What it does | Fitted from |
|---|---|---|
| **Cadence** (`engine/cadence.py`) | Hierarchical Bayesian renewal model. Log-gaps are Weibull with a family level `mu_f` partially pooled across families, a change-point trend (gaps before mid-2025 were longer), recency weighting (half-life 0.75 years, a power prior), and a right-censored open interval. Fit by adaptive Metropolis at every forecast origin. | Release dates before the origin |
| **Wave** (`engine/wave.py`) | Company-level renewal on distinct release days, plus a conditional logistic model of which families ride each wave. Captures co-launches. Tested in the backtest and given **zero weight** in the final model: it lost on both tuning and lockbox. | Same |
| **Calendar** (`engine/modifiers.py`) | Proportional-hazard multipliers. A Dirichlet-smoothed weekday profile (fitted), a Dec 20 – Jan 4 freeze and Thanksgiving Thu–Fri (factor 0.25, a priori). | Releases before the origin |
| **Competitors** (`engine/modifiers.py`) | A competitor-release hazard multiplier `exp(γ·x_t)`, pre-registered with two definitions. **Tested and excluded.** It made scores worse, and γ is slightly negative. | `data/competitor_releases.csv` |
| **Signals** (`engine/signals.py`) | Bayesian update on the date distribution from pre-release sightings in four classes (infrastructure, client strings, reports, soft). For each class: detection rate, log-normal lead-time density and false-alarm rate, all estimated from signals already resolved at the origin. The false-alarm rate has a floor of 0.01 per family-day, and grade A/B sightings take precedence. Tempered by ρ = 0.5 and capped at 5× per class. The absence-of-evidence term is **switched off** in the final model, because it hurt in both periods. | `data/signals.csv` (98 true and 9 false sightings, 2023–2026) |
| **EWMA pool** (`engine/ewma.py`) | Linear pool, 70% this model and 30% the repo's EWMA model, for Opus, Sonnet and Haiku. The EWMA window is read as an 80% interval. | — |
| **Markets** (`engine/market.py`) | Polymarket ladders, cleaned with an isotonic fit, shown beside the model. A 50/50 log-odds blend is displayed but is not the model, because markets and signals share sources. | `data/raw/markets_2026-10-30.csv` |
| **Parameters** (`engine/params.py`) | Generation clock (P(Claude 6 by date)), next-name distribution, price change, co-launch rate, SWE-bench Pro projection. | Release table, repo benchmark data |

## How the configuration was chosen

The history is kept because it changes how the scores should be read.

1. **Stage 1** compared 27 configs (3 error families × 3 trend forms × 3 wave weights) on **tuning origins only** (weekly, 2024-06-03 → 2025-06-30). The winner was v1: Weibull, linear trend, half wave.
2. v1 was scored **once** on the untouched **lockbox** (weekly, 2025-07-07 → 2026-10-26). It beat climatology but lost to the old EWMA model at 30 and 90 days on Opus, Sonnet and Haiku. It was too slow to adapt when Opus moved to a 6–8 week cadence. **This is the only clean out-of-sample result.**
3. **Stage 1b** added recency weighting. The choice was again made on tuning origins only, giving v2: Weibull, change-point, no wave, half-life 0.75 years. But v2 was designed *after* seeing the lockbox, so its lockbox score is post-hoc.
4. **v3 / final**: v2 plus signals (no absence term), linear-pooled 70/30 with the EWMA. Both choices were made looking at full-period results. Over the full backtest, the pool beats both of its parts, which is the standard forecast-combination result (Clemen 1989; Claeskens et al. 2016).
5. **Adversarial review** (an independent agent, 12 findings; `data/raw/adversarial_review.md`). Fixes: the EWMA baseline was leaking same-day releases, now called as of origin − 1. A false-alarm floor and A/B precedence in signals. Four MCMC chains averaged. A 180-day recent-rate baseline. Per-family scoring, block-level significance tests, calibration by period, and claims rewritten. Re-run as `run_final.py` → `score_final.py`. Model version `v3c-post-review`.
6. The probability of backtest overfitting (CSCV, Bailey et al.) across the 27 stage-1 configs is **0.83**. Picking among near-identical configs is mostly noise. Across the 20 configs scored on every origin it is **0.20**. The gains that hold up are structural, and none of them depend on that choice: cadence over climatology, signals over none, and pooling over either part alone.

**The only fully honest test from here is prospective.** Every `live.py` run appends its calls to `forecast_log.csv`, and those rows are never edited.

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
- **The live Fable call** rests on sightings now 15–17 days past the rumored week. With a thin two-release cadence, the model reads them as stale (38% by Nov 30). The market reads them as delay-but-coming (89%). The blend (69%) is the better single number.
- **Hard-coded structure.** The change-point date (2025-06-01) and the holiday freeze were chosen knowing the full record.
- **Not modelled:** the IPO calendar (no base rate exists), the S-1's safety-gating disclosures (qualitative), compute coming online.
