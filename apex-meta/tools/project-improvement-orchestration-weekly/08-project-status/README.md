# Module 08 — Project Status Projection

## Purpose

Decide whether a separate ProjectStatus artifact remains useful after the orchestration/state redesign, and if so make it a simple projection rather than quasi-independent state.

## Starting hypothesis

Canonical confirmed project/task state is truth. A ProjectStatus view may be valuable for human cross-project orientation, but it should be derived from confirmed truth and should not require artificial numeric translation merely to satisfy its own schema.

## Questions

- Who currently consumes ProjectStatus?
- Does Weekly Planning need it, or can it read canonical/planning context directly?
- Is a human portfolio projection still useful?
- Which fields are derived/redundant?
- Are priority/urgency numeric scores required by any real current consumer?
- Should the view be generated on demand instead of persisted after every mutation?

## Known current defect

Current W34 ProjectStatus is large, YAML-heavy and includes provisional numeric mappings that may add false precision.

## Post-Module-00 repair pass findings (2026-08-18)

A verification sweep found the live `.claude/skills/ProjectStatus/` package is more tangled than the defect above suggests. Recorded here as evidence for this module's keep/simplify/derive-on-demand/retire decision -- nothing below has been resolved, only documented and, where it was a live false-authority hazard, moved out of the active path.

**`ProjectStatus/SKILL.md` cannot load its own declared files.** Four `supporting_files` paths are broken: it declares `references/project-status-overview-contract.md`, `templates/current-project-status-overview-template.md`, `examples/starter-manual-test-overview.md`, and `references/ranking-and-validation-rules.md`, but the package is flat -- those subdirectories don't exist. This repair pass did not repoint them, because doing so means picking a winner among the divergent versions below, which is this module's call.

**The targets are divergent multiples, not exact duplicates or simple typos:**

| Declared target | Candidate | Bytes | MD5 |
|---|---|---|---|
| `templates/current-project-status-overview-template.md` | root `current-project-status-overview-template.md` | 1842 | e6e62377 |
| | root `project-status-overview-template.md` | 4797 | 5ba0185d |
| | (archived) `FirstIteration/current-project-status-overview-template.md` | 2928 | 69dea339 |
| `references/project-status-overview-contract.md` | root `project-status-overview-contract_v2_fixed.md` | 4850 | 527a7d34 |
| | (archived) `FirstIteration/project-status-overview-contract.md` | 9392 | ed5d98cb |
| `references/ranking-and-validation-rules.md` | root `ranking-and-validation-rules.md` | 7913 | 05ce5e43 |
| | (archived) `FirstIteration/ranking-and-validation-rules.md` | 10436 | e2281512 |

**A competing entrypoint claim existed inside the package.** `FirstIteration/project-status-overview_SKILL.md` opened with `# FILE: .claude/skills/project-status-overview/SKILL.md` -- a self-declared claim to be the package's entrypoint. `package-manifest.md` separately declares `entrypoint: project-status-overview_SKILL_v3.md`, a file that does not exist anywhere in the repo. Because the four broken pointers above would send a fresh agent searching, it could land in this stale folder and be misled by that claim.

**Archived, not deleted.** `FirstIteration/` and `FolderStructure/` (a second stale folder containing a partial `references/`+`templates/`+`examples/` build-out, never promoted or referenced by `SKILL.md`) were moved to `apex-meta/archive/weekly-orchestration/topology-pre-forked-skills-2026-08/ProjectStatus/` with `archive_metadata`, per operator instruction. Every divergent version above remains available there as evidence for this module's decision -- archiving only removed the live false-authority hazard; it did not choose a winner.

## Module work

Keep, simplify, derive-on-demand or retire the active ProjectStatus stage based on named-consumer evidence. Archive superseded active contracts according to project policy.

## Completion

Production decision/implementation -> Master verifies no state authority duplication -> fresh projection test if retained -> operator acceptance.
