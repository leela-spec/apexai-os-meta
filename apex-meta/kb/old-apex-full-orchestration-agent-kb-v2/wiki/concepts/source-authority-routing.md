---
title: Source Authority Routing
page_type: concept
kb_slug: old-apex-full-orchestration-agent-kb-v2
concept_slug: source-authority-routing
source_refs: [{source_id: source-184e996257212fbb, source_path: raw/other/managed/knowledge/KB_STARTING_SOURCE_MAP.md, source_hash: NA, source_pointer: Source classes and authority order, source_storage_mode: copy_into_kb}]
created_at: 2026-07-10T22:10:00Z
updated_at: 2026-07-10T22:10:00Z
confidence: high
claim_label: source_backed_summary
status: active
---
# Source Authority Routing
## Definition
Route evidence according to source class and authority before treating it as doctrine.
## Operating Rules
- final-system surfaces establish current implementation truth;
- binding locks govern decisions where implementation is silent;
- staging and research remain evidence-only;
- conflicts are exposed, not averaged.
## Adaptive Ranked Source Set
- source_id: source-184e996257212fbb; rationale: direct authority map; coverage: classes, precedence, conflict handling.
## Macro / Meso / Micro
### Macro
Authority routing prevents a persuasive historical document from silently overriding current truth. It gives the next LLM a stable rule for distinguishing implementation evidence, binding decisions, operator rulings, governance evidence, and research that is useful only as support.
### Meso
Classify source, compare against higher-authority surfaces, and route conflict to validation or operator decision. The comparison must preserve both claims, explain the authority difference, and identify whether the disagreement affects runtime behavior, permissions, source custody, or only explanatory prose.
### Micro
Preserve source path, exact claim pointer, authority label, conflict, risk, and required disposition. A micro-level record is complete only when a later reviewer can reopen the raw file and reproduce why the claim was accepted, downgraded, or left unresolved.
## Key Claims
- claim_id: SA01; claim: Source class determines how evidence may be used and whether it can be a runtime patch target.; source_pointer: KB_STARTING_SOURCE_MAP.md#Source-classes; confidence: high; claim_label: source_backed_summary
- claim_id: SA02; claim: Lower-authority sources must not silently override higher-authority sources.; source_pointer: KB_STARTING_SOURCE_MAP.md#Conflict-handling; confidence: high; claim_label: source_backed_summary
## Routes Here
- question: How should contradictory files be handled?; leads_to: wiki/audit/high-impact-conflict-register.md; rationale: conflict disposition.
- related_page: wiki/summaries/failure-patterns-and-conflicts.md; relation: failure prevention.
## Uncertainty / Raw Source Reopen Triggers
- id: U-SA01; description: Historical source labels may be incomplete; classify conservatively.; source_pointer: KB_STARTING_SOURCE_MAP.md; proposed_handling: audit_item
