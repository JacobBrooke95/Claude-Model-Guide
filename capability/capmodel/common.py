"""Shared paths, constants and small helpers. No modelling here."""
from __future__ import annotations
import datetime as dt
import json
import math
from pathlib import Path

import numpy as np

SEED = 20261116
AS_OF = "2026-11-16"
MODEL_VERSION = "cap-v2.2"
PREDICTION_VERSION = "cap-v2.1"      # version under which the open predictions were issued; v2.2 adds a variant only

ROOT = Path(__file__).resolve().parents[1]          # capability/
REPO = ROOT.parent
RAW = ROOT / "data" / "raw"
DATA = ROOT / "data"
OUT = ROOT / "output"
CACHE = ROOT / "cache"

FAMILIES = ["opus", "sonnet", "haiku", "fable", "mythos"]
LEVELS = (0.5, 0.8, 0.95)
EPOCH0 = dt.date(2020, 1, 1)


def rng(tag: str = "") -> np.random.Generator:
    """Deterministic generator: fixed seed plus a stable hash of a tag."""
    h = sum((i + 1) * ord(c) for i, c in enumerate(tag)) % 1_000_003
    return np.random.default_rng([SEED, h])


def to_date(s) -> dt.date:
    if isinstance(s, dt.datetime):
        return s.date()
    if isinstance(s, dt.date):
        return s
    return dt.date.fromisoformat(str(s)[:10])


def yr(d) -> float:
    """Decimal year of a date (365.25-day years since 2020-01-01, plus 2020)."""
    return 2020.0 + (to_date(d) - EPOCH0).days / 365.25


def from_yr(y: float) -> dt.date:
    return EPOCH0 + dt.timedelta(days=int(round((y - 2020.0) * 365.25)))


def q(x, probs):
    return [float(v) for v in np.quantile(np.asarray(x, float), probs)]


def summarize(x, nd=2) -> dict:
    """Median and central 50/80/95% intervals of a sample."""
    x = np.asarray(x, float)
    x = x[np.isfinite(x)]
    if x.size == 0:
        return {"median": None, "mean": None, "lo50": None, "hi50": None, "lo80": None,
                "hi80": None, "lo95": None, "hi95": None}
    p = np.quantile(x, [0.5, 0.25, 0.75, 0.10, 0.90, 0.025, 0.975])
    r = lambda v: round(float(v), nd)
    return {"median": r(p[0]), "mean": r(x.mean()), "lo50": r(p[1]), "hi50": r(p[2]),
            "lo80": r(p[3]), "hi80": r(p[4]), "lo95": r(p[5]), "hi95": r(p[6])}


def widen(x, factor_by_level: dict, center=None, nd=2):
    """Summarize a sample, then stretch each interval about the median by a calibration
    factor (one per nominal level). Used for conformal-style widening."""
    s = summarize(x, 4)
    if s["median"] is None:
        return s
    m = s["median"] if center is None else center
    out = {"median": round(m, nd), "mean": round(s["mean"], nd)}
    lo_w = hi_w = 0.0
    for lv, tag in ((0.5, "50"), (0.8, "80"), (0.95, "95")):
        f = float(factor_by_level.get(lv, 1.0))
        lo_w = max(lo_w, f * (m - s["lo" + tag]))     # a wider level is never narrower than the one inside it
        hi_w = max(hi_w, f * (s["hi" + tag] - m))
        out["lo" + tag] = round(m - lo_w, nd)
        out["hi" + tag] = round(m + hi_w, nd)
    return out


def clean(o):
    """Make an object strict-JSON safe: NaN/inf -> None, numpy -> python."""
    if isinstance(o, dict):
        return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [clean(v) for v in o]
    if isinstance(o, (np.floating, float)):
        v = float(o)
        return None if (math.isnan(v) or math.isinf(v)) else v
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.bool_,)):
        return bool(o)
    if isinstance(o, np.ndarray):
        return clean(o.tolist())
    if isinstance(o, (dt.date, dt.datetime)):
        return o.isoformat()[:10]
    if o is None or isinstance(o, (str, int, bool)):
        return o
    try:
        import pandas as pd
        if o is pd.NaT or pd.isna(o):
            return None
    except Exception:
        pass
    return str(o)


def dump_json(obj, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    txt = json.dumps(clean(obj), indent=1, allow_nan=False, sort_keys=False)
    path.write_text(txt + "\n")


def load_json(path: Path):
    return json.loads(Path(path).read_text())


def wquantile(x, w, probs):
    """Weighted quantiles of x (1-d) with weights w."""
    x = np.asarray(x, float)
    w = np.asarray(w, float)
    ok = np.isfinite(x) & (w > 0)
    x, w = x[ok], w[ok]
    if x.size == 0:
        return [float("nan")] * len(probs)
    o = np.argsort(x)
    x, w = x[o], w[o]
    c = (np.cumsum(w) - 0.5 * w) / w.sum()
    return [float(v) for v in np.interp(probs, c, x)]


def wsummary(x, w, nd=2):
    p = wquantile(x, w, [0.5, 0.25, 0.75, 0.10, 0.90, 0.025, 0.975])
    r = lambda v: None if not np.isfinite(v) else round(float(v), nd)
    return {"median": r(p[0]), "lo50": r(p[1]), "hi50": r(p[2]), "lo80": r(p[3]), "hi80": r(p[4]),
            "lo95": r(p[5]), "hi95": r(p[6])}
