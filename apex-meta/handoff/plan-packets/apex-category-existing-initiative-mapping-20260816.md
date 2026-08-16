---
title: "Apex Category — Existing Initiative Mapping"
document_role: portfolio_project_mapping_checkpoint
created: 2026-08-16
status: evidence_checked
category: Apex
canonical_mutation_performed: false
---

# Apex Category — Existing Initiative Mapping

## Operator inputs

- first weekly flow
- ApexKB alternatives or upgrade
- first Apex Plan/Sync and project management

## Mapping decision

### First weekly flow

Do **not** create a duplicate new epic.

Current owner initiative:

- `FEE2/00-WEEKLY-ORCHESTRATION-PILOT.okf.md`
- status: `static_readiness_pass_waiting_on_project_intake`
- next gate: `real_project_intake`

This conversation is currently supplying the missing portfolio/project-management intake and durable Plan packets needed to advance that pilot.

The FEE2 pilot is explicitly a control/iteration ledger and does not own project/task truth; project truth remains under canonical `apex-meta/epics/` after Session confirmation.

### First Apex Plan/Sync/Session project management

Do **not** create a duplicate new epic.

Current owner initiative/context:

- `apex-meta/handoff/weekly-cycle-project-management-infrastructure-handover-20260816.okf.md`
- current work in `apex-meta/handoff/plan-packets/`

This work establishes the first real portfolio records using:

- Apex Plan for proposals;
- Apex Session for operator-confirmed durable writes;
- Apex Sync for deterministic read-side validation/ranking;
- ProjectStatus as cross-project input to the weekly cycle.

Therefore this operator bullet is the **current infrastructure work itself**, not another project container.

### ApexKB alternatives or upgrade

Create a separate candidate epic:

- slug: `apex-kb-evolution`
- reason: it has an independent product-value decision and implementation path outside the weekly-orchestration pilot.

## Category structure

```yaml
Apex:
  existing_initiatives:
    first_weekly_flow:
      maps_to: FEE2 Weekly-Orchestration Pilot
      new_epic: false
    first_plan_sync_session_project_management:
      maps_to: Weekly-cycle project-management infrastructure
      new_epic: false

  new_candidate_epics:
    - apex-kb-evolution
```

## Continuation rule

Weekly ProjectStatus should reference these existing Apex initiatives by their current control artifacts rather than duplicate their status into a new task database.
