# Batch 01 — Workflow Boundary Architecture

## source_scope

```yaml
kb_slug: apex-plan-sync-session-workflow
batch_focus: cross_package_boundary_architecture
source_roots:
  - .claude/skills/apex-plan/
  - .claude/skills/apex-sync/
  - .claude/skills/apex-session/
phase: ingest_phase_1
phase2_allowed: false
```

## source_files_read

```yaml
source_files_read:
  - path: .claude/skills/apex-plan/SKILL.md
    lines: 1-260
  - path: .claude/skills/apex-plan/package-manifest.md
    lines: 1-94
  - path: .claude/skills/apex-sync/SKILL.md
    lines: 1-210
  - path: .claude/skills/apex-sync/package-manifest.md
    lines: 1-172
  - path: .claude/skills/apex-session/SKILL.md
    lines: 1-322
  - path: .claude/skills/apex-session/package-manifest.md
    lines: 1-335
```

## source_grounded_claims

```yaml
claims:
  - id: C001
    text: "The three-package architecture separates planning, deterministic read-side computation, and session mutation/handoff into distinct skills."
    source: ".claude/skills/apex-plan/SKILL.md lines 26-47; .claude/skills/apex-sync/SKILL.md lines 18-25; .claude/skills/apex-session/SKILL.md lines 18-36"
    confidence: high
    label: source_backed_summary

  - id: C002
    text: "apex-plan owns qualitative planning and proposal creation but explicitly hands exact computation to apex-sync and confirmed writes/status/session work to apex-session."
    source: ".claude/skills/apex-plan/SKILL.md lines 26-47, 75-92, 141-155"
    confidence: high
    label: source_backed_summary

  - id: C003
    text: "apex-sync owns deterministic read-side reports over task files and delegates exact computation to scripts/apex_sync.py; it does not author handoffs or mutate task status."
    source: ".claude/skills/apex-sync/SKILL.md lines 18-25, 45-57, 80-111, 155-177"
    confidence: high
    label: source_backed_summary

  - id: C004
    text: "apex-session owns gated mutation records, state deltas, entity update records, H6 handoff artifacts, and next-session context; it explicitly excludes ranking, blocker scans, registry rebuilds, scoring, scripts, and decomposition."
    source: ".claude/skills/apex-session/SKILL.md lines 18-36, 109-129, 188-210, 212-262"
    confidence: high
    label: source_backed_summary

  - id: C005
    text: "The architecture uses a shared H1 status enum across the package boundary: open, in-progress, blocked, done, deferred."
    source: ".claude/skills/apex-plan/SKILL.md lines 48-55; .claude/skills/apex-sync/SKILL.md lines 157-162; .claude/skills/apex-session/SKILL.md lines 47-52"
    confidence: high
    label: source_backed_summary

  - id: C006
    text: "The central risk pattern is boundary collapse: apex-plan computing exact rank, apex-sync mutating state or authoring handoff files, or apex-session scanning/ranking/rebuilding."
    source: ".claude/skills/apex-plan/SKILL.md lines 80-92; .claude/skills/apex-sync/SKILL.md lines 120-149, 176-177; .claude/skills/apex-session/SKILL.md lines 250-262"
    confidence: high
    label: source_backed_summary
```

## concepts_extracted

```yaml
concepts:
  - slug: three_package_boundary
    description: "Apex Plan, Apex Sync, and Apex Session divide the workflow into proposal, deterministic validation/computation, and mutation/handoff memory."
  - slug: qualitative_vs_exact_computation
    description: "apex-plan may explain priority and urgency qualitatively, while apex-sync owns exact ranking/scoring."
  - slug: read_side_sync_boundary
    description: "apex-sync reads task state and produces reports, with a narrow registry write exception."
  - slug: operator_gated_session_mutation
    description: "apex-session can create mutation records but consequential mutations require operator validation before being treated as confirmed."
  - slug: shared_status_enum
    description: "All three packages preserve the H1 status vocabulary."
```

## entities_or_roles_extracted

```yaml
entities:
  - id: E001
    name: apex-plan
    role: qualitative_planning_and_handoff_request_skill
  - id: E002
    name: apex-sync
    role: deterministic_read_side_sync_and_report_skill
  - id: E003
    name: apex-session
    role: session_state_delta_mutation_gate_and_handoff_skill
  - id: E004
    name: scripts/apex_sync.py
    role: canonical_deterministic_sync_script
  - id: E005
    name: apex-meta/registry/index.md
    role: registry_surface_with_sync_write_exception
```

## contradictions_or_tensions

```yaml
tensions:
  - id: T001
    text: "apex-sync is mostly read-side and no-mutation, but it has an explicit registry write exception for registry --dry-run false."
    source: ".claude/skills/apex-sync/SKILL.md lines 21-23, 97-108"
    confidence: high
    label: source_backed_summary
  - id: T002
    text: "apex-plan references durable paths such as epics, registry, and handoff, but its own package boundary forbids durable writes."
    source: ".claude/skills/apex-plan/SKILL.md lines 19-24, 75-92, 141-155"
    confidence: high
    label: source_backed_summary
```

## migration_notes

```yaml
migration_notes:
  - "Preserve the package split as a core Apex workflow invariant."
  - "Represent handoff edges explicitly in Phase 2 wiki pages rather than burying them inside prose."
  - "Use the shared H1 status enum as a cross-package concept page."
  - "Treat registry writes as a special sync exception, not a general mutation permission."
```

## proposed_phase2_targets

```yaml
proposed_phase2_targets:
  summaries:
    - apex-plan-sync-session-workflow-summary
  concepts:
    - three-package-boundary
    - shared-h1-status-enum
    - qualitative-vs-exact-computation
    - read-side-sync-boundary
    - operator-gated-session-mutation
  entities:
    - apex-plan
    - apex-sync
    - apex-session
    - scripts-apex-sync-py
```

## operator_gate

```yaml
operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
```
