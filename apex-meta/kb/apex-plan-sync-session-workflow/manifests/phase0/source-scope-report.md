# Phase 0 Source Scope Report — Apex Plan Sync Session Workflow

```yaml
phase0_report:
  kb_slug: apex-plan-sync-session-workflow
  source_corpus_accessible: true
  source_roots:
    - .claude/skills/apex-plan/
    - .claude/skills/apex-sync/
    - .claude/skills/apex-session/
  deterministic_scope: source_pointer_manifest_and_read_ledger
  semantic_ingest_started_after_phase0: true
  phase2_allowed: false
  required_phrase: approve ingest
```

## Files read

| Source ID | Path | Lines read | Role |
|---|---|---:|---|
| APS-001 | `.claude/skills/apex-plan/SKILL.md` | 1-260 | Planning skill entrypoint and boundary contract |
| APS-002 | `.claude/skills/apex-plan/package-manifest.md` | 1-94 | Planning package inventory and acceptance checks |
| APS-003 | `.claude/skills/apex-sync/SKILL.md` | 1-210 | Deterministic sync entrypoint and command policy |
| APS-004 | `.claude/skills/apex-sync/package-manifest.md` | 1-172 | Sync package inventory and invariants |
| APS-005 | `.claude/skills/apex-session/SKILL.md` | 1-322 | Session mutation and handoff entrypoint |
| APS-006 | `.claude/skills/apex-session/package-manifest.md` | 1-335 | Session package inventory and invariants |

## Deterministic observations

```yaml
deterministic_observations:
  package_count: 3
  skill_entrypoints_read: 3
  package_manifests_read: 3
  common_status_enum:
    - open
    - in-progress
    - blocked
    - done
    - deferred
  main_path_surfaces:
    apex_plan:
      - apex-meta/epics/
      - apex-meta/registry/index.md
      - apex-meta/handoff/
    apex_sync:
      - apex-meta/epics/*/[0-9][0-9][0-9].md
      - apex-meta/registry/index.md
      - scripts/apex_sync.py
    apex_session:
      - task_plan.md
      - findings.md
      - progress.md
      - next-session.md
```

## Corpus-read limitation

Supporting references and templates were not fully read in this pass. This does not block Phase 1 because the entrypoints and manifests expose package ownership, handoff surfaces, file inventories, and acceptance gates. It does mean Phase 2 page synthesis should either remain high-level or read the relevant reference files before creating detailed concept/entity pages.
