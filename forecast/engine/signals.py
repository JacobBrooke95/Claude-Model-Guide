"""Layer 3 — pre-release signal likelihoods.

A signal is a public trace that a model is coming: a cloud-catalog row, a
model ID in a client, an arena codename, a press report, a tipster claim. Each
belongs to a class with three parameters, all estimated at the forecast
origin from signals already *resolved* by then (target shipped, or 120 days
passed without it):

    q_c   detection rate: share of recent releases that had a class-c signal
    d_c   lead-time density: days from first sighting to release (log-normal,
          shrunk toward the all-class pool)
    λ_c   false-alarm rate: class-c signals per family-day that led nowhere

Given the signals visible for family f at origin t, the likelihood of the next
release landing on day τ is

    observed class c, first seen s:  L_c(τ) = q_c · d_c(τ − s) + λ_c
    no class-c signal yet:           L_c(τ) = 1 − q_c · P(τ − t < L_c ≤ τ − last_f)   (off in the final model)

λ_c gets a floor of 0.01 per family-day: the researched false-alarm list is a
hindsight sample (one false row before 2026), so the fitted rate would be
near zero and every sighting would hit the cap. 0.01 means a misleading
sighting of each class roughly every hundred days per family, in line with the
2026 record (11+ EAP codenames against 8 launches, repeated mistimed tipster calls).

The second line is the absence-of-evidence term: if catalog rows usually
appear 2–5 days early and none has appeared, a release tomorrow is less likely.

Two guards against the hindsight bias of signal data collected after the fact:
the product over classes is tempered by (1 − ρ) because classes share
sources (TestingCatalog feeds tipsters, press and markets), and every class's
likelihood ratio against its far-future value is capped at `cap`.
"""
from __future__ import annotations

import numpy as np
import pandas as pd
from scipy import stats

from .data import d

# Coarse classes (raw codes in data/signals.csv → estimation class).
CLASS_OF = {
    "CLOUD_CATALOG": "infra",      # Bedrock / Vertex / Azure rows
    "FIRST_PARTY_DOC": "infra",    # docs, status page, SDK constants, system-card URLs
    "SDK_COMMIT": "infra",
    "CLIENT_STRING": "client",     # Cursor / Devin / Copilot / app bundle strings
    "ARENA_CODENAME": "client",
    "EAP_PARTNER": "report",       # partners have it
    "RED_TEAM": "report",          # red-team codename rounds (Neptune, Jupiter, Oceanus)
    "AB_ROUTING": "report",        # traffic apparently routed to a stronger checkpoint
    "PRESS_REPORT": "report",      # Information / Bloomberg / Verge …
    "TIPSTER": "soft",             # X / Reddit claim with no artifact
    "EXEC_TEASE": "soft",
    "OTHER": "soft",
}
CLASSES = ["infra", "client", "report", "soft"]
RESOLVE_DAYS = 120


class SignalModel:
    def __init__(self, sig: pd.DataFrame, rel: pd.DataFrame, asof, era_days=365,
                 rho=0.5, cap=5.0, lambda_floor=0.01, q_discount=0.85, recent=False, same_day=False,
                 split_first_party=False):
        self.asof = d(asof)
        # split_first_party: Anthropic's own surfaces (docs, model pages, pricing,
        # system-card URLs) get their own class instead of sharing "infra" with
        # third-party cloud catalogs, so they carry their own lead time and
        # detection rate and are not masked by a catalog row in the same class.
        self.classes = CLASSES + (["first_party"] if split_first_party else [])
        # v3d options. recent: the clock for each class runs from the most recent
        # grade A/B sighting (lead times are then estimated the same way), so a
        # fresh first-party artifact is not masked by an older one in the same
        # class. same_day: live runs also see sightings first seen on the run date
        # (backtests keep the strict "before the origin" rule).
        self.recent = recent
        self.cut = self.asof + pd.Timedelta(days=1) if same_day else self.asof
        self.rho, self.cap = rho, cap
        s = sig.copy()
        s["cls"] = s.signal_code.map(CLASS_OF).fillna("soft")
        if split_first_party:
            s.loc[s.signal_code == "FIRST_PARTY_DOC", "cls"] = "first_party"
        self.sig = s
        known = s[s.first_seen < self.cut]
        # resolved as of origin: true signals whose release already happened,
        # false signals older than RESOLVE_DAYS
        tp = known[(known.is_false == 0) & (known.release_date < self.asof)]
        fp = known[(known.is_false == 1) & (known.first_seen < self.asof - pd.Timedelta(days=RESOLVE_DAYS))]
        rel_known = rel[(rel.date < self.asof) & (rel.date >= self.asof - pd.Timedelta(days=era_days))
                        & (rel.family != "legacy")]
        n_rel = max(len(rel_known), 1)
        fam_days = era_days * 4.0  # ~4 active family groups over the era
        all_leads = np.log1p(tp.lead_days.clip(lower=0).values) if len(tp) else np.array([np.log(8.0)])
        g_mu, g_sd = float(np.mean(all_leads)), float(max(np.std(all_leads), 0.6))
        self.par = {}
        for c in self.classes:
            tpc = tp[tp.cls == c]
            # earliest sighting per release for this class
            if self.recent:
                # latest A/B sighting before the release (falls back to C when that is all there is)
                t2 = tpc.assign(_weak=(tpc.grade.astype(str) == "C").astype(int))
                first = t2.sort_values(["_weak", "first_seen"], ascending=[True, False]).drop_duplicates("release_id")
                first = first.assign(lead_days=(first.release_date - first.first_seen).dt.days)
            else:
                first = tpc.sort_values("first_seen").drop_duplicates("release_id")
            detected = first[first.release_id.isin(rel_known.release_id)]
            q = (len(detected) + 0.5) / (n_rel + 1.0) * q_discount
            leads = np.log1p(first.lead_days.clip(lower=0).values)
            k = 3.0
            n = len(leads)
            mu = (leads.sum() + k * g_mu) / (n + k) if n else g_mu
            var = ((((leads - mu) ** 2).sum() if n else 0) + k * g_sd ** 2) / (n + k)
            fpc = fp[(fp.cls == c) & (fp.first_seen >= self.asof - pd.Timedelta(days=era_days + RESOLVE_DAYS))]
            lam = max((len(fpc) + 0.5) / fam_days, lambda_floor)
            self.par[c] = dict(q=float(min(q, 0.95)), mu=float(mu), sd=float(np.sqrt(var)), lam=float(lam),
                               n_tp=int(n), n_fp=int(len(fpc)))

    def _lead_pdf(self, c, lead):
        p = self.par[c]
        lead = np.asarray(lead, dtype=float)
        x = np.log1p(np.maximum(lead, 0))
        pdf = stats.norm.pdf(x, p["mu"], p["sd"]) / (1 + np.maximum(lead, 0))
        return np.where(lead >= 0, pdf, 0.0)

    def _lead_sf(self, c, lead):
        p = self.par[c]
        return stats.norm.sf(np.log1p(np.maximum(lead, 0)), p["mu"], p["sd"])

    def visible(self, family, last_release):
        s = self.sig
        v = s[(s.family == family) & (s.first_seen < self.cut) & (s.first_seen > d(last_release))]
        # a sighting stops counting once its own target has shipped
        v = v[~((v.is_false == 0) & (v.release_date < self.asof))]
        # earliest sighting per class, preferring grade A/B artifacts over C-grade claims
        v = v.assign(_weak=(v.grade.astype(str) == "C").astype(int))
        return v.sort_values(["_weak", "first_seen"], ascending=[True, not self.recent]).drop_duplicates("cls").drop(columns="_weak")

    def likelihood(self, family, last_release, H, use_absence=True):
        j = np.arange(H, dtype=float)
        since_last = (self.asof - d(last_release)).days
        vis = self.visible(family, last_release)
        logL = np.zeros(H)
        log_tail = 0.0
        detail = []
        for c in self.classes:
            p = self.par[c]
            row = vis[vis.cls == c]
            if len(row):
                s0 = (self.asof - row.first_seen.iloc[0]).days  # days since first sighting
                L = p["q"] * self._lead_pdf(c, j + s0) + p["lam"]
                L_far = p["lam"] + p["q"] * self._lead_pdf(c, H + s0)
                kind = "observed"
            elif use_absence:
                L = 1 - p["q"] * (self._lead_sf(c, j) - self._lead_sf(c, j + since_last))
                L_far = 1 - p["q"] * (self._lead_sf(c, H) - self._lead_sf(c, H + since_last))
                kind = "absent"
            else:
                continue
            ratio = np.clip(L / L_far, 1 / self.cap, self.cap)
            logL += (1 - self.rho) * np.log(ratio)
            detail.append(dict(cls=c, kind=kind, peak_ratio=float(ratio.max()), min_ratio=float(ratio.min()),
                               first_seen=str(row.first_seen.iloc[0].date()) if len(row) else None))
        return np.exp(logL), 1.0, detail

    @staticmethod
    def update(pmf, tail, L, L_tail):
        post = pmf * L
        t = tail * L_tail
        Z = post.sum() + t
        return post / Z, float(t / Z)
