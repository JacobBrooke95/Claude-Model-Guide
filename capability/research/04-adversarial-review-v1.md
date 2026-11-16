# Adversarial review of cap-v1.0 (2026-11-16)

Independent reviewer's findings, saved by the orchestrator. The reviewer's check scripts are in `capability/research/review-scripts/`. Two blockers, eight majors. "Mine" = reviewer's recomputation.

## BLOCKER

**B1. Headline backtest omits the model's worst fold and uses strawman baselines.** `backtest.py: release_summary(common_only=True)`, METHODS 7.1.
- The dropped fold is Fable 5 (first of a family; errors +5.9, +6.5, +7.9).
- On all folds the model's RMSE is 2.64 / 2.85 / 4.70 at 0 / 3 / 6 months, against 2.35 / 1.98 / 2.93 reported.
- Baseline CRPS and coverage are computed on 15 folds but labelled n=19.
- A two-line baseline (previous-in-family + trailing-12-month Anthropic record slope x elapsed time; new family placed on the line) scores 2.57 / 2.29 / 3.63 on all folds.
- So "beats every baseline at every lead" is false at 3 and 6 months.
- Fix: report all folds, add this baseline, and give paired differences with intervals.

**B2. Open benchmark predictions contradict observed scores.** `links.py` (ceilings fixed in `build_data.META`), `next_models.*.benchmarks`.

| Benchmark | Prediction (80% unless stated) | Observed |
|---|---|---|
| ARC-AGI-2 | Opus 99.2 (95.9-99.9); Fable 99.7 (97.9-99.97) | four strongest models (ECI 168.5-173.4) score 93.3-95.0; Fable 5.2 = 93.8 |
| OSWorld | Fable lower bound 90.8; curve gives 94.6 at the frontier | best ever 89.3 |
| GDPval-AA | Fable lower bound 1920 | best ever 1866; Fable 5.2 = 1831 |
| FrontierMath | Fable upper 95% bound 94.9 | Fable 5.2 = 95.09 (ceiling set at 95) |
| Terminal-Bench 2.0 | 97.6 | data end April 2026, max 84.7 |
| GPQA | 96.28 (95.6-96.7) | ceiling 97; a ceiling artefact |

Fix: estimate ceilings, or predict previous-in-family plus a link delta; drop saturated and stale benchmarks.

## MAJOR

**M1. Stacking weights are arbitrary and now push the wrong way.**
- Every stack is a corner solution: one candidate at 0.70, the rest at the 5% floor.
- The winner flips: hinge at h=0.25 and in rolling weights until mid-2026, `pool_all` afterwards.
- 45 folds from 19 origins and 11 distinct targets; in a block bootstrap `pool_all` ranges 0.28-0.70.
- `pool_all` won because it predicted higher than `lin_12` in 81% of folds (+1.7). Live it is lower: -4.9 at mid-2027, -7.0 at end-2027.
- 54% of live weight sits on `lin_all`, `jump` and `pool_all`, although every form under-predicted.
- The two layers disagree: the next-model record line is 181.7 at 2027-07-13, while the projection implies about 185 (frontier median 183.7 at 2027-06-30). Haiku 6 (173.1) is probably about 3 low.
- Fix: one shared level process, equal weights over recent-trend forms, and an explicit bias term.

**M2. The 2027-30 band is an untested prior.**
- `project.simulate` is never backtested; the frontier backtest scores a different model.
- `sigma_w` = 4.34 is the sd of one-year errors and drops the +5.6 bias (RMSE 5.93).
- Frontier calibration factors (1.13-1.37 at 50%; rolling 50% coverage 0.24) are computed but not applied.
- "Data-only" P(revert) = 0.355 is the unweighted mean of 0.20 (two episodes, Laplace), 0.009 and 0.856.
- "Reversion" means 1.0-1.4x the pre-break slope (about 17.9/yr, above Epoch's 16.6). No scenario runs below pre-break pace in 2027.
- The all-lab frontier is Anthropic plus a gap, so it inherits a break the all-lab data reject (hinge ratio 0.72).
- Tails: 80% upper 373, 95% upper 513.5, explosive median 480, on a scale METHODS says is undefined above ~200.
- Research note 1's central path is +65 by 2030 (about 238); the model's median is 254.

**M3. Implied METR horizon is false precision.** "101 h" today (95% low 68 h) against a last measurement of 17.4 h; the link has no point above ECI 157.9. It reports P(1 work-month by 2030) = 1.0 and P(1 work-year) = 0.995.

**M4. AECI layer.**
- Three of seven drift transitions, including one of the two +5 steps, rest on Opus 5.5 alone, read from cards with no stated fit.
- Over those three refits the other four models moved +3.8 to +4.5, not the +5.4 Opus 5.5 moved.
- Steps are resampled as iid with mean +1.38 (SE 1.05), so Haiku 6's own-card value gets +9.9 over 8 refits (171.8-210.3).
- Leave-one-out misses both jumps; there is no AECI backtest.
- The mapping gap tracks recency, not level: Haiku 5.5 (ECI 160.4) printed 167.11 (+6.7) and Sonnet 5.5 is about +7.0, against +3 to +5 mapped. Sonnet and Haiku AECI are biased 2-4 low.
- The level-shift threshold is unidentified between 156.3 and 164.1.
- The Sonnet 5 card printed no AECI, so Sonnet/Haiku own-card predictions may never resolve.

**M5. Twins and grading.**
- Fable and Mythos get different dates (Feb 2 vs Jan 26), ECI (176.29 vs 175.94) and RLI (49.1 vs 47.6).
- Nine Mythos benchmark predictions resolve against `series["mythos"]`, which stopped in June 2026; 5.1 and 5.2 are charted under Fable only.
- ForecastBench ends June 2026 and has no Fable series; Haiku has no RLI series.
- No expiry rule, so the scorecard will be survivorship-selected.
- `grade.py` reads the current ECI, not the "first published value" its rule states.

**M6. Regression odds contradict the record.** P(next < predecessor) is 12.5% for Opus, 25% for Fable and 28% for Mythos, against 0 of 21 historical within-family steps (minimum +0.86).

**M7. Section 7.4 is not reproducible.** It depends on the git-ignored `cache/irt_vintages.pkl`.
- A clean run gives 18 folds (12/4/2), not 33.
- Vintage RMSE becomes 3.36 / 4.48 / 6.73, not 2.88 / 3.37 / 5.30.
- `--check` passes either way because the hash ignores the cache.

**M8. Live leads are untested.** Live forecasts are date-unknown at 1-8 months.
- That variant has n=8 (RMSE 2.62) and n=3 (RMSE 5.90, bias +5.7).
- All four 6-month folds under-predict (+4.15); Haiku 6 lies beyond any fold.
- Calibration factors are all floored at 1, so calibration is a no-op.
- Fable and Haiku 80% coverage is 0.67 (n=3 each).

## MINOR / NIT
- No release-date leak in any audited fold. But 9 of 20 day-of folds use an Anthropic model under 30 days old at its settled ECI; a one-month lead costs little (RMSE 2.66 vs 2.58).
- Full-sample choices: the blend rule, type-effect switch, degrees of freedom, floors and half-life. Variants span RMSE 2.36-2.83, so the effect is small.
- The matcher merges LMArena and AA "Claude 3.5 Sonnet (20241022 / Oct '24)" into the June model; likewise Mistral Large 2402/2411 and DeepSeek-R1 (0528). None is logged.
- The frontier floor is degenerate: 95% low equals the median (173.44) at end-2026, though Fable 5.2 rests on 19 benchmarks.
- m = 2.01 is compared with METR's 1.7-1.9x total-slope figure; the model's own total ratio is 1.57.
- The "bootstrap" is a subsample (`np.unique`); slope draws are truncated.
- The leak tests assert a cutoff the code writes itself; the mapping test is tautological.
- Monte Carlo noise is about +/-0.07 RMSE (2.35 vs `rule_blend` 2.42), the same size as the differences between candidates.

## Recomputed vs reported

| Quantity | Reviewer | Author |
|---|---|---|
| Model RMSE at 0 / 3 / 6 months, author's fold subset | 2.35 / 1.98 / 2.93 | same (confirmed) |
| Model RMSE, all folds | 2.64 / 2.85 / 4.70 | only in 7.4 |
| Previous-in-family RMSE | 8.52 / 11.82 / 17.63 | same (confirmed) |
| Fair simple baseline, all folds | 2.57 / 2.29 / 3.63 | absent |
| Model 80% coverage at lead 0, all folds | 0.85 | 0.89 |
| Mapping: hinge knee and slope; shift; RMSE | 150.0, +0.251; +4.607; 1.07 / 0.78 | same |
| Drift steps; mean / sd | 0.61, 0.01, -1.61, 5.21, -0.24, 5.44, 0.22; 1.38 / 2.78 | same |
| "Hold" path to end-2030, by hand | about 257 (pace 22.4, 21.6, 20.4, 19.7) | 257.8 |
| "Reversion" path, by hand | about 240 | 240.2 |
| Opus / Sonnet / Haiku / Fable ECI, by hand | 172.3 / 171.9 / 174.2 / 176.3 | 172.7 / 171.8 / 173.1 / 176.3 |
| Opus AECI Nov 6 scale / own card | 177.7 / 179.9 | 178.2 / 180.2 |
| 17 link fits (slope, difficulty, RMSE) | identical | - |
| Scenario weights | all sum to 1.000 | - |

## How much to trust it (reviewer)
- Opus, Sonnet, Fable ECI (1-3 months): widths adequate, if anything wide. Medians probably 1-3 low. Honest evidence is RMSE of about 2.6-2.9 on 20 + 9 folds, no better than a two-line baseline.
- Haiku 6: not validated.
- AECI own-card: judgement with a +/-6-10 band, not a tested forecast.
- Benchmarks: SWE-bench Pro, HLE, Terminal-Bench 2.1, RLI and the AA and Vals indices are usable. ARC-AGI-2, OSWorld, GDPval, FrontierMath, Terminal-Bench 2.0, GPQA, Vending-Bench, ForecastBench and METR should not be published as they stand.
- 2030: the median to end-2027 (about 195 +/- 10) is defensible. Beyond that it is a scenario prior. An Epoch or METR reader would attack first the Anthropic-only break imposed on all labs, then ECI above 200 and the hour figures.

## Reviewer's top five changes
1. Rebuild 7.1 on all folds with the previous-plus-slope baseline, and withdraw "beats every baseline".
2. Fix or drop the contradicted benchmark predictions: estimate ceilings, anchor on previous-in-family, and add a test that no interval excludes the current model's score in the wrong direction.
3. Replace stacking with one level process shared by both layers, carry the under-prediction bias explicitly, and backtest the projection machinery at 0.5-1.5 years.
4. Force Fable = Mythos, prune unresolvable predictions, add expiry and first-published rules to grade.py, and commit or hash the IRT cache.
5. Publish 2028-30 as labelled scenarios, capped where ECI stops being defined; drop the hours series; state that the weights and AECI drift are judgement.
