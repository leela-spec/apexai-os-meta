# Migration and legacy surfaces

## Supported migration

`apex-kb status` detects legacy controlled runs and reports `migration_required` without changing them. The next supported `continue` or `update` creates a timestamped backup under `log/migrations/`, normalizes supported configuration into the current schema, records a migration result, and begins a controlled current-version run.

Migration does not infer completion from page counts, old status prose, or an existing search database. Current manifests, state, semantic acceptance, postflight, retrieval health, and completion evidence must satisfy the current contracts.

## Legacy scripts

Historical `apex_kb.py`, `apex_kb_start.py`, and `apex_kb_control.py` may be retained only as donors or clearly deprecated wrappers. They must not own configuration normalization, lifecycle state, next-action derivation, semantic orchestration, completion, or retrieval in parallel with the installed CLI.

The optional `.claude/skills/apex-kb/SKILL.md` is also a thin launcher. Removing it must not change direct `apex-kb` behavior.

## Operator rules

- Use public `start`, `status`, `continue`, `query`, `update`, and diagnostic `doctor` commands.
- Do not copy old control files over a current run.
- Do not edit run identity or configuration hashes to suppress drift.
- Preserve migration backups and repair evidence.
- If a legacy shape is not supported, stop with the reported blocker rather than inventing a transition.
