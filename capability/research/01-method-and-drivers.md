# Research note 1: forecasting method and input drivers (as of 2026-11-16)

Worker report, saved by the orchestrator. Rows in the CSVs are flagged VERIFIED (opened), RELAYED (search summary only) or DERIVED (worker's computation). Data files: `capability/data/raw/` — drivers_compute.csv, drivers_algorithmic.csv, driver_scenarios_2026_2030.csv, external_forecasts.csv, forecast_track_record.csv, method_evidence.csv, family_tier_lag.csv, trend_backtest_eci_frontier.csv, downloads/ (raw pages and PDFs, incl. anthropic_s1a2_20261110.htm and system-card PDFs).

## (a) Modelling recommendation

Structure: forecast latent ability, then map it to scores. Both ECI docs and Pimpale et al.'s backtest (date -> latent -> sigmoid beat five alternatives) support this.

1. Ability trend: piecewise-linear with a changepoint prior and Student-t errors.
   - Public ECI frontier: 16.6 ECI/yr in the reasoning era (90% 14.6-18.7) versus 8.0 before (Epoch Bayesian report, Nov 2026).
   - AECI: slope change 1.88x at Oct 2025 (95% CI 1.62-2.28; Fable 5.2 card).
2. Family offsets, partially pooled (derived from public ECI, n = 3-8 per tier):
   - Sonnet: median 0.5 ECI below Anthropic's best (range 0-7.2); 1.7 months behind the global frontier.
   - Haiku: median 8.1 ECI below; 4.8 months behind Anthropic's frontier.
   - Epoch's open-vs-closed lag (4 months = 8 ECI) gives about 2 ECI per month.
3. Benchmark link: score = sigmoid(alpha_b * (C - D_b)) on chance/ceiling-rescaled scores, with Beta noise.
   - Even with ability known, held-out score error is RMSE 0.092, MAE 0.067; 90% coverage is 89.6%.
   - Going from 50% to 90% takes 2.2/alpha_b ECI points (27 at slope 0.08, 10 at 0.21).
4. Scenario mixture: no change, one-time jump, slope change, compute-limited slowdown.
   - Anthropic's jump-vs-slope verdict flipped from 99/100 refits to 0/100 between consecutive cards.
   - Epoch's break detector has a 38% false-positive rate.

Uncertainty sources to include:
- Slope estimation: error grows as sqrt(tau + tau^2/m) with t(m-1) tails (Farmer & Lafond).
- Scale drift: the same model (Mythos Preview) moved 158.3 -> 165.71 across AECI refits. Epoch's Bayesian switch moved frontier models about 1 point but models below 125 by 13.7. Forecast within-fit increments: AECI local CI is about +/-1.4 versus +/-5 global.
- Selection: the AECI frontier is a running maximum of best configurations and "most capable" snapshots.
- Benchmark supply: new-benchmark difficulty is overestimated.

Calibration from track records:
- Direction: under-prediction dominates. XPT superforecasters put 9.7% on realised benchmark outcomes; domain experts 24.6%. AI Digest 2025 one-year medians: Cybench +20 pp, OSWorld +12.6, FrontierMath +0.7, SWE-bench -7.1; revenue under-predicted 1.9x.
- Exception: scenario-style forecasts ran hot. AI 2027 is at 58-66% of its pace, later revised to about 75%.
- Worker's rolling-origin ECI backtest (single current fit, n <= 8):

| Fit window | Horizon | Median error (actual - predicted) | MAE |
|---|---|---|---|
| All history | 1 yr | +8.5 (under-predicted 6/6) | 8.2 |
| All history | 2 yr | +23 (n = 2) | 23.2 |
| Trailing 12 months | 1 yr | -1.8 (p10-p90: -3.6 to +3.9) | 3.1 |
| Trailing 12 months | 1.5 yr | -2.8 | 4.8 |

- Suggested 80% intervals for the ECI frontier (worker's judgement, widened for small n and drift): +/-5 at 1 year, -8/+14 at 2 years, -20/+45 at 4 years, right-skewed.
- Single benchmark scores at 1 year: roughly -10/+25 pp mid-sigmoid.

## (b) Drivers

| Driver | Low | Central | High | Basis |
|---|---|---|---|---|
| Training compute, x/yr 2027->2030 | 2.5, 2, 1.5, 1.5 | 5, 4, 3, 2.5 | 5 flat | Epoch 5x/yr (4-6); chip compute sold 2.5x/yr |
| Algorithmic efficiency, x/yr | 2 | 3 | 6 | Ho 2024 (8-month halving, CI 5-14); Gundlach 3x; Whitfill 3.5x; Rosetta 6x (1-50) |
| Frontier ECI, points/yr | 10 -> 7 | 17 -> 15 | 22 -> 45 | scenario rows in driver_scenarios_2026_2030.csv |

- Decomposition (Rosetta): total 0.55 units/yr, of which 0.3 (0.1-0.5) is algorithms at fixed compute. Worker derives roughly 9 ECI per 10x compute; approximate.
- Anthropic (S-1/A, 10 Nov 2026): committed spend $900.9B, $451.6B before end-2030, $70.7B due within 12 months. Fixed purchase commitments by year: 2027 $28.4B, 2028 $43.5B, 2029 $46.9B, 2030 $44.2B. Minimums: Google $121.3B plus $125-150B of additional TPUs delivered 2028-31; Amazon $110B; Microsoft $47.2-49.2B; SpaceXAI up to $120.5B. Compute expense: $7.3B in FY25; $18.8B in first nine months of 2026. Run-rate revenue: ~$9B (Dec 2025) -> >$30B (Apr 2026) -> ~$81B (31 Oct 2026).
- Constraints: lead times add about 1 year per 10x compute; 5x/yr sustainable "another 1-2 years" (Epoch). A gigawatt site takes 2.1 years and costs $38B per GW. Largest training run reaches 4-16 GW by 2030; 2e29 FLOP feasible. New chip export restrictions under consideration (10-11 Nov).

## (c) External comparators
- FutureSearch, ECI rise during 2029: p10 11.7, p50 27.3, p90 74.
- Rosetta naive forecast: about 189 ECI by Oct 2028 (worker's conversion), already running about 8 ECI behind reality.
- Anthropic's unreleased internal model: AECI 178.78, versus Mythos 5.2 at 177.12.
- AI Futures Automated Coder medians: mid-2028 (Kokotajlo), mid-2030 (Lifland).
- OpenAI capacity: "low double-digit GW" in 2027.
- Whitfill et al.: a compute slowdown delays the 1-month horizon by 7 years.

## (d) Not obtained
- Metaculus (403; secondary medians conflict, RELAYED). Manifold / Polymarket not searched. Lab-leader timelines: secondary trackers only. Anthropic gigawatt totals: S-1 has no GW figures. AI Impacts survey vs outcomes: no retrospective found. Steinhardt 2021 contest figures: relayed. AI Futures Q2.5 forecast table: image, not extracted. No published flagship-vs-tier lag analysis found; tier numbers are the worker's derivation. Vintage ECI fits unavailable, so the worker's backtest excludes scale drift. GATE: only the default 2027 output read.
