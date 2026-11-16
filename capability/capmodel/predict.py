"""Next-model predictions per family, integrating the release-date distribution from the
site's release forecaster (forecast/output/forecast.json), trend uncertainty, the family
offset and the model-combination weights."""
from __future__ import annotations
import datetime as dt
import re
import numpy as np

from .common import REPO, load_json, to_date, yr, AS_OF, summarize, widen, FAMILIES
from .families import version_type_of_name

T_NOW = yr(AS_OF)


class ReleaseDates:
    """Sampler for 'days until the family's next release' built from forecast.json.

    Days 0-179 use the published daily pmf. Beyond that the CDF is linearly interpolated
    through the published quantiles / 'by' dates that fall after day 179, then continued
    with a constant hazard (that of the last known segment) until 99.9%."""

    def __init__(self, path=None):
        self.fc = load_json(path or REPO / "forecast" / "output" / "forecast.json")
        self.as_of = to_date(self.fc["as_of"])
        self.cdf = {}
        for f in FAMILIES + ["frontier"]:
            self.cdf[f] = self._build(self.fc["targets"][f]["with_signals"])

    def _build(self, t):
        c = np.asarray(t["cdf180"], float)
        days = list(range(len(c)))
        vals = list(c)
        extra = []
        for k, p in (("q10", 0.10), ("q25", 0.25), ("median", 0.5), ("q75", 0.75), ("q90", 0.90)):
            dd = (to_date(t[k]) - self.as_of).days
            if dd > days[-1] and p > vals[-1]:
                extra.append((dd, p))
        for ds, p in t.get("by", {}).items():
            dd = (to_date(ds) - self.as_of).days
            if dd > days[-1] and p > vals[-1]:
                extra.append((dd, float(p)))
        for dd, p in sorted(set(extra)):
            if dd > days[-1] and p > vals[-1]:
                days.append(dd)
                vals.append(p)
        # constant-hazard tail from the last segment
        d1, d0 = days[-1], days[-2] if len(days) > 180 else days[-31]
        p1, p0 = vals[-1], vals[days.index(d0)]
        haz = max(np.log((1 - p0) / (1 - p1)) / max(d1 - d0, 1), 1e-4)
        dd, p = d1, p1
        while p < 0.999 and dd < 2000:
            dd += 15
            p = 1 - (1 - p1) * np.exp(-haz * (dd - d1))
            days.append(dd)
            vals.append(min(p, 0.9995))
        return np.asarray(days, float), np.maximum.accumulate(np.asarray(vals, float))

    def sample_days(self, family, n, rng):
        days, cdf = self.cdf[family]
        u = rng.random(n) * cdf[-1]
        return np.interp(u, np.concatenate([[0.0], cdf]), np.concatenate([[0.0], days]))

    def summary(self, family):
        t = self.fc["targets"][family]["with_signals"]
        return {k: t[k] for k in ("q10", "q25", "median", "q75", "q90")} | {
            "p_within_30d": round(t["p30"], 3), "p_within_90d": round(t["p90"], 3),
            "source": "forecast/output/forecast.json (with_signals), as_of " + self.fc["as_of"]}

    def names(self, family):
        return dict(self.fc["params"][family]["names"])

    def gap_years(self, family):
        return float(self.fc["cadence_params"][family]["median_gap_now_days"]) / 365.25


def type_probs(names: dict, last_version: float, last_gen: int):
    out = {}
    for nm, p in names.items():
        ty = version_type_of_name(nm, last_gen)
        out[ty] = out.get(ty, 0.0) + float(p)
    return out


def refit_count(rd: ReleaseDates, family, days_f, n, rng):
    """Number of AECI card refits from now up to and including the family's own card:
    1 + releases of the other card-publishing families before it (Fable and Mythos share a card)."""
    cards = {"opus": "opus", "sonnet": "sonnet", "haiku": "haiku", "fable": "fable", "mythos": "fable"}
    K = np.ones(n)
    for g in ("opus", "sonnet", "haiku", "fable"):
        if cards[family] == g:
            continue
        dg = rd.sample_days(g, n, rng)
        gap = rd.gap_years(g) * 365.25
        before = dg < days_f
        K += before + np.where(before, np.floor((days_f - dg) / gap), 0)
    return K.astype(int)
