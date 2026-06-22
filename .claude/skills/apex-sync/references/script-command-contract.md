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