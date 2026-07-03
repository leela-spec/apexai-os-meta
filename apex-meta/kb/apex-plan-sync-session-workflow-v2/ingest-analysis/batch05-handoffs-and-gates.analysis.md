# Handoffs and Gates

## source_scope

```yaml
source_scope:
  kb_slug: apex-plan-sync-session-workflow-v2
  batch: batch05-handoffs-and-gates
  purpose: "Extract handoff edges, review gates, shared checks, and Phase 2 targets across apex-plan, apex-sync, and apex-session."
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
      text: "The apex-plan to apex-sync handoff covers exact next-task computation, dependency validation, blocker review, registry refresh, drift review, exact sorting, urgency scoring, and focus-candidate computation."
      source: ".claude/skills/apex-plan/SKILL.md#hands_off_to_apex_sync lines 34-40; Output Requirements lines 233-239"
      confidence: high
      label: source_backed_summary
  - claim:
      id: C002
      text: "The apex-plan to apex-session handoff covers status change records, entity updates, session progress, next-session context, durable task updates, progress capture, findings capture, and confirmed durable-change requests."
      source: ".claude/skills/apex-plan/SKILL.md#hands_off_to_apex_session lines 41-46; Output Requirements lines 240-244"
      confidence: high
      label: source_backed_summary
  - claim:
      id: C003
      text: "apex-session routes new decomposition to apex-plan and routes ranking, blocker review, registry refresh, drift review, stale review, or score computation to apex-sync."
      source: ".claude/skills/apex-session/SKILL.md#Procedure lines 190-191"
      confidence: high
      label: raw_source
  - claim:
      id: C004
      text: "apex-sync routes project capture, decomposition, status changes, handoff authoring, session narrative, operator validation, and planning-feed authoring away from apex-sync."
      source: ".claude/skills/apex-sync/SKILL.md#Procedure lines 120-123 and 143-145"
      confidence: high
      label: raw_source
  - claim:
      id: C005
      text: "The apex-plan operator gate requires review before handoff into state/session change work."
      source: ".claude/skills/apex-plan/SKILL.md#Output Requirements/operator_gate lines 245-250"
      confidence: high
      label: source_backed_summary
  - claim:
      id: C006
      text: "The apex-sync dry-run default and registry exception constrain deterministic output behavior."
      source: ".claude/skills/apex-sync/SKILL.md#Canonical Command Policy lines 97-108; Procedure lines 137-145"
      confidence: high
      label: source_backed_summary
  - claim:
      id: C007
      text: "The apex-session confirmation gate prevents consequential status change records from being treated as confirmed without operator_validation: confirmed."
      source: ".claude/skills/apex-session/SKILL.md#Procedure lines 198-200; Validation Rules lines 238-243"
      confidence: high
      label: raw_source
  - claim:
      id: C008
      text: "H1 status values recur across plan, sync, and session; the package split is proposal, deterministic validation, and confirmation validation."
      source: ".claude/skills/apex-plan/SKILL.md lines 48-55; .claude/skills/apex-sync/SKILL.md lines 157-162; .claude/skills/apex-session/SKILL.md lines 216-223"
      confidence: high
      label: source_backed_summary
  - claim:
      id: C009
      text: "depends_on appears as a shared dependency field in planning and synchronization, while session preserves it as task evidence."
      source: ".claude/skills/apex-plan/SKILL.md lines 57-60; .claude/skills/apex-sync/SKILL.md lines 163-169; .claude/skills/apex-session/SKILL.md lines 75-83"
      confidence: high
      label: source_backed_summary
```

## concepts_extracted

```yaml
concepts_extracted:
  - handoff-edge
  - operator-review-gate
  - dry-run-default
  - registry-exception
  - confirmation-gate
  - raw-source-preservation
  - status-enum-validation
  - depends-on-validation
  - h6-handoff-artifacts
  - apex-plan-packet
```

## entities_or_roles_extracted

```yaml
entities_or_roles_extracted:
  - entity: apex-plan
    role: "handoff origin for exact computation and session-continuity requests"
  - entity: apex-sync
    role: "handoff recipient for deterministic reports"
  - entity: apex-session
    role: "handoff recipient for session continuity and router back to plan/sync"
  - entity: operator
    role: "approval authority across planning and confirmation gates"
  - entity: apex-meta/registry/index.md
    role: "narrow registry exception target"
  - entity: H6 handoff artifacts
    role: "final session continuity artifacts"
```

## contradictions_or_tensions

```yaml
contradictions_or_tensions:
  - id: T001
    text: "Handoffs require coordination, but each package forbids doing adjacent package work."
    source: ".claude/skills/apex-plan/SKILL.md lines 34-46 and 80-92; .claude/skills/apex-sync/SKILL.md lines 120-145; .claude/skills/apex-session/SKILL.md lines 250-264"
    status: coordination_boundary
  - id: T002
    text: "apex-sync and apex-session both inspect task evidence, but sync returns deterministic reports while session records validated handoff state."
    source: ".claude/skills/apex-sync/SKILL.md lines 18-25; .claude/skills/apex-session/SKILL.md lines 18-20"
    status: evidence_role_split
```

## migration_notes

```yaml
migration_notes:
  - "Create Phase 2 pages that keep handoff edges directional."
  - "Represent gates as separate concepts because they constrain transitions at multiple points."
  - "Keep status validation, dependency validation, and confirmation validation distinct."
  - "Entity pages should expose owns and does-not-own boundaries."
```

## proposed_phase2_targets

```yaml
proposed_phase2_targets:
  summaries:
    - handoffs-and-gates-summary
    - plan-sync-session-workflow-boundary
  concepts:
    - handoff-edge
    - operator-review-gate
    - dry-run-default
    - registry-exception
    - confirmation-gate
    - raw-source-preservation
    - status-enum-validation
    - depends-on-validation
    - h6-handoff-artifacts
    - apex-plan-packet
  entities:
    - apex-plan
    - apex-sync
    - apex-session
    - scripts-apex-sync-py
    - operator
    - apex-meta-registry-index-md
```

## operator_gate

```yaml
operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
```
