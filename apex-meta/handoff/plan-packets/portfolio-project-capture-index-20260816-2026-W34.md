---
title: "2026-W34 Portfolio Project Capture Index"
document_role: apex_plan_portfolio_index
created: 2026-08-16
status: proposal_set_ready_for_operator_gate
week: 2026-W34
canonical_project_mutation_performed: false
next_authority_after_approval: apex-session
---

# 2026-W34 Portfolio Project Capture Index

## Purpose

Provide one durable entry point for the first real full-portfolio Apex project intake. Future sessions must read this index before reconstructing portfolio state from chat history.

This index points to proposal packets only. It does not create or mutate canonical `apex-meta/epics/` state.

## Authority rule

```yaml
planning_authority:
  proposals: Apex Plan packets under apex-meta/handoff/plan-packets/
  confirmed_writes: Apex Session only after operator approval
  deterministic_validation: Apex Sync after canonical records exist
  weekly_direction: PreCap Week only after ProjectStatus/input readiness
```

## Portfolio

### Leela

#### New candidate epic — Leela Core Interaction Development

Current packet:

- `apex-meta/handoff/plan-packets/apex_plan_packet-20260816-leela-core-interaction-development-v2.md`

Supporting durable evidence:

- `leela-core-interaction-development-worklog-20260816.md`
- `leela-core-interaction-checkpoint-02-skill-tree-routing-20260816.md`
- `leela-core-interaction-checkpoint-03-home-skilltree-scope-slice-20260816.md`
- `leela-core-interaction-checkpoint-04-algorithm-resolution-seam-20260816.md`

Primary first milestone:

`Home -> bounded spatial Skill Tree -> confirmed ScopeSelection -> frozen ResolutionContext`

Key evidence-adjusted truth:

- Home already exists and must not be rebuilt from scratch.
- bounded spatial Skill Tree already exists but is effectively hidden behind `/skill-cluster` while normal navigation uses legacy `/skill-tree`.
- canonical `ScopeSelection` already exists.
- Packet-09 fingerprinted ResolutionRequest/ResolutionContext already exists but requires reconciliation with Skill Tree scope/Home narrowing and Path optionality.
- full candidate/ranking/DecisionTrace engine is not required for the first integration milestone.

Status: `operator_review_needed`.

#### New candidate epic — Close Leela Decisions and Questions

Packet:

- `apex-meta/handoff/plan-packets/apex_plan_packet-20260816-leela-product-decisions.md`

Evidence checkpoints:

- `leela-product-decisions-checkpoint-01-ledger-triage-20260816.md`
- `leela-product-decisions-checkpoint-02-resolution-profiles-20260816.md`
- `leela-product-decisions-checkpoint-03-home-override-persistence-20260816.md`
- `leela-product-decisions-checkpoint-04-spatial-accessibility-fallback-20260816.md`
- `leela-product-decisions-checkpoint-05-harmonization-ownership-20260816.md`

Key current decision state:

- ledger contains stale open rows; reconcile before asking operator broadly.
- QA-02/QA-11: real near-term operator choice remains.
- QA-100: real near-term operator choice remains.
- QA-138: broad policy remains but does not block bounded-cluster primary routing after accessibility verification.
- QA-73: evidence strongly supports migration-shell-not-feature and does not block first core interaction slice; formal ratification remains operator-owned.

Status: `operator_review_needed`.

#### New candidate epic — Leela Project Management Cleanup

Packet:

- `apex-meta/handoff/plan-packets/apex_plan_packet-20260816-leela-project-management-cleanup.md`

Checkpoint:

- `leela-project-management-cleanup-checkpoint-01-authority-drift-20260816.md`

Target authority map:

- product truth -> `Leela-Cloud-2026/docs/ssot/`
- runtime increment execution -> application Macro/Meso/sole Micro packet
- cross-project task/state -> central Apex `apex-meta/epics/`
- precanonical proposals -> this plan-packets directory
- old Leela/Spatial-Opus control handovers -> historical/superseded unless explicitly current

Status: `operator_review_needed`.

### MasterOfArts

Source reconnaissance:

- `apex-meta/handoff/plan-packets/masterofarts-checkpoint-01-source-reconnaissance-20260816.md`

#### New candidate epic — MasterOfArts Website Definition

Packet:

- `apex_plan_packet-20260816-masterofarts-website-definition.md`

Source state:

- current repo found, but no clearly identified current website-definition baseline by repository search.
- first task locates/establishes that baseline rather than inventing prior state.

Status: `operator_review_needed` with `source_baseline_missing` flag.

#### New candidate epic — TransenDance Concept

Packet:

- `apex_plan_packet-20260816-transendance-concept.md`

Target:

- concept core/experiential arc;
- module set;
- event timeline logic;
- facilitation/safety boundaries;
- assembled concept draft.

Preserved operator ingredients:

- psychology/meditation;
- breathing;
- intention;
- surrender;
- ecstatic dance;
- emotional release.

Unknown total event duration remains explicitly un-invented.

Status: `operator_review_needed`.

#### New candidate epic — Business Invoicing

Packet:

- `apex_plan_packet-20260816-business-invoicing.md`

Existing source authority:

- `leela-spec/MasterOfArts/Business/Invoices/`
- canonical invoice process/SSOT already exists.

Tasks:

- Martial Arts invoice;
- AkiiByte invoice;
- AI Consulting invoice;
- final numbering/archive consistency check.

No ranking or deadline invented.

Status: `operator_review_needed`.

### Apex

Existing initiative mapping:

- `apex-meta/handoff/plan-packets/apex-category-existing-initiative-mapping-20260816.md`

#### Existing initiative — First Weekly Flow

Maps to:

- `FEE2/00-WEEKLY-ORCHESTRATION-PILOT.okf.md`

Current FEE2 state:

- `static_readiness_pass_waiting_on_project_intake`
- next gate `real_project_intake`

No duplicate epic proposed.

#### Existing initiative — First Plan/Sync/Session Project Management

Maps to:

- `apex-meta/handoff/weekly-cycle-project-management-infrastructure-handover-20260816.okf.md`
- current portfolio capture work represented by this index and packets.

No duplicate epic proposed.

#### New candidate epic — ApexKB Alternatives or Upgrade

Packet:

- `apex_plan_packet-20260816-apex-kb-evolution.md`

Important prior evidence:

- mature source-preserving deterministic lifecycle exists;
- completed real KB run exists;
- prior audit records major residual value/operator/retrieval risks;
- project explicitly evaluates continue/freeze/replace/hybrid rather than presuming another custom upgrade.

Status: `operator_review_needed`.

### Investment

Checkpoint:

- `investment-intelligence-automation-checkpoint-01-source-reconnaissance-20260816.md`

#### New candidate epic — Investment Intelligence and Decision Automation

Packet:

- `apex_plan_packet-20260816-investment-intelligence-automation.md`

Three operator-equal workstreams:

1. scheduled video/information discovery using existing OpenClaw/Hermes Cron capability;
2. low-noise alerts;
3. portfolio/trading decision feedback automation.

No global ranking between workstreams is allowed.

No autonomous trade execution authority inferred.

Status: `operator_review_needed`; detailed search topics/alert rules/decision schema remain execution inputs.

### Residual

#### New candidate epic — Apartment Improvements

Packet:

- `apex_plan_packet-20260816-apartment-improvements.md`

Items:

- art;
- washing machine;
- plumbing.

Exact issues/outcomes are preserved as unknown; no ranking/deadline invented.

Status: `operator_review_needed`.

#### Weekly capacity only — Dating / Meeting Women

Packet:

- `weekly-capacity-input-2026-W34-residual-dating.md`

Rules:

- no epic;
- no task records;
- no todo fabrication;
- weekly plan should reserve meaningful time for getting dates/meeting women.

Status: `confirmed_operator_intent_non_task`.

## New candidate epic set

```yaml
new_candidate_epics:
  Leela:
    - leela-core-interaction-development
    - leela-product-decisions
    - leela-project-management-cleanup
  MasterOfArts:
    - masterofarts-website-definition
    - transendance-concept
    - business-invoicing
  Apex:
    - apex-kb-evolution
  Investment:
    - investment-intelligence-automation
  Residual:
    - apartment-improvements
```

Total new candidate epics: 9.

## Existing initiatives referenced, not duplicated

```yaml
existing_initiatives:
  - first-real-weekly-flow -> FEE2 Weekly-Orchestration Pilot
  - first-apex-plan-sync-session-project-management -> weekly-cycle project-management infrastructure
```

## Non-project weekly capacity

```yaml
capacity_inputs:
  - dating / meeting women -> Residual weekly time slot, no todo/task backlog
```

## Gate state

```yaml
portfolio_gate:
  stage: Apex Plan proposal set complete
  canonical_epic_task_writes: false
  recommended_gate_decision: approve_proposal_set_for_apex_session_handoff
  next_if_approved:
    - use Apex Session to create confirmed epic/task records
    - preserve each packet/source path in canonical task sources
    - then run Apex Sync deterministic validation
    - rebuild/validate registry only through Sync authority
    - create ProjectStatus overview
    - collect remaining week-specific inputs
    - run PreCap Week G1 and stop at G1 approval
```

## Stop conditions

Do not:

- create canonical epics/tasks from these packets without operator approval through the proper Session boundary;
- run Apex Sync as if proposal packets were canonical task records;
- run PreCap Week G1 yet;
- fabricate missing website sources, investment rules, apartment issue details, invoice fields, dates, dependencies, or priorities;
- turn dating into tasks;
- duplicate FEE2/current PM initiatives as new epics.

## Restart instruction

Future AI session:

1. read this index;
2. read only the packet(s) relevant to the current next stage;
3. for repo-specific execution, reread the current source repository rather than relying on packet summaries when implementation truth may have changed;
4. preserve proposal/canonical authority boundaries;
5. do not reconstruct portfolio state from chat memory.
