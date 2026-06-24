# Apex KB ChatGPT Edit Verification

This folder records deterministic verification material for the accidental Apex KB ChatGPT edits from 2026-06-24.

Backup branch: $BackupRef

Audited commits:
- ac259b632f77d0836aef722b1b640392f623f24d
- 96b21e861c738fd2ccb2eaa7abecf509a924a487
- daa8e25e1758192ffc9632e9629070a38d7c1d8d
- cc9f69ad44280615368877d6234bc3983d7fba54
- ae59348c953b9a946638c4bd25f1a1f013e2c064
- d5e9dd0eac2ec44797764a3558f5087ff62c503d
- 84757a7b0498b76710c78bae0b1e25d48c2bfc48

Touched files:
- .claude/skills/apex-kb/references/source-custody-and-read-verification.md
- .claude/skills/apex-kb/templates/source-intake-lock-template.md
- .claude/skills/apex-kb/SKILL.md
- .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
- .claude/skills/apex-kb/templates/ingest-analysis-template.md
- .claude/skills/apex-kb/package-manifest.md
- .claude/skills/apex-kb/references/kb-contract.md

Safe next actions:
- Review files under diffs/ and reports under eports/.
- Compare efore/ and fter/ with git diff --no-index.
- Decide whether to keep, revert, or branch from $BackupRef.

Unsafe next actions:
- Do not continue Apex KB design/update work until the operator decides.
- Do not modify .claude/skills/apex-kb/ as part of this verification.
- Do not run ingestion for this verification task.

If a user stash needs restoration later, inspect it first with git stash list and git stash show --stat <stash>, then restore only after operator approval. This script does not restore stashes.
