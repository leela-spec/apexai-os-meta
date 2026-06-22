---
name: apex-sync
description: >
  Use this skill when the operator asks to compute deterministic Apex read-side
  synchronization reports: next actions, blockers, stale tasks, registry
  rebuild previews, drift checks, dependency validation, priority, urgency,
  unlock depth, or focus candidates. Uses `scripts/apex_sync.py`. Does not
  capture projects, decompose work, mutate task status, author handoff files,
  validate operator decisions, or write session narrative.
---

# Apex Sync

## Objective

`apex-sync` computes deterministic read-side synchronization reports over Apex
task files. It reads task frontmatter and Markdown body content under
`apex-meta/epics/`, validates dependency and status consistency, and delegates
all exact computation to the canonical Python command at `scripts/apex_sync.py`.
It may write only `apex-meta/registry/index.md`, only through the `registry`
subcommand, and only when the operator explicitly uses `--dry-run false`.
It does not capture new projects, decompose work, mutate task status, author
handoff files, validate operator decisions, or create session narrative.

## Accepted Inputs

- Operator request for one or more deterministic read-side reports.
- Apex task files discovered at `apex-meta/epics/*/[0-9][0-9][0-9].md`.
- Task frontmatter containing, when available:
  - `id`
  - `title` or `name`
  - `status`
  - `priority`
  - `due_date`
  - `depends_on`
  - `blocked_by`
  - `updated_date` or `created_date`
- Existing registry file at `apex-meta/registry/index.md` when running drift
  checks.
- Optional command flags described in
  `references/script-command-contract.md`.

## Required Outputs

The package produces only these canonical reports:

- `next_action_report`
- `blocker_report`
- `registry_report`
- `stall_report`
- `drift_report`
- `score_report`
- `focus_candidate_report`
- `dependency_validation_report`

Each JSON report must include:

- `report_name`
- `generated_at`
- `dry_run`
- `root`
- `script_exit_code`
- `review_flags`

## Supporting File Navigation

Read these files only when the request requires their detail:

| File | Read when |
|---|---|
| `references/sync-cluster-contract.md` | Confirming B_SYNC ownership, package boundaries, read-side-only policy, registry write exception, or cross-package routing. |
| `references/script-command-contract.md` | Selecting or explaining `scripts/apex_sync.py` commands, flags, JSON output, dry-run behavior, or exit-code policy. |
| `references/registry-and-drift-rules.md` | Rebuilding registry previews, checking drift, validating registry schema, or handling malformed task files. |
| `references/scoring-and-focus-rules.md` | Computing priority, urgency, dependency-satisfied actionability, unlock depth, blockers, stale tasks, or focus candidates. |
| `package-manifest.md` | Validating the final package file set, source basis, invariants, forbidden claims, or backup notes. |
| `scripts/apex_sync.py` | Running deterministic Apex synchronization reports. |

## Canonical Command Policy

Use this command shape:

```bash
python scripts/apex_sync.py <subcommand> --root . --json --dry-run true
```

Allowed subcommands:

- `next`
- `blockers`
- `registry`
- `stall`
- `drift`
- `score`

The default mode is dry-run. The only non-dry-run command allowed by this
package is:

```bash
python scripts/apex_sync.py registry --root . --json --dry-run false
```

That command may write only:

```txt
apex-meta/registry/index.md
```

Do not run shell scripts, TypeScript, JavaScript, package managers, or external
dependencies for this skill.

## Procedure

1. **Classify the request.** Map the operator request to one or more canonical
   reports: `next_action_report`, `blocker_report`, `registry_report`,
   `stall_report`, `drift_report`, `score_report`,
   `focus_candidate_report`, or `dependency_validation_report`.

2. **Check package boundary.** Confirm the request is read-side synchronization.
   If the request is about project capture, decomposition, status mutation,
   handoff authoring, session narrative, operator validation, or planning-feed
   authoring, route it away from `apex-sync`.

3. **Load the command contract.** Use
   `references/script-command-contract.md` before presenting or running any
   command.

4. **Select the subcommand.** Choose:
   - `next` for next action and dependency validation.
   - `blockers` for blockers and dependency validation.
   - `registry` for registry rebuild preview or explicit registry write.
   - `stall` for stale task candidates.
   - `drift` for registry/source mismatch.
   - `score` for priority, urgency, unlock depth, and focus candidates.

5. **Preserve dry-run default.** Keep `--dry-run true` unless the operator
   explicitly requests the `registry` subcommand with `--dry-run false`.

6. **Run deterministic computation.** Use `python scripts/apex_sync.py` with
   `--root .` and `--json` when machine-readable output is needed.

7. **Return script reports without scope expansion.** Preserve report names and
   `review_flags`. Do not add planning recommendations, session narrative,
   status changes, operator-validation claims, or handoff text.

8. **Surface failures exactly.** If the script returns `script_failed` or a
   nonzero `script_exit_code`, return the script failure report and do not
   infer missing data.

9. **Completion gate.** Stop when the requested canonical report or reports
   have been returned and the dry-run and registry-write policies remain
   intact.

## Validation Rules

- H1 status values are exactly:
  - `open`
  - `in-progress`
  - `blocked`
  - `done`
  - `deferred`
- H3 dependency field is `depends_on`.
- Every `depends_on` item is treated as an integer task id.
- A task is actionable only when:
  - status is `open` or `in-progress`;
  - every `depends_on` target exists;
  - every `depends_on` target has status `done`;
  - `blocked_by` is empty or references completed numeric blockers.
- A task with status `blocked` and empty `blocked_by` must be flagged.
- Missing or malformed frontmatter must be reported, not silently ignored.
- Duplicate task ids must be reported.
- Missing dependency targets must be reported.
- Circular dependency risk must be reported.
- Registry drift must be reported before any write.
- Task files, handoff files, skill files, and session artifacts must not be
  mutated by this skill.

## Failure Modes

| Review flag | Trigger | Required behavior |
|---|---|---|
| `malformed_frontmatter` | A task file lacks valid YAML-like frontmatter. | Report the file and continue processing other valid task files. |
| `missing_task_id` | A task lacks an integer `id`. | Report the file and exclude it from exact graph computation. |
| `duplicate_task_id` | Two or more task files use the same id. | Report all affected files. |
| `unsupported_status` | A status is not one of the H1 values. | Report the task and keep it visible in validation output. |
| `missing_dependency_target` | `depends_on` references an id that does not exist. | Report the task in `dependency_validation_report`. |
| `circular_dependency_risk` | The `depends_on` graph contains a cycle. | Report the cycle and do not treat the affected graph as fully valid. |
| `blocked_without_reason` | A task has status `blocked` but empty `blocked_by`. | Report the task in `blocker_report`. |
| `stale_task_candidate` | A non-done, non-deferred task exceeds the stale threshold. | Report the task without mutating status. |
| `registry_out_of_date` | Generated registry content differs from the current registry. | Report drift and require explicit registry non-dry-run before writing. |
| `drift_detected` | Source task files and registry content do not match. | Include regenerated registry content for review. |
| `script_failed` | `scripts/apex_sync.py` raises an exception or exits nonzero. | Return the script failure report and stop inference. |

## Completion Gate

`apex-sync` is complete only when:

- The requested report name is identified.
- The command contract has been applied.
- The command path is `scripts/apex_sync.py`.
- The subcommand is one of `next`, `blockers`, `registry`, `stall`, `drift`,
  or `score`.
- Dry-run default is preserved.
- Registry write policy is preserved.
- The exact script report is returned.
- No task status mutation is claimed.
- No handoff file authoring is claimed.
- No operator validation is claimed.
- `apex-plan` and `apex-session` boundaries remain intact.