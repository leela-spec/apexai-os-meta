---
title: Special Ops Prompts and Workflows: Reusable Execution Patterns
page_type: entity
kb_slug: old-apex-full-orchestration-agent-kb-v2
entity_slug: special-ops-prompts-workflows
source_refs: [{source_id: source-61ddea16db778b76, source_path: raw/other/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md, source_hash: dcb817d554ff6ca32db6d499ab559decb96083f4af84bbf7b91f1acea80d58dc, source_pointer: Purpose; Agent boundary; Core doctrine; Default sequence, source_storage_mode: copy_into_kb}, {source_id: source-8c534a90902556f2, source_path: raw/other/managed/agents/AGENT_INDEX.md, source_hash: 9e02b3849e58a9175f7dac4494e26e5a20f22632c65c906db351f252b08365f6, source_pointer: Final v1 first-wave activation map; Hard overlap reminders, source_storage_mode: copy_into_kb}]
created_at: 2026-07-10T22:10:00Z
updated_at: 2026-07-11T12:15:00Z
confidence: high
claim_label: source_backed_summary
status: active
---
# Special Ops Prompts and Workflows: Reusable Execution Patterns

## Purpose and Scope
This lane owns reusable prompts, stage-gated workflows, promptflow skeletons, bounded execution sequences, and handoff templates. For Claude, it is the pattern library for repeatable work; it is not the orchestration authority, model/config authority, KB placement authority, QA authority, or promotion authority.

## Decision / Use Guidance
Use this lane when a successful bounded procedure should become reusable. Build the reusable pattern around target, scope, non-goals, source authority, output contract, and stop condition. Execute one substantial deliverable or closed file set per pass, verify it against source/file state, capture out-of-mode improvements separately, then stop or hand off.

## Adaptive Ranked Source Set
- source_id: source-61ddea16db778b76; rationale: accepted execution-pattern doctrine; coverage: ownership, gate sequence, anti-drift controls, and boundaries.
- source_id: source-8c534a90902556f2; rationale: activation and overlap authority; coverage: validator pairing and non-ownership.

## Macro / Meso / Micro
### Macro
Reusable workflow value comes from preserving control points, not from storing long prompts. The lane turns repeated execution lessons into constrained procedures that another AI can run without relying on conversational continuity.

### Meso
Stage gates place source lock and plausibility checks before scaffold/execution. Constant-frame control carries explicit state, atomic task payload, gate check, stop signal, and closure proof for high-risk promptflows. Templates support construction but cannot create governance or runtime permission.

### Micro
The default sequence is target/source lock, overload and non-goal classification, mode selection, one bounded deliverable, verification, candidate capture, and explicit stop/handoff. Diff transport fragility is handled by selecting patch, full-body, or live-edit mode, rather than pretending every change is a safe patch.

## Overlap and Evidence
The activation index says this lane owns reusable execution patterns but not orchestration authority. Its accepted doctrine independently repeats target-first, authority-before-action, verify-before-trust, bounded execution, and capture-not-smuggle. The overlap supports a narrow implementation role: patterns improve execution but do not decide what the system is authorized to do.

## Alternatives Ranked by Use Case
| Rank | Design | Wins when | Disqualifier |
|---|---|---|---|
| 1 | Stage-gated reusable workflow | A procedure repeats or drift risk is meaningful | Needs explicit source and stop conditions. |
| 2 | One-off bounded prompt | Work will not recur and scope is small | Do not promote it as general doctrine. |
| 3 | Long conversational prompt | Never for high-risk continuity | Omits explicit state, gate, and closure controls. |

## Key Claims
- claim_id: PW01; claim: This lane owns reusable prompt/workflow construction, stage-gated execution shapes, bounded handoff templates, and anti-drift promptflow scaffolds.; source_pointer: special_ops__prompts_workflows/ESSENCE.md#Agent-boundary; confidence: high; claim_label: source_backed_summary
- claim_id: PW02; claim: Target, scope, non-goals, source authority, output contract, and stop condition must be named before execution.; source_pointer: special_ops__prompts_workflows/ESSENCE.md#Core-doctrine-Target-first; confidence: high; claim_label: source_backed_summary
- claim_id: PW03; claim: High-risk promptflows carry explicit state, atomic task payload, gate check, stop signal, and closure proof instead of relying on conversational continuity.; source_pointer: special_ops__prompts_workflows/ESSENCE.md#Core-doctrine-Constant-frame-control; confidence: high; claim_label: source_backed_summary
- claim_id: PW04; claim: Out-of-mode improvements are captured rather than silently applied to the current bounded run.; source_pointer: special_ops__prompts_workflows/ESSENCE.md#Core-doctrine-Capture-do-not-smuggle; confidence: high; claim_label: source_backed_summary

## Routes Here
- question: How should a Claude procedure become reusable without broadening authority?; leads_to: wiki/concepts/source-authority-routing.md; rationale: workflow reuse does not promote source/candidate material.
- question: What must a reusable handoff contain?; leads_to: wiki/concepts/explicit-handoff-continuity.md; rationale: a template needs explicit continuation fields.
- question: Who sequences the workflow?; leads_to: wiki/entities/meta-ops.md; rationale: Meta Ops owns orchestration, this lane owns the pattern.

## Uncertainty / Raw Source Reopen Triggers
- id: U-PW01; description: Patch/full-body/live-edit modes describe historical execution discipline. Reopen raw evidence before mapping those modes to a specific Claude tool surface.; source_pointer: special_ops__prompts_workflows/ESSENCE.md#Core-doctrine-Patch-write-mode-by-context; proposed_handling: revisit_source
- id: U-PW02; description: Templates are explicitly not governance; do not treat a workflow file as Claude runtime authorization.; source_pointer: special_ops__prompts_workflows/ESSENCE.md#Core-doctrine-Templates-are-not-governance; proposed_handling: leave_as_gap
