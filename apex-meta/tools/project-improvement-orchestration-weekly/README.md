# Weekly Orchestration Improvement Project

## Purpose

This folder is the durable coordination home for repairing the Apex Weekly Orchestration system without losing orientation across long or fresh AI chats.

It is **not** a second production orchestrator. The production system remains `.claude/skills/weekly-orchestrator/` plus its stage agents/skills. This project exists so a Master Orchestrator chat can understand, repair, verify, and progressively simplify that production system while keeping design intent, decisions, module boundaries, and test status durable in the repository.

## Core objective

Make the Weekly Orchestration loop simple, resilient, effective, repeatable, human-usable, and faithful to the previously verified operator-facing design.

The project succeeds when the real production loop can be started fresh, follows its encoded skills/contracts without relying on hidden chat context, produces the intended human-facing outputs, preserves only necessary machine/safety infrastructure, and passes fresh-session tests on the existing W34 example data.

## Start here

A Master Orchestrator chat should read, in this order:

1. `README.md`
2. `PROJECT-CHARTER.md`
3. `CURRENT-STATE.md`
4. `DECISIONS.md`
5. `PROCESS.md`
6. `ORCHESTRATOR-DEFINITION.md`
7. `CONTEXT-RESILIENCE.md`
8. the README of the currently active module only

Then read the production files referenced by that module. Do not load the entire project history by default.

## Project lifecycle

```text
MASTER ORCHESTRATOR CHAT
  -> understand / repair global orchestration spine
  -> produce bounded module handover

FRESH MODULE CHAT
  -> discuss one module/output with operator
  -> update real production skill/agent/template/contracts
  -> return implementation evidence

MASTER ORCHESTRATOR CHAT
  -> inspect actual changes
  -> verify against whole infrastructure
  -> reject or approve for runtime test

FRESH TEST CHAT
  -> invoke real production implementation
  -> use frozen W34/example inputs only
  -> no design explanation or hidden context

OPERATOR REVIEW
  -> fail: return to module
  -> pass: Master closes module and opens next module
```

## Macro files

- `PROJECT-CHARTER.md` — project capture, scope, acceptance and definition of done using Apex Plan concepts.
- `PROCESS.md` — macro/meso execution process for the whole improvement project.
- `ORCHESTRATOR-DEFINITION.md` — role, authority, boundaries and verification responsibilities of the Master Orchestrator chat.
- `CONTEXT-RESILIENCE.md` — token/context resilience and cross-chat handoff rules.
- `CURRENT-STATE.md` — single compact project-position record. Update after every meaningful phase/module transition.
- `DECISIONS.md` — durable operator decisions and unresolved architecture questions.
- `TEST-PROTOCOL.md` — fresh-session production testing rules.
- `ARCHIVE-POLICY.md` — how stale/replaced material is preserved without remaining active authority.

## Modules

| Order | Module | Purpose |
|---|---|---|
| 00 | `00-orchestration-spine/` | Repair the whole weekly loop: lifecycle, ownership, transactions, gates, state boundaries, AI/deterministic roles, stage relationships. |
| 01 | `01-weekly-command-brief/` | Weekly operator Q&A and Weekly Command Brief. |
| 02 | `02-next-day-brief/` | Next-day planning interaction and day-level overview. |
| 03 | `03-flow-execution-card/` | One human execution workspace per flow, with exactly three sprints for a full flow. |
| 04 | `04-sprint-prompts/` | Real materialized prompt assets linked from sprints. |
| 05 | `05-execution-evidence/` | Minimal truthful execution/skip evidence returned after work. |
| 06 | `06-flow-recap/` | Concise recap of actual results, decisions, blockers and candidate state changes. |
| 07 | `07-status-merge/` | Decide and encode what changes can apply automatically versus what requires operator review. |
| 08 | `08-project-status/` | Decide whether ProjectStatus remains, and if so reduce it to a useful projection of confirmed state. |

Module order is provisional after Module 00. The Master may change later module order when dependency analysis demonstrates a better sequence, but must record the reason in `DECISIONS.md`.

## Non-negotiable anti-drift rules

1. The production Weekly Orchestrator is the runtime control plane; this folder is the redesign project control surface.
2. Do not create a second runtime state model here.
3. Work from operator experience and validated examples backwards to minimum machinery.
4. No field, file, gate, stage, script, score, review or packet survives only because it already exists.
5. Every retained machine element needs a named consumer and concrete value/failure prevented.
6. Plan != evidence. Candidate != confirmed state.
7. Human-facing output is primary; machine payload is secondary and minimal.
8. A module is not complete because its files look correct. The Master must verify integration, then a fresh context must run the real production implementation.
9. Do not improve test prompts to rescue a bad implementation. Fix the implementation.
10. Replaced active material is archived according to `ARCHIVE-POLICY.md`, not left beside current authority as ambiguous stale guidance.
