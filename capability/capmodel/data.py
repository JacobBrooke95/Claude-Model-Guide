"""Load the canonical tables and build the frontier series used by the model."""
from __future__ import annotations
import numpy as np
import pandas as pd

from .common import DATA, RAW, yr
from .trend import Series

ALL_START = 2023.15     # all-lab frontier starts at GPT-4 (Mar 2023); the Feb 2023 LLaMA row is not a frontier model
ANTH_START = 2023.4     # Anthropic frontier starts at Claude 2


class D:
    """Bundle of canonical tables."""

    def __init__(self):
        self.models = pd.read_csv(DATA / "models.csv")
        self.index = pd.read_csv(DATA / "index_values.csv")
        self.bench = pd.read_csv(DATA / "benchmark_scores.csv")
        self.meta = pd.read_csv(DATA / "benchmarks_meta.csv")
        self.draws = pd.read_csv(RAW / "eci_posterior_draws.csv.gz", index_col=0)
        m = self.models
        m["t"] = m.release_date.map(yr)
        self.bench["t"] = self.bench.release_date.map(yr)
        self.eci_models = m[m.in_public_eci == 1].reset_index(drop=True)

    def ability_table(self, abilities: pd.Series | None = None, draws: pd.DataFrame | None = None):
        """Models with an ability. `abilities` (model_id -> value) overrides the published
        ECI, e.g. with a vintage IRT refit; in that case draws are the published draws
        shifted to the new point estimate (posterior shape kept, location replaced)."""
        e = self.eci_models.copy()
        Y = self.draws.loc[e.model_id].to_numpy()
        if abilities is not None:
            e = e[e.model_id.isin(abilities.index)].reset_index(drop=True)
            Y = self.draws.loc[e.model_id].to_numpy()
            new = abilities.loc[e.model_id].to_numpy()
            Y = Y - e.eci.to_numpy()[:, None] + new[:, None]
            e["eci"] = new
        return e, Y

    def series(self, which="all", abilities=None):
        e, Y = self.ability_table(abilities)
        if which == "anthropic":
            m = (e.lab == "Anthropic").to_numpy()
            return Series(e.t.to_numpy()[m], Y[m], e.eci.to_numpy()[m], e.model_id.to_numpy()[m], ANTH_START)
        if which == "others":
            m = (e.lab != "Anthropic").to_numpy()
            return Series(e.t.to_numpy()[m], Y[m], e.eci.to_numpy()[m], e.model_id.to_numpy()[m], ALL_START)
        return Series(e.t.to_numpy(), Y, e.eci.to_numpy(), e.model_id.to_numpy(), ALL_START)

    def claude(self, abilities=None):
        """Claude releases in the five tracked families that have an ability, in date order."""
        e, _ = self.ability_table(abilities)
        c = e[(e.lab == "Anthropic") & e.family.isin(["opus", "sonnet", "haiku", "fable"])]
        return c.sort_values(["t", "model_id"]).reset_index(drop=True)

    def aeci(self, fit="fable5.2", printed_or_read=True):
        a = self.index[(self.index.scale == "aeci") & (self.index.fit == fit)]
        return a.merge(self.models[["model_id", "release_date", "t", "family", "eci", "twin", "internal_date"]],
                       on="model_id", how="left")
