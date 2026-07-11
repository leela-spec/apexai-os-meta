# `apex-plan` Skill Package Proposal

## Package Summary

This package defines a Claude-native, planning-only skill for Apex. It captures intent, decomposes work into epics and task candidates, proposes `depends_on`, suggests H1 status plus H7 priority and urgency, and prepares operator-gated planning packets. It does **not** run scripts, mutate project state, rebuild registries, compute the exact next task, write handoff files, or take over sync or session-mutation behavior. The package below is therefore constrained to the locked planning boundary and preserves the required substitute-label rule for PM2-style task-contract references. 

## Generated Files

**File One — `.claude/skills/apex-plan/SKILL.md`**

markdown

Kopieren

```markdown
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
```

### Validation Checklist

- Preserves a planning-only scope and explicitly forbids scripts, state mutation, registry rebuilds, stale detection, exact next-task computation, and handoff-file writing.
- Uses the locked H1 status enum exactly.
- Preserves H2 canonical paths, including `scripts/` and `.claude/skills/`.
- Uses `depends_on` as an int-array concept with the rule that all dependencies must be `done`.
- Treats H7 priority and urgency as suggestions only.
- Preserves the mandatory `CrewAI_task_py_SUBSTITUTE` label and warns against misclaiming original-source status.

### Source-Basis Note

- `capsule_based`. Grounded in the uploaded access-independent decision capsule and locked boundary rules supplied with the task; no external research or reopened decisions were used. 

**File Two — `.claude/skills/apex-plan/references/planning-contract.md`**

markdown

Kopieren

```markdown
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
```

### Validation Checklist

- Defines the planning packet as the required product.
- Keeps all prohibited behaviors outside the contract.
- Enforces H1, H3, and H7 usage in the packet fields.
- Keeps delegation to `apex-sync` and `apex-session` descriptive rather than performative.

### Source-Basis Note

- `capsule_based`. The contract directly mirrors the uploaded planning-only boundary, required packet-generation task, H1/H3/H7 constraints, and delegation rules. 

**File Three — `.claude/skills/apex-plan/references/task-decomposition-rules.md`**

markdown

Kopieren

```markdown
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
```

### Validation Checklist

- Decomposes work into outcome-based epics and reviewable task candidates.
- Keeps decomposition boundary-aware and avoids script-driven or mutation-driven tasks.
- Uses the H1 status set correctly for planning semantics.
- Preserves the substitute-label rule for PM2-style task-contract reasoning.

### Source-Basis Note

- `capsule_based`. The decomposition rules are constrained by the uploaded planning boundary, A_PLAN-first package scope, and the locked substitute-evidence requirement. 

**File Four — `.claude/skills/apex-plan/references/dependency-and-priority-rules.md`**

markdown

Kopieren

```markdown
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
```

### Validation Checklist

- Preserves `depends_on` as an int-array with the “all must be done” rule.
- Treats priority and urgency as separate planning inputs.
- Prevents the package from claiming exact next-task computation.
- Keeps `blocked` usage tied to real blockers rather than vague uncertainty.

### Source-Basis Note

- `capsule_based`. This rule set is directly grounded in the uploaded H3 and H7 decisions and in the planning-only prohibition on exact sync logic. 

**File Five — `.claude/skills/apex-plan/references/operator-gate.md`**

markdown

Kopieren

```markdown
# Operator Gate

## Purpose

Use the operator gate to stop planning outputs from silently turning into mutation or sync claims.

The operator gate is required whenever the packet is ready for review, approval, or downstream delegation.

## Gate Outcomes

The gate may produce only these outcomes:

- ready for operator review
- needs operator clarification
- ready for downstream planning handoff
- deferred by operator choice

The gate does not authorize this skill to mutate state.

## Required Gate Checks

Before closing a planning packet, check the following:

### Boundary Check

Confirm that the packet remains planning-only and does not claim script execution, mutation, registry rebuild, blocker scan, stale detection, exact sync result, or session mutation.

### Intent Check

Confirm that the operator intent is represented accurately enough for review.

### Scope Check

Confirm that the packet distinguishes in-scope planning work from out-of-scope execution work.

### Dependency Check

Confirm that proposed `depends_on` relationships are explicit and justified.

### Status Check

Confirm that only the allowed status values are used.

### Priority and Urgency Check

Confirm that priority and urgency are presented as suggestions, not as final scheduling or execution decisions.

### Evidence Check

Confirm that substitute or missing evidence is labeled correctly.

If PM2-style task-contract reasoning used the accepted substitute pattern, preserve `CrewAI_task_py_SUBSTITUTE`.

## Recommended Gate Questions

Use these question types when needed:

- Is the planning scope correct?
- Are any proposed epics missing or merged incorrectly?
- Are the dependency proposals acceptable?
- Which blocked or deferred items should remain in the packet?
- Should any task candidate priority or urgency suggestion be adjusted?
- Is the packet ready for downstream sync review?

## Downstream Delegation Statements

Use concise boundary-preserving language.

Allowed examples:

- exact next-task computation is deferred to `apex-sync`
- state mutation and session continuity are deferred to `apex-session`

Not allowed:

- sync completed
- session updated
- handoff files written
- registry rebuilt

## Final Gate Output Shape

End with a short gate summary:

- `gate_status`
- `operator_confirmations_needed`
- `boundary_reminders`
- `downstream_delegate`

Keep this summary short and explicit.
```

### Validation Checklist

- Makes operator review a required stop point.
- Prevents planning output from turning into mutation, sync, session, or registry claims.
- Preserves substitute and missing-evidence labeling requirements.
- Keeps downstream delegation language bounded and non-performative.

### Source-Basis Note

- `capsule_based`. The operator gate is derived from the uploaded requirement for operator-gated planning packets and from the explicit non-mutation, non-sync, non-session boundaries. 

**File Six — `.claude/skills/apex-plan/references/source-basis.md`**

markdown

Kopieren

```markdown
# Source Basis

## Purpose

This reference defines how `apex-plan` should describe evidence basis without overstating certainty.

## Source-Basis Principle

Use evidence to constrain planning output.

Do not use planning output to invent evidence.

Do not claim substitute or missing sources as direct original evidence.

## Approved Labels

Use these labels when relevant:

- `source_backed`
- `adapted`
- `substitute`
- `custom_boundary`
- `source_missing`

## Label Meanings

### `source_backed`

Backed by accepted project source.

Use when the relevant behavior or planning rule is directly supported by an accepted project source basis.

### `adapted`

Adapted from accepted mechanism source.

Use when the pattern is accepted and intentionally adapted to Apex planning use.

### `substitute`

Accepted substitute evidence, not original source.

Use when the package relies on an accepted substitute source rather than the original source.

### `custom_boundary`

Custom Apex mechanism or project-specific boundary.

Use when the rule is a project-defined boundary or a custom Apex mechanism rather than copied source behavior.

### `source_missing`

Known missing source; do not claim direct source backing.

Use when the planning output can proceed only because the boundary allows it, while the direct original source is absent.

## Mandatory Substitute Label

When PM2-style task-contract reasoning depends on the accepted CrewAI substitute pattern, preserve this exact label:

`CrewAI_task_py_SUBSTITUTE`

## Mandatory Warning

When `CrewAI_task_py_SUBSTITUTE` is used, do not claim that the original CrewAI getting-started source was read.

The correct interpretation is:

- accepted substitute task-contract evidence
- not original-source evidence

## Writing Rule

Keep evidence notes short.

Good examples:

- source_backed by accepted project planning rule
- substitute via CrewAI_task_py_SUBSTITUTE
- custom_boundary due to Apex planning-only split
- source_missing for direct original task-contract proof

Bad examples:

- definitely from original source
- confirmed by source we did not read
- copied exactly from missing material

## Capsule-Based Operation

If project file access is incomplete or inconsistent, planning may proceed using the accepted decision capsule.

When this happens:

- keep the package inside the planning-only boundary
- do not reopen decisions
- do not invent additional evidence
- make source-basis notes explicit about capsule-based grounding

## Skill-Level Consequence

Weak or partial evidence narrows the allowed claim surface.

It does not authorize speculative architecture changes.
```

### Validation Checklist

- Defines all required evidence labels.
- Preserves the exact mandatory substitute label and warning.
- Adds capsule-based handling without inventing new evidence.
- Narrows claims when evidence is partial or substitute-based.

### Source-Basis Note

- `capsule_based`. This file operationalizes the uploaded evidence-discipline rules, including substitute, custom-boundary, source-missing, and capsule-fallback behavior. 

**File Seven — `.claude/skills/apex-plan/package-manifest.md`**

markdown

Kopieren

```markdown
# apex-plan Package Manifest

## Package Identity

- `name`: `apex-plan`
- `root`: `.claude/skills/apex-plan/`
- `entrypoint`: `.claude/skills/apex-plan/SKILL.md`
- `mode`: planning-only
- `status`: ready for review

## Package Scope

This package defines a Claude-native planning skill that:

- captures project or task intent
- clarifies operator intent
- decomposes work into epics and task candidates
- proposes `depends_on` relationships
- proposes provisional status using the approved enum
- suggests priority and urgency inputs
- prepares operator-gated planning packets

## Package Exclusions

This package does not:

- run scripts
- mutate state
- rebuild registries
- compute the exact next task
- scan blockers
- perform stale detection
- write handoff files
- own session mutation

## Canonical Path Assumptions

Preserve these paths:

- `apex-meta/`
- `apex-meta/harmonization/`
- `apex-meta/epics/`
- `apex-meta/handoff/`
- `apex-meta/registry/`
- `scripts/`
- `.claude/skills/`

## Required References

- `references/planning-contract.md`
- `references/task-decomposition-rules.md`
- `references/dependency-and-priority-rules.md`
- `references/operator-gate.md`
- `references/source-basis.md`

## Data Contract Summary

Task candidates produced by this skill should use:

- integer `id`
- allowed `status`
- integer-array `depends_on`
- `priority_label`
- `priority_score`
- `urgency_days`
- `evidence_basis`
- short `notes`

## Boundary Delegation

Downstream responsibilities:

- `apex-sync` handles exact next-task computation
- `apex-session` handles mutation, handoff continuity, and session-state responsibilities

This package must never claim those downstream actions already happened.

## Review Notes

Package reviewers should verify:

- planning-only boundary is preserved
- H1 status enum is unchanged
- H2 paths are unchanged
- H3 dependency rule is preserved
- H7 priority and urgency remain suggestions only
- substitute evidence is labeled correctly
- missing sources are not overstated

## File Inventory

- `.claude/skills/apex-plan/SKILL.md`
- `.claude/skills/apex-plan/references/planning-contract.md`
- `.claude/skills/apex-plan/references/task-decomposition-rules.md`
- `.claude/skills/apex-plan/references/dependency-and-priority-rules.md`
- `.claude/skills/apex-plan/references/operator-gate.md`
- `.claude/skills/apex-plan/references/source-basis.md`
- `.claude/skills/apex-plan/package-manifest.md`
```

### Validation Checklist

- Declares the correct entrypoint and full file inventory.
- Re-states the planning-only boundary and exclusions.
- Preserves H2 path assumptions and downstream delegation boundaries.
- Keeps review focus on H1, H3, H7, and substitute/missing-source integrity.

### Source-Basis Note

- `capsule_based`. The manifest reflects the uploaded required package structure, package boundary, locked paths, and review constraints for the first generated Apex skill package. 

## Package-Level Validation

Checked against the supplied controlled-generation rules and access-independent decision capsule, the package is ready for human review as a planning-only skill package. 

yaml

Kopieren

```yaml
package_validation:
  skill_entrypoint_exists: true
  references_exist: true
  planning_only_boundary_preserved: true
  no_scripts: true
  no_state_mutation: true
  no_sync_logic_claimed: true
  no_session_handoff_mutation_claimed: true
  H1_status_enum_used_correctly: true
  H2_paths_preserved: true
  H3_depends_on_used_correctly: true
  H7_priority_urgency_used_as_suggestion_only: true
  CrewAI_task_py_SUBSTITUTE_label_preserved: true
  missing_sources_not_claimed: true
  ready_for_review: true
```

## Next Step

Copy each file into the target path and review the operator-gate wording as the final human check before repo replacement.