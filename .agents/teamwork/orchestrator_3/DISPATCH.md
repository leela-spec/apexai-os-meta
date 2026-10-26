# Dispatch Assignment: Project Orchestrator

## Working Directory
`c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_3`

## Sentinel (Parent)
- Conversation ID: `0f13bb14-0c53-4202-b3ea-68102b58cb65`
- Report progress in `progress.md` and `BRIEFING.md`.
- On final completion, notify Sentinel via `send_message`.

## Authoritative Request
See `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (specifically the section `## 2026-10-21T16:45:38Z`).

## Core Target
Independently audit, stress-test, and validate the `v1.0` Finalization Dossier (`FinalizationDossier/00`–`06`), its architectural recommendations (`DEC-21`–`DEC-24`), and the finalized `v1.0` candidate, blueprint, and canonical library files against the 10-packet research corpus (`ResearchOfFile10/`).

Key deliverable:
`c:\GitDev\apexai-os-meta\apex-meta\informatics\Agent_Setup\NextIteration\v2-always-on-architecture\FinalizationDossier\07-teamwork-independent-validation.md`
and linking it from `FinalizationDossier/index.md`.

## Conformance & Acceptance Gates
1. Deterministic Validator Gate: `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` -> 0 errors.
2. Adversarial & Ownership Test Suite: `python -m pytest apex-meta/informatics/tests/ -q` -> 100% pass (196/196).
3. Independent Metric Reproduction: Exact line, word, character, repo-estimator, and `cl100k_base` BPE token counts recomputed and verified.
4. Strict Boundary: Zero changes to live root `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`.

## Execution Protocol
- Decompose task into milestones.
- Spawn specialized subagents (explorers, workers, reviewers, challengers, forensic auditors).
- Regularly update `progress.md` and `BRIEFING.md` in your workspace.
- Enforce strict single-writer boundaries for subagents under `.agents/teamwork/<agent_dir>/`.


## 2026-10-21T16:47:20Z
[Message] timestamp=2026-10-21T16:47:20Z sender=0f13bb14-0c53-4202-b3ea-68102b58cb65 priority=MESSAGE_PRIORITY_HIGH content=You are the Project Orchestrator for the v1.0 Finalization Dossier & Architecture Independent Audit and Validation.

Your assigned working directory is:
`c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_3`

Read your onboarding briefing and task instructions in:
`c:\GitDev\apexai-os-meta\.agents\teamwork\orchestrator_3\DISPATCH.md`
and the authoritative user request in:
`c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md` (section `## 2026-10-21T16:45:38Z`).

Parent / Sentinel conversation ID: `0f13bb14-0c53-4202-b3ea-68102b58cb65`.

Deliverables & Acceptance Criteria:
1. Conduct the independent audit across R1 (Research Critique & DEC-21..DEC-24), R2 (Byte-level & Token-metric verification of 3A/3B candidates & 03-BLUEPRINT-agents.md), R3 (Bidirectional traceability & cross-dependency audit across Plane 4 library suite), and R4 (Comprehensive validation report `FinalizationDossier/07-teamwork-independent-validation.md` linked in `FinalizationDossier/index.md`).
2. Run deterministic gates: `python apex-meta/scripts/okf_validator.py --target apex-meta/informatics` and `python -m pytest apex-meta/informatics/tests/ -q`.
3. Strictly preserve root `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` (zero live carrier modifications).
4. Maintain `progress.md` and `BRIEFING.md` in your working directory.
5. Notify Sentinel (`0f13bb14-0c53-4202-b3ea-68102b58cb65`) via `send_message` upon claiming completion.
