---
title: "Flow Recap Packet"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "flow-recap-packet"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; flow recap stage"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001, B04-C009, B04-C011"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "active"
related_concepts:
  - "flow-packet"
  - "agent-learning-queue-candidate-only"
  - "candidate-is-not-accepted-truth"
related_entities: []
review_flags:
  - "operator_review_needed_before_treating_as_settled_doctrine"
---

# Flow Recap Packet

## Definition

A flow recap packet is the structured-memory artifact FlowRecapSkill produces after a flow packet executes: it compresses raw execution evidence into a durable summary, a set of candidate state deltas, and any open questions, so a downstream status-merge stage does not need to re-read raw execution logs. This is an Apex-specific synthesis built from Phase 1 batch 04's FlowRecapSkill entity (medium confidence) and its clean-handoff and state-frame claims (B04-C009, B04-C011); no Phase 1 claim defines a "flow recap packet" schema verbatim.

## Operating Rules

```yaml
rules:
  - "A flow recap packet is only produced after execution evidence exists for the corresponding flow packet, not before or instead of it."
  - "Recap output is a candidate state delta, not an automatically accepted state update (see candidate-is-not-accepted-truth)."
  - "The recap packet preserves enough source pointer/evidence for later audit even after the raw execution dump is discarded."
  - "The recap packet is read by the downstream status-merge stage; it is not itself treated as final doctrine."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Names the FlowRecapSkill entity directly and supplies the clean-handoff and state-frame claims (B04-C009, B04-C011) this packet's contents are derived from."
    coverage: "FlowRecapSkill entity role; clean-handoff fields; explicit state frames."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Frames the weekly_routine_case_index questions about canonical state vs. temporary execution evidence and preventing raw dumps from bloating future context, which this packet type directly answers."
    coverage: "canonical_state_vs_temporary_execution_evidence; how_raw_dumps_are_prevented_from_bloating_future_context."
```

## Macro / Meso / Micro

### Macro

This is the concrete mechanism by which raw, verbose flow-execution evidence is converted into small, reusable memory instead of bloating future session context — directly answering the `token_economy_and_information_design_index`'s concern about preventing raw dumps from bloating future context.

### Meso

At the entity level, this corresponds to the Phase 1 batch 04 "FlowRecapSkill" entity (medium confidence): a digest skill converting raw flow execution evidence into structured recap memory. The flow recap packet is hypothesized here as that skill's concrete output artifact.

### Micro

B04-C001 states that Apex maps the PreCap/FlowRecap/APSU loop into discrete Claude skills. B04-C009 requires that clean handoffs include settled state, source priority, non-redo list, exact next job, risks, and success condition — the recap packet is where that settled state would live. B04-C011 requires explicit state frames rather than chat-history reconstruction, which the recap packet operationalizes for the post-execution stage specifically.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "FlowRecapSkill is a digest skill entity that converts raw flow execution evidence into structured recap memory."
    source_pointer: "phase1-batch04-apex-application-patterns.md entity flow-recap-skill (section 5)"
    confidence: medium
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "Clean handoffs should include settled state, source priority, non-redo list, exact next job, risks, and success condition."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C009"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "Generalizing B04-C001 and B04-C009, a flow recap packet is hypothesized as the concrete artifact where FlowRecapSkill's settled-state output lives, produced from a flow packet's execution evidence and consumed as a candidate (not accepted) state delta by later status-merge steps."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 99-111 (weekly_routine_case_index)"
    confidence: medium
    claim_label: working_hypothesis
```

## Routes Here

```yaml
routes:
  - question: "How does raw flow execution evidence become durable memory without bloating future context?"
    leads_to: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/flow-recap-packet.md"
    rationale: "This page defines the flow recap packet as the compression artifact answering that question."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/flow-packet.md"
    relation: "The flow recap packet is produced from the execution evidence of a preceding flow packet."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/candidate-is-not-accepted-truth.md"
    relation: "The recap packet's state deltas remain candidate status until validated and accepted downstream."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "entity flow-recap-skill"
    supports: "FlowRecapSkill as a digest skill converting raw execution evidence into structured recap memory."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C009"
    supports: "Clean-handoff fields (settled state, source priority, non-redo list, next job, risks, success condition) that the recap packet carries."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C011"
    supports: "Explicit state frames over chat-history reconstruction, applied here to the post-execution recap stage."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 99-111"
    supports: "weekly_routine_case_index framing of canonical state vs. temporary execution evidence."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "\"Flow recap packet\" is a synthesized artifact name built from the FlowRecapSkill entity (itself only medium confidence in Phase 1) and general clean-handoff/state-frame claims; it is not a defined schema in any Phase 1 batch claim. This synthesis should be reviewed by the operator before being treated as settled doctrine."
    source_pointer: "phase1-batch04-apex-application-patterns.md entity flow-recap-skill; claims B04-C001, B04-C009, B04-C011"
    proposed_handling: "ask_operator"
  - id: U002
    description: "No FlowRecap runtime artifact schema or field list exists yet from this compile; exact recap packet contents remain open."
    source_pointer: "phase1-batch04-apex-application-patterns.md B04-Q002"
    proposed_handling: "planning_task_candidate"
```
