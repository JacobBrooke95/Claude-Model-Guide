#!/usr/bin/env python3
"""One command: data layer -> backtests -> fit -> next-model predictions -> projection ->
JSON, plots and METHODS.md.

    python3 capability/run.py            regenerate everything (about 1-2 minutes)
    python3 capability/run.py --full     rebuild data/irt_vintages.csv.gz (the leave-future-out IRT refits) from scratch
    python3 capability/run.py --check    verify the outputs are current and well-formed (no recompute)
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from capmodel.common import OUT, ROOT  # noqa: E402


def _strict_load(path):
    def bad(x):
        raise ValueError(f"non-strict JSON constant {x}")
    return json.loads(Path(path).read_text(), parse_constant=bad)


def _walk_intervals(o, path="", errs=None):
    errs = [] if errs is None else errs
    if isinstance(o, dict):
        seq = [o.get(k) for k in ("lo95", "lo80", "lo50", "median", "hi50", "hi80", "hi95")]
        if all(isinstance(v, (int, float)) for v in seq) and any(a > b + 1e-6 for a, b in zip(seq, seq[1:])):
            errs.append(path)
        for k, v in o.items():
            _walk_intervals(v, path + "/" + str(k), errs)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            _walk_intervals(v, f"{path}[{i}]", errs)
    return errs


def check():
    from capmodel.report import input_hash
    f = OUT / "capability_forecast.json"
    problems = []
    if not f.exists():
        print("FAIL: output/capability_forecast.json is missing")
        return 1
    J = _strict_load(f)
    if J["metadata"]["input_hash"] != input_hash():
        problems.append("outputs are stale: inputs or code changed since the last run (re-run capability/run.py)")
    bad = _walk_intervals(J)
    if bad:
        problems.append(f"{len(bad)} interval blocks out of order, e.g. {bad[:3]}")
    for p in J["open_predictions"]:
        if not p.get("resolution_source") or not p.get("expires"):
            problems.append(f"open prediction {p['id']} lacks a resolution source or expiry")
    for name, w in J["projection"]["weights"].items():
        if abs(sum(w.values()) - 1) > 1e-3:
            problems.append(f"scenario weights '{name}' sum to {sum(w.values())}")
    for p in J["metadata"]["plots"]:
        if not (OUT / p).exists():
            problems.append(f"missing plot {p}")
    if not (ROOT / "METHODS.md").exists():
        problems.append("METHODS.md missing")
    if problems:
        for p in problems:
            print("FAIL:", p)
        return 1
    print(f"OK: outputs current (as_of {J['metadata']['as_of']}, {len(J['open_predictions'])} open predictions, strict JSON)")
    return 0


def main(argv):
    if "--check" in argv:
        return check()
    import build_data
    from capmodel import pipeline, report, plots
    build_data.main()
    R = pipeline.run(full="--full" in argv)
    names = plots.make_all(R)
    J = report.build_json(R, names)
    report.write_methods(_strict_load(OUT / "capability_forecast.json"))
    # snapshot of the open predictions for later grading (one file per as_of date)
    from capmodel.common import dump_json, AS_OF, MODEL_VERSION
    dump_json(dict(as_of=AS_OF, model_version=MODEL_VERSION, open_predictions=J["open_predictions"]),
              ROOT / "history" / f"predictions_{AS_OF}_{MODEL_VERSION}.json")
    print(f"wrote output/capability_forecast.json, METHODS.md and {len(names)} plots")
    return check()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
