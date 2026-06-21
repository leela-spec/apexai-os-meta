# Planning Contract

## Contract Goal

This reference defines the minimum contract for any `apex-plan` output.

The result must be a reviewable planning packet, not an execution step.

## Non-Negotiable Boundary

The planning packet must not:

- run scripts
- mutate repo or project state
- rebuild registries
- compute the exact next task
- scan blockers from project state
- perform stale detection
- write handoff files
- own session mutation or session continuity

The planning packet may prepare information for later review and downstream execution by other skills.

## Required Packet Shape

Every planning packet should contain the following sections in order.

### Boundary Statement

A one-sentence confirmation that the output is planning-only.

### Operator Intent

A concise statement of the operator request, desired outcome, and important constraints.

### Scope Summary

A short in-scope and out-of-scope summary.

### Assumptions

Only assumptions required to make the packet usable. Keep this section short.

### Epic Candidates

Each epic candidate should include:

- `epic_id`
- `title`
- `objective`
- `planning_rationale`

Epic candidates must reflect outcome groupings, not implementation trivia.

### Task Candidates

Each task candidate must include:

- `id`
- `title`
- `objective`
- `deliverable`
- `status`
- `depends_on`
- `priority_label`
- `priority_score`
- `urgency_days`
- `evidence_basis`
- `notes`

## Field Constraints

### `id`

Use integers only.

### `status`

Use only:

- `open`
- `in-progress`
- `blocked`
- `done`
- `deferred`

### `depends_on`

Use an integer array. Use an empty array when there are no known dependencies.

### `priority_label`

Use one of:

- `high`
- `medium`
- `low`

### `priority_score`

Use:

- `3` for `high`
- `2` for `medium`
- `1` for `low`

### `urgency_days`

Use due-date days until due, or `999` when no due date is known.

### `evidence_basis`

Use project-approved basis labels only. If substitute evidence is used for PM2-style task-contract reasoning, preserve the exact substitute label in notes.

## Deliverable Rule

Each task candidate must name a concrete planned deliverable such as:

- planning packet section
- epic draft
- task list draft
- dependency proposal
- operator review packet
- clarification question set

Do not name a script run, registry rebuild, or direct repo mutation as the deliverable of this skill.

## Reviewability Rule

The packet must be reviewable by a human operator without requiring hidden context.

If evidence is incomplete, state the uncertainty in `notes` rather than inventing certainty.

## Delegation Rule

The planning packet may recommend downstream delegation but must not claim downstream completion.

Allowed delegation statements:

- exact next-task computation belongs to `apex-sync`
- mutation and session continuity belong to `apex-session`

Disallowed delegation statements:

- sync completed
- registry rebuilt
- handoff written
- blockers scanned from live state
- stale detection completed

## Minimum Completion Standard

A planning packet is complete when it:

- captures operator intent
- proposes reviewable epics
- proposes reviewable task candidates
- includes dependency proposals
- includes provisional status proposals
- includes suggested priority and urgency values
- includes required operator gates
- clearly states what remains outside the skill boundary