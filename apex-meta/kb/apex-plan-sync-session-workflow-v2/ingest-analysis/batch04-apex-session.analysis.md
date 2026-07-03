# Apex Session

## source_scope

```yaml
source_scope:
  kb_slug: apex-plan-sync-session-workflow-v2
  batch: batch04-apex-session
  purpose: "Extract apex-session task/session evidence handling, H6 artifacts, mutation gate, raw source preservation, planning feed, and non-computation boundary."
  phase2_outputs_created: false
```

## source_files_read

```yaml
source_files_read:
  - ".claude/skills/apex-session/SKILL.md"
  - ".claude/skills/apex-session/package-manifest.md"
```

## source_grounded_claims

```yaml
claims:
  - claim:
      id: C001
      text: "apex-session converts current task/session evidence into H6 handoff artifacts, gated mutation records, state deltas, entity update records, and next-session context."
      source: ".claude/skills/apex-session/SKILL.md#Objective lines 16-18"
      confidence: high
      label: raw_source
  - claim:
      id: C002
      text: "apex-session owns PM6_update_status, session progress writing, state delta extraction, entity maintenance, next-session context, operator validation for mutation, and planning-layer feed."
      source: ".claude/skills/apex-session/SKILL.md#Skill Contract/owns lines 29-36"
      confidence: high
      label: raw_source
  - claim:
      id: C003
      text: "The H6 handoff artifacts are task_plan.md, findings.md, progress.md, and next-session.md."
      source: ".claude/skills/apex-session/SKILL.md#Skill Contract/final_handoff_files lines 41-45; Final Outputs lines 124-128"
      confidence: high
      label: raw_source
  - claim:
      id: C004
      text: "Task evidence includes task_id, task_title, status_before, status_after, status_change_reason, depends_on, raw_source_ref, and raw_source_path."
      source: ".claude/skills/apex-session/SKILL.md#Accepted Inputs lines 73-84"
      confidence: high
      label: raw_source
  - claim:
      id: C005
      text: "Session evidence includes operator instructions, handoff notes, prior H6 files, raw sources, and unresolved context."
      source: ".claude/skills/apex-session/SKILL.md#Accepted Inputs lines 85-94"
      confidence: high
      label: raw_source
  - claim:
      id: C006
      text: "The mutation gate checks status_before and status_after against the H1 enum, creates mutation records and before-after previews, and requires operator_validation: confirmed before consequential mutations count as confirmed."
      source: ".claude/skills/apex-session/SKILL.md#Procedure lines 196-200; Validation Rules lines 216-243"
      confidence: high
      label: source_backed_summary
  - claim:
      id: C007
      text: "apex-session must preserve every available raw_source_ref and raw_source_path in relevant state delta, entity update, findings, or progress entries."
      source: ".claude/skills/apex-session/SKILL.md#Procedure line 194; Validation Rules lines 244-249"
      confidence: high
      label: raw_source
  - claim:
      id: C008
      text: "apex-session creates a planning_feed for the planning layer, but must not compute final rank or exact focus candidate."
      source: ".claude/skills/apex-session/SKILL.md#Procedure lines 206-208"
      confidence: high
      label: raw_source
  - claim:
      id: C009
      text: "next-session.md must contain exactly Current Step, Open Items, Risks, Decisions Made, and Next Actions."
      source: ".claude/skills/apex-session/SKILL.md#Procedure line 206; Validation Rules lines 225-237"
      confidence: high
      label: raw_source
  - claim:
      id: C010
      text: "apex-session must not compute exact ranking, dependency scoring, blocker scans, stale detection, registry rebuild, drift detection, priority score, urgency score, unlock depth, script execution, calendar operations, public web research, or new project decomposition."
      source: ".claude/skills/apex-session/SKILL.md#Validation Rules lines 250-264; package-manifest.md#forbidden_claims lines 319-333"
      confidence: high
      label: source_backed_summary
```

## concepts_extracted

```yaml
concepts_extracted:
  - h6-handoff-artifacts
  - status-mutation-record
  - before-after-preview
  - operator-validation-record
  - state-delta-summary
  - entity-update-record
  - planning-feed
  - raw-source-reference-preservation
```

## entities_or_roles_extracted

```yaml
entities_or_roles_extracted:
  - entity: apex-session
    role: "session artifact and gated mutation package"
  - entity: H6 handoff artifacts
    role: "task_plan.md, findings.md, progress.md, next-session.md"
  - entity: operator
    role: "validation authority for consequential mutations"
  - entity: planning layer
    role: "consumer of planning_feed"
  - entity: raw_source_ref and raw_source_path
    role: "preserved evidence references"
```

## contradictions_or_tensions

```yaml
contradictions_or_tensions:
  - id: T001
    text: "apex-session can create status mutation records, but consequential mutation confirmation is gated by operator_validation: confirmed."
    source: ".claude/skills/apex-session/SKILL.md lines 29-36 and 198-200"
    status: operator_gate
  - id: T002
    text: "apex-session can record unlock-depth context but cannot compute unlock depth."
    source: ".claude/skills/apex-session/SKILL.md lines 38-39 and 250-264"
    status: record_vs_compute_boundary
  - id: T003
    text: "apex-session feeds planning but cannot decompose new work or compute exact focus/ranking."
    source: ".claude/skills/apex-session/SKILL.md lines 206-208 and 250-264"
    status: planning_feed_vs_planning_computation_boundary
```

## migration_notes

```yaml
migration_notes:
  - "Represent apex-session as evidence-preserving handoff and mutation-gate layer."
  - "Preserve the exact H6 artifact list and exact next-session sections."
  - "Model operator validation as a hard gate for consequential mutations."
  - "Keep raw source reference preservation visible as a first-class concept."
```

## proposed_phase2_targets

```yaml
proposed_phase2_targets:
  summaries:
    - apex-session-package-summary
  concepts:
    - h6-handoff-artifacts
    - status-mutation-record
    - before-after-preview
    - operator-validation-record
    - state-delta-summary
    - entity-update-record
    - planning-feed
    - raw-source-reference-preservation
  entities:
    - apex-session
    - h6-handoff-artifacts
    - operator
```

## operator_gate

```yaml
operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
```
