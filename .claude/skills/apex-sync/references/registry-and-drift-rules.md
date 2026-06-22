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