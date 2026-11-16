# Capability model

Forecasts the capability of Anthropic's next models and of the frontier through 2030: public ECI, AECI, and the benchmarks the
site charts. Methods, tables and limitations are in [METHODS.md](METHODS.md); the research it rests on is in `research/`.

## Run

```
python3 capability/run.py            # data layer -> backtests -> fit -> predictions -> projection -> outputs (2-3 min)
python3 capability/run.py --full     # also recompute the cached leave-future-out IRT refits (capability/cache/)
python3 capability/run.py --check    # verify outputs are current (input hash), strict JSON, ordered intervals
python3 -m unittest discover -s capability/tests -v
python3 capability/grade.py          # resolve open predictions whose release has shipped -> scorecard.csv
```

Needs Python 3.13 with numpy, scipy, pandas and Pillow. One fixed seed (`capmodel/common.py`); the same inputs give the same outputs.

## Layout

| Path | What |
|---|---|
| `build_data.py` | canonical tables in `data/` from `data/raw/*.csv`, `../data/models.json`, `../data/benchmarks.json`; `data/build_log.csv` lists every rename, conflict and dropped row |
| `capmodel/trend.py` | frontier trend candidates, bootstrap, CRPS stacking |
| `capmodel/families.py` | family offsets with partial pooling |
| `capmodel/aeci.py` | ECI to AECI mapping and refit drift |
| `capmodel/links.py` | benchmark link functions |
| `capmodel/irt.py` | own IRT refit for leave-future-out vintages |
| `capmodel/core.py` | the model as fitted at one origin date (used by backtest and live forecast alike) |
| `capmodel/backtest.py` | rolling-origin folds, baselines, calibration, break reference class |
| `capmodel/predict.py` | release-date sampler over `../forecast/output/forecast.json` |
| `capmodel/project.py` | 2026-2030 scenario simulation |
| `capmodel/pipeline.py`, `report.py`, `plots.py` | orchestration, JSON and METHODS.md, PNG diagnostics |
| `output/capability_forecast.json` | everything a page needs (see its `metadata`) |
| `output/*.png` | diagnostic plots |
| `history/predictions_<date>.json` | the open predictions as issued, for grading |
| `scorecard.csv` | graded predictions (appended by `grade.py`) |

`data/raw/downloads/` (raw pages, 236 MB) and `cache/` are not committed. The one file the model needs from downloads, Epoch's
posterior draws, is committed as `data/raw/eci_posterior_draws.csv.gz`.

## When a new model ships

1. Add the release to `data/models.json` (the site's normal process) and its chart rows to `data/benchmarks.json`.
2. Refresh `capability/data/raw/eci_public.csv`, `eci_benchmarks.csv`, `eci_posterior_draws.csv.gz` from Epoch, and append the
   card's AECI rows to `aeci_all.csv` (`own_card=1` for the new model's own value; a new `fit_card` needs an entry in
   `AECI_FIT` in `build_data.py` and `FIT_ORDER` in `capmodel/aeci.py`).
3. `python3 capability/grade.py` grades every open prediction that can now be resolved and appends to `scorecard.csv`.
   Predictions whose value is not published yet (Epoch usually lags a release by days) stay open; run it again later.
4. Set `AS_OF` in `capmodel/common.py`, run `python3 capability/run.py`, and commit. The new run writes a new
   `history/predictions_<date>.json`; earlier snapshots are left alone.

Grade first, then re-run: the scorecard must be filled from predictions issued before the release.
