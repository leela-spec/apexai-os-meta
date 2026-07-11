---
title: Resilient Iterative Orchestration
page_type: summary
kb_slug: old-apex-full-orchestration-agent-kb-v2
summary_slug: resilient-iterative-orchestration
source_refs:
  - {source_id: source-401eeb0e75bfbd22, source_path: raw/other/managed/processes/HOLDING_ORCHESTRATION_FLOW.md, source_hash: NA, source_pointer: orchestration flow, source_storage_mode: copy_into_kb}
  - {source_id: source-32d8ac59f1ed8f06, source_path: raw/other/managed/processes/AGENT_HANDOFF_CONTRACTS.md, source_hash: NA, source_pointer: handoff minimums, source_storage_mode: copy_into_kb}
  - {source_id: source-05bc8d6b022c9444, source_path: raw/other/managed/rules/AGENT_SWARM_INTERACTION_CANON.md, source_hash: NA, source_pointer: state transitions, source_storage_mode: copy_into_kb}
created_at: 2026-07-10T22:05:00Z
updated_at: 2026-07-10T22:05:00Z
confidence: mixed
claim_label: behavioral_inference
status: active
---
# Resilient Iterative Orchestration

## Core Summary
The source system supports an iterative workflow in which a coordinator frames the whole task, specialized agents partition and execute bounded work, validators inspect the result, and the system loops back or escalates before promotion. The exact macro/meso/micro label is an operator-level synthesis, while the underlying build/verify/lock and handoff mechanics are source-backed.

## Adaptive Ranked Source Set
- source_id: source-401eeb0e75bfbd22; rationale: primary process surface; coverage: holding and orchestration flow.
- source_id: source-32d8ac59f1ed8f06; rationale: handoff contract surface; coverage: durable transfer requirements.
- source_id: source-05bc8d6b022c9444; rationale: state law; coverage: build, verify, lock, loop-back, escalation.

## Macro / Meso / Micro
### Macro
Define the objective, constraints, authority posture, and desired output; keep one visible coordinator and one bounded active flow.
### Meso
Partition the objective into agent-owned surfaces, establish dependencies and handoffs, then assign build and review states. Use overlapping validators where ambiguity or drift risk is high.
### Micro
Execute a bounded artifact or evidence step, record source pointers and unresolved risk, hand it to the next role, and either advance, loop back from VERIFY to BUILD, or lock/escalate.
### Upward synthesis
Micro evidence is reconciled into meso conclusions; meso conclusions update the macro frame. This upward pass prevents local completion from being mistaken for system completion.

## Key Claims
- claim_id: W01; claim: A valid handoff identifies role, state, target, next role/state, prerequisites, expected action, and unresolved risk.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Handoff-rules; confidence: high; claim_label: source_backed_summary
- claim_id: W02; claim: BUILD to VERIFY and VERIFY to BUILD are normal transitions when review finds repair work.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Normal-transitions; confidence: high; claim_label: source_backed_summary
- claim_id: W03; claim: The macro/meso/micro naming is a behavioral inference over the documented process surfaces.; source_pointer: HOLDING_ORCHESTRATION_FLOW.md; confidence: medium; claim_label: behavioral_inference

## Routes Here
- question: How should a complex task be decomposed and recombined?; leads_to: wiki/concepts/macro-meso-micro-synthesis-loop.md; rationale: full loop.
- question: What must a handoff contain?; leads_to: wiki/concepts/explicit-handoff-continuity.md; rationale: continuity mechanism.
- related_page: wiki/summaries/agent-architecture.md; relation: agents supply bounded roles.

## Uncertainty / Raw Source Reopen Triggers
- id: U-W01; description: No single canonical source defines the full macro-to-micro-to-macro vocabulary.; source_pointer: HOLDING_ORCHESTRATION_FLOW.md; proposed_handling: working_hypothesis
- id: U-W02; description: Conservative single-flow doctrine may conflict with historical swarm experiments.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Default-operating-stance; proposed_handling: audit_item
