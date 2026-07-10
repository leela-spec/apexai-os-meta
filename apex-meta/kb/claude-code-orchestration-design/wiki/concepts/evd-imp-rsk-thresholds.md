---
title: "EVD IMP RSK Thresholds"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "evd-imp-rsk-thresholds"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "line 82; EVD_IMP_RSK semantics"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C007, B04-C013, B04-C014; gates and validation"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "needs_review"
related_concepts:
  - "candidate-is-not-accepted-truth"
  - "gated-write-side-mutation"
  - "current-state-vs-target-state"
related_entities: []
review_flags:
  - "operator_review_needed_before_treating_as_settled_doctrine"
---

# EVD IMP RSK Thresholds

## Definition

EVD (evidence strength), IMP (impact if wrong), and RSK (risk of proceeding) are hypothesized as the three axes an Apex handoff contract should score before deciding whether a candidate output may proceed automatically, needs validator or operator review, or must halt. This vocabulary is synthesized directly from the Phase 2 compile plan's explicit `EVD_IMP_RSK_semantics` core question in the `handoff_contract_index` (line 82) — no Phase 1 batch 04 source defines this acronym or its thresholds outright, so it is treated here as a working hypothesis rather than a directly quoted pattern.

## Operating Rules

```yaml
rules:
  - "Every candidate output receives an evidence-strength read (how well-sourced is this claim)."
  - "Every candidate output receives an impact read (how costly would being wrong be)."
  - "Every candidate output receives a risk read (how reversible is the target, how gated is the action)."
  - "Low evidence combined with high impact or high risk forces validator or operator review rather than auto-proceed; this is the condition B04-C013's HALT/CLARIFY controls are designed to catch."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Sole direct naming source for the EVD_IMP_RSK acronym as a required semantics question; without this pointer the page would have no grounding for its vocabulary."
    coverage: "EVD_IMP_RSK_semantics core question, when_validator_or_operator_review_is_required."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the closest directly-quoted mechanisms (HALT/CLARIFY, file-output validation status) that this hypothesized triage vocabulary would sit on top of."
    coverage: "Gate/HALT/CLARIFY controls; file-output and task-closure validation status."
```

## Macro / Meso / Micro

### Macro

The compile plan's `handoff_contract_index` needs a compact way to decide, for any candidate output, whether it can proceed, needs review, or must stop. EVD/IMP/RSK is proposed here as that compact shorthand — letting a three-letter triage replace a longer risk conversation on every handoff — but it is a proposed answer to the compile plan's question, not a term already defined by Phase 1 evidence.

### Meso

This connects the general gate and HALT/CLARIFY claims (B04-C013) and the file-output/closure validation claims (B04-C014) to a triage vocabulary that has not yet been given worked numeric thresholds anywhere in the ingested corpus. It functions as the scoring layer that feeds the candidate-to-accepted ladder described in `candidate-is-not-accepted-truth`.

### Micro

B04-C013 defines HALT and CLARIFY as routing controls that stop guessing, scope expansion, unsafe continuation, and silent failure — this is the enforcement mechanism EVD/IMP/RSK would trigger once a threshold is crossed. B04-C014 requires explicit validation status before success is claimed — this is the closure state EVD/IMP/RSK would need to feed. B04-C007's stop-condition freeze item is the closest existing Phase 1 concept to a pre-declared risk threshold, but it does not use or define an EVD/IMP/RSK vocabulary.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Execution-control contracts define HALT and CLARIFY as routing controls that stop guessing, scope expansion, unsafe continuation, and silent failure."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C013"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "File-output and task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C014"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "The handoff_contract_index poses EVD_IMP_RSK_semantics as an open core question, implying Apex needs a working shorthand for evidence/impact/risk triage; no Phase 1 batch 04 source defines this acronym or its numeric thresholds."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md line 82"
    confidence: medium
    claim_label: working_hypothesis
```

## Routes Here

```yaml
routes:
  - question: "What decides whether a candidate output can auto-proceed, needs review, or must halt?"
    leads_to: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/evd-imp-rsk-thresholds.md"
    rationale: "This page proposes the evidence/impact/risk triage vocabulary named as an open question by the compile plan."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/candidate-is-not-accepted-truth.md"
    relation: "EVD/IMP/RSK scoring is the mechanism that would decide when a candidate is allowed to move up the claim-status ladder."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/gated-write-side-mutation.md"
    relation: "High IMP/RSK readings are the condition under which a write-side mutation must stay gated rather than auto-proceed."
```

## Evidence

```yaml
evidence:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "line 82"
    supports: "Direct naming of EVD_IMP_RSK_semantics as an unresolved handoff_contract_index question."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C013"
    supports: "HALT/CLARIFY as the enforcement mechanism for a risk threshold being crossed."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C014"
    supports: "Explicit validation status as the closure state a threshold decision would feed."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "EVD/IMP/RSK is a hypothesized triage vocabulary synthesized from the compile plan's open question framing (line 82), not a term defined, named, or quoted verbatim anywhere in Phase 1 batch claims. This synthesis must be reviewed by the operator before being treated as settled doctrine."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md line 82"
    proposed_handling: "ask_operator"
  - id: U002
    description: "No numeric thresholds, scoring scale, or field names exist for EVD, IMP, or RSK; these require explicit operator policy before implementation."
    source_pointer: "phase1-batch04-apex-application-patterns.md B04-Q003"
    proposed_handling: "planning_task_candidate"
```
