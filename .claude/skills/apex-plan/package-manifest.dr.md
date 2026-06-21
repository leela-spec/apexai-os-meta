# apex-plan Package Manifest

## Package Identity

- `name`: `apex-plan`
- `root`: `.claude/skills/apex-plan/`
- `entrypoint`: `.claude/skills/apex-plan/SKILL.md`
- `mode`: planning-only
- `status`: ready for review

## Package Scope

This package defines a Claude-native planning skill that:

- captures project or task intent
- clarifies operator intent
- decomposes work into epics and task candidates
- proposes `depends_on` relationships
- proposes provisional status using the approved enum
- suggests priority and urgency inputs
- prepares operator-gated planning packets

## Package Exclusions

This package does not:

- run scripts
- mutate state
- rebuild registries
- compute the exact next task
- scan blockers
- perform stale detection
- write handoff files
- own session mutation

## Canonical Path Assumptions

Preserve these paths:

- `apex-meta/`
- `apex-meta/harmonization/`
- `apex-meta/epics/`
- `apex-meta/handoff/`
- `apex-meta/registry/`
- `scripts/`
- `.claude/skills/`

## Required References

- `references/planning-contract.md`
- `references/task-decomposition-rules.md`
- `references/dependency-and-priority-rules.md`
- `references/operator-gate.md`
- `references/source-basis.md`

## Data Contract Summary

Task candidates produced by this skill should use:

- integer `id`
- allowed `status`
- integer-array `depends_on`
- `priority_label`
- `priority_score`
- `urgency_days`
- `evidence_basis`
- short `notes`

## Boundary Delegation

Downstream responsibilities:

- `apex-sync` handles exact next-task computation
- `apex-session` handles mutation, handoff continuity, and session-state responsibilities

This package must never claim those downstream actions already happened.

## Review Notes

Package reviewers should verify:

- planning-only boundary is preserved
- H1 status enum is unchanged
- H2 paths are unchanged
- H3 dependency rule is preserved
- H7 priority and urgency remain suggestions only
- substitute evidence is labeled correctly
- missing sources are not overstated

## File Inventory

- `.claude/skills/apex-plan/SKILL.md`
- `.claude/skills/apex-plan/references/planning-contract.md`
- `.claude/skills/apex-plan/references/task-decomposition-rules.md`
- `.claude/skills/apex-plan/references/dependency-and-priority-rules.md`
- `.claude/skills/apex-plan/references/operator-gate.md`
- `.claude/skills/apex-plan/references/source-basis.md`
- `.claude/skills/apex-plan/package-manifest.md`