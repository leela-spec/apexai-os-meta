# Apex Plan

## source_scope

```yaml
source_scope:
  kb_slug: apex-plan-sync-session-workflow-v2
  batch: batch02-apex-plan
  purpose: "Extract apex-plan purpose, apex_plan_packet shape, proposal scope, handoffs, and package boundary."
  phase2_outputs_created: false
```

## source_files_read

```yaml
source_files_read:
  - ".claude/skills/apex-plan/SKILL.md"
  - ".claude/skills/apex-plan/package-manifest.md"
```

## source_grounded_claims

```yaml
claims:
  - claim:
      id: C001
      text: "apex-plan is for project capture, epic/task planning, work decomposition, dependency proposal, priority and due-date rationale, and provisional focus recommendation."
      source: ".claude/skills/apex-plan/SKILL.md#frontmatter description lines 3-6"
      confidence: high
      label: raw_source
  - claim:
      id: C002
      text: "The primary apex-plan output is an apex_plan_packet for operator review."
      source: ".claude/skills/apex-plan/SKILL.md#Skill Contract lines 14-17; Output Requirements lines 196-200"
      confidence: high
      label: raw_source
  - claim:
      id: C003
      text: "The apex_plan_packet includes metadata, project capture, epic record, proposed task records, dependency plan, priority/urgency/focus rationale, review flags, handoff requests, and operator gate."
      source: ".claude/skills/apex-plan/SKILL.md#Output Requirements lines 201-210"
      confidence: high
      label: raw_source
  - claim:
      id: C004
      text: "apex-plan can draft proposed epic and task records and propose depends_on relationships, but it must keep them as review-packet content."
      source: ".claude/skills/apex-plan/SKILL.md#Procedure lines 145-152; Output Requirements lines 217-227"
      confidence: high
      label: source_backed_summary
  - claim:
      id: C005
      text: "apex-plan assigns qualitative priority, due_date urgency explanation, and provisional focus rationale; exact ranking belongs outside apex-plan."
      source: ".claude/skills/apex-plan/SKILL.md#priority_policy lines 62-69; urgency_policy lines 70-73; Output Requirements lines 228-231"
      confidence: high
      label: source_backed_summary
  - claim:
      id: C006
      text: "apex-plan hands exact next-task computation, dependency validation, blocker scan, registry rebuild, drift check, urgency score calculation, and focus-candidate computation to apex-sync."
      source: ".claude/skills/apex-plan/SKILL.md#hands_off_to_apex_sync lines 34-40; Output Requirements lines 233-239"
      confidence: high
      label: raw_source
  - claim:
      id: C007
      text: "apex-plan hands status mutation, entity update, session progress, next-session context, and confirmed durable-change requests to apex-session."
      source: ".claude/skills/apex-plan/SKILL.md#hands_off_to_apex_session lines 41-46; Output Requirements lines 240-244"
      confidence: high
      label: raw_source
  - claim:
      id: C008
      text: "apex-plan must not perform exact next-task computation, dependency traversal, blocker scan, registry rebuild, drift detection, exact sorting, status mutation, entity update, session progress log, next-session context, or operator-confirmed durable change."
      source: ".claude/skills/apex-plan/SKILL.md#boundaries lines 80-92; package-manifest.md#package_boundaries lines 74-83"
      confidence: high
      label: raw_source
```

## concepts_extracted

```yaml
concepts_extracted:
  - apex-plan-packet
  - project-capture-record
  - proposed-task-record
  - dependency-proposal
  - qualitative-priority-urgency-rationale
  - provisional-focus-recommendation
  - planning-handoff-request
```

## entities_or_roles_extracted

```yaml
entities_or_roles_extracted:
  - entity: apex-plan
    role: "operator-gated planning package"
  - entity: apex_plan_packet
    role: "primary planning review packet"
  - entity: apex-sync
    role: "exact-computation handoff recipient"
  - entity: apex-session
    role: "session-continuity handoff recipient"
  - entity: operator
    role: "review gate owner"
```

## contradictions_or_tensions

```yaml
contradictions_or_tensions:
  - id: T001
    text: "apex-plan drafts epic/task records for durable paths while its package boundary keeps the output as a review packet."
    source: ".claude/skills/apex-plan/SKILL.md lines 19-24, 145-149, 217-221"
    status: proposal_vs_durable_change_boundary
  - id: T002
    text: "apex-plan can reason about priority and focus, but exact scoring and sorting are routed to apex-sync."
    source: ".claude/skills/apex-plan/SKILL.md lines 62-73, 153-154, 228-239"
    status: qualitative_vs_exact_computation_boundary
```

## migration_notes

```yaml
migration_notes:
  - "Represent apex-plan as a proposal/review layer."
  - "Preserve apex_plan_packet as a central Phase 2 concept."
  - "Separate qualitative planning rationale from exact deterministic computation."
  - "Route confirmed session-continuity changes to apex-session."
```

## proposed_phase2_targets

```yaml
proposed_phase2_targets:
  summaries:
    - apex-plan-package-summary
  concepts:
    - apex-plan-packet
    - project-capture-record
    - proposed-task-record
    - dependency-proposal
    - qualitative-priority-urgency-rationale
    - planning-handoff-request
  entities:
    - apex-plan
    - apex_plan_packet
    - operator
```

## operator_gate

```yaml
operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
```
