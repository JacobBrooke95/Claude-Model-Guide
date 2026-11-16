# Research note 3: time horizons and AI R&D acceleration (as of 2026-11-16)

Worker report, saved by the orchestrator. CSVs under `capability/data/raw/`: metr_horizons.csv, metr_trend_statements.csv, rnd_acceleration_statements.csv, takeoff_forecasts.csv. S-1 text extracts in `downloads/sec/`.

Headline: Anthropic's S-1/A No. 2 (Nov 10, 2026) says it has determined the RSP AI R&D threshold is MET, on the "expect" prong.

## Horizon dataset (metr_horizons.csv, 78 rows)
- Source: METR's machine-readable YAMLs, metr.org/assets/benchmark_results_1_0.yaml (TH1.0, 33 models) and _1_1.yaml (TH1.1, 26 models). Suite version per row.
- Extra rows: 8 flagged non-comparable rows (GPT-5.6 Sol, MirrorCode-Early, sensitivity variants) and 11 explicit "no METR horizon published" rows.
- Coverage stops in spring 2026: METR's page says "no longer actively updated"; last model added was Claude Mythos Preview (early), 2026-05-08.
- Claude on TH1.1 (50% horizon; 80% horizon): Opus 4.5 293 min; 49 min. Opus 4.6 719 min (95% CI 317-3,634); 70 min. Mythos Preview (early) 1,045 min = 17.4 h (509-3,304); 186 min.
- Mythos Preview sits above METR's 16-hour "unreliable" ceiling.
- No METR horizon exists for any Claude model after Mythos Preview, including Opus 5.5 and Fable/Mythos 5.2 (those METR evaluations were five qualitative AI R&D tasks).

## METR trend numbers (metr_trend_statements.csv, 41 rows)
- Full period: doubling about 7 months (TH1.0 201 d [176-225]; TH1.1 stitched 188-196 d).
- Since 2023: 129-131 d [104-161] on TH1.1, against 165-176 d on TH1.0.
- Since 2024: 89 d (TH1.1 post) and 105 d (Frontier Risk Report, R^2 0.98); worker's own fit on the YAML gives 103 d.
- 80% horizon: about one-fifth of the 50% horizon, with a similar slope.
- Caveats METR states: error bars about 2x each way; alternative fits move the 50% horizon by up to -35%; GPT-5.6 Sol reads 11 h, 71 h or >270 h depending on how cheating is treated.
- Shape: Epoch finds 3 of 4 metrics accelerating, WeirdML V2 flat. AI 2027 authors put 40-45% on superexponential growth. Worker's fit shows no superexponential bend within TH1.1, but the suite is saturated.
- Epoch: about 5 ECI points per METR horizon doubling.

## Acceleration evidence (rnd_acceleration_statements.csv, 70 rows)

| Who / when | Multiplier | Measured how |
|---|---|---|
| Mythos Preview card, Apr 2026 | slope ratio 1.86-4.3x; staff uplift ~4x; "progress multiplier below 2x" | AECI two-phase fit; survey |
| Fable 5 -> Fable 5.1 cards | "well short of" 2x; no further slope change | internal measures |
| Opus 5.5 card, Sep 22 | 1.53x [1.20-1.82]; one-time jump fits better in 99/100 refits | AECI |
| METR preliminary, Sep 22 | ~1.5x, 30% chance of 2x | high-access review |
| Haiku 5.5 card, Oct 7 | 1.7x (relayed by METR; not in the card text) | AECI |
| METR assessment, Nov 5 | 1.9x [1.5-2.8]; robustness range 1.1-2.9x; subjective ~2x (1.3-3x); ~80% AI-attributable; 1.4x if all labs included | piecewise OLS, break at 2025-10-07, includes internal Models 2-4 |
| Fable 5.2 card, Nov 9 | 1.88x [1.62-2.28]; 32/100 refits >=2x; jump better in 0/100; Opus 5.5 figure restated as ~1.6x | AECI, Nov 6 fit |
| AI Futures Project, Nov 10 | 1.7x AI-attributable; AECI 29 vs 15 points/yr | derived from METR |

## S-1 quotes (opened on EDGAR, CIK 2130357)
- S-1, Oct 26: "we may not identify a significant acceleration in our rate of development until after it has occurred."
- S-1/A No. 1, Nov 2: "our internal estimates and our expectations regarding future models, rather than our current models, indicate that we may imminently meet our Responsible Scaling Policy's definition of 'dramatically accelerated progress attributable to AI.' We have not designated any of our current models as exceeding this threshold".
- S-1/A No. 2, Nov 10: "Because the AI research and development capability threshold under our Responsible Scaling Policy applies where we 'observe or expect' a specified degree of accelerated progress, we made a determination that we have met this threshold based on what we expect from future models and our overall rate of progress, rather than on what we have observed from current models."
- Also in No. 2: code per engineer ">45 times" FY2024; ">90%" of code written by Claude; internal usage value up ">250 times" Jan-Sep 2026.

## Takeoff models (takeoff_forecasts.csv, 28 rows)

| Source | Implied rate |
|---|---|
| AI Futures Project, trend held at 1.9x | Superhuman AI Researcher (SAR) median Jul-Nov 2027 |
| AI Futures model filtered on 1.7x | SAR Feb 2027; 90% by end-2027 |
| AI Futures authors' own medians | SAR May-Aug 2027 |
| Halstead (AI Futures), progress in 2027 vs 2026 | >=1x 90%; >2x 60%; >4x 40%; >8x 20% |
| Cotra toy model | pace doubles again in 6 months, then 3 |
| Forethought, after full automation | >=3 years of progress in 1 year: 60%; >=10 years: 20% |
| METR simple model, Feb 2026 | 99% automation of AI R&D by late 2032 |

## Strongest evidence each way
- For acceleration: the jump-versus-slope test flipped from 99/100 to 0/100 once internal models were added; a public-ECI replication gets 1.42-1.64x for Anthropic alone; METR saw no bottleneck within 12 months and rules out training compute as the cause; the S-1 determination.
- For slowdown or artefact: the estimate falls to 1.1x under a cloglog link and 1.4x across all labs. Model 4 scores above 50% on every benchmark, so the index is saturating. Excluding the internal model and Mythos 5.2, the jump fits better in 63/100 refits. Most of METR's evidence is redacted. Mythos 5.2 quits 63% of open-ended research sessions. METR's developer RCT found +19% slower in 2025; the follow-up found -18% and -4%, not significant. The public all-lab ECI frontier shows no break in October 2025.

## Not obtained
- Davidson's compute-centric model; Epoch GATE headline numbers; a primary source for Kokotajlo's "spooked" remark; METR's GitHub repo; METR's redacted full report.

## Worker's recommended scenarios (k = multiplier on the pre-October-2025 AECI slope of ~15 points/yr; d = horizon doubling time on TH1.1)
The worker notes its probabilities lean on a bullish source (Halstead / AI Futures).

| Scenario | k | AECI points/yr | d (days) | Worker's probability |
|---|---|---|---|---|
| Reversion / one-time jump | 1.0-1.4 | 15-21 | 130-200 | ~15% |
| New trend holds | 1.6-2.3 (centre 1.9) | 24-34 | 90-130 | ~35% |
| Compounding | rising to 3-5 by end-2027 (pace doubling every 6-12 months) | 45-75 | <70 | ~30% |
| Explosive | >=8 during 2027-28 (cap at Forethought's "won't be 30X") | - | - | ~20% |

## Orchestrator's note on these weights
Do not adopt the worker's probabilities as given. Evidence pulling the other way: scenario-style forecasts have run hot (AI 2027 at ~60-75% of its predicted pace); the public all-lab ECI frontier shows no October 2025 break and the public Claude series bends to ~22/yr, not 28.7; the AECI estimate is sensitive to link function (1.1x under cloglog) and to including unreleased internal models; Anthropic has a commercial and regulatory context for its statements. Evidence pulling toward acceleration: forecasters have systematically under-predicted benchmark progress; compute is contractually committed through 2030; the lab itself now says the threshold is met. The model must make scenario weights an explicit, documented prior with a sensitivity analysis, and should let data-based evidence (how often past trend breaks persisted, the public-ECI replication) inform them.
