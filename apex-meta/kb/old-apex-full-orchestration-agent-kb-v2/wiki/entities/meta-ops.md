---
title: Meta Ops
page_type: entity
kb_slug: old-apex-full-orchestration-agent-kb-v2
entity_slug: meta-ops
source_refs: [{source_id: source-8c534a90902556f2, source_path: raw/other/managed/agents/AGENT_INDEX.md, source_hash: NA, source_pointer: Meta Ops role and routing, source_storage_mode: copy_into_kb}]
created_at: 2026-07-10T22:10:00Z
updated_at: 2026-07-10T22:10:00Z
confidence: high
claim_label: source_backed_summary
status: active
---
# Meta Ops
## Definition
Orchestration, activation, sequence control, and handoff routing.
## Adaptive Ranked Source Set
- source_id: source-8c534a90902556f2; rationale: activation index; coverage: role, validator, and route boundaries.
## Macro / Meso / Micro
### Macro
Maintains the visible execution spine.
### Meso
Sequences bounded work and routes it to specialized agents.
### Micro
Uses explicit handoff fields and sends its own orchestration to Meta Detective for validation.
## Key Claims
- claim_id: MO01; claim: Meta Ops orchestrates but does not own final strategy or adversarial validation.; source_pointer: AGENT_INDEX.md#Hard-overlap-reminders; confidence: high; claim_label: source_backed_summary
- claim_id: MO02; claim: Meta Ops is the default starting point for concrete bounded execution.; source_pointer: AGENT_INDEX.md#Default-routing; confidence: high; claim_label: source_backed_summary
## Routes Here
- question: Which agent sequences a bounded task?; leads_to: wiki/entities/meta-detective.md; rationale: validator pairing.
## Uncertainty / Raw Source Reopen Triggers
- id: U-MO01; description: Historical orchestration flows may use different coordinator names.; source_pointer: HOLDING_ORCHESTRATION_FLOW.md; proposed_handling: revisit_source
