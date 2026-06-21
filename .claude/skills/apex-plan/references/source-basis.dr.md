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