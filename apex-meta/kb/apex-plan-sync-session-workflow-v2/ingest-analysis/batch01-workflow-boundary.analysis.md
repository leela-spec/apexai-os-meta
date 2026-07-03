# Workflow Boundary

## source_scope

```yaml
source_scope:
  kb_slug: apex-plan-sync-session-workflow-v2
  batch: batch01-workflow-boundary
  purpose: "Cross-package boundary extraction for apex-plan, apex-sync, and apex-session."
  read_only_sources: true
  phase2_outputs_created: false
```

## source_files_read

```yaml
source_files_read:
  - ".claude/skills/apex-plan/SKILL.md"
  - ".claude/skills/apex-plan/package-manifest.md"
  - ".claude/skills/apex-sync/SKILL.md"
  - ".claude/skills/apex-sync/package-manifest.md"
  - ".claude/skills/apex-session/SKILL.md"
  - ".claude/skills/apex-session/package-manifest.md"
```

## source_grounded_claims

```yaml
claims:
  - claim:
      id: C001
      text: "apex-plan owns no-script operator-gated planning and produces an apex_plan_packet rather than durable state mutation."
      source: ".claude/skills/apex-plan/SKILL.md#Skill Contract lines 14-17; package-manifest.md#package_boundaries lines 66-83"
      confidence: high
      label: raw_source
  - claim:
      id: C002
      text: "apex-plan owns project capture, decomposition, dependency proposals, priority policy, urgency policy, and focus recommendation rationale."
      source: ".claude/skills/apex-plan/SKILL.md#Skill Contract/process_scope/owns lines 26-33"
      confidence: high
      label: raw_source
  - claim:
      id: C003
      text: "apex-plan hands exact computation, dependency graph traversal, blocker scan, registry rebuild, drift detection, and exact sorting to apex-sync."
      source: ".claude/skills/apex-plan/SKILL.md#hands_off_to_apex_sync lines 34-40"
      confidence: high
      label: raw_source
  - claim:
      id: C004
      text: "apex-plan hands status mutation, entity update, session progress, next-session context, and operator-confirmed writes to apex-session."
      source: ".claude/skills/apex-plan/SKILL.md#hands_off_to_apex_session lines 41-46"
      confidence: high
      label: raw_source
  - claim:
      id: C005
      text: "apex-sync owns deterministic read-side reports over task files and delegates exact computation to scripts/apex_sync.py."
      source: ".claude/skills/apex-sync/SKILL.md#Objective lines 18-23"
      confidence: high
      label: raw_source
  - claim:
      id: C006
      text: "apex-sync may write only apex-meta/registry/index.md, only through the registry subcommand, and only with explicit --dry-run false."
      source: ".claude/skills/apex-sync/SKILL.md#Objective lines 21-24; Canonical Command Policy lines 97-108"
      confidence: high
      label: raw_source
  - claim:
      id: C007
      text: "apex-session owns session artifacts, gated mutation records, state deltas, entity records, next-session context, and planning feed."
      source: ".claude/skills/apex-session/SKILL.md#Skill Contract/owns lines 29-36; Final Outputs lines 109-129"
      confidence: high
      label: raw_source
  - claim:
      id: C008
      text: "apex-session does not rank tasks, scan blockers, rebuild registries, compute scores, run scripts, or decompose new work."
      source: ".claude/skills/apex-session/SKILL.md#Objective lines 16-18; Validation Rules lines 250-264"
      confidence: high
      label: raw_source
  - claim:
      id: C009
      text: "Shared workflow logic is proposal to deterministic report/validation to gated session recording."
      source: ".claude/skills/apex-plan/SKILL.md#Procedure lines 153-155; .claude/skills/apex-sync/SKILL.md#Procedure lines 137-145; .claude/skills/apex-session/SKILL.md#Procedure lines 198-208"
      confidence: high
      label: source_backed_summary
  - claim:
      id: C010
      text: "If boundaries collapse, planning could mutate or compute exact rankings, sync could author narrative or validation claims, and session could perform scoring or drift computation."
      source: ".claude/skills/apex-plan/SKILL.md#boundaries lines 80-92; .claude/skills/apex-sync/SKILL.md#Procedure lines 120-145; .claude/skills/apex-session/SKILL.md#Validation Rules lines 250-264"
      confidence: high
      label: source_backed_summary
```

## concepts_extracted

```yaml
concepts_extracted:
  - operator-gated-planning
  - deterministic-read-side-synchronization
  - registry-write-exception
  - gated-mutation-record
  - h6-handoff-artifacts
  - package-boundary
  - handoff-edge
```

## entities_or_roles_extracted

```yaml
entities_or_roles_extracted:
  - entity: apex-plan
    role: "proposal/planning package"
  - entity: apex-sync
    role: "deterministic computation/report package"
  - entity: apex-session
    role: "session artifact and mutation-gate package"
  - entity: operator
    role: "review, confirmation, and validation authority"
  - entity: scripts/apex_sync.py
    role: "canonical deterministic sync script"
```

## contradictions_or_tensions

```yaml
contradictions_or_tensions:
  - id: T001
    text: "apex-plan defines durable paths and drafts epic/task records but forbids durable writes."
    source: ".claude/skills/apex-plan/SKILL.md lines 19-24, 145-155, 80-92"
    status: boundary_tension_not_contradiction
  - id: T002
    text: "apex-sync is read-side except for the registry write exception."
    source: ".claude/skills/apex-sync/SKILL.md lines 18-25 and 97-108"
    status: intentional_exception
  - id: T003
    text: "apex-session creates mutation records but requires operator validation before consequential mutations are confirmed."
    source: ".claude/skills/apex-session/SKILL.md lines 198-200 and 238-243"
    status: operator_gate
```

## migration_notes

```yaml
migration_notes:
  - "Model the lifecycle as plan proposes, sync computes/reports, session records/gates."
  - "Keep apex-plan outputs review packets only."
  - "Keep apex-sync report-oriented and dry-run-first."
  - "Keep apex-session evidence-preserving and mutation-gated."
```

## proposed_phase2_targets

```yaml
proposed_phase2_targets:
  summaries:
    - plan-sync-session-workflow-boundary
  concepts:
    - operator-gated-planning
    - deterministic-read-side-synchronization
    - registry-write-exception
    - gated-mutation-record
    - h6-handoff-artifacts
    - package-boundary
    - handoff-edge
  entities:
    - apex-plan
    - apex-sync
    - apex-session
    - scripts-apex-sync-py
    - operator
```

## operator_gate

```yaml
operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
```
