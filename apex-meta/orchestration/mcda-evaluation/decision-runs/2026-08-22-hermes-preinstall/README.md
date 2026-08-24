# Hermes Pre-Install Decision Run

Status: **ACTIVE — HERMES ARCHITECTURE ACCEPTED / PRE-INSTALL VALIDATION**  
Architecture accepted: **2026-08-23**  
Implementation authorized: **NO**

## Current authority

Read in this order:

1. `ADR-002-full-functional-hermes-target.md` — current architecture/decision record.
2. `state.yaml` — machine-readable current state.
3. `QA-VALIDATION-RUNBOOK-v2.md` — interactive step-by-step execution process.
4. `research/` — separate decision-critical research specifications loaded only when their phase begins.

## Superseded active guidance

These files are retained as historical provenance but are no longer active instructions:

- `ADR-001-provisional-hermes-stack.md`
- `QA-VALIDATION-RUNBOOK.md`

The key correction is that the project is **not targeting a smaller/minimal/MVP architecture**. It is validating a complete end-to-end Hermes stack using existing upstream components and supported integrations. Custom replacement subsystems remain prohibited.

## Active target components

- Hermes Agent
- Hermes Kanban
- existing MasterOfArts project folders
- Hermes native hierarchical context
- BMAD
- MarketingSkills
- official Hermes/QMD integration
- Hermes memory/Curator
- verified model/provider path
- verified low-friction Hermes safety configuration

OpenClaw, Agency Agents, AnythingLLM, and Semantic Router are deferred to `Orchestration/future-development/OPENCLAW-ALTERNATIVE-EVALUATION.md`. The optional Agency Agents pre-install pilot was explicitly skipped on 2026-08-23.

## Research order

1. `research/R01-HERMES-LOCAL-SAFETY-GUARDRAILS.md`
2. `research/R02-HERMES-MACRO-MESO-MICRO-PROJECT-KNOWLEDGE.md`
3. `research/R03-HERMES-QMD-REPO-INTEGRATION.md`
4. `research/R04-HERMES-PROJECT-KNOWLEDGE-LIFECYCLE.md`
5. `research/R05-HERMES-SPECIALIST-AGENT-AND-SKILL-PRIMING.md`
6. `research/R06-HERMES-CONTINUOUS-LEARNING.md`
7. `research/R07-MARKETINGSKILLS-HERMES-INTEGRATION.md`
8. integrated user-story simulations in the v2 runbook
9. official installation blueprint
10. explicit CEO install/no-install decision

## Patch provenance

Exact-match patch instructions for mutable existing state files are stored under `Patches/`. New ADR/runbook versions are additive so historical decision records remain inspectable.
