# Second-round review of cap-v2.0 (HEAD dea42e3), 2026-11-16

Independent verifier's findings, saved by the orchestrator. Verdict: publish with caveats, after small text/label fixes and prediction withdrawals. No blockers; no remodel needed. Both v1 blockers substantively fixed; pipeline reproduces from a clean copy (three runs, identical JSON apart from runtime_seconds). The main new problem is the bias term.

## MAJOR

**N1. The bias term adds about +5 ECI/yr to every scenario, and the scenario table does not show it.** `pipeline.py` L271-275, METHODS 10.

Realised 2027 level gain per scenario, from the 40,000 paths:

| Scenario | With bias | Without | Stated in table |
|---|---|---|---|
| slowdown | 17.8 | 12.8 | 12.7 |
| reversion | 21.0 | 15.9 | 15.9 |
| hold | 25.9 | 20.8 | 20.6 |
| mixture median | 24.7 | 19.5 | n/a |

- "Slowdown: below pre-break pace" therefore runs above the 15.0 pre-break slope in 2027, and "reversion" equals today's fitted pace (20.5). The "share below pre-break pace 0.85" excludes the term.
- The term contributes +5.65 to the end-2027 line level (198.5 vs 192.9), and +7.8 to 7.9 permanently through 2030.
- "Hold" plus bias is about 26/yr, which is the last 6-9 months' record slope (25-26), not the 12-month slope (21.0-21.5).
- Fix: report scenario paces including the term, or apply the term only to hold and faster scenarios; state the end-2027 contribution in `headline`.

**N2. "The out-of-sample correction helped (MAE 4.62 -> 1.95)" rests on 4 folds.** `backtest.score_machine`, METHODS 7.2.
- All four at h=0.5, consecutive origins Feb-May 2026, only 2 distinct outcomes (164.68, 168.54).
- No fold at 1.0 or 1.5 years has a rolling beta, yet the term is applied out to 1.5 years.
- The live beta (6.24 x 0.80 = 4.99) is the full-sample estimate. Leave-one-block-out gives 5.6-8.1.
- On the all-lab series the same correction made things worse (1.66 -> 6.63, 16 folds; per-block betas 8.4, 1.6, -1.5, 3.2). The term is regime-dependent.
- In release folds the term was live in only 4 of 14 folds with lead > 0 (errors +2.8, -3.6, -2.4, -0.9). The no-bias variant has MAE 2.00 vs 2.22 at 3 months.

**N3. "Validated through 2027-12-31" is too strong.** `pipeline.py` L673-674. From "longest horizon with >=10 folds" (1.0 yr) plus a 0.13-yr fudge. Those 10 folds have 7 distinct targets; all under-predicted (bias 6.30, 50% coverage 0.30). The published, bias-corrected configuration has never been scored at that horizon. Fix: rename to `backtested_through` with a caveat.

**N4. GDPval-AA still over-extrapolates.** 80% lower bounds for Opus (1917), Sonnet (1921), Haiku (1877) exceed the best score ever (1866). Fable's lower bound (1863) exceeds Fable 5.2's 1831. Haiku 95% upper bound 4778. The six highest-ECI models sit on average 251 Elo below the linear link (link RMSE 196). Backtest over-predicted in 10 of 12 folds, bias -59. Fix: withdraw, or fit a concave link.

**N5. All-lab frontier is the Anthropic frontier in 76% of paths at end-2027.** All-lab line alone gives 190.6; published 198.7. It inherits the Anthropic bias term although the all-lab backtest rejected one. Must be stated.

## MINOR
- Terminal-Bench 2.1, Fable/Mythos: anchored on Fable 5.1 (85.0); Fable 5.2 and Haiku 5.5 have no 2.1 score, and 4.0 has appeared. 80% lower bound (88.0) above best ever (87.6). Will probably expire unresolved; it sits in `headline`. Drop it.
- Admission rule text disagrees with the code: Vals has 0 folds; Terminal-Bench 2.1 and RLI have 2; AA Index 3; SWE-bench Pro 4 (80% coverage 0.50). Four published benchmarks have a best score above 90% of ceiling (SWE-bench Pro 93/100, OSWorld 89.3/89.5, ARC-AGI-2 95.0/95.2, FrontierMath 95.09/95.09). Opus 5.5 at 89.9 gets a numeric SWE-bench Pro forecast (94.3) while Fable at 93.0 is "saturated". The 0.6 coverage threshold admits OSWorld (0.60, bias -5.0), WebDev (0.67), LMArena (0.67).
- Estimated ceilings hug the record (ARC-AGI-2 95.2 vs best 95.0; OSWorld 89.5 vs 89.3; FrontierMath's estimate is the best observed). 95% upper bounds are hard-capped there.
- Arena scores: WebDev and LMArena ratings are each model's last snapshot, so scales are mixed; not in the open list; cannot be resolved. Label "indicative, not graded" or remove.
- Layers agree within about 1 ECI, not within Monte Carlo noise (2027-03-31 frontier median 178.91 vs first-next releases implying >=179.72). The shared-process test only checks "inside the 95% band".
- Vintage check has mild target leakage at lead 0 (origin vintage includes the target in all 22 cases). Strict-origin lead-0 vintage RMSE is 2.85, not 2.72.
- Grading matches chart rows by exact date; a row one day off never resolved. Match on model name.
- Measured-scale threshold 207.6 is lenient (depends on a 0.04 slope cut-off; at 197.5 only 4 of 50 benchmarks are below 90% solved).
- Calibration still near a no-op; frontier factors were fitted on the rolling-beta configuration, not the published one.
- All-lab slope draws clipped: 19.8%.

## NIT
- Own-card AECI arithmetic checks (gap +3.91, RMSE 4.32); interval widths consistent. The simpler "last gap" rule scores better (3.93); chosen rule's mean error +2.9.
- Claude 3.5 Haiku enters the vintages 13 days early (2024-10-22 vs canonical 2024-11-04).
- The positive-step model does not shift medians, except Opus by +0.45.

## v1 findings: B1 fixed; B2 partly (GDPval, Fable TB2.1); M1 fixed; M2 partly (N1, N5); M3 fixed; M4 partly as claimed; M5 fixed (simulation passed); M6 fixed (3.0/1.9/0.4/4.7%); M7 fixed, root-cause claim true; M8 partly as claimed; minors fixed, tests weak.

## Recomputed vs reported (all matched)
Model RMSE/MAE date-given 0/3/6 mo: 2.47/2.12, 2.70/2.22, 3.78/3.30. Date-unknown 3/6 mo: 2.67, 5.71. Baseline: 2.52, 2.20 (2.61), 3.63 (5.25). 80% coverage 0.86/0.90/1.00. Mean 80% interval width 10.1/14.1/21.8.

## Headline sanity (reviewer's back-of-envelope vs v2)
Opus 5.6: 173.3 vs 174.2. Sonnet 5.6: ~173.0 vs 173.8. Fable/Mythos 5.3: 177.5-178.4 vs 179.2. Haiku 6: 174.6-176.1 vs 177.4. Frontier end-2027: 192-195 vs 197.5 — all of the gap is the bias term. Historical within-family steps at matched gaps: median 4.4, mean 5.0 (n=13); v2 median steps 5.7-5.8.

## Caveat sentences the reviewer wants in headline.notes
1. The next-model point forecasts are, in effect, predecessor + recent Anthropic record slope x elapsed time; in backtest (RMSE about 2.5 at release, n=21) they are no better than that two-line rule.
2. Frontier figures include an under-prediction correction (state value); its out-of-sample check is four overlapping six-month folds.
3. Scenario paces: state them including the correction.
4. "Backtested through 2027" means the uncorrected code was run at one-year horizons on 10 overlapping origins in one regime and under-predicted every time (mean 6.3); the corrected forecast is untested beyond six months.
5. The all-lab frontier equals the Anthropic frontier in about three-quarters of paths.
6. Benchmark forecasts are thinly tested (0-16 folds); arena and index rows are indicative and not graded.
7. Haiku 6 lies beyond any tested lead.
