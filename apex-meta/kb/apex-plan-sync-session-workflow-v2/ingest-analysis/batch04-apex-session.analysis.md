# Apex Session

## source_scope

apex-session SKILL.md and package manifest only.

## source_files_read

- .claude/skills/apex-session/SKILL.md
- .claude/skills/apex-session/package-manifest.md

## source_grounded_claims

- apex-session creates final H6 handoff artifacts, gated status mutation records, state deltas, entity update records, planning feed, and next-session context.
- It validates status movement against open, in-progress, blocked, done, and deferred.
- It preserves raw source references and unresolved context.
- It does not rank tasks, scan blockers, rebuild registries, compute scores, run scripts, or decompose new work.

## concepts_extracted

- status mutation record
- before-after preview
- operator validation record
- state delta summary
- entity update record
- next-session context

## entities_or_roles_extracted

- apex-session package
- operator
- H6 handoff artifacts
- planning feed

## contradictions_or_tensions

- apex-session may create mutation records, but records are not confirmed unless operator validation is confirmed.
- It can record unlock-depth context but cannot compute unlock depth.

## migration_notes

Represent apex-session as the evidence-preserving session and mutation-gate layer with exact H6 artifact expectations.

## proposed_phase2_targets

- wiki/entities/apex-session.md
- wiki/concepts/gated-mutation-record.md
- wiki/concepts/h6-handoff-artifact.md
- wiki/concepts/state-delta-summary.md

## operator_gate

operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
