"""Forward scorecard → output/scorecard.json and SCORECARD.md.

    python3 tools/scorecard.py [AS_OF]

Rebuilt from scratch on every run from forecast_log.csv, history/ and the
release table; nothing here is hand-edited. It answers one question: on
forecasts frozen before the outcome, is the model beating the market, the old
EWMA model and the base rate?

Why this is not just "mean Brier over log rows"
-----------------------------------------------
Daily snapshots of the same question are almost the same forecast, and every
checkpoint of a family resolves on the same release. Counting rows would make
one release look like a hundred tests. So scores are averaged in three steps:

  1. week      forecasts of one question (target × checkpoint) made in the
               same ISO week are averaged into one number
  2. question  the weekly numbers of a question are averaged
  3. block     the questions of one family within one inter-release interval
               (from the family's last release before the forecast to its
               next) are averaged; Fable and Mythos share a block because
               they ship together

The headline is the mean over blocks, and n_blocks is the sample size to
quote. A block is one release cycle of one family, the same unit the backtest
uses for its significance tests (score_final.py).

Primary set: per-family targets, checkpoint at most 92 days after the
forecast. Longer-dated rows are reported separately; "Fable by May 2027" asked
in November could hardly fail and says nothing about skill.

Baselines, each on the rows where it exists:
  market   p_market in the log (Polymarket ladder rung for that checkpoint)
  ewma     the site's EWMA model as of the day before the origin (Opus, Sonnet, Haiku)
  clim     base rate: share of past windows of that length that held a release

Voice-model questions (voice.py; voice_forecast_log.csv, graded against
data/voice_resolutions.json) are scored in a section of their own, as one
block, and enter none of the family numbers above.
"""
from __future__ import annotations

import glob
import json
import os
import sys

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, ROOT)
os.chdir(ROOT)

from engine import backtest as bt          # noqa: E402
from engine.ewma import ewma_pmf           # noqa: E402
from engine.market import pool             # noqa: E402

FAMS = ["fable", "opus", "sonnet", "haiku", "mythos"]
PRIMARY_MAX_LEAD = 92
BUCKETS = [(0, .1), (.1, .3), (.3, .7), (.7, .9), (.9, 1.0001)]
MIN_BLOCKS_FOR_CLAIMS = 8


def brier(p, y):
    return (p - y) ** 2


def logloss(p, y):
    p = np.clip(p, 1e-4, 1 - 1e-4)
    return -(y * np.log(p) + (1 - y) * np.log(1 - p))


def load_rows(as_of):
    rel = pd.read_csv("data/anthropic_releases.csv", parse_dates=["date"])
    log = pd.read_csv("forecast_log.csv", parse_dates=["as_of", "checkpoint"])
    log = log.drop_duplicates(["as_of", "model_version", "target", "checkpoint"])
    log = log[log.target.isin(FAMS)].copy()
    today = pd.Timestamp(as_of)
    out = []
    ew_cache = {}
    for _, q in log.iterrows():
        fam_dates = rel[rel.family == q.target].date
        nxt = fam_dates[fam_dates >= q.as_of]
        hit = (nxt <= q.checkpoint).any()
        if hit:
            y = 1
        elif q.checkpoint < today:
            y = 0
        else:
            continue
        prev = fam_dates[fam_dates < q.as_of]
        # Fable and Mythos ship together (one clock in the engine), so they share a block
        clock = "fable+mythos" if q.target in ("fable", "mythos") else q.target
        block = f"{clock}, after {prev.max().date() if len(prev) else 'start'}"
        lead = (q.checkpoint - q.as_of).days
        h = lead + 1   # "by checkpoint" includes the checkpoint day
        row = dict(as_of=q.as_of, version=q.model_version, target=q.target, checkpoint=q.checkpoint, y=y, lead=lead,
                   block=block, week=f"{q.as_of.isocalendar().year}-W{q.as_of.isocalendar().week:02d}",
                   p_model=float(q.p_model), p_market=(np.nan if pd.isna(q.p_market) else float(q.p_market)),
                   p_clim=float(bt.climatology(rel, q.target, q.as_of, h)), p_ewma=np.nan)
        if q.target in ("opus", "sonnet", "haiku"):
            k = str(q.as_of.date())
            if k not in ew_cache:
                ew_cache[k] = bt.ewma_baseline(q.as_of)
            e = ewma_pmf(ew_cache[k].get(q.target), q.as_of, 400)
            if e is not None and h <= 400:
                row["p_ewma"] = float(np.sum(e[0][:h]))
        out.append(row)
    return pd.DataFrame(out), rel


def clustered(df, col, loss=brier):
    """week → question → block mean of the loss of column `col`. Returns (mean over blocks, per-block series)."""
    d = df.dropna(subset=[col])
    if d.empty:
        return None, pd.Series(dtype=float)
    d = d.assign(L=loss(d[col].values.astype(float), d.y.values))
    w = d.groupby(["block", "target", "checkpoint", "week"]).L.mean()
    q = w.groupby(level=["block", "target", "checkpoint"]).mean()
    b = q.groupby(level="block").mean()
    return float(b.mean()), b


def versus(df, base):
    """Model against one baseline on the rows where the baseline exists."""
    d = df.dropna(subset=[base])
    if d.empty:
        return None
    m, mb = clustered(d, "p_model")
    o, ob = clustered(d, base)
    ml, _ = clustered(d, "p_model", logloss)
    ol, _ = clustered(d, base, logloss)
    diff = (mb - ob)
    return dict(n_rows=int(len(d)), n_questions=int(d.groupby(["target", "checkpoint"]).ngroups), n_blocks=int(len(mb)),
                brier_model=m, brier_baseline=o, logloss_model=ml, logloss_baseline=ol,
                blocks_model_better=int((diff < 0).sum()), blocks_baseline_better=int((diff > 0).sum()),
                per_block={k: dict(model=float(mb[k]), baseline=float(ob[k])) for k in mb.index},
                raw_row_brier_model=float(brier(d.p_model, d.y).mean()), raw_row_brier_baseline=float(brier(d[base], d.y).mean()))


def calibration(df):
    rows = []
    for lo, hi in BUCKETS:
        d = df[(df.p_model >= lo) & (df.p_model < hi)]
        if d.empty:
            continue
        # one number per block first, so a cycle with many snapshots does not dominate
        b = d.groupby("block").agg(p=("p_model", "mean"), y=("y", "mean"))
        rows.append(dict(bucket=f"{lo:.0%}–{min(hi, 1):.0%}", n_rows=int(len(d)), n_blocks=int(len(b)),
                         mean_p=float(b.p.mean()), observed=float(b.y.mean())))
    return rows


def name_calls(rel):
    """For each release since the forward log began: what the frozen snapshots
    of that cycle gave the name that shipped."""
    snaps = [json.load(open(p)) for p in sorted(glob.glob("history/forecast_*.json"))]
    out = []
    if not snaps:
        return out
    first = pd.Timestamp(min(s["as_of"] for s in snaps))
    for _, r in rel[(rel.date >= first) & rel.family.isin(FAMS)].iterrows():
        prev = rel[(rel.family == r.family) & (rel.date < r.date)].date.max()
        ps, tops = [], []
        for s in snaps:
            a = pd.Timestamp(s["as_of"])
            if not (a <= r.date and (pd.isna(prev) or a > prev)):
                continue
            names = s.get("params", {}).get(r.family, {}).get("names") or {}
            if not names:
                continue
            ps.append(float(names.get(r.model, 0.0)))
            tops.append(max(names, key=names.get))
        if ps:
            top = max(set(tops), key=tops.count)
            out.append(dict(model=r.model, date=str(r.date.date()), n_snapshots=len(ps), mean_p_shipped_name=float(np.mean(ps)),
                            top_call=top, top_call_hit=bool(top == r.model),
                            log_score=float(np.log(max(np.mean(ps), 1e-4)))))
    return out


def voice_block(as_of):
    """Voice-model questions as their own block. A row resolves Yes when its rung has a
    resolution date on or before the checkpoint, No when the checkpoint has passed without
    one. All three rungs hang on the same event, so together they are ONE block."""
    lp, rp = "voice_forecast_log.csv", "data/voice_resolutions.json"
    if not os.path.exists(lp):
        return None
    log = pd.read_csv(lp, parse_dates=["as_of", "checkpoint"]).drop_duplicates(["as_of", "model_version", "target", "checkpoint"])
    res = json.load(open(rp)) if os.path.exists(rp) else {}
    today = pd.Timestamp(as_of)
    rows, n_open = [], 0
    for _, q in log.iterrows():
        rd = (res.get(q.target.split("_")[-1]) or {}).get("resolved_date")
        rd = pd.Timestamp(rd) if rd else None
        if rd is not None and rd < q.as_of:
            continue                                # logged after the rung had resolved: not a forecast
        if rd is not None and rd <= q.checkpoint:
            y = 1
        elif q.checkpoint < today:
            y = 0
        else:
            n_open += 1
            continue
        rows.append(dict(block="voice (first speech model)", target=q.target, checkpoint=q.checkpoint, y=y, version=q.model_version,
                         week=f"{q.as_of.isocalendar().year}-W{q.as_of.isocalendar().week:02d}",
                         p_model=float(q.p_model), p_final=float(q.p_final), p_base=float(q.p_base),
                         p_market=(np.nan if pd.isna(q.p_market) else float(q.p_market))))
    out = dict(n_logged_rows=int(len(log)), n_snapshots=int(log.as_of.nunique()), n_open_rows=int(n_open), n_resolved_rows=len(rows),
               first_checkpoint=str(log.checkpoint.min().date()) if len(log) else None,
               resolutions={k: v.get("resolved_date") for k, v in res.items() if isinstance(v, dict)},
               note="one block; separate from the family headline")
    if rows:
        d = pd.DataFrame(rows)
        out.update(n_blocks=1, n_questions=int(d.groupby(["target", "checkpoint"]).ngroups),
                   brier_model=clustered(d, "p_model")[0], brier_published=clustered(d, "p_final")[0], brier_base_rate=clustered(d, "p_base")[0],
                   logloss_model=clustered(d, "p_model", logloss)[0], vs_market=versus(d, "p_market"),
                   per_rung={t: dict(n_questions=int(g.checkpoint.nunique()), brier_model=clustered(g, "p_model")[0],
                                     brier_base_rate=clustered(g, "p_base")[0]) for t, g in d.groupby("target")})
    return out


def main(as_of):
    df, rel = load_rows(as_of)
    sc = dict(as_of=as_of, generated_by="tools/scorecard.py", primary_max_lead_days=PRIMARY_MAX_LEAD,
              unit="block = one family within one inter-release interval; n_blocks is the sample size",
              min_blocks_for_claims=MIN_BLOCKS_FOR_CLAIMS)
    if df.empty:
        sc["note"] = "no resolved questions yet"
    else:
        prim = df[df.lead <= PRIMARY_MAX_LEAD]
        long = df[df.lead > PRIMARY_MAX_LEAD]
        m, mb = clustered(prim, "p_model")
        ml, _ = clustered(prim, "p_model", logloss)
        sc["primary"] = dict(n_rows=int(len(prim)), n_questions=int(prim.groupby(["target", "checkpoint"]).ngroups),
                             n_blocks=int(len(mb)), brier_model=m, logloss_model=ml,
                             per_block={k: float(v) for k, v in mb.items()},
                             raw_row_brier_model=float(brier(prim.p_model, prim.y).mean()) if len(prim) else None)
        sc["vs_market"] = versus(prim, "p_market")
        sc["vs_ewma"] = versus(prim, "p_ewma")
        sc["vs_climatology"] = versus(prim, "p_clim")
        sc["by_version"] = {v: dict(n_rows=int(len(g)), n_blocks=int(g.block.nunique()), brier_model=clustered(g, "p_model")[0])
                            for v, g in prim.groupby("version")}
        sc["by_lead"] = {}
        for name, lo, hi in (("0-30d", 0, 30), ("31-92d", 31, 92)):
            g = prim[(prim.lead >= lo) & (prim.lead <= hi)]
            if len(g):
                sc["by_lead"][name] = dict(n_rows=int(len(g)), n_blocks=int(g.block.nunique()), brier_model=clustered(g, "p_model")[0],
                                           brier_market=clustered(g, "p_market")[0], brier_clim=clustered(g, "p_clim")[0])
        sc["long_dated"] = dict(n_rows=int(len(long)), n_blocks=int(long.block.nunique()) if len(long) else 0,
                                brier_model=clustered(long, "p_model")[0] if len(long) else None,
                                note="checkpoints more than 92 days out; not part of the headline")
        sc["calibration"] = calibration(prim)
        # what a log-odds blend of model and market would have scored (EXPERIMENTS.md E1); descriptive only
        mk = prim.dropna(subset=["p_market"])
        if len(mk):
            sc["blend_curve"] = {f"w_market={w:.2f}": clustered(mk.assign(p_blend=pool(mk.p_model.values, mk.p_market.values, w)), "p_blend")[0]
                                 for w in (0, .25, .5, .75, .9, 1)}
            sc["blend_curve_n_blocks"] = int(mk.block.nunique())
    sc["name_calls"] = name_calls(rel)
    try:
        v = voice_block(as_of)
        if v:
            sc["voice"] = v
    except Exception as e:      # the voice block must never break the family scorecard
        sc["voice"] = dict(error=f"{type(e).__name__}: {e}")
    gp = "output/grades.json"
    if os.path.exists(gp):
        g = pd.DataFrame(json.load(open(gp)).get("releases", []))
        if len(g):
            sc["release_timing"] = [dict(model=k, n_snapshots=int(len(v)), mean_p_by_release_day=float(v.p_by_date.mean()),
                                         in80_share=float(v.in80.mean()),
                                         mean_median_error_days=(float(v.median_error_days.dropna().mean()) if v.median_error_days.notna().any() else None))
                                    for k, v in g.groupby("model", sort=False)]
    json.dump(sc, open("output/scorecard.json", "w"), indent=1, default=float)
    open("SCORECARD.md", "w").write(render(sc))
    print(headline(sc))
    return sc


def _f(v, fmt=".3f"):
    return "—" if v is None or (isinstance(v, float) and np.isnan(v)) else format(v, fmt)


def headline(sc):
    if "primary" not in sc:
        return f"Scorecard {sc['as_of']}: no resolved questions yet."
    p = sc["primary"]
    s = f"Scorecard {sc['as_of']}: model Brier {_f(p['brier_model'])} over {p['n_blocks']} blocks ({p['n_questions']} questions, {p['n_rows']} rows)"
    for key, lab in (("vs_market", "market"), ("vs_ewma", "EWMA"), ("vs_climatology", "base rate")):
        v = sc.get(key)
        if v:
            s += f"; vs {lab} {_f(v['brier_model'])} / {_f(v['brier_baseline'])} ({v['n_blocks']} blocks)"
    nc = sc.get("name_calls") or []
    if nc:
        s += f"; name calls {sum(x['top_call_hit'] for x in nc)}/{len(nc)}"
    return s + "."


def render(sc):
    L = ["# Forward scorecard", "",
         f"Generated by `tools/scorecard.py` on every run; do not edit by hand. As of {sc['as_of']}.", "",
         "The bar: beat the market baseline on this log. Scores are Brier (lower is better), averaged "
         "week → question → block, where a block is one family within one inter-release interval. "
         "**n blocks is the sample size**, not the number of rows; daily snapshots of one question are one observation. "
         f"Primary set: per-family questions with the checkpoint at most {sc['primary_max_lead_days']} days out. "
         f"Below {sc['min_blocks_for_claims']} blocks, treat every comparison as an anecdote.", ""]
    if "primary" not in sc:
        return "\n".join(L + ["No resolved questions yet.", ""] + render_voice(sc))
    p = sc["primary"]
    L += ["## Headline", "",
          "| Comparison | Model | Baseline | Blocks | Blocks model better / worse | Questions | Rows | Log loss model / baseline |",
          "|---|---|---|---|---|---|---|---|",
          f"| Model alone | {_f(p['brier_model'])} | | {p['n_blocks']} | | {p['n_questions']} | {p['n_rows']} | {_f(p['logloss_model'])} |"]
    for key, lab in (("vs_market", "vs market (Polymarket rung)"), ("vs_ewma", "vs old EWMA model"), ("vs_climatology", "vs base rate")):
        v = sc.get(key)
        if v:
            L.append(f"| {lab} | {_f(v['brier_model'])} | {_f(v['brier_baseline'])} | {v['n_blocks']} | "
                     f"{v['blocks_model_better']} / {v['blocks_baseline_better']} | {v['n_questions']} | {v['n_rows']} | "
                     f"{_f(v['logloss_model'])} / {_f(v['logloss_baseline'])} |")
    L += ["", "Each row uses only the questions where that baseline has a number, so the model column differs between rows.", ""]
    v = sc.get("vs_market")
    if v:
        L += ["## Per block, model vs market", "", "| Block | Model | Market |", "|---|---|---|"]
        L += [f"| {k} | {_f(x['model'])} | {_f(x['baseline'])} |" for k, x in v["per_block"].items()]
        L.append("")
    if sc.get("blend_curve"):
        L += [f"## What a model–market blend would have scored ({sc['blend_curve_n_blocks']} blocks; descriptive, see EXPERIMENTS.md E1)", "",
              "| " + " | ".join(sc["blend_curve"]) + " |", "|" + "---|" * len(sc["blend_curve"]),
              "| " + " | ".join(_f(x) for x in sc["blend_curve"].values()) + " |", ""]
    L += ["## Calibration (primary set)", "", "| Model said | Blocks | Rows | Mean forecast | Happened |", "|---|---|---|---|---|"]
    L += [f"| {c['bucket']} | {c['n_blocks']} | {c['n_rows']} | {c['mean_p']:.0%} | {c['observed']:.0%} |" for c in sc["calibration"]]
    L += ["", "## By lead time and model version", "", "| Slice | Blocks | Rows | Model | Market | Base rate |", "|---|---|---|---|---|---|"]
    for k, x in sc["by_lead"].items():
        L.append(f"| lead {k} | {x['n_blocks']} | {x['n_rows']} | {_f(x['brier_model'])} | {_f(x['brier_market'])} | {_f(x['brier_clim'])} |")
    for k, x in sc["by_version"].items():
        L.append(f"| {k} | {x['n_blocks']} | {x['n_rows']} | {_f(x['brier_model'])} | | |")
    ld = sc["long_dated"]
    L += ["", f"Long-dated rows (not in the headline): {ld['n_rows']} rows, {ld['n_blocks']} blocks, model Brier {_f(ld['brier_model'])}.", ""]
    L += ["## Name calls", ""]
    if sc.get("name_calls"):
        L += ["| Shipped | Date | Snapshots | Mean P(shipped name) | Top call | Hit |", "|---|---|---|---|---|---|"]
        L += [f"| {n['model']} | {n['date']} | {n['n_snapshots']} | {n['mean_p_shipped_name']:.0%} | {n['top_call']} | {'yes' if n['top_call_hit'] else 'no'} |"
              for n in sc["name_calls"]]
    else:
        L.append("None resolved yet.")
    if sc.get("release_timing"):
        L += ["", "## Release timing", "", "| Shipped | Snapshots | Mean P(by release day) | Inside 80% window | Mean median error (days) |", "|---|---|---|---|---|"]
        L += [f"| {t['model']} | {t['n_snapshots']} | {t['mean_p_by_release_day']:.0%} | {t['in80_share']:.0%} | {_f(t['mean_median_error_days'], '+.0f')} |"
              for t in sc["release_timing"]]
    L += render_voice(sc)
    return "\n".join(L) + "\n"


def render_voice(sc):
    v = sc.get("voice")
    if not v:
        return []
    L = ["", "## Voice model (its own block; in none of the numbers above)", ""]
    if v.get("error"):
        return L + [f"Could not be scored: {v['error']}", ""]
    L += [f"Questions: will Anthropic ship a speech model of its own by each horizon date, on three rungs (`voice.py`, `data/voice_params.json`). "
          f"{v['n_logged_rows']} rows logged over {v['n_snapshots']} snapshot(s); {v['n_resolved_rows']} resolved, {v['n_open_rows']} open. "
          f"All rungs hang on one event, so this is one block however many rows it holds."]
    if not v["n_resolved_rows"]:
        return L + ["", f"Nothing has resolved. The first horizon is {v['first_checkpoint']}.", ""]
    L += ["", "| Comparison | Brier | Questions |", "|---|---|---|",
          f"| Model (base rate + signals) | {_f(v['brier_model'])} | {v['n_questions']} |",
          f"| Published (after any market blend) | {_f(v['brier_published'])} | {v['n_questions']} |",
          f"| Base rate alone | {_f(v['brier_base_rate'])} | {v['n_questions']} |"]
    m = v.get("vs_market")
    L.append(f"| Market, on the {m['n_questions']} questions with a price: model {_f(m['brier_model'])} | {_f(m['brier_baseline'])} | {m['n_questions']} |"
             if m else "| Market | — (no matching market) | 0 |")
    L += ["", "| Rung | Questions | Model | Base rate |", "|---|---|---|---|"]
    L += [f"| {k} | {x['n_questions']} | {_f(x['brier_model'])} | {_f(x['brier_base_rate'])} |" for k, x in v["per_rung"].items()]
    return L + [""]


if __name__ == "__main__":
    from datetime import datetime
    from zoneinfo import ZoneInfo
    main(sys.argv[1] if len(sys.argv) > 1 else datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d"))
