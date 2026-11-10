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

# Polymarket ladder wording, e.g. "Next Fable Model (5.2+) released by November 30, 2026?"
# and "Next Claude Opus (5.6+) released by December 31, 2026?". The version in brackets is
# the lowest version that resolves the ladder Yes, so it says which "next model" the ladder
# is about. It is captured, not hard-coded: when a model ships Polymarket opens a new ladder
# with a higher threshold, and `ladders(..., latest=)` keeps only ladders whose threshold is
# above the family's latest released version. A ladder about a model that has already
# shipped is a closed question and is dropped. This is data parsing, not a model setting.
_V = r"\((\d+(?:\.\d+)?)\+\)"
LADDERS = {
    "fable": r"^Next (?:Claude )?Fable(?: Model)? " + _V + r" released by (.+?)\?$",
    "opus": r"^Next (?:Claude )?Opus(?: Model)? " + _V + r" released by (.+?)\?$",
    "sonnet": r"^Next (?:Claude )?Sonnet(?: Model)? " + _V + r" released by (.+?)\?$",
    "haiku": r"^Next (?:Claude )?Haiku(?: Model)? " + _V + r" released by (.+?)\?$",
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


def ladders(markets: pd.DataFrame, platform="Polymarket", latest: dict | None = None):
    """Per-family ladder of P(released by date). `latest` maps family -> latest
    released version; a ladder is kept only if its threshold version is above
    it. If a family has ladders at two thresholds, the lowest remaining one is
    used (it is the one about the next model)."""
    out = {}
    m = markets[markets.platform == platform]
    for fam, pat in LADDERS.items():
        rows = []
        for _, r in m.iterrows():
            g = re.match(pat, str(r.question))
            if g:
                thr = float(g.group(1))
                if latest and fam in latest and thr <= float(latest[fam]) + 1e-9:
                    continue
                try:
                    dt = pd.Timestamp(g.group(2))
                except Exception:
                    continue
                rows.append((thr, dt, float(r.prob), _vol(r.volume)))
        if not rows:
            continue
        lo = min(x[0] for x in rows)
        rows = sorted(x[1:] for x in rows if x[0] == lo)
        dts, p, w = zip(*rows)
        out[fam] = pd.DataFrame(dict(date=dts, raw=p, volume=w, prob=isotonic(np.array(p), np.log1p(np.array(w)))))
    return out


def pool(p_model, p_market, w=W_MARKET):
    pm = np.clip(p_model, 1e-4, 1 - 1e-4)
    pk = np.clip(p_market, 1e-4, 1 - 1e-4)
    lo = (1 - w) * np.log(pm / (1 - pm)) + w * np.log(pk / (1 - pk))
    return 1 / (1 + np.exp(-lo))
