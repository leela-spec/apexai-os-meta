---
title: Failure Patterns and Highest-Impact Conflicts
page_type: summary
kb_slug: old-apex-full-orchestration-agent-kb-v2
summary_slug: failure-patterns-and-conflicts
source_refs:
  - {source_id: source-184e996257212fbb, source_path: raw/other/managed/knowledge/KB_STARTING_SOURCE_MAP.md, source_hash: NA, source_pointer: Conflict handling and anti-canonization safeguards, source_storage_mode: copy_into_kb}
  - {source_id: source-ed16187e00eb7e87, source_path: raw/other/managed/agent_kb/meta_detective/MISTAKES.md, source_hash: NA, source_pointer: failure ledger, source_storage_mode: copy_into_kb}
  - {source_id: source-4fdadd0a0747b26b, source_path: raw/other/managed/agent_kb/special_ops__hygiene_clean/MISTAKES.md, source_hash: NA, source_pointer: hygiene failures, source_storage_mode: copy_into_kb}
created_at: 2026-07-10T22:05:00Z
updated_at: 2026-07-10T22:05:00Z
confidence: mixed
claim_label: source_backed_summary
status: active
---
# Failure Patterns and Highest-Impact Conflicts

## Core Summary
The highest-impact failures are authority drift, self-review, weak handoff continuity, source-custody loss, and candidate-to-canon leakage. They are dangerous because they make a locally plausible result appear globally authoritative.

## Adaptive Ranked Source Set
- source_id: source-184e996257212fbb; rationale: explicit authority and anti-canonization rules; coverage: source classes and precedence.
- source_id: source-ed16187e00eb7e87; rationale: adversarial failure evidence; coverage: detective mistakes and drift patterns.
- source_id: source-4fdadd0a0747b26b; rationale: structural failure evidence; coverage: hygiene, pointers, and cleanup failures.

## Macro / Meso / Micro
### Macro
The system fails when evidence, interpretation, approval, and runtime truth collapse into one undifferentiated stream.
### Meso
This appears as unclear authority, role conflation, silent self-review, ambiguous handoffs, stale indexes, and broad edits that cannot be traced to a source or decision.
### Micro
Indicators include missing source pointers, staging prose treated as doctrine, a builder declaring its own work verified, an agent continuing from an unclear handoff, or a mirror overriding a final-system surface.

## Key Claims
- claim_id: F01; claim: Source, candidate, canon, validation, and promotion are separate states and surfaces.; source_pointer: KB_STARTING_SOURCE_MAP.md#Anti-canonization-safeguards; confidence: high; claim_label: source_backed_summary
- claim_id: F02; claim: Build and review of the same load-bearing change must remain separated.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Role-switching-and-separation-rules; confidence: high; claim_label: source_backed_summary
- claim_id: F03; claim: Conflicts between authority classes must not be averaged.; source_pointer: KB_STARTING_SOURCE_MAP.md#Conflict-handling; confidence: high; claim_label: source_backed_summary

## Routes Here
- question: Which conflicts should be handled first?; leads_to: wiki/audit/high-impact-conflict-register.md; rationale: ranked conflict register.
- question: How do we distinguish source truth from candidate doctrine?; leads_to: wiki/concepts/source-authority-routing.md; rationale: authority routing.
- related_page: wiki/summaries/agent-architecture.md; relation: failures arise at role boundaries.

## Uncertainty / Raw Source Reopen Triggers
- id: U-F01; description: Historical mistakes files mix resolved, repeated, and superseded failures.; source_pointer: managed/agent_kb/*/MISTAKES.md; proposed_handling: revisit_source
- id: U-F02; description: Impact ranking is an evidence-based prioritization, not a canonical severity scale from one source.; source_pointer: KB_STARTING_SOURCE_MAP.md; proposed_handling: audit_item
