---
title: "Operator-Confirmed Mutation"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "operator-confirmed-mutation"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 86-98; confirmed mutation records"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 54-68; hard gates"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C005 and B04-C014; operator gates and closure proof"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "gated-write-side-mutation"
  - "dry-run-first-state-policy"
  - "candidate-is-not-accepted-truth"
related_entities: []
review_flags: []
---

# Operator-Confirmed Mutation

## Definition

An operator-confirmed mutation is a durable write to canonical state, schema, source custody, or execution records that becomes accepted only after explicit operator approval or an equivalent approved gate. This directly answers the `project_execution_index` core question `which_components_may_write_confirmed_mutation_records`: the answer is that no automated component writes a confirmed mutation record on its own — a human operator gate stands between a proposed change and its acceptance as durable state. It is grounded directly in B04-C005 (operator gates as a first-class Apex design rule) and B04-C014 (file-output/task-closure contracts requiring explicit validation status before success is claimed).

## Operating Rules

```yaml
rules:
  - "A write that changes canonical state, schema, source custody, or execution records requires explicit operator confirmation before it is treated as accepted."
  - "Skills must pause for explicit approval before downstream use when validation is required, rather than assuming silent acceptance."
  - "Success is not claimed until complete content, scope proof, target-root validation, and fetch-back verification have all occurred."
  - "A Phase 2 compiled wiki page already authorized under an existing operator gate (e.g. 'approve ingest') does not require a fresh per-page confirmation cycle."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Primary and most specific source: B04-C005 states the operator-gate rule directly, and B04-C014 states the closure-proof contract that must precede a claim of successful mutation."
    coverage: "Claims B04-C005 (operator gates as first-class design rule) and B04-C014 (file-output/task-closure contracts)."
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Records the operator's own hard-gate decisions for this KB run, directly evidencing the pattern in practice."
    coverage: "Lines 54-68: hard gates applied during Phase 1 review."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Supplies the exact project_execution_index question this concept answers."
    coverage: "project_execution_index core_questions, lines 86-98, especially which_components_may_write_confirmed_mutation_records and what_defaults_to_dry_run."
```

## Macro / Meso / Micro

### Macro

Across the Apex application-pattern material, no component is trusted to make a durable state change unilaterally. The `project_execution_index` frames this as one of the central separations in project execution: semantic planning, deterministic read-side computation, and gated write-side mutation are distinct layers, and only the last one produces durable, accepted records — and only with operator confirmation.

### Meso

Operator gates are described as a first-class Apex design rule: skills must pause for explicit approval before downstream use when validation is required (B04-C005). This pairs with the closure-proof requirement in B04-C014 — file-output and task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed. Together these mean an operator-confirmed mutation is not just "operator said yes" but "operator said yes, and the write was independently verified afterward."

### Micro

`Apex_Alfred_Skill_Definition_Guide.md` lines 108-120 is the direct source for the operator-gate pattern (B04-C005). `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` continuation lines 52-94 and 125-153, and lines 247-280, are the direct sources for the file-output and task-closure contract (B04-C014). The operator's own Phase 1 review decisions (lines 54-68 of the review-decisions log) show this same hard-gate pattern applied to this KB's own ingest process — reinforcing that the pattern is not merely theoretical for this KB.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Operator gates are a first-class Apex design rule: skills must pause for explicit approval before downstream use when validation is required."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C005"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "File-output and task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C014"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "The project_execution_index's question of which components may write confirmed mutation records is answered by this KB's own operator hard-gate practice: no automated write becomes canonical without an explicit operator decision."
    source_pointer: "operator-phase1-review-decisions-20260702 lines 54-68"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "Which components may write confirmed mutation records versus just propose or compute them?"
    leads_to: "claude-code-orchestration-design/concepts/operator-confirmed-mutation.md"
    rationale: "Direct match to the project_execution_index core question."
  - related_page: "claude-code-orchestration-design/concepts/gated-write-side-mutation.md"
    relation: "Operator-confirmed mutation is the acceptance step that follows a proposed gated write-side mutation."
  - related_page: "claude-code-orchestration-design/concepts/dry-run-first-state-policy.md"
    relation: "Dry-run defaults are the precondition that keeps unconfirmed proposals from becoming durable state before operator confirmation."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C005"
    supports: "Definition and Operating Rules: operator-gate requirement."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C014"
    supports: "Operating Rules and Meso section: closure-proof requirement before success is claimed."
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "lines 54-68"
    supports: "Micro section and Key Claim C003: hard gates applied in this KB's own run."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "No state mutation outside the KB wiki/log paths has occurred during this compile session (S6), so the pattern is documented but not yet exercised against a live Apex Plan/Sync/Session mutation."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 phase2_non_goals, lines 199-211"
    proposed_handling: "leave_as_gap"
  - id: U002
    description: "Whether HALT/CLARIFY/file-output/task-closure schemas (which underlie the closure-proof half of this pattern) become reusable Apex-wide contracts or stay local to the prompt/workflow lane is an open question (B04-Q003)."
    source_pointer: "phase1-batch04-apex-application-patterns open question B04-Q003"
    proposed_handling: "planning_task_candidate"
```
