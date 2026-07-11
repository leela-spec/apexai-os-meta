---
title: Special Ops AI Handling and Routing
page_type: entity
kb_slug: old-apex-full-orchestration-agent-kb-v2
entity_slug: special-ops-ai-handling-routing
source_refs: [{source_id: source-8c534a90902556f2, source_path: raw/other/managed/agents/AGENT_INDEX.md, source_hash: NA, source_pointer: AI Handling/Routing role and routing, source_storage_mode: copy_into_kb}]
created_at: 2026-07-10T22:10:00Z
updated_at: 2026-07-10T22:10:00Z
confidence: high
claim_label: source_backed_summary
status: active
---
# Special Ops AI Handling and Routing
## Definition
Advisory model and tool routing posture.
## Adaptive Ranked Source Set
- source_id: source-8c534a90902556f2; rationale: activation index; coverage: role, KB root, and Meta Ops validator.
## Macro / Meso / Micro
### Macro
Keeps model and tool choices aligned with quality, cost, and safety.
### Meso
Advises route selection without becoming runtime configuration authority.
### Micro
Identifies when model/tool posture materially affects execution and returns an advisory packet to Meta Ops.
## Key Claims
- claim_id: AR01; claim: AI Handling/Routing is advisory and is not config authority.; source_pointer: AGENT_INDEX.md#Hard-overlap-reminders; confidence: high; claim_label: source_backed_summary
- claim_id: AR02; claim: Meta Ops remains the validator for routing posture.; source_pointer: AGENT_INDEX.md#Final-v1-first-wave-activation-map; confidence: high; claim_label: source_backed_summary
## Routes Here
- question: Does model or tool posture change the route?; leads_to: wiki/entities/meta-ops.md; rationale: routing decision returns to coordinator.
## Uncertainty / Raw Source Reopen Triggers
- id: U-AR01; description: External research may describe capabilities not present in the final runtime surface.; source_pointer: KB_STARTING_SOURCE_MAP.md#Evidence-only-staging-source; proposed_handling: audit_item
