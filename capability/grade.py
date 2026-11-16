#!/usr/bin/env python3
"""Grade open predictions whose release has shipped.

Reads every snapshot in capability/history/predictions_*.json (snapshots marked
"withdrawn" are kept for the record and never graded). For each open prediction it finds
the first release of that family after the snapshot date in data/models.json and looks
the realised value up in the current data.

  first published value  The first time a value is seen for (quantity, model) it is written
                         to history/first_values.csv; grading always uses that stored
                         value, so later refits of ECI or AECI cannot move a grade.
  expiry                 A prediction with no resolvable value by its `expires` date is
                         recorded as expired (not dropped), so the scorecard is not
                         survivorship-selected.

Appends one row per newly resolved or expired prediction to capability/scorecard.csv.
Safe to run daily.

    python3 capability/grade.py [--dry-run] [--today YYYY-MM-DD]
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

FIELDS = ["id", "status", "issued", "entity", "family", "quantity", "model", "release_date", "median", "lo50", "hi50", "lo80", "hi80",
          "lo95", "hi95", "actual", "error", "in50", "in80", "in95", "value_first_seen", "graded_on", "source"]
FIRST = ROOT / "history" / "first_values.csv"


def next_release(releases, family, issued):
    c = sorted((r for r in releases if r["family"] == family and r["date"] > issued), key=lambda r: r["date"])
    return c[0] if c else None


def lookup(quantity, family, rel):
    """Current value in the data -> (value, source) or (None, reason)."""
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
        norm = lambda x: "".join(ch for ch in str(x).lower().replace("claude", "") if ch.isalnum())
        want = norm(rel["model"])
        for p in charts[quantity]["series"].get(family, []):      # match on the model's name; the chart's date may differ by a day or two
            if p.get("score") is not None and (norm(p.get("model", "")) == want or norm(p.get("label", "")) == want):
                return float(p["score"]), f"data/benchmarks.json charts.{quantity}.series.{family}"
        return None, "no chart row yet"
    return None, "unknown quantity"


def load_first():
    out = {}
    if FIRST.exists():
        with open(FIRST, newline="") as f:
            for r in csv.DictReader(f):
                out[(r["quantity"], r["model"])] = (float(r["value"]), r["first_seen"], r["source"])
    return out


def main(argv):
    dry = "--dry-run" in argv
    today = dt.date.fromisoformat(argv[argv.index("--today") + 1]) if "--today" in argv else dt.date.today()
    releases = json.loads((REPO / "data/models.json").read_text())["releases"]
    card = ROOT / "scorecard.csv"
    done = set()
    if card.exists():
        with open(card, newline="") as f:
            done = {r["id"] for r in csv.DictReader(f)}
    first = load_first()
    new_first, new, pending, withdrawn = [], [], 0, 0
    for snap in sorted((ROOT / "history").glob("predictions_*.json")):
        S = json.loads(snap.read_text())
        if S.get("withdrawn"):
            withdrawn += len(S["open_predictions"])
            continue
        for p in S["open_predictions"]:
            if p["id"] in done:
                continue
            rel = next_release(releases, p["family"], S["as_of"])
            val = src = seen = None
            if rel is not None:
                key = (p["quantity"], rel["model"])
                if key in first:
                    val, seen, src = first[key]
                else:
                    val, src = lookup(p["quantity"], p["family"], rel)
                    if val is not None:
                        seen = today.isoformat()
                        first[key] = (val, seen, src)
                        new_first.append(dict(quantity=key[0], model=key[1], value=val, first_seen=seen, source=src))
            row = dict(id=p["id"], issued=S["as_of"], entity=p.get("entity", p["family"]), family=p["family"], quantity=p["quantity"],
                       model=rel["model"] if rel else "", release_date=rel["date"] if rel else "",
                       **{k: p[k] for k in ("median", "lo50", "hi50", "lo80", "hi80", "lo95", "hi95")}, graded_on=today.isoformat())
            if val is not None:
                inside = lambda lo, hi: int(p[lo] <= val <= p[hi])
                new.append(dict(row, status="resolved", actual=val, error=round(val - p["median"], 3), in50=inside("lo50", "hi50"),
                                in80=inside("lo80", "hi80"), in95=inside("lo95", "hi95"), value_first_seen=seen, source=src))
            elif p.get("expires") and today.isoformat() > p["expires"]:
                new.append(dict(row, status="expired", source="no value published by " + p["expires"]))
            else:
                pending += 1
                continue
            done.add(p["id"])
    if not dry:
        if new_first:
            ex = FIRST.exists()
            with open(FIRST, "a", newline="") as f:
                w = csv.DictWriter(f, fieldnames=["quantity", "model", "value", "first_seen", "source"])
                if not ex:
                    w.writeheader()
                w.writerows(new_first)
        ex = card.exists()
        with open(card, "a", newline="") as f:
            w = csv.DictWriter(f, fieldnames=FIELDS)
            if not ex:
                w.writeheader()
            w.writerows(new)
    print(f"graded {sum(r['status'] == 'resolved' for r in new)}, expired {sum(r['status'] == 'expired' for r in new)}"
          f"{' (dry run)' if dry else ''}; {pending} still open; {withdrawn} withdrawn predictions on file, not graded")
    for r in new:
        if r["status"] == "resolved":
            print(f"  {r['id']}: predicted {r['median']} [{r['lo80']}, {r['hi80']}], actual {r['actual']} ({r['model']})")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
