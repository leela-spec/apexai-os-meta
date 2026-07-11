---
title: Special Ops Hygiene Clean
page_type: entity
kb_slug: old-apex-full-orchestration-agent-kb-v2
entity_slug: special-ops-hygiene-clean
source_refs: [{source_id: source-8c534a90902556f2, source_path: raw/other/managed/agents/AGENT_INDEX.md, source_hash: NA, source_pointer: Hygiene role and routing, source_storage_mode: copy_into_kb}, {source_id: source-4fdadd0a0747b26b, source_path: raw/other/managed/agent_kb/special_ops__hygiene_clean/MISTAKES.md, source_hash: NA, source_pointer: hygiene failures, source_storage_mode: copy_into_kb}]
created_at: 2026-07-10T22:10:00Z
updated_at: 2026-07-10T22:10:00Z
confidence: high
claim_label: source_backed_summary
status: active
---
# Special Ops Hygiene Clean
## Definition
QA findings, structural correctness, pointer integrity, and cleanup safety.
## Adaptive Ranked Source Set
- source_id: source-8c534a90902556f2; rationale: activation index; coverage: role and Detective validator.
- source_id: source-4fdadd0a0747b26b; rationale: direct hygiene evidence; coverage: structural and pointer failure patterns.
## Macro / Meso / Micro
### Macro
Protects the system from stale, malformed, or untraceable artifacts.
### Meso
Checks indexes, pointers, file structure, and cleanup boundaries.
### Micro
Reports defects and routes governance-critical issues without silently mutating truth.
## Key Claims
- claim_id: HC01; claim: Hygiene audits structural correctness and pointer integrity.; source_pointer: AGENT_INDEX.md#Final-v1-first-wave-activation-map; confidence: high; claim_label: source_backed_summary
- claim_id: HC02; claim: Detective validates plausibility and drift while Hygiene validates structure.; source_pointer: AGENT_INDEX.md#Hard-overlap-reminders; confidence: high; claim_label: source_backed_summary
## Routes Here
- question: Which agent handles broken pointers or stale state?; leads_to: wiki/summaries/failure-patterns-and-conflicts.md; rationale: failure evidence.
## Uncertainty / Raw Source Reopen Triggers
- id: U-HC01; description: Historical hygiene reports may contain already-resolved defects.; source_pointer: managed/agent_kb/special_ops__hygiene_clean/MISTAKES.md; proposed_handling: revisit_source
