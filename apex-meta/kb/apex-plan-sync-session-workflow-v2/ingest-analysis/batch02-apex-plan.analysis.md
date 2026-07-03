# Apex Plan

## source_scope

apex-plan SKILL.md and package manifest only.

## source_files_read

- .claude/skills/apex-plan/SKILL.md
- .claude/skills/apex-plan/package-manifest.md

## source_grounded_claims

- apex-plan captures project goals, scope, constraints, sources, and review flags.
- It drafts epic records and proposed task records for operator review without durable mutation.
- It proposes depends_on relationships and qualitative priority, due_date urgency, and focus rationale.
- It hands exact ranking and validation to apex-sync and confirmed writes or status mutation to apex-session.

## concepts_extracted

- apex_plan_packet
- project capture record
- proposed task record
- depends_on proposal
- qualitative priority rationale
- provisional focus recommendation

## entities_or_roles_extracted

- apex-plan package
- operator
- apex-sync handoff recipient
- apex-session handoff recipient

## contradictions_or_tensions

- The package references templates and supporting contracts for detailed task drafting, but this Phase 1 batch only read entrypoint and manifest files.
- It defines durable paths while also forbidding durable writes by apex-plan.

## migration_notes

Represent apex-plan as a proposal layer with explicit review flags and handoff requests, not as a state-changing executor.

## proposed_phase2_targets

- wiki/entities/apex-plan.md
- wiki/concepts/apex-plan-packet.md
- wiki/concepts/dependency-proposal.md
- wiki/concepts/qualitative-focus-rationale.md

## operator_gate

operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
