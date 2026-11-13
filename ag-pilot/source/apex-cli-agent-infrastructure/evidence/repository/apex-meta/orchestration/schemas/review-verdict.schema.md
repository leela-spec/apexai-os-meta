---
title: "Review Input & Verdict Schema (Claude-only adaptation)"
purpose: >
  Schemas for the two-lens Detective review: the blind input packet each reviewer
  receives and the verdict it must return. Adapted from the external deep-research
  answer on adversarial-review wiring; the different-model-family validity judge was
  REMOVED per operator direction (no external calls) — compensating controls are the
  falsification contract and the evidence-bearing PASS gate.
created: 2026-07-11
source: >
  apex-meta/fable-orchestrator/prompts/PromptAnswers/Adversarial-review wiring… (DEEP).md §2,
  ground-checked in prompts/PromptAnswers/research-integration-note.md §2.
---

# Review Input & Verdict Schema

## Review input packet (built by Meta Ops, one per lens)

```yaml
review_input_packet:
  schema_version: "apex.review.input.v1"
  run_id: string
  review_id: string
  review_lens: validity | strategic_alignment
  artifact:
    path: string
    version: integer            # ≥1, immutable versions — corrections create vN+1
    sha256: string              # review binds to the hash, not the filename
    declared_scope: [string]
  criteria:                     # ≥1; criterion-level review, not one holistic score
    - criterion_id: string
      question: string
      severity: critical | major | minor
      evidence_requirement: string
      owner_on_failure: worker | orchestrator | source_owner | strategy_owner | operator | review_configuration
      pass_condition: string
  sources: [ { source_id, path_or_locator, required: bool } ]
  assumptions: [ { assumption_id, statement, materiality } ]
  uncertainties: [ { uncertainty_id, statement, blocks_pass: bool } ]
  stop_conditions: [string]
  strategic_context:            # ONLY when review_lens: strategic_alignment; forbidden for validity
    macro_goal_path: string
    decision_log_path: string
  forbidden_context:            # MUST be withheld from the packet — blindness contract
    - worker_identity_and_confidence
    - worker_success_claim_or_persuasive_rationale
    - other_lens_verdict
    - prior_overall_verdict
```

## Verdict

```yaml
review_verdict:
  schema_version: "apex.review.verdict.v1"
  verdict_id: string
  review_id: string
  review_lens: validity | strategic_alignment
  artifact: { path, version, expected_sha256, observed_sha256, hash_verified: bool }
  overall_verdict: pass | revise | hold | needs_input | escalate
  criterion_verdicts:
    - criterion_id: string
      verdict: pass | revise | hold | needs_input | escalate | not_applicable
      falsification_attempt:            # mandatory — no PASS without it
        strongest_wrong_case: string
        evidence_sought: [string]       # ≥1
        search_completed: bool
        result: falsified_artifact | did_not_falsify_artifact | inconclusive
      evidence_refs: [ { source_id, locator, supports } ]   # every PASS needs ≥1
      reasoning_summary: string
      defect:                           # required when verdict ≠ pass/not_applicable
        severity: critical | major | minor
        owner: worker | orchestrator | source_owner | strategy_owner | operator | review_configuration
        artifact_location: string
        required_outcome: string
        prohibited_adjacent_changes: [string]
  unresolved_uncertainties: [ { uncertainty_id, statement, materiality, blocks_pass } ]
  evidence_free_pass_gate:              # ALL must be true for overall pass
    artifact_hash_verified: bool
    required_sources_retrieved: bool
    every_pass_has_evidence: bool
    every_pass_has_falsification_attempt: bool
    no_unresolved_critical_uncertainty: bool
  prohibited_actions_confirmation:      # all must be true
    reviewer_did_not_modify_artifact: true
    reviewer_did_not_write_correction: true
    reviewer_did_not_consult_other_lens_verdict: true
```

## Deterministic aggregation (no LLM aggregator, no majority vote)

Precedence: `escalate > needs_input > hold > revise > pass`. Promotion of the reviewed artifact to `authority.state: verified` requires: both lenses `pass`, all critical criteria `pass`, every PASS carries evidence + completed falsification, hashes match, no unresolved critical uncertainty. A single critical non-pass blocks. Reviewer timeout, malformed output, or truncation ⇒ `hold`, never implicit PASS.

## Recorded limitation

Both lenses run as fresh isolated Claude subagents (`meta-detective` definition). Context isolation is not epistemic independence — same-family review shares training priors (self/family-preference, correlated blind spots). Compensating controls: blindness contract, criterion-level falsification, evidence-bearing PASS gate, deterministic aggregation. A different-model-family validity judge is **out of scope by operator direction** (2026-07-11, no external calls); if this control ever proves insufficient in simulation records, that is the recorded escalation path.
