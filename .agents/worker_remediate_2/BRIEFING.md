# BRIEFING — 2026-09-07T10:59:00Z

## Mission
Remediate all 10 operational, runbook, lifecycle, and script portability findings from reviewer_2 and challenger_1 for ki-basis dual-instance separation.

## 🔒 My Identity
- Archetype: worker_remediate_2
- Roles: implementer, qa, specialist
- Working directory: C:\GitDev\apexai-os-meta\.agents\worker_remediate_2
- Original parent: 96367b83-1fd0-4e20-8a61-cc9640b72e38 (orchestrator_1)
- Milestone: M4/Remediation Iteration 2

## 🔒 Key Constraints
- DO NOT CHEAT. All implementations must be genuine.
- Strict multi-tenant isolation between ki-basis-private and ki-basis-community.
- No pseudo-TTY (-t) on binary streams/dumps.
- Stopping a single instance must NEVER kill the host Docker engine.
- Client scripts must support environment variables and CLI parameters (F17).
- Verify all changes with verify_dual_isolation.py and test_adversarial_isolation.py.

## Current Parent
- Conversation ID: 96367b83-1fd0-4e20-8a61-cc9640b72e38
- Updated: 2026-09-07T10:59:00Z

## Task Summary
- **What to build**: Full remediation of 10 items across runbooks, backup scripts, stop scripts, start scripts, nginx templates, client integration scripts (F17), and test suites.
- **Success criteria**: All 10 review findings resolved, tests passing (32 in verify_dual_isolation, 21 in test_adversarial_isolation), zero regressions, full documentation.
- **Interface contracts**: PROJECT.md
- **Code layout**: ki-basis/

## Key Decisions Made
- Replaced `docker exec -t` with `docker exec -i` in all backup and migration runbooks to eliminate binary stream CRLF corruption.
- Hardened Disaster Recovery to clean PostgreSQL data volumes first and restored all 9 application state volumes (`paperless-data` and `hermes-workspaces` included).
- Upgraded `backup-stack.sh` to dynamically handle `private`, `community`, and `all` instances.
- Added explicit temporary PostgreSQL boot & `ALTER USER` commands to synchronize database passwords.
- Guarded Docker Desktop engine termination in `stop-ki-basis.ps1` with `-StopEngine` switch on `-Instance all` only.
- Created `stop-ki-basis.sh` for Linux/WSL2 and fixed timeout loop in `start-ki-basis.sh`.
- Remediated Nginx dashboard links using client-side port inspection and institutional badges.
- Parameterized all 6 client scripts with `argparse` and environment variables.
- Added security warning header to `ki-basis/.env`.

## Artifact Index
- DISPATCH.md — Task assignment and requirements
- BRIEFING.md — Situational awareness and working memory
- progress.md — Liveness heartbeat and task breakdown
- remediation_report.md — Comprehensive forensic remediation report
- handoff.md — 5-component hard handoff report

## Change Tracker
- **Files modified**:
  - `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md` (TTY fix, DR clean volume, password sync)
  - `ki-basis/scripts/backup-stack.sh` (Dual-instance upgrade, -i flag)
  - `ki-basis/scripts/stop-ki-basis.ps1` (Protected Docker Desktop engine)
  - `ki-basis/scripts/stop-ki-basis.sh` (Created symmetric Linux stop script)
  - `ki-basis/scripts/start-ki-basis.sh` (Fixed dynamic timeout loop)
  - `ki-basis/docker/nginx/default.conf` (Multi-instance dashboard links)
  - `ki-basis/docker/nginx/templates/default.conf.template` (Template for envsubst)
  - `ki-basis/scripts/populate_firefly.py` (CLI & env var parameterization)
  - `ki-basis/scripts/populate_openproject.py` (CLI & env var parameterization)
  - `ki-basis/scripts/populate_paperless.py` (CLI & env var parameterization)
  - `ki-basis/scripts/verify_fundraiser_stack.py` (CLI & env var parameterization)
  - `ki-basis/scripts/generate_euer_tax_report.py` (CLI & env var parameterization)
  - `ki-basis/scripts/invoke-hermes.ps1` (CLI & env var parameterization)
  - `ki-basis/.env` (Safety warning banner)
  - `ki-basis/tests/test_adversarial_isolation.py` (Remediation test & F17 verification suite)
- **Build status**: PASS (All tests green)
- **Pending issues**: None

## Quality Status
- **Build/test result**: 32/32 PASSED in verify_dual_isolation.py; 21/21 PASSED in test_adversarial_isolation.py.
- **Lint status**: Clean; shell syntax verified (`bash -n`), PowerShell syntax verified (AST).
- **Tests added/modified**: Added `TestClientScriptPortability` (7 tests) and updated `test_nginx_default_conf_multi_instance_support` in `test_adversarial_isolation.py`.

## Loaded Skills
- None
