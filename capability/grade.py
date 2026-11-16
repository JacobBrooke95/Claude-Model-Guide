#!/usr/bin/env python3
"""Grade open predictions whose release has shipped.

Reads every snapshot in capability/history/predictions_*.json (written by run.py; a
snapshot is never rewritten once its date has passed), finds for each open prediction
the first release of that family after the snapshot date in data/models.json, looks the
realised value up in the current data, and appends one row per newly resolved prediction
to capability/scorecard.csv. Safe to run daily: already-graded ids are skipped and
predictions whose value is not published yet stay open.

    python3 capability/grade.py [--dry-run]
"""
from __future__ import annotations
import csv
import datetime as dt
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO = ROOT.parent
sys.path.insert(0, str(ROOT))
from build_data import REPO_TO_EPOCH  # noqa: E402

FIELDS = ["id", "issued", "family", "quantity", "model", "release_date", "median", "lo50", "hi50", "lo80", "hi80", "lo95",
          "hi95", "actual", "error", "in50", "in80", "in95", "graded_on", "source"]


def next_release(releases, family, issued):
    c = sorted((r for r in releases if r["family"] == family and r["date"] > issued), key=lambda r: r["date"])
    return c[0] if c else None


def lookup(quantity, family, rel):
    """Return (value, source) or (None, reason)."""
    name = REPO_TO_EPOCH.get(rel["model"], rel["model"])
    if quantity == "eci_public":
        with open(ROOT / "data/raw/eci_public.csv", newline="") as f:
            for r in csv.DictReader(f):
                if r["model"] == name:
                    return float(r["eci"]), "eci_public.csv"
        return None, "not in eci_public.csv yet"
    if quantity == "aeci_own_card":
        short = name.replace("Claude ", "")
        with open(ROOT / "data/raw/aeci_all.csv", newline="") as f:
            for r in csv.DictReader(f):
                if r["model"] == short and r["own_card"] == "1" and r["value_type"] == "printed":
                    return float(r["value"]), "aeci_all.csv (own card)"
        return None, "no own-card AECI row yet"
    charts = json.loads((REPO / "data/benchmarks.json").read_text())["charts"]
    if quantity in charts and "series" in charts[quantity]:
        for p in charts[quantity]["series"].get(family, []):
            if p.get("date") == rel["date"] and p.get("score") is not None:
                return float(p["score"]), f"data/benchmarks.json charts.{quantity}"
        return None, "no chart row yet"
    return None, "unknown quantity"


def main(argv):
    dry = "--dry-run" in argv
    releases = json.loads((REPO / "data/models.json").read_text())["releases"]
    card = ROOT / "scorecard.csv"
    done = set()
    if card.exists():
        with open(card, newline="") as f:
            done = {r["id"] for r in csv.DictReader(f)}
    new, pending = [], 0
    for snap in sorted((ROOT / "history").glob("predictions_*.json")):
        S = json.loads(snap.read_text())
        for p in S["open_predictions"]:
            if p["id"] in done:
                continue
            rel = next_release(releases, p["family"], S["as_of"])
            if rel is None:
                pending += 1
                continue
            val, src = lookup(p["quantity"], p["family"], rel)
            if val is None:
                pending += 1
                continue
            inside = lambda lo, hi: int(p[lo] <= val <= p[hi])
            new.append(dict(id=p["id"], issued=S["as_of"], family=p["family"], quantity=p["quantity"], model=rel["model"],
                            release_date=rel["date"], median=p["median"], lo50=p["lo50"], hi50=p["hi50"], lo80=p["lo80"],
                            hi80=p["hi80"], lo95=p["lo95"], hi95=p["hi95"], actual=val, error=round(val - p["median"], 3),
                            in50=inside("lo50", "hi50"), in80=inside("lo80", "hi80"), in95=inside("lo95", "hi95"),
                            graded_on=dt.date.today().isoformat(), source=src))
            done.add(p["id"])
    if new and not dry:
        exists = card.exists()
        with open(card, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            if not exists:
                w.writeheader()
            w.writerows(new)
    elif not card.exists() and not dry:
        with open(card, "w", newline="") as f:
            csv.DictWriter(f, fieldnames=FIELDS).writeheader()
    print(f"graded {len(new)} prediction(s){' (dry run)' if dry else ''}; {pending} still open")
    for r in new:
        print(f"  {r['id']}: predicted {r['median']} [{r['lo80']}, {r['hi80']}], actual {r['actual']} ({r['model']})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
