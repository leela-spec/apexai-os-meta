---
title: Macro Meso Micro Synthesis Loop
page_type: concept
kb_slug: old-apex-full-orchestration-agent-kb-v2
concept_slug: macro-meso-micro-synthesis-loop
source_refs: [{source_id: source-401eeb0e75bfbd22, source_path: raw/other/managed/processes/HOLDING_ORCHESTRATION_FLOW.md, source_hash: NA, source_pointer: orchestration flow, source_storage_mode: copy_into_kb}, {source_id: source-32d8ac59f1ed8f06, source_path: raw/other/managed/processes/AGENT_HANDOFF_CONTRACTS.md, source_hash: NA, source_pointer: handoff minimums, source_storage_mode: copy_into_kb}]
created_at: 2026-07-10T22:10:00Z
updated_at: 2026-07-10T22:10:00Z
confidence: medium
claim_label: behavioral_inference
status: active
---
# Macro Meso Micro Synthesis Loop
## Definition
An operator-specified name for the documented pattern of framing a task, partitioning it, executing bounded evidence steps, and synthesizing results upward.
## Operating Rules
- never treat micro completion as macro completion;
- every upward synthesis must preserve evidence and uncertainty;
- loop back when verification finds a defect.
## Adaptive Ranked Source Set
- source_id: source-401eeb0e75bfbd22; rationale: process surface; coverage: orchestration flow.
- source_id: source-32d8ac59f1ed8f06; rationale: handoff surface; coverage: continuity requirements.
## Macro / Meso / Micro
### Macro
Set objective, constraints, authority, completion definition, and the evidence needed to know whether the whole task is advancing. The macro frame also identifies which uncertainties must remain visible rather than being compressed into a premature answer.
### Meso
Partition agents, dependencies, handoffs, validation responsibilities, and the order in which evidence should be assembled. Meso synthesis makes the relationship between local outputs and the global objective explicit.
### Micro
Perform one bounded action, capture exact evidence and source pointers, state what changed and what did not, identify unresolved risk, and return a legible result that another role can verify without reconstructing hidden reasoning.
### Upward synthesis
Reconcile micro evidence into meso state, then revise the macro understanding and next bounded action.
## Key Claims
- claim_id: MM01; claim: The full label is a behavioral inference rather than a single canonical protocol name.; source_pointer: HOLDING_ORCHESTRATION_FLOW.md; confidence: medium; claim_label: behavioral_inference
- claim_id: MM02; claim: Handoff continuity is required for iterative recombination.; source_pointer: AGENT_HANDOFF_CONTRACTS.md; confidence: high; claim_label: source_backed_summary
## Routes Here
- question: How can agents work iteratively without losing the whole task?; leads_to: wiki/summaries/resilient-iterative-orchestration.md; rationale: complete workflow.
- related_page: wiki/summaries/agent-architecture.md; relation: role allocation.
## Uncertainty / Raw Source Reopen Triggers
- id: U-MM01; description: Historical swarm experiments may use different granularity or concurrency.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md; proposed_handling: audit_item
