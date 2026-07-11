---
title: Special Ops Prompts and Workflows
page_type: entity
kb_slug: old-apex-full-orchestration-agent-kb-v2
entity_slug: special-ops-prompts-workflows
source_refs: [{source_id: source-8c534a90902556f2, source_path: raw/other/managed/agents/AGENT_INDEX.md, source_hash: NA, source_pointer: Prompts/Workflows role and routing, source_storage_mode: copy_into_kb}, {source_id: source-14e5fbc383dd73e1, source_path: raw/other/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md, source_hash: NA, source_pointer: mistakes, source_storage_mode: copy_into_kb}]
created_at: 2026-07-10T22:10:00Z
updated_at: 2026-07-10T22:10:00Z
confidence: high
claim_label: source_backed_summary
status: active
---
# Special Ops Prompts and Workflows
## Definition
Reusable prompt, workflow, and patchspec patterns.
## Adaptive Ranked Source Set
- source_id: source-8c534a90902556f2; rationale: activation index; coverage: role and Meta Ops validator.
- source_id: source-14e5fbc383dd73e1; rationale: failure evidence; coverage: reusable-pattern mistakes.
## Macro / Meso / Micro
### Macro
Turns repeated execution lessons into reusable bounded patterns.
### Meso
Defines inputs, steps, handoffs, outputs, and validation points.
### Micro
Produces prompt packets or patch specifications that another executor can follow without hidden reasoning.
## Key Claims
- claim_id: PW01; claim: Prompts/Workflows owns reusable execution patterns, not orchestration authority.; source_pointer: AGENT_INDEX.md#Hard-overlap-reminders; confidence: high; claim_label: source_backed_summary
- claim_id: PW02; claim: Meta Ops validates workflow routing.; source_pointer: AGENT_INDEX.md#Final-v1-first-wave-activation-map; confidence: high; claim_label: source_backed_summary
## Routes Here
- question: Where should a repeated procedure become reusable?; leads_to: wiki/summaries/resilient-iterative-orchestration.md; rationale: workflow synthesis.
## Uncertainty / Raw Source Reopen Triggers
- id: U-PW01; description: Historical patch patterns may be obsolete; preserve them as evidence until revalidated.; source_pointer: managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md; proposed_handling: revisit_source
