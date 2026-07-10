---
title: "Standard Handoff Packet"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "standard-handoff-packet"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 72-85; handoff_contract_index questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C004, B04-C009, B04-C011, B04-C014"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "current-state-vs-target-state"
  - "handoff-stop-conditions"
  - "low-token-handoff-design"
related_entities: []
review_flags:
  - "canonical field schema (EVD/IMP/RSK style semantics) is Phase 2 synthesis, not a verbatim Phase 1 schema"
---

# Standard Handoff Packet

## Definition

A standard handoff packet is the smallest explicit artifact that lets one role (a skill, an agent, or the operator) continue another role's work without relying on shared chat memory. It carries current state, target state, source authority/references, claim status, risk, and a stop or validation condition. It answers the `handoff_contract_index` questions `smallest_valid_handoff_packet` and `required_handoff_fields`, and is directly grounded in Batch 04's artifact-contract (B04-C004), clean-handoff (B04-C009), atomic-task-packet (B04-C011), and file-output/closure (B04-C014) claims.

## Operating Rules

```yaml
rules:
  - "Must reference current state and target state explicitly rather than embedding or assuming full prior context."
  - "Must use source_refs/pointers instead of copying full source bodies into the packet."
  - "Must state authority basis and claim status (evidence vs candidate vs validated vs accepted) and risk."
  - "Must name a stop condition or the single required next action."
  - "Must not be treated as closed until file-output/task-closure requirements (complete content, scope proof, fetch-back, explicit validation status) are satisfied for any artifact it produced."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Direct source for the artifact-contract (B04-C004), clean-handoff (B04-C009), atomic-task-packet (B04-C011), and closure (B04-C014) claims that define this packet's required content and completion condition."
    coverage: "Skill-to-skill artifact contracts, clean-handoff field list, explicit state frames, and file-output/task-closure requirements."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Defines the handoff_contract_index questions this page is organized to answer, including the smallest-valid-packet and required-fields framing."
    coverage: "handoff_contract_index core questions on smallest valid packet, required fields, authority visibility, claim-status semantics, and stop conditions."
```

## Macro / Meso / Micro

### Macro

The `handoff_contract_index` frames agent-to-agent and agent-to-operator handoffs around explicit authority, current/target state, claim-status semantics, and mandatory stop conditions. This maps directly onto Batch 04's existing doctrine that Apex skills exchange work through artifact contracts rather than direct calls or memory, and that high-risk execution requires an explicit packet rather than conversational continuity.

### Meso

B04-C004 establishes that skills are connected by artifact contracts: one skill writes an artifact to a canonical slot and a downstream skill reads it. B04-C009 supplies the concrete field list a clean handoff needs: settled state, source priority, a non-redo list, the exact next job, risks, and a success condition. B04-C011 requires explicit state frames and atomic task packets for high-risk execution rather than chat-history reconstruction. B04-C014 supplies the closure half: complete content, scope proof, target-root validation, fetch-back, and explicit validation status must all be satisfied before success is claimed on any packet's output.

### Micro

Batch 04's concept `atomic-task-payload` (a one-task instruction object with explicit target, scope, input references, constraints, and validation conditions) is essentially the inbound half of this packet; B04-C014's file-output contract is the outbound/closure half. Combining the two into a single named "standard handoff packet" concept is this KB's organizing step, done to answer the compile plan's handoff_contract_index directly.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Apex skills are connected by artifact contracts rather than direct calls: one skill writes an artifact to a canonical slot and downstream skills read that artifact."
    source_pointer: "B04-C004 (Apex_Alfred_Skill_Definition_Guide.md lines 94-107)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Clean handoffs should include settled state, source priority, a non-redo list, the exact next job, risks, and a success condition."
    source_pointer: "B04-C009 (BEST_PRACTICES_v_old.md lines 114-149)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "High-risk execution should carry explicit state frames and atomic task packets rather than relying on chat-history reconstruction."
    source_pointer: "B04-C011 (BEST_PRACTICES_v_old.md lines 190-230; APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 118-190)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "File-output and task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed."
    source_pointer: "B04-C014 (APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md continuation lines 52-94, 125-153, 247-280)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C005
    claim: "The specific field taxonomy implied by the handoff_contract_index (e.g., EVD/IMP/RSK-style claim-status semantics, current-state-vs-target-state as distinct named fields) is a Phase 2 synthesis organizing Batch 04's claims into a canonical schema, not a verbatim Phase 1 schema."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 72-85"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "What is the smallest packet that lets one agent hand bounded work to another without shared chat history?"
    leads_to: "claude-code-orchestration-design/concepts/current-state-vs-target-state.md"
    rationale: "Current-state-vs-target-state is one of the required fields this packet must make explicit."
  - related_page: "claude-code-orchestration-design/concepts/handoff-stop-conditions.md"
    relation: "The stop-condition subset of this packet's required fields, elaborated separately."
  - related_page: "claude-code-orchestration-design/concepts/low-token-handoff-design.md"
    relation: "The token-economy rationale for keeping this packet's field set small and reference-based."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C004"
    supports: "Artifact-contract handoff between skills."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C009"
    supports: "Clean-handoff required field list."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C011"
    supports: "Explicit state frames and atomic task packets for high-risk work."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C014"
    supports: "File-output/task-closure requirements before success is claimed."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 72-85"
    supports: "handoff_contract_index core questions this page answers."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The exact canonical schema/field names for a 'standard handoff packet' are not finalized in Phase 1; filesystem/artifact conventions remain open."
    source_pointer: "B04-C019; B04-Q001"
    proposed_handling: "revisit_source"
  - id: U002
    description: "EVD/IMP/RSK-style claim-status semantics are named in the compile plan's index question but not spelled out as a concrete schema in Batch 04; treat as a working hypothesis until a dedicated schema page is compiled."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 76-81"
    proposed_handling: "planning_task_candidate"
```
