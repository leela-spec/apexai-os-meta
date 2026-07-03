# Workflow Boundary

## source_scope

Cross-package boundary review for apex-plan, apex-sync, and apex-session using only the three SKILL.md files and package manifests.

## source_files_read

- .claude/skills/apex-plan/SKILL.md
- .claude/skills/apex-plan/package-manifest.md
- .claude/skills/apex-sync/SKILL.md
- .claude/skills/apex-sync/package-manifest.md
- .claude/skills/apex-session/SKILL.md
- .claude/skills/apex-session/package-manifest.md

## source_grounded_claims

- apex-plan produces operator-gated planning packets and must not run scripts, compute exact next tasks, rebuild registries, or mutate state.
- apex-sync produces deterministic read-side synchronization reports through scripts/apex_sync.py and does not author planning or session narrative.
- apex-session produces final H6 handoff artifacts and gated mutation records, but does not rank tasks, scan blockers, rebuild registries, compute scores, or decompose new work.

## concepts_extracted

- operator gate
- handoff boundary
- read-side deterministic report
- gated mutation record
- planning packet
- H6 handoff artifact

## entities_or_roles_extracted

- apex-plan: planning packet owner
- apex-sync: deterministic synchronization report owner
- apex-session: session artifact and gated mutation owner
- operator: approval and validation authority

## contradictions_or_tensions

- apex-plan emits handoff requests but cannot write durable files.
- apex-sync may write only the registry through an explicit non-dry-run registry command.
- apex-session creates mutation records, but consequential mutations require operator validation before being treated as confirmed.

## migration_notes

Preserve workflow as a three-role lifecycle: plan proposes, sync computes read-side state, session records validated changes and next-session context.

## proposed_phase2_targets

- wiki/concepts/operator-gate.md
- wiki/concepts/handoff-boundary.md
- wiki/entities/apex-plan.md
- wiki/entities/apex-sync.md
- wiki/entities/apex-session.md

## operator_gate

operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
