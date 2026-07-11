---
title: Meta Detective: Independent Validation Lane
page_type: entity
kb_slug: old-apex-full-orchestration-agent-kb-v2
entity_slug: meta-detective
source_refs: [{source_id: source-8c534a90902556f2, source_path: raw/other/managed/agents/AGENT_INDEX.md, source_hash: 9e02b3849e58a9175f7dac4494e26e5a20f22632c65c906db351f252b08365f6, source_pointer: Final v1 first-wave activation map; Default routing; Hard overlap reminders, source_storage_mode: copy_into_kb}, {source_id: source-c88ec66204ff70b9, source_path: raw/other/managed/agent_kb/meta_detective/ESSENCE.md, source_hash: f7f50182d6a7b3ebcf4e458ece92ae8335c6a888777b58c6f50c4a2421d0fa2f, source_pointer: Purpose; Agent boundary; Core constraints; Default verdicts; Detective to Hygiene boundary, source_storage_mode: copy_into_kb}, {source_id: source-5deee57ba0cf6861, source_path: raw/other/managed/agent_kb/meta_detective/BEST_PRACTICES.md, source_hash: 296d3e93b079a3752a0807b48088eea80e4718312a5b29bb410ef75a3a933353, source_pointer: DET-BP-001 through DET-BP-009, source_storage_mode: copy_into_kb}]
created_at: 2026-07-10T22:10:00Z
updated_at: 2026-07-11T12:00:00Z
confidence: high
claim_label: source_backed_summary
status: active
---
# Meta Detective: Independent Validation Lane

## Purpose and Scope
Meta Detective is the adversarial validation lane: it tests authority, evidence, plausibility, contradiction, role drift, risk, and escalation readiness before an output is trusted or promoted. It validates and challenges; it does not implement the fix it recommends. For Claude orchestration, use it as an independent review function, not as an extra executor or generic critic.

## Decision / Use Guidance
Route a task to Detective when evidence is weak or contested, risk is high, sources conflict, a reusable handoff needs review, candidate material may become accepted knowledge, or a polished output has not been independently checked. Require a verdict packet that names checked evidence, finding class, confidence, owner route, and stop condition.

## Adaptive Ranked Source Set
- source_id: source-c88ec66204ff70b9; rationale: accepted boundary doctrine; coverage: ownership, exclusions, constraints, modes, and verdicts.
- source_id: source-5deee57ba0cf6861; rationale: accepted practices; coverage: authority-first review, evidence checks, stop conditions, and finding routing.
- source_id: source-8c534a90902556f2; rationale: activation authority; coverage: route trigger and non-overlap with Meta Ops.

## Macro / Meso / Micro
### Macro
Detective protects the system from plausible but unsupported progress. Its value is pressure on the precise assumption, authority conflict, or boundary failure that could make an output unsafe.

### Meso
It classifies evidence, contradiction, boundary, risk, and hygiene findings before producing a verdict. Structural QA routes to Hygiene; orchestration implications route to Meta Ops; recommendation revision routes to Meta Strategy; KB placement/canon status routes to Knowledge Bank.

### Micro
Its five internal modes are evidence verification, contradiction/logic audit, boundary/authority review, risk/failure-mode red team, and verdict synthesis. They are internal modes, not separate agents. Outputs are `pass`, `revise`, `hold`, `needs_input`, or `escalate`; a verified partial verdict is preferable to unsupported approval.

## Overlap and Evidence
Three sources converge: the activation index assigns Detective adversarial validation and a Hygiene validator; accepted doctrine excludes execution, patching, promotion, and orchestration control; accepted practices require authority-first review, named evidence, stop conditions, and classified findings. This repetition supports an independent verifier rather than a reviewer-executor hybrid.

## Alternatives Ranked by Use Case
| Rank | Design | Wins when | Disqualifier |
|---|---|---|---|
| 1 | Independent Detective-style verdict lane | High-risk, contested, reusable, or promotion-bound work | Needs a distinct reviewer and handoff. |
| 2 | Narrow evidence check | One source/pointer claim needs confirmation | Insufficient for mixed authority, logic, and risk failures. |
| 3 | Executor self-review | Never as final approval on load-bearing work | Violates the defined validator/executor boundary. |

## Key Claims
- claim_id: MD01; claim: Meta Detective validates and challenges but does not execute the fix it recommends.; source_pointer: meta_detective/ESSENCE.md#Agent-boundary; confidence: high; claim_label: source_backed_summary
- claim_id: MD02; claim: Detective owns authority challenge, evidence-before-approval, contradiction surfacing, drift challenge, failure-mode pressure, and escalation recommendations.; source_pointer: meta_detective/ESSENCE.md#Owns; confidence: high; claim_label: source_backed_summary
- claim_id: MD03; claim: A coherent or polished artifact is not evidence; approval requires a check against an identified source, state, diff, test, schema, criterion, or governing surface.; source_pointer: meta_detective/BEST_PRACTICES.md#DET-BP-002; confidence: high; claim_label: source_backed_summary
- claim_id: MD04; claim: Detective should hold or escalate when required evidence is missing, primary sources conflict, failure repeats, or confidence is unsafe.; source_pointer: meta_detective/BEST_PRACTICES.md#DET-BP-005; confidence: high; claim_label: source_backed_summary
- claim_id: MD05; claim: Hygiene owns structural QA while Detective owns adversarial plausibility, authority, contradiction, assumption, risk, and drift challenge.; source_pointer: meta_detective/ESSENCE.md#Detective-to-Hygiene-boundary; confidence: high; claim_label: source_backed_summary

## Routes Here
- question: How should Claude review high-risk work without self-approval?; leads_to: wiki/concepts/explicit-handoff-continuity.md; rationale: review returns a legible verdict and disposition.
- question: Who validates Meta Ops orchestration?; leads_to: wiki/entities/meta-ops.md; rationale: Detective is Meta Ops' default validator.
- question: Is a defect structural or adversarial?; leads_to: wiki/entities/special-ops-hygiene-clean.md; rationale: classify separately and route to the owning lane.

## Uncertainty / Raw Source Reopen Triggers
- id: U-MD01; description: The five Detective modes are accepted internal modes, not separately managed agents or execution authority; do not compile them as independent Claude agents without new evidence.; source_pointer: meta_detective/ESSENCE.md#Accepted-internal-Detective-modes; proposed_handling: revisit_source
- id: U-MD02; description: The source's staging status and review date are historical evidence; reopen doctrine before treating them as current Claude runtime governance.; source_pointer: meta_detective/ESSENCE.md#Evidence-and-status; proposed_handling: revisit_source
