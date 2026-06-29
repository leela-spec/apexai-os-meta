# Apex KB Full Lifecycle Test Handover

## Current state

- Repo: `C:\GitDev\apexai-os-meta`
- Branch policy from operator: work directly on `main`; do not create task branches unless explicitly re-authorized.
- Canonical package: `.claude/skills/apex-kb/`
- Main scripts:
  - `apex-meta/scripts/apex_kb.py`
  - `apex-meta/scripts/apex_kb_retrieval.py`

## Recent completed work

- `apex_kb.py` was patched and pushed on `main` in commit `83b3792a`:
  - Phase 0 now scans both `<kb-root>/sources/` and `<kb-root>/raw/`.
  - Phase 0 reads `manifests/source-inventory.json` with `utf-8-sig`.
  - Phase 0 reports source inventory status in command output and `corpus-profile.md`.
- Generated Phase 0 outputs for `apex-meta/kb/claude-skill-design/` were explicitly committed and pushed in commit `3b824c5a`.
- `main` was clean and synced after that push.

## Suggested next-chat mission

Run a full Apex KB lifecycle test against a clearly chosen KB root, likely either:

- existing real KB: `apex-meta/kb/claude-skill-design/`
- temporary smoke KB: `apex-meta/kb/apex-kb-lifecycle-smoke/`

Recommended flow:

1. Confirm `git status --short --branch` on `main`.
2. Read live package files before acting:
   - `.claude/skills/apex-kb/SKILL.md`
   - `.claude/skills/apex-kb/package-manifest.md`
   - `.claude/skills/apex-kb/references/kb-contract.md`
   - `.claude/skills/apex-kb/references/script-command-contract.md`
   - `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md`
   - `.claude/skills/apex-kb/references/retrieval-contract.md`
   - `apex-meta/scripts/apex_kb.py`
   - `apex-meta/scripts/apex_kb_retrieval.py`
3. Run lifecycle commands end to end:
   - `scaffold`
   - `hash`
   - `source-intake`
   - `preflight`
   - `phase0`
   - `ingest-phase1`
   - blocked `ingest-phase2` with wrong phrase
   - allowed `ingest-phase2` with `approve ingest`
   - manual minimal compiled wiki page if using a smoke KB
   - `index`
   - retrieval `health`, `build-index`, `stale`, `query --save`, `export`
   - `lint --strict`, `audit`, `status`
4. Verify boundaries:
   - Phase 0 creates no semantic wiki pages.
   - Phase 0 creates no ingest analysis.
   - Phase 2 only validates the gate; Python must not invent wiki prose.
   - Retrieval indexes are derived and rebuildable.
   - No Apex Plan/Sync/Session/PreCap/FlowRecap/APSU mutation.
5. Commit only targeted source-code fixes if tests prove a defect. Do not commit smoke folders, caches, `node_modules`, or generated artifacts unless the operator explicitly asks.

## Known caveats

- `claude-skill-design` is a real KB with existing `sources/` and committed Phase 0 artifacts. Treat it as a test KB, not as a hardcoded default.
- If using a temporary smoke KB, remove it after recording results.
- The operator prefers direct `main` work and minimal branch overhead.
