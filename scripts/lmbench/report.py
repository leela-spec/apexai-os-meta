"""Aggregation across trials into a `validated_profile_candidate`. Stdlib only.

Failed trials are never dropped -- `failed_trial_refs` names them (VAL-11).
`infra_invalid_rate` above 20% marks a fixture's result `INVALID` rather than
folding it into a pass rate: a flaky harness must not be able to launder
itself into "the model did fine" by inflating the denominator.

The harness computes `certification_eligible_task_classes` only, as a
deterministic consequence of the hard gates and the observed pass rate.
`certification_decision` is always `null` -- this module has no code path
that can write anything else, so a hard-gate-failing configuration cannot be
marked eligible regardless of how well it scores elsewhere (VAL-16).

At n=5, one observed failure is "one failure in five," not "80% reliable" --
`eligible` requires a clean run at the declared repeat count; anything less
is reported honestly, not smoothed into a percentage. A fixture with at least
one failure must be rerun at a larger n before its task class can be marked
eligible; this module does not do that rerun, it just refuses to call a
5-trial 4/5 result "eligible."
"""

from __future__ import annotations

from dataclasses import dataclass

from .verdict import ACTOR_FAIL, ACTOR_PASS, INFRA_INVALID

_INFRA_INVALID_THRESHOLD = 0.20


@dataclass(frozen=True, slots=True)
class FixtureAggregate:
    fixture_id: str
    total: int
    actor_pass: int
    actor_fail: int
    infra_invalid: int
    failed_trial_refs: tuple
    hard_gate_violations: int

    @property
    def infra_invalid_rate(self) -> float:
        return self.infra_invalid / self.total if self.total else 0.0

    @property
    def is_invalid(self) -> bool:
        return self.infra_invalid_rate > _INFRA_INVALID_THRESHOLD

    @property
    def valid_total(self) -> int:
        return self.total - self.infra_invalid

    @property
    def pass_rate(self) -> float | None:
        if self.valid_total == 0:
            return None
        return self.actor_pass / self.valid_total

    @property
    def eligible(self) -> bool:
        if self.is_invalid:
            return False
        if self.hard_gate_violations > 0:
            return False
        if self.valid_total == 0:
            return False
        return self.actor_pass == self.valid_total


def aggregate(fixture_id: str, verdicts) -> FixtureAggregate:
    verdicts = list(verdicts)
    total = len(verdicts)
    actor_pass = sum(1 for v in verdicts if v.verdict == ACTOR_PASS)
    actor_fail = sum(1 for v in verdicts if v.verdict == ACTOR_FAIL)
    infra_invalid = sum(1 for v in verdicts if v.verdict == INFRA_INVALID)
    failed_refs = tuple(sorted(v.trial_id for v in verdicts if v.verdict == ACTOR_FAIL))
    hard_gate_violations = sum(1 for v in verdicts if v.hard_gate_violation)
    return FixtureAggregate(
        fixture_id=fixture_id,
        total=total,
        actor_pass=actor_pass,
        actor_fail=actor_fail,
        infra_invalid=infra_invalid,
        failed_trial_refs=failed_refs,
        hard_gate_violations=hard_gate_violations,
    )


def emit_profile_candidate(*, configuration_id: str, fixture_aggregates: dict) -> dict:
    certification_eligible = sorted(
        fixture_id for fixture_id, agg in fixture_aggregates.items() if agg.eligible
    )
    failed_task_classes = sorted(
        fixture_id for fixture_id, agg in fixture_aggregates.items() if not agg.eligible
    )
    all_failed_refs: list = []
    for agg in fixture_aggregates.values():
        all_failed_refs.extend(agg.failed_trial_refs)

    return {
        "schema_version": 1,
        "profile_candidate_id": None,
        "configuration_id": configuration_id,
        "certified_task_classes": [],
        "failed_task_classes": failed_task_classes,
        "certification_eligible_task_classes": certification_eligible,
        "hard_gate_results": {
            fixture_id: {
                "hard_gate_violations": agg.hard_gate_violations,
                "infra_invalid_rate": agg.infra_invalid_rate,
            }
            for fixture_id, agg in fixture_aggregates.items()
        },
        "reliability": {
            fixture_id: {
                "total_trials": agg.total,
                "actor_pass": agg.actor_pass,
                "actor_fail": agg.actor_fail,
                "infra_invalid": agg.infra_invalid,
                "pass_rate": agg.pass_rate,
            }
            for fixture_id, agg in fixture_aggregates.items()
        },
        "failed_trial_refs": sorted(all_failed_refs),
        "evidence_status": "candidate",
        "certification_decision": None,
        "certification_authority": "downstream_operator",
    }


__all__ = ["FixtureAggregate", "aggregate", "emit_profile_candidate"]
