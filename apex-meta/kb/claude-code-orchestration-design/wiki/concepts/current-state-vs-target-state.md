---
title: "Current State vs Target State"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "current-state-vs-target-state"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 72-85; current_state_vs_target_state"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C007 and B04-C011; state frames and target locks"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "file-state-over-chat-state"
  - "gated-write-side-mutation"
related_entities: []
review_flags: []
---

# Current State vs Target State

## Definition

A handoff or task packet names both what is currently true (current state) and what a successful completion looks like (target state) explicitly, rather than leaving either to be inferred from conversation history. This pairing is named directly by the Phase 2 compile plan's `handoff_contract_index` core question `current_state_vs_target_state`, and it operationalizes Phase 1 batch 04's requirement that target, source authority, non-goals, output contract, and stop condition be frozen before execution begins.

## Operating Rules

```yaml
rules:
  - "Current state is captured from files or artifacts, not from memory or assumed continuity."
  - "Target state (the output contract) is frozen before execution begins, per B04-C007's freeze list."
  - "Progress or drift is measured as the delta between current state and target state, not by subjective impression."
  - "A task is not complete until current state matches target state and that match has been verified, not merely asserted."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Directly names current_state_vs_target_state as a required handoff_contract_index core question."
    coverage: "current_state_vs_target_state question framing within the handoff contract index."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the concrete freeze-list and state-frame claims that this pairing formalizes."
    coverage: "Target/source-authority/non-goals/output-contract/stop-condition freeze list; explicit state frames and atomic task packets."
```

## Macro / Meso / Micro

### Macro

This is one of the core dimensions the `handoff_contract_index` must answer: without explicitly naming both the current state and the target state of a handoff, agents tend to either silently narrow scope (assuming less has changed than actually has) or silently expand scope (assuming the target is broader than actually agreed). Naming both ends closes that gap before execution starts.

### Meso

This pairs directly with B04-C007's freeze list — target, source authority, non-goals, output contract, and stop condition — which must be named before execution and verified only after execution. Current-state-vs-target-state is essentially the "current" and "target" halves of that freeze list, formalized as a reusable field on any handoff or task packet.

### Micro

B04-C011 requires that high-risk execution carry explicit state frames and atomic task packets rather than relying on chat-history reconstruction — the state frame is precisely where current state is recorded. B04-C007 requires target, source authority, non-goals, output contract, and stop condition to be named before execution, with verification following execution before completion is reported — the output contract is precisely the target state.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Apex prompt/workflow doctrine requires target, source authority, non-goals, output contract, and stop condition to be named before execution; verification follows execution before completion is reported."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C007"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "High-risk execution should carry explicit state frames and atomic task packets rather than relying on chat-history reconstruction."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C011"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "The handoff_contract_index must answer how current state and target state are distinguished within a handoff."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 78 (current_state_vs_target_state)"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "How does a handoff packet avoid silent scope drift between what exists now and what the operator wants?"
    leads_to: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/current-state-vs-target-state.md"
    rationale: "This page defines the paired current/target state fields that close that gap."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/file-state-over-chat-state.md"
    relation: "Current state must be read from durable files/artifacts, not from chat memory, for this pairing to be trustworthy."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/gated-write-side-mutation.md"
    relation: "A gated mutation compares current state to target state before proceeding to a dry-run or confirmed write."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C007"
    supports: "Freeze list naming target, source authority, non-goals, output contract, stop condition before execution."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C011"
    supports: "Explicit state frames and atomic task packets over chat-history reconstruction."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 72-85"
    supports: "Direct naming of current_state_vs_target_state as a handoff_contract_index core question."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The exact schema/fields for encoding current state versus target state (e.g., diff format, packet shape) are not specified in Phase 1 batch claims; this page synthesizes the general rule from the compile plan's question framing and B04's freeze-list claims, and that synthesis should be reviewed by the operator before being treated as final doctrine."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 72-85; phase1-batch04-apex-application-patterns.md claims B04-C007, B04-C011"
    proposed_handling: "ask_operator"
  - id: U002
    description: "No runtime state packet is created by this Phase 2 compile step; only the rule is documented."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 199-211 (phase2_non_goals)"
    proposed_handling: "leave_as_gap"
```
