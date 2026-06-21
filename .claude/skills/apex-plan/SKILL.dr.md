# apex-plan

## Purpose

Use `apex-plan` to turn an operator request into a planning packet for Apex work.

This skill is planning-only. It captures intent, clarifies scope, decomposes work into epics and task candidates, proposes dependency relationships, suggests provisional status values, and prepares an operator-gated packet for downstream review.

## Use This Skill When

Use this skill when the operator needs a structured plan for project work and wants:

- project or task intent captured cleanly
- work decomposed into epic and task candidates
- provisional `depends_on` relationships proposed
- provisional H1 status labels proposed
- suggested H7 priority and urgency values
- a reviewable packet before any sync or mutation step

## Do Not Use This Skill When

Do not use this skill to:

- run scripts
- mutate repo or project state
- rebuild registries
- compute the exact next task
- scan blockers across state
- perform stale detection
- write handoff files
- own session continuity or session mutation
- claim missing or substitute evidence as direct original evidence

Route exact computation to `apex-sync`.

Route mutation, handoff continuity, and session-state operations to `apex-session`.

## Inputs

Expect the operator to provide one or more of the following:

- a project goal, request, or change description
- constraints, due dates, or review expectations
- known decisions that must remain locked
- accepted source packets or planning evidence
- existing project terminology that must be preserved

If evidence is incomplete, stay inside the planning-only boundary and make the uncertainty explicit.

## Required Operating Rules

1. Preserve the planning-only boundary at all times.
2. Capture operator intent before decomposing work.
3. Produce a planning packet rather than executable system changes.
4. Use only these provisional status values when proposing status:
   - `open`
   - `in-progress`
   - `blocked`
   - `done`
   - `deferred`
5. Use `depends_on` as an integer array.
6. Treat a task as actionable only when every item in `depends_on` is already `done`.
7. Suggest priority using:
   - `high = 3`
   - `medium = 2`
   - `low = 1`
8. Suggest urgency as due-date days until due, or `999` when no due date is known.
9. Treat priority and urgency as planning suggestions only.
10. Keep canonical paths unchanged:
    - `apex-meta/`
    - `apex-meta/harmonization/`
    - `apex-meta/epics/`
    - `apex-meta/handoff/`
    - `apex-meta/registry/`
    - `scripts/`
    - `.claude/skills/`
11. If PM2-style task-contract reasoning is referenced through the accepted CrewAI substitute pattern, label it exactly as `CrewAI_task_py_SUBSTITUTE`.
12. Never describe `CrewAI_task_py_SUBSTITUTE` as the original CrewAI getting-started source.

## Default Output

Return a planning packet with these sections:

### Boundary Statement
One short statement confirming that the output is planning-only.

### Operator Intent
A concise statement of what the operator is trying to achieve.

### Scope Summary
In-scope and out-of-scope planning boundaries.

### Assumptions
Only assumptions needed to make the packet reviewable.

### Epic Candidates
A structured set of epic candidates with objectives and rationale.

### Task Candidates
A structured set of candidate tasks using this shape:

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

### Dependency Notes
Short notes explaining why dependencies were proposed.

### Operator Gate
Questions, confirmations, or approvals needed before downstream actions.

### Delegation Boundary
A short statement that exact next-task computation belongs to `apex-sync`, while mutation and session continuity belong to `apex-session`.

## Task Candidate Requirements

Each task candidate should be:

- outcome-oriented
- reviewable by a human
- small enough to be completed without hidden subprojects
- explicit about deliverable shape
- explicit about dependency conditions
- explicit about uncertain evidence or boundary limits

Do not create fake certainty to fill missing evidence.

## Evidence Labels

Use these values when needed in planning notes:

- `source_backed`
- `adapted`
- `substitute`
- `custom_boundary`
- `source_missing`

Use `CrewAI_task_py_SUBSTITUTE` when the accepted substitute task-contract pattern is relevant.

## Reference Files

Read and apply these reference files while using this skill:

- `references/planning-contract.md`
- `references/task-decomposition-rules.md`
- `references/dependency-and-priority-rules.md`
- `references/operator-gate.md`
- `references/source-basis.md`

## Response Style

Keep outputs operational, lean, and copyable.

Do not include:

- citation markup
- research narrative
- private reasoning
- broad architecture summaries
- speculative redesigns
- sync logic claims
- session mutation claims