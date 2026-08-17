# Module 01 Handover — Weekly Command Brief

Module 00 (forked-skill topology) is closed. This is the bounded starting context for Module 01 — read this, not the Module 00 migration history.

```yaml
module_handover:
  target: Weekly_Command_Brief

  global_runtime_invariant: >
    weekly-orchestrator dispatches PrecapWeek directly as an isolated forked
    Skill (execution: context: fork). PrecapWeek's primary_operator_output
    is already Weekly_Command_Brief (templates/weekly-command-brief-
    template.md) -- this is the active, required runtime output now, not
    merely a promoted file sitting beside a stale contract. The active
    project set derives from confirmed project context (no fixed five-
    project roster gate); numeric priority/urgency ratings are an optional
    aid, never a required schema field or approval gate. The downstream
    seed PrecapNextDay consumes is the Brief's own "Compact downstream
    handoff" block -- there is no separate duplicated machine seed artifact.

  owner: PrecapWeek (.claude/skills/PrecapWeek/SKILL.md)

  upstream: >
    confirmed Apex Session planning_feed + Apex Sync reports (or the
    compact current_project_status_overview when that's all that exists);
    operator weekly intent; calendar/capacity constraints when available;
    recent flow-recap packets / skip markers from the closing week.

  downstream: >
    PrecapNextDay consumes the Brief's compact downstream handoff block as
    its planning seed on week start.

  validated_design_sources:
    - apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml
    - .claude/skills/PrecapWeek/templates/weekly-command-brief-template.md (J02 -- already active, not a scaffold)

  active_files:
    - .claude/skills/PrecapWeek/SKILL.md
    - .claude/skills/PrecapWeek/weekly-command-brief-template.md
    - .claude/skills/PrecapWeek/weekly-blueprint-standard.md
    - .claude/skills/PrecapWeek/weekly-blueprint-meeting-example.md
    - .claude/skills/PrecapWeek/calendar-planning-guidance.md
    - .claude/skills/PrecapWeek/references/validation-checklist.md
    - .claude/skills/PrecapWeek/package-manifest.md
    - .claude/skills/weekly-orchestrator/references/roles/meta-strategy-doctrine.md (now a real PrecapWeek consumer, not orphaned)

  known_stale_files:
    - apex-meta/archive/weekly-orchestration/topology-pre-forked-skills-2026-08/PrecapWeek/weekly-plan-output-contract.md
      (the superseded schema-first output contract this replaced -- history only, per D007; do not resurrect it)
    - existing artifacts/weekly-plans/weekly_plan_packet-*.md files predate
      this migration and still show produced_by: apex-precap-week and the
      old schema shape -- historical evidence, not something to edit or a
      currently-valid template instance

  unresolved_module_questions:
    - exact Weekly Command Brief wording/section depth for each operator
      decision point -- Module 00 wired the template in; it deliberately
      did not refine its language or layout (that's this module's job)
    - whether the template's "Daily seed map" section should be populated
      by PrecapWeek itself or left entirely to PrecapNextDay
    - how much of weekly-blueprint-standard.md's default project-flow
      order should surface directly in the Brief's prose vs. stay internal
      planning reasoning

  test_fixture:
    - artifacts/weekly-plans/weekly_plan_packet-20260816-2026-W34.md
      (latest confirmed weekly plan -- produced under the OLD schema;
      useful as a before/after comparison, not a valid current-shape example)
    - artifacts/weekly-orchestrator-simulation/US-SEQ-01/J2-weekly-command-brief.md
      (simulation fixture already shaped like the target Brief)

  definition_of_done: >
    A fresh W34-equivalent weekly run produces a Weekly Command Brief (not
    the old precap_week_output shape) at the real production path; an
    operator can approve/edit/reject from it without needing machine-schema
    literacy; PrecapNextDay consumes its compact downstream handoff without
    requiring a separate duplicated seed artifact.
```
