---
title: "Leela Project Management Cleanup Checkpoint 01 — Authority Drift"
document_role: iterative_planning_checkpoint
created: 2026-08-16
status: evidence_checked
project: leela-project-management-cleanup
canonical_mutation_performed: false
---

# Leela Project Management Cleanup — Authority Drift Checkpoint

## Evidence inspected

Repositories:

- `leela-spec/leela@main`
  - `apex-meta/handoff/Leela_APEX_Orchestration_Control.okf.md`
  - `apex-meta/handoff/SpatialOpus_NextChat_Handover.okf.md`
- `leela-spec/Leela-Cloud-2026@master`
  - `AGENTS.md`
  - current `docs/ssot/` decision/orchestration conventions from prior Leela evidence work
- `leela-spec/apexai-os-meta@main`
  - current weekly-cycle project-management handover
  - current Leela Apex Plan packets/checkpoints created 2026-08-16

## Confirmed project-management layers

### 1. Product semantic truth

Current application repo `AGENTS.md` says authoritative product truth is `docs/ssot/`, with authority tiers and stable rule/decision IDs.

`docs/orchestration/` routes execution only; it must not re-own semantic truth.

### 2. Runtime execution orchestration

Current application repo requires:

- Macro program map;
- current Meso wave contract;
- exactly one active Micro packet;
- smallest sufficient context only;
- session outcomes recorded in `docs/data-architecture/STATE.md`;
- no new top-level HANDOVER/PLAN/RANKING files under `docs/orchestration/`;
- orchestration contract checks after packet edits.

### 3. Cross-portfolio Apex project management

Current weekly-cycle infrastructure uses `leela-spec/apexai-os-meta` for:

- Apex Plan proposal packets;
- eventual canonical `apex-meta/epics/<slug>/epic.md` and task records through Apex Session;
- Apex Sync deterministic read-side validation/ranking;
- cross-project weekly ProjectStatus/PreCap inputs.

### 4. Historical Leela-specific Apex handovers

`leela-spec/leela/apex-meta/handoff/` currently contains at least:

- `Leela_APEX_Orchestration_Control.okf.md`
- `SpatialOpus_NextChat_Handover.okf.md`

These were useful control artifacts for the prior Spatial Opus workflow, but they are no longer safe as universal restart authority without qualification.

## Confirmed drift examples

### Nowa status contradiction

Old Spatial Opus handover says:

- never structurally edit `@NowaGenerated` files;
- preserve Nowa-generated-code safety as a non-negotiable constraint.

Current application `AGENTS.md` says:

- Nowa retired 2026-07-25;
- annotations and old verification scripts are historical only;
- agents do not need to preserve or verify `@NowaGenerated()` markers for new/unrelated work.

Therefore the old handover contains stale execution constraints.

### Decision-state contradiction

Old Spatial Opus handover says OD-1 through OD-6 are OPEN and research-gated.

Current Leela decision system has since locked/applied multiple later design decisions (`SSOT-D-023` through `SSOT-D-029`), including spatial orientation, design alignment, macro answers, metallic construction, and Algorithm/Rhythm policies.

Therefore the handover's decision-state section is historical, not current truth.

### Orchestration-generation overlap

Old control/handover artifacts describe one browser project chat + worker chats + Work/Claude Code/Codex routing.

Current application repo has a later, narrower Macro/Meso/Micro execution protocol and explicitly prohibits new top-level orchestration handovers/plans.

Current weekly portfolio work adds another layer: centralized Apex project records feeding a cross-project weekly cycle.

These layers can coexist only if their scopes are explicit. Today old handovers read as restart authority even when parts are superseded.

## Cleanup principle

Do **not** delete product source, research, decision history, or old plans merely because they are old.

Decluttering should mean:

1. one current pointer for each kind of truth;
2. stale control artifacts clearly marked historical/superseded;
3. active plans/tasks stored in the current Apex project-management layer;
4. product truth remains in Leela SSOT;
5. runtime execution packets remain in the application repo's Macro/Meso/Micro protocol;
6. historical artifacts remain discoverable without being executable by default.

## Proposed target authority map

```yaml
authority_map:
  product_semantics:
    repo: leela-spec/Leela-Cloud-2026
    root: docs/ssot/

  runtime_increment_execution:
    repo: leela-spec/Leela-Cloud-2026
    root: docs/orchestration/context/
    rule: exactly_one_active_micro_packet

  cross_project_project_management:
    repo: leela-spec/apexai-os-meta
    root: apex-meta/epics/
    writers:
      proposal: Apex Plan
      confirmed_state: Apex Session
      deterministic_reads: Apex Sync

  planning_evidence_and_precanonical_packets:
    repo: leela-spec/apexai-os-meta
    root: apex-meta/handoff/plan-packets/

  historical_leela_control_artifacts:
    repo: leela-spec/leela
    current_root: apex-meta/handoff/
    target_rule: clearly_mark_historical_or_superseded; never implicit restart authority
```

## Next workstep

Create an Apex Plan packet for `leela-project-management-cleanup` centered on inventory/classification, authority pointers, stale-control retirement/annotation, and migration into the cross-portfolio Apex backbone. Do not delete files during planning.
