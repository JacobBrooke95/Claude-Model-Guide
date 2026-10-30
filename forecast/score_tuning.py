"""Rank stage-1 configurations on the tuning period only."""
import numpy as np
import pandas as pd
from engine import backtest as bt

df = pd.read_pickle("output/tuning_scores.pkl")
cfg_cols = [c for c in df.columns if "|" in c]
tg = ["opus", "sonnet", "haiku", "frontier", "any"]
d = df[df.target.isin(tg)]
rows = []
for c in cfg_cols + ["clim", "ewma"]:
    sub = d.dropna(subset=[c])
    r = dict(config=c, n=len(sub))
    for h in (7, 30, 90):
        s = sub[sub.h == h]
        r[f"brier{h}"] = bt.brier(s[c], s.y)
        r[f"ll{h}"] = bt.logloss(s[c], s.y)
    r["mean_brier"] = np.mean([r[f"brier{h}"] for h in (7, 30, 90)])
    r["mean_ll"] = np.mean([r[f"ll{h}"] for h in (7, 30, 90)])
    rows.append(r)
res = pd.DataFrame(rows).sort_values("mean_ll")
pd.set_option("display.width", 200)
print(res.round(4).to_string(index=False))
# ewma is only defined for opus/sonnet/haiku — compare like with like
d3 = d[d.target.isin(["opus", "sonnet", "haiku"])]
best = res.config.iloc[0]
print("\nopus/sonnet/haiku only:")
for c in [best, "clim", "ewma"]:
    for h in (7, 30, 90):
        s = d3[d3.h == h].dropna(subset=[c])
        print(f"  {c:28s} h={h:3d} brier={bt.brier(s[c], s.y):.4f} ll={bt.logloss(s[c], s.y):.4f} n={len(s)}")
res.to_csv("output/tuning_ranking.csv", index=False)
