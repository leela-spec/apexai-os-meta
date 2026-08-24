# MasterOfArts Source Migration Manifest

Status: **SOURCE INVENTORY / NO MOVE OR DELETE AUTHORIZED**  
Date: 2026-08-24

Purpose: identify the MasterOfArts files that formed the evidence/implementation basis of the Hermes architecture so a later executor can deliberately copy/re-home the **control-plane knowledge** into Apex AIOS Meta without moving project truth or losing provenance.

## A. Architecture and decision authority

Copy/re-home later as provenance/reference, preserving original paths in metadata:

- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/ADR-002-full-functional-hermes-target.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/state.yaml`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/QA-VALIDATION-RUNBOOK-v2.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/README.md`

Historical only; preserve provenance but do not make active authority:

- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/ADR-001-provisional-hermes-stack.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/QA-VALIDATION-RUNBOOK.md`

## B. Core research results that established the architecture

Preserve all seven final work results:

- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R01-HERMES-LOCAL-SAFETY-GUARDRAILS-WORK-RESULT.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R02-HERMES-MACRO-MESO-MICRO-PROJECT-KNOWLEDGE-WORK-RESULT.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R03-HERMES-QMD-REPO-INTEGRATION-WORK-RESULT.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R04-HERMES-PROJECT-KNOWLEDGE-LIFECYCLE-WORK-RESULT.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R05-HERMES-SPECIALIST-AGENT-AND-SKILL-PRIMING-WORK-RESULT.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R06-HERMES-CONTINUOUS-LEARNING-WORK-RESULT.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work/R07-MARKETINGSKILLS-HERMES-INTEGRATION-WORK-RESULT.md`

## C. Optional-stack research/provenance

Preserve final synthesis and audit because they justify what was *not* added:

- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work-stack-expansion/R08-ADVERSARIAL-EVIDENCE-AUDIT-RESULT.md`
- `Orchestration/decision-runs/2026-08-22-hermes-preinstall/research-results/chatgpt-work-stack-expansion/R09-SOPHISTICATED-V2-SYNTHESIS-RESULT.md`

Preserve candidate research when future reevaluation is needed:

- Agency Agents result
- Semantic Router result
- AnythingLLM result
- CrewAI result
- Superpowers result

Do not make deferred candidates part of the active v2 implementation by copying their research.

## D. Implementation runbooks and proven runtime evidence

These are especially important because they contain what actually worked on the Windows/WSL/Docker machine rather than only pre-install reasoning:

- `Orchestration/Implementation/Antigravity Executor Runbook — Hermes Master of Arts Installation.md`
- `Orchestration/Implementation/Hermes Installation Baseline — Windows + WSL2 + Docker.md`
- `Orchestration/Implementation/OKF-EXECUTION-OBSERVATIONS.yaml`
- `Orchestration/Implementation/MASTER_HANDOVER_AND_AUDIT_REPORT.md`
- `Orchestration/Implementation/AUTONOMOUS_LEARNINGS_SUMMARY.md`
- `Orchestration/Implementation/CODEX_HANDOVER_HERMES_ORCHESTRATION.md`
- `IMPLEMENTATION-ACCEPTANCE-REPORT.md`
- `CODEX_HANDOVER.md`

Also preserve `implementation-evidence/` phase evidence, especially:

- P03 Docker baseline;
- P07 Hermes Docker backend;
- P08 QMD integration;
- P09 Lika knowledge package;
- P10 Kanban/context;
- P11 BMAD;
- P12 MarketingSkills;
- P13 shared specialists;
- P14 autonomous learning;
- P15 end-to-end integration;
- P16 recovery.

## E. Context files that demonstrate the working knowledge model

Preserve as examples/reference, not global Apex truth:

- `AGENTS.md`
- `Lika/AGENTS.md`
- `IPOS/AGENTS.md`

These prove the macro/meso context pattern. Their project facts remain MasterOfArts-owned.

## F. Do NOT migrate into Apex as copied control-plane truth

Do not copy the following merely because Apex is the portfolio layer:

- all of `Lika/`, `IPOS/`, `ACIM/`, `Business/`, workshop content, websites or other MasterOfArts project content;
- generated project deliverables;
- QMD index databases/caches;
- Hermes `kanban.db`;
- Hermes profile memory files;
- Hermes sessions;
- OpenRouter/API credentials;
- Docker runtime state;
- duplicate repository checkouts.

The source repo continues to own those things.

## G. Later migration method

When an executor is authorized to re-home the architecture provenance:

1. read each source file completely;
2. preserve original path, original repo, original commit and date in a migration manifest;
3. copy architecture/research evidence into the v2 Apex epic or a dedicated evidence subtree;
4. convert only genuinely current cross-repo decisions into new Apex v2 ADRs;
5. do not silently turn old MasterOfArts-specific paths/config into multi-repo defaults;
6. do not delete the originals until the operator separately decides archive/migration policy;
7. verify links/authority after migration.

The target is **preserved evidence + new v2 authority**, not a bulk folder move.
