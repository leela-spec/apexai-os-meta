# Handoffs And Gates

## source_scope

Cross-cutting handoff and gate review from the three package entrypoints and manifests.

## source_files_read

- .claude/skills/apex-plan/SKILL.md
- .claude/skills/apex-plan/package-manifest.md
- .claude/skills/apex-sync/SKILL.md
- .claude/skills/apex-sync/package-manifest.md
- .claude/skills/apex-session/SKILL.md
- .claude/skills/apex-session/package-manifest.md

## source_grounded_claims

- apex-plan hands exact computation, blocker scans, registry rebuilds, and focus candidate computation to apex-sync.
- apex-plan hands status mutation, confirmed writes, and session handoff updates to apex-session.
- apex-sync must not validate operator decisions or author handoff files.
- apex-session must not perform planning decomposition or deterministic scoring.

## concepts_extracted

- package boundary
- operator review gate
- dry-run policy
- registry write exception
- consequential mutation confirmation
- raw source preservation

## entities_or_roles_extracted

- operator
- planning layer
- synchronization layer
- session layer
- registry

## contradictions_or_tensions

- Handoffs coordinate work across packages, but each package forbids expanding into adjacent responsibilities.
- apex-sync and apex-session both touch task state evidence; sync reports it, while session records validated changes.

## migration_notes

Phase 2 synthesis should model handoff edges explicitly so package pages do not collapse separate planning, computation, and mutation roles.

## proposed_phase2_targets

- wiki/concepts/package-boundary.md
- wiki/concepts/operator-review-gate.md
- wiki/concepts/dry-run-policy.md
- wiki/concepts/consequential-mutation-confirmation.md

## operator_gate

operator_gate:
  phase2_allowed: false
  required_phrase: approve ingest
  note: "Phase 1 analysis exists for operator review. Wiki synthesis is blocked until explicit approval."
