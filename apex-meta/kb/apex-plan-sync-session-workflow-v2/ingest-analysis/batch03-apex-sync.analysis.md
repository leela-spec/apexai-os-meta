# Apex Sync

## source_scope

apex-sync SKILL.md and package manifest only.

## source_files_read

- .claude/skills/apex-sync/SKILL.md
- .claude/skills/apex-sync/package-manifest.md

## source_grounded_claims

- apex-sync computes deterministic read-side reports over Apex task files.
- Canonical reports include next action, blockers, registry, stall, drift, score, focus candidates, and dependency validation.
- The canonical script path is scripts/apex_sync.py.
- Default mode is dry-run, with the only allowed write being apex-meta/registry/index.md through registry --dry-run false.

## concepts_extracted

- deterministic read-side synchronization
- dependency validation report
- registry drift
- blocker report
- stale task candidate
- focus candidate report

## entities_or_roles_extracted

- apex-sync package
- scripts/apex_sync.py
- registry index
- Apex task files

## contradictions_or_tensions

- apex-sync can compute focus candidates but must not add planning recommendations or session narrative.
- It can write the registry only through a narrowly gated exception.

## migration_notes

Represent apex-sync as the deterministic computation layer with JSON report contracts and dry-run-first behavior.

## proposed_phase2_targets

- wiki/entities/apex-sync.md
- wiki/entities/scripts-apex-sync-py.md
- wiki/concepts/read-side-synchronization.md
- wiki/concepts/registry-drift.md

## operator_gate

operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
