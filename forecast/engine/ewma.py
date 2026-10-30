"""The repo's original EWMA model (claude-models.html) as a probability
distribution, so it can be scored with the same rules and pooled.

Its window is read as a central 80% interval of a normal on the release date,
truncated to dates on or after the origin; an overdue family is centred on the
origin. This is a generous reading — the page never claimed a coverage level.
"""
from __future__ import annotations

import numpy as np
from scipy.stats import norm

from .data import d


def ewma_pmf(fam: dict, origin, H: int):
    if not fam:
        return None
    o = d(origin)
    centre = o if fam["overdue"] else d(fam["predictedDate"])
    sd = max(fam["spreadDays"], 3) / 1.2816
    mu = (centre - o).days
    edges = np.arange(H + 1) - 0.5
    cdf = norm.cdf(edges, mu, sd)
    lo = 1 - cdf[0]
    pmf = np.diff(cdf) / max(lo, 1e-12)
    tail = max(0.0, 1.0 - pmf.sum())
    return pmf, tail
