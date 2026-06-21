# Dependency and Priority Rules

## Dependency Rule

Use `depends_on` as an integer array that references task candidate `id` values.

A task candidate is actionable only when every item in `depends_on` is already `done`.

Do not treat `open` or `in-progress` dependencies as satisfied.

## Dependency Proposal Principles

Only propose a dependency when it changes the order of work in a meaningful way.

Good dependency reasons:

- the later task requires earlier clarification
- the later task requires operator approval first
- the later task relies on an earlier planning deliverable
- the later task would otherwise create contradictory planning outputs

Bad dependency reasons:

- vague preference
- assumed ordering without consequence
- duplication of epic ordering when no task-level constraint exists

## Dependency Design Constraints

Avoid these patterns unless strictly necessary:

- deep chains of single-step dependencies
- circular dependencies
- dependencies on tasks from outside the packet
- dependencies that imply live-state checks by this skill

If a task depends on external confirmation, mark that clearly in notes or operator gate text.

## Blocked-State Rule

Use `blocked` only when a real blocker exists, such as:

- missing operator decision
- missing approved source basis
- unsatisfied required prior task
- boundary-sensitive information that cannot be assumed

Do not use `blocked` as a substitute for uncertainty that belongs in notes.

## Priority Rule

Priority is a planning suggestion, not an execution command.

Use only:

- `high` with score `3`
- `medium` with score `2`
- `low` with score `1`

Use priority to express importance or consequence, not dependency satisfaction.

## Priority Guidance

Prefer `high` when a task candidate:

- unlocks several later planning tasks
- resolves critical operator ambiguity
- prevents major planning drift
- is required for near-term review

Prefer `medium` when a task candidate:

- advances the packet materially
- matters to sequencing but is not the main unlock
- improves planning quality without being time-critical

Prefer `low` when a task candidate:

- is supportive but not central
- can wait without harming the packet
- captures optional refinement

## Urgency Rule

Set `urgency_days` to due-date days until due.

If no due date is known, set `urgency_days` to `999`.

Urgency is a planning input, not a scheduling guarantee.

## Combined Use of Dependency, Priority, and Urgency

These three fields must not be collapsed into one value.

- `depends_on` explains sequencing constraints
- `priority` explains importance
- `urgency_days` explains time pressure

A task can be high priority and still not actionable if dependencies are incomplete.

A task can be urgent and still remain blocked.

## Exact-Next-Task Boundary

`apex-plan` may describe candidate ordering implications, but it must not compute or claim the exact next task.

Exact next-task computation belongs to `apex-sync`.

Allowed wording:

- likely focus candidate after approvals
- provisional ordering implication
- ready for downstream sync review

Disallowed wording:

- exact next task is
- sync result
- registry-confirmed order