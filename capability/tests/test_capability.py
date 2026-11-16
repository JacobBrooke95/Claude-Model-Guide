"""Tests for the capability model (v2). Run from the repo root:

    python3 -m unittest discover -s capability/tests -v

They read the committed outputs (run capability/run.py first) and re-derive the properties
they check from the raw tables or by re-running pieces of the model; none of them only
re-reads a value the pipeline wrote about itself."""
import json
import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent
sys.path.insert(0, str(ROOT))

import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from capmodel.common import rng, yr, AS_OF  # noqa: E402
from capmodel.data import D  # noqa: E402

SEQ = ("lo95", "lo80", "lo50", "median", "hi50", "hi80", "hi95")


def strict(path):
    def bad(x):
        raise ValueError(x)
    return json.loads(Path(path).read_text(), parse_constant=bad)


class Outputs(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.J = strict(ROOT / "output" / "capability_forecast.json")
        cls.d = D()

    def test_json_is_strict_and_intervals_ordered(self):
        txt = (ROOT / "output" / "capability_forecast.json").read_text()
        self.assertNotIn("NaN", txt)
        self.assertNotIn("Infinity", txt)
        n = [0]

        def walk(o, path=""):
            if isinstance(o, float):
                self.assertTrue(math.isfinite(o), path)
            elif isinstance(o, dict):
                seq = [o.get(k) for k in SEQ]
                if all(isinstance(v, (int, float)) for v in seq):
                    self.assertTrue(all(a <= b + 1e-6 for a, b in zip(seq, seq[1:])), path)
                    n[0] += 1
                for k, v in o.items():
                    walk(v, path + "/" + k)
            elif isinstance(o, list):
                for i, v in enumerate(o):
                    walk(v, f"{path}[{i}]")
        walk(self.J)
        self.assertGreater(n[0], 300)

    def test_scenario_weights_sum_to_one(self):
        for name, w in self.J["projection"]["weights"].items():
            self.assertAlmostEqual(sum(w.values()), 1.0, places=3, msg=name)
            self.assertTrue(all(v >= 0 for v in w.values()))

    def test_fold_cutoffs_recomputed_from_the_models_table(self):
        """Independent of the pipeline's own bookkeeping: for every release fold, recompute
        from data/models.csv the newest Anthropic model released before the origin and
        require it to match the fold's recorded cut-off and to precede the origin."""
        m = pd.read_csv(ROOT / "data" / "models.csv")
        m = m[(m.in_public_eci == 1) & (m.lab == "Anthropic")]
        t = m.release_date.map(yr).to_numpy()
        rows = self.J["backtest"]["release"]["per_release"]
        self.assertGreater(len(rows), 100)
        for r in rows:
            before = t[t < r["t0"] - 1e-4]      # t0 is stored rounded to 5 decimals
            self.assertLess(before.max(), r["t0"])
            self.assertAlmostEqual(before.max(), r["cutoff"], places=4, msg=r["fold"])
            self.assertLessEqual(r["t0"], r["t"] + 1e-6)
            tgt_t = yr(m[m.model_id == r["model_id"]].release_date.iloc[0])
            self.assertGreaterEqual(tgt_t, r["t0"] - 1e-4, r["fold"])       # the target itself is not in the fold's data

    def test_future_data_cannot_change_a_fold(self):
        """Perturb every model released on or after the origin (ability +40, dates intact)
        and require the fitted level process to be bit-identical."""
        from capmodel.level import LevelProcess, WEIGHTS
        from capmodel.trend import Series
        for which in ("anthropic", "all"):
            t0 = 2026.2
            s1 = self.d.series(which)
            s2 = Series(s1.t.copy(), s1.Y + 40.0 * (s1.t >= t0)[:, None], s1.y + 40.0 * (s1.t >= t0), s1.names, s1.start)
            out = []
            for s in (s1, s2):
                lp = LevelProcess(s, t0, 10, rng("leak-" + which))
                P = lp.paths(500, WEIGHTS["central"], t0 + 1.0)
                out.append((P["level"].copy(), lp.F0, lp.sigma_w))
            self.assertTrue(np.array_equal(out[0][0], out[1][0]), which)
            self.assertEqual(out[0][1:], out[1][1:])

    def test_machine_folds_precede_their_targets(self):
        m = pd.read_csv(ROOT / "data" / "models.csv")
        t_all = m[m.in_public_eci == 1].release_date.map(yr).to_numpy()
        for key in ("all_lab", "anthropic"):
            for f in self.J["backtest"]["machine"][key]["per_fold"]:
                self.assertLess(f["cutoff"], f["t0"])
                self.assertAlmostEqual(f["t0"] + f["h"], f["t"], places=2)
                self.assertLessEqual(f["cutoff"], t_all[t_all < f["t0"]].max() + 1e-4)

    def test_mapping_error_holds_leave_one_out(self):
        """Refit the ECI->AECI mapping without each overlap model in turn and check the
        stated residual sd against the errors on the left-out model."""
        from capmodel import aeci
        a = self.J["aeci"]["nov6_mapping"]
        tab = pd.DataFrame(a["overlap"])
        p, sd = a["p_level_shift_form"], a["residual_sd_used"]
        errs = []
        for i in range(len(tab)):
            keep = np.arange(len(tab)) != i
            e = []
            for form in ("hinge", "offset"):
                q = aeci._fit(tab.eci.to_numpy()[keep], tab.aeci.to_numpy()[keep], form)
                x = max(tab.eci[i] - q["k"], 0.0) if form == "hinge" else float(tab.eci[i] > q["k"])
                e.append(tab.aeci[i] - (q["a0"] + tab.eci[i] + q["c"] * x))
            errs.append((1 - p) * e[0] + p * e[1])
        errs = np.abs(errs)
        self.assertGreaterEqual(len(errs), 12)
        self.assertGreaterEqual(float(np.mean(errs <= 1.2816 * sd)), 0.7)     # ~80% nominal
        self.assertLessEqual(float(errs.max()), 3 * sd)

    def test_fable_and_mythos_are_one_entity(self):
        ents = self.J["next_models"]["entities"]
        self.assertEqual(set(ents), {"opus", "sonnet", "haiku", "fable_mythos"})
        ops = [p for p in self.J["open_predictions"] if p["entity"] == "fable_mythos"]
        self.assertEqual({p["family"] for p in ops if p["quantity"] == "eci_public"}, {"fable"})
        self.assertEqual({p["family"] for p in ops if p["quantity"] == "aeci_own_card"}, {"mythos"})
        self.assertFalse([p for p in self.J["open_predictions"] if p["family"] == "mythos" and p["quantity"] not in ("aeci_own_card",)])

    def test_regression_is_rare_but_possible(self):
        cl = self.d.claude().sort_values("t")
        steps = cl.groupby("family").eci.diff().dropna()
        self.assertEqual(int((steps < 0).sum()), 0)                      # the record the model is built on
        for e, v in self.J["next_models"]["entities"].items():
            self.assertGreater(v["p_regression_below_predecessor"], 0.0, e)
            self.assertLess(v["p_regression_below_predecessor"], 0.10, e)
            self.assertGreater(v["eci"]["median"], v["previous_eci"], e)

    def test_benchmark_predictions_do_not_contradict_observed_scores(self):
        """For every published benchmark prediction:
        (i)  all interval ends lie in the feasible range;
        (ii) the 95% upper bound is not below the best score the same family has already
             achieved (with lower-capability models);
        (iii) the 95% lower bound is not above the best score achieved by any model at least
             as capable as the low end (95%) of the entity's predicted ECI, when one exists."""
        b = self.d.bench
        meta = self.d.meta.set_index("benchmark")
        fam = {"opus": "opus", "sonnet": "sonnet", "haiku": "haiku", "fable_mythos": "fable"}
        n = 0
        for e, v in self.J["next_models"]["entities"].items():
            for k, p in v["benchmarks"].items():
                if not p.get("available"):
                    continue
                n += 1
                if meta.loc[k, "kind"] == "bounded":
                    self.assertGreaterEqual(p["lo95"], meta.loc[k, "lo"] - 1e-6, (e, k))
                    self.assertLessEqual(p["hi95"], meta.loc[k, "hi"] + 1e-6, (e, k))
                own = b[(b.benchmark == k) & (b.family == fam[e])]
                self.assertGreaterEqual(p["hi95"], own.value.max() - 1e-6, (e, k))
                peers = b[(b.benchmark == k) & (b.eci >= v["eci"]["lo95"])]
                if len(peers):
                    self.assertLessEqual(p["lo95"], peers.value.max() + 1e-6, (e, k))
        self.assertGreater(n, 15)

    def test_saturated_families_get_statements_not_numbers(self):
        b = self.d.bench
        links = {r["benchmark"]: r for r in self.J["links"]["table"]}
        fam = {"opus": "opus", "sonnet": "sonnet", "haiku": "haiku", "fable_mythos": "fable"}
        for e, v in self.J["next_models"]["entities"].items():
            for k, p in v["benchmarks"].items():
                r = links[k]
                if r["kind"] != "bounded" or not p.get("available"):
                    continue
                prev = b[(b.benchmark == k) & (b.family == fam[e])].sort_values("t").value.iloc[-1]
                self.assertLess((prev - r["lo"]) / (r["ceiling"] - r["lo"]), 0.9, (e, k))
        for r in self.J["links"]["table"]:
            if r["kind"] == "bounded":
                self.assertGreaterEqual(r["ceiling"], r["best_observed"] - 1e-6, r["benchmark"])   # no ceiling below an observed score

    def test_open_predictions_can_resolve(self):
        charts = json.loads((REPO / "data" / "benchmarks.json").read_text())["charts"]
        ids = set()
        for p in self.J["open_predictions"]:
            self.assertNotIn(p["id"], ids)
            ids.add(p["id"])
            self.assertTrue(p["resolution_source"] and p["resolution"] and p["expires"] > AS_OF)
            if p["quantity"] in charts:
                srs = charts[p["quantity"]]["series"].get(p["family"], [])
                self.assertTrue(srs, p["id"])
                age = (pd.Timestamp(AS_OF) - pd.Timestamp(max(x["date"] for x in srs))).days
                self.assertLessEqual(age, 183, p["id"])                  # the series is still being reported for this family

    def test_frontier_floor_is_not_degenerate_and_scale_is_flagged(self):
        b = self.J["projection"]["series"]["anthropic_frontier_eci"]
        self.assertLess(b[0]["lo95"], b[0]["median"])
        thr = self.J["scale"]["beyond_measured_scale_above_eci"]
        for row in b:
            self.assertEqual(row["median_beyond_measured_scale"], row["median"] > thr)
        self.assertNotIn("anthropic_frontier_metr_h50_hours", self.J["projection"]["series"])
        self.assertFalse(self.J["projection"]["metr_horizon"]["implied_horizon_published"])

    def test_both_layers_share_one_level_process(self):
        """The next-model forecast for the family that sets the frontier must sit inside the
        frontier band at its median release date (v1's two layers disagreed by ~3 points)."""
        v = self.J["next_models"]["entities"]["fable_mythos"]
        tq = [yr(q) for q in self.J["projection"]["quarters"]]
        b = self.J["projection"]["series"]["anthropic_frontier_eci"]
        j = int(np.argmin([abs(t - yr(v["release_date"]["median"])) for t in tq]))
        self.assertLessEqual(b[j]["lo95"], v["eci"]["median"])
        self.assertGreaterEqual(b[j]["hi95"], v["eci"]["median"])

    def test_headline_block(self):
        h = self.J["headline"]
        self.assertEqual(len(h["families"]), 4)
        self.assertEqual(len(h["frontier"]), 5)
        self.assertTrue(h["validated_through"] and h["beyond_measured_scale_above"] and h["display_cap_eci"])
        for f in h["families"]:
            self.assertLessEqual(len(f["benchmarks"]), 3)


class Units(unittest.TestCase):
    def test_irt_vintage_cache_matches_a_fresh_refit(self):
        from capmodel import irt
        d = D()
        pub = d.eci_models.set_index("model_id").eci
        df = pd.read_csv(ROOT / "data" / irt.VINTAGE_FILE)
        obs = irt.load_inputs()
        for k in (sorted(df.date.unique())[5], sorted(df.date.unique())[-1]):
            fresh = irt.fit_irt(obs[obs.t <= k + irt.DATE_TOL], pub)[0].round(3)
            cached = df[df.date == k].set_index("model").ability
            self.assertEqual(set(fresh.index), set(cached.index))
            self.assertLess(float((fresh - cached[fresh.index]).abs().max()), 0.01)
        # the target of each release-date vintage is in its own vintage (the v1 bug)
        last = d.claude().sort_values("t").iloc[-1]
        self.assertIn(last.model_id, set(df[df.date == round(float(last.t), 4)].model))

    def test_name_matcher_keeps_dated_variants_apart(self):
        import build_data as bd
        m = pd.read_csv(ROOT / "data" / "models.csv")
        f = bd.make_matcher(list(m.model_id))
        self.assertEqual(f("Claude 3.5 Sonnet (20241022)"), "Claude 3.5 Sonnet (October 2024)")
        self.assertEqual(f("claude-3-5-sonnet-20241022"), "Claude 3.5 Sonnet (October 2024)")
        self.assertEqual(f("claude-3-5-sonnet-20240620"), "Claude 3.5 Sonnet")
        self.assertEqual(f("Claude Opus 5.5 (Max)"), "Claude Opus 5.5")
        for name in ("Mistral Large (2411)", "DeepSeek-R1 (0528)", "Claude Opus 5.5 (preview 2)"):
            got = f(name)
            self.assertTrue(got is None or bd._n(got) == bd._n(name), (name, got))   # never merged into a sibling
        log = pd.read_csv(ROOT / "data" / "build_log.csv")
        self.assertGreater(int((log.step == "name_match").sum()), 20)                # merges are logged

    def test_release_date_sampler_matches_forecaster_median(self):
        from capmodel.predict import ReleaseDates
        from capmodel.common import to_date
        rd = ReleaseDates()
        for fam in ("opus", "sonnet", "haiku", "fable"):
            days = rd.sample_days(fam, 40000, rng("t" + fam))
            target = (to_date(rd.fc["targets"][fam]["with_signals"]["median"]) - rd.as_of).days
            self.assertLess(abs(float(np.median(days)) - target), 6, fam)

    def test_step_model_is_positive_before_measurement_noise(self):
        from capmodel import families as fam
        g = fam.predict_step(170.0, np.linspace(-2, 8, 2000), 0.0, 0.6, 0.0, rng("step"))
        self.assertGreaterEqual(float(g.min()), 170.0)

    def test_grading_first_value_and_expiry(self):
        import grade
        self.assertEqual(grade.main(["--dry-run"]), 0)
        import io
        import contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            grade.main(["--dry-run", "--today", "2029-01-01"])
        self.assertIn("expired 27", buf.getvalue().replace("expired %d" % 0, "x"))


if __name__ == "__main__":
    unittest.main()
