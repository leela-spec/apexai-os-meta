---
type: Research
title: "APEX baseline and authority conflicts"
description: "APEX baseline and authority conflicts for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# APEX baseline and authority conflicts

## Baseline to preserve

The supplied entry point describes operator-triggered Multi-Agent Orchestration, not a continuously active swarm.
Its seven definitions are four accountabilities and three specialist lanes. Their files do not automatically activate them.

| Component | Existing responsibility | Invocation | Integration consequence |
|---|---|---|---|
| Alfred | Intake, constraints, decision presentation, exact answer capture | Main conversation | Keep operator dialogue with the run controller |
| Meta Strategy | Direction options, leverage, timing, alignment | Bounded read-only worker | Returns options; cannot select for the operator |
| Meta Ops | Sequencing, packets, integration, backbone, closure | Same main conversation | Owns the durable run record |
| Meta Detective | Independent validity or alignment review | Fresh read-only invocation per lens | No authoring, fixing, or shared verdict context |
| Knowledge Bank | Provenance, custody, placement, retrieval | Bounded lane | Candidate output; approved KB lifecycle |
| Informatics Design | Terminology, structure, taxonomy, consistency | Bounded lane | Uses existing glossary and informatics standard |
| Prompts & Workflows | Reusable prompts, methods, workflow templates | Bounded lane | Instantiates existing packet shapes |
| Domain worker | One domain deliverable | Temporary worker | Scoped tools and explicit stop condition |

Evidence: [A01–A11](14-source-register.md#apex-source-register).

## Non-negotiable translation requirements

These are existing APEX requirements, not new vendor best practices.

1. Files remain the authority for plans, packets, verdicts, decisions, and continuation.
2. A role name never grants execution permission.
3. The three state axes remain separate: lifecycle, artifact authority, operator validation.
4. Consequential artifacts require independent review before operator-authorized application.
5. Candidate learning never silently becomes doctrine.
6. Plan proposes; Sync computes; Session records and applies confirmed changes.
7. Registry updates use the existing explicit non-dry-run path after preview and drift reporting.
8. Weekly Orchestrator remains separate and requires explicit cross-system handoff.

A completed OpenMausBot turn therefore does not mean an APEX artifact is verified.
An Allow button therefore does not automatically populate a valid APEX gate record.
A bot's memory therefore does not become the accepted decision log.

## Existing evidence is mixed, not absent

US-IDEA-01's frontmatter records a full pass after the operator gate and confirmed writes.
Its body retains an older gate-pending heading. The simulation index still says no story has run.
US-SEQ-01 explicitly records only a partial pass, with later work dependent on operator choices and a human pilot.

Research treatment: retain these contradictions in the evidence ledger. Do not silently edit historical records.
The first OpenMausBot pilot should replay a bounded idea workflow, not assume every user story is already adopted.
See [A13–A16](14-source-register.md#apex-source-register).

## Enforcement gap found in the current checker

The architecture and authority schema describe digest enforcement as an open implementation item.
A later gate workflow invokes scripts/orchestration_check.py, which now exists.
Inspection establishes a partial implementation, not complete enforcement of the declared authority model:

| Requirement | Inspected code | Remaining gap |
|---|---|---|
| Confirmation field exists and equals confirmed | Checked | Does not authenticate the human who authored it |
| Each declared input says verified | Checked | Trusts the declaration |
| Input file digest matches | Checked, CRLF normalized to LF | No recursive dependency closure |
| verification_ref resolves to independent passing review | Not checked by canon-write | Sidecar field is not actually resolved |
| Every criterion has supporting evidence and falsification | Verdict checker checks booleans | It does not prove evidence fidelity or complete criterion structure |
| Writes cannot bypass checker | A callable command exists | Arbitrary filesystem writes are not intercepted |

These findings derive from [A15](../../../scripts/orchestration_check.py), particularly check_verdict and check_canon_write.
The research does not change the checker or the canonical workflow.
Closing this gap is a P0 prerequisite for claiming mechanically enforced adoption.

## Later architecture must be reconciled

The September WF01–WF10 plans describe Hermes, Windows tasks, Docker Desktop, WSL, and several external services.
A later September 26 migration bundle reports that both stacks now run on one WSL2-native engine.
It reports Docker Desktop uninstalled, with separate databases in a shared PostgreSQL service.
This is a local recorded outcome, not a live infrastructure audit performed here.

The OpenProject consolidation handover introduces another boundary:
a single personal/professional root project, a five-account test ambition, and operator-designed taxonomy.
Lika is explicitly excluded from that initiative. OpenMausBot adoption does not reopen that decision.

Implication: preserve the July role contracts as the supplied baseline while treating September runtime plans as migration inputs.
This is a working research assumption, pending the operator's baseline answer.
Do not treat an old Windows/Alpine command as a current deployment instruction.
Evidence: [A18–A20](14-source-register.md#apex-source-register).

## Source-of-truth allocation to decide

| Data | Existing authority | Proposed OpenMausBot treatment |
|---|---|---|
| APEX role law and schemas | Repository files | Reference, not copied mutable memory |
| Run phase and accepted gates | File-backed packets | UI projects their status |
| OpenMausBot bot/profile/thread IDs | Product state | Record mapping in run receipts |
| Project/task state | APEX plus project-specific authority | Avoid a new competing task database |
| OpenProject work packages | Existing instance and its skill contract | Integrate only after identity and authority decisions |
| App preferences and credentials | Product/OS/provider storage | Keep outside research Git history |
| Domain evidence | Source-preserving repositories/services | Link through exact locators |

No bidirectional synchronization is assumed. Which system may author each field is an explicit integration decision.
