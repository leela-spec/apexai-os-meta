---
title: Agent Architecture, Isolation, and Intentional Overlap
page_type: summary
kb_slug: old-apex-full-orchestration-agent-kb-v2
summary_slug: agent-architecture
source_refs:
  - {source_id: source-8c534a90902556f2, source_path: raw/other/managed/agents/AGENT_INDEX.md, source_hash: NA, source_pointer: Final v1 first-wave activation map, source_storage_mode: copy_into_kb}
  - {source_id: source-05bc8d6b022c9444, source_path: raw/other/managed/rules/AGENT_SWARM_INTERACTION_CANON.md, source_hash: NA, source_pointer: Semantic role layer and operational state model, source_storage_mode: copy_into_kb}
  - {source_id: source-184e996257212fbb, source_path: raw/other/managed/knowledge/KB_STARTING_SOURCE_MAP.md, source_hash: NA, source_pointer: Authority order summary, source_storage_mode: copy_into_kb}
created_at: 2026-07-10T22:05:00Z
updated_at: 2026-07-10T22:05:00Z
confidence: high
claim_label: source_backed_summary
status: active
---
# Agent Architecture, Isolation, and Intentional Overlap

## Core Summary
The old Apex system is a routed swarm of specialized accountability surfaces. Isolation is created by explicit role/state boundaries and target surfaces; resilience is created by bounded overlap between neighboring agents that can detect one another’s failures without owning the same final decision.

## Adaptive Ranked Source Set
- source_id: source-8c534a90902556f2; rationale: named activation and routing authority; coverage: nine agents, validators, read order, overlap reminders.
- source_id: source-05bc8d6b022c9444; rationale: governing role/state law; coverage: BUILD, VERIFY, LOCK, delegation, handoffs.
- source_id: source-184e996257212fbb; rationale: authority and source-routing boundary; coverage: final, lock, seed, governance, staging classes.

## Macro / Meso / Micro
### Macro
The system decomposes orchestration into intake, sequencing, strategy, investigation, knowledge placement, information design, workflow construction, AI/tool routing, and hygiene validation. No single agent is supposed to absorb the whole system.

### Meso
Meta Ops sequences and routes; Alfred clarifies operator intent; Strategy explores options; Detective applies adversarial pressure; Knowledge Bank owns placement; Informatics owns taxonomy; Prompts/Workflows owns reusable execution patterns; AI Handling advises model/tool routing; Hygiene checks structural integrity. Validators create controlled overlap.

### Micro
The activation index pairs Alfred with Meta Ops, Meta Ops with Detective, Strategy with Detective, Knowledge Bank with Informatics, Prompts/Workflows with Meta Ops, AI Handling with Meta Ops, and Hygiene with Detective. The swarm canon further constrains every handoff with role, state, target, prerequisites, next action, and unresolved risk.

## Key Claims
- claim_id: A01; claim: The nine-agent seed set has explicit role summaries, KB roots, and default validators.; source_pointer: AGENT_INDEX.md#Final-v1-first-wave-activation-map; confidence: high; claim_label: source_backed_summary
- claim_id: A02; claim: Operational state, not role name, determines permission.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Default-operating-stance; confidence: high; claim_label: source_backed_summary
- claim_id: A03; claim: Overlap is bounded by ownership and validator pairings rather than unrestricted multi-agent concurrency.; source_pointer: AGENT_INDEX.md#Hard-overlap-reminders; confidence: high; claim_label: source_backed_summary

## Routes Here
- question: Which agent should handle a bounded execution task?; leads_to: wiki/entities/first-wave-agent-roster.md; rationale: start with activation roles and default validators.
- question: Why are agents both isolated and redundant?; leads_to: wiki/concepts/bounded-redundant-overlap.md; rationale: overlap is a validation resilience mechanism.
- related_page: wiki/summaries/resilient-iterative-orchestration.md; relation: workflow realization of the role/state model.

## Uncertainty / Raw Source Reopen Triggers
- id: U-A01; description: Mirrored OpenClaw trees and historical seed files may not all represent the final runtime surface.; source_pointer: KB_STARTING_SOURCE_MAP.md#Authority-order-summary; proposed_handling: audit_item
- id: U-A02; description: Domain-master agents are explicitly future or companion work, not part of the nine-agent seed set.; source_pointer: AGENT_INDEX.md#Domain-axis-note; proposed_handling: leave_as_gap
