---
title: Highest-Impact Conflict Register
page_type: audit_item
kb_slug: old-apex-full-orchestration-agent-kb-v2
source_refs:
  - {source_id: source-184e996257212fbb, source_path: raw/other/managed/knowledge/KB_STARTING_SOURCE_MAP.md, source_hash: NA, source_pointer: Authority order summary and conflict handling, source_storage_mode: copy_into_kb}
created_at: 2026-07-10T22:05:00Z
updated_at: 2026-07-10T22:05:00Z
confidence: mixed
claim_label: operator_question
status: needs_review
---
# Highest-Impact Conflict Register

## Adaptive Ranked Source Set
- source_id: source-184e996257212fbb; rationale: defines authority conflict handling; coverage: source classes and precedence.
- source_id: source-05bc8d6b022c9444; rationale: defines role/state conflicts; coverage: self-review and permission boundaries.

## Macro / Meso / Micro
### Macro
Conflicts are highest impact when they can change what the system treats as authoritative truth or who is allowed to change it.
### Meso
Priority 1: final-system surface versus mirror/staging material. Priority 2: role authority versus operational state. Priority 3: builder versus verifier responsibility. Priority 4: conservative single-flow doctrine versus historical swarm experiments. Priority 5: source custody versus copied or summarized evidence.
### Micro
Each conflict retains both sides, cites exact paths, identifies the higher-authority source, states operational risk, and names the decision required before promotion.

## Key Claims
- claim_id: C01; claim: Final-system surfaces outrank lower-authority mirrors for current implementation truth.; source_pointer: KB_STARTING_SOURCE_MAP.md#Authority-order-summary; confidence: high; claim_label: source_backed_summary
- claim_id: C02; claim: A role label cannot override BUILD, VERIFY, or LOCK state.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#State-assignment-rules; confidence: high; claim_label: source_backed_summary
- claim_id: C03; claim: A builder cannot self-promote an artifact as verified.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Forbidden-transitions; confidence: high; claim_label: source_backed_summary

## Routes Here
- question: Which disagreement should be resolved first?; leads_to: wiki/summaries/failure-patterns-and-conflicts.md; rationale: impact framing.
- question: What evidence decides a conflict?; leads_to: wiki/concepts/source-authority-routing.md; rationale: authority routing.

## Uncertainty / Raw Source Reopen Triggers
- id: U-C01; description: Exact severity scores are not defined in one authoritative source.; source_pointer: KB_STARTING_SOURCE_MAP.md; proposed_handling: ask_operator
- id: U-C02; description: Historical mirror trees may contain later or alternate decisions.; source_pointer: NewFinals/MetaHeadsKBUpdateState; proposed_handling: revisit_source
