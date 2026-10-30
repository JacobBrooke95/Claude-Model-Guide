"""Post-review backtest (after the adversarial review of 2026-10-30).

Changes from run_all.py: EWMA baseline called as of the day before each origin
(same-day leak fixed), signal false-alarm floor 0.01, A/B-grade sightings
preferred, four MCMC chains averaged per origin, a 180-day recent-rate
baseline. Writes output/final_{lock,tune,events}.pkl.

    python3 run_final.py --part=lock|tune|events
"""
import sys
from dataclasses import replace

import pandas as pd

from engine import backtest as bt
from engine.data import load_competitors, load_releases, load_signals
from engine.forecast import Config, FitCache

PART = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--part=")), "lock")
DATA_END = "2026-10-29"
rel, comp, sig = load_releases(), load_competitors(), load_signals()


def parse(cfg):
    p = cfg.split("|")
    hl = float(p[3][2:]) if len(p) > 3 and p[3] != "hlNone" else None
    return Config(err=p[0], trend=p[1], w_wave=float(p[2][1:]), half_life=hl)


V1 = parse(pd.read_csv("output/tuning_ranking.csv").config.iloc[0])
V2 = replace(parse(pd.read_csv("output/tuning_v2_ranking.csv").config.iloc[0]), n_seeds=4)
configs = {
    "v1": V1,
    "base": V2,
    "signals": replace(V2, signals=True, absence=False),
    "signals_abs": replace(V2, signals=True, absence=True),
    "comp_major": replace(V2, competitor="major21"),
    "final": replace(V2, signals=True, absence=False, w_ewma=0.3),
}
cache = FitCache()
if PART == "lock":
    df, _ = bt.run(rel, comp, sig, configs, bt.weekly_origins("2025-07-07", "2026-10-26"), DATA_END, cache=cache, progress=True)
    df.to_pickle("output/final_lock.pkl")
elif PART == "tune":
    df, _ = bt.run(rel, comp, sig, configs, bt.weekly_origins("2024-06-03", "2025-06-30"), DATA_END, cache=cache, progress=True)
    df.to_pickle("output/final_tune.pkl")
else:
    keep = {k: configs[k] for k in ("v1", "base", "signals", "final")}
    bt.run_events(rel, comp, sig, keep, bt.event_origins(rel), cache=cache).to_pickle("output/final_events.pkl")
print("part done", PART, flush=True)
