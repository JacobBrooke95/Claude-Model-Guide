"""Stage 2 backtests for the final (v2) configuration and its ablations.

    python3 run_all.py --part=lock     # lockbox origins ≥ 2025-07-07
    python3 run_all.py --part=tune     # tuning origins 2024-06 → 2025-06 (same configs, for comparison)
    python3 run_all.py --part=events   # event view (CRPS / PIT / date error)

History of the configuration, kept because it matters for reading the scores:
  v1  = stage-1 winner weibull|linear|w0.5 (output/tuning_ranking.csv). Its
        lockbox run was the clean, untouched test. It beat climatology but
        lost to the repo's EWMA at 30/90 days on Opus/Sonnet/Haiku.
  v2  = stage-1b winner (output/tuning_v2_ranking.csv), which added recency
        weighting of past gaps. Chosen on tuning origins only, but designed
        after seeing v1's lockbox, so v2's lockbox score is post-hoc.
"""
from __future__ import annotations

import sys
from dataclasses import replace

import pandas as pd

from engine import backtest as bt
from engine.data import load_competitors, load_releases, load_signals
from engine.forecast import Config, FitCache

PART = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--part=")), "lock")
DATA_END = "2026-10-29"
LOCK_START = "2025-07-07"

rel, comp, sig = load_releases(), load_competitors(), load_signals()


def parse(cfg):
    p = cfg.split("|")
    hl = None
    if len(p) > 3 and p[3] != "hlNone":
        hl = float(p[3][2:])
    return Config(err=p[0], trend=p[1], w_wave=float(p[2][1:]), half_life=hl)


V1 = parse(pd.read_csv("output/tuning_ranking.csv").config.iloc[0])
V2 = parse(pd.read_csv("output/tuning_v2_ranking.csv").config.iloc[0])
print("v1:", V1, "\nv2:", V2, flush=True)

configs = {
    "v1": V1,
    "base": V2,
    "base_nocal": replace(V2, weekday=False, holiday=False),
    "wave_half": replace(V2, w_wave=0.5),
    "comp_major": replace(V2, competitor="major21"),
    "comp_sota": replace(V2, competitor="sota30"),
    "signals": replace(V2, signals=True),
    "full": replace(V2, signals=True, competitor="sota30"),
    "sig_rho35_cap8": replace(V2, signals=True, rho=0.35, cap=8.0),
    "sig_rho70_cap5": replace(V2, signals=True, rho=0.7, cap=5.0),
    "sig_noabsence": replace(V2, signals=True, absence=False),
    # v3 (post-hoc, after the v2 lockbox): pool the signal model with the repo's EWMA
    "ensemble": replace(V2, signals=True, w_ewma=0.3),
    "ensemble50": replace(V2, signals=True, w_ewma=0.5),
    # final (v3b): ensemble without the absence-of-evidence term, which hurt in
    # both periods — consistent with detection rates inflated by hindsight
    "final": replace(V2, signals=True, absence=False, w_ewma=0.3),
}
ONLY = next((a.split("=", 1)[1].split(",") for a in sys.argv if a.startswith("--only=")), None)
if ONLY:
    configs = {k: v for k, v in configs.items() if k in ONLY}
SUFFIX = "_" + "-".join(ONLY) if ONLY else ""
cache = FitCache()
if PART == "lock":
    df, _ = bt.run(rel, comp, sig, configs, bt.weekly_origins(LOCK_START, "2026-10-26"), DATA_END, cache=cache, progress=True)
    df.to_pickle(f"output/lockbox_scores_v2{SUFFIX}.pkl")
elif PART == "tune":
    df, _ = bt.run(rel, comp, sig, configs, bt.weekly_origins("2024-06-03", "2025-06-30"), DATA_END, cache=cache, progress=True)
    df.to_pickle(f"output/tuning_full_scores_v2{SUFFIX}.pkl")
else:
    keep = [k for k in ["v1", "base", "signals", "full", "sig_noabsence", "ensemble", "final"] if k in configs]
    ev = bt.run_events(rel, comp, sig, {k: configs[k] for k in keep}, bt.event_origins(rel), cache=cache)
    ev.to_pickle(f"output/event_scores_v2{SUFFIX}.pkl")
print("part done", PART, flush=True)
