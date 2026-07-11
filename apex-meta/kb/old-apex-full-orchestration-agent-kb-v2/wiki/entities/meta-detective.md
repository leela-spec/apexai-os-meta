---
title: Meta Detective
page_type: entity
kb_slug: old-apex-full-orchestration-agent-kb-v2
entity_slug: meta-detective
source_refs: [{source_id: source-8c534a90902556f2, source_path: raw/other/managed/agents/AGENT_INDEX.md, source_hash: NA, source_pointer: Meta Detective role and routing, source_storage_mode: copy_into_kb}, {source_id: source-ed16187e00eb7e87, source_path: raw/other/managed/agent_kb/meta_detective/MISTAKES.md, source_hash: NA, source_pointer: failure ledger, source_storage_mode: copy_into_kb}]
created_at: 2026-07-10T22:10:00Z
updated_at: 2026-07-10T22:10:00Z
confidence: high
claim_label: source_backed_summary
status: active
---
# Meta Detective
## Definition
Adversarial validation, drift detection, plausibility pressure, and escalation pressure.
## Adaptive Ranked Source Set
- source_id: source-8c534a90902556f2; rationale: activation index; coverage: role and validators.
- source_id: source-ed16187e00eb7e87; rationale: direct failure evidence; coverage: mistakes and drift patterns.
## Macro / Meso / Micro
### Macro
Protects the system from plausible but unsupported progress.
### Meso
Checks authority, evidence, contradictions, and drift across agent outputs.
### Micro
Rejects weak handoffs, identifies unresolved risks, and routes escalation without silently rewriting the artifact.
## Key Claims
- claim_id: MD01; claim: Detective is the default validator for Meta Ops and Strategy.; source_pointer: AGENT_INDEX.md#Final-v1-first-wave-activation-map; confidence: high; claim_label: source_backed_summary
- claim_id: MD02; claim: Detective review is review-first, not build-first.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#VERIFIER; confidence: high; claim_label: source_backed_summary
## Routes Here
- question: Which agent tests plausibility and drift?; leads_to: wiki/summaries/failure-patterns-and-conflicts.md; rationale: failure routing.
## Uncertainty / Raw Source Reopen Triggers
- id: U-MD01; description: Historical Detective files may contain unresolved or superseded failure claims.; source_pointer: managed/agent_kb/meta_detective/MISTAKES.md; proposed_handling: revisit_source
