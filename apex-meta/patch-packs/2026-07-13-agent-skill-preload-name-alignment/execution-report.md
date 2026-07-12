# Execution report — agent skill preload name alignment

## Scope

Only these three frontmatter values changed:

| Agent file | Previous `skills:` value | Canonical package name |
|---|---|---|
| `.claude/agents/apex-precap-week.md` | `PrecapWeek` | `precap-week` |
| `.claude/agents/apex-precap-next-day.md` | `PrecapNextDay` | `precap-next-day` |
| `.claude/agents/apex-project-status.md` | `ProjectStatus` | `project-status-overview` |

The canonical names are declared in the corresponding live `SKILL.md` frontmatter. Each agent body
already referred to that same canonical skill name; this repair aligns only its preload declaration.

## Deterministic process

- Executor: `.claude/skills/deterministic-markdown-patcher2/scripts/patch_executor.py`
- Policy: `patch_policy.json` limits mutation to the three files above and forbids full-file rewrites.
- Intent: `patch_intent.json` uses `frontmatter-set`; follow-up intent files restore the original YAML
  list formatting while retaining the same canonical values.
- No commit or push was performed.

## Validation

| Check | Result |
|---|---|
| Intent and policy validation | PASS |
| YAML parsing of all three frontmatter blocks | PASS |
| Git whitespace check for the three target files | PASS |
| Diff scope | exactly 1 added line and 1 removed line per file |
| Final semantic diff | only the three `skills:` values changed |

Machine-readable executor output is in `reports/`. The target-file diff is intentionally limited to
the three replacements listed in the scope table.
