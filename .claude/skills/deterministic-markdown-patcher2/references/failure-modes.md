# Failure Modes

## Canonical Modes

| Mode | Detection | Required response |
|---|---|---|
| target path outside allowlist | Target path does not match policy allowlist or matches protected paths. | Reject before reading or writing the target. |
| zero target matches | Live resolver cannot find a span, heading section, or frontmatter block. | Emit failure report with unresolved hints. |
| multiple target matches | Resolver finds more than one viable target. | Emit ambiguity report with candidate summaries. |
| duplicate or ambiguous heading path | Heading stack is not unique or is underspecified. | Require a unique heading path before mutation. |
| frontmatter missing when operation requires it | File lacks a parseable frontmatter block for a frontmatter operation. | Stop unless policy explicitly permits creation. |
| validation failed | Schema, fixture, command, or diff-scope validation fails. | Roll back or discard the worktree and report command output. |
| diff touches unallowed path | Git diff includes paths outside approved scope. | Roll back and report all unexpected paths. |
| optional tool requested as core | Plan depends on a trial-only or rejected tool as the primary mutator. | Replace with core executor path or mark unsupported. |

## Report Requirements

Failure reports must name the mode, the rejected operation, the governing policy or schema field, the safe candidate summary, rollback status, and the next acceptable operator action. Do not transform a failure into a best-effort edit.
