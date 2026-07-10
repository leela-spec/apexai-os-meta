---
title: "Flow Packet"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "flow-packet"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; each stage reads and writes"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 100-107; flow packet points to prompt pack"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "active"
related_concepts:
  - "flow-recap-packet"
  - "gated-write-side-mutation"
related_entities: []
review_flags:
  - "operator_review_needed_before_treating_as_settled_doctrine"
---

# Flow Packet

## Definition

A flow packet is the planning-side artifact that scopes one discrete execution unit ("flow") within a larger Apex routine. It names an objective, its input references, and a pointer to the associated execution prompt pack, rather than embedding the full prompt text inline. This is an Apex-specific synthesis: the operator's Phase 1 review decisions (Q007) establish that a flow packet is a planning artifact distinct from — and pointing to — a separate prompt-pack execution artifact, and Phase 1 batch 04's artifact-contract-handoff claim (B04-C004) supplies the general mechanism this specific pairing instantiates. No Phase 1 batch claim names "flow packet" verbatim as a defined term.

## Operating Rules

```yaml
rules:
  - "One flow packet corresponds to one bounded unit of work, not an entire day's or week's plan."
  - "A flow packet references — rather than duplicates — its execution prompt pack, per the operator decision that flow_packet points to prompt_pack."
  - "Flow packet input refs replace full context re-statement, consistent with the handoff_contract_index question of how input refs replace full context."
  - "Execution prompt packs are not placed inside Apex KB wiki pages; they remain separate execution artifacts."
  - "After execution, the flow packet is read by the flow-recap stage to produce a flow recap packet."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Direct operator decision (Q007) establishing the flow_packet / prompt_pack split and pointing relationship, the most specific grounding available for this concept."
    coverage: "one_prompt_pack_file_per_flow decision; flow_packet as planning artifact vs prompt_pack as execution artifact."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the general artifact-contract-handoff mechanism (B04-C004) and the PreCap/FlowRecap/APSU skill mapping (B04-C001) this packet type fits into."
    coverage: "Artifact contracts between skills; PreCap/FlowRecap/APSU loop mapping."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Frames the weekly_routine_case_index question of what each stage reads and writes, which this page answers for the flow-execution stage."
    coverage: "what_each_stage_reads_and_writes core question."
```

## Macro / Meso / Micro

### Macro

Flow packets are the mechanism by which a multi-stage routine (such as a weekly or daily planning loop) stays composed of small, independently auditable units instead of one large, undifferentiated plan. Each flow is scoped, sourced, and closeable on its own.

### Meso

The flow packet sits between the planning layer (a next-day or weekly plan) and the execution layer (a prompt pack). This two-artifact split — planning artifact vs. execution artifact — was an explicit operator decision (Q007), not merely an inference: "flow_packet: planning artifact; prompt_pack: execution prompt artifact; relationship: flow_packet_points_to_prompt_pack."

### Micro

B04-C004 states that Apex skills are connected by artifact contracts rather than direct calls: one skill writes an artifact to a canonical/logical slot and downstream skills read that artifact. B04-C001 states that Apex maps the PreCap/FlowRecap/APSU loop into discrete Claude skills. The flow packet is the concrete planning-stage artifact instance of that general contract, feeding into the flow-recap stage described in `flow-recap-packet`.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Apex skills are connected by artifact contracts rather than direct calls: one skill writes an artifact to a canonical/logical slot and downstream skills read that artifact."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C004"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "Apex uses one prompt-pack file per flow; the flow packet is the planning artifact, the prompt pack is the execution artifact, and the flow packet points to the prompt pack. Execution prompt packs should not be placed inside Apex KB wiki pages."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 98-105 (Q007_prompt_pack_filesystem)"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "Generalizing the Q007 decision and B04-C001/B04-C004, a \"flow packet\" is hypothesized as the concrete planning-artifact instance of the general artifact-contract-handoff pattern, scoped to one execution unit within a routine such as the weekly or daily loop."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 99-111 (weekly_routine_case_index)"
    confidence: medium
    claim_label: working_hypothesis
```

## Routes Here

```yaml
routes:
  - question: "What artifact scopes a single unit of planned work before it is executed?"
    leads_to: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/flow-packet.md"
    rationale: "This page defines the flow packet as that scoping artifact and its relationship to the prompt pack."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/flow-recap-packet.md"
    relation: "The flow packet's execution evidence is what the flow recap packet later compresses into structured memory."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/gated-write-side-mutation.md"
    relation: "Executing a flow packet may propose state changes that must pass through the gated write-side mutation path."
```

## Evidence

```yaml
evidence:
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "lines 98-105"
    supports: "Direct decision naming the flow_packet/prompt_pack split and pointing relationship."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C004"
    supports: "General artifact-contract-handoff mechanism between skills."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C001"
    supports: "PreCap/FlowRecap/APSU loop mapped into discrete Claude skills, of which the flow stage is one link."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 99-111"
    supports: "weekly_routine_case_index framing of what each stage reads and writes."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "\"Flow packet\" as a named artifact is synthesized from the operator's Q007 decision and the general artifact-contract-handoff and weekly-routine-case-index framing, not from a verbatim Phase 1 batch definition. This synthesis should be reviewed by the operator before being treated as settled doctrine."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 98-105; phase2-specialized-index-compile-plan-20260702.md lines 99-111"
    proposed_handling: "ask_operator"
  - id: U002
    description: "The exact filesystem convention for per-flow prompt-pack artifacts remains unresolved; current evidence supports separate prompt-pack artifacts, but exact paths must not be invented without further operator confirmation."
    source_pointer: "phase1-batch04-apex-application-patterns.md B04-Q001"
    proposed_handling: "planning_task_candidate"
```
