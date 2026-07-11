---
title: "Operator-Gated Phase Boundary"
page_type: "concept"
kb_slug: "apex-plan-sync-session-workflow-v2"
concept_slug: "operator-gated-phase-boundary"
source_refs:
  - source_id: "apex-plan-skill"
    source_path: "raw/other/SKILL.md"
    source_hash: "a83172f1d3f075273ca05a7e91254ed65ef77294a7519f74e94267c1ff3629cf"
    source_pointer: "lines 243-249 (operator_gate)"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-sync-skill"
    source_path: "raw/notes/SKILL.md"
    source_hash: "698848fede4076f10bf3cca2e03d16ffbb9497e9fc9f8d03a851869a54af5b14"
    source_pointer: "lines 78-109 (dry-run default and single non-dry-run exception)"
    source_storage_mode: "copy_into_kb"
  - source_id: "apex-session-skill"
    source_path: "raw/refs/SKILL.md"
    source_hash: "c45445a3499990275483e0103b7cfc7c1e5b35e7ed0c3ab48d3556fb6902537c"
    source_pointer: "lines 52-56, 196-198, 236-240 (operator_validation gate)"
    source_storage_mode: "copy_into_kb"
created_at: "2026-07-03T12:00:00Z"
updated_at: "2026-07-11T10:04:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "proposal-computation-mutation-split.md"
  - "isolation-with-overlap.md"
related_entities:
  - "../entities/apex-session.md"
review_flags: []
---

# Operator-Gated Phase Boundary

## Definition

This project implements "nothing consequential by default" as three structurally different gates
in three different packages, rather than one shared gate mechanism — apex-plan's `operator_gate`
(a required packet field before any handoff is acted on), apex-sync's dry-run default (a CLI flag
that must be explicitly flipped), and apex-session's `operator_validation` enum (a four-state
field that must reach `confirmed` before a mutation counts). This same three-gate pattern also
governs this KB's own lifecycle: Phase 1 analysis explicitly halts before Phase 2 wiki compilation
until the operator supplies the literal phrase `approve ingest` (apex-kb skill,
semantic_compile_policy.legacy_explicit_gate_phrase) — the KB tooling that documents this project
uses the identical pattern it is documenting.

## Operating Rules

```yaml
rules:
  - apex_plan_gate: "operator_gate.required_before_mutation_handoff: true; accepted_states are operator_review_needed, approved_for_handoff, needs_revision (apex-plan SKILL.md lines 243-249)."
  - apex_sync_gate: "default_mode: dry_run on every command; only registry --dry-run false is allowed to write, and only to apex-meta/registry/index.md (apex-sync SKILL.md lines 95-106)."
  - apex_session_gate: "operator_validation must equal confirmed before a status_mutation_record counts as final; needs_revision and not_requested both keep it open (apex-session SKILL.md lines 52-56, 236-240)."
  - kb_lifecycle_gate: "This KB's own Phase 2 wiki compile required the operator to type 'approve ingest' before this page was written -- this page IS an artifact of that gate having been satisfied."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "plan-sync-session-interconnection"
    rationale: "Registry-driven ranking for the interconnection topic, which covers gate/handoff/mutate keywords directly relevant to this concept."
    coverage: "Cross-package gate and handoff evidence, script-ranked."
  - source_id: "apex-session-mutation-gate-rules"
    rationale: "53 hits under apex-session-contract — the canonical source for the most granular of the three gate implementations (four-state operator_validation enum)."
    coverage: "status_mutation_record, before_after_preview, operator_validation_record schemas."
  - source_id: "apex-sync-skill"
    rationale: "Direct source for the dry-run-default gate pattern."
    coverage: "Canonical Command Policy: dry-run default, single non-dry-run exception."
```

## Macro / Meso / Micro

### Macro

An operator gate is the point where a system stops being able to act on its own judgment and must
wait for an external, human confirmation signal. This project puts a gate at every boundary where
an action becomes hard to reverse: handing off a plan for execution, writing a file, or confirming
a state change as final. The KB-compilation process that produced this very page is itself gated
the same way — Phase 2 could not begin until this session's operator supplied `approve ingest`.

### Meso

The three gates differ in shape but share a common property: none of them silently default to the
"acted" state. apex-plan's `operator_gate` requires an explicit state
(`operator_review_needed`/`approved_for_handoff`/`needs_revision`) rather than assuming approval
once a packet exists. apex-sync's dry-run default means the absence of a flag is the safe state,
not the dangerous one — you must add `--dry-run false` to leave safety, rather than add
`--dry-run true` to enter it. apex-session's `operator_validation` enum has two "not yet decided"
states (`needs_revision`, `not_requested`) in addition to `confirmed`/`rejected`, so an ambiguous
or incomplete validation input does not get coerced into either a false-confirm or a false-reject.

### Micro

Concretely, this KB's own Phase 1 completion report (superseded by the batch06-10 analyses
written in this run) previously recorded `phase2_allowed: false`, and Phase 2 compilation of this
very page did not proceed until the operator's message containing the literal phrase
`approve ingest` was received in this session — the gate is not metaphorical, it is a real
blocking condition enforced by this KB's own semantic_compile_policy.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "apex-plan's operator_gate requires one of exactly three accepted states before mutation handoff: operator_review_needed, approved_for_handoff, needs_revision."
    source_pointer: "raw/other/SKILL.md lines 243-249"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "apex-sync's default_mode is dry_run for every command; the single allowed non-dry-run invocation is registry --dry-run false, writing only apex-meta/registry/index.md."
    source_pointer: "raw/notes/SKILL.md lines 95-106"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "apex-session's operator_validation enum has four states (confirmed, rejected, needs_revision, not_requested), and only confirmed causes a mutation record to count as final."
    source_pointer: "raw/refs/SKILL.md lines 52-56, 236-240"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C004
    claim: "This KB's own Phase 2 wiki compile step was blocked pending the operator's explicit 'approve ingest' phrase, received in this session before this page was authored -- the KB tooling enforces the same gate pattern it documents."
    source_pointer: "this session's conversation record; .claude/skills/apex-kb/SKILL.md semantic_compile_policy.legacy_explicit_gate_phrase"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What exactly counts as a 'confirmed' vs. 'proposed' vs. 'computed' claim in this system?"
    leads_to: "proposal-computation-mutation-split.md"
    rationale: "The gate pattern documented here is the mechanism that enforces the epistemic-state split documented there."
  - question: "How does the apex-kb tooling that built this wiki decide when it's allowed to compile pages?"
    leads_to: "../entities/apex-session.md"
    rationale: "apex-session's operator_validation gate is the closest in-system analog to apex-kb's own approve-ingest gate."
  - related_page: "apex-plan-sync-session-workflow-v2/concepts/isolation-with-overlap.md"
    relation: "The gate pattern is one of the three repeated-overlap mechanisms that concept identifies as producing resilience."
```

## Evidence

```yaml
evidence:
  - source_id: "apex-plan-skill"
    source_pointer: "lines 243-249"
    supports: "C001"
  - source_id: "apex-sync-skill"
    source_pointer: "lines 95-106"
    supports: "C002"
  - source_id: "apex-session-skill"
    source_pointer: "lines 52-56, 236-240"
    supports: "C003"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: >
      Whether a later deterministic status report should store the Phase 2 approval event
      (the operator's 'approve ingest' message) as a machine-readable lifecycle record rather
      than only as conversational history remains an open design question for the apex-kb
      tooling itself, not a claim this KB can resolve about its sources.
    source_pointer: "n/a (tooling design question)"
    proposed_handling: ask_operator
```
