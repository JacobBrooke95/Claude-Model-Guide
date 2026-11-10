"""Weekly update: forecast, snapshot, grade, summarize, rebuild the page.

    python3 weekly.py                 # as of today (America/Chicago)
    python3 weekly.py 2026-11-06      # as of a given day

Mechanical steps only. The judgment steps (finding new releases, signals and
market prices, editing data files, writing the narrative) are in
WEEKLY_RUNBOOK.md and happen before this script runs.

The steps are functions so daily.py can reuse them (see DAILY_RUNBOOK.md). The
daily task normally runs `daily.py`, which on Sundays also writes the weekly
summary; this script stays as the weekly-only entry point.

Writes:
  output/forecast.json            the live forecast (via live.py)
  history/forecast_<date>.json    frozen snapshot, never edited
  forecast_log.csv                appended by live.py, never edited
  output/grades.json              forward track record, rebuilt from history/
  weekly/<date>.md                the weekly summary (narrative section left for the runbook)
  ../release-forecast.html        rebuilt page
"""
from __future__ import annotations

import glob
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
FORWARD_START = "2026-10-30"   # first frozen forecast; grading starts here
FAMS = ["fable", "opus", "sonnet", "haiku", "mythos"]


def today_chicago():
    return datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write(r.stdout + r.stderr)
        raise SystemExit(f"failed: {' '.join(cmd)}")
    return r.stdout


def _err(v):
    # the median can lie beyond the 400-day horizon (">YYYY-MM-DD"); then there is no error in days
    return f" ({v:+d} d)" if v is not None else ""


# 1. forecast + snapshot -------------------------------------------------------
def forecast_and_snapshot(as_of):
    """Run live.py for `as_of` and freeze the snapshot. One forecast per origin:
    if history/forecast_<as_of>.json already exists, live.py is not run again
    and output/forecast.json is restored from the snapshot. A second run on the
    same day (the daily and weekly tasks both firing, or a retry) therefore
    cannot leave the published forecast disagreeing with the frozen one or with
    the log. Inputs found after the day's first run go into the next day's run.
    Returns True if a new forecast was made."""
    os.makedirs("history", exist_ok=True)
    snap = f"history/forecast_{as_of}.json"
    if os.path.exists(snap):
        shutil.copy(snap, "output/forecast.json")
        print(f"{snap} exists: the forecast for this origin is already frozen; live.py not re-run")
        return False
    print(run([sys.executable, "live.py", as_of]))
    shutil.copy("output/forecast.json", snap)
    return True


# 2. grade ---------------------------------------------------------------------
def grade(as_of):
    """Rebuild output/grades.json from history/, forecast_log.csv and the
    release table. Returns (grades, snapshots)."""
    rel = pd.read_csv("data/anthropic_releases.csv", parse_dates=["date"])
    snaps = []
    for p in sorted(glob.glob("history/forecast_*.json")):
        s = json.load(open(p))
        snaps.append(s)

    grades = {"forward_start": FORWARD_START, "releases": [], "checkpoints": [], "summary": {}}
    fwd = rel[rel.date > pd.Timestamp(FORWARD_START)]
    for _, r in fwd.iterrows():
        f = r.family
        if f not in FAMS:
            continue
        prev = rel[(rel.family == f) & (rel.date < r.date)].date.max()
        for s in snaps:
            a = pd.Timestamp(s["as_of"])
            # a snapshot grades this release if it was made after the previous
            # release of the family and before this one
            if not (a <= r.date and (pd.isna(prev) or a > prev)):
                continue
            t = s["targets"][f]["with_signals"]
            off = (r.date - a).days
            cdf, pmf = t["cdf180"], t["pmf180"]
            if off < len(cdf):
                p_by = cdf[off]
                p_week = float(sum(pmf[max(off - 3, 0):off + 4]))
                p_day = pmf[off]
            else:
                p_by, p_week, p_day = 1 - t["tail_beyond_horizon"], None, None
            med = t["median"]
            med_err = (pd.Timestamp(med) - r.date).days if not med.startswith(">") else None
            in80 = (not t["q10"].startswith(">")) and pd.Timestamp(t["q10"]) <= r.date and \
                   (t["q90"].startswith(">") or r.date <= pd.Timestamp(t["q90"]))
            mk = [m for m in s["markets"].get(f, []) if pd.Timestamp(m["date"]) >= r.date]
            grades["releases"].append(dict(model=r.model, family=f, date=str(r.date.date()), as_of=s["as_of"], days_ahead=off,
                                           p_by_date=float(p_by), p_week=p_week, p_day=p_day, median=med,
                                           median_error_days=med_err, in80=bool(in80),
                                           market_next_rung=(dict(date=mk[0]["date"], p=mk[0]["market"]) if mk else None),
                                           log_score_week=(float(np.log(max(p_week, 1e-4))) if p_week is not None else None)))

    # dated checkpoint questions from the forward log
    log = pd.read_csv("forecast_log.csv", parse_dates=["as_of", "checkpoint"])
    today = pd.Timestamp(as_of)
    TF = {f: [f] for f in FAMS} | {"frontier": ["opus", "fable", "mythos"], "any": FAMS}
    rows = []
    for _, q in log.iterrows():
        ds = rel[rel.family.isin(TF[q.target]) & (rel.date >= q.as_of)].date
        hit = ((ds >= q.as_of) & (ds <= q.checkpoint)).any()
        if hit:
            y = 1
        elif q.checkpoint < today:
            y = 0
        else:
            continue
        rows.append(dict(as_of=str(q.as_of.date()), target=q.target, checkpoint=str(q.checkpoint.date()), y=int(y),
                         p_model=float(q.p_model), p_market=(None if pd.isna(q.p_market) else float(q.p_market))))
    grades["checkpoints"] = rows
    if rows:
        c = pd.DataFrame(rows)
        fam = c[c.target.isin(FAMS)]
        sm = dict(n=int(len(fam)), brier_model=float(((fam.p_model - fam.y) ** 2).mean()) if len(fam) else None)
        wm = fam.dropna(subset=["p_market"])
        if len(wm):
            sm.update(n_market=int(len(wm)), brier_model_on_market=float(((wm.p_model - wm.y) ** 2).mean()),
                      brier_market=float(((wm.p_market - wm.y) ** 2).mean()))
        grades["summary"] = sm
    json.dump(grades, open("output/grades.json", "w"), indent=1, default=float)
    return grades, snaps


# 3. weekly summary --------------------------------------------------------------
def summary_lines(as_of, grades, snaps):
    cur = json.load(open("output/forecast.json"))
    prev = [s for s in snaps if s["as_of"] < cur["as_of"]]
    prev = prev[-1] if prev else None
    C1, C2 = cur["checkpoints"]
    lines = [f"# Claude release forecast — week of {as_of}", "",
             f"Model {cur['model_version']}. Page: https://jacobbrooke95.github.io/Claude-Model-Guide/release-forecast.html", "",
             f"| Family | P(by {C1}) | P(by {C2}) | Median | 80% window | Market {C2} | Change since {prev['as_of'] if prev else '—'} |",
             "|---|---|---|---|---|---|---|"]
    for f in FAMS + ["frontier", "any"]:
        t = cur["targets"][f]["with_signals"]
        m = {r["date"]: r["market"] for r in cur["markets"].get(f, [])}
        delta = ""
        if prev and f in prev["targets"]:
            pt = prev["targets"][f]["with_signals"]
            pv = pt.get("by", {}).get(C2)
            if pv is None and "cdf180" in pt:
                j = (pd.Timestamp(C2) - pd.Timestamp(prev["as_of"])).days
                pv = pt["cdf180"][j] if 0 <= j < len(pt["cdf180"]) else None
            if pv is not None:
                delta = f"{100 * (t['by'][C2] - pv):+.0f} pts (by {C2})"
        lines.append(f"| {f.capitalize()} | {t['by'][C1]:.0%} | {t['by'][C2]:.0%} | {t['median']} | {t['q10']} – {t['q90']} | "
                     f"{(format(m[C2], '.0%') if C2 in m else '—')} | {delta} |")
    lines += ["", "## Graded since launch", ""]
    if grades["releases"]:
        for g in grades["releases"]:
            lines.append(f"- **{g['model']}** ({g['date']}): forecast of {g['as_of']} gave {g['p_by_date']:.0%} by that day, "
                         f"{(g['p_week'] or 0):.0%} for that week; median call {g['median']}{_err(g['median_error_days'])}; "
                         f"inside 80% window: {'yes' if g['in80'] else 'no'}.")
    else:
        lines.append("- No release since the forward log began.")
    if grades["summary"].get("n"):
        s = grades["summary"]
        lines.append(f"- Dated questions resolved: {s['n']}, model Brier {s['brier_model']:.3f}"
                     + (f"; where a market existed ({s['n_market']}): model {s['brier_model_on_market']:.3f} vs market {s['brier_market']:.3f}" if s.get("n_market") else "") + ".")
    lines += ["", "## What changed this week", "", "<!-- NARRATIVE: filled in by the weekly run (see WEEKLY_RUNBOOK.md) -->", ""]
    return lines


def write_summary(as_of, grades, snaps):
    """Write weekly/<as_of>.md (never overwritten). Returns the summary lines."""
    lines = summary_lines(as_of, grades, snaps)
    os.makedirs("weekly", exist_ok=True)
    wp = f"weekly/{as_of}.md"
    if not os.path.exists(wp):
        open(wp, "w").write("\n".join(lines))
    else:
        print(f"{wp} exists — left as is")
    return lines


# 4. page ------------------------------------------------------------------------
def build_page():
    print(run([sys.executable, "tools/build_page.py"]))


def main(as_of):
    forecast_and_snapshot(as_of)
    grades, snaps = grade(as_of)
    lines = write_summary(as_of, grades, snaps)
    build_page()
    print("\n".join(lines))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else today_chicago())
