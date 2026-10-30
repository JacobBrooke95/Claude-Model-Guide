"""Stage 1b (added 2026-10-30 after v1's lockbox showed the model adapting too
slowly to the 2025–26 cadence): recency weighting (half-life) × trend × wave
weight. Selection still uses ONLY tuning origins (< 2025-07-01). Because the
lockbox has now been looked at once, v2's lockbox score is reported as
post-hoc, and the clean test is the forward log (forecast_log.csv)."""
import itertools
import pandas as pd
from engine.data import load_releases
from engine.forecast import Config
from engine import backtest as bt

rel = load_releases()
origins = bt.weekly_origins("2024-06-03", "2025-06-30")
configs = {}
for trend, hl, w in itertools.product(["none", "linear", "changepoint"], [None, 1.5, 0.75], [0.0, 0.5]):
    configs[f"weibull|{trend}|w{w}|hl{hl}"] = Config(err="weibull", trend=trend, w_wave=w, half_life=hl)
df, _ = bt.run(rel, None, None, configs, origins, data_end="2026-10-29", with_ewma=True, progress=True)
df.to_pickle("output/tuning_v2_scores.pkl")
print("done", len(df))
