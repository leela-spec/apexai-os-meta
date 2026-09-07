# Task Assignment: Dual-Instance Architecture Implementation Worker

## Identity
- Role: Implementation Worker
- Working Directory: C:\GitDev\apexai-os-meta\.agents\worker_impl_1
- Parent Orchestrator: orchestrator_1 (ID: 96367b83-1fd0-4e20-8a61-cc9640b72e38)

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Mandatory Inputs to Read First
- `C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md`
- `C:\GitDev\apexai-os-meta\.agents\PROJECT.md`
- `C:\GitDev\apexai-os-meta\.agents\spec_miner_survey_1\spec_report.md`
- `C:\GitDev\apexai-os-meta\.agents\explorer_survey_2\codebase_survey.md`
- `C:\GitDev\apexai-os-meta\.agents\explorer_survey_3\infra_diagnostics.md`

## Concrete Scope & Deliverables
1. **Refactor `ki-basis/compose.yaml`**:
   - Parameterize container names (or remove static `container_name` so Docker Compose uses `${COMPOSE_PROJECT_NAME}-<service>`).
   - Parameterize top-level named volumes (use `name: ${COMPOSE_PROJECT_NAME:-ki-basis}-<volume_name>` or remove explicit static `name:` so project namespace prefixes automatically).
   - Parameterize network name `name: ${KI_NETWORK_NAME:-ki-basis-net}`.
   - Ensure all published host ports use variable substitution with defaults matching the Private port band:
     - Firefly: `127.0.0.1:${FIREFLY_HOST_PORT:-8086}:8080`
     - Paperless: `127.0.0.1:${PAPERLESS_HOST_PORT:-8010}:8000`
     - OpenProject: `127.0.0.1:${OPENPROJECT_HOST_PORT:-8082}:80`
     - Nginx: `127.0.0.1:${NGINX_HOST_PORT:-8084}:80`
     - Hermes Gateway: `127.0.0.1:${HERMES_GATEWAY_HOST_PORT:-8642}:8642`
     - Hermes Dashboard: `127.0.0.1:${HERMES_DASHBOARD_HOST_PORT:-9119}:9119`
   - Implement OpenProject crash loop fix & headless tuning:
     - `OPENPROJECT_WEB_WORKERS: "${OPENPROJECT_WEB_WORKERS:-1}"`
     - `PG_STARTUP_WAIT_TIME: "${PG_STARTUP_WAIT_TIME:-60}"`
     - `PAPERLESS_WORKERS: "${PAPERLESS_WORKERS:-1}"`
     - `PAPERLESS_TASK_WORKERS: "${PAPERLESS_TASK_WORKERS:-1}"`
     - Maintain 100% named volumes (zero 9P bind mounts for state).

2. **Generate Instance Environment Configurations**:
   - `ki-basis/.env.private`:
     - `COMPOSE_PROJECT_NAME=ki-basis-private`
     - `KI_NETWORK_NAME=ki-basis-private-net`
     - Port band 8080-8089 (8086, 8010, 8082, 8084, 8642, 9119)
     - Unique, high-entropy passwords and secret keys.
   - `ki-basis/.env.community`:
     - `COMPOSE_PROJECT_NAME=ki-basis-community`
     - `KI_NETWORK_NAME=ki-basis-community-net`
     - Port band 9080-9089 (9086, 9010, 9082, 9084, 9642, 9219)
     - Unique, high-entropy passwords and secret keys distinct from private.
   - Update `ki-basis/.env.example` documenting all dual-instance parameters.

3. **Deliver Architecture & Evaluation Document (R1, R2, R3)**:
   - Create `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md`:
     - R1: WSL2/ext4 vs 9P storage architecture, 350% CPU cause & cure, OpenProject exit status 1 root-cause analysis (POSIX locking, UID permissions, startup wait time, Puma memory limits), headless parameters.
     - R2: Dual-Instance Isolation Architecture (namespaces, bridge network isolation, non-overlapping port bands, storage segregation across 18 named volumes, database isolation).
     - R3: Multi-Engine vs Multi-Project Strategy Evaluation (detailed comparison of Strategy A: Dual Compose on Single Engine vs Strategy B: Dual Daemon Split, WSL2 `localhostForwarding` conflicts, memory/CPU overhead, and formal ADR).

4. **Deliver Migration & Operations Runbook**:
   - Create `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md`:
     - Complete step-by-step migration guide from single-instance to dual-instance without data loss.
     - Daily operations guide (CLI commands, starting, stopping, logging, status).
     - Backup and restore procedures for both instances.
     - Troubleshooting runbook (port conflicts, healthchecks, WSL2 issues).

5. **Operational Scripts & Automated Isolation Verification**:
   - Update/create `ki-basis/scripts/start-ki-basis.ps1` and `start-ki-basis.sh` to support `-Instance private|community|all`.
   - Create `ki-basis/scripts/verify_dual_isolation.py` to automatically validate:
     - Compose syntax and variable substitution.
     - Zero port overlap across stacks.
     - Zero shared volumes or networks.
     - Valid loopback bindings (127.0.0.1).
     - Ext4 named volume compliance.
   - Execute the verification script and document results.

## Output
Write your comprehensive implementation report to:
`C:\GitDev\apexai-os-meta\.agents\worker_impl_1\changes.md`
And write `handoff.md` with complete verification commands and results. Send a message to orchestrator_1 when finished.

## 2026-09-07T08:38:11Z
You are worker_impl_1. Your working directory is C:\GitDev\apexai-os-meta\.agents\worker_impl_1.
Read your instructions and the MANDATORY INTEGRITY WARNING in C:\GitDev\apexai-os-meta\.agents\worker_impl_1\DISPATCH.md.
Read C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md, PROJECT.md, and the survey reports from spec_miner_survey_1, explorer_survey_2, and explorer_survey_3.
Implement the dual-instance architecture for ki-basis:
1. Refactor compose.yaml (dynamic project namespaces, parameterized volume and network names, port variables, headless/OpenProject stability parameters).
2. Create .env.private, .env.community, and update .env.example.
3. Write C:\GitDev\apexai-os-meta\ki-basis\docs\DUAL_INSTANCE_ARCHITECTURE.md covering R1, R2, R3, and formal ADR.
4. Write C:\GitDev\apexai-os-meta\ki-basis\docs\DUAL_INSTANCE_RUNBOOK.md covering migration, daily ops, backups, and troubleshooting.
5. Update/create start-ki-basis.ps1 and start-ki-basis.sh with dual-instance flags.
6. Create and run C:\GitDev\apexai-os-meta\ki-basis\scripts\verify_dual_isolation.py to automatically verify zero port collision, zero shared volume/network, and ext4 compliance.
Document your changes in C:\GitDev\apexai-os-meta\.agents\worker_impl_1\changes.md and write your handoff to C:\GitDev\apexai-os-meta\.agents\worker_impl_1\handoff.md.
When finished, notify orchestrator_1 via send_message.
