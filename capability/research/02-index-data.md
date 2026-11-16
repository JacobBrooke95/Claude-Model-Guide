# Research note 2: composite-index and leaderboard data (downloaded 2026-11-16)

Worker report, saved by the orchestrator. All files in `capability/data/raw/` (raw pulls in `downloads/`). VERIFIED unless noted.

## Datasets

**Public ECI** — `eci_public.csv` (256 models, all labs, 2023-02 to 2026-11-09, 27 Claude), `eci_benchmarks.csv` (2,879 scores, 57 benchmarks), `eci_benchmark_difficulty.csv`, `epoch_hub_benchmarks_long.csv` (7,110 rows, 85 benchmarks).
- Model form: performance = sigmoid(alpha_b * (C_m - D_b)), Beta likelihood, anchors Claude 3.5 Sonnet = 130 and GPT-5 = 150.
- Epoch switched to a joint Bayesian fit on 2026-11-04. Intervals are now 90% credible intervals, not 95%. Frontier models moved about 1 point; models below 125 fell a lot.
- The whole scale is refit on every data update. 500 posterior draws per model are in `downloads/epoch/benchmark_data/epoch_capabilities_index/eci_bootstraps.json`.
- Public ECI scores Fable, not Mythos, and has no Mythos Preview.

**AECI** — `aeci_all.csv` (37 rows), `aeci_trend_statements.csv` (41), `aeci_internal_dates.csv` (15).
- `aeci_all.csv`: the 25 printed values with global CIs (local CIs for the Sept 18 and Nov 6 fits), the internal model, 7 figure reads, both anchors, and the repo's 2 rescaled estimates (flagged RELAYED).
- Each card refits the scale; frontier values rose 4.1-6.1 points between the Sept 1 and Sept 18 fits. Never mix fits.
- Internal dates: read off the x-axis of Figure 2.3.5.3.B ("Internal release date"), about +/-3 days. Lag to public release is 3-13 days for most models, 25 for Mythos 5.1 and 47 for Mythos 5.2; the internal model sits at about 2026-09-26.
- No card figure plots non-Anthropic models.

**Artificial Analysis** — `aa_index.csv` (287), `aa_index_versions.csv`, `aa_elo_gdpval_briefcase.csv` (330), `aa_model_releases.csv` (527 release dates).
- Intelligence Index v5.0.1 (November 2026, 9 evals). Only 113 configs carry a value.
- Claude coverage: Fable 5.2 (64.6 at max), Opus 5.5, Sonnet 5.5, Haiku 5.5, Fable 5.1, Opus 5, Haiku 4.5; every older Claude is N/A.
- Very effort-sensitive: Sonnet 5.5 runs from 25.6 to 54.5.

**LMArena** — `lmarena_text.csv` (57,984 rows, overall category, 257 snapshots 2023-05 to 2026-11-11), `lmarena_webdev.csv` (116 snapshots from 2025-11-12), `lmarena_agent.csv`, `lmarena_vision.csv`, plus `*_categories.csv.gz`.
- Official Hugging Face history, with CI bounds and vote counts per snapshot.
- Scale breaks: Bradley-Terry from 2024-01-09, style control from 2025-05-16, re-weighting from 2025-07-23.
- Model names switch from API ids to display names around 2026-10-15; joins need a name map.

**Vals** — `vals_index.csv` (2,672 rows): Vals Index v1, v1.1, v1.2, v2, v2.1, v2.2 (2026-05 to 2026-11-15) plus Finance, Legal, Science and Time Horizon indices, with stderr. Components change between versions.

**Claude per-benchmark** — `claude_benchmarks_long.csv` (2,557 rows, 160 benchmarks): 48 Epoch hub benchmarks with >=6 Claude models (GPQA Diamond 26, OTIS AIME 27, FrontierMath, ARC-AGI, WebDev Arena, ...), AA component evals, and 48 system-card capability metrics reported in >=6 cards (RELAYED from the repo index, number parsed from the raw value string).

**Releases** — `frontier_model_releases.csv` (460 models): Epoch, AA and repo dates side by side with a conflict flag (42 conflicts). Tiers from the repo CSV by fuzzy name match; check `repo_matched_model` before trusting a tier.

## Trend parameters

| Source | Statement |
|---|---|
| Opus 4.7 card | 13.6 AECI/yr through Opus 4.6 (n=8); Mythos Preview +5.8 above trend |
| Mythos Preview card | slope ratio 1.86x-4.3x depending on breakpoint |
| Opus 5.5 card (Sept 18 fit) | 14.75/yr (13.2-17.1); jump +5.9 at Mythos Preview; or 14.4->22.2/yr from Sept 2025, 1.53x (1.20-1.82); jump fit better in 99 of 100 refits |
| Fable 5.2 card (Nov 6 fit) | 15.3->28.7/yr from Oct 2025, 1.88x (1.62-2.28; 32 of 100 refits reach 2x); or 16.2/yr with a +8.8 jump; Mythos 5.2 about 11 above trend; slope fit better in 100 of 100; restates the Opus 5.5 ratio as about 1.6x |
| Epoch, Dec 2025 (superseded) | 8.3->15.5 ECI/yr, breakpoint April 2024 |
| Epoch, Sept 2026 | 14/yr (90% CI 12-17) for the reasoning-era frontier |
| Epoch, Nov 2026 Bayesian refit | 16.6/yr (14.6-18.7) reasoning era; 8.0 before |

Epoch also says about 5 ECI points per METR horizon doubling. Epoch publishes no ECI forecast.

## Surprises
- Public ECI shows a milder bend than AECI. Worker's least-squares fit on the Claude public frontier: 15.3/yr from Opus 3 to Opus 4.6 and about 22/yr after, against AECI's 28.7. The all-lab public frontier is about 17-18/yr since October 2025.
- AECI sits well above public ECI at the top: Opus 5.5 is 174.78 vs 168.54; Mythos 5.2 is 177.12 vs Fable 5.2 at 173.44. They agree at Opus 4.6 (157.3 vs 156.3). Ordering is consistent.
- The Mythos Preview card says internal use began 2026-02-24, but the Fable 5.2 figure plots it at about 2026-04-01.

## Not obtained
- AA index values for earlier versions (v1-v4). Epoch domain ECIs (SWE, Math). AECI benchmark counts for the Sonnet 5.5 and Haiku 5.5 fits. Stanford AI Index not checked. lmarena.ai returns 403; the Hugging Face dataset replaces it.

## Housekeeping
- `downloads/` is about 236 MB untracked, including a 64 MB LMArena parquet. Do not commit `downloads/`; add it to .gitignore and keep only the derived CSVs (compress very large ones).
