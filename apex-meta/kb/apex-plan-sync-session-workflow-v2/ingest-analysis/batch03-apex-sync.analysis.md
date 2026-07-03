# Apex Sync

## source_scope

```yaml
source_scope:
  kb_slug: apex-plan-sync-session-workflow-v2
  batch: batch03-apex-sync
  purpose: "Extract apex-sync report ownership, scripts/apex_sync.py role, dry-run policy, registry exception, validation rules, and boundaries."
  phase2_outputs_created: false
```

## source_files_read

```yaml
source_files_read:
  - ".claude/skills/apex-sync/SKILL.md"
  - ".claude/skills/apex-sync/package-manifest.md"
```

## source_grounded_claims

```yaml
claims:
  - claim:
      id: C001
      text: "apex-sync computes deterministic read-side reports for next actions, blockers, stale tasks, registry previews, drift checks, dependency validation, priority, urgency, unlock depth, and focus candidates."
      source: ".claude/skills/apex-sync/SKILL.md#frontmatter description lines 3-10"
      confidence: high
      label: raw_source
  - claim:
      id: C002
      text: "apex-sync reads task frontmatter and Markdown body content under apex-meta/epics and delegates exact computation to scripts/apex_sync.py."
      source: ".claude/skills/apex-sync/SKILL.md#Objective lines 18-21"
      confidence: high
      label: raw_source
  - claim:
      id: C003
      text: "Canonical apex-sync reports are next_action_report, blocker_report, registry_report, stall_report, drift_report, score_report, focus_candidate_report, and dependency_validation_report."
      source: ".claude/skills/apex-sync/SKILL.md#Required Outputs lines 45-57"
      confidence: high
      label: raw_source
  - claim:
      id: C004
      text: "Each JSON report must include report_name, generated_at, dry_run, root, script_exit_code, and review_flags."
      source: ".claude/skills/apex-sync/SKILL.md#Required Outputs lines 58-66"
      confidence: high
      label: raw_source
  - claim:
      id: C005
      text: "The canonical command shape is python scripts/apex_sync.py <subcommand> --root . --json --dry-run true."
      source: ".claude/skills/apex-sync/SKILL.md#Canonical Command Policy lines 80-86"
      confidence: high
      label: raw_source
  - claim:
      id: C006
      text: "Allowed subcommands are next, blockers, registry, stall, drift, and score."
      source: ".claude/skills/apex-sync/SKILL.md#Canonical Command Policy lines 88-96"
      confidence: high
      label: raw_source
  - claim:
      id: C007
      text: "The default mode is dry-run, and the only non-dry-run command allowed by this package is registry --dry-run false."
      source: ".claude/skills/apex-sync/SKILL.md#Canonical Command Policy lines 97-103"
      confidence: high
      label: raw_source
  - claim:
      id: C008
      text: "The registry write exception may write only apex-meta/registry/index.md."
      source: ".claude/skills/apex-sync/SKILL.md#Canonical Command Policy lines 104-108; package-manifest.md#package_invariants lines 103-105"
      confidence: high
      label: raw_source
  - claim:
      id: C009
      text: "apex-sync validation rules cover the exact H1 status values, depends_on integer ids, actionability, blocked-without-reason cases, malformed frontmatter, duplicate ids, missing dependencies, circular dependency risk, and registry drift."
      source: ".claude/skills/apex-sync/SKILL.md#Validation Rules lines 155-178"
      confidence: high
      label: source_backed_summary
  - claim:
      id: C010
      text: "apex-sync must not capture projects, decompose work, mutate task status, author handoff files, validate operator decisions, or write session narrative."
      source: ".claude/skills/apex-sync/SKILL.md#frontmatter lines 9-11; Objective lines 24-25; Procedure lines 120-145"
      confidence: high
      label: raw_source
```

## concepts_extracted

```yaml
concepts_extracted:
  - deterministic-read-side-report
  - dry-run-default
  - registry-write-exception
  - dependency-validation-report
  - registry-drift
  - actionability-rule
  - focus-candidate-report
```

## entities_or_roles_extracted

```yaml
entities_or_roles_extracted:
  - entity: apex-sync
    role: "deterministic read-side synchronization package"
  - entity: scripts/apex_sync.py
    role: "canonical Python command for exact computation"
  - entity: apex-meta/registry/index.md
    role: "only allowed write target under registry exception"
  - entity: Apex task files
    role: "task evidence read by sync reports"
  - entity: operator
    role: "explicit dry-run false authority for registry exception"
```

## contradictions_or_tensions

```yaml
contradictions_or_tensions:
  - id: T001
    text: "apex-sync is read-side by default but has one narrow registry write exception."
    source: ".claude/skills/apex-sync/SKILL.md lines 18-25 and 97-108"
    status: intentional_exception
  - id: T002
    text: "apex-sync computes focus candidates but must not add planning recommendations or session narrative."
    source: ".claude/skills/apex-sync/SKILL.md lines 55-56 and 143-145"
    status: report_vs_planning_boundary
  - id: T003
    text: "apex-sync may report blockers and stale tasks but must not mutate task or handoff files."
    source: ".claude/skills/apex-sync/SKILL.md lines 49-56, 176-177, 189-190"
    status: report_vs_mutation_boundary
```

## migration_notes

```yaml
migration_notes:
  - "Represent apex-sync as the deterministic computation/report package around scripts/apex_sync.py."
  - "Preserve dry-run default as a gate."
  - "Document registry --dry-run false as an exception."
  - "Keep validation outputs as reports with review_flags, not narrative."
```

## proposed_phase2_targets

```yaml
proposed_phase2_targets:
  summaries:
    - apex-sync-package-summary
  concepts:
    - deterministic-read-side-report
    - dry-run-default
    - registry-write-exception
    - dependency-validation-report
    - registry-drift
    - actionability-rule
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
