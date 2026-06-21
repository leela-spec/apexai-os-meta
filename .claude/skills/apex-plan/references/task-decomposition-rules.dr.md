# Task Decomposition Rules

## Decomposition Objective

Decompose operator intent into epic candidates and task candidates that are small enough to review, large enough to matter, and clear enough to support downstream synchronization without claiming it has happened.

## Core Decomposition Sequence

Use this sequence:

1. restate operator intent
2. identify the planning outcome
3. split work into outcome-based epics
4. split epics into reviewable task candidates
5. attach dependency proposals
6. assign provisional status
7. suggest priority and urgency
8. prepare operator-gated questions or approvals

## Epic Rules

An epic candidate should:

- represent a meaningful outcome group
- group related planning work
- avoid low-level implementation detail
- avoid combining unrelated concerns
- stay inside the planning-only boundary

Good epic examples for this skill include:

- project intent clarification
- decomposition and task proposal
- dependency and sequencing proposal
- operator review and approval packet

## Task Rules

A task candidate should:

- express one clear objective
- produce one reviewable deliverable
- avoid hidden multi-step execution bundles
- avoid direct state mutation
- avoid script-running instructions as completion criteria
- be understandable without private reasoning
- include dependencies only when they are actually needed

If a task candidate cannot be reviewed on its own, split it further.

If several tasks only differ by wording and not by outcome, merge them.

## Atomicity Standard

A task candidate is sufficiently atomic when:

- its objective can be explained in one or two sentences
- its deliverable can be named concretely
- its dependency list is short and justified
- its status can be proposed without ambiguity
- it does not mask a separate downstream skill responsibility

## Boundary-Aware Splitting

When a request crosses skill boundaries, split the planning work from the execution work.

Examples:

- planning candidate: draft dependency proposal
- not allowed as an `apex-plan` task: rebuild registry

- planning candidate: prepare operator-gated sync handoff note
- not allowed as an `apex-plan` task: compute exact next task

- planning candidate: identify session continuity requirements
- not allowed as an `apex-plan` task: write handoff files

## Status Proposal Rules

Use status to describe the planning view only.

- `open` when the task is proposed but not started
- `in-progress` only when the operator explicitly indicates active work
- `blocked` when a dependency or approval prevents progress
- `done` only when the planning deliverable is already complete
- `deferred` when intentionally postponed

Do not use status to imply execution outside the planning packet.

## Evidence-Aware Decomposition

When the source basis is strong, write tighter task candidates.

When the source basis is partial, keep the task candidate narrower and note the uncertainty.

When PM2-style task-contract reasoning depends on the accepted substitute pattern, preserve the label `CrewAI_task_py_SUBSTITUTE` in the relevant note.

Do not convert substitute evidence into a direct-original-source claim.

## Good Tasks for This Skill

Examples of task-candidate shapes:

- clarify operator intent and constraints
- draft epic candidate list
- draft task candidate list for an approved epic
- propose `depends_on` relationships
- assign provisional status values
- suggest priority and urgency inputs
- assemble operator-gated review packet

## Bad Tasks for This Skill

Do not generate task candidates whose completion depends on this skill doing any of the following:

- running Python scripts
- mutating files
- rebuilding registries
- scanning blockers across stored state
- performing stale detection
- selecting the exact next task from project state
- writing handoff files
- updating session state

## Stopping Rule

Stop decomposition once the packet is ready for human review.

Do not continue into implementation planning that belongs to another skill.