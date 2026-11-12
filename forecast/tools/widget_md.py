"""Print the forecast widget as a plain-Markdown block for a daily note.

    python3 forecast/tools/widget_md.py [DATE] [--heading]

The static twin of ../../forecast-widget.html (see ../WIDGET.md): same numbers,
same rounding, same date forms. Reads only files in this repo, standard library
only, writes nothing.

  no DATE      the latest forecast (output/forecast.json, output/voice_forecast.json)
  DATE         the snapshot of that day (history/forecast_<DATE>.json); if there was
               no run that day, the newest snapshot on or before it, and the block
               says so. The voice line is left out when no voice snapshot exists on
               or before DATE.
  --heading    start the block with "### Claude Forecast"
"""
import csv
import glob
import json
import os
import re
import sys
from decimal import ROUND_HALF_UP, Decimal

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
URL = "https://jacobbrooke95.github.io/Claude-Model-Guide/release-forecast.html"
FAMS = ["opus", "sonnet", "haiku", "fable", "mythos"]
MON = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def pct(x):
    """The page's (100 * x).toFixed(0) + '%': half rounds up, on the double's exact value."""
    return "—" if x is None else f"{Decimal(100 * x).quantize(Decimal(1), rounding=ROUND_HALF_UP)}%"


def fmt(s, base_year, short=False, year=False):
    """'Dec 10'; outside the as-of year 'Jan 19, 2027', or 'Jan 19 ’27' when short."""
    if not s:
        return "—"
    if s[0] == ">":
        return "later" if short else "after " + fmt(s[1:], base_year)
    y, m, d = map(int, s.split("-"))
    out = f"{MON[m - 1]} {d}"
    if year or y != base_year:
        out += f" ’{y % 100:02d}" if short else f", {y}"
    return out


def load(kind, date):
    """(snapshot, exact). With a date: the newest history file on or before it, else (None, False)."""
    if not date:
        p = os.path.join(ROOT, "output", kind + ".json")
        return (json.load(open(p)) if os.path.exists(p) else None), True
    days = sorted(re.search(r"_(\d{4}-\d{2}-\d{2})\.json$", p).group(1)
                  for p in glob.glob(os.path.join(ROOT, "history", kind + "_*.json")))
    days = [d for d in days if d <= date]
    if not days:
        return None, False
    return json.load(open(os.path.join(ROOT, "history", f"{kind}_{days[-1]}.json"))), days[-1] == date


def delta(log, as_of, target, checkpoint, now, col):
    """' ▲6' when the number moved 3 points or more against the snapshot before as_of."""
    p = os.path.join(ROOT, log)
    if now is None or not os.path.exists(p):
        return ""
    rows = list(csv.DictReader(open(p)))
    before = sorted({r["as_of"] for r in rows if r["as_of"] < as_of})
    if not before:
        return ""
    was = [r[col] for r in rows if r["as_of"] == before[-1] and r["target"] == target and r["checkpoint"] == checkpoint]
    if not was or not was[0]:
        return ""
    d = 100 * (now - float(was[0]))
    if abs(d) < 3:
        return ""
    return f" {'▲' if d > 0 else '▼'}{Decimal(abs(d)).quantize(Decimal(1), rounding=ROUND_HALF_UP)}"


def main(argv):
    args = [a for a in argv if not a.startswith("--")]
    date = args[0] if args else None
    if date and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        sys.exit("DATE must be YYYY-MM-DD")
    F, exact = load("forecast", date)
    note = ""
    if F is None:  # nothing on or before the date: show the latest and say so
        F, _ = load("forecast", None)
        if F is None:
            sys.exit("no forecast found")
        note = f"No snapshot on or before {fmt(date, int(F['as_of'][:4]))}; showing "
    elif not exact:
        note = f"No snapshot for {fmt(date, int(F['as_of'][:4]))}; showing "
    by = int(F["as_of"][:4])
    T = {f: F["targets"][f]["with_signals"] for f in FAMS if f in F["targets"]}
    c1, c2 = (F.get("checkpoints") or sorted(d for d in next(iter(T.values()))["by"] if d >= F["as_of"]))[:2]
    top = max(T, key=lambda f: (T[f]["by"][c2], T[f]["by"][c1]))

    L = []
    if "--heading" in argv:
        L += ["### Claude Forecast", ""]
    L += [f"*{note or 'As of '}{fmt(F['as_of'], by, year=True)} · {F.get('model_version', '')} · [Full forecast →]({URL})*", "",
          f"**Next most likely: {top.capitalize()} — {pct(T[top]['by'][c2])} by {fmt(c2, by)}, median {fmt(T[top]['median'], by)}**", "",
          f"| Next | by {fmt(c1, by)} | by {fmt(c2, by)} | Median | 80% window |",
          "|:--|--:|--:|:--|:--|"]
    for f, t in T.items():
        L.append(f"| {f.capitalize()} "
                 f"| {pct(t['by'][c1])}{delta('forecast_log.csv', F['as_of'], f, c1, t['by'][c1], 'p_model')} "
                 f"| {pct(t['by'][c2])}{delta('forecast_log.csv', F['as_of'], f, c2, t['by'][c2], 'p_model')} "
                 f"| {fmt(t['median'], by, short=True)} | {fmt(t['q10'], by, short=True)} – {fmt(t['q90'], by, short=True)} |")

    V, _ = load("voice_forecast", date)
    A = (V or {}).get("rungs", {}).get("A")
    if A:
        tag = "" if V["as_of"] == F["as_of"] else f" (as of {fmt(V['as_of'], by)})"
        if A.get("resolved"):
            L += ["", f"Voice model (rung A): **resolved {fmt((A.get('resolution') or {}).get('resolved_date'), by)}**{tag}"]
        else:
            hz = [h for h in V.get("horizons", sorted(A["by"])) if h in A["by"] and h >= V["as_of"]][:2]
            bits = [f"**{pct(A['by'][h]['final'])}**{delta('voice_forecast_log.csv', V['as_of'], 'voice_A', h, A['by'][h]['final'], 'p_final')} by {fmt(h, by)}"
                    for h in hz]
            L += ["", "Voice model (rung A): " + " · ".join(bits + [f"median {fmt(A['median'], by)}"]) + tag]
    print("\n".join(L))


if __name__ == "__main__":
    main(sys.argv[1:])
