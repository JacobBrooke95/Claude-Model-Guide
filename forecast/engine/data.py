"""Data loading and small date helpers for the release forecaster.

Every function that takes an `asof` date returns only what was knowable on
that date. That rule is what keeps the backtest honest: the forecaster never
sees a release, a signal or a competitor launch dated after its origin.
"""
from __future__ import annotations

import os
from datetime import date, timedelta

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data")

# Families with their own cadence process. `legacy` (Claude 1/2/2.1) predates
# the tiered lineup and only feeds the weekday profile and the all-releases view.
FAMILIES = ["opus", "sonnet", "haiku", "fable", "mythos"]
FRONTIER = ["opus", "fable", "mythos"]  # "top-tier" releases


def d(s) -> pd.Timestamp:
    return pd.Timestamp(s).normalize()


def load_releases() -> pd.DataFrame:
    df = pd.read_csv(os.path.join(DATA, "anthropic_releases.csv"), parse_dates=["date"])
    return df.sort_values("date").reset_index(drop=True)


def load_competitors() -> pd.DataFrame:
    p = os.path.join(DATA, "competitor_releases.csv")
    if not os.path.exists(p):
        return pd.DataFrame(columns=["date", "lab", "model", "tier", "is_major", "took_sota", "beat_claude_coding"])
    df = pd.read_csv(p, parse_dates=["date"])
    for c in ["is_major", "took_sota", "beat_claude_coding"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    return df.sort_values("date").reset_index(drop=True)


def load_signals() -> pd.DataFrame:
    p = os.path.join(DATA, "signals.csv")
    if not os.path.exists(p):
        return pd.DataFrame(columns=["release_id", "family", "signal_class", "first_seen", "is_false", "grade"])
    df = pd.read_csv(p, parse_dates=["first_seen", "release_date"])
    return df.sort_values("first_seen").reset_index(drop=True)


def releases_asof(rel: pd.DataFrame, asof) -> pd.DataFrame:
    """Releases strictly before the origin day (the origin day itself is the
    first day being forecast)."""
    return rel[rel["date"] < d(asof)]


def family_history(rel: pd.DataFrame, family: str, asof) -> list[pd.Timestamp]:
    r = releases_asof(rel, asof)
    return list(r.loc[r["family"] == family, "date"].drop_duplicates())


def next_release(rel: pd.DataFrame, family: str, asof):
    r = rel[(rel["family"] == family) & (rel["date"] >= d(asof))]
    return None if r.empty else r["date"].iloc[0]


def weekday_profile(rel: pd.DataFrame, asof, alpha: float = 1.0) -> np.ndarray:
    """Multiplicative weekday hazard factors (Mon=0..Sun=6), mean 1, from
    distinct release days before `asof`, Dirichlet-smoothed with `alpha`
    pseudo-counts on weekdays and a tenth of that on weekend days."""
    days = releases_asof(rel, asof)["date"].drop_duplicates()
    counts = np.bincount(days.dt.weekday, minlength=7).astype(float)
    prior = np.array([alpha] * 5 + [alpha * 0.1] * 2)
    p = (counts + prior) / (counts + prior).sum()
    return p * 7.0


def holiday_mask(days: pd.DatetimeIndex) -> np.ndarray:
    """US end-of-year freeze: Dec 20 – Jan 4. No Anthropic model has shipped
    in that window (2023–2025)."""
    m, dd = days.month, days.day
    return ((m == 12) & (dd >= 20)) | ((m == 1) & (dd <= 4))
