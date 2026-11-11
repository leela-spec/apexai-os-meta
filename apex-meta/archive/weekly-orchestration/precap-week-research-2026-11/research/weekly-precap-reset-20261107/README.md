---
type: handover-entrypoint
id: M01-PRECAP-RESET-README-20261107
title: Weekly Precap reset — start here
description: Entry point for reviewing the authoritative specifications, conversation artifacts and next project-planning/resource-planning phase.
status: ready_for_review
date: 2026-11-07
scope: [weekly_precap, handover, layered_project_overview]
---

# Weekly Precap reset — start here

## Active intent

- [P0 | I99] Build understanding around a layered project → epic/workstream → task → next-work overview, then guide the operator through planning the coming week.
- [P0 | I98] Validate individual project reality before using it as weekly planning input; distinguish native task records from accepted implementation evidence.
- [P0 | I97] Treat this packet as a review handover. No production specification, project record or calendar was changed by this handover task.

## Reading order

1. [HANDOVER.md](HANDOVER.md): the operator's intent, scope, source priority, drift conclusion and next-session walkthrough.
2. [SOURCE-FINDINGS.md](SOURCE-FINDINGS.md): exact locations and roles of the specifications, accepted corrections and evidence for the drift assessment.
3. [INDEX.md](INDEX.md): every file created in the task-owned conversation artifact locations, plus the modified source showroom. Each entry has a purpose and authority classification.
4. [ARTIFACT-MANIFEST.json](ARTIFACT-MANIFEST.json): machine-readable paths and classifications for the index.
5. [VERIFICATION.json](VERIFICATION.json): file existence, link coverage and source-evidence checks for this packet.

Repository copies of the externally saved screenshots, diagnostics and render helpers are linked in [workspace-artifacts/README.md](workspace-artifacts/README.md). The original index retains their originating workstation paths for provenance.

## Where the actual specifications are

| Need | File |
|---|---|
| Current PrecapWeek runtime owner and procedure | [PrecapWeek/SKILL.md](../../../../../../.claude/skills/PrecapWeek/SKILL.md) |
| Active Weekly Command Brief rendering template | [weekly-command-brief-template.md](../../../../../../.claude/skills/PrecapWeek/weekly-command-brief-template.md) |
| Matrix 1 versus Matrix 2 architectural specification | [SPEC-DUAL-VIEW-WEEKLY-PRECAP.md](../../SPEC-DUAL-VIEW-WEEKLY-PRECAP.md) |
| Accepted design decisions | [DESIGN-DECISIONS.md](../../DESIGN-DECISIONS.md) |
| Later corrections to project coverage, sequences, weekends and weekly/daily ownership | [Operator decision delta](../OPERATOR-DECISION-DELTA-Q06-Q08-Q09-Q12-Q13-20261106.okf.md) |
| Explicit layered project/epic/task model | [Matrix 1 assumption-first design](../../HANDOVER-MATRIX-1-DESIGN-ASSUMPTION-FIRST-20261106.okf.md) |
| Existing guided planning walkthrough | [Guided real-workflow handover](../../HANDOVER-MODULE-01-GUIDED-REAL-WORKFLOW-WALKTHROUGH.md) |

Runtime files describe what currently runs; some clauses still conflict with newer operator decisions. Read [the source findings](SOURCE-FINDINGS.md) before treating an older example as an active requirement. No single existing document reconciles all of those differences.

## What to do next

Walk one real project through current goal, epic, task readiness, dependencies and next useful output. Identify the missing data with the operator. Use that experience to define a reusable per-project planning input, then reconcile it with actual weekly capacity. Preserve one Weekly Command Brief and its compact daily handoff; do not create a second PM database or assume a new skill is needed.

The conversation's diagrams, Gantts, mock portfolios and exports remain reference material. Their existence and rendering checks do not establish an accepted weekly planning workflow. All artifact links remain available in the index; none were deleted or promoted to production by this task.

## Failure guards

- [P0 | I99] Do not start with another presentation rebuild before the operator can navigate project → epic → task → next work.
- [P0 | I98] Do not use illustrative priorities, dates or mock acceptance criteria as confirmed planning inputs.
- [P0 | I97] Do not implement the future project/resource planning phase without its own concrete scope and authorization.
