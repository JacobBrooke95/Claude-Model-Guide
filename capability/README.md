# Capability model

**Current version: cap-v2.2** (default forecast identical to cap-v2.1; v2.2 adds the `with_model_4` what-if variant). cap-v1.0 was withdrawn after an independent review (`research/04-adversarial-review-v1.md`); its output is archived unedited in `history/capability_forecast_v1.0_withdrawn.json` and METHODS.md section 14 lists what changed.

Forecasts the capability of Anthropic's next models and of the frontier through 2030: public ECI, AECI, and the benchmarks the
site charts. Methods, tables and limitations are in [METHODS.md](METHODS.md); the research it rests on is in `research/`.

## Run

```
python3 capability/run.py            # data layer -> backtests -> fit -> predictions -> projection -> outputs (1-2 min)
python3 capability/run.py --full     # rebuild data/irt_vintages.csv.gz (leave-future-out IRT refits; committed, covered by the input hash)
python3 capability/run.py --check    # verify outputs are current (input hash), strict JSON, ordered intervals
python3 -m unittest discover -s capability/tests -v
python3 capability/grade.py          # resolve open predictions whose release has shipped -> scorecard.csv
```

Needs Python 3.13 with numpy, scipy, pandas and Pillow. One fixed seed (`capmodel/common.py`); the same inputs give the same outputs.

## The 'with Model 4' variant

Anthropic's unreleased internal research model (METR's "Model 4") is **not** in the default forecast. `output/capability_forecast.json`
carries a what-if alongside it at `variants.with_model_4` (same shapes as the default's `headline`, `next_models`, `projection.series`,
plus `delta_vs_default`, `components` and `p_sensitivity`). To flip a page or analysis to it, read those paths instead of the top-level
ones; nothing needs re-running. To change its assumptions, edit the constants at the top of `capmodel/variant.py` (`P_RELEASE`,
`REMAINING_LAG_MEAN_DAYS`, `MAX_TREND_SHIFT`) and re-run. The variant is never graded and issues no predictions. METHODS.md section 15.

## Layout

| Path | What |
|---|---|
| `build_data.py` | canonical tables in `data/` from `data/raw/*.csv`, `../data/models.json`, `../data/benchmarks.json`; `data/build_log.csv` lists every rename, conflict and dropped row |
| `capmodel/trend.py` | trend forms fitted to record-setters, subsample bootstrap, CRPS |
| `capmodel/level.py` | the one level process: recent-trend fit, scenario paths, bias term; used by both the next-model layer and the projection |
| `capmodel/families.py` | positive-step gain model for the next release; pooled family offsets (post-2027 family paths) |
| `capmodel/aeci.py` | own-card AECI model, secondary Nov-6 mapping, refit table |
| `capmodel/links.py` | benchmark links with estimated ceilings; anchored predictions |
| `capmodel/irt.py` | own IRT refit for leave-future-out vintages |
| `capmodel/backtest.py` | backtest of the level process itself; release folds on all folds with baselines and paired differences; calibration |
| `capmodel/variant.py` | the 'with Model 4' what-if: importance re-weighting of the default's paths |
| `capmodel/predict.py` | release-date sampler over `../forecast/output/forecast.json` |
| `capmodel/pipeline.py`, `report.py`, `plots.py` | orchestration, JSON and METHODS.md, PNG diagnostics |
| `output/capability_forecast.json` | everything a page needs (see its `metadata`) |
| `output/*.png` | diagnostic plots |
| `history/predictions_<date>_<version>.json` | the open predictions as issued, for grading (withdrawn snapshots are kept and never graded) |
| `history/first_values.csv` | first published value seen for each graded quantity (grades never move with later refits) |
| `scorecard.csv` | graded predictions (appended by `grade.py`) |

`data/raw/downloads/` (raw pages, 236 MB) is not committed. The one file the model needs from downloads, Epoch's
posterior draws, is committed as `data/raw/eci_posterior_draws.csv.gz`.

## When a new model ships

1. Add the release to `data/models.json` (the site's normal process) and its chart rows to `data/benchmarks.json`.
2. Refresh `capability/data/raw/eci_public.csv`, `eci_benchmarks.csv`, `eci_posterior_draws.csv.gz` from Epoch, and append the
   card's AECI rows to `aeci_all.csv` (`own_card=1` for the new model's own value; a new `fit_card` needs an entry in
   `AECI_FIT` in `build_data.py` and `FIT_ORDER` in `capmodel/aeci.py`).
3. `python3 capability/grade.py` grades every open prediction that can now be resolved and appends to `scorecard.csv`.
   The first value it sees for a quantity is stored in `history/first_values.csv` and is what gets graded. Predictions whose
   value is not published yet stay open; after their `expires` date they are recorded as expired.
4. Set `AS_OF` in `capmodel/common.py`, run `python3 capability/run.py`, and commit. The new run writes a new
   `history/predictions_<date>_<version>.json`; earlier snapshots are left alone.

Grade first, then re-run: the scorecard must be filled from predictions issued before the release.
