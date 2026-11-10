"""Pull today's prediction-market prices → data/raw/markets_<DATE>.csv.

    python3 tools/pull_markets.py [DATE] [--force]

Same columns and the same question wording the hand-written files use
(platform, question, prob, volume, close_date, url, retrieved_at), so
engine/market.py and tools/build_page.py read it unchanged.

Polymarket: gamma-api public search for a few fixed queries; open markets only,
kept when the question is about a Claude/Anthropic model release (or the
Anthropic IPO date, which the weekly narrative uses). prob is the Yes price.
Manifold: open markets whose question is about a Claude release date; each
answer of a multiple-choice market becomes one row.

A market that has closed or resolved is not written: it answers a question
that is no longer open. If a platform cannot be reached, its rows are simply
missing and the script says so; it never writes prices it did not fetch. If
nothing at all could be fetched, no file is written and live.py falls back to
the most recent earlier file (the forecast's `market_file` field shows which).

The file for a date is written once. A second run the same day leaves it
alone unless --force is given (use --force only before the day's forecast has
been frozen).
"""
from __future__ import annotations

import csv
import json
import os
import re
import subprocess
import sys
import urllib.parse
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
PM_QUERIES = ["claude", "next claude", "next fable", "next mythos", "claude 6", "anthropic ipo by", "anthropic model released"]
MODEL = r"(claude|anthropic|fable|mythos|opus|sonnet|haiku)"
KEEP = re.compile(rf"(?i)({MODEL}.*\breleased?\b|\breleased?\b.*{MODEL}|will anthropic ipo by)")
DROP = re.compile(r"(?i)(price|arena|exam|hle|score|valuation|market cap|weights|cheaper)")
MF_KEEP = re.compile(r"(?i)(claude|fable|mythos).*(release date|released? (by|before|in)|be released)")


def get(url):
    r = subprocess.run(["curl", "-sS", "-L", "-m", "40", "-A", "release-sweep/1.0", url], capture_output=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.decode("utf-8", "replace")[:200])
    return json.loads(r.stdout)


def polymarket(now):
    rows, seen = [], set()
    for q in PM_QUERIES:
        j = get("https://gamma-api.polymarket.com/public-search?limit_per_type=50&events_status=active&q=" + urllib.parse.quote(q))
        for ev in j.get("events") or []:
            if ev.get("closed"):
                continue
            for m in ev.get("markets") or []:
                qn = (m.get("question") or "").strip()
                if m.get("closed") or qn in seen or not KEEP.search(qn) or DROP.search(qn):
                    continue
                try:
                    prob = float(json.loads(m["outcomePrices"])[0])
                except Exception:
                    continue
                seen.add(qn)
                rows.append(["Polymarket", qn, round(prob, 4), int(float(m.get("volume") or 0)), (m.get("endDate") or "")[:10],
                             "https://polymarket.com/event/" + ev.get("slug", ""), now])
    return rows


def manifold(now):
    rows, seen = [], set()
    for term in ("claude release date", "claude released", "claude fable", "claude opus"):
        j = get("https://api.manifold.markets/v0/search-markets?filter=open&limit=50&term=" + urllib.parse.quote(term))
        for m in j:
            qn = m.get("question", "").strip()
            if m.get("isResolved") or m["id"] in seen or not MF_KEEP.search(qn) or DROP.search(qn):
                continue
            seen.add(m["id"])
            if m.get("outcomeType") == "BINARY" and m.get("probability") is not None:
                rows.append(["Manifold", qn, round(float(m["probability"]), 4), f"{int(m.get('volume') or 0)} mana", "", m.get("url", ""), now])
            elif m.get("outcomeType") == "MULTIPLE_CHOICE":
                full = get("https://api.manifold.markets/v0/market/" + m["id"])
                for a in full.get("answers") or []:
                    if a.get("resolution") or a.get("probability") is None:
                        continue
                    rows.append(["Manifold", f"{qn}: {a.get('text', '').strip()}", round(float(a["probability"]), 4),
                                 f"{int(full.get('volume') or 0)} mana (market total)", "", m.get("url", ""), now])
    return rows


def main(argv):
    force = "--force" in argv
    argv = [a for a in argv if not a.startswith("--")]
    date = argv[0] if argv else datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d")
    path = os.path.join(ROOT, f"data/raw/markets_{date}.csv")
    if os.path.exists(path) and not force:
        print(f"{os.path.relpath(path, ROOT)} exists: left as is")
        return 0
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    rows, failed = [], []
    for name, fn in (("Polymarket", polymarket), ("Manifold", manifold)):
        try:
            got = fn(now)
            rows += got
            print(f"{name}: {len(got)} rows")
        except Exception as e:  # network, API shape
            failed.append(name)
            print(f"{name}: FAILED ({type(e).__name__}: {str(e)[:160]}). Record this in the daily note.")
    if not rows:
        print("no market rows fetched: no file written; live.py will use the latest earlier markets file")
        return 1
    with open(path, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["platform", "question", "prob", "volume", "close_date", "url", "retrieved_at"])
        w.writerows(rows)
    print(f"wrote {os.path.relpath(path, ROOT)} ({len(rows)} rows){' - missing: ' + ', '.join(failed) if failed else ''}")
    # show what the engine will read from it
    sys.path.insert(0, ROOT)
    import pandas as pd
    from engine import market as mk
    lad = mk.ladders(pd.read_csv(path))
    for fam, L in lad.items():
        print(f"  ladder {fam}: " + ", ".join(f"{d.date()} {p:.2f}" for d, p in zip(L.date, L.raw)))
    if not lad:
        print("  no 'Next <family> (X+) released by <date>?' ladder parsed; check the wording against engine/market.py LADDERS")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
