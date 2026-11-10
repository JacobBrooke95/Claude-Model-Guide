"""One model experiment: the live configuration against one variant, on the
rolling-origin backtest and on the forward snapshots.

    python3 tools/experiment.py --name E4-slow-decay --set rho=0.3
    python3 tools/experiment.py --name smoke --set cap=3 --every 8          # quick check, every 8th origin
    python3 tools/experiment.py --name E7 --set w_ewma=0.4 --periods tune   # selection period only

`--set key=value` overrides fields of engine.forecast.Config for the variant
(repeatable). A new idea first gets a Config flag that defaults to off, so
the base configuration is untouched until the idea is adopted. Nothing in the
repo's records is written: the only output is output/experiments/<name>.json
and the table printed here. Paste the table into EXPERIMENTS.md whatever the
result.

Protocol (EXPERIMENTS.md has the full rules)
  selection   tuning origins, weekly 2024-06-03 → 2025-06-30. The pre-registered
              metric is the mean 30-day Brier over Opus, Sonnet and Haiku there.
              With `--layer signal` (changes to engine/signals.py behaviour) the
              selection metric is the holdout's all-family 30-day Brier with a
              doubled margin, because the tuning period has almost no sightings;
              such an adoption is provisional (EXPERIMENTS.md, rule 4).
  no-harm     holdout origins, weekly 2025-07-07 → 2026-10-26, incl. Fable/Mythos.
              Never used to choose a value: the holdout was already seen many
              times (README, "How the configuration was chosen").
  forward     base and variant re-run at every frozen snapshot origin and scored
              on the resolved questions, clustered as in tools/scorecard.py.
              Today's signal file carries mappings made after the fact, so this
              is a sanity check that the variant does no harm, not a score.

One MCMC chain per origin (the live model averages four), as the v3d check did.
Differences below about 0.002 Brier are inside chain noise.
"""
from __future__ import annotations

import json
import os
import sys
from dataclasses import fields, replace

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
sys.path.insert(0, ROOT)
sys.path.insert(0, HERE)
os.chdir(ROOT)

from engine import backtest as bt                                   # noqa: E402
from engine.data import load_competitors, load_releases, load_signals  # noqa: E402
from engine.forecast import Config, FitCache, forecast              # noqa: E402

PERIODS = {"tune": ("2024-06-03", "2025-06-30"), "lock": ("2025-07-07", "2026-10-26")}
OSH, FM = ["opus", "sonnet", "haiku"], ["fable", "mythos"]
MIN_GAIN, MAX_HARM, MAX_HARM_OTHER = 0.002, 0.002, 0.005


def live_config():
    """The configuration live.py runs (keep in step with live.py's FULL), one chain,
    with the backtest's strict before-the-origin rule for sightings."""
    best = pd.read_csv("output/tuning_v2_ranking.csv").config.iloc[0]
    err, trend, w, hl = best.split("|")
    base = Config(err=err, trend=trend, w_wave=float(w[1:]), half_life=None if hl == "hlNone" else float(hl[2:]))
    return replace(base, signals=True, absence=False, w_ewma=0.3, n_seeds=1, sig_recent=True, same_day=False)


def parse_sets(sets):
    types = {f.name: f.type for f in fields(Config)}
    out = {}
    for s in sets:
        k, _, v = s.partition("=")
        if k not in types:
            raise SystemExit(f"unknown Config field '{k}'. Fields: {', '.join(types)}")
        if v in ("None", "none"):
            out[k] = None
        elif v in ("True", "true", "False", "false"):
            out[k] = v.lower() == "true"
        else:
            try:
                out[k] = int(v) if v.lstrip("-").isdigit() and "int" in str(types[k]) else float(v)
            except ValueError:
                out[k] = v
    return out


def block_means(df, col, rel):
    d = df.assign(L=(df[col] - df.y) ** 2, block=bt.interval_blocks(df, rel))
    return d.groupby("block").L.mean()


def table(df, rel):
    rows = []
    for grp, fams in (("opus/sonnet/haiku", OSH), ("fable/mythos", FM), ("all five", OSH + FM)):
        for h in (7, 30, 90):
            d = df[df.target.isin(fams) & (df.h == h)].dropna(subset=["base", "variant"])
            if d.empty:
                continue
            b, v = block_means(d, "base", rel), block_means(d, "variant", rel)
            rows.append(dict(group=grp, h=h, n=int(len(d)), n_blocks=int(len(b)), base=float(((d.base - d.y) ** 2).mean()),
                             variant=float(((d.variant - d.y) ** 2).mean()), blocks_better=int((v < b - 1e-9).sum()),
                             blocks_worse=int((v > b + 1e-9).sum())))
    return rows


def forward(rel, comp, sig, cfgs):
    """Re-run both configs at each frozen snapshot origin; score resolved primary questions."""
    import scorecard as sc
    rows, _ = sc.load_rows(str(pd.Timestamp.now().date()))
    if rows.empty:
        return None
    rows = rows[rows.lead <= sc.PRIMARY_MAX_LEAD].copy()
    cache = FitCache()
    for name, cfg in cfgs.items():
        cfg = replace(cfg, same_day=True)   # live runs count same-day sightings
        fc = {}
        for o in sorted(rows.as_of.unique()):
            fc[o] = forecast(rel, comp, sig, o, cfg, cache)[0]
        rows[f"p_{name}"] = [float(np.sum(fc[r.as_of][r.target][0][:r.lead + 1])) for r in rows.itertuples()]
    out = {}
    for name in cfgs:
        m, b = sc.clustered(rows, f"p_{name}")
        out[name] = dict(brier=m, n_blocks=int(len(b)))
    out["n_rows"] = int(len(rows))
    return out


def main(argv):
    def opt(flag, default=None):
        return argv[argv.index(flag) + 1] if flag in argv else default
    name = opt("--name")
    sets = [argv[i + 1] for i, a in enumerate(argv) if a == "--set"]
    if not name or not sets:
        raise SystemExit(__doc__)
    every = int(opt("--every", "1"))
    periods = opt("--periods", "tune,lock").split(",")
    rel, comp, sig = load_releases(), load_competitors(), load_signals()
    base = live_config()
    over = parse_sets(sets)
    cfgs = {"base": base, "variant": replace(base, **over)}
    res = dict(name=name, overrides=over, every=every, run_at=str(pd.Timestamp.now().date()), periods={})
    data_end = str((rel.date.max()).date())
    for p in periods:
        origins = bt.weekly_origins(*PERIODS[p])[::every]
        df, _ = bt.run(rel, comp, sig, cfgs, origins, data_end, cache=FitCache(), with_ewma=False)
        res["periods"][p] = dict(n_origins=len(origins), rows=table(df, rel))
    if "--no-forward" not in argv:
        res["forward"] = forward(rel, comp, sig, cfgs)

    def pick(p, grp, h):
        return next((r for r in res["periods"].get(p, {}).get("rows", []) if r["group"] == grp and r["h"] == h), None)

    checks = []
    layer = opt("--layer", "cadence")
    res["layer"] = layer
    if layer == "signal":
        # almost all sightings are from 2026, so the tuning period cannot see a signal-layer
        # change. Selection moves to the holdout, with a doubled margin and a block-count
        # condition, and the variant's value must have been written down before the run.
        t = pick("lock", "all five", 30)
        if t:
            checks.append(("selection (signal layer): holdout all-family 30-day Brier improves by >= %.3f" % (2 * MIN_GAIN),
                           t["base"] - t["variant"] >= 2 * MIN_GAIN))
            checks.append(("selection (signal layer): more holdout blocks better than worse", t["blocks_better"] > t["blocks_worse"]))
    else:
        t = pick("tune", "opus/sonnet/haiku", 30)
        if t:
            checks.append(("selection: tuning O/S/H 30-day Brier improves by >= %.3f" % MIN_GAIN, t["base"] - t["variant"] >= MIN_GAIN))
    for grp in ("opus/sonnet/haiku", "fable/mythos"):
        r = pick("lock", grp, 30)
        if r:
            checks.append((f"no-harm: holdout {grp} 30-day not worse by > {MAX_HARM}", r["variant"] - r["base"] <= MAX_HARM))
    for p in res["periods"]:
        for r in res["periods"][p]["rows"]:
            if r["h"] != 30 and r["group"] != "all five":
                checks.append((f"no-harm: {p} {r['group']} {r['h']}-day not worse by > {MAX_HARM_OTHER}", r["variant"] - r["base"] <= MAX_HARM_OTHER))
    f = res.get("forward")
    if f and f["base"]["brier"] is not None:
        checks.append((f"no-harm: forward snapshots not worse by > {MAX_HARM_OTHER}", f["variant"]["brier"] - f["base"]["brier"] <= MAX_HARM_OTHER))
    complete = every == 1 and set(periods) == {"tune", "lock"} and "forward" in res
    res["checks"] = [dict(check=c, passed=bool(ok)) for c, ok in checks]
    res["verdict"] = ("PASS" if all(ok for _, ok in checks) else "FAIL") if complete else "INCOMPLETE (partial run: not a basis for adoption)"

    os.makedirs("output/experiments", exist_ok=True)
    json.dump(res, open(f"output/experiments/{name}.json", "w"), indent=1, default=float)
    print(f"\nExperiment {name}: variant = live config with {over}\n")
    print("| Period | Group | Horizon | Rows | Blocks | Base | Variant | Diff | Blocks better / worse |")
    print("|---|---|---|---|---|---|---|---|---|")
    for p, v in res["periods"].items():
        for r in v["rows"]:
            print(f"| {p} | {r['group']} | {r['h']} d | {r['n']} | {r['n_blocks']} | {r['base']:.4f} | {r['variant']:.4f} | "
                  f"{r['variant'] - r['base']:+.4f} | {r['blocks_better']} / {r['blocks_worse']} |")
    if f:
        print(f"| forward | primary questions | ≤92 d | {f['n_rows']} | {f['base']['n_blocks']} | {f['base']['brier']:.4f} | "
              f"{f['variant']['brier']:.4f} | {f['variant']['brier'] - f['base']['brier']:+.4f} | |")
    print()
    for c, ok in checks:
        print(f"  [{'ok' if ok else 'NO'}] {c}")
    print(f"\nVerdict: {res['verdict']}  (saved output/experiments/{name}.json)")


if __name__ == "__main__":
    main(sys.argv[1:])
