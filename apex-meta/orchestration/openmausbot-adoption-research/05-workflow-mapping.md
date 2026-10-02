---
type: Research
title: "Existing workflow integration"
description: "Existing workflow integration for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# Existing workflow integration

## Canonical ten-phase loop

This is a proposed runtime mapping of [A04](../workflows/orchestrator-run.md), not a replacement workflow.

| Phase | OpenMausBot use | Durable APEX output | Advancement condition |
|---|---|---|---|
| 1 Intake | Operator conversation | Intent/constraints packet | Objective and scope recorded |
| 2 Strategy | Bounded worker | Distinct option packet | Operator selects where required |
| 3 Plan | Controller invokes existing Plan procedure | Candidate dependency skeleton | No computed ranking invented |
| 4 Sync | Existing deterministic read-side command | Reproduction command and computed report | Inputs valid; failures visible |
| 5 Execute | Native worker or proven peer route | Candidate artifact per bounded packet | Stop condition reached |
| 6 Integrate | Controller | Integrated candidate and conflicts | No conflict silently absorbed |
| 7 Review | Two fresh blind reviewers | Lock, verdicts, deterministic outcome | Both required lenses pass |
| 8 Gate | Operator-facing conversation | Exact G-item answers and basis | No inferred confirmation |
| 9 Apply | Existing Session path | Before/after and mutation receipt | Current verified evidence plus confirmation |
| 10 Close | Controller | H6 files, state delta, candidate learning | Disk-only continuation possible |

The product's task state remains execution metadata.
APEX's lifecycle, authority, and operator_validation fields remain the governance record.

## Worked pilot: US-IDEA-01

Use one real operator-supplied idea with no public release, payment, or production service write.

1. Preserve the original wording in the intake artifact.
2. Record interpretation separately from the raw source.
3. Produce a candidate structured entry.
4. Ask Knowledge Bank for source-preserving placement advice.
5. Use Sync only if a project/task implication requires its reports.
6. Freeze the candidate and declared evidence.
7. Produce separate validity and alignment packets.
8. Run two actual fresh reviewers.
9. Route any defect to its creating owner.
10. Create a new version after correction.
11. Present durable placement and project creation as separate decisions.
12. Apply only the confirmed scope.
13. Read back the result and create continuation files.

This sequence comes from the existing story and simulation, including the distinction between preserving an idea and starting a project.
The first rehearsal should stop before a live canonical write.
A later real adoption run can perform that write after the established gate.
Evidence: [A12–A13](14-source-register.md#apex-source-register).

## Seven story migrations

| Story | First OpenMausBot use | Preserve | Hold before |
|---|---|---|---|
| US-IDEA-01 | Intake and custody pilot | Raw source, placement, optional null action | Canonical promotion or project creation |
| US-SEQ-01 | Strategy options and method packet | Operator thesis choice and actual pilot evidence | Pilot authorization and claimed results |
| US-MEDIA-01 | Parallel draft assets | Shared series constraints and consistency review | Public release |
| US-LEELA-01 | Use-case and backlog preparation | Human-led value and implementation gate | Coding batch execution |
| US-WORKSHOP-01 | Facilitator materials | Safety review and professional boundaries | Physical/child-facing pilot |
| US-OFFER-01 | Demand/offer evidence preparation | Demand validation before launch | Spend, demand test, publication |
| US-COMP-01 | Evidence register and exception queue | Qualified professional authority | External filing or compliance action |

These are integration designs. The research did not execute these stories inside OpenMausBot.

## Weekly Orchestrator stays separate

The existing weekly skill owns PrecapWeek, PrecapNextDay, evidence intake/normalization, FlowRecap, StatusMerge, and optional ProjectStatus.
It holds G1–G5 and routes approved durable changes through Session.
Its stage skills use isolated forks; its review pair uses independent subagents.

Proposed product mapping:

| Weekly stage | Product surface | Required preservation |
|---|---|---|
| PrecapWeek | Explicitly started weekly task | run_date, week_id, confirmed planning input, G1 |
| PrecapNextDay | Separate stage execution | Paths-only dispatch, G2 |
| Operator execution | Human/external surface | Actual evidence or explicit skip, G3 |
| Evidence normalization | Conditional worker | Source custody and missing-input flags |
| FlowRecap | Independent per-flow worker | Evidence-grounded recap, G4 |
| StatusMerge | Serialized integration task | Candidate changes, G5 |
| Session | Existing mutation owner | Confirmed application and planning feed |
| ProjectStatus | Derived optional view | No competing authoritative state |

An OpenMausBot schedule can remind or dispatch an authorized weekly stage.
It does not supply a missing gate answer.
An autonomous run without the operator leaves gates not_requested and holds canonical writes.
Evidence: [A17](../../../.claude/skills/weekly-orchestrator/SKILL.md), [S10–S11](14-source-register.md#s10).

## WF01–WF10 migration inventory

These later plans are first-party design inputs, not verified service capabilities.
Their product-specific claims were not adopted as official truth.

| Plan | Preserve as outcome | Proposed OpenMausBot responsibility | Required correction or verification |
|---|---|---|---|
| [WF01](../new_final_v4/workflow_plans/WF01_WEEKLY_META_ORCHESTRATION.md) | Cross-repository health and backup receipts | Dispatch read-only inspection; report evidence | Replace obsolete dual-engine assumptions; distinguish this sweep from Weekly Orchestrator |
| [WF02](../new_final_v4/workflow_plans/WF02_CREATIVE_WRITING_SYNTHESIS.md) | Cited creative synthesis | Bounded source worker and draft review | Verify actual source paths, profile semantics, publication gate |
| [WF03](../new_final_v4/workflow_plans/WF03_TRANSCENDENTS_WORKSHOP_CONCEPT.md) | Workshop curriculum | Packet routing to domain and structure specialists | Human review of content, pacing, venue, safety |
| [WF04](../new_final_v4/workflow_plans/WF04_MOA_BUSINESS_WEBSITE_PIPELINE.md) | Built variants and operator selection | Invoke existing builder; collect build and preview receipts | Verify current gateway and assets; no automatic publishing |
| [WF05](../new_final_v4/workflow_plans/WF05_IPOS_WEEKLY_MACRO_REGIME.md) | Deterministic macro pipeline | Dispatch existing computation; summarize exact outputs | Select one scheduler owner; preserve prohibition on broker execution |
| [WF06](../new_final_v4/workflow_plans/WF06_IPOS_EVIDENCE_CUSTODY_WATCHDOG.md) | Custody and thesis contradiction alerts | Read approved evidence interface; produce watch candidates | Dummy hash command does not test real ingestion or retrieval |
| [WF07](../new_final_v4/workflow_plans/WF07_COACHING_LIFECYCLE_INVOICING.md) | Draft invoices/reminders and reconciliation | Prepare reviewed service actions | Embedded credential-like literal must not be reused; legal claims need qualified review |
| [WF08](../new_final_v4/workflow_plans/WF08_EQUINOX_PRETIX_TICKETING.md) | Settlement evidence and community accounting | Route to scoped service worker | Old host assumption conflicts with migration; malformed command path; real payout reconciliation required |
| [WF09](../new_final_v4/workflow_plans/WF09_TELEGRAM_BOT_OFFLINE_INTAKE.md) | Durable intake and staged review | Consume approved intake bridge events | Help output is not an end-to-end delivery test; define deduplication and offset custody |
| [WF10](../new_final_v4/workflow_plans/WF10_ACIM_SECULAR_CROSS_REFERENCE.md) | Exact corpus citations and extraction | Bounded retrieval worker | Full-text matching does not alone prove semantic relevance; verify quotes against source |

The program text says sequential WF01 through WF10.
Its explicit schedule instead orders WF01, WF05, WF06, WF02, WF03, WF04, WF10, WF07, WF08, WF09.
Record this conflict before executing the portfolio. This research does not resolve it by silently choosing one.

## Cross-system handoff design

A reference to a result is not automatic activation of its receiver.
Each transfer records sender, receiving system, artifact version, expected action, stop condition, and required operator decision.

Examples:

- Weekly planning discovers a strategic ambiguity: produce a bounded Multi-Agent intake request.
- Multi-Agent work completes a reviewed deliverable: return a confirmed reference to weekly planning.
- OpenMausBot completes a worker task: persist its candidate return; do not update project status directly.
- OpenProject reports a changed work package: reconcile through its existing skill and APEX authority decisions.

## What should remain deterministic

Dependency checks, scores, file digests, status validation, receipt completeness, duplicate identifiers, and numeric domain calculations remain code-owned.
Models interpret ambiguity, propose options, and synthesize evidence.
They must not calculate authoritative investment scores, invent legal compliance, or infer service success from coherent text.
