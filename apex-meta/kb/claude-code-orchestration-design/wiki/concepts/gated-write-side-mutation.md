---
title: "Gated Write-Side Mutation"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "gated-write-side-mutation"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 86-98; gated write-side mutation"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 54-68; hard-enforce high-risk gates"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C005, B04-C014, B04-C017"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "candidate-is-not-accepted-truth"
  - "file-state-over-chat-state"
  - "current-state-vs-target-state"
related_entities: []
review_flags: []
---

# Gated Write-Side Mutation

## Definition

Write-side mutation — any operation that changes durable project, KB, or execution state — is gated: it defaults to a dry-run or proposal mode, and only becomes a confirmed mutation record after explicit approval and validation against the intended target. This directly answers the Phase 2 compile plan's `project_execution_index` core questions `which_components_may_write_confirmed_mutation_records` and `what_defaults_to_dry_run`, and is grounded in Phase 1 batch 04's operator-gate and closure-contract claims plus the operator's own hard-enforcement decisions.

## Operating Rules

```yaml
rules:
  - "The default mode for any state-changing operation is dry-run/proposal, not immediate write."
  - "Only specifically authorized components may write confirmed mutation records; proposing a change is not the same authority as writing it."
  - "High-risk targets are hard-enforced gates rather than soft guidance: writes outside the KB root, raw-source delete or mutation, KB schema overwrite without an explicit flag, and destructive archive delete."
  - "A mutation is not \"confirmed\" until target-root validation and fetch-back proof exist, per the file-output and task-closure contract."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Direct operator decision (Q002) naming the exact high-risk items that are hard-enforced versus the items left as soft guidance; the most specific and authoritative source for this page's rules."
    coverage: "hard_enforce_high_risk_gates_only decision and the specific hard_enforce / soft_enforce lists."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the general operator-gate (B04-C005) and file-output/closure (B04-C014) claims this pattern applies specifically to write-side mutation."
    coverage: "Operator gates as first-class design rule; file-output and task-closure validation requirements."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Names the project_execution_index questions this page directly answers."
    coverage: "which_components_may_write_confirmed_mutation_records; what_defaults_to_dry_run."
```

## Macro / Meso / Micro

### Macro

This is the `project_execution_index`'s central safety separation between semantic planning, deterministic read-side computation, and gated write-side mutation. It is what keeps an LLM-driven system from silently corrupting canonical state: proposing a change and confirming a change are treated as two different authority levels, not one continuous action.

### Meso

This pattern is the write-path-specific instance of the general operator-gate pattern (B04-C005) and closure-contract pattern (B04-C014), scoped specifically to state mutation rather than to any artifact in general. The operator's own Q002 decision makes this concrete by hard-enforcing a specific short list of high-risk mutation targets while leaving lower-risk conventions as soft guidance.

### Micro

B04-C005 states that operator gates are a first-class Apex design rule: skills must pause for explicit approval before downstream use when validation is required. B04-C014 requires complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed for any file-output or task-closure. Operator decision Q002 hard-enforces `phase2_without_approve_ingest`, `write_outside_kb_root`, `raw_source_delete_or_mutation`, `kb_schema_overwrite_without_explicit_flag`, and `destructive_archive_delete`, while treating style, terminology, and low-risk documentation conventions as soft enforcement only.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Operator gates are a first-class Apex design rule: skills must pause for explicit approval before downstream use when validation is required."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C005"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "File-output and task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C014"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "Apex hard-enforces high-risk gates only — writes outside the KB root, raw-source delete or mutation, KB schema overwrite without an explicit flag, and destructive archive delete are hard enforcement; style, terminology, source ordering, and low-risk documentation conventions are soft enforcement."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 52-65 (Q002_hook_or_script_enforcement)"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What stops an agent from writing an unreviewed state change directly to a canonical file?"
    leads_to: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/gated-write-side-mutation.md"
    rationale: "This page defines the dry-run-by-default, gate-before-confirm rule that prevents that."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/candidate-is-not-accepted-truth.md"
    relation: "A proposed mutation is a candidate; it only becomes a confirmed mutation record after the same validation discipline is applied."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/current-state-vs-target-state.md"
    relation: "A gated mutation compares current state to target state before proceeding to a dry-run or confirmed write."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C005"
    supports: "Operator gates as a first-class design rule requiring explicit approval before downstream use."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C014"
    supports: "Target-root validation and fetch-back proof required before a mutation is confirmed."
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "lines 52-65"
    supports: "Specific hard-enforce list for high-risk write targets versus soft-enforce list for style/terminology."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 86-98"
    supports: "Direct naming of which_components_may_write_confirmed_mutation_records and what_defaults_to_dry_run as project_execution_index questions."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "This Phase 2 compile documents the gating rule but creates no enforcement hooks or scripts, per the explicit Phase 2 non-goal of writing hooks or executable runtime surfaces; the rule is source-backed, but its mechanical enforcement is not yet built anywhere."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 199-211 (phase2_non_goals)"
    proposed_handling: "leave_as_gap"
  - id: U002
    description: "Which components beyond the KB-compile hard-enforce list count as \"authorized\" to write confirmed mutation records, and the exact dry-run mechanics, remain open per B04-Q003 (whether HALT/CLARIFY/file-output/task-closure schemas become Apex-wide contracts or stay local to prompt/workflow lanes)."
    source_pointer: "phase1-batch04-apex-application-patterns.md B04-Q003"
    proposed_handling: "ask_operator"
```
