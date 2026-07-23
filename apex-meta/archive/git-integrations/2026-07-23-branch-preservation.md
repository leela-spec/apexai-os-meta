# Branch preservation record

## Purpose

This record documents the 2026-07-23 integration into `main`. The operator required all potentially valuable information to remain recoverable. No local branch was deleted, reset, rebased, or squashed. Explicit merge commits retain the complete commit graph and both parent trees.

## Working-material checkpoint

- Preservation commit: `2a183baf`
- Content retained: Apex KB audit handover, Phase 0 failure chat history, research reports, CLI design material, completion-gate notes, therapy Markdown sources, local configuration, and the existing CLI wrapper change.
- The prior bytes of files renamed or removed at the working-tree tip remain available from the parent history.

## Remote main integration

- Remote commit integrated: `b314b6e9`
- Merge commit: `39c20a30`
- Remote content retained: the newer `apex-meta/kb/therapy/raw/notes/MyTherapy.md`.

## Local branch integrations

### `fix/weekly-template-activation-validation`

- Branch tip: `c87edfcb3c844501b326d398282d10870888e541`
- Unique commits retained: `66ed8a3a`, `c87edfcb`
- Added artifacts and non-conflicting corrections were integrated into the current tree.
- Two package-manifest conflicts were resolved in favor of the newer compact `main` manifests:
  - `.claude/skills/project-kb-manager/package-manifest.md`
  - `.claude/skills/status-merge/package-manifest.md`
- The branch versions were not discarded. They remain byte-for-byte recoverable from the merge parent, for example:

```powershell
git show c87edfcb:.claude/skills/project-kb-manager/package-manifest.md
git show c87edfcb:.claude/skills/status-merge/package-manifest.md
```

The branch-side status-merge manifest was not installed as current truth because it is an older verbose inventory, while `main` contains the newer compact live manifest and the promoted-template pointer. The historical inventory remains available through the retained parent commit.

## Remaining integration targets

The following local branches were identified as containing commits not yet reachable from `main` when this record was created:

- `codex/weekly-orchestrator-audit` at `c9900103`
- `codex/download-claude-orchestration-sources` at `28c2f701`

This record must be updated after those merges. Branch names may remain as convenience references, but the merge commits—not the continued existence of a local branch name—are the durable preservation mechanism.

