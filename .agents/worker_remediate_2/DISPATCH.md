# Task Assignment: Remediation Worker (Iteration 2)

## Identity
- Role: Remediation Worker
- Working Directory: C:\GitDev\apexai-os-meta\.agents\worker_remediate_2
- Parent Orchestrator: orchestrator_1 (ID: 96367b83-1fd0-4e20-8a61-cc9640b72e38)

## Mandatory Integrity Warning
DO NOT CHEAT. All implementations must be genuine. DO NOT hardcode test results, create dummy/facade implementations, or circumvent the intended task. A teamwork_preview_auditor will independently verify your work. Integrity violations WILL be detected and your work WILL be rejected.

## Mandatory Inputs to Read First
- `C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md`
- `C:\GitDev\apexai-os-meta\.agents\PROJECT.md`
- `C:\GitDev\apexai-os-meta\.agents\reviewer_2\review.md`
- `C:\GitDev\apexai-os-meta\.agents\reviewer_2\handoff.md`
- `C:\GitDev\apexai-os-meta\.agents\challenger_1\handoff.md`

## Concrete Remediation Tasks
You must address all feedback from Reviewer 2 and Challenger 1:

1. **Fix Binary Dump TTY CRLF Corruption in `DUAL_INSTANCE_RUNBOOK.md`**:
   - Remove `-t` flag from all `docker exec` commands that output binary/archive streams (such as `pg_dump -Fc`, `pg_dumpall`, and tar pipelines). Use `docker exec -i` only. Explain in the runbook that pseudo-TTY allocation converts `\n` to `\r\n` and injects terminal control sequences, causing fatal archive corruption in `pg_restore`.
2. **Fix Disaster Recovery Procedure in `DUAL_INSTANCE_RUNBOOK.md`**:
   - In Section 4.3 (Disaster Recovery), make sure the PostgreSQL cluster is completely clean (fresh/empty named volume) before restoring `postgres_all.sql`, preventing duplicate key/table collision errors.
   - Add the missing named volumes (`paperless-data` and `hermes-workspaces`) to the volume restore table/commands.
3. **Upgrade `ki-basis/scripts/backup-stack.sh` for Dual-Instance**:
   - Update `backup-stack.sh` to support an instance parameter (`private`, `community`, or `all`).
   - Dynamically namespace container names (e.g. `${PROJECT_NAME}-postgres`, `${PROJECT_NAME}-valkey`) and volume names (`${PROJECT_NAME}-*`).
   - Use `docker exec -i` (strictly no `-t`) for all database dumps.
4. **Fix Migration Runbook Password Sync (Section 2.1)**:
   - In `DUAL_INSTANCE_RUNBOOK.md`, document that when cloning `ki-basis-postgres-data` to `ki-basis-community-postgres-data`, the existing passwords inside the database remain unchanged. Provide the explicit SQL commands (`ALTER USER openproject_app WITH PASSWORD '...';`, etc.) to sync passwords with `.env.community` so community services authenticate successfully.
5. **Protect Docker Desktop Daemon in `ki-basis/scripts/stop-ki-basis.ps1`**:
   - Ensure stopping a single instance (`-Instance private` or `-Instance community`) NEVER terminates the host Docker Desktop engine!
   - Only terminate Docker Desktop when `-Instance all` is specified AND an explicit `-StopEngine` switch is passed by the operator.
6. **Create Symmetric `ki-basis/scripts/stop-ki-basis.sh`**:
   - Create a Linux/WSL2 shutdown script `stop-ki-basis.sh` supporting `-Instance private|community|all`.
7. **Fix Timeout Handling in `ki-basis/scripts/start-ki-basis.sh`**:
   - Ensure the `-t TIMEOUT` option actually configures the retry wait loop rather than using a hardcoded 15-iteration limit.
8. **Fix Nginx Landing Page Dashboard Links**:
   - Update `ki-basis/docker/nginx/default.conf` or document dynamic reverse proxy routing so Community operators on `:9084` are not redirected to Private ports (`:8086`, `:8010`, `:8082`, `:8642`).
9. **Implement Feature F17: Client Script Parameterization**:
   - Refactor client scripts (`populate_firefly.py`, `populate_openproject.py`, `populate_paperless.py`, `verify_fundraiser_stack.py`, `generate_euer_tax_report.py`, `invoke-hermes.ps1`) to read service base URLs from environment variables (`FIREFLY_URL`, `OPENPROJECT_URL`, `PAPERLESS_URL`, `HERMES_URL`) and/or command-line arguments (e.g. `--instance community` or `--port`), defaulting to Private.
10. **Residual `ki-basis/.env` Safety**:
    - Ensure `ki-basis/.env` does not conflict with `.env.private` and `.env.community`. Document or clean up.
11. **Verification**:
    - Run `python ki-basis/scripts/verify_dual_isolation.py` and `pytest ki-basis/tests/test_adversarial_isolation.py`. Ensure all checks pass.

## Output
Write your remediation report to:


## 2026-09-07T10:51:19Z
You are worker_remediate_2. Your working directory is C:\GitDev\apexai-os-meta\.agents\worker_remediate_2.
Read your instructions and the MANDATORY INTEGRITY WARNING in C:\GitDev\apexai-os-meta\.agents\worker_remediate_2\DISPATCH.md.
Read reviewer_2's review in C:\GitDev\apexai-os-meta\.agents\reviewer_2\review.md and challenger_1's findings.
Implement the remediation for all 10 items:
1. Fix TTY CRLF corruption in DUAL_INSTANCE_RUNBOOK.md (remove -t, use -i only for pg_dump/pg_dumpall/tar).
2. Fix Disaster Recovery in DUAL_INSTANCE_RUNBOOK.md (clean postgres volume first, add paperless-data and hermes-workspaces).
3. Upgrade backup-stack.sh for dual-instance namespaces and use -i (no -t).
4. Add PostgreSQL password synchronization step in migration runbook.
5. Fix stop-ki-basis.ps1 so stopping a single instance does NOT terminate Docker Desktop engine.
6. Create stop-ki-basis.sh.
7. Fix timeout handling in start-ki-basis.sh.
8. Fix nginx/default.conf dashboard links for multi-instance support.
9. Implement F17: parameterize client scripts (populate_firefly.py, populate_openproject.py, populate_paperless.py, verify_fundraiser_stack.py, generate_euer_tax_report.py, invoke-hermes.ps1) with env vars and CLI args.
10. Verify with verify_dual_isolation.py and test_adversarial_isolation.py.
Document your changes in remediation_report.md and write handoff.md.
When finished, notify orchestrator_1 via send_message.
