# Batch 05 — Handoffs, Validation, and Phase 2 Targets

## source_scope

```yaml
batch_focus: cross_package_handoffs_validation_and_phase2_targets
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
  - id: H001
    text: "The intended handoff sequence is not a single linear automation pipeline; it is a bounded package workflow in which apex-plan proposes, apex-sync computes/validates, and apex-session records or packages confirmed state."
    source: ".claude/skills/apex-plan/SKILL.md lines 141-155; .claude/skills/apex-sync/SKILL.md lines 113-153; .claude/skills/apex-session/SKILL.md lines 188-210"
    confidence: high
    label: source_backed_summary

  - id: H002
    text: "apex-plan handoff requests to apex-sync include dependency validation, next action computation, blocker scan, registry rebuild, and focus candidate computation."
    source: ".claude/skills/apex-plan/SKILL.md lines 40-50"
    confidence: high
    label: raw_source

  - id: H003
    text: "apex-plan handoff requests to apex-session include status mutation, operator-confirmed write, and session handoff update."
    source: ".claude/skills/apex-plan/SKILL.md lines 40-50"
    confidence: high
    label: raw_source

  - id: H004
    text: "apex-sync routes away requests about project capture, decomposition, status mutation, handoff authoring, session narrative, operator validation, or planning-feed authoring."
    source: ".claude/skills/apex-sync/SKILL.md lines 120-123"
    confidence: high
    label: raw_source

  - id: H005
    text: "apex-session routes new decomposition to apex-plan and ranking/blocker/registry/drift/stale/score computation to apex-sync."
    source: ".claude/skills/apex-session/SKILL.md lines 188-190"
    confidence: high
    label: raw_source

  - id: H006
    text: "All three packages use completion gates to preserve their own boundaries: apex-plan requires review packet integrity, apex-sync requires exact script-report and dry-run/registry policy integrity, and apex-session requires mutation/handoff/source/boundary integrity."
    source: ".claude/skills/apex-plan/SKILL.md lines 60-69 of second fetch; .claude/skills/apex-sync/SKILL.md lines 195-210; .claude/skills/apex-session/SKILL.md lines 44-62 of second fetch"
    confidence: high
    label: source_backed_summary
```

## concepts_extracted

```yaml
concepts:
  - slug: proposal-computation-mutation-split
    description: "Planning proposes; sync computes and validates; session records and hands off confirmed state."
  - slug: bidirectional-routing-boundary
    description: "Each package knows when to route work to the others instead of absorbing scope."
  - slug: completion-gate-as-boundary-enforcement
    description: "Completion gates are not cosmetic; they are package-boundary enforcement surfaces."
  - slug: operator-reviewed-not-autonomous-workflow
    description: "The workflow has gates and handoffs rather than an autonomous chain of writes."
```

## entities_or_roles_extracted

```yaml
workflow_edges:
  - from: apex-plan
    to: apex-sync
    edge_type: handoff_request
    examples:
      - validate_dependencies
      - compute_next_action
      - scan_blockers
      - rebuild_registry
      - compute_focus_candidates
  - from: apex-plan
    to: apex-session
    edge_type: handoff_request
    examples:
      - request_status_mutation
      - request_operator_confirmed_write
      - request_session_handoff_update
  - from: apex-sync
    to: apex-plan
    edge_type: route_scope_away
    examples:
      - project_capture
      - decomposition
  - from: apex-sync
    to: apex-session
    edge_type: route_scope_away
    examples:
      - status_mutation
      - handoff_authoring
      - session_narrative
      - operator_validation
  - from: apex-session
    to: apex-plan
    edge_type: route_scope_away
    examples:
      - new_project_decomposition
  - from: apex-session
    to: apex-sync
    edge_type: route_scope_away
    examples:
      - ranking
      - blocker_scan
      - registry_rebuild
      - drift_detection
      - stale_detection
      - score_computation
```

## contradictions_or_tensions

```yaml
tensions:
  - id: H-T001
    text: "The workflow is likely to be misread as plan -> sync -> session automation, but the source files define gated handoffs and routing, not automatic mutation."
    source: ".claude/skills/apex-plan/SKILL.md lines 141-155; .claude/skills/apex-session/SKILL.md lines 196-210"
    confidence: medium
    label: working_hypothesis
  - id: H-T002
    text: "Registry rebuild appears in apex-plan handoff requests to sync, while apex-sync itself limits actual registry writing to an explicit non-dry-run command."
    source: ".claude/skills/apex-plan/SKILL.md lines 40-46; .claude/skills/apex-sync/SKILL.md lines 97-108"
    confidence: high
    label: source_backed_summary
```

## migration_notes

```yaml
migration_notes:
  - "Phase 2 should model workflow edges explicitly; this KB is valuable as a navigation graph, not only as summaries."
  - "Completion gates should become reusable concepts and not be flattened into generic validation prose."
  - "The Phase 2 wiki should include a compact workflow map with allowed and forbidden cross-package moves."
  - "Before detailed Phase 2 pages, read the reference files for each package to avoid over-relying on entrypoint summaries."
```

## proposed_phase2_targets

```yaml
proposed_phase2_targets:
  summaries:
    - apex-plan-sync-session-handoff-map
  concepts:
    - proposal-computation-mutation-split
    - bidirectional-routing-boundary
    - completion-gate-as-boundary-enforcement
    - operator-reviewed-not-autonomous-workflow
  entities:
    - apex-plan-to-apex-sync-handoff
    - apex-plan-to-apex-session-handoff
    - apex-sync-registry-write-exception
    - apex-session-h6-handoff
```

## operator_gate

```yaml
operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
```
