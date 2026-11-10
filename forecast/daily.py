"""Daily run: the mechanical half of DAILY_RUNBOOK.md, in one command.

    python3 daily.py                      # today (America/Chicago)
    python3 daily.py 2026-11-12           # a given run date
    python3 daily.py --dry-run            # full run in a throwaway copy of the repo; the repo is not touched
    python3 daily.py --weekly             # also write weekly/<date>.md (automatic on Sundays)
    python3 daily.py --no-markets         # skip the market pull (use the latest markets file on disk)

Order: build signals → pull markets → forecast + frozen snapshot → grade →
scorecard → source ledger → daily note → (Sunday) weekly summary → page.
The judgment steps (the sweep, reading sources, logging signals, registering a
release, the narrative, the day's experiment) are in DAILY_RUNBOOK.md; do
them before this script, then fill in the note it writes.

Safe to run twice. One forecast per origin: if history/forecast_<origin>.json
exists, the forecast is not recomputed and no log rows are added; the
scorecard, ledger and page are rebuilt, and the existing note is left alone.

Release days. The engine counts only releases dated before its origin. If a
release dated on or after the run date is already in the release table, the
origin moves to the day after it ("data through the release day"), as the
2026-11-10 run did by hand. The next day's run then finds that origin frozen
and adds no second forecast.
"""
from __future__ import annotations

import csv
import filecmp
import json
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
COPY = ["forecast", "data", "scripts", "styles.css", "package.json"]  # plus root *.html; enough to run everything


def dry_run(argv):
    tmp = tempfile.mkdtemp(prefix="forecast-dryrun-")
    for name in COPY + [f for f in os.listdir(REPO) if f.endswith(".html")]:
        src = os.path.join(REPO, name)
        if os.path.isdir(src):
            shutil.copytree(src, os.path.join(tmp, name), ignore=shutil.ignore_patterns("__pycache__"))
        elif os.path.exists(src):
            shutil.copy(src, os.path.join(tmp, name))
    print(f"DRY RUN in {tmp} (the repo is not modified)\n")
    r = subprocess.run([sys.executable, os.path.join(tmp, "forecast", "daily.py")] + [a for a in argv if a != "--dry-run"])
    changed = []

    def walk(c, rel=""):
        changed.extend(os.path.join(rel, f) + "  (new)" for f in c.right_only)
        changed.extend(os.path.join(rel, f) for f in c.diff_files)
        for name, sub in c.subdirs.items():
            walk(sub, os.path.join(rel, name))
    walk(filecmp.dircmp(REPO, tmp, ignore=["__pycache__", ".git", "system-cards", "node_modules", ".githooks", ".claude"]))
    print("\nDRY RUN: a real run would add or change these files:")
    for c in sorted(changed):
        print("  " + c)
    print(f"\nDRY RUN finished with exit code {r.returncode}. Copy left at {tmp} for inspection.")
    return r.returncode


def step(title):
    print(f"\n== {title} " + "=" * max(4, 70 - len(title)), flush=True)


def soft(cmd, what):
    """Run a helper whose failure must not stop the forecast. Returns (ok, output)."""
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(out)
    if r.returncode != 0:
        print(f"!! {what} failed (exit {r.returncode}). Carrying on; record it under 'Failures and gaps' in the note.")
    return r.returncode == 0, out


def main(argv):
    if "--dry-run" in argv:
        return dry_run(argv)
    import pandas as pd
    import weekly as W                      # chdirs into forecast/
    sys.path.insert(0, os.path.join(HERE, "tools"))
    flags = {a for a in argv if a.startswith("--")}
    args = [a for a in argv if not a.startswith("--")]
    run_date = args[0] if args else W.today_chicago()
    gaps = []

    step("signals: data/raw/signals_research.csv → data/signals.csv")
    print(W.run([sys.executable, "tools/build_signals.py"]))

    step("markets")
    if "--no-markets" in flags:
        print("skipped (--no-markets)")
    else:
        ok, _ = soft([sys.executable, "tools/pull_markets.py", run_date], "market pull")
        if not ok:
            gaps.append("market pull failed; the forecast used an older markets file")

    step("origin")
    rel = pd.read_csv("data/anthropic_releases.csv", parse_dates=["date"])
    origin = run_date
    late = rel[rel.date >= pd.Timestamp(run_date)]
    if len(late):
        last = late.date.max()
        if last > pd.Timestamp(run_date):
            raise SystemExit(f"release table has a release dated {last.date()}, after the run date {run_date}. Fix data/models.json first.")
        origin = str((last + pd.Timedelta(days=1)).date())
        print(f"A release dated {run_date} is in the table ({', '.join(late.model)}). Origin moved to {origin}: "
              f"the engine only counts releases dated before its origin.")
    else:
        print(f"origin {origin}")

    step("forecast + snapshot")
    made = W.forecast_and_snapshot(origin)

    step("grade")
    grades, snaps = W.grade(run_date)
    print(f"output/grades.json: {len(grades['releases'])} release grades, {len(grades['checkpoints'])} resolved checkpoint rows")

    step("scorecard")
    import scorecard
    sc = scorecard.main(run_date)

    step("source ledger")
    import build_ledger
    build_ledger.main()

    step("checks")
    cur = json.load(open("output/forecast.json"))
    bad = []
    for k, t in cur["targets"].items():
        c = t["with_signals"]["cdf180"]
        if any(b < a - 1e-6 for a, b in zip(c, c[1:])) or min(c) < -1e-9 or max(c) > 1 + 1e-9:
            bad.append(k)
    keys = [tuple(r[:4]) for r in csv.reader(open("forecast_log.csv"))][1:]
    dup = len(keys) - len(set(keys))
    if bad:
        gaps.append(f"CDF not monotone or out of range for: {', '.join(bad)}")
    if dup:
        gaps.append(f"forecast_log.csv has {dup} duplicate (as_of, version, target, checkpoint) rows")
    mfile = cur.get("market_file", "")
    mdate = os.path.basename(mfile)[8:18]
    if mdate < run_date:
        gaps.append(f"market prices are from {mdate}, not today ({mfile})")
    sweep_rows = []
    if os.path.exists("data/raw/sweep_log.csv"):
        sweep_rows = [r for r in csv.DictReader(open("data/raw/sweep_log.csv")) if r["date"] == run_date]
    if not sweep_rows:
        gaps.append("no sweep rows logged for today (run tools/sweep.py run before the forecast)")
    print("ok" if not (bad or dup) else "PROBLEMS: " + "; ".join(gaps))

    step("daily note")
    prev = [s for s in snaps if s["as_of"] < cur["as_of"]]
    prev = prev[-1] if prev else None
    C1, C2 = cur["checkpoints"]

    def prev_by(f, cp):
        if not prev or f not in prev["targets"]:
            return None
        pt = prev["targets"][f]["with_signals"]
        v = pt.get("by", {}).get(cp)
        if v is None:
            j = (pd.Timestamp(cp) - pd.Timestamp(prev["as_of"])).days
            v = pt["cdf180"][j] if 0 <= j < len(pt["cdf180"]) else None
        return v

    def delta(f, cp):
        v = prev_by(f, cp)
        return "" if v is None else f"{100 * (cur['targets'][f]['with_signals']['by'][cp] - v):+.0f}"

    L = [f"# Daily forecast {run_date}", "",
         f"Model {cur['model_version']}, origin {cur['as_of']}"
         + ("" if made else " (already frozen by an earlier run; no new forecast or log rows today)")
         + f". Markets file: `{mfile}`. Compared with the snapshot of {prev['as_of'] if prev else '—'}.", "",
         f"| Family | P(by {C1}) | Δ pts | P(by {C2}) | Δ pts | Median | 80% window | Market {C1} | Market {C2} |",
         "|---|---|---|---|---|---|---|---|---|"]
    for f in W.FAMS + ["frontier", "any"]:
        t = cur["targets"][f]["with_signals"]
        m = {r["date"]: r["market"] for r in cur["markets"].get(f, [])}
        L.append(f"| {f.capitalize()} | {t['by'][C1]:.0%} | {delta(f, C1)} | {t['by'][C2]:.0%} | {delta(f, C2)} | {t['median']} | "
                 f"{t['q10']} – {t['q90']} | {format(m[C1], '.0%') if C1 in m else '—'} | {format(m[C2], '.0%') if C2 in m else '—'} |")
    n = {k: sum(1 for r in sweep_rows if r["result"] == k) for k in ("changed", "signal", "release", "nothing", "baseline", "error", "skipped")}
    L += ["", f"**Scorecard.** {scorecard.headline(sc)} Blocks are the sample size; see `SCORECARD.md`.", "",
          f"**Sweep.** {len(sweep_rows)} checks logged today: {n['changed']} changed, {n['signal']} signal, {n['release']} release, "
          f"{n['nothing'] + n['baseline']} nothing, {n['error']} failed, {n['skipped']} skipped."]
    L += [f"- `{r['source_id']}`: {r['result']}. {r['detail']}" for r in sweep_rows if r["result"] in ("changed", "signal", "release", "error")]
    L += ["", "## New signals", "", "<!-- one line per row added to signals_research.csv today, with grade and URL; or 'None.' -->", "",
          "## Why the numbers moved", "", "<!-- one line per family that moved 3 points or more: which input changed -->", "",
          "## Experiment", "", "<!-- the one experiment run today (id, verdict, one line), or 'None today.' -->", "",
          "## Failures and gaps", ""]
    L += [f"- {g}" for g in gaps] or ["- None found by the script."]
    L += ["", "## Open questions for Jacob", "", "<!-- decisions only he can make; or 'None.' -->", ""]
    os.makedirs("daily", exist_ok=True)
    np_ = f"daily/{run_date}.md"
    if os.path.exists(np_):
        print(f"{np_} exists: left as is")
    else:
        open(np_, "w").write("\n".join(L))
        print(f"wrote {np_}: fill in the commented sections")

    if "--weekly" in flags or pd.Timestamp(run_date).weekday() == 6:
        step("weekly summary (Sunday)")
        W.write_summary(run_date, grades, snaps)
        print(f"weekly/{run_date}.md: write the narrative (WEEKLY_RUNBOOK.md §5)")

    step("page")
    W.build_page()

    print("\n".join(L[:13]))
    print(f"\nDone. {'New forecast frozen for ' + origin if made else 'No new forecast (origin ' + origin + ' already frozen)'}."
          f"{' Gaps: ' + '; '.join(gaps) if gaps else ''}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
