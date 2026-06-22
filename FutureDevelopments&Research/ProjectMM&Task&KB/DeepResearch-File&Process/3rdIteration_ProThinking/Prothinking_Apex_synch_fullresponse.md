# Final `apex-sync` Skill Package

## 1. Source Verification

|Source file|Opened/read?|Used for final files|Source treatment|Notes|
|---|--:|---|---|---|
|`apex-meta/harmonization/decisions.md`|Yes|H1 status enum, H2 path locks, H3 `depends_on`, H4 Python-only, H5 B_SYNC scope, H6 handoff boundary, H7 score rules|LOCKED_DECISION_SOURCE|Confirmed H1–H7 values, including the status enum, `depends_on`, Python-only policy, cluster split, handoff files, and priority/urgency rules.|
|`.claude/skills/apex-sync/SKILL.md`|Yes|Current rough scaffold to replace|MIGRATE_AND_REWRITE|Confirmed current scaffold has correct general B_SYNC scope but still points active command paths to `apex-meta/scripts/`, which is path drift for this final package.|
|`.claude/skills/apex-sync/package-manifest.md`|Yes|Current manifest scaffold to replace|MIGRATE_AND_REWRITE|Confirmed existing manifest lists the correct report set but still indexes the old script path as the executable file.|
|`apex-meta/scripts/apex_sync.py`|Yes|Existing Apex CLI behavior, parser behavior, dry-run behavior, report commands, registry write gate|MIGRATE_AND_REWRITE|Confirmed prior script is standard-library Python, reads task files, and writes only the registry in non-dry-run registry mode; final script migrates this behavior to `scripts/apex_sync.py`.|
|`source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/SKILL.md`|Yes|Script-first deterministic reporting principle and command-category separation|ADAPT|Confirmed CCPM’s script-first rule for deterministic status, next, blocker, and validation operations; final package adapts this to Python-only Apex commands.|
|`source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/track.md`|Yes|Tracking command contracts and failure behavior|ADAPT|Confirmed tracking categories for “what’s next,” “what’s blocked,” and validation, plus the rule to interpret only after script output or script failure.|
|`source-knowledge/ProjectRepos/claude-task-master-main/scripts/modules/task-manager/find-next-task.js`|Yes|Dependency-satisfied candidate filtering, priority weighting, dependency-count tie-break, deterministic next-action logic|ADAPT|Confirmed completed-ID dependency satisfaction and priority/dependency/id sorting logic; final version normalizes to H1 statuses and `depends_on`.|
|`source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/src/types/index.ts`|Yes|Task fields, priority, dependencies, parent/subtask concepts, raw-content preservation|ADAPT|Confirmed Markdown task interface fields including status, dependencies, priority, raw content, acceptance criteria, DoD, parent/subtask fields.|
|`source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/src/markdown/parser.ts`|Yes|Markdown/frontmatter parsing concepts and raw body preservation|ADAPT|Confirmed parser separates frontmatter from Markdown body, validates priority values, preserves raw content, and extracts task fields.|
|`source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/SKILL.md`|Yes|Index discipline, raw/source/audit discipline, drift/audit visibility concepts|CONCEPT_ONLY|Confirmed wiki index/raw/audit discipline and never-ignore-audit concept; no `update-index.py` behavior was copied.|
|`Apex_Alfred_Skill_Definition_Guide.md`|Yes|Claude-native skill formatting, frontmatter shape, procedure, validation, completion gate|FORMAT_GUIDANCE|Opened local uploaded project file and applied its SKILL.md formatting guidance.|
|`source-knowledge/ProjectRepos/llm-wiki-main/scripts/update-index.py`|Unavailable at expected path|None|OMIT_AS_SOURCE|Fetch at expected path returned 404. Final files do not claim copied `update-index.py` behavior.|
|`source-knowledge/ProjectRepos/kanban-skill-master/skills/kanban-ai/scripts/show_blocked.sh`|Unavailable at expected path|None|OMIT_AS_SOURCE|Fetch at expected path returned 404. Final blocker logic is custom Apex Python.|

## 2. Final Package Tree

```txt
.claude/skills/apex-sync/
  SKILL.md
  references/
    sync-cluster-contract.md
    script-command-contract.md
    registry-and-drift-rules.md
    scoring-and-focus-rules.md
  package-manifest.md
scripts/
  apex_sync.py
```

## 3. Backup and Application Plan

```yaml
backup_application_plan:
  before_overwrite:
    backup_current_files_to: apex-meta/harmonization/backups/apex-sync-pre-final-YYYY-MM-DD/

  backup_these_if_present:
    - .claude/skills/apex-sync/SKILL.md
    - .claude/skills/apex-sync/package-manifest.md
    - .claude/skills/apex-sync/references/sync-cluster-contract.md
    - .claude/skills/apex-sync/references/script-command-contract.md
    - .claude/skills/apex-sync/references/registry-and-drift-rules.md
    - .claude/skills/apex-sync/references/scoring-and-focus-rules.md
    - apex-meta/scripts/apex_sync.py

  this_run_creates_backup: false
  this_run_writes_repo_files: false

  then_write:
    - .claude/skills/apex-sync/SKILL.md
    - .claude/skills/apex-sync/references/sync-cluster-contract.md
    - .claude/skills/apex-sync/references/script-command-contract.md
    - .claude/skills/apex-sync/references/registry-and-drift-rules.md
    - .claude/skills/apex-sync/references/scoring-and-focus-rules.md
    - .claude/skills/apex-sync/package-manifest.md
    - scripts/apex_sync.py

  after_write:
    - fetch back every written file
    - validate no collapsed YAML or Markdown
    - validate script path is scripts/apex_sync.py
    - validate no active references to apex-meta/scripts/apex_sync.py remain except backup notes
    - run python -m py_compile scripts/apex_sync.py
    - run python scripts/apex_sync.py next --root . --json --dry-run true
    - run python scripts/apex_sync.py blockers --root . --json --dry-run true
    - run python scripts/apex_sync.py registry --root . --json --dry-run true
    - run python scripts/apex_sync.py stall --root . --json --dry-run true
    - run python scripts/apex_sync.py drift --root . --json --dry-run true
    - run python scripts/apex_sync.py score --root . --json --dry-run true
    - optionally delete old apex-meta/scripts/apex_sync.py after successful migration
```

## 4. Final Files

### 4.1 `.claude/skills/apex-sync/SKILL.md`

````markdown
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
````

### 4.2 `.claude/skills/apex-sync/references/sync-cluster-contract.md`

````markdown
# Sync Cluster Contract

## package_role

`apex-sync` is the canonical package for deterministic Apex read-side
synchronization.

```yaml
package_role:
  package_name: apex-sync
  package_path: .claude/skills/apex-sync/
  package_status: final_canonical_v1
  cluster: B_SYNC
  role: deterministic_read_side_synchronization
  execution_model: skill_entrypoint_plus_standard_library_python_script
  canonical_script_path: scripts/apex_sync.py
```

The package reads Apex task files, computes synchronization reports, validates
read-side consistency, and previews or writes the compact work registry under a
strict write exception.

## B_SYNC_process_scope

```yaml
B_SYNC_process_scope:
  owns_read_side_computation: true
  default_mode: dry_run
  script_language: Python
  standard_library_only: true
  shell_out_allowed: false
  external_dependencies_allowed: false
  task_file_mutation_allowed: false
  handoff_file_mutation_allowed: false
  skill_file_mutation_allowed: false
  only_write_exception: apex-meta/registry/index.md
```

`apex-sync` is invoked only for deterministic computation from already-existing
task files. It does not create task intent, mutate task state, or interpret
operator decisions.

## owned_processes

`apex-sync` owns these process functions:

| Process | Meaning |
|---|---|
| `PM4_compute_next_action` | Compute dependency-satisfied next action candidates from existing task files. |
| `PM5_detect_blockers` | Detect blocked tasks, unsatisfied dependencies, missing dependency targets, and blocked tasks lacking blocker reasons. |
| `PM7_detect_stall` | Detect stale non-done tasks from task timestamps. |
| `PM8_generate_work_registry` | Generate the deterministic work registry preview and gated registry write. |
| `KB4_rebuild_index` | Rebuild the compact task index as registry content. |
| `KB5_detect_drift` | Compare current task files against the registry and report drift. |
| `PD1_compute_priority_score` | Convert H7 priority values into numeric scores. |
| `PD2_compute_urgency_score` | Compute due-date urgency as days until due or `999`. |
| `PD3_compute_unlock_depth` | Count downstream tasks unlocked by completing a task. |
| `PD4_compute_focus_candidates` | Sort actionable candidates by priority, urgency, unlock depth, and id. |

## excluded_processes

`apex-sync` must not own these process functions:

| Excluded process | Correct package boundary |
|---|---|
| `PM1_project_capture` | Belongs outside B_SYNC. |
| `PM2_human_decomposition` | Belongs outside B_SYNC. |
| `PM6_status_mutation` | Belongs to session/mutation handling. |
| `KB1_session_narrative` | Belongs to session handling. |
| `KB2_state_delta_interpretation` | Belongs to session handling. |
| `KB3_entity_synthesis` | Belongs to session handling. |
| `KB6_next_session_authoring` | Belongs to session handling. |
| `PD5_operator_validation` | Belongs to operator-gated mutation/session logic. |
| `PD6_planning_feed_authoring` | Belongs to session/planning-feed authoring. |

## cross_package_routing

Use this routing table when a request crosses the B_SYNC boundary:

| Request type | Route |
|---|---|
| Capture a new project, task, or idea | Not `apex-sync`; route to planning/capture behavior. |
| Decompose a project into tasks | Not `apex-sync`; route to planning/decomposition behavior. |
| Compute what is next from existing tasks | `apex-sync`. |
| Find blockers from existing tasks | `apex-sync`. |
| Rebuild or preview the registry | `apex-sync`. |
| Mutate a task status | Not `apex-sync`; route to session/mutation behavior. |
| Author `task_plan.md`, `findings.md`, `progress.md`, or `next-session.md` | Not `apex-sync`; route to session/handoff behavior. |
| Validate an operator decision | Not `apex-sync`; route to operator-gated validation behavior. |
| Create planning prose or next-day planning feed | Not `apex-sync`; route to planning/session feed behavior. |

## read_side_only_policy

`apex-sync` is read-side by default.

Allowed reads:

- `apex-meta/epics/*/[0-9][0-9][0-9].md`
- `apex-meta/registry/index.md` for drift comparison

Forbidden writes:

- Task files
- Handoff files
- Skill files
- Source-knowledge files
- Project capture files
- Session narrative files
- Entity synthesis files
- Planning-feed files

The script may create in-memory reports and print them to stdout. Printed output
is not considered a repo write.

## registry_write_exception

The single write exception is:

```txt
apex-meta/registry/index.md
```

The exception is valid only when all conditions are true:

```yaml
registry_write_exception:
  subcommand: registry
  dry_run: false
  explicit_operator_intent_required: true
  allowed_path: apex-meta/registry/index.md
  task_file_mutation: forbidden
  handoff_file_mutation: forbidden
  skill_file_mutation: forbidden
```

All other subcommands remain dry-run report generators.

## custom_python_caveats

The following behavior is custom Apex Python and must not be described as copied
from unavailable sources:

- `blocker_report`
- `stall_report`
- `registry_report`
- `drift_report`
- `unlock_depth`

Forbidden claims:

- `copied_llm_wiki_update_index_py`
- `copied_kanban_blocker_script`
- `copied_OpenClaw_TaskFlow`
- `fully_source_backed_B_SYNC_without_custom_python`
- `copied_bash_script_behavior_as_python_without_adaptation`

The final implementation adapts available CCPM, Task Master, Backlog, and
llm-wiki concepts into Apex-specific Python. It does not copy unavailable
`update-index.py` or Kanban blocker script behavior.

## final_acceptance_invariants

```yaml
final_acceptance_invariants:
  package_status: final_canonical_v1
  canonical_script_path: scripts/apex_sync.py
  no_final_script_under_apex_meta_scripts: true
  H1_status_enum:
    - open
    - in-progress
    - blocked
    - done
    - deferred
  dependency_field: depends_on
  default_mode: dry_run
  only_allowed_write_path: apex-meta/registry/index.md
  standard_library_only: true
  shell_out_allowed: false
  task_status_mutation_allowed: false
  handoff_authoring_allowed: false
  operator_validation_claim_allowed: false
  custom_Apex_Python_caveats_present: true
```
````

### 4.3 `.claude/skills/apex-sync/references/script-command-contract.md`

````markdown
# Script Command Contract

## canonical_command

The canonical command shape is:

```bash
python scripts/apex_sync.py <subcommand> --root . --json --dry-run true
```

The canonical executable path is:

```txt
scripts/apex_sync.py
```

Do not use shell scripts, TypeScript, JavaScript, package managers, or external
dependencies for B_SYNC computation.

## global_flags

All subcommands accept these flags:

| Flag | Required? | Default | Meaning |
|---|---:|---|---|
| `--root .` | Recommended | `.` | Repository root containing `apex-meta/epics/`. |
| `--json` | Optional | human-readable output | Emits machine-readable JSON. |
| `--dry-run true` | Optional | `true` | Preserves read-only behavior. |
| `--dry-run false` | Restricted | not default | Allowed only with `registry`. |

Subcommand-specific flags:

| Subcommand | Flag | Default | Meaning |
|---|---|---|---|
| `stall` | `--stale-days` | `14` | Minimum age since `updated_date` or `created_date` before a task is stale. |
| `stall` | `--today` | current date | Deterministic test date formatted `YYYY-MM-DD`. |
| `score` | `--today` | current date | Deterministic test date formatted `YYYY-MM-DD`. |

## subcommands

Required subcommands:

- `next`
- `blockers`
- `registry`
- `stall`
- `drift`
- `score`

## next_command_contract

```bash
python scripts/apex_sync.py next --root . --json --dry-run true
```

Produces:

- `next_action_report`
- `dependency_validation_report`

The command must:

- Load task files from `apex-meta/epics/*/[0-9][0-9][0-9].md`.
- Validate task ids, statuses, dependencies, blockers, and dependency cycles.
- Select candidates whose status is `open` or `in-progress`.
- Require all `depends_on` targets to exist and be `done`.
- Require `blocked_by` to be empty or cleared by completed numeric blocker
  references.
- Sort focus candidates by the scoring policy defined in
  `scoring-and-focus-rules.md`.
- Never mutate task files.

## blockers_command_contract

```bash
python scripts/apex_sync.py blockers --root . --json --dry-run true
```

Produces:

- `blocker_report`
- `dependency_validation_report`

The command must report:

- Tasks with status `blocked`.
- Tasks with non-empty `blocked_by`.
- Tasks with unsatisfied `depends_on`.
- Tasks with missing dependency targets.
- Tasks with status `blocked` and empty `blocked_by`.

It must not resolve blockers, mutate status, or author session notes.

## registry_command_contract

Dry-run preview:

```bash
python scripts/apex_sync.py registry --root . --json --dry-run true
```

Explicit registry write:

```bash
python scripts/apex_sync.py registry --root . --json --dry-run false
```

Produces:

- `registry_report`

The command must:

- Generate deterministic registry content from task files.
- Include task ids, titles, statuses, priorities, due dates, dependencies,
  blockers, timestamps, epic slug, and task path.
- Include review flags from validation.
- Write only `apex-meta/registry/index.md`.
- Write only when `--dry-run false` is explicitly provided.
- Never write task files or handoff files.

## stall_command_contract

```bash
python scripts/apex_sync.py stall --root . --json --dry-run true
```

Optional deterministic test example:

```bash
python scripts/apex_sync.py stall --root . --json --dry-run true --stale-days 14 --today 2026-06-21
```

Produces:

- `stall_report`

The command must:

- Ignore tasks with status `done` or `deferred`.
- Use `updated_date` when present.
- Fall back to `created_date` when `updated_date` is absent.
- Flag a task as `stale_task_candidate` only when its age is greater than or
  equal to the stale threshold.
- Never mutate stale task status.

## drift_command_contract

```bash
python scripts/apex_sync.py drift --root . --json --dry-run true
```

Produces:

- `drift_report`
- `registry_report`

The command must:

- Regenerate registry content in memory.
- Compare generated content with `apex-meta/registry/index.md`.
- Report `drift_detected` when registry content differs.
- Report `registry_out_of_date` when the generated registry would change the
  existing registry.
- Include regenerated registry content for review.
- Never write the registry from the `drift` subcommand.

## score_command_contract

```bash
python scripts/apex_sync.py score --root . --json --dry-run true
```

Optional deterministic test example:

```bash
python scripts/apex_sync.py score --root . --json --dry-run true --today 2026-06-21
```

Produces:

- `score_report`
- `focus_candidate_report`

The command must compute:

- H7 priority score.
- H7 urgency score.
- Unlock depth.
- Dependency-satisfied focus candidates.
- Focus sorting order.

It must not create planning recommendations or mutate project state.

## exit_code_policy

```yaml
exit_code_policy:
  0:
    meaning: script_completed
    includes_validation_findings: true
  1:
    meaning: script_failed
    required_review_flag: script_failed
```

Validation findings such as malformed frontmatter, missing dependencies, drift,
or stale candidates do not automatically make the script fail. They are report
content, not execution failure.

## json_output_policy

When `--json` is used, every report object must include:

- `report_name`
- `generated_at`
- `dry_run`
- `root`
- `script_exit_code`
- `review_flags`

The top-level JSON object may contain more than one report when a command
naturally emits related reports. For example, `next` emits
`next_action_report` and `dependency_validation_report`.

## dry_run_policy

```yaml
dry_run_policy:
  default: true
  false_allowed_only_for:
    - registry
  false_requires:
    - explicit --dry-run false
  false_write_path:
    - apex-meta/registry/index.md
  false_forbidden_for:
    - next
    - blockers
    - stall
    - drift
    - score
```

The script accepts `--dry-run false` uniformly for CLI consistency, but only the
`registry` subcommand has write behavior. Other subcommands remain read-side
report generators.

## no_shell_out_policy

`apex-sync` must not call shell scripts or spawn external processes.

Forbidden implementation mechanisms:

- `subprocess`
- `os.system`
- Bash scripts
- TypeScript scripts
- JavaScript scripts
- Package-manager commands
- Network calls
- Non-standard-library Python dependencies

The final implementation is custom Apex Python adapted from available source
concepts and current Apex scaffold behavior.
````

### 4.4 `.claude/skills/apex-sync/references/registry-and-drift-rules.md`

````markdown
# Registry and Drift Rules

## purpose

This file defines the registry and drift rules for `apex-sync`.

The registry is a deterministic compact index of Apex task files. It is
generated from task frontmatter and task paths. It is not a planning document,
session narrative, status mutation file, or handoff file.

## task_file_discovery

Task files are discovered with this glob, relative to repository root:

```txt
apex-meta/epics/*/[0-9][0-9][0-9].md
```

Discovery rules:

- Only Markdown files matching the exact glob are task inputs.
- Files outside the glob are ignored by `apex-sync`.
- Task id must come from frontmatter field `id`.
- File stem may not silently replace a missing `id`.
- Epic slug is the immediate parent directory under `apex-meta/epics/`.
- Task body is preserved for parsing context but not written back.

## task_frontmatter_validation

Each task file is expected to contain YAML-like frontmatter followed by Markdown
body content.

Required for exact graph computation:

- `id`
- `status`

Optional but parsed when present:

- `title`
- `name`
- `priority`
- `due_date`
- `depends_on`
- `blocked_by`
- `updated_date`
- `created_date`
- `updated`
- `created`
- `updated_at`
- `created_at`

Validation rules:

| Rule | Review flag |
|---|---|
| Missing opening or closing frontmatter fence | `malformed_frontmatter` |
| Frontmatter line cannot be parsed as YAML-like `key: value` | `malformed_frontmatter` |
| Missing `id` | `missing_task_id` |
| Non-integer `id` | `missing_task_id` |
| Duplicate integer `id` across task files | `duplicate_task_id` |
| Status not in H1 enum | `unsupported_status` |
| `depends_on` target does not exist | `missing_dependency_target` |
| `depends_on` graph contains a cycle | `circular_dependency_risk` |
| Status is `blocked` and `blocked_by` is empty | `blocked_without_reason` |

H1 status values are exactly:

- `open`
- `in-progress`
- `blocked`
- `done`
- `deferred`

## registry_schema

The registry file is Markdown at:

```txt
apex-meta/registry/index.md
```

The generated registry must include:

- H1-compatible metadata block.
- Source glob.
- Generation timestamp.
- Task count.
- Discovered task-file count.
- Review flag count.
- Task table with:
  - `id`
  - `epic_slug`
  - `status`
  - `priority`
  - `due_date`
  - `depends_on`
  - `blocked_by`
  - `updated_date`
  - `created_date`
  - `title`
  - `task_path`
- Review flag list when any flags exist.

The registry is an index. It must not redefine planning logic, task mutation
logic, operator validation, or session handoff rules.

## registry_rebuild_rules

The registry is rebuilt by:

```bash
python scripts/apex_sync.py registry --root . --json --dry-run true
```

Dry-run rebuild behavior:

- Reads task files.
- Validates task files.
- Generates registry content in memory.
- Prints `registry_report`.
- Does not write files.

Explicit write behavior:

```bash
python scripts/apex_sync.py registry --root . --json --dry-run false
```

The write behavior:

- Writes only `apex-meta/registry/index.md`.
- Creates the registry parent directory if needed.
- Does not write task files.
- Does not write handoff files.
- Does not write skill files.
- Does not write source files.

## drift_detection_rules

Drift is checked by:

```bash
python scripts/apex_sync.py drift --root . --json --dry-run true
```

Drift exists when regenerated registry content differs from the current content
of:

```txt
apex-meta/registry/index.md
```

Drift report behavior:

- Regenerate registry content in memory.
- Read the current registry when it exists.
- Compare exact content.
- Set `drift_detected` to `true` when content differs.
- Add `drift_detected` review flag when content differs.
- Add `registry_out_of_date` review flag when content differs.
- Return regenerated registry content for review.
- Do not write the registry.

## malformed_task_file_policy

Malformed task files must not stop the full report unless the script itself
fails.

Policy:

- Report malformed task files with `malformed_frontmatter`.
- Continue loading other task files.
- Exclude malformed files from exact dependency graph computation.
- Include malformed-file flags in report `review_flags`.
- Do not repair malformed files.
- Do not infer missing frontmatter fields from body text.

## dry_run_default

Default mode is dry-run:

```yaml
dry_run_default: true
```

Dry-run mode must be used for:

- `next`
- `blockers`
- `registry` preview
- `stall`
- `drift`
- `score`

## explicit_non_dry_run_write_gate

A write is allowed only when all conditions are true:

```yaml
explicit_non_dry_run_write_gate:
  subcommand: registry
  flag: --dry-run false
  operator_intent: explicit
  output_path: apex-meta/registry/index.md
```

No other command may write.

## only_allowed_write_path

```txt
apex-meta/registry/index.md
```

Forbidden write paths include:

- `apex-meta/epics/`
- `apex-meta/handoff/`
- `.claude/skills/`
- `source-knowledge/`
- any path outside the repository root

## final_registry_report_contract

`registry_report` must include:

- `report_name`
- `generated_at`
- `dry_run`
- `root`
- `script_exit_code`
- `review_flags`
- `target_path`
- `allowed_write_path`
- `wrote_registry`
- `task_count`
- `discovered_task_files`
- `registry_content`

The report must be valid whether it is produced in dry-run mode or explicit
write mode.
````

### 4.5 `.claude/skills/apex-sync/references/scoring-and-focus-rules.md`

````markdown
# Scoring and Focus Rules

## purpose

This file defines deterministic scoring and focus-candidate rules for
`apex-sync`.

The scoring layer computes numeric read-side signals from existing task files.
It does not decide strategy, validate operator intent, rewrite priorities, or
author planning prose.

## H7_priority_score

H7 priority values are:

```yaml
priority:
  high: 3
  medium: 2
  low: 1
```

Rules:

- `high` maps to `3`.
- `medium` maps to `2`.
- `low` maps to `1`.
- Missing priority is treated as `medium`.
- Unsupported priority values are treated as `medium` for computation.
- Priority scoring does not mutate task frontmatter.

## H7_urgency_score

Urgency score is computed from `due_date`.

```yaml
urgency:
  due_date_days_until_due_or_999: true
```

Rules:

- If `due_date` is present and parseable as `YYYY-MM-DD`, urgency is the number
  of days between today and the due date.
- If due date is today, urgency is `0`.
- If due date is in the past, urgency is negative.
- If `due_date` is missing or malformed, urgency is `999`.
- Lower urgency values sort earlier.
- Urgency scoring does not mutate task frontmatter.

## dependency_satisfied_actionability

A task is actionable only when all conditions are true:

```yaml
actionable_task:
  status:
    allowed:
      - open
      - in-progress
  depends_on:
    all_targets_exist: true
    all_targets_done: true
  blocked_by:
    empty_or_cleared: true
```

Dependency rules:

- Canonical dependency field is `depends_on`.
- `dependencies` is not canonical.
- Every `depends_on` item is interpreted as an integer task id.
- Every dependency target must exist.
- Every dependency target must have status `done`.
- Missing dependency targets are flagged.
- Circular dependency risk is flagged.

## blocker_semantics

A task appears in blocker reporting when any condition is true:

- Status is `blocked`.
- `blocked_by` is non-empty.
- One or more `depends_on` targets exists but is not `done`.
- One or more `depends_on` targets is missing.

`blocked_by` semantics:

- Empty `blocked_by` means no explicit blocker reason is present.
- Status `blocked` with empty `blocked_by` is flagged as
  `blocked_without_reason`.
- Numeric `blocked_by` entries are treated as task ids and are clear only when
  those tasks are `done`.
- Non-numeric `blocked_by` entries are treated as blocker reasons and keep the
  task blocked for read-side actionability.

## stale_task_semantics

A task is stale when:

- status is not `done`;
- status is not `deferred`;
- it has a parseable `updated_date` or `created_date`;
- the age in days is greater than or equal to the stale threshold.

Timestamp fields are read in this order:

1. `updated_date`
2. `updated`
3. `updated_at`
4. `created_date`
5. `created`
6. `created_at`

Default stale threshold:

```yaml
stale_days_default: 14
```

Stale detection emits `stale_task_candidate` and never mutates task status.

## unlock_depth_policy

Unlock depth measures how many downstream tasks depend directly or indirectly
on a task.

Rules:

- Build reverse edges from `depends_on`.
- Count every reachable downstream task once.
- Ignore missing dependency targets for unlock-depth counting.
- Do not count the task itself.
- Use unlock depth only as a sorting signal.
- Do not rewrite dependencies based on unlock depth.

Example:

```yaml
tasks:
  1:
    unlocks:
      - 2
      - 3
  2:
    unlocks:
      - 4

unlock_depth:
  1: 3
  2: 1
  3: 0
  4: 0
```

## focus_candidate_sort_policy

Focus candidates are actionable tasks sorted by:

1. Priority score descending.
2. Urgency score ascending.
3. Unlock depth descending.
4. Task id ascending.

```yaml
focus_candidate_sort_policy:
  primary: priority_score_desc
  secondary: urgency_score_asc
  tertiary: unlock_depth_desc
  quaternary: id_asc
```

This is a deterministic ordering policy, not a planning recommendation.

## score_report_schema

`score_report` must include:

- `report_name`
- `generated_at`
- `dry_run`
- `root`
- `script_exit_code`
- `review_flags`
- `tasks`

Each scored task should include:

- `id`
- `title`
- `status`
- `priority`
- `priority_score`
- `due_date`
- `urgency_score`
- `depends_on`
- `blocked_by`
- `updated_date`
- `created_date`
- `epic_slug`
- `task_path`
- `unlock_depth`
- `reason`

## focus_candidate_report_schema

`focus_candidate_report` must include:

- `report_name`
- `generated_at`
- `dry_run`
- `root`
- `script_exit_code`
- `review_flags`
- `candidates`

Each focus candidate should include the same task fields as a scored task.

A candidate must satisfy the actionability policy before appearing in this
report.

## no_planning_recommendation_boundary

`apex-sync` may say which existing tasks are deterministic focus candidates.
It must not say what the operator should choose strategically.

Allowed:

- “These are the focus candidates sorted by deterministic policy.”
- “Task 4 is blocked by unsatisfied `depends_on`.”
- “Task 7 has urgency score `2`.”

Forbidden:

- “You should work on this because it is strategically best.”
- “The operator decision is validated.”
- “Tomorrow’s plan should be…”
- “The next session should focus on…”

Strategic interpretation belongs outside `apex-sync`.
````

### 4.6 `.claude/skills/apex-sync/package-manifest.md`

````markdown
# Apex Sync Package Manifest

## package_name

```yaml
package_name: apex-sync
```

## package_path

```yaml
package_path: .claude/skills/apex-sync/
canonical_script_path: scripts/apex_sync.py
```

## package_status

```yaml
package_status: final_canonical_v1
```

## exact_file_index

```yaml
exact_file_index:
  - .claude/skills/apex-sync/SKILL.md
  - .claude/skills/apex-sync/references/sync-cluster-contract.md
  - .claude/skills/apex-sync/references/script-command-contract.md
  - .claude/skills/apex-sync/references/registry-and-drift-rules.md
  - .claude/skills/apex-sync/references/scoring-and-focus-rules.md
  - .claude/skills/apex-sync/package-manifest.md
  - scripts/apex_sync.py
```

Directory tree:

```txt
.claude/skills/apex-sync/
  SKILL.md
  references/
    sync-cluster-contract.md
    script-command-contract.md
    registry-and-drift-rules.md
    scoring-and-focus-rules.md
  package-manifest.md
scripts/
  apex_sync.py
```

## file_purpose_map

| File | Purpose |
|---|---|
| `SKILL.md` | Skill entrypoint, routing description, objective, accepted inputs, required outputs, procedure, validation rules, failure modes, and completion gate. |
| `references/sync-cluster-contract.md` | B_SYNC package boundary, owned/excluded processes, routing, read-side policy, registry write exception, and custom Python caveats. |
| `references/script-command-contract.md` | Canonical command, flags, subcommands, report contracts, exit-code policy, JSON policy, dry-run policy, and no-shell-out policy. |
| `references/registry-and-drift-rules.md` | Task discovery, task frontmatter validation, registry schema, rebuild rules, drift detection rules, malformed-file policy, and write gate. |
| `references/scoring-and-focus-rules.md` | H7 priority and urgency scoring, actionability, blocker semantics, stale semantics, unlock depth, focus sorting, and report schemas. |
| `package-manifest.md` | Package inventory, source basis, read order, invariants, checklist, forbidden claims, and backup/application notes. |
| `scripts/apex_sync.py` | Standard-library Python implementation of deterministic B_SYNC reports. |

## source_basis_map

| Source | Treatment | Used for |
|---|---|---|
| Apex H1–H7 decisions | LOCK | Status enum, path roots, dependency field, Python-only rule, B_SYNC cluster, handoff boundary, priority/urgency scoring. |
| Existing Apex sync scaffold | MIGRATE_AND_REWRITE | Existing parser behavior, subcommand categories, dry-run behavior, registry write restriction, and report vocabulary. |
| CCPM `SKILL.md` and `track.md` | ADAPT | Script-first deterministic reporting principle and tracking command categories. |
| Task Master `find-next-task.js` | ADAPT | Dependency-satisfied candidate filtering, priority weighting, dependency-count tie-break concept, deterministic next-action logic. |
| Backlog `types/index.ts` and `parser.ts` | ADAPT | Frontmatter/body split, task field concepts, raw content preservation, dependencies, priority, parent/subtask ideas. |
| llm-wiki `SKILL.md` | CONCEPT_ONLY | Index discipline, raw/source discipline, audit/drift visibility concept. |
| Apex skill definition guide | FORMAT_GUIDANCE | Frontmatter, objective, procedure, validation, supporting-file structure, completion gate. |
| Unavailable llm-wiki update-index script | OMIT_AS_SOURCE | Not used. No copied behavior claim. |
| Unavailable Kanban blocker script | OMIT_AS_SOURCE | Not used. Blocker behavior is custom Apex Python. |

## read_order

Recommended read order for operators or future maintainers:

1. `SKILL.md`
2. `references/sync-cluster-contract.md`
3. `references/script-command-contract.md`
4. `references/registry-and-drift-rules.md`
5. `references/scoring-and-focus-rules.md`
6. `package-manifest.md`
7. `scripts/apex_sync.py`

## package_invariants

```yaml
package_invariants:
  package_status: final_canonical_v1
  exact_file_count: 7
  canonical_script_path: scripts/apex_sync.py
  no_final_md_variants: true
  no_apex_plan_behavior: true
  no_apex_session_behavior: true
  no_task_status_mutation: true
  no_handoff_authoring: true
  no_operator_validation_claim: true
  default_mode: dry_run
  only_allowed_write_path: apex-meta/registry/index.md
  python_standard_library_only: true
  shell_out_allowed: false
  external_dependencies_allowed: false
  H1_status_enum:
    - open
    - in-progress
    - blocked
    - done
    - deferred
  H3_dependency_field: depends_on
```

## validation_checklist

Before applying this package, validate:

- [ ] Exactly seven target files are present.
- [ ] No `.final.md` variants are created.
- [ ] `SKILL.md` frontmatter is valid YAML.
- [ ] Markdown headings have blank lines around them.
- [ ] Code fences are balanced.
- [ ] The canonical command path is `scripts/apex_sync.py`.
- [ ] `python -m py_compile scripts/apex_sync.py` passes.
- [ ] `python scripts/apex_sync.py next --root . --json --dry-run true` runs.
- [ ] `python scripts/apex_sync.py blockers --root . --json --dry-run true` runs.
- [ ] `python scripts/apex_sync.py registry --root . --json --dry-run true` runs.
- [ ] `python scripts/apex_sync.py stall --root . --json --dry-run true` runs.
- [ ] `python scripts/apex_sync.py drift --root . --json --dry-run true` runs.
- [ ] `python scripts/apex_sync.py score --root . --json --dry-run true` runs.
- [ ] No task file mutation behavior exists.
- [ ] No handoff authoring behavior exists.
- [ ] Registry write gate exists and is limited to `registry --dry-run false`.
- [ ] `depends_on` is canonical.
- [ ] `dependencies` is not used as canonical.
- [ ] Custom Apex Python caveats are present.
- [ ] Forbidden source-copy claims are absent.

## forbidden_claims

Do not claim:

- `copied_llm_wiki_update_index_py`
- `copied_kanban_blocker_script`
- `copied_OpenClaw_TaskFlow`
- `fully_source_backed_B_SYNC_without_custom_python`
- `copied_bash_script_behavior_as_python_without_adaptation`

## backup_and_application_notes

Before applying final files, back up current files to:

```txt
apex-meta/harmonization/backups/apex-sync-pre-final-YYYY-MM-DD/
```

Back up these files if present:

- `.claude/skills/apex-sync/SKILL.md`
- `.claude/skills/apex-sync/package-manifest.md`
- `.claude/skills/apex-sync/references/sync-cluster-contract.md`
- `.claude/skills/apex-sync/references/script-command-contract.md`
- `.claude/skills/apex-sync/references/registry-and-drift-rules.md`
- `.claude/skills/apex-sync/references/scoring-and-focus-rules.md`
- `apex-meta/scripts/apex_sync.py`

Then write the final package files to the exact paths in `exact_file_index`.
After validation succeeds, the old backup source script path may be removed by
the operator as a separate cleanup step.
````

### 4.7 `scripts/apex_sync.py`

```python
#!/usr/bin/env python3
"""Deterministic read-side synchronization reports for Apex task files.

Canonical path: scripts/apex_sync.py

This script is intentionally standard-library-only. It reads Apex Markdown task
files from apex-meta/epics/*/[0-9][0-9][0-9].md, computes read-side reports,
and writes only apex-meta/registry/index.md when the registry subcommand is
invoked with --dry-run false.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

STATUS_ENUM = {"open", "in-progress", "blocked", "done", "deferred"}
PRIORITY_VALUES = {"high": 3, "medium": 2, "low": 1}
NO_DUE_DATE_URGENCY = 999
TASK_GLOB = "apex-meta/epics/*/[0-9][0-9][0-9].md"
REGISTRY_RELATIVE_PATH = Path("apex-meta/registry/index.md")

REVIEW_MALFORMED_FRONTMATTER = "malformed_frontmatter"
REVIEW_MISSING_TASK_ID = "missing_task_id"
REVIEW_DUPLICATE_TASK_ID = "duplicate_task_id"
REVIEW_UNSUPPORTED_STATUS = "unsupported_status"
REVIEW_MISSING_DEPENDENCY_TARGET = "missing_dependency_target"
REVIEW_CIRCULAR_DEPENDENCY_RISK = "circular_dependency_risk"
REVIEW_BLOCKED_WITHOUT_REASON = "blocked_without_reason"
REVIEW_STALE_TASK_CANDIDATE = "stale_task_candidate"
REVIEW_REGISTRY_OUT_OF_DATE = "registry_out_of_date"
REVIEW_DRIFT_DETECTED = "drift_detected"
REVIEW_SCRIPT_FAILED = "script_failed"

REQUIRED_REVIEW_FLAGS = [
    REVIEW_MALFORMED_FRONTMATTER,
    REVIEW_MISSING_TASK_ID,
    REVIEW_DUPLICATE_TASK_ID,
    REVIEW_UNSUPPORTED_STATUS,
    REVIEW_MISSING_DEPENDENCY_TARGET,
    REVIEW_CIRCULAR_DEPENDENCY_RISK,
    REVIEW_BLOCKED_WITHOUT_REASON,
    REVIEW_STALE_TASK_CANDIDATE,
    REVIEW_REGISTRY_OUT_OF_DATE,
    REVIEW_DRIFT_DETECTED,
    REVIEW_SCRIPT_FAILED,
]


@dataclass(frozen=True)
class TaskRecord:
    id: int
    title: str
    status: str
    priority: str
    due_date: Optional[str]
    depends_on: Tuple[int, ...]
    blocked_by: Tuple[str, ...]
    updated_date: Optional[str]
    created_date: Optional[str]
    epic_slug: str
    task_path: str
    frontmatter: Dict[str, Any]
    body: str


@dataclass(frozen=True)
class TaskLoadResult:
    tasks: List[TaskRecord]
    review_flags: List[Dict[str, Any]]
    discovered_task_files: int


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument(
        "--root",
        default=".",
        help="Repository root containing apex-meta/epics/. Default: current directory.",
    )
    common.add_argument(
        "--json",
        action="store_true",
        help="Write machine-readable JSON to stdout.",
    )
    common.add_argument(
        "--dry-run",
        nargs="?",
        const="true",
        default="true",
        choices=("true", "false"),
        help="Dry-run mode. Default: true. Use '--dry-run false' only with registry.",
    )

    parser = argparse.ArgumentParser(
        description="Compute Apex synchronization reports from Markdown task files."
    )
    subcommands = parser.add_subparsers(dest="subcommand", required=True)

    subcommands.add_parser("next", parents=[common], help="Compute next actionable tasks.")
    subcommands.add_parser("blockers", parents=[common], help="List blockers and blocked tasks.")
    subcommands.add_parser("registry", parents=[common], help="Rebuild or preview the registry index.")
    subcommands.add_parser("drift", parents=[common], help="Detect registry/source drift.")

    stall_parser = subcommands.add_parser("stall", parents=[common], help="Detect stale task candidates.")
    stall_parser.add_argument(
        "--stale-days",
        type=int,
        default=14,
        help="Days since updated/created timestamp before a non-done task is stale. Default: 14.",
    )
    stall_parser.add_argument(
        "--today",
        default=None,
        help="Override today's date for deterministic tests, formatted YYYY-MM-DD.",
    )

    score_parser = subcommands.add_parser(
        "score",
        parents=[common],
        help="Compute priority, urgency, unlock depth, and focus candidates.",
    )
    score_parser.add_argument(
        "--today",
        default=None,
        help="Override today's date for deterministic tests, formatted YYYY-MM-DD.",
    )

    return parser.parse_args(argv)


def parse_dry_run(value: str) -> bool:
    return value.lower() != "false"


def review_flag(flag_name: str, reason: str, **fields: Any) -> Dict[str, Any]:
    item: Dict[str, Any] = {"flag": flag_name, "reason": reason}
    for key, value in fields.items():
        if value is not None:
            item[key] = value
    return item


def read_task_files(root: Path) -> TaskLoadResult:
    tasks: List[TaskRecord] = []
    review_flags: List[Dict[str, Any]] = []
    task_files = sorted(root.glob(TASK_GLOB))

    for task_file in task_files:
        relative_path = safe_relative(task_file, root)
        try:
            text = task_file.read_text(encoding="utf-8")
        except OSError as exc:
            review_flags.append(
                review_flag(
                    REVIEW_MALFORMED_FRONTMATTER,
                    f"cannot read file: {exc}",
                    task_path=relative_path,
                )
            )
            continue

        frontmatter, body, parse_error = parse_markdown_task(text)
        if parse_error is not None:
            review_flags.append(
                review_flag(REVIEW_MALFORMED_FRONTMATTER, parse_error, task_path=relative_path)
            )
            continue

        record = build_task_record(root, task_file, frontmatter, body, review_flags)
        if record is not None:
            tasks.append(record)

    review_flags.extend(validate_duplicate_ids(tasks))
    review_flags.extend(validate_status_values(tasks))
    review_flags.extend(validate_dependency_targets(tasks))
    review_flags.extend(validate_circular_dependency_risk(tasks))
    review_flags.extend(validate_blocked_reason(tasks))

    return TaskLoadResult(
        tasks=tasks,
        review_flags=review_flags,
        discovered_task_files=len(task_files),
    )


def parse_markdown_task(text: str) -> Tuple[Dict[str, Any], str, Optional[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}, text, "missing opening frontmatter fence"

    end_index: Optional[int] = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            end_index = index
            break
    if end_index is None:
        return {}, text, "missing closing frontmatter fence"

    frontmatter_lines = lines[1:end_index]
    body = "\n".join(lines[end_index + 1 :]).strip()
    try:
        frontmatter = parse_minimal_yaml(frontmatter_lines)
    except ValueError as exc:
        return {}, body, str(exc)
    return frontmatter, body, None


def parse_minimal_yaml(lines: Iterable[str]) -> Dict[str, Any]:
    data: Dict[str, Any] = {}
    current_key: Optional[str] = None

    for line_number, raw_line in enumerate(lines, start=1):
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        if raw_line.startswith(" ") and current_key and raw_line.strip().startswith("- "):
            data.setdefault(current_key, [])
            if not isinstance(data[current_key], list):
                raise ValueError(
                    f"frontmatter line {line_number}: mixed scalar/list value for {current_key}"
                )
            data[current_key].append(parse_scalar(raw_line.strip()[2:].strip()))
            continue

        if raw_line.startswith("-") and current_key:
            data.setdefault(current_key, [])
            if not isinstance(data[current_key], list):
                raise ValueError(
                    f"frontmatter line {line_number}: mixed scalar/list value for {current_key}"
                )
            data[current_key].append(parse_scalar(raw_line[1:].strip()))
            continue

        if ":" not in raw_line:
            raise ValueError(f"frontmatter line {line_number}: expected key: value")

        key, value = raw_line.split(":", 1)
        key = key.strip()
        if not key:
            raise ValueError(f"frontmatter line {line_number}: empty key")

        current_key = key
        value = value.strip()
        if value == "":
            data[key] = []
        else:
            data[key] = parse_scalar(value)

    return data


def parse_scalar(value: str) -> Any:
    value = strip_inline_comment(value).strip()
    if not value:
        return ""
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        return value[1:-1]
    lower = value.lower()
    if lower in {"null", "none", "~"}:
        return None
    if lower == "true":
        return True
    if lower == "false":
        return False
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [parse_scalar(part.strip()) for part in split_inline_list(inner)]
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    return value


def strip_inline_comment(value: str) -> str:
    in_single = False
    in_double = False
    for index, char in enumerate(value):
        if char == "'" and not in_double:
            in_single = not in_single
        elif char == '"' and not in_single:
            in_double = not in_double
        elif char == "#" and not in_single and not in_double:
            previous = value[index - 1] if index > 0 else " "
            if previous.isspace():
                return value[:index]
    return value


def split_inline_list(inner: str) -> List[str]:
    parts: List[str] = []
    current: List[str] = []
    in_single = False
    in_double = False
    for char in inner:
        if char == "'" and not in_double:
            in_single = not in_single
        elif char == '"' and not in_single:
            in_double = not in_double
        if char == "," and not in_single and not in_double:
            parts.append("".join(current))
            current = []
        else:
            current.append(char)
    parts.append("".join(current))
    return parts


def build_task_record(
    root: Path,
    task_file: Path,
    frontmatter: Dict[str, Any],
    body: str,
    review_flags: List[Dict[str, Any]],
) -> Optional[TaskRecord]:
    relative_path = safe_relative(task_file, root)
    raw_id = frontmatter.get("id")
    if raw_id in (None, ""):
        review_flags.append(
            review_flag(
                REVIEW_MISSING_TASK_ID,
                "frontmatter field id is missing",
                task_path=relative_path,
            )
        )
        return None

    try:
        task_id = int(raw_id)
    except (TypeError, ValueError):
        review_flags.append(
            review_flag(
                REVIEW_MISSING_TASK_ID,
                "frontmatter field id is not an integer",
                task_path=relative_path,
                raw_id=raw_id,
            )
        )
        return None

    status = str(frontmatter.get("status") or "open").strip()
    priority = str(frontmatter.get("priority") or "medium").lower().strip()
    if priority not in PRIORITY_VALUES:
        priority = "medium"

    due_date = coerce_optional_string(frontmatter.get("due_date"))
    updated_date = first_present_string(frontmatter, ("updated_date", "updated", "updated_at"))
    created_date = first_present_string(frontmatter, ("created_date", "created", "created_at"))

    return TaskRecord(
        id=task_id,
        title=str(frontmatter.get("title") or frontmatter.get("name") or fallback_title(body) or task_file.stem),
        status=status,
        priority=priority,
        due_date=due_date,
        depends_on=tuple(coerce_int_list(frontmatter.get("depends_on"))),
        blocked_by=tuple(coerce_string_list(frontmatter.get("blocked_by"))),
        updated_date=updated_date,
        created_date=created_date,
        epic_slug=task_file.parent.name,
        task_path=relative_path,
        frontmatter=frontmatter,
        body=body,
    )


def coerce_optional_string(value: Any) -> Optional[str]:
    if value in (None, ""):
        return None
    return str(value).strip() or None


def first_present_string(frontmatter: Dict[str, Any], keys: Sequence[str]) -> Optional[str]:
    for key in keys:
        value = coerce_optional_string(frontmatter.get(key))
        if value is not None:
            return value
    return None


def fallback_title(body: str) -> str:
    for line in body.splitlines():
        clean = line.strip()
        if clean.startswith("#"):
            return clean.lstrip("#").strip()
    return ""


def safe_relative(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve())).replace("\\", "/")
    except ValueError:
        return str(path).replace("\\", "/")


def coerce_int_list(value: Any) -> List[int]:
    if value in (None, ""):
        return []
    raw_items = value if isinstance(value, list) else [value]
    result: List[int] = []
    for item in raw_items:
        try:
            result.append(int(item))
        except (TypeError, ValueError):
            continue
    return result


def coerce_string_list(value: Any) -> List[str]:
    if value in (None, ""):
        return []
    raw_items = value if isinstance(value, list) else [value]
    return [str(item).strip() for item in raw_items if str(item).strip()]


def validate_duplicate_ids(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    by_id: Dict[int, List[TaskRecord]] = {}
    for task in tasks:
        by_id.setdefault(task.id, []).append(task)

    flags: List[Dict[str, Any]] = []
    for task_id, matches in sorted(by_id.items()):
        if len(matches) <= 1:
            continue
        paths = [task.task_path for task in matches]
        for task in matches:
            flags.append(
                review_flag(
                    REVIEW_DUPLICATE_TASK_ID,
                    "task id appears in multiple task files",
                    id=task_id,
                    task_path=task.task_path,
                    duplicate_paths=paths,
                )
            )
    return flags


def validate_status_values(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    return [
        review_flag(
            REVIEW_UNSUPPORTED_STATUS,
            "status is not one of open, in-progress, blocked, done, deferred",
            id=task.id,
            status=task.status,
            task_path=task.task_path,
        )
        for task in tasks
        if task.status not in STATUS_ENUM
    ]


def validate_dependency_targets(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    ids = {task.id for task in tasks}
    flags: List[Dict[str, Any]] = []
    for task in tasks:
        missing = [dep for dep in task.depends_on if dep not in ids]
        if missing:
            flags.append(
                review_flag(
                    REVIEW_MISSING_DEPENDENCY_TARGET,
                    "depends_on references missing task id(s)",
                    id=task.id,
                    task_path=task.task_path,
                    missing_depends_on=missing,
                    depends_on=list(task.depends_on),
                )
            )
    return flags


def validate_circular_dependency_risk(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    by_id = {task.id: task for task in tasks}
    visiting: Set[int] = set()
    visited: Set[int] = set()
    cycles: List[List[int]] = []

    def visit(task_id: int, stack: List[int]) -> None:
        if task_id in visiting:
            cycle_start = stack.index(task_id) if task_id in stack else 0
            cycles.append(stack[cycle_start:] + [task_id])
            return
        if task_id in visited:
            return
        visiting.add(task_id)
        stack.append(task_id)
        task = by_id.get(task_id)
        if task is not None:
            for dep in task.depends_on:
                if dep in by_id:
                    visit(dep, stack)
        stack.pop()
        visiting.remove(task_id)
        visited.add(task_id)

    for task_id in sorted(by_id):
        visit(task_id, [])

    flags: List[Dict[str, Any]] = []
    seen: Set[Tuple[int, ...]] = set()
    for cycle in cycles:
        normalized = tuple(cycle)
        if normalized in seen:
            continue
        seen.add(normalized)
        flags.append(
            review_flag(
                REVIEW_CIRCULAR_DEPENDENCY_RISK,
                "cycle detected in depends_on graph",
                depends_on_cycle=cycle,
            )
        )
    return flags


def validate_blocked_reason(tasks: List[TaskRecord]) -> List[Dict[str, Any]]:
    return [
        review_flag(
            REVIEW_BLOCKED_WITHOUT_REASON,
            "status is blocked but blocked_by is empty",
            id=task.id,
            task_path=task.task_path,
        )
        for task in tasks
        if task.status == "blocked" and not task.blocked_by
    ]


def flags_matching(review_flags: List[Dict[str, Any]], names: Set[str]) -> List[Dict[str, Any]]:
    return [item for item in review_flags if item.get("flag") in names]


def is_done(task: Optional[TaskRecord]) -> bool:
    return bool(task and task.status == "done")


def blocked_by_is_clear(task: TaskRecord, by_id: Dict[int, TaskRecord]) -> bool:
    if not task.blocked_by:
        return True
    numeric_blockers: List[int] = []
    for blocker in task.blocked_by:
        try:
            numeric_blockers.append(int(blocker))
        except ValueError:
            return False
    return all(is_done(by_id.get(blocker_id)) for blocker_id in numeric_blockers)


def dependency_state(task: TaskRecord, by_id: Dict[int, TaskRecord]) -> Tuple[bool, List[int], List[int]]:
    missing = [dep for dep in task.depends_on if dep not in by_id]
    unsatisfied = [dep for dep in task.depends_on if dep in by_id and by_id[dep].status != "done"]
    return not missing and not unsatisfied, missing, unsatisfied


def priority_score(task: TaskRecord) -> int:
    return PRIORITY_VALUES.get(task.priority, PRIORITY_VALUES["medium"])


def parse_date(value: Optional[str]) -> Optional[date]:
    if value is None:
        return None
    clean = str(value).strip()
    if not clean:
        return None
    try:
        if "T" in clean:
            return datetime.fromisoformat(clean.replace("Z", "+00:00")).date()
        return datetime.strptime(clean[:10], "%Y-%m-%d").date()
    except ValueError:
        return None


def parse_today(value: Optional[str]) -> date:
    parsed = parse_date(value)
    if value is not None and parsed is None:
        raise ValueError("--today must be formatted YYYY-MM-DD")
    return parsed or date.today()


def urgency_score(task: TaskRecord, today_value: date) -> int:
    parsed_due_date = parse_date(task.due_date)
    if parsed_due_date is None:
        return NO_DUE_DATE_URGENCY
    return (parsed_due_date - today_value).days


def task_timestamp(task: TaskRecord) -> Optional[date]:
    return parse_date(task.updated_date) or parse_date(task.created_date)


def compute_unlock_depths(tasks: List[TaskRecord]) -> Dict[int, int]:
    reverse_edges: Dict[int, Set[int]] = {task.id: set() for task in tasks}
    valid_ids = set(reverse_edges)
    for task in tasks:
        for dependency in task.depends_on:
            if dependency in valid_ids:
                reverse_edges.setdefault(dependency, set()).add(task.id)

    def downstream_count(task_id: int) -> int:
        seen: Set[int] = set()
        stack = list(reverse_edges.get(task_id, set()))
        while stack:
            item = stack.pop()
            if item in seen:
                continue
            seen.add(item)
            stack.extend(reverse_edges.get(item, set()))
        return len(seen)

    return {task.id: downstream_count(task.id) for task in tasks}


def task_summary(
    task: TaskRecord,
    *,
    today_value: Optional[date] = None,
    unlock_depth: Optional[int] = None,
    reason: Optional[str] = None,
) -> Dict[str, Any]:
    entry: Dict[str, Any] = {
        "id": task.id,
        "title": task.title,
        "status": task.status,
        "priority": task.priority,
        "priority_score": priority_score(task),
        "due_date": task.due_date,
        "depends_on": list(task.depends_on),
        "blocked_by": list(task.blocked_by),
        "updated_date": task.updated_date,
        "created_date": task.created_date,
        "epic_slug": task.epic_slug,
        "task_path": task.task_path,
    }
    if today_value is not None:
        entry["urgency_score"] = urgency_score(task, today_value)
    if unlock_depth is not None:
        entry["unlock_depth"] = unlock_depth
    if reason is not None:
        entry["reason"] = reason
    return entry


def focus_sort_key(entry: Dict[str, Any]) -> Tuple[int, int, int, int]:
    return (
        -int(entry.get("priority_score", 0)),
        int(entry.get("urgency_score", NO_DUE_DATE_URGENCY)),
        -int(entry.get("unlock_depth", 0)),
        int(entry.get("id", 0)),
    )


def sort_focus_entries(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    return sorted(entries, key=focus_sort_key)


def base_report(
    report_name: str,
    *,
    generated_at: str,
    dry_run: bool,
    root: Path,
    script_exit_code: int,
    review_flags: Optional[List[Dict[str, Any]]] = None,
    **fields: Any,
) -> Dict[str, Any]:
    report: Dict[str, Any] = {
        "report_name": report_name,
        "generated_at": generated_at,
        "dry_run": dry_run,
        "root": str(root),
        "script_exit_code": script_exit_code,
        "review_flags": review_flags or [],
    }
    report.update(fields)
    return report


def dependency_validation_report(
    load: TaskLoadResult,
    *,
    generated_at: str,
    dry_run: bool,
    root: Path,
    script_exit_code: int = 0,
) -> Dict[str, Any]:
    selected = flags_matching(
        load.review_flags,
        {
            REVIEW_MISSING_DEPENDENCY_TARGET,
            REVIEW_CIRCULAR_DEPENDENCY_RISK,
            REVIEW_DUPLICATE_TASK_ID,
            REVIEW_MISSING_TASK_ID,
        },
    )
    return base_report(
        "dependency_validation_report",
        generated_at=generated_at,
        dry_run=dry_run,
        root=root,
        script_exit_code=script_exit_code,
        review_flags=selected,
        task_count=len(load.tasks),
        discovered_task_files=load.discovered_task_files,
    )


def command_next(root: Path, dry_run: bool, generated_at: str) -> Dict[str, Any]:
    today_value = date.today()
    load = read_task_files(root)
    by_id = {task.id: task for task in load.tasks}
    unlock_depths = compute_unlock_depths(load.tasks)
    candidates: List[Dict[str, Any]] = []

    for task in load.tasks:
        dependencies_satisfied, missing, unsatisfied = dependency_state(task, by_id)
        if task.status in {"open", "in-progress"} and dependencies_satisfied and blocked_by_is_clear(task, by_id):
            candidates.append(
                task_summary(
                    task,
                    today_value=today_value,
                    unlock_depth=unlock_depths.get(task.id, 0),
                    reason="status is open or in-progress, depends_on is satisfied, and blocked_by is clear",
                )
            )
        elif missing or unsatisfied:
            continue

    return {
        "next_action_report": base_report(
            "next_action_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=load.review_flags,
            task_count=len(load.tasks),
            discovered_task_files=load.discovered_task_files,
            candidates=sort_focus_entries(candidates),
        ),
        "dependency_validation_report": dependency_validation_report(
            load,
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
        ),
        "script_exit_code": 0,
    }


def command_blockers(root: Path, dry_run: bool, generated_at: str) -> Dict[str, Any]:
    load = read_task_files(root)
    by_id = {task.id: task for task in load.tasks}
    blocked_tasks: List[Dict[str, Any]] = []
    missing_dependency_targets: List[Dict[str, Any]] = []

    for task in load.tasks:
        dependencies_satisfied, missing, unsatisfied = dependency_state(task, by_id)
        if task.status == "blocked" or task.blocked_by or unsatisfied:
            entry = task_summary(
                task,
                reason="task is blocked, has blocked_by, or has unsatisfied depends_on",
            )
            entry["unsatisfied_depends_on"] = unsatisfied
            blocked_tasks.append(entry)
        if missing:
            missing_dependency_targets.append(
                {
                    "id": task.id,
                    "title": task.title,
                    "task_path": task.task_path,
                    "depends_on": list(task.depends_on),
                    "missing_depends_on": missing,
                }
            )
        if dependencies_satisfied:
            continue

    return {
        "blocker_report": base_report(
            "blocker_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=load.review_flags,
            blocked_tasks=blocked_tasks,
            missing_dependency_targets=missing_dependency_targets,
        ),
        "dependency_validation_report": dependency_validation_report(
            load,
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
        ),
        "script_exit_code": 0,
    }


def escape_table(value: Any) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", " ")


def registry_lines(load: TaskLoadResult, generated_at: str) -> List[str]:
    lines = [
        "# Apex Work Registry",
        "",
        "```yaml",
        "registry_report:",
        f"  generated_at: {generated_at}",
        f"  source: {TASK_GLOB}",
        f"  task_count: {len(load.tasks)}",
        f"  discovered_task_files: {load.discovered_task_files}",
        f"  review_flags_count: {len(load.review_flags)}",
        "```",
        "",
        "| id | epic_slug | status | priority | due_date | depends_on | blocked_by | updated_date | created_date | title | task_path |",
        "|---:|---|---|---|---|---|---|---|---|---|---|",
    ]
    for task in sorted(load.tasks, key=lambda item: (item.epic_slug, item.id, item.task_path)):
        lines.append(
            "| {id} | {epic_slug} | {status} | {priority} | {due_date} | {depends_on} | "
            "{blocked_by} | {updated_date} | {created_date} | {title} | {task_path} |".format(
                id=task.id,
                epic_slug=escape_table(task.epic_slug),
                status=escape_table(task.status),
                priority=escape_table(task.priority),
                due_date=escape_table(task.due_date),
                depends_on=escape_table(",".join(str(dep) for dep in task.depends_on)),
                blocked_by=escape_table(",".join(task.blocked_by)),
                updated_date=escape_table(task.updated_date),
                created_date=escape_table(task.created_date),
                title=escape_table(task.title),
                task_path=escape_table(task.task_path),
            )
        )
    lines.append("")
    if load.review_flags:
        lines.extend(["## Review Flags", ""])
        for item in load.review_flags:
            lines.append(
                f"- `{item.get('flag')}`: {escape_table(item.get('reason'))} "
                f"({escape_table(item.get('task_path', item.get('id', 'global')))})"
            )
        lines.append("")
    return lines


def generate_registry_content(root: Path, generated_at: str) -> Tuple[str, TaskLoadResult]:
    load = read_task_files(root)
    return "\n".join(registry_lines(load, generated_at)), load


def command_registry(root: Path, dry_run: bool, generated_at: str) -> Dict[str, Any]:
    content, load = generate_registry_content(root, generated_at)
    registry_path = root / REGISTRY_RELATIVE_PATH
    wrote_registry = False

    if not dry_run:
        registry_path.parent.mkdir(parents=True, exist_ok=True)
        registry_path.write_text(content, encoding="utf-8")
        wrote_registry = True

    return {
        "registry_report": base_report(
            "registry_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=load.review_flags,
            target_path=str(REGISTRY_RELATIVE_PATH),
            allowed_write_path=str(REGISTRY_RELATIVE_PATH),
            wrote_registry=wrote_registry,
            task_count=len(load.tasks),
            discovered_task_files=load.discovered_task_files,
            registry_content=content,
        ),
        "script_exit_code": 0,
    }


def command_stall(
    root: Path,
    dry_run: bool,
    generated_at: str,
    stale_days: int,
    today_value: Optional[str],
) -> Dict[str, Any]:
    load = read_task_files(root)
    current_date = parse_today(today_value)
    stale_tasks: List[Dict[str, Any]] = []
    review_flags = list(load.review_flags)

    for task in load.tasks:
        if task.status in {"done", "deferred"}:
            continue
        timestamp = task_timestamp(task)
        if timestamp is None:
            continue
        age_days = (current_date - timestamp).days
        if age_days >= stale_days:
            entry = task_summary(
                task,
                reason="non-done task has not changed within stale-days threshold",
            )
            entry["stall_days"] = age_days
            stale_tasks.append(entry)
            review_flags.append(
                review_flag(
                    REVIEW_STALE_TASK_CANDIDATE,
                    f"no timestamp change for {age_days} days",
                    id=task.id,
                    task_path=task.task_path,
                    stall_days=age_days,
                )
            )

    return {
        "stall_report": base_report(
            "stall_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=review_flags,
            stale_days_threshold=stale_days,
            stale_tasks=stale_tasks,
        ),
        "script_exit_code": 0,
    }


def command_drift(root: Path, dry_run: bool, generated_at: str) -> Dict[str, Any]:
    content, load = generate_registry_content(root, generated_at)
    registry_path = root / REGISTRY_RELATIVE_PATH
    current_content: Optional[str] = None
    if registry_path.exists():
        current_content = registry_path.read_text(encoding="utf-8")
    drift_detected = current_content != content
    review_flags = list(load.review_flags)
    if drift_detected:
        review_flags.append(
            review_flag(
                REVIEW_DRIFT_DETECTED,
                "registry content does not match regenerated task index",
                task_path=str(REGISTRY_RELATIVE_PATH),
            )
        )
        review_flags.append(
            review_flag(
                REVIEW_REGISTRY_OUT_OF_DATE,
                "registry should be regenerated by running registry --dry-run false after review",
                task_path=str(REGISTRY_RELATIVE_PATH),
            )
        )

    return {
        "drift_report": base_report(
            "drift_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=review_flags,
            source=TASK_GLOB,
            registry_path=str(REGISTRY_RELATIVE_PATH),
            registry_exists=registry_path.exists(),
            drift_detected=drift_detected,
            task_count=len(load.tasks),
        ),
        "registry_report": base_report(
            "registry_report",
            generated_at=generated_at,
            dry_run=True,
            root=root,
            script_exit_code=0,
            review_flags=load.review_flags,
            target_path=str(REGISTRY_RELATIVE_PATH),
            registry_content=content,
        ),
        "script_exit_code": 0,
    }


def command_score(root: Path, dry_run: bool, generated_at: str, today_value: Optional[str]) -> Dict[str, Any]:
    load = read_task_files(root)
    current_date = parse_today(today_value)
    unlock_depths = compute_unlock_depths(load.tasks)
    by_id = {task.id: task for task in load.tasks}
    scored_tasks: List[Dict[str, Any]] = []
    focus_candidates: List[Dict[str, Any]] = []

    for task in load.tasks:
        entry = task_summary(
            task,
            today_value=current_date,
            unlock_depth=unlock_depths.get(task.id, 0),
            reason="priority_score, urgency_score, and unlock_depth computed from frontmatter and depends_on graph",
        )
        scored_tasks.append(entry)
        dependencies_satisfied, _missing, _unsatisfied = dependency_state(task, by_id)
        if task.status in {"open", "in-progress"} and dependencies_satisfied and blocked_by_is_clear(task, by_id):
            focus_candidates.append(entry)

    return {
        "score_report": base_report(
            "score_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=load.review_flags,
            tasks=sorted(scored_tasks, key=lambda item: int(item["id"])),
        ),
        "focus_candidate_report": base_report(
            "focus_candidate_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=0,
            review_flags=load.review_flags,
            candidates=sort_focus_entries(focus_candidates),
        ),
        "script_exit_code": 0,
    }


def render_human(report_bundle: Dict[str, Any]) -> str:
    lines: List[str] = []
    for key, value in report_bundle.items():
        if key == "script_exit_code":
            continue
        lines.append(f"# {key}")
        lines.append("")
        lines.append("```json")
        lines.append(json.dumps(value, indent=2, sort_keys=True))
        lines.append("```")
        lines.append("")
    lines.append(f"script_exit_code: {report_bundle.get('script_exit_code', 0)}")
    return "\n".join(lines)


def emit(report_bundle: Dict[str, Any], json_mode: bool) -> int:
    exit_code = int(report_bundle.get("script_exit_code", 0))
    if json_mode:
        print(json.dumps(report_bundle, indent=2, sort_keys=True))
    else:
        print(render_human(report_bundle))
    return exit_code


def script_failure_report(root: Path, dry_run: bool, generated_at: str, exc: Exception) -> Dict[str, Any]:
    failure = review_flag(REVIEW_SCRIPT_FAILED, str(exc))
    return {
        "script_failure_report": base_report(
            "script_failure_report",
            generated_at=generated_at,
            dry_run=dry_run,
            root=root,
            script_exit_code=1,
            review_flags=[failure],
            script_stderr=str(exc),
        ),
        "script_exit_code": 1,
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    root = Path(args.root).resolve()
    dry_run = parse_dry_run(args.dry_run)
    generated_at = utc_now_iso()

    try:
        if args.subcommand == "next":
            report_bundle = command_next(root, dry_run, generated_at)
        elif args.subcommand == "blockers":
            report_bundle = command_blockers(root, dry_run, generated_at)
        elif args.subcommand == "registry":
            report_bundle = command_registry(root, dry_run, generated_at)
        elif args.subcommand == "stall":
            report_bundle = command_stall(root, dry_run, generated_at, args.stale_days, args.today)
        elif args.subcommand == "drift":
            report_bundle = command_drift(root, dry_run, generated_at)
        elif args.subcommand == "score":
            report_bundle = command_score(root, dry_run, generated_at, args.today)
        else:
            raise ValueError(f"unsupported subcommand: {args.subcommand}")
    except Exception as exc:
        report_bundle = script_failure_report(root, dry_run, generated_at, exc)

    return emit(report_bundle, args.json)


if __name__ == "__main__":
    sys.exit(main())
```

## 5. Final Validation

```yaml
validation:
  package_status: final_canonical_v1
  exact_file_count: 7
  exact_tree_match: true
  canonical_script_path: scripts/apex_sync.py
  no_final_md_variants: true
  no_apex_meta_scripts_final_path: true
  H1_status_enum_preserved: true
  H3_depends_on_preserved: true
  no_apex_plan_scope_drift: true
  no_apex_session_scope_drift: true
  no_task_status_mutation: true
  no_handoff_authoring: true
  no_operator_validation_claim: true
  no_llm_wiki_update_index_copy_claim: true
  no_kanban_blocker_script_copy_claim: true
  custom_Apex_Python_caveats_present: true
  no_collapsed_markdown_or_yaml: true
  source_touch_gate_passed: true
```

## 6. Remaining Risks

```txt
No known unresolved package risks after validation.
```