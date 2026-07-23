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

### `codex/weekly-orchestrator-audit`

- Branch tip: `c9900103ae8a1c0886a032dbeac275e1c7f7aa5c`
- Unique commit retained: `c9900103`
- The branch is chronologically later than the activation-validation work and provides the US-SEQ-01 lifecycle fixture plus contract/path-drift corrections.
- Current `main`'s newer two-orchestrator `.claude/Claude.md` remained current truth. The older weekly-only activation surface remains recoverable from `c9900103`.
- The branch's compact `AIRouting`, `PrecapWeek`, and `ProjectStatus` manifests were selected because they use the live package names and paths and remove stale package-shape drift.
- The audited evidence and skip-marker templates were selected because they avoid misleading live-example links.
- The activation report preserves both evidence sets: detailed link/fixture counts from the activation branch and link-audit, lifecycle, and synthetic US-SEQ-01 results from the weekly audit.

Example recovery commands:

```powershell
git show c9900103:.claude/Claude.md
git show c9900103:.claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md
git show c9900103:apex-meta/operator-output-design/step6-activation-validation/00-activation-validation-report.okf.md
```

### `codex/download-claude-orchestration-sources`

- Branch tip: `28c2f701`
- Unique commits retained: `17d4a5f0`, `cfdba974`, `28c2f701`
- Merge commit: `9bd50f8e2096e71eaae20243bdc7e70fd5baa31b`
- The merge was additive and conflict-free.
- The complete downloaded research corpus, source metadata, manifests, reports, logs, and download scripts are now reachable from `main`.

## Final reachability result

All three local branches that were not initially merged into `main` are now ancestors of `main`. No local branch was deleted. Branch names remain as convenience references, but the explicit merge commits -- not the continued existence of a local branch name -- are the durable preservation mechanism.
