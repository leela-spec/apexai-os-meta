---
title: Explicit Handoff Continuity
page_type: concept
kb_slug: old-apex-full-orchestration-agent-kb-v2
concept_slug: explicit-handoff-continuity
source_refs: [{source_id: source-05bc8d6b022c9444, source_path: raw/other/managed/rules/AGENT_SWARM_INTERACTION_CANON.md, source_hash: f849f642eecfc16e377e69c92dcf1b3557d058012176f1398255b5b3b054f9fd, source_pointer: Delegation rules; Handoff rules; Routing boundaries and guardrails, source_storage_mode: copy_into_kb}]
created_at: 2026-07-11T12:00:00Z
updated_at: 2026-07-11T12:00:00Z
confidence: high
claim_label: source_backed_summary
status: active
---
# Explicit Handoff Continuity

## Purpose and Scope
This page specifies the minimum context a downstream AI needs to continue bounded work without reconstructing hidden reasoning from chat history. It governs delegation and transfers between roles, states, or surfaces; it does not select Claude storage or messaging technology.

## Decision / Use Guidance
Use one compact handoff object whenever work changes agent, state, or durable surface. Reject or hold a transfer lacking target, state, next action, or risk. Keep simple, personal, sensitive, approval-bound, or conversational work local rather than manufacturing delegation.

## Adaptive Ranked Source Set
- source_id: source-05bc8d6b022c9444; rationale: managed law directly defines delegation prerequisites, handoff fields, and receiver dispositions; coverage: all claims.

## Macro / Meso / Micro
### Macro
Explicit handoffs turn transient reasoning into a reviewable continuation boundary. This is the mechanism that lets the system delegate without relying on broad context sharing.

### Meso
Delegation needs bounded work, explicit criteria, identified context, constraints, and return format. The receiver must act with reduced context; delegation never transfers authority beyond the receiving role, state, and surface.

### Micro
The handoff records role, state, target, intended next role/state, inputs or missing prerequisites, expected action, and unresolved risk. The receiver accepts, rejects with a stated reason, or escalates through a durable route. Silent continuation is invalid.

## Overlap and Evidence
Delegation rules establish the preconditions, handoff rules define the transfer record, and routing guardrails forbid hidden-reasoning continuation. The same requirement appears in three sections, making continuity rather than verbosity the core pattern.

## Alternatives Ranked by Use Case
| Rank | Design | Wins when | Disqualifier |
|---|---|---|---|
| 1 | Structured handoff record | Owner, state, or surface changes | Small authoring cost. |
| 2 | Local continuation | Task is simple or approval-bound | Not independent delegation. |
| 3 | Free-form chat relay | Never for material governed work | Hides state, prerequisites, and risk. |

## Key Claims
- claim_id: HC01; claim: Delegation requires bounded work, explicit success criteria, context, constraints, and a legible return format.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Delegation-rules; confidence: high; claim_label: source_backed_summary
- claim_id: HC02; claim: A receiver must be able to act without reconstructing hidden reasoning from transient chat context.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Delegation-rules; confidence: high; claim_label: source_backed_summary
- claim_id: HC03; claim: A valid handoff names role, state, target, next role/state, prerequisites, expected action, and unresolved risk.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Handoff-rules; confidence: high; claim_label: source_backed_summary
- claim_id: HC04; claim: A receiver accepts, rejects with a reason, or escalates; silent continuation is invalid.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Handoff-rules; confidence: high; claim_label: source_backed_summary

## Routes Here
- question: What exact context must a Claude subagent receive?; leads_to: wiki/concepts/role-state-permission-separation.md; rationale: handoff carries a task's role/state boundary.
- question: Who sequences handoffs?; leads_to: wiki/entities/meta-ops.md; rationale: Meta Ops routes work but does not validate itself.
- question: How should a weak handoff be handled?; leads_to: wiki/entities/meta-detective.md; rationale: Detective provides hold, revise, or escalation pressure.

## Uncertainty / Raw Source Reopen Triggers
- id: U-HC01; description: The source permits session, plan, packet, or equivalent durable handoff state but does not choose Claude persistence mechanics.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Handoff-rules; proposed_handling: ask_operator
- id: U-HC02; description: This continuity guidance does not authorize KB mutation of Apex plan, sync, or session systems.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Handoff-rules; proposed_handling: leave_as_gap
