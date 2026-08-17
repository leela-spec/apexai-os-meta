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

## Module work

Keep, simplify, derive-on-demand or retire the active ProjectStatus stage based on named-consumer evidence. Archive superseded active contracts according to project policy.

## Completion

Production decision/implementation -> Master verifies no state authority duplication -> fresh projection test if retained -> operator acceptance.
