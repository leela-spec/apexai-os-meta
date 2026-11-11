---
okf_version: "0.2"
title: "Precap Week Modular Handovers — Forensic Baseline & Per-Part Execution Bundle"
description: "Bounded, self-contained EM-09 handover bundle dividing Precap Week repair, Command Brief separation, Stats, Operator Decisions, Matrix 1, Matrix 2/Residuals, Sequencing, and Macro convergence into isolated chats."
status: current
date: 2026-11-11
tags: [weekly-orchestration, precap-week, handovers, index, informatics, em-09]
---

# Precap Week Modular Handovers (`2026-11-11`)

This bundle is the clean handoff hub reconstructed from a full forensic audit across commits `7e4ed05c -> ec3e12f3` (`2026-11-06 .. 2026-11-11`), `.claude/skills/PrecapWeek/`, `01-weekly-command-brief/`, `02-weekly-dispersal/`, `00-orchestration-spine/`, and `DECISIONS.md` (`D001..D019`).

It prevents cross-module token overload by isolating **one part per chat**, paired with the canonical decision-lock governance rule so locked decisions update their single dominating owner immediately.

## Bundle Contents & Canonical Owner Map

| Order | Handover File | Scope / Module | Canonical Dominating Target File(s) |
|---|---|---|---|
| **00** | [00-RULE-CANONICAL-DECISION-LOCK.md](00-RULE-CANONICAL-DECISION-LOCK.md) | Decision-to-Owner governance rule (why sprawl happened + permanent fix) | `../CONTEXT-RESILIENCE.md`, `../../.claude` / carrier contract options |
| **01** | [01-HANDOVER-COMMAND-BRIEF-AND-INTAKE.md](01-HANDOVER-COMMAND-BRIEF-AND-INTAKE.md) | `Weekly Command Brief` (Operator Input) vs `PrecapWeek` Skill & Brief Boundary | `../../../.claude/skills/PrecapWeek/SKILL.md`, `references/validation-checklist.md` |
| **02** | [02-HANDOVER-STATS-COMPASS.md](02-HANDOVER-STATS-COMPASS.md) | Section `00 · Portfolio Compass` (5 Header KPIs, `OPERATOR_TODO`, T1 math fix) | `../01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md`, `HANDOVER-05` |
| **03** | [03-HANDOVER-OPERATOR-DECISIONS.md](03-HANDOVER-OPERATOR-DECISIONS.md) | Section `01 · Operator Decision Brief` (`New \| Ongoing \| Standard`, `G1` sign-off) | `../01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md`, `HANDOVER-04` |
| **04** | [04-HANDOVER-MATRIX-1.md](04-HANDOVER-MATRIX-1.md) | Section `02 · Matrix 1` (`L1/L2`, `G\|I\|P\|S\|O\|C`, `EM-13`, Live OP, `🔗` pills) | `../01-weekly-command-brief/SPEC-PRECAP-WEEK-ITERATIONS.okf.md`, `HANDOVER-03`, `HANDOVER-06` |
| **05** | [05-HANDOVER-MATRIX-2-AND-RESIDUALS.md](05-HANDOVER-MATRIX-2-AND-RESIDUALS.md) | Sections `03 · Matrix 2` (`week-blueprint.json`, `Mon-Sun`, `M\|P\|R`) & `04 · Residuals` | `../02-weekly-dispersal/week-blueprint.json`, `HANDOVER-02`, GCal spec |
| **06** | [06-HANDOVER-SEQUENCING.md](06-HANDOVER-SEQUENCING.md) | Section `05 · Sequencing` & Dispersal Engine (`epics.json`, `T2`, `T4`, `Q13`) | `MasterOfArts/Sequencing/dispersal/*` (mirror `../02-weekly-dispersal/*`) |
| **07** | [07-MACRO-RETURN-AND-ARCHIVE-MAP.md](07-MACRO-RETURN-AND-ARCHIVE-MAP.md) | End-to-End 4-Stage Loop convergence (`CB -> PrecapWeek -> RecapDay -> PrecapDay`) & Archive plan | `../../../.claude/skills/weekly-orchestrator/SKILL.md`, `../CURRENT-STATE.md` |

## Recommended Individual Chat Order

- **Step 0 (Approve Rule First):** Lock placement of `00-RULE-CANONICAL-DECISION-LOCK.md` so every module chat writes back cleanly.
- **Step 1 (Intake Boundary):** Run `01` (`Command Brief & PrecapWeek Spine`) so inputs, rosters, and offline fallbacks are unified.
- **Step 2 (Parallel UI/Contract Modules):** Run `02` (`Stats`), `03` (`Operator Decisions`), `04` (`Matrix 1`), `05` (`Matrix 2 + Residuals`), and `06` (`Sequencing / T2`) in separate chats.
- **Step 3 (Macro Convergence):** Run `07` (`Macro Return`) to patch `PrecapWeek/SKILL.md` + `weekly-command-brief-template.md`, retire superseded drafts via `git mv`, and wire the clean handoff into `Recap Day` and `Precap Day`.
