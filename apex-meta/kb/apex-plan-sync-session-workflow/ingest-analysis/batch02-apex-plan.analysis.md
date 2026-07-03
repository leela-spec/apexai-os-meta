# Batch 02 — Apex Plan Ingest Analysis

## source_scope

```yaml
batch_focus: apex_plan_package
source_root: .claude/skills/apex-plan/
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
```

## source_grounded_claims

```yaml
claims:
  - id: P001
    text: "apex-plan produces an apex_plan_packet as a no-script, operator-gated project planning artifact."
    source: ".claude/skills/apex-plan/SKILL.md lines 13-18; .claude/skills/apex-plan/package-manifest.md lines 5-10"
    confidence: high
    label: source_backed_summary

  - id: P002
    text: "apex-plan owns project capture, work decomposition, dependency proposals, priority policy, urgency policy, and focus recommendation rationale."
    source: ".claude/skills/apex-plan/SKILL.md lines 26-33"
    confidence: high
    label: source_backed_summary

  - id: P003
    text: "apex-plan must not compute exact next tasks, traverse dependency graphs, scan blockers, rebuild registries, mutate status, update entities, write session logs, or create next-session context."
    source: ".claude/skills/apex-plan/SKILL.md lines 80-92; .claude/skills/apex-plan/package-manifest.md lines 74-83"
    confidence: high
    label: source_backed_summary

  - id: P004
    text: "The apex-plan output packet must contain metadata, project capture, epic record, proposed task records, dependency plan, priority/urgency/focus rationale, review flags, handoff requests, and an operator gate."
    source: ".claude/skills/apex-plan/SKILL.md lines 194-258"
    confidence: high
    label: source_backed_summary

  - id: P005
    text: "apex-plan treats depends_on as an integer array and preserves the rule that all dependencies must be done before a task is actionable, but it delegates exact validation to apex-sync."
    source: ".claude/skills/apex-plan/SKILL.md lines 57-60, 141-155"
    confidence: high
    label: source_backed_summary

  - id: P006
    text: "apex-plan may assign high, medium, or low priority qualitatively and explain due_date urgency qualitatively, while apex-sync owns exact scoring."
    source: ".claude/skills/apex-plan/SKILL.md lines 62-73, 151-155"
    confidence: high
    label: source_backed_summary
```

## concepts_extracted

```yaml
concepts:
  - slug: apex-plan-packet
    description: "Operator-review-only planning output with project capture, epic/task drafts, dependency proposals, review flags, and handoff requests."
  - slug: no-script-planning-boundary
    description: "apex-plan forbids bash, Python, exact computation, and durable writes."
  - slug: dependency-proposal-not-validation
    description: "apex-plan proposes depends_on relations but does not perform graph validation."
  - slug: qualitative-priority-and-urgency
    description: "apex-plan provides qualitative rationale; exact weights and ranking belong to apex-sync."
```

## entities_or_roles_extracted

```yaml
entities:
  - name: apex-plan
    role: planning_packet_author
  - name: references/task-record-contract.md
    role: canonical_task_field_contract_for_plan_outputs
  - name: references/decomposition-and-dependency-rules.md
    role: dependency_proposal_rules
  - name: references/priority-urgency-focus-policy.md
    role: qualitative_priority_urgency_focus_policy
  - name: templates/epic-template.md
    role: proposed_epic_record_template
  - name: templates/task-template.md
    role: proposed_task_record_template
```

## contradictions_or_tensions

```yaml
tensions:
  - id: P-T001
    text: "apex-plan needs enough project/task structure to draft useful records, but it must not cross into durable write behavior or exact computation."
    source: ".claude/skills/apex-plan/SKILL.md lines 141-155; .claude/skills/apex-plan/package-manifest.md lines 66-83"
    confidence: high
    label: source_backed_summary
```

## migration_notes

```yaml
migration_notes:
  - "Phase 2 should create a concept page for apex_plan_packet."
  - "Phase 2 should make apex-plan handoff requests visible as edges to apex-sync and apex-session."
  - "Do not treat apex-plan's durable path awareness as permission to write files."
  - "Support files should be read before a more detailed wiki page about task record schema."
```

## proposed_phase2_targets

```yaml
proposed_phase2_targets:
  summaries:
    - apex-plan-package-summary
  concepts:
    - apex-plan-packet
    - no-script-planning-boundary
    - dependency-proposal-not-validation
    - qualitative-priority-and-urgency
  entities:
    - apex-plan
    - task-record-contract
    - decomposition-and-dependency-rules
    - priority-urgency-focus-policy
```

## operator_gate

```yaml
operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
```
