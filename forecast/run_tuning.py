"""Stage 1: choose the cadence error family, trend form and wave weight using
ONLY origins before 2025-07-01. The lockbox (origins ≥ 2025-07-01) is not
scored here."""
import itertools, pickle, sys
import pandas as pd
from engine.data import load_releases
from engine.forecast import Config, FitCache
from engine import backtest as bt

rel = load_releases()
origins = bt.weekly_origins("2024-06-03", "2025-06-30")
configs = {}
for err, trend, w in itertools.product(["weibull", "normal", "t"], ["changepoint", "linear", "none"], [0.0, 0.5, 1.0]):
    configs[f"{err}|{trend}|w{w}"] = Config(err=err, trend=trend, w_wave=w, weekday=True, holiday=True)
df, cache = bt.run(rel, None, None, configs, origins, data_end="2026-10-29", with_ewma=True, progress=True)
df.to_pickle("output/tuning_scores.pkl")
print("done", len(df))
