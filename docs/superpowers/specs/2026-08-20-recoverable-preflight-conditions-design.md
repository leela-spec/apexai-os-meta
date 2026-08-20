# Recoverable Preflight Conditions Design

## Goal

Allow the deterministic Markdown patcher to repair and retry mechanical failures that have a single, verifiable, non-semantic remedy, without weakening target, scope, or content safeguards.

## Location and routing

Add `references/recoverable-preflight-conditions.md` to the `supporting_files` list in `.claude/skills/deterministic-markdown-patcher2/SKILL.md`. Its `read_when` triggers are `blocked_by_mechanical_or_environmental_failure` and `deciding_whether_to_repair_and_retry`.

## Policy

The reference is headed `# Recoverable Preflight Conditions` and uses a machine-readable YAML block. It permits only these preflight repairs: normalize text line endings for comparison; ignore trailing horizontal whitespace and whitespace-only blank lines for Markdown target resolution; remove a proven stale Git lock; retry a no-write transient tool or network failure within a bounded budget; canonicalize an in-repository path before allowlist enforcement.

The policy always requires a unique live target after repair, resolved-path allowlist enforcement, bounded retry, post-mutation diff-scope verification, and a machine-readable report. It prohibits automatic recovery from any ambiguity, visible content difference, path escape, active/unknown lock owner, partial mutation, rollback failure, unexpected diff, or policy/schema violation.

## Validation

Run the patch executor self-test, validate the two patch intents, apply through the executor, verify the expected routing and policy phrases, inspect the scoped Git diff, commit the two changed skill files, then pull/rebase if required and push `main`.
