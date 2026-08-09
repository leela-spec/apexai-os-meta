"""VAL-11 (failed trials survive aggregation and are named) and VAL-16 (a
hard-gate failure blocks eligibility regardless of how good the pass rate
looks otherwise)."""

from __future__ import annotations

import unittest

from scripts.lmbench import report, verdict


def _verdict(trial_id, v, hard_gate_violation=False):
    return verdict.TrialVerdict(
        trial_id=trial_id, fixture_id="F1", verdict=v,
        hard_gate_violation=hard_gate_violation, grader_results=(),
    )


class TestVAL11FailedTrialsSurvive(unittest.TestCase):
    def test_failed_trial_is_named_not_averaged_away(self):
        verdicts = [
            _verdict("T1", verdict.ACTOR_PASS),
            _verdict("T2", verdict.ACTOR_PASS),
            _verdict("T3", verdict.ACTOR_FAIL),
            _verdict("T4", verdict.ACTOR_PASS),
            _verdict("T5", verdict.ACTOR_PASS),
        ]
        agg = report.aggregate("F1", verdicts)
        self.assertEqual(agg.total, 5)
        self.assertEqual(agg.actor_pass, 4)
        self.assertEqual(agg.actor_fail, 1)
        self.assertIn("T3", agg.failed_trial_refs)
        self.assertEqual(len(agg.failed_trial_refs), 1)

    def test_infra_invalid_trials_excluded_from_pass_rate_denominator(self):
        verdicts = [
            _verdict("T1", verdict.ACTOR_PASS),
            _verdict("T2", verdict.INFRA_INVALID),
        ]
        agg = report.aggregate("F1", verdicts)
        self.assertEqual(agg.valid_total, 1)
        self.assertEqual(agg.pass_rate, 1.0)

    def test_high_infra_invalid_rate_marks_fixture_invalid_not_averaged_in(self):
        verdicts = [_verdict("T1", verdict.ACTOR_PASS)] + [
            _verdict(f"T{i}", verdict.INFRA_INVALID) for i in range(2, 6)
        ]
        agg = report.aggregate("F1", verdicts)  # 4/5 infra invalid = 80%
        self.assertTrue(agg.is_invalid)
        self.assertFalse(agg.eligible)


class TestVAL16HardGateBlocksEligibility(unittest.TestCase):
    def test_hard_gate_violation_blocks_eligibility_even_with_perfect_pass_rate(self):
        verdicts = [_verdict(f"T{i}", verdict.ACTOR_PASS) for i in range(5)]
        # One of them is flagged hard_gate_violation even though it's recorded ACTOR_PASS
        # in this synthetic scenario is not realistic (hard gate violations are ACTOR_FAIL
        # per verdict.combine), but the aggregate must still refuse eligibility if the
        # violation counter is nonzero for any reason.
        verdicts[2] = _verdict("T2", verdict.ACTOR_FAIL, hard_gate_violation=True)
        agg = report.aggregate("F1", verdicts)
        self.assertGreater(agg.hard_gate_violations, 0)
        self.assertFalse(agg.eligible)

    def test_eligibility_unaffected_by_utility_only_by_gates_and_completeness(self):
        # 5/5 clean pass -> eligible.
        clean = report.aggregate("F1", [_verdict(f"T{i}", verdict.ACTOR_PASS) for i in range(5)])
        self.assertTrue(clean.eligible)
        # 4/5 pass, no hard gate violation -> NOT eligible (n=5 discipline: one
        # observed failure blocks eligibility until a larger rerun, regardless
        # of how good 80% "looks").
        verdicts = [_verdict(f"T{i}", verdict.ACTOR_PASS) for i in range(4)] + [
            _verdict("T5", verdict.ACTOR_FAIL)
        ]
        four_of_five = report.aggregate("F1", verdicts)
        self.assertFalse(four_of_five.eligible)

    def test_certification_decision_is_always_null(self):
        agg = report.aggregate("F1", [_verdict(f"T{i}", verdict.ACTOR_PASS) for i in range(5)])
        candidate = report.emit_profile_candidate(
            configuration_id="CFG-8B-VULKAN-01", fixture_aggregates={"F1": agg}
        )
        self.assertIsNone(candidate["certification_decision"])
        self.assertIn("F1", candidate["certification_eligible_task_classes"])

    def test_single_trial_pass_is_not_eligible_one_lucky_run_is_not_a_certification(self):
        # Found the hard way in this initiative's own first real bake-off:
        # n=1 all-pass must NOT read as eligible, or a single lucky trial is
        # indistinguishable from a validated capability.
        one_clean_trial = report.aggregate("F1", [_verdict("T1", verdict.ACTOR_PASS)])
        self.assertEqual(one_clean_trial.actor_pass, one_clean_trial.valid_total)  # looks "clean"
        self.assertFalse(one_clean_trial.eligible)

        two_clean_trials = report.aggregate(
            "F1", [_verdict("T1", verdict.ACTOR_PASS), _verdict("T2", verdict.ACTOR_PASS)]
        )
        self.assertFalse(two_clean_trials.eligible)

        three_clean_trials = report.aggregate(
            "F1", [_verdict(f"T{i}", verdict.ACTOR_PASS) for i in range(3)]
        )
        self.assertTrue(three_clean_trials.eligible)

    def test_certification_decision_null_even_when_nothing_is_eligible(self):
        bad_agg = report.aggregate(
            "F1",
            [_verdict("T1", verdict.ACTOR_FAIL, hard_gate_violation=True)],
        )
        candidate = report.emit_profile_candidate(
            configuration_id="CFG-8B-VULKAN-01", fixture_aggregates={"F1": bad_agg}
        )
        self.assertIsNone(candidate["certification_decision"])
        self.assertEqual(candidate["certification_eligible_task_classes"], [])
        self.assertIn("F1", candidate["failed_task_classes"])


if __name__ == "__main__":
    unittest.main()
