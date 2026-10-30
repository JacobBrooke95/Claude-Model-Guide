"""Prediction markets as an input.

Markets aggregate the same leaks the signal layer reads (TestingCatalog →
X → Polymarket), so stacking them on top of the signal-updated model would
count that evidence twice. They are used two ways instead:

  1. Displayed side by side with the model at each market date, so the gap
     between them is visible ("the difference is the bet", as the vault's
     predictions register puts it).
  2. A headline blend: logarithmic (geometric) pooling of the model's and
     the market's P(released by date), weight W_MARKET set a priori at 0.5.
     There are too few historical market readings to fit it.

Ladder markets are cleaned with a volume-weighted isotonic fit, because thin
daily rungs are sometimes non-monotone (Polymarket "by Nov 9" 0.475 vs
"by Nov 6" 0.515 on 10/30).
"""
from __future__ import annotations

import re

import numpy as np
import pandas as pd

W_MARKET = 0.5

LADDERS = {
    "fable": r"^Next Fable Model \(5\.2\+\) released by (.+?)\?$",
    "opus": r"^Next Claude Opus \(5\.6\+\) released by (.+?)\?$",
    "sonnet": r"^Next Claude Sonnet \(5\.6\+\) released by (.+?)\?$",
    "haiku": r"^Next Claude Haiku \(5\.6\+\) released by (.+?)\?$",
}


def _vol(v):
    try:
        return float(str(v).split()[0].replace(",", ""))
    except Exception:
        return 1.0


def isotonic(x, w):
    """Pool-adjacent-violators for a non-decreasing fit."""
    blocks = [[xi, wi, 1] for xi, wi in zip(x, w)]
    i = 0
    while i < len(blocks) - 1:
        if blocks[i][0] > blocks[i + 1][0]:
            a, b = blocks[i], blocks[i + 1]
            wt = a[1] + b[1]
            blocks[i] = [(a[0] * a[1] + b[0] * b[1]) / wt, wt, a[2] + b[2]]
            del blocks[i + 1]
            i = max(i - 1, 0)
        else:
            i += 1
    out = []
    for v, _, n in blocks:
        out += [v] * n
    return np.array(out)


def ladders(markets: pd.DataFrame, platform="Polymarket"):
    out = {}
    m = markets[markets.platform == platform]
    for fam, pat in LADDERS.items():
        rows = []
        for _, r in m.iterrows():
            g = re.match(pat, str(r.question))
            if g:
                try:
                    dt = pd.Timestamp(g.group(1))
                except Exception:
                    continue
                rows.append((dt, float(r.prob), _vol(r.volume)))
        if not rows:
            continue
        rows.sort()
        dts, p, w = zip(*rows)
        out[fam] = pd.DataFrame(dict(date=dts, raw=p, volume=w, prob=isotonic(np.array(p), np.log1p(np.array(w)))))
    return out


def pool(p_model, p_market, w=W_MARKET):
    pm = np.clip(p_model, 1e-4, 1 - 1e-4)
    pk = np.clip(p_market, 1e-4, 1 - 1e-4)
    lo = (1 - w) * np.log(pm / (1 - pm)) + w * np.log(pk / (1 - pk))
    return 1 / (1 + np.exp(-lo))
