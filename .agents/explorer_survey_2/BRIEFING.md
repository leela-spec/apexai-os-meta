# BRIEFING — 2026-09-07T08:31:46Z

## Mission
Survey C:\GitDev\apexai-os-meta for all existing ki-basis files, docker-compose manifests, services, ports, volumes, networks, environment configs, and scripts.

## 🔒 My Identity
- Archetype: explorer
- Roles: Codebase & Service Explorer
- Working directory: C:\GitDev\apexai-os-meta\.agents\explorer_survey_2
- Original parent: 96367b83-1fd0-4e20-8a61-cc9640b72e38
- Milestone: M1 — Discovery & Codebase Survey

## 🔒 Key Constraints
- Read-only investigation — do NOT implement
- Write only to C:\GitDev\apexai-os-meta\.agents\explorer_survey_2
- Evidence-based findings citing exact file paths and line numbers
- Output full survey to codebase_survey.md and handoff report to handoff.md

## Current Parent
- Conversation ID: 96367b83-1fd0-4e20-8a61-cc9640b72e38
- Updated: 2026-09-07T08:31:46Z

## Investigation State
- **Explored paths**:
  - `ki-basis/compose.yaml`
  - `ki-basis/.env`, `.env.example`
  - `ki-basis/docker/` (`nginx/default.conf`, `postgres/init/01-init-databases.sh`)
  - `ki-basis/scripts/` (16 operational, verification, and seed scripts)
  - `ki-basis/fixtures/fundraiser_hamburg/` (13 fixtures)
  - `ki-basis/skills/equinox-intake/SKILL.md`
  - `ki-basis/AGENT-OPERATING-CONTEXT.md`, `CURRENT-STATE.md`, `SECURITY-GUIDANCE.md`, `STACK_ARCHITECTURE.md`, `AGENTS.md`, `SOUL.md`
  - `apex-meta/Alpine/` (`ARCHITEKTUR-BASIS.md`, `TARGET-ACCEPTANCE-REPORT.md`, `INTEGRATION-ACCEPTANCE-REPORT.md`, `HANDOVER-REVIEWER-DOSSIER.md`)
  - `apex-meta/Alpine/Iteration2/Performance_Problem.md`, `Maybe3rdIt/SoFarNotLean.md`, `ImplementationPlans/2026-09-03-ki-basis-finalization/`
- **Key findings**:
  - Identified all 7 services, 10 named volumes, 1 bridge network, and host port mappings.
  - Detected critical collision points preventing naive dual execution: static `container_name`, static top-level volume `name: ki-basis-*`, static network name, and colliding port bindings.
  - Discovered hardcoded port URLs in 6 client Python scripts, PowerShell scripts, and Nginx edge config.
  - Traced root causes of 350% CPU and OpenProject crash loops to WSL2 9P `/mnt/c` latency, Puma asset/PID locking, `PG_STARTUP_WAIT_TIME=30` timeouts, and unmanaged Puma/GoodJob concurrency under 2 GB VM ceiling.
- **Unexplored areas**: None for codebase survey; complete repo mapped.

## Key Decisions Made
- Documented complete architecture map, port table, volume inventory, script bindings, and crash mechanics in `codebase_survey.md`.
- Authored 5-component self-contained `handoff.md`.
- Evaluated Strategy A vs Strategy B tradeoffs based on memory pressure, `localhostForwarding` conflicts, and operational complexity.

## Artifact Index
- C:\GitDev\apexai-os-meta\.agents\explorer_survey_2\codebase_survey.md — Comprehensive survey report
- C:\GitDev\apexai-os-meta\.agents\explorer_survey_2\handoff.md — Self-contained 5-component handoff report
- C:\GitDev\apexai-os-meta\.agents\explorer_survey_2\progress.md — Liveness heartbeat and step tracking
