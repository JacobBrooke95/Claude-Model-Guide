#!/usr/bin/env python3
"""Regenerate the data blocks in claude-models.html and the forecast's release
table from the JSON files under data/.

    python3 scripts/build-site-data.py            # rewrite whatever is stale
    python3 scripts/build-site-data.py --check    # exit 1 if anything is stale
    python3 scripts/build-site-data.py --list     # show the generated regions

Sources (see data/README.md):
    data/models.json        families, every release, price fields
    data/benchmarks.json    every benchmark chart's rows, with provenance
    data/board-checks.json  third-party boards and per-(model, board) checks

Outputs:
    claude-models.html                    the regions between
                                          "// >>> generated:NAME" and
                                          "// <<< generated:NAME"
    forecast/data/anthropic_releases.csv  the whole file

The data stays inline in the page on purpose: scripts/predict-releases.js lifts
the release-data block out of the HTML and runs it, and forecast/engine/
backtest.py shells out to that script. A runtime fetch would break both.

Python rather than Node because the two other build steps (build-system-cards.py
and the pre-commit hook that calls this with --check) are Python, and the CSV
half needs no JS. Standard library only.
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGE = ROOT / "claude-models.html"
CSV = ROOT / "forecast" / "data" / "anthropic_releases.csv"
DATA = ROOT / "data"

CSV_COLUMNS = ["release_id", "date", "family", "model", "version", "generation", "access",
               "price_in", "price_out", "colaunch_group", "source_url", "note"]

# Provenance fields. They live in the JSON and are never written into the page.
META_KEYS = {"source", "source_url", "as_of", "note", "caveats", "derivation"}

# region name -> (benchmarks.json chart id, key inside the chart, JS const name)
CHART_REGIONS = [
    ("osworld",          "osworld",            "series", "benchmarkData"),
    ("vending-bench-2",  "vending_bench_2",    "series", "earningsData"),
    ("vending-arena",    "vending_bench_arena", "rounds", "rounds"),
    ("gdpval",           "gdpval_aa",          "series", "gdpvalData"),
    ("arc-agi-2",        "arc_agi_2",          "series", "arcData"),
    ("arc-agi-3",        "arc_agi_3",          "series", "arc3Data"),
    ("arc-agi-3-adapter", "arc_agi_3",         "adapter", "arc3Adapter"),
    ("hle",              "hle",                "series", "hleData"),
    ("aeci",             "aeci",               "points", "aeciData"),
    ("aeci-drift",       "aeci",               "drift",  "aeciDrift"),
    ("radar-axes",       "capability_profile", "axes",   "axes"),
    ("radar-models",     "capability_profile", "models", "models"),
    ("rli",              "rli",                "series", "rliData"),
    ("swe-bench-pro",    "swe_bench_pro",      "series", "sweData"),
    ("terminal-bench",   "terminal_bench_2_1", "series", "tbData"),
]

STATUSES = {"listed", "pending", "not_applicable", "uncheckable"}


class DataError(Exception):
    pass


def load(name: str):
    path = DATA / name
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise DataError(f"{path.relative_to(ROOT)}: {e}") from e


def check_date(value, where: str) -> str:
    try:
        if not isinstance(value, str) or datetime.date.fromisoformat(value).isoformat() != value:
            raise ValueError
    except ValueError:
        raise DataError(f"{where}: {value!r} is not a YYYY-MM-DD date") from None
    return value


def short(model: str) -> str:
    """'Claude Opus 5.5' -> 'Opus 5.5', the label the charts use."""
    return model[len("Claude "):] if model.startswith("Claude ") else model


# ---------------------------------------------------------------- JS output

IDENT = re.compile(r"^[A-Za-z_$][A-Za-z0-9_$]*$")


def js_scalar(v) -> str:
    if v is None:
        return "null"
    if v is True:
        return "true"
    if v is False:
        return "false"
    if isinstance(v, (int, float)):
        return repr(v)
    if isinstance(v, str):
        return "'" + v.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n") + "'"
    raise DataError(f"cannot write {type(v).__name__} as JS")


def js_inline(v) -> str:
    if isinstance(v, dict):
        if not v:
            return "{}"
        return "{ " + ", ".join(f"{js_key(k)}: {js_inline(x)}" for k, x in v.items()) + " }"
    if isinstance(v, list):
        return "[" + ", ".join(js_inline(x) for x in v) + "]"
    return js_scalar(v)


def js_key(k: str) -> str:
    return k if IDENT.match(k) else js_scalar(k)


def holds_rows(v) -> bool:
    """True when v contains a list of objects, which always gets one row per line."""
    if isinstance(v, list):
        return any(isinstance(x, (dict, list)) for x in v) or any(holds_rows(x) for x in v)
    if isinstance(v, dict):
        return any(holds_rows(x) for x in v.values())
    return False


def js(v, indent: str, width: int = 110) -> str:
    """Pretty-print v as a JS literal: leaf rows on one line, containers expanded."""
    if not isinstance(v, (dict, list)) or not v:
        return js_inline(v)
    one = js_inline(v)
    if not holds_rows(v) and (isinstance(v, dict) or len(indent) + len(one) <= width):
        return one  # a leaf row is one line however long; only containers expand
    inner = indent + "    "
    if isinstance(v, dict):
        body = ",\n".join(f"{inner}{js_key(k)}: {js(x, inner, width)}" for k, x in v.items())
        return "{\n" + body + "\n" + indent + "}"
    body = ",\n".join(f"{inner}{js(x, inner, width)}" for x in v)
    return "[\n" + body + "\n" + indent + "]"


def strip_meta(v):
    if isinstance(v, dict):
        return {k: strip_meta(x) for k, x in v.items() if k not in META_KEYS}
    if isinstance(v, list):
        return [strip_meta(x) for x in v]
    return v


# ------------------------------------------------------------------ releases

def validate_models(models) -> dict:
    fams = {f["key"] for f in models["families"]}
    by_id = {}
    for r in models["releases"]:
        where = f"models.json release {r.get('id')!r}"
        for k in ("id", "date", "family", "model", "version", "generation", "access", "url"):
            if k not in r:
                raise DataError(f"{where}: missing {k!r}")
        if r["id"] in by_id:
            raise DataError(f"{where}: duplicate id")
        check_date(r["date"], where)
        if r["family"] not in fams and r["family"] != "legacy":
            raise DataError(f"{where}: unknown family {r['family']!r}")
        if r["access"] not in ("ga", "restricted"):
            raise DataError(f"{where}: access must be 'ga' or 'restricted'")
        if (r.get("price_in") is None) != (r.get("price_out") is None):
            raise DataError(f"{where}: price_in and price_out must both be set or both null")
        by_id[r["id"]] = r
    dates = [r["date"] for r in models["releases"]]
    if dates != sorted(dates):
        raise DataError("models.json: releases must be in date order (the CSV is written in file order)")
    return by_id


def model_data(models) -> dict:
    """The page's modelData: one entry per family, releases in date order."""
    out = {}
    for fam in models["families"]:
        rows = []
        for r in models["releases"]:
            if r["family"] != fam["key"]:
                continue
            row = {"version": r.get("site_label", r["model"]), "date": r["date"]}
            flag = r.get("site_flag", "restricted" if r["access"] == "restricted" else None)
            if flag not in (None, "restricted", "notReleased"):
                raise DataError(f"models.json release {r['id']!r}: bad site_flag {flag!r}")
            if flag:
                row[flag] = True
            row["url"] = r["url"]
            rows.append(row)
        if not rows:
            raise DataError(f"models.json: family {fam['key']!r} has no releases")
        out[fam["key"]] = {"name": fam["name"], "tier": fam["tier"],
                           "headerClass": fam["headerClass"], "releases": rows}
    return out


def pricing_rows(models) -> list:
    """The pricing chart, derived from the release list.

    Per family: the bars are the newest generally available release's price; `prev`
    is the price the family carried before its most recent change, named after the
    last model that had it and dated to the first release at today's price.
    """
    rows = []
    for fam in models["pricing_chart"]["families"]:
        rel = [r for r in models["releases"]
               if r["family"] == fam and r["access"] == "ga" and r.get("price_in") is not None]
        if not rel:
            raise DataError(f"models.json pricing_chart: no priced GA release for {fam!r}")
        cur = rel[-1]
        price = (cur["price_in"], cur["price_out"])
        row = {"name": short(cur["model"]), "family": fam, "input": price[0], "output": price[1]}
        if cur.get("price_long"):
            row["long"] = cur["price_long"]
        i = len(rel) - 1
        while i > 0 and (rel[i - 1]["price_in"], rel[i - 1]["price_out"]) == price:
            i -= 1
        if i > 0:
            old = rel[i - 1]
            row["prev"] = {"model": short(old["model"]), "input": old["price_in"],
                           "output": old["price_out"], "until": rel[i]["date"]}
        rows.append(row)
    return rows


def csv_text(models) -> str:
    def cell(v, where):
        s = "" if v is None else (v if isinstance(v, str) else repr(v))
        # The file is written unquoted, as it always has been (pandas reads a quote in
        # mid-field literally). That only works while no field needs quoting.
        if "," in s or "\n" in s or "\r" in s or s.startswith('"'):
            raise DataError(f"{where}: {s!r} has a comma, newline or leading quote, "
                            "which the unquoted CSV cannot carry")
        return s

    lines = [",".join(CSV_COLUMNS)]
    for r in models["releases"]:
        where = f"models.json release {r['id']!r}"
        lines.append(",".join(cell(v, where) for v in (
            r["id"], r["date"], r["family"], r["model"], r["version"], r["generation"], r["access"],
            r.get("price_in"), r.get("price_out"), r.get("colaunch_group"), r["url"], r.get("note"))))
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- benchmarks

def validate_benchmarks(bench, models) -> None:
    release_date = {short(r["model"]): r["date"] for r in models["releases"]}
    release_date.update({r["site_label"]: r["date"] for r in models["releases"] if "site_label" in r})

    def rows_of(v):
        if isinstance(v, dict):
            if "model" in v and "date" in v:
                yield v
            for x in v.values():
                yield from rows_of(x)
        elif isinstance(v, list):
            for x in v:
                yield from rows_of(x)

    for cid, chart in bench["charts"].items():
        for row in rows_of(chart):
            where = f"benchmarks.json {cid} {row['model']!r}"
            check_date(row["date"], where)
            if "as_of" in row:
                check_date(row["as_of"], where + " as_of")
            want = release_date.get(row["model"])
            # A chart point sits at its model's release date. Arena rounds are dated by
            # round instead, so their entries carry no date and are not checked here.
            if want and want != row["date"]:
                raise DataError(f"{where}: date {row['date']} is not the release date {want} in models.json")


# ------------------------------------------------------------ board coverage

def board_coverage(checks_doc, models, by_id) -> dict:
    boards = checks_doc["boards"]
    board_ids = [b["id"] for b in boards]
    if len(set(board_ids)) != len(board_ids):
        raise DataError("board-checks.json: duplicate board id")
    for b in boards:
        for k in ("id", "name", "short", "url", "feeds", "tracked_since"):
            if k not in b:
                raise DataError(f"board-checks.json board {b.get('id')!r}: missing {k!r}")
        check_date(b["tracked_since"], f"board {b['id']} tracked_since")
        if b.get("last_checked"):
            check_date(b["last_checked"], f"board {b['id']} last_checked")
    board = {b["id"]: b for b in boards}

    explicit = {}
    for c in checks_doc["checks"]:
        where = f"board-checks.json check {c.get('model')!r} x {c.get('board')!r}"
        if c.get("model") not in by_id:
            raise DataError(f"{where}: no such release id in models.json")
        if c.get("board") not in board:
            raise DataError(f"{where}: no such board")
        if c.get("status") not in STATUSES:
            raise DataError(f"{where}: status must be one of {sorted(STATUSES)}")
        key = (c["model"], c["board"])
        if key in explicit:
            raise DataError(f"{where}: listed twice")
        released = by_id[c["model"]]["date"]
        for k in ("first_listed", "first_seen_by_site", "not_listed_as_of", "last_checked"):
            if c.get(k):
                check_date(c[k], f"{where} {k}")
        if c["status"] == "listed":
            if not (c.get("first_listed") or c.get("first_seen_by_site")):
                raise DataError(f"{where}: a listed row needs first_listed (a date the board or a "
                                "dated read establishes) or first_seen_by_site (an upper bound)")
            if c.get("first_listed") and not c.get("first_listed_basis"):
                raise DataError(f"{where}: first_listed needs first_listed_basis saying where the date comes from")
            if c.get("first_seen_by_site") and c["first_seen_by_site"] < released:
                raise DataError(f"{where}: first_seen_by_site is before the release date")
            if c.get("first_listed") and c.get("first_seen_by_site") and c["first_listed"] > c["first_seen_by_site"]:
                raise DataError(f"{where}: first_listed is after first_seen_by_site")
        elif c.get("first_listed") or c.get("first_seen_by_site") or c.get("value") is not None:
            raise DataError(f"{where}: only a listed row carries first_listed, first_seen_by_site or value")
        explicit[key] = c

    since = check_date(checks_doc["matrix"]["since"], "board-checks.json matrix.since")
    rows = []
    for r in models["releases"]:
        if r["family"] == "legacy":
            continue
        for b in boards:
            c = explicit.get((r["id"], b["id"]))
            if c is None:
                if r["date"] < b["tracked_since"]:
                    continue  # the site kept no record for this board that far back
                if r["access"] == "restricted":
                    c = {"status": "not_applicable",
                         "note": "Restricted access: third-party boards cannot run it."}
                else:
                    # A new release with no entry here yet: queued, never checked.
                    c = {"status": b.get("default_status", "pending"), "last_checked": None,
                         "note": "No check recorded yet."}
            status = c["status"]
            last = c["last_checked"] if "last_checked" in c else (
                b.get("last_checked") if status in ("pending", "listed") else None)
            if last and last < r["date"]:
                last = None  # a check made before the release says nothing about it
            rows.append({
                "model": r["id"], "board": b["id"], "status": status,
                "firstListed": c.get("first_listed"), "basis": c.get("first_listed_basis"),
                "firstSeen": c.get("first_seen_by_site"), "notListedAsOf": c.get("not_listed_as_of"),
                "lastChecked": last, "value": c.get("value"), "note": c.get("note"),
            })
    return {
        "matrixSince": since,
        "boards": [{"id": b["id"], "name": b["name"], "short": b["short"], "url": b["url"],
                    "feeds": b["feeds"], "lastChecked": b.get("last_checked")} for b in boards],
        "models": [{"id": r["id"], "label": short(r["model"]), "family": r["family"], "released": r["date"],
                    "restricted": r["access"] == "restricted"}
                   for r in models["releases"] if any(x["model"] == r["id"] for x in rows)],
        "rows": [{k: v for k, v in row.items() if v is not None or k == "lastChecked"} for row in rows],
    }


# ------------------------------------------------------------------- regions

def region_re(name: str) -> re.Pattern:
    return re.compile(
        r"^(?P<indent>[ \t]*)// >>> generated:" + re.escape(name) + r"(?=[ \n])[^\n]*\n"
        r"(?P<body>.*?)"
        r"^[ \t]*// <<< generated:" + re.escape(name) + r"[ \t]*\n",
        re.S | re.M)


def build_regions() -> tuple[dict, str]:
    models = load("models.json")
    bench = load("benchmarks.json")
    checks = load("board-checks.json")
    by_id = validate_models(models)
    validate_benchmarks(bench, models)

    regions = {
        "model-data": ("models.json", "modelData", model_data(models)),
        "pricing": ("models.json", "pricing", pricing_rows(models)),
        "board-coverage": ("board-checks.json + models.json", "BOARD_COVERAGE",
                           board_coverage(checks, models, by_id)),
    }
    for name, cid, key, const in CHART_REGIONS:
        try:
            value = bench["charts"][cid][key]
        except KeyError:
            raise DataError(f"benchmarks.json: charts.{cid}.{key} is missing") from None
        regions[name] = ("benchmarks.json", const, strip_meta(value))
    return regions, csv_text(models)


def render(page: str, regions: dict) -> str:
    for name, (src, const, value) in regions.items():
        pat = region_re(name)
        found = pat.findall(page)
        if len(found) != 1:
            raise DataError(f"claude-models.html: expected one generated:{name} region, found {len(found)}")

        def repl(m, name=name, src=src, const=const, value=value):
            ind = m.group("indent")
            return (f"{ind}// >>> generated:{name} from data/{src} by scripts/build-site-data.py. Do not edit here.\n"
                    f"{ind}const {const} = {js(value, ind)};\n"
                    f"{ind}// <<< generated:{name}\n")
        page = pat.sub(repl, page)
    stray = set(re.findall(r"// >>> generated:([\w-]+)", page)) - set(regions)
    if stray:
        raise DataError(f"claude-models.html: unknown generated region(s): {sorted(stray)}")
    return page


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--check", action="store_true", help="write nothing; exit 1 if an output is stale")
    ap.add_argument("--list", action="store_true", help="list the generated regions and exit")
    args = ap.parse_args()

    try:
        regions, csv_new = build_regions()
        page_old = PAGE.read_text(encoding="utf-8")
        page_new = render(page_old, regions)
    except DataError as e:
        print(f"build-site-data: {e}", file=sys.stderr)
        return 2

    if args.list:
        for name, (src, const, _) in regions.items():
            print(f"{name:18} const {const:15} <- data/{src}")
        print(f"{'(whole file)':18} {CSV.relative_to(ROOT)} <- data/models.json")
        return 0

    stale = []
    if page_new != page_old:
        old = {n: region_re(n).search(page_old).group(0) for n in regions}
        new = {n: region_re(n).search(page_new).group(0) for n in regions}
        stale.append(f"{PAGE.name} ({', '.join(n for n in regions if old[n] != new[n])})")
    if not CSV.exists() or CSV.read_text(encoding="utf-8") != csv_new:
        stale.append(str(CSV.relative_to(ROOT)))

    if args.check:
        if stale:
            print("build-site-data: stale, generated from data/*.json but out of date:", file=sys.stderr)
            for s in stale:
                print(f"  {s}", file=sys.stderr)
            print("  run: python3 scripts/build-site-data.py", file=sys.stderr)
            return 1
        print("build-site-data: up to date")
        return 0

    if page_new != page_old:
        PAGE.write_text(page_new, encoding="utf-8")
    if CSV in [ROOT / s for s in stale]:
        CSV.write_text(csv_new, encoding="utf-8")
    print("build-site-data: " + ("rewrote " + "; ".join(stale) if stale else "nothing to do"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
