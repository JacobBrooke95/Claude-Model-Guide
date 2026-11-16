#!/usr/bin/env python3
"""Canonical data layer.

Reads capability/data/raw/*.csv plus the repo's data/models.json and
data/benchmarks.json and writes four tidy tables to capability/data/:

  models.csv            one row per model (lab, family, dates, version type)
  index_values.csv      index values by scale and fit (public ECI; AECI by card fit)
  benchmark_scores.csv  one row per (benchmark, model) in the comparable configuration
  benchmarks_meta.csv   bounds, link type and configuration note per benchmark
  build_log.csv         every rename, merge, conflict and dropped row

Nothing is interpolated or imputed here. A row that cannot be matched to a model is
dropped and logged, never guessed.
"""
from __future__ import annotations
import gzip
import json
import re
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
from capmodel.common import RAW, DATA, REPO, AS_OF  # noqa: E402

LOG: list[dict] = []


def log(step, item, action, reason=""):
    LOG.append({"step": step, "item": str(item), "action": action, "reason": reason})


# ---- explicit name tables (no fuzzy guesses beyond the normaliser below) ------------
REPO_TO_EPOCH = {  # repo models.json name -> Epoch ECI name, where they differ
    "Claude 3.5 Sonnet (new)": "Claude 3.5 Sonnet (October 2024)",
}
AECI_NAME = {  # aeci_all.csv short name -> canonical id
    "3 Opus": "Claude 3 Opus", "3.5 Sonnet": "Claude 3.5 Sonnet",
    "3.5 Sonnet (new)": "Claude 3.5 Sonnet (October 2024)", "3.7 Sonnet": "Claude 3.7 Sonnet",
    "GPT-5": "GPT-5", "Internal Model (unreleased)": "Anthropic internal model (unreleased)",
}
AECI_FIT = {  # fit_card -> (fit id, order)
    "Opus 4.8 card": ("opus4.8", 1), "Mythos 5 card": ("fable5", 2), "Opus 5 card": ("opus5", 3),
    "Mythos 5.1 card": ("fable5.1", 4), "Opus 5.5 card": ("opus5.5", 5),
    "Sonnet 5.5 card": ("sonnet5.5", 6), "Haiku 5.5 card": ("haiku5.5", 7),
    "Mythos 5.2 card": ("fable5.2", 8),
}
METR_NAME = {
    "gpt_4": "GPT-4 (Mar 2023)", "gpt_4_1106": "GPT-4 Turbo (Nov 2023)", "claude_3_opus": "Claude 3 Opus",
    "gpt_4_turbo": "GPT-4 Turbo (Apr 2024)", "gpt_4o": "GPT-4o (May 2024)",
    "claude_3_5_sonnet_20240620": "Claude 3.5 Sonnet", "o1_preview": "o1-preview",
    "claude_3_5_sonnet_20241022": "Claude 3.5 Sonnet (October 2024)", "o1": "o1",
    "claude_3_7_sonnet": "Claude 3.7 Sonnet", "o3": "o3", "claude_4_opus": "Claude Opus 4",
    "claude_4_1_opus": "Claude Opus 4.1", "gpt_5_2025_08_07": "GPT-5", "gemini_3_pro": "Gemini 3 Pro",
    "gpt_5_1_codex_max": "GPT-5.1-Codex-Max", "claude_opus_4_5": "Claude Opus 4.5", "gpt_5_2": "GPT-5.2",
    "claude_opus_4_6": "Claude Opus 4.6", "gpt_5_3_codex": "GPT-5.3 Codex",
    "gemini_3_1_pro": "Gemini 3.1 Pro", "gpt_5_4": "GPT-5.4",
    "claude_mythos_preview_early": "Claude Mythos Preview",
}

_ORG = re.compile(r"^[a-z0-9\-_.]+/")
_PAREN = re.compile(r"\s*\(([^)]*)\)")
_DATE8 = re.compile(r"[-_ ]?(20\d{6})$")
_CLAUDE_SWAP = re.compile(r"^claude (\d[\d.]*) (haiku|sonnet|opus)$")
# a parenthesised suffix may be dropped only if it is purely a run configuration, never a version or date
_CONFIG_WORDS = {"high", "max", "xhigh", "low", "medium", "minimal", "none", "reasoning", "thinking", "non", "nonreasoning",
                 "default", "fallback", "adaptive", "32k", "64k", "16k", "128k", "effort", "extended"}
ALIASES = {   # explicit, checked by hand: board/API names of models whose plain name is shared by two versions
    "claude-3-5-sonnet-20241022": "Claude 3.5 Sonnet (October 2024)", "claude-3-5-sonnet-20240620": "Claude 3.5 Sonnet",
    "Claude 3.5 Sonnet (20241022)": "Claude 3.5 Sonnet (October 2024)", "Claude 3.5 Sonnet (Oct '24)": "Claude 3.5 Sonnet (October 2024)",
    "Claude 3.5 Sonnet (Oct)": "Claude 3.5 Sonnet (October 2024)", "Claude 3.5 Sonnet (20240620)": "Claude 3.5 Sonnet",
    "Claude 3.5 Sonnet (June '24)": "Claude 3.5 Sonnet",
}
MATCH_LOG: dict = {}


def _n(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def _config_only(inner: str) -> bool:
    toks = [t for t in re.split(r"[^a-z0-9]+", inner.lower()) if t]
    return bool(toks) and all(t in _CONFIG_WORDS for t in toks)


def make_matcher(canon: list[str]):
    """Return f(name) -> canonical id or None. In order: explicit alias; exact normalised
    match; org prefix stripped; a trailing parenthesis dropped ONLY if it holds nothing but
    run-configuration words (effort, thinking, fallback); a trailing 8-digit API date
    dropped ONLY if exactly one canonical model has that base name (dated variants such as
    'Mistral Large 2411' or 'DeepSeek-R1 (0528)' therefore never merge into a sibling);
    'Claude 4.5 Haiku' -> 'Claude Haiku 4.5'. Every non-exact match is recorded in MATCH_LOG."""
    table = {_n(c): c for c in canon}
    # base names that are ambiguous because several canonical models extend them with a version/date
    stems = {}
    for c in canon:
        stems.setdefault(_n(_PAREN.sub("", c)), []).append(c)

    def unique_base(key):
        return key in table and len(stems.get(key, [])) <= 1

    def f(name):
        if not isinstance(name, str):
            return None
        raw = name.strip()
        if raw in ALIASES:
            MATCH_LOG[raw] = (ALIASES[raw], "alias")
            return ALIASES[raw]
        if _n(raw) in table:
            return table[_n(raw)]
        s = _ORG.sub("", raw)
        if s in ALIASES:
            MATCH_LOG[raw] = (ALIASES[s], "alias")
            return ALIASES[s]
        steps = [("org prefix stripped", s)]
        m = _PAREN.search(s)
        s2 = s
        if m and s.endswith(")") and _config_only(m.group(1)):
            s2 = s[:m.start()].strip()
            steps.append(("config suffix dropped", s2))
        d8 = _DATE8.search(s2)
        s3 = s2
        if d8:
            s3 = s2[:d8.start()].strip()
            steps.append(("api date dropped", s3))
        for how, cand in steps:
            cands = [cand, re.sub(r"[-_]", " ", cand)]
            mm = _CLAUDE_SWAP.match(cands[1].lower())
            if mm:
                cands.append(f"claude {mm.group(2)} {mm.group(1)}")
            m2 = re.match(r"^claude[- ](opus|sonnet|haiku|fable|mythos)[- ](\d)[- .](\d)$", cand.lower())
            if m2:
                cands.append(f"claude {m2.group(1)} {m2.group(2)}.{m2.group(3)}")
            m3 = re.match(r"^claude[- ](\d)[- .](\d)[- ](opus|sonnet|haiku)$", cand.lower())
            if m3:
                cands.append(f"claude {m3.group(1)}.{m3.group(2)} {m3.group(3)}")
            for c in cands:
                k = _n(c)
                if k in table and (how != "api date dropped" or unique_base(k)) and (how == "org prefix stripped" or unique_base(k)):
                    MATCH_LOG[raw] = (table[k], how)
                    return table[k]
        return None
    return f


def version_type(prev_gen, gen, version) -> str:
    """'gen' = first release of a new generation in its family; 'half' = x.5; else 'minor'."""
    if prev_gen is None or gen > prev_gen:
        return "gen"
    return "half" if abs(version * 10 % 10 - 5) < 1e-6 else "minor"


def build_models():
    e = pd.read_csv(RAW / "eci_public.csv")
    rel = json.loads((REPO / "data" / "models.json").read_text())["releases"]
    internal = pd.read_csv(RAW / "aeci_internal_dates.csv")
    rows = {}
    for _, r in e.iterrows():
        rows[r.model] = dict(
            model_id=r.model, lab=r.organization, family=None, version=None, generation=None,
            version_type=None, access=r.accessibility, release_date=r.release_date,
            release_date_epoch=r.release_date, release_date_repo=None, internal_date=None,
            in_public_eci=1, eci=r.eci, eci_lo90=r.ci90_low, eci_hi90=r.ci90_high,
            n_benchmarks_eci=r.n_benchmarks_in_fit, is_anchor=int(r.is_anchor), twin=None,
            status=r.status)
    prev_gen = {}
    for r in rel:
        mid = REPO_TO_EPOCH.get(r["model"], r["model"])
        if mid != r["model"]:
            log("models", r["model"], "renamed", f"-> Epoch name '{mid}'")
        fam = r["family"]
        vt = version_type(prev_gen.get(fam), r["generation"], float(r["version"])) if fam != "legacy" else None
        prev_gen[fam] = r["generation"]
        if mid in rows:
            d = rows[mid]
            if d["release_date_epoch"] != r["date"]:
                log("models", mid, "date_conflict",
                    f"Epoch {d['release_date_epoch']} vs repo {r['date']}; repo date used (first public availability)")
            d.update(release_date=r["date"], release_date_repo=r["date"])
        else:
            rows[mid] = dict(
                model_id=mid, lab="Anthropic", family=None, version=None, generation=None,
                version_type=None, access=r.get("access"), release_date=r["date"], release_date_epoch=None,
                release_date_repo=r["date"], internal_date=None, in_public_eci=0, eci=None, eci_lo90=None,
                eci_hi90=None, n_benchmarks_eci=None, is_anchor=0, twin=None, status="REPO")
            log("models", mid, "added_from_repo", "Claude release with no public ECI row")
        rows[mid].update(family=fam, version=float(r["version"]), generation=r["generation"],
                         version_type=vt, access=r.get("access") or rows[mid]["access"])
    # Anthropic models in Epoch that the repo does not list
    for mid, d in rows.items():
        if d["lab"] == "Anthropic" and d["family"] is None:
            d["family"] = "legacy"
            log("models", mid, "family_legacy", "in Epoch ECI, not in repo models.json")
    # Fable <-> Mythos twins (same underlying model per Anthropic; restricted vs general access)
    for r in rel:
        if r["family"] == "mythos":
            tw = [x for x in rel if x["family"] == "fable" and x["date"] == r["date"]]
            if tw:
                rows[r["model"]]["twin"] = tw[0]["model"]
                rows[tw[0]["model"]]["twin"] = r["model"]
    # internal dates (figure reads)
    canon = list(rows)
    match = make_matcher(canon)
    for _, r in internal.iterrows():
        mid = REPO_TO_EPOCH.get(r.model, r.model)
        if mid in rows:
            rows[mid]["internal_date"] = r.internal_date_figure_read
        else:
            log("models", r.model, "internal_date_unmatched", "no model row (unreleased internal model)")
    m = pd.DataFrame(rows.values()).sort_values(["release_date", "model_id"]).reset_index(drop=True)
    assert m.model_id.is_unique
    return m


def build_index(models):
    e = pd.read_csv(RAW / "eci_public.csv")
    out = []
    for _, r in e.iterrows():
        out.append(dict(model_id=r.model, scale="eci_public", fit="epoch_bayes_2026-11", fit_order=0,
                        fit_date=r.as_of, value=r.eci, lo=r.ci90_low, hi=r.ci90_high, ci_level=0.90,
                        ci_kind="credible", local_lo=None, local_hi=None, value_type="published",
                        own_card=None, n_benchmarks=r.n_benchmarks_in_fit, status=r.status))
    a = pd.read_csv(RAW / "aeci_all.csv")
    ids = set(models.model_id) | {"Anthropic internal model (unreleased)"}
    for _, r in a.iterrows():
        mid = AECI_NAME.get(r.model, "Claude " + r.model)
        if mid not in ids:
            log("index", r.model, "dropped", "AECI row with no model match")
            continue
        card = r.fit_card
        if card.startswith("all cards"):
            fit, order = "anchor", 99
        elif "rescaled by repo" in card:
            fit, order = "fable5.2_repo_rescaled", 98
        else:
            fit, order = AECI_FIT[card]
        out.append(dict(model_id=mid, scale="aeci", fit=fit, fit_order=order,
                        fit_date=r.fit_date if isinstance(r.fit_date, str) else r.card_date,
                        value=r.value, lo=r.ci95_global_lo, hi=r.ci95_global_hi, ci_level=0.95,
                        ci_kind="global", local_lo=r.ci95_local_lo, local_hi=r.ci95_local_hi,
                        value_type=r.value_type, own_card=int(r.own_card), n_benchmarks=r.n_benchmarks_model,
                        status=r.status))
    return pd.DataFrame(out)


def extract_draws(models):
    """Epoch's 500 joint posterior draws per model -> data/raw/eci_posterior_draws.csv.gz.
    The source JSON sits in downloads/ (not committed); the extract is committed so the
    pipeline regenerates without it."""
    dst = RAW / "eci_posterior_draws.csv.gz"
    src = RAW / "downloads/epoch/benchmark_data/epoch_capabilities_index/eci_bootstraps.json"
    if src.exists():
        b = json.loads(src.read_text())
        names = b["model"]["names"]
        s = np.asarray(b["model"]["capability_samples"], float)  # 500 x 256
        df = pd.DataFrame(np.round(s.T, 3), index=names, columns=[f"d{i}" for i in range(s.shape[0])])
        df.index.name = "model_id"
        new = df.to_csv().encode()
        old = gzip.decompress(dst.read_bytes()) if dst.exists() else b""
        if new != old:
            with gzip.GzipFile(dst, "wb", mtime=0) as f:
                f.write(new)
    d = pd.read_csv(dst, index_col=0)
    missing = set(models[models.in_public_eci == 1].model_id) - set(d.index)
    assert not missing, missing
    return d


# ---- benchmarks ---------------------------------------------------------------------
META = [
    # key, title, kind, lo, hi, unit, group, source, configuration
    ("swe_bench_pro", "SWE-bench Pro", "bounded", 0, 100, "% pass", "site", "site",
     "Anthropic system cards, mean of five trials (first-party)"),
    ("terminal_bench_2_1", "Terminal-Bench 2.1", "bounded", 0, 100, "% completion", "site", "site",
     "Vals AI harness snapshot"),
    ("osworld", "OSWorld", "bounded", 0, 100, "% of tasks", "site", "site",
     "Anthropic-reported; three eval versions on one series (original, Verified, 2.1 partial credit)"),
    ("gdpval_aa", "GDPval-AA v2.1", "elo", None, None, "Elo", "site", "site+aa",
     "Artificial Analysis v2.1, strongest (max-effort) config per release"),
    ("rli", "Remote Labor Index", "bounded", 0, 100, "% of 240 projects", "site", "site+hub",
     "Scale AI / CAIS leaderboard; Fable 5.2 Anthropic-reported"),
    ("arc_agi_2", "ARC-AGI-2", "bounded", 0, 100, "%", "site", "site+hub",
     "ARC Prize leaderboard, strongest listed config per model"),
    ("arc_agi_3", "ARC-AGI-3", "bounded", 0, 100, "%", "site", "site",
     "ARC Prize verified, Standard harness, mixed efforts"),
    ("hle", "Humanity's Last Exam (no tools)", "bounded", 0, 100, "% of 2,500", "site", "site",
     "Anthropic system cards, no-tools, max effort / adaptive thinking (first-party)"),
    ("forecastbench", "ForecastBench (baseline)", "linear", 0, 100, "Brier Index", "site", "site",
     "ForecastBench baseline board, best config per model; prompt set-ups differ by model"),
    ("vending_bench_2", "Vending-Bench 2", "linear", None, None, "USD", "site", "site+hub",
     "Andon Labs leaderboard, mean final balance"),
    ("metr_h50", "METR 50% time horizon (TH1.1)", "loghorizon", None, None, "minutes", "other", "metr",
     "METR-Horizon-v1.1 YAML; coverage ends with Mythos Preview (May 2026)"),
    ("gpqa_diamond", "GPQA Diamond", "bounded", 25, 97, "%", "other", "hub",
     "Epoch hub, best score across configs; chance 25%, ceiling 97% per Epoch"),
    ("frontiermath_t13", "FrontierMath Tiers 1-3", "bounded", 0, 95, "%", "other", "hub",
     "Epoch hub (v2 private set), best config; ceiling 95% per Epoch"),
    ("terminal_bench_2", "Terminal-Bench 2.0", "bounded", 0, 100, "%", "other", "hub",
     "Epoch hub 'Terminal Bench', best accuracy per model; coverage ends April 2026"),
    ("webdev_arena", "WebDev Arena", "elo", None, None, "Arena score", "other", "hub",
     "Epoch hub copy of LMArena WebDev scores, best per model"),
    ("lmarena_text", "LMArena text", "elo", None, None, "Arena score", "other", "lmarena",
     "LMArena text 'overall', latest snapshot per model (style-controlled era)"),
    ("aa_index", "AA Intelligence Index v5", "bounded", 0, 100, "index", "other", "aa",
     "Artificial Analysis v5.0.1, strongest config per release"),
    ("vals_index", "Vals Index v2.2", "bounded", 0, 100, "% accuracy", "other", "vals",
     "Vals Index v2.2 overall, best config per model"),
]
HUB = {  # key -> (hub benchmark name, multiplier to native units)
    "rli": ("Remote Labor Index", 100.0), "arc_agi_2": ("ARC-AGI-2", 100.0),
    "vending_bench_2": ("vending_bench_2 (file; no metadata row)", 1.0),
    "gpqa_diamond": ("GPQA diamond", 100.0),
    "frontiermath_t13": ("FrontierMath-Tiers-1-3-v2-Private", 100.0),
    "terminal_bench_2": ("Terminal Bench", 100.0),
    "webdev_arena": ("webdev_arena (file; no metadata row)", 1.0),
}


def build_benchmarks(models):
    canon = list(models.model_id)
    match = make_matcher(canon)
    by_fd = {(r.family, r.release_date_repo): r.model_id for r in models.itertuples() if r.release_date_repo}
    rows = []

    def add(key, mid, value, source, config="", status="VERIFIED"):
        rows.append(dict(benchmark=key, model_id=mid, value=float(value), source=source, config=config,
                         status=status))

    # 1. the site's charted series (the comparable configuration, with provenance in benchmarks.json)
    charts = json.loads((REPO / "data" / "benchmarks.json").read_text())["charts"]
    for key in ["swe_bench_pro", "terminal_bench_2_1", "osworld", "gdpval_aa", "rli", "arc_agi_2",
                "arc_agi_3", "hle", "forecastbench", "vending_bench_2"]:
        for fam, pts in charts[key]["series"].items():
            for p in pts:
                mid = by_fd.get((fam, p["date"]))
                if mid is None:
                    log("bench:" + key, f"{fam}/{p.get('model')}/{p['date']}", "dropped", "no models.json release on that family+date")
                    continue
                cfg = p.get("config", "")
                if p.get("v21"):
                    cfg = "OSWorld 2.1 partial credit"
                if p.get("reported_by"):
                    cfg = (cfg + " reported_by=" + p["reported_by"]).strip()
                add(key, mid, p["score"], "site", cfg)
    have = {(r["benchmark"], r["model_id"]) for r in rows}

    def add_best(key, df, name_col, val_col, source, mult=1.0, cfg=""):
        df = df[df[val_col].notna()]
        n_un, un = 0, []
        best = {}
        for name, v in zip(df[name_col], df[val_col]):
            mid = None
            for part in str(name).split(","):   # 'Claude Fable 5.2,Claude Mythos 5.2'
                mid = match(part.strip())
                if mid:
                    break
            if mid is None:
                n_un += 1
                un.append(str(name))
                continue
            if models.loc[models.model_id == mid, "in_public_eci"].iloc[0] == 0 and key != "metr_h50":
                tw = models.loc[models.model_id == mid, "twin"].iloc[0]
                mid = tw if isinstance(tw, str) else mid
            best[mid] = max(best.get(mid, -np.inf), float(v) * mult)
        k = 0
        for mid, v in best.items():
            if (key, mid) in have:
                continue
            add(key, mid, v, source, cfg)
            k += 1
        log("bench:" + key, source, "merged", f"{k} models added; {len(set(un))} distinct names unmatched to any model row "
            f"(not in public ECI): e.g. {sorted(set(un))[:6]}")

    hub = pd.read_csv(RAW / "epoch_hub_benchmarks_long.csv", low_memory=False)
    for key, (bn, mult) in HUB.items():
        add_best(key, hub[hub.benchmark == bn], "model_group", "value", "hub", mult, "best config per model")
    g = pd.read_csv(RAW / "aa_elo_gdpval_briefcase.csv")
    add_best("gdpval_aa", g[g.benchmark == "GDPval-AA"], "release", "elo", "aa", 1.0, "max over configs")
    aa = pd.read_csv(RAW / "aa_index.csv")
    aa = aa[(aa.index_name == "AA Intelligence Index") & (aa.index_version == "v5.0.1")]
    add_best("aa_index", aa, "release", "value", "aa", 1.0, "max over configs")
    v = pd.read_csv(RAW / "vals_index.csv")
    v = v[(v["index"] == "Vals Index") & (v.index_version.astype(str) == "2.2") & (v.task_key == "overall")]
    add_best("vals_index", v, "model_key", "accuracy_pct", "vals", 1.0, "best config")
    lm = pd.read_csv(RAW / "lmarena_text.csv", low_memory=False)
    lm = lm[(lm.category == "overall") & (lm.leaderboard_publish_date >= "2025-07-23")]
    lm = lm.sort_values("leaderboard_publish_date").groupby("model_name").tail(1)
    add_best("lmarena_text", lm, "model_name", "rating", "lmarena", 1.0, "last snapshot the model appears in")
    # METR TH1.1 only; flagged non-comparable rows are excluded by suite string
    mh = pd.read_csv(RAW / "metr_horizons.csv")
    mh = mh[mh.suite_version.astype(str).str.startswith("TH1.1 (METR-Horizon-v1.1")]
    mh = mh[mh.release_date >= "2023-01-01"]
    for r in mh.itertuples():
        mid = METR_NAME.get(r.model)
        try:
            val = float(r.horizon_50_minutes)
        except (TypeError, ValueError):
            log("bench:metr_h50", r.model, "dropped", "non-numeric horizon")
            continue
        if mid is None or mid not in set(canon):
            log("bench:metr_h50", r.model, "dropped", "no model match")
            continue
        add("metr_h50", mid, val, "metr", "TH1.1 50% horizon")
    b = pd.DataFrame(rows).merge(
        models[["model_id", "lab", "family", "release_date", "eci"]], on="model_id", how="left")
    dup = b.duplicated(["benchmark", "model_id"])
    assert not dup.any(), b[dup]
    meta = pd.DataFrame(META, columns=["benchmark", "title", "kind", "lo", "hi", "unit", "group", "source",
                                       "configuration"])
    cnt = b.groupby("benchmark").agg(n=("value", "size"), n_with_eci=("eci", "count"),
                                     n_claude=("lab", lambda s: int((s == "Anthropic").sum())))
    meta = meta.merge(cnt, left_on="benchmark", right_index=True, how="left")
    return b.sort_values(["benchmark", "release_date", "model_id"]).reset_index(drop=True), meta


def main(verbose=True):
    LOG.clear()
    MATCH_LOG.clear()
    models = build_models()
    draws = extract_draws(models)
    index = build_index(models)
    bench, meta = build_benchmarks(models)
    DATA.mkdir(exist_ok=True)
    models.to_csv(DATA / "models.csv", index=False)
    index.to_csv(DATA / "index_values.csv", index=False)
    bench.to_csv(DATA / "benchmark_scores.csv", index=False)
    meta.to_csv(DATA / "benchmarks_meta.csv", index=False)
    for raw, (mid, how) in sorted(MATCH_LOG.items()):
        log("name_match", raw, "merged", f"-> '{mid}' ({how})")
    pd.DataFrame(LOG).to_csv(DATA / "build_log.csv", index=False)
    if verbose:
        print(f"[data] models {len(models)} ({int((models.lab == 'Anthropic').sum())} Anthropic), "
              f"index rows {len(index)}, benchmark rows {len(bench)}, draws {draws.shape}, log {len(LOG)}")
        print(meta[["benchmark", "kind", "n", "n_with_eci", "n_claude"]].to_string(index=False))
    return models, index, bench, meta, draws


if __name__ == "__main__":
    main()
