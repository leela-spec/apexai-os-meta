---
title: Role-State Permission Separation
page_type: concept
kb_slug: old-apex-full-orchestration-agent-kb-v2
concept_slug: role-state-permission-separation
source_refs: [{source_id: source-05bc8d6b022c9444, source_path: raw/other/managed/rules/AGENT_SWARM_INTERACTION_CANON.md, source_hash: f849f642eecfc16e377e69c92dcf1b3557d058012176f1398255b5b3b054f9fd, source_pointer: Default operating stance; Operational state model; State assignment rules; State transition rules, source_storage_mode: copy_into_kb}]
created_at: 2026-07-11T12:00:00Z
updated_at: 2026-07-11T12:00:00Z
confidence: high
claim_label: source_backed_summary
status: active
---
# Role-State Permission Separation

## Purpose and Scope
This page answers how to assign accountability without accidentally granting authority. Old Apex separates semantic role (responsibility) from operational state (permission on a bounded task). A Claude implementation should retain this as explicit task metadata; an agent name, prompt, or tool capability is not permission.

## Decision / Use Guidance
Before material work, record role, state, target/bounded object, and intended output. Read permissions from state first, then narrow by task boundary, target surface, protocol, and approval conditions. If a field is missing, hold or clarify; never infer authority from a role label.

## Adaptive Ranked Source Set
- source_id: source-05bc8d6b022c9444; rationale: governing law directly defines roles, states, assignment, and transitions; coverage: all claims.

## Macro / Meso / Micro
### Macro
The system limits orchestration drift by keeping identity separate from permission. Roles make accountability visible; states prevent a plausible agent persona from becoming implicit authority.

### Meso
BUILD permits bounded creation and revision. VERIFY permits checking, reconciliation, and promotion proposal. LOCK permits reading and controlled routing around frozen work. The same role may operate in different states, but changing roles never erases the state boundary.

### Micro
BUILD cannot silently self-verify or mutate accepted truth; VERIFY cannot silently rewrite the exact reviewed artifact; LOCK cannot be bypassed for convenience. Normal transitions are BUILD -> VERIFY, VERIFY -> BUILD with a stated failure reason, and VERIFY -> LOCK with a legible lock reason.

## Overlap and Evidence
The canon repeats the distinction in its default stance, state model, assignment rules, and transition rules: role is accountability and state is permission. Four independent sections supporting one invariant make explicit state modeling a high-confidence implementation pattern.

## Alternatives Ranked by Use Case
| Rank | Design | Wins when | Disqualifier |
|---|---|---|---|
| 1 | Explicit role/state task record | Any reusable, high-impact, or governed task | Requires a small durable record. |
| 2 | One executor plus acceptance checklist | Local low-risk work | No independent review/promotion decision. |
| 3 | Role-only prompting | Never for permissions | Explicitly prohibited by the source. |

## Key Claims
- claim_id: RS01; claim: Semantic roles are the accountability layer while operational states are the permission layer.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Default-operating-stance; confidence: high; claim_label: source_backed_summary
- claim_id: RS02; claim: BUILD, VERIFY, and LOCK apply to a bounded task or target surface, not permanently to an agent.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Operational-state-model; confidence: high; claim_label: source_backed_summary
- claim_id: RS03; claim: Every material task identifies role, state, target/bounded object, and intended output; permissions are interpreted from state first.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#State-assignment-rules; confidence: high; claim_label: source_backed_summary
- claim_id: RS04; claim: BUILD self-promotion, VERIFY silent rewrite, and convenience bypass of LOCK are forbidden.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#State-transition-rules; confidence: high; claim_label: source_backed_summary

## Routes Here
- question: How should Claude prevent a persona from becoming implicit authority?; leads_to: wiki/entities/meta-ops.md; rationale: the coordinator applies role/state routing.
- question: What must be carried to a downstream agent?; leads_to: wiki/concepts/explicit-handoff-continuity.md; rationale: handoff makes state durable.
- question: Who challenges an authority violation?; leads_to: wiki/entities/meta-detective.md; rationale: Detective validates authority and drift.

## Uncertainty / Raw Source Reopen Triggers
- id: U-RS01; description: The source specifies OpenClaw managed law, not a Claude API or storage schema.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Scope-and-non-scope; proposed_handling: ask_operator
- id: U-RS02; description: The source uses a conservative one-main-flow baseline; reopen it before inferring parallel Claude-worker policy.; source_pointer: AGENT_SWARM_INTERACTION_CANON.md#Default-operating-stance; proposed_handling: revisit_source
