# BRIEFING — 2026-09-07T08:46:15Z

## Mission
Perform an independent, objective, and adversarial review of the operational procedures, migration runbook, daily ops, backup/restore, and lifecycle scripts for the dual-instance ki-basis architecture.

## 🔒 My Identity
- Archetype: reviewer-critic
- Roles: reviewer, critic
- Working directory: C:\GitDev\apexai-os-meta\.agents\reviewer_2
- Original parent: 96367b83-1fd0-4e20-8a61-cc9640b72e38
- Milestone: Review of operations, migration runbook, daily ops, backup/restore, and lifecycle scripts
- Instance: 1 of 1

## 🔒 Key Constraints
- Review-only — do NOT modify implementation code
- Integrity check: detect hardcoding, facade implementations, bypassed tasks, fabricated outputs
- Adversarial check: stress-test assumptions, failure modes, data-loss risks, edge cases

## Current Parent
- Conversation ID: 96367b83-1fd0-4e20-8a61-cc9640b72e38
- Updated: 2026-09-07T08:46:15Z

## Review Scope
- **Files to review**:
  - `C:\GitDev\apexai-os-meta\ki-basis\docs\DUAL_INSTANCE_RUNBOOK.md`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\start-ki-basis.ps1`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\start-ki-basis.sh`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\stop-ki-basis.ps1`
  - `C:\GitDev\apexai-os-meta\ki-basis\scripts\backup-stack.sh`
  - `C:\GitDev\apexai-os-meta\ki-basis\docker\nginx\default.conf`
  - Client scripts in `ki-basis/scripts/`
- **Interface contracts**: `C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md`, `C:\GitDev\apexai-os-meta\.agents\PROJECT.md`, `worker_impl_1` handoff
- **Review criteria**: correctness, migration safety, backup/restore validity, independent instance management, script execution/syntax, adversarial resilience

## Key Decisions Made
- Verdict determined: REQUEST_CHANGES based on 3 Critical and 4 Major findings.
- Found critical binary dump corruption via `docker exec -t`.
- Found restore failure mode (restoring full dump into existing DB, missing essential volumes).
- Identified untransformed `backup-stack.sh` presented as functional in runbook.
- Discovered blast-radius bug in `stop-ki-basis.ps1` killing host Docker Desktop during single-instance stop.
- Discovered Nginx default dashboard hardcoding Private ports for Community.
- Identified unparameterized client scripts violating milestone requirement F17.

## Artifact Index
- `C:\GitDev\apexai-os-meta\.agents\reviewer_2\DISPATCH.md` — task assignment
- `C:\GitDev\apexai-os-meta\.agents\reviewer_2\BRIEFING.md` — persistent memory
- `C:\GitDev\apexai-os-meta\.agents\reviewer_2\progress.md` — liveness heartbeat
- `C:\GitDev\apexai-os-meta\.agents\reviewer_2\review.md` — detailed quality and adversarial review
- `C:\GitDev\apexai-os-meta\.agents\reviewer_2\handoff.md` — 5-component handoff report

## Review Checklist
- **Items reviewed**:
  - `DUAL_INSTANCE_RUNBOOK.md`
  - `start-ki-basis.ps1`
  - `start-ki-basis.sh`
  - `stop-ki-basis.ps1`
  - `backup-stack.sh`
  - `docker/nginx/default.conf`
  - `populate_*.py`, `verify_*.py`, `invoke-hermes.ps1`
  - `verify_dual_isolation.py`
- **Verdict**: REQUEST_CHANGES
- **Unverified claims**: `backup-stack.sh` working for dual-instance (DISPROVEN - completely broken).

## Attack Surface
- **Hypotheses tested**:
  - `docker exec -t` with binary dumps -> FAILS (corrupts stream)
  - Restore procedure into existing DB -> FAILS (primary key / object collision)
  - Single stack shutdown via `stop-ki-basis.ps1 -Instance private` -> FAILS (kills Docker Desktop)
  - Community Nginx dashboard links -> FAILS (points to Private ports)
  - Client script execution against Community -> FAILS (hardcoded to Private ports)
- **Vulnerabilities found**: 3 Critical, 4 Major, 2 Minor findings.
- **Untested angles**: Live long-term container uptime under load.
