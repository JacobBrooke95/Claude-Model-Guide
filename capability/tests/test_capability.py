"""Tests for the capability model. Run from the repo root:

    python3 -m unittest discover -s capability/tests -v

They read the committed outputs (run capability/run.py first) and re-check a few
properties directly against the code."""
import json
import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402

from capmodel.common import rng, yr  # noqa: E402
from capmodel.data import D  # noqa: E402


def strict(path):
    def bad(x):
        raise ValueError(x)
    return json.loads(Path(path).read_text(), parse_constant=bad)


class Outputs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.J = strict(ROOT / "output" / "capability_forecast.json")

    def test_json_is_strict_no_nan(self):
        txt = (ROOT / "output" / "capability_forecast.json").read_text()
        for tok in ("NaN", "Infinity"):
            self.assertNotIn(tok, txt)

        def walk(o):
            if isinstance(o, float):
                self.assertTrue(math.isfinite(o))
            elif isinstance(o, dict):
                for v in o.values():
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
        walk(self.J)

    def test_intervals_are_ordered(self):
        n = [0]

        def walk(o, path=""):
            if isinstance(o, dict):
                seq = [o.get(k) for k in ("lo95", "lo80", "lo50", "median", "hi50", "hi80", "hi95")]
                if all(isinstance(v, (int, float)) for v in seq):
                    self.assertTrue(all(a <= b + 1e-6 for a, b in zip(seq, seq[1:])), path)
                    n[0] += 1
                for k, v in o.items():
                    walk(v, path + "/" + k)
            elif isinstance(o, list):
                for i, v in enumerate(o):
                    walk(v, f"{path}[{i}]")
        walk(self.J)
        self.assertGreater(n[0], 500)

    def test_scenario_weights_sum_to_one(self):
        for name, w in self.J["projection"]["weights"].items():
            self.assertAlmostEqual(sum(w.values()), 1.0, places=3, msg=name)
            self.assertTrue(all(v >= 0 for v in w.values()))
        self.assertAlmostEqual(sum(self.J["backtest"]["release"]["live_trend_weights"].values()), 1.0, places=2)

    def test_no_future_data_in_any_release_fold(self):
        rows = self.J["backtest"]["release"]["per_release"]
        self.assertGreater(len(rows), 50)
        for r in rows:
            self.assertLess(r["cutoff"], r["t0"], r["fold"])      # newest model the fold saw precedes its origin
            self.assertLessEqual(r["t0"], r["t"] + 1e-9, r["fold"])  # origin is on or before the target's release
        for r in self.J["backtest"]["benchmarks"]["per_release"]:
            self.assertLess(r["cutoff"], r["t0"])

    def test_no_future_data_in_frontier_folds(self):
        self.assertGreater(self.J["backtest"]["frontier"]["min_cutoff_gap_days"], 0)

    def test_fold_refit_excludes_target_and_later_models(self):
        """Rebuild one fold from scratch and assert on dates directly."""
        from capmodel.core import OriginModel
        d = D()
        tgt = d.claude().query("model_id == 'Claude Opus 5'").iloc[0]
        om = OriginModel(d, tgt.t - 0.25, 5, rng("test"))
        self.assertLess(om.all.series.t.max(), tgt.t - 0.25)
        self.assertLess(om.anth.series.t.max(), tgt.t - 0.25)
        self.assertLess(om.hist.t.max(), tgt.t - 0.25)
        self.assertNotIn("Claude Opus 5", set(om.hist.model_id))
        self.assertNotIn("Claude Opus 5", set(om.all.series.names))

    def test_aeci_mapping_reproduces_overlap_within_stated_error(self):
        a = self.J["aeci"]
        sd = a["mapping_residual_sd_used"]
        p = a["p_offset_form_used"]
        res = [o["aeci"] - (p * o["fit_offset"] + (1 - p) * o["fit_hinge"]) for o in a["overlap"]]
        self.assertGreaterEqual(len(res), 12)
        rmse = math.sqrt(sum(x * x for x in res) / len(res))
        self.assertLessEqual(rmse, sd + 1e-6)                    # stated error is not smaller than the in-sample miss
        self.assertLessEqual(max(abs(x) for x in res), 3 * sd)   # no overlap model more than 3 sd away
        # and the stated error also covers the two site-rescaled values that were held out
        for e in a["out_of_sample_check_repo_rescaled"]:
            self.assertLessEqual(abs(e["repo_rescaled_aeci"] - (p * e["mapped_offset"] + (1 - p) * e["mapped_hinge"])), 3 * sd)

    def test_next_model_blocks_complete(self):
        fams = self.J["next_models"]["families"]
        self.assertEqual(set(fams), {"opus", "sonnet", "haiku", "fable", "mythos"})
        for f, v in fams.items():
            for k in ("eci", "aeci_nov6_scale", "aeci_own_card"):
                self.assertIsNotNone(v[k]["median"], f)
            self.assertGreaterEqual(v["aeci_own_card"]["hi80"] - v["aeci_own_card"]["lo80"],
                                    v["aeci_nov6_scale"]["hi80"] - v["aeci_nov6_scale"]["lo80"] - 1e-6)
            for b in v["benchmarks"].values():
                self.assertIsNotNone(b["median"])

    def test_bounded_benchmark_predictions_respect_bounds(self):
        links = {r["benchmark"]: r for r in self.J["links"]["table"]}
        for v in self.J["next_models"]["families"].values():
            for k, b in v["benchmarks"].items():
                if links[k]["kind"] == "bounded":
                    self.assertGreaterEqual(b["lo95"], links[k]["lo"] - 1e-6)
                    self.assertLessEqual(b["hi95"], links[k]["hi"] + 1e-6)

    def test_projection_bands_widen_and_medians_do_not_fall(self):
        b = self.J["projection"]["series"]["anthropic_frontier_eci"]["mixture"]
        med = [x["median"] for x in b]
        self.assertTrue(all(a <= c + 1e-6 for a, c in zip(med, med[1:])))
        self.assertGreater(b[-1]["hi80"] - b[-1]["lo80"], b[4]["hi80"] - b[4]["lo80"])

    def test_open_predictions_have_resolution_criteria(self):
        ids = set()
        for p in self.J["open_predictions"]:
            self.assertNotIn(p["id"], ids)
            ids.add(p["id"])
            self.assertTrue(p["resolution"] and p["applies_to"])
            self.assertLessEqual(p["lo80"], p["median"])


class Units(unittest.TestCase):
    def test_records_are_a_running_max(self):
        from capmodel.trend import records
        t = np.array([1.0, 2, 3, 4, 5])
        y = np.array([10.0, 9, 12, 11, 15])
        self.assertEqual(list(records(t, y)), [0, 2, 4])

    def test_release_date_sampler_matches_forecaster_median(self):
        from capmodel.predict import ReleaseDates
        from capmodel.common import to_date
        rd = ReleaseDates()
        for f in ("opus", "sonnet", "haiku", "fable", "mythos"):
            days = rd.sample_days(f, 40000, rng("t" + f))
            target = (to_date(rd.fc["targets"][f]["with_signals"]["median"]) - rd.as_of).days
            self.assertLess(abs(float(np.median(days)) - target), 6, f)

    def test_data_layer_has_no_duplicate_scores_and_keeps_provenance(self):
        d = D()
        self.assertFalse(d.bench.duplicated(["benchmark", "model_id"]).any())
        self.assertTrue(d.bench.source.notna().all())
        self.assertTrue(d.models.model_id.is_unique)

    def test_grade_dry_run(self):
        import grade
        self.assertEqual(grade.main(["--dry-run"]), 0)


if __name__ == "__main__":
    unittest.main()
