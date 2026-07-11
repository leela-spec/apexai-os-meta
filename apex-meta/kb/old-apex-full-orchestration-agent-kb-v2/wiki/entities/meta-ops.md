---
title: Meta Ops: Operational Meta-Agent Layer
page_type: entity
kb_slug: old-apex-full-orchestration-agent-kb-v2
entity_slug: meta-ops
source_refs: [{source_id: source-8c534a90902556f2, source_path: raw/other/managed/agents/AGENT_INDEX.md, source_hash: 9e02b3849e58a9175f7dac4494e26e5a20f22632c65c906db351f252b08365f6, source_pointer: Final v1 first-wave activation map; Default routing; Hard overlap reminders, source_storage_mode: copy_into_kb}, {source_id: source-05bc8d6b022c9444, source_path: raw/other/managed/rules/AGENT_SWARM_INTERACTION_CANON.md, source_hash: f849f642eecfc16e377e69c92dcf1b3557d058012176f1398255b5b3b054f9fd, source_pointer: Default operating stance; Delegation rules; Handoff rules, source_storage_mode: copy_into_kb}]
created_at: 2026-07-10T22:10:00Z
updated_at: 2026-07-11T10:00:00Z
confidence: mixed
claim_label: source_backed_summary
status: active
---
# Meta Ops: Operational Meta-Agent Layer

## Purpose and Scope
Meta Ops is the Old Apex execution coordinator: it activates bounded work, controls sequence, and routes handoffs. For a Claude implementation, use it as an operational orchestration layer, not as the entire architecture or a substitute for strategy, validation, durable knowledge placement, or operator priorities.

## Decision / Use Guidance
Prefer a Meta Ops-like coordinator after intake has made the task concrete. Require it to emit role, state, target, next action, prerequisites, and unresolved risk; send high-risk or weak-evidence work to Meta Detective. Do not give it unilateral authority to set personal priorities, choose final strategy, or approve its own work.

## Adaptive Ranked Source Set
- source_id: source-8c534a90902556f2; rationale: primary activation authority; coverage: Meta Ops mandate, default route, and explicit non-ownership boundaries.
- source_id: source-05bc8d6b022c9444; rationale: managed coordination law; coverage: state-first permissions, delegation conditions, and handoff fields.

## Macro / Meso / Micro
### Macro
The coordinator makes one visible execution spine rather than an undifferentiated swarm. This is a source-backed design pattern for Claude orchestration, while the choice of Claude as runtime is an operator implementation directive, not historical runtime evidence.
### Meso
Meta Ops sequences bounded tasks across the specialized roles: it starts concrete work, sends strategy choices to Meta Strategy, risk and drift checks to Meta Detective, and durable knowledge work to the Knowledge Bank/Informatics pair. This preserves complementary ownership rather than consolidating it.
### Micro
For every material handoff, the canon requires current role/state, bounded target, intended next role or state, inputs/prerequisites, expected action, and unresolved risk. Meta Ops' default validator is Meta Detective; the state model permits BUILD -> VERIFY, loop-back VERIFY -> BUILD, and escalation/approval VERIFY -> LOCK.

## Overlap and Evidence
Two independent managed sources reinforce the same pattern: `AGENT_INDEX.md` names Meta Ops as sequence/handoff coordinator and Meta Detective as validator, while `AGENT_SWARM_INTERACTION_CANON.md` defines the state-first delegation and handoff constraints. This is strong evidence for coordinator-plus-independent-review; it is not evidence that every historical workflow or PMKB/PD artifact belongs inside the coordinator.

## Alternatives Ranked by Use Case
| Rank | Option | When it wins | Disqualifier |
|---|---|---|---|
| 1 | Meta Ops-style coordinator plus specialist routes | Concrete multi-step Claude task with explicit acceptance criteria | Do not use as sole strategy or verification authority. |
| 2 | Alfred intake then Meta Ops | Operator request remains ambiguous or priority-bound | Adds avoidable routing for already-bounded work. |
| 3 | Single bounded executor | Simple, local, low-risk work | Loses the independent review and handoff trace needed for high-risk work. |

## Key Claims
- claim_id: MO01; claim: Meta Ops orchestrates but does not own final strategy or adversarial validation.; source_pointer: AGENT_INDEX.md#Hard-overlap-reminders; confidence: high; claim_label: source_backed_summary
- claim_id: MO02; claim: Meta Ops is the default starting point for concrete bounded execution.; source_pointer: AGENT_INDEX.md#Default-routing; confidence: high; claim_label: source_backed_summary
- claim_id: MO03; claim: Delegation is valid only when work, criteria, context, constraints, and return format are explicit enough for the receiver to act without hidden reasoning.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Delegation-rules; confidence: high; claim_label: source_backed_summary
- claim_id: MO04; claim: A valid handoff carries role, state, target, next role/state, prerequisites, expected action, and unresolved risk.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Handoff-rules; confidence: high; claim_label: source_backed_summary

## Routes Here
- question: Which component sequences a concrete bounded Claude task?; leads_to: wiki/entities/meta-detective.md; rationale: pair orchestration with independent validation.
- question: How should a Claude handoff be structured?; leads_to: wiki/summaries/resilient-iterative-orchestration.md; rationale: workflow realization of the role/state law.
- question: Where should reusable PMKB/PD workflow material sit?; leads_to: wiki/entities/special-ops-prompts-workflows.md; rationale: Meta Ops routes reusable patterns but does not own them.

## Uncertainty / Raw Source Reopen Triggers
- id: U-MO01; description: Historical orchestration flows may use different coordinator names.; source_pointer: HOLDING_ORCHESTRATION_FLOW.md; proposed_handling: revisit_source
- id: U-MO02; description: PMKB/PD terminology is an operator-identified operational meta-agent concern, but this Phase 1 evidence set does not establish its exact artifact boundaries or authority; do not promote it as the whole Claude architecture.; source_pointer: ingest-analysis/phase1-agent-architecture.md#Source-Summary; proposed_handling: revisit_source
