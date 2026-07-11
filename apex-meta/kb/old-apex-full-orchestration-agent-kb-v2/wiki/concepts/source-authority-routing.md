---
title: Source Authority, Candidate Status, and Target Routing
page_type: concept
kb_slug: old-apex-full-orchestration-agent-kb-v2
concept_slug: source-authority-routing
source_refs: [{source_id: source-184e996257212fbb, source_path: raw/other/managed/knowledge/KB_STARTING_SOURCE_MAP.md, source_hash: 68be02eec9889f1ae0346daa01f08e37cb7236583652a064603a5dde8668f7af, source_pointer: Source classes; Authority order summary; Evidence-only staging and source boundary; Anti-canonization safeguards, source_storage_mode: copy_into_kb}, {source_id: source-530a02df0c8f3de7, source_path: raw/other/managed/agent_kb/special_ops__knowledge_bank/ESSENCE.md, source_hash: fe4ee9eb5df1d0d1d7148cdb1a3f4defeff7e2bfff9f514ae8181104ddcc4589, source_pointer: Agent boundary; Core constraints; Source basis, source_storage_mode: copy_into_kb}]
created_at: 2026-07-10T22:05:00Z
updated_at: 2026-07-11T12:15:00Z
confidence: high
claim_label: source_backed_summary
status: active
---
# Source Authority, Candidate Status, and Target Routing

## Purpose and Scope
This page tells an AI what a source may support, where its content may be routed, and what it must not be promoted into. It prevents source text, historical staging, candidate queues, and accepted doctrine from being treated as the same truth class. It does not itself approve promotion or select Claude runtime behavior.

## Decision / Use Guidance
Classify every material source before using it. Prefer final-system surfaces, binding locks, and required operator decisions over managed/seed evidence; never average conflicts across classes. Route unresolved conflicts to validation, escalation, or an operator decision. Keep source evidence and candidates visible, but do not convert either into accepted doctrine by summarizing it fluently.

## Adaptive Ranked Source Set
- source_id: source-184e996257212fbb; rationale: shared authority and routing map; coverage: classes, precedence, conflict, target routing, and anti-canonization.
- source_id: source-530a02df0c8f3de7; rationale: Knowledge Bank operational boundary; coverage: placement/lifecycle ownership and candidate-only safeguards.

## Macro / Meso / Micro
### Macro
Knowledge is a controlled promotion pipeline, not a flat document collection. The system separates evidence, candidate, accepted doctrine, validation, and promotion so retrieval does not accidentally manufacture runtime truth.

### Meso
Final-system surfaces describe current runtime truth; binding locks constrain architecture; operator decisions supply required human authority; governance and seed sources support implementation; staging/research remains evidence-only. Knowledge Bank owns placement and lifecycle routing, while it does not own final strategy, promotion approval, or shared-governance mutation.

### Micro
Use `LEARNING_QUEUE.md` for candidate capture only. Route rich accepted doctrine to the appropriate per-agent KB after governed validation; keep shared governance for source classes, promotion packaging, overlap validation, and reference mapping. A lower-class source cannot silently override a higher-class source, and unresolved conflict cannot be averaged away.

## Overlap and Evidence
The source map repeats the source/candidate/canon distinction in source classes, authority order, staging boundaries, routing rules, and anti-canonization safeguards. Knowledge Bank repeats it as operational constraints: no silent canonization, no candidate/accepted-truth merge, and candidate-only learning queues. This repeated boundary is core architecture, not documentation style.

## Alternatives Ranked by Use Case
| Rank | Design | Wins when | Disqualifier |
|---|---|---|---|
| 1 | Authority-class route plus validation | Any claim that may influence durable or runtime behavior | Requires source classification. |
| 2 | Evidence-only candidate capture | Useful but unvalidated insight | Cannot be cited as accepted doctrine. |
| 3 | Merge sources into one summary | Never for conflicting or promotion-bound material | Loses provenance and creates false canon. |

## Key Claims
- claim_id: SA01; claim: Conflicting source classes must not be averaged, and lower authority may not silently override higher authority.; source_pointer: KB_STARTING_SOURCE_MAP.md#Authority-order-summary; confidence: high; claim_label: source_backed_summary
- claim_id: SA02; claim: Evidence-only staging may seed a candidate or rationale but may not become runtime truth merely by being cited or summarized.; source_pointer: KB_STARTING_SOURCE_MAP.md#Evidence-only-staging-and-source-boundary; confidence: high; claim_label: source_backed_summary
- claim_id: SA03; claim: Learning queues are candidate-only and neither runtime truth nor proof of promotion.; source_pointer: KB_STARTING_SOURCE_MAP.md#Candidate-learning; confidence: high; claim_label: source_backed_summary
- claim_id: SA04; claim: Knowledge Bank owns placement, lifecycle routing, manifests, candidate packaging, and anti-sprawl safeguards, but not direct promotion approval.; source_pointer: special_ops__knowledge_bank/ESSENCE.md#Agent-boundary-and-Core-constraints; confidence: high; claim_label: source_backed_summary

## Routes Here
- question: Can this historical Hermes material become Claude runtime logic?; leads_to: wiki/summaries/claude-orchestration-implementation-brief.md; rationale: historical blueprint evidence is not target-runtime authority.
- question: How should a candidate be passed for review?; leads_to: wiki/entities/meta-detective.md; rationale: Detective validates evidence and candidate/canon leakage.
- question: Where should a verified reusable workflow live?; leads_to: wiki/entities/special-ops-prompts-workflows.md; rationale: workflow ownership is distinct from promotion.

## Uncertainty / Raw Source Reopen Triggers
- id: U-SA01; description: This source map governs Old Apex/OpenClaw routing. Reopen operator decisions before mapping its classes directly to Claude files, tools, or permissions.; source_pointer: KB_STARTING_SOURCE_MAP.md#Scope-and-authority; proposed_handling: ask_operator
- id: U-SA02; description: A source may be authoritative evidence yet describe a historical implementation. Reopen its own status and target boundary before calling it current runtime law.; source_pointer: KB_STARTING_SOURCE_MAP.md#Evidence-only-staging-and-source-boundary; proposed_handling: revisit_source
