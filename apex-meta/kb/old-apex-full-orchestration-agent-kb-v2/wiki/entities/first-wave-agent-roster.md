---
title: First-Wave Agent Roster
page_type: entity
kb_slug: old-apex-full-orchestration-agent-kb-v2
entity_slug: first-wave-agent-roster
source_refs:
  - {source_id: source-8c534a90902556f2, source_path: raw/other/managed/agents/AGENT_INDEX.md, source_hash: NA, source_pointer: Final v1 first-wave activation map, source_storage_mode: copy_into_kb}
  - {source_id: source-05bc8d6b022c9444, source_path: raw/other/managed/rules/AGENT_SWARM_INTERACTION_CANON.md, source_hash: NA, source_pointer: Role-state interaction rules, source_storage_mode: copy_into_kb}
created_at: 2026-07-10T22:05:00Z
updated_at: 2026-07-10T22:05:00Z
confidence: high
claim_label: source_backed_summary
status: active
---
# First-Wave Agent Roster

## Definition
The first-wave roster is the named activation set: Alfred, Meta Ops, Meta Strategy, Meta Detective, Knowledge Bank, Informatics Design, Prompts/Workflows, AI Handling/Routing, and Hygiene Clean.

## Operating Rules
- roles are accountability, not permission;
- operational state is explicit;
- every agent has a bounded surface and default validator;
- overlap must preserve ownership boundaries.

## Adaptive Ranked Source Set
- source_id: source-8c534a90902556f2; rationale: direct roster authority; coverage: all nine agents and routing defaults.
- source_id: source-05bc8d6b022c9444; rationale: governing interaction law; coverage: role/state and delegation constraints.

## Macro / Meso / Micro
### Macro
The roster separates intake, execution, strategy, detection, knowledge, structure, workflow, routing, and hygiene.
### Meso
Validators form deliberate overlap: Meta Ops is checked by Detective; Knowledge Bank by Informatics; Hygiene by Detective; operational routing by Meta Ops.
### Micro
The activation index identifies the seed path, KB root, and default validator for each named agent. Those paths are the first navigation points for another LLM.

## Key Claims
- claim_id: E01; claim: The roster contains nine first-wave agents.; source_pointer: AGENT_INDEX.md#Final-v1-first-wave-activation-map; confidence: high; claim_label: source_backed_summary
- claim_id: E02; claim: Alfred starts operator-context requests while Meta Ops starts bounded execution requests.; source_pointer: AGENT_INDEX.md#Default-routing; confidence: high; claim_label: source_backed_summary
- claim_id: E03; claim: Domain masters are not part of the first-wave seed set.; source_pointer: AGENT_INDEX.md#Domain-axis-note; confidence: high; claim_label: source_backed_summary

## Routes Here
- question: Which agent owns knowledge placement?; leads_to: raw/other/managed/agents/special_ops__knowledge_bank.md; rationale: roster route.
- question: Which agent validates drift?; leads_to: raw/other/managed/agents/meta_detective.md; rationale: validator route.

## Uncertainty / Raw Source Reopen Triggers
- id: U-E01; description: Mirrored agent directories may contain names not in the first-wave roster.; source_pointer: KB_STARTING_SOURCE_MAP.md#Current-seed-sources; proposed_handling: leave_as_gap
