# Batch 03 — Apex Sync Ingest Analysis

## source_scope

```yaml
batch_focus: apex_sync_package
source_root: .claude/skills/apex-sync/
phase: ingest_phase_1
phase2_allowed: false
```

## source_files_read

```yaml
source_files_read:
  - path: .claude/skills/apex-sync/SKILL.md
    lines: 1-210
  - path: .claude/skills/apex-sync/package-manifest.md
    lines: 1-172
```

## source_grounded_claims

```yaml
claims:
  - id: S001
    text: "apex-sync is a deterministic read-side synchronization skill that reads Apex task files and produces canonical reports."
    source: ".claude/skills/apex-sync/SKILL.md lines 16-25, 45-57"
    confidence: high
    label: source_backed_summary

  - id: S002
    text: "apex-sync delegates exact computation to scripts/apex_sync.py and uses the command shape python scripts/apex_sync.py <subcommand> --root . --json --dry-run true."
    source: ".claude/skills/apex-sync/SKILL.md lines 80-111; .claude/skills/apex-sync/package-manifest.md lines 11-16, 24-35"
    confidence: high
    label: source_backed_summary

  - id: S003
    text: "apex-sync allows subcommands next, blockers, registry, stall, drift, and score."
    source: ".claude/skills/apex-sync/SKILL.md lines 88-96, 129-135"
    confidence: high
    label: raw_source

  - id: S004
    text: "The default sync mode is dry-run; the only allowed non-dry-run command is registry with --dry-run false, and the only allowed write path is apex-meta/registry/index.md."
    source: ".claude/skills/apex-sync/SKILL.md lines 21-23, 97-108, 137-145; .claude/skills/apex-sync/package-manifest.md lines 90-115"
    confidence: high
    label: source_backed_summary

  - id: S005
    text: "apex-sync validation preserves H1 status values, treats depends_on as integer task ids, requires dependency targets to exist and be done for actionability, and reports malformed or inconsistent task data."
    source: ".claude/skills/apex-sync/SKILL.md lines 155-178"
    confidence: high
    label: source_backed_summary

  - id: S006
    text: "apex-sync must not claim apex-plan behavior, apex-session behavior, task status mutation, handoff authoring, or operator validation."
    source: ".claude/skills/apex-sync/SKILL.md lines 120-123, 143-145, 195-210; .claude/skills/apex-sync/package-manifest.md lines 90-115"
    confidence: high
    label: source_backed_summary
```

## concepts_extracted

```yaml
concepts:
  - slug: deterministic-read-side-sync
    description: "Sync computes reports from task files without changing task/session state."
  - slug: apex-sync-command-contract
    description: "All exact computation routes through scripts/apex_sync.py with known subcommands and JSON/dry-run conventions."
  - slug: registry-write-exception
    description: "The registry subcommand may write apex-meta/registry/index.md only with explicit non-dry-run."
  - slug: dependency-validation-reporting
    description: "Sync reports dependency, blocker, circularity, stale, and drift issues instead of mutating them."
```

## entities_or_roles_extracted

```yaml
entities:
  - name: apex-sync
    role: deterministic_sync_report_skill
  - name: scripts/apex_sync.py
    role: canonical_computation_script
  - name: apex-meta/registry/index.md
    role: registry_file_with_limited_write_exception
  - name: references/script-command-contract.md
    role: command_and_flag_contract
  - name: references/registry-and-drift-rules.md
    role: registry_and_drift_validation_contract
  - name: references/scoring-and-focus-rules.md
    role: scoring_focus_and_actionability_contract
```

## contradictions_or_tensions

```yaml
tensions:
  - id: S-T001
    text: "apex-sync is non-mutating for task/session state but has a narrow registry write exception, so Phase 2 must describe it as read-side plus exception rather than read-only without qualification."
    source: ".claude/skills/apex-sync/SKILL.md lines 21-23, 97-108"
    confidence: high
    label: source_backed_summary
  - id: S-T002
    text: "The SKILL file says supporting file navigation includes scripts/apex_sync.py, while the package manifest places it outside the package root; this is not a contradiction but a path-boundary point."
    source: ".claude/skills/apex-sync/SKILL.md lines 67-79; .claude/skills/apex-sync/package-manifest.md lines 37-50"
    confidence: medium
    label: working_hypothesis
```

## migration_notes

```yaml
migration_notes:
  - "Phase 2 should produce an apex-sync command contract concept page only after reading references/script-command-contract.md."
  - "Treat scripts/apex_sync.py as an entity even though it is outside .claude/skills/apex-sync/."
  - "Highlight dry-run default and registry write exception in the compiled wiki because this is the main safety gate."
```

## proposed_phase2_targets

```yaml
proposed_phase2_targets:
  summaries:
    - apex-sync-package-summary
  concepts:
    - deterministic-read-side-sync
    - apex-sync-command-contract
    - registry-write-exception
    - dependency-validation-reporting
  entities:
    - apex-sync
    - scripts-apex-sync-py
    - apex-meta-registry-index-md
```

## operator_gate

```yaml
operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
```
