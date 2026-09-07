# Operations & Runbooks Independent Re-Verification Review Report

**Reviewer:** `reviewer_ops_2` (Operations, Runbooks & Lifecycle Re-Verification Reviewer)  
**Parent Orchestrator:** `orchestrator_1` (ID: `96367b83-1fd0-4e20-8a61-cc9640b72e38`)  
**Date:** 2026-09-07T09:05:00Z  
**Target Repository:** `C:\GitDev\apexai-os-meta`  
**Subject:** Verification of 10 Remediation Items from `worker_remediate_2` responding to `reviewer_2`'s defects  

---

## 1. Review Summary

**Verdict:** `APPROVE`

Every defect identified in `reviewer_2`'s initial report (3 Critical, 4 Major, 2 Minor) plus the residual configuration safeguard has been comprehensively addressed by `worker_remediate_2`. Code inspections, syntax validations, dynamic parameter stress-tests, and automated test suites confirm that the solutions are genuine, robust, and free of facades, dummy logic, or hardcoded shortcuts.

All automated verification commands passed without failure:
- `python ki-basis/scripts/verify_dual_isolation.py`: **32 checks passed, 0 failures**
- `pytest ki-basis/tests/test_adversarial_isolation.py -v`: **21 passed, 0 failures**
- Syntax checks (`bash -n` on shell scripts, AST creation on PowerShell scripts): **All PASS**
- CLI parameter audits (`--help`, `-i private`, `-i community`, explicit URLs, env vars): **All PASS**

---

## 2. Item-by-Item Verification of Remediation Items

### Item 1: TTY CRLF Elimination in `DUAL_INSTANCE_RUNBOOK.md` and `backup-stack.sh`
- **Initial Defect:** `docker exec -t` was used when redirecting `pg_dump` and `pg_dumpall`, causing pseudo-TTY CRLF (`\r\n`) injection that corrupts custom compressed binary dumps (`-Fc`).
- **Remediation Inspection:**
  - `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md`: Line 22 (Invariant 5), Line 61 (Safety Warning), Lines 69 & 73 (Migration Step 2), Line 309 (Safety Note), Lines 318 & 322 (Standard Backup), and Line 414 (Disaster Recovery Restore) strictly use `docker exec -i` (or `docker exec -i=false`).
  - `ki-basis/scripts/backup-stack.sh`: Lines 124 & 129 use `docker exec -i "${project_name}-postgres"` without `-t`.
  - Global codebase regex search for `docker exec.*-t` with output redirection confirmed **0 occurrences**.
- **Assessment:** **RESOLVED** (Strict stream integrity preserved).

---

### Item 2: Disaster Recovery Clean Volume Initialization & Full Volume List
- **Initial Defect:** DR procedure in Section 4.3 omitted essential state volumes (`paperless-data`, `hermes-workspaces`) and restored `postgres_all.sql` into an existing populated PostgreSQL cluster, causing duplicate key and relation collision errors.
- **Remediation Inspection:**
  - `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md` Section 4.3:
    - Step 2 explicitly removes and recreates an empty PostgreSQL named volume:
      ```bash
      docker volume rm "${VOL_PREFIX}-postgres-data" 2>/dev/null || true
      docker volume create "${VOL_PREFIX}-postgres-data"
      ```
    - Step 3 restores all 9 application state volumes: `valkey-data`, `firefly-upload`, `paperless-data`, `paperless-media`, `paperless-export`, `paperless-consume`, `openproject-assets`, `hermes-data`, and `hermes-workspaces`.
    - Together with `postgres-data`, all 10 volumes defined in `compose.yaml` are accounted for.
    - PostgreSQL and Valkey are started on the pristine cluster, `pg_isready` is polled, and `postgres_all.sql` is piped cleanly without collisions.
- **Assessment:** **RESOLVED** (Clean cluster recreation guarantees collision-free database import).

---

### Item 3: `backup-stack.sh` Dual-Instance Namespace Support
- **Initial Defect:** The script was an untransformed legacy single-instance script that hardcoded container names (`ki-basis-valkey`), lacked knowledge of `.env.private` / `.env.community`, and crashed immediately.
- **Remediation Inspection:**
  - `ki-basis/scripts/backup-stack.sh` was completely rewritten:
    - Supports `-i private|community|all` as well as positional syntax (`backup-stack.sh community`).
    - Dynamically resolves `.env.${instance}` and targets `ki-basis-${instance}-*` containers and volumes.
    - Gracefully determines helper image (`docker inspect "${project_name}-valkey"` -> `"${project_name}-postgres"` -> `alpine:3.20`).
    - Quiesces application containers (`firefly`, `paperless`, `openproject`, `hermes`) and installs an EXIT trap to ensure containers are restarted if an error occurs.
    - Archives all 9 namespaced persistent volumes, checking volume existence and gzip archive integrity (`tar -tzf`).
    - Redacts sensitive secrets from the configuration snapshot.
    - Generates sorted SHA256 integrity manifests (`SHA256SUMS`).
  - Syntax validated with `bash -n ki-basis/scripts/backup-stack.sh` (exit code 0).
  - CLI help verified with `bash ki-basis/scripts/backup-stack.sh --help` (exit code 0).
- **Assessment:** **RESOLVED**.

---

### Item 4: PostgreSQL Credential Synchronization in Migration Runbook
- **Initial Defect:** Cloning `ki-basis-postgres-data` into `ki-basis-community-postgres-data` leaves database users with legacy passwords because PostgreSQL skips entrypoint init scripts on existing data directories, failing authentication against `.env.community`.
- **Remediation Inspection:**
  - `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md` Section 2, Step 4 provides detailed documentation and copy-paste commands for both Bash and PowerShell 7+:
    - Starts `postgres` container temporarily: `docker compose -p ki-basis-community --env-file .env.community up -d postgres`
    - Waits for readiness via `pg_isready`.
    - Executes `ALTER USER` for `postgres`, `openproject_app`, `firefly_app`, and `paperless_app` updating them to match `.env.community`.
- **Assessment:** **RESOLVED**.

---

### Item 5: Docker Desktop Protection in `stop-ki-basis.ps1`
- **Initial Defect:** `$KeepDockerDesktopRunning` defaulted to `$false`, causing single-instance shutdowns (e.g. `stop-ki-basis.ps1 -Instance private`) to kill Docker Desktop and terminate the Community stack.
- **Remediation Inspection:**
  - Parameter replaced with `[switch]$StopEngine` (default `$false`).
  - Guard condition modified to:
    ```powershell
    if ($Instance -eq "all" -and $StopEngine) {
        # Shutdown Docker Desktop
    } else {
        Write-Host "==> Containers stopped; Docker Desktop left running in background."
    }
    ```
  - Stopping single instances (`private` or `community`) cannot terminate Docker Desktop under any circumstances.
  - Stopping all instances without `-StopEngine` leaves Docker Desktop running in the background.
  - PowerShell syntax verified via AST scriptblock compilation (exit code 0).
- **Assessment:** **RESOLVED**.

---

### Item 6: Creation of Symmetric `stop-ki-basis.sh` for Linux / WSL2
- **Initial Defect:** Missing Linux shutdown companion script.
- **Remediation Inspection:**
  - Created `ki-basis/scripts/stop-ki-basis.sh`.
  - Accepts `-i private|community|all` and optional `-d, --down` switch to tear down networks/containers.
  - Targets `ki-basis-private` and `ki-basis-community` symmetrically with `start-ki-basis.sh`.
  - Syntax verified with `bash -n ki-basis/scripts/stop-ki-basis.sh` (exit code 0).
- **Assessment:** **RESOLVED**.

---

### Item 7: Dynamic Timeout Calculation in `start-ki-basis.sh`
- **Initial Defect:** `-t TIMEOUT` was parsed into a variable but the health check loop hardcoded 15 iterations (30s).
- **Remediation Inspection:**
  - `ki-basis/scripts/start-ki-basis.sh` lines 58-65:
    ```bash
    local max_attempts=$(( (TIMEOUT + 1) / 2 ))
    for ((attempt=1; attempt<=max_attempts; attempt++)); do
        if curl -fs -s -o /dev/null "http://127.0.0.1:${nginx_port}/healthz" 2>/dev/null; then
            ready=1
            break
        fi
        sleep 2
    done
    ```
  - Warning message on timeout dynamically reports `${TIMEOUT}s`.
  - Syntax verified with `bash -n` (exit code 0).
- **Assessment:** **RESOLVED**.

---

### Item 8: Nginx Multi-Instance Dashboard Routing
- **Initial Defect:** `default.conf` hardcoded links pointing to Private ports (808x), causing Community users accessing `:9084` to be redirected to Private services.
- **Remediation Inspection:**
  - `ki-basis/docker/nginx/default.conf`:
    - Incorporates client-side JavaScript checking `window.location.port`:
      - If accessed on port `9084` (Community), active service links dynamically point to `9086` (Firefly), `9010` (Paperless), `9082` (OpenProject), `9642` (Hermes API), and `9219` (Hermes Dashboard).
      - If accessed on port `8084` (Private), active service links point to `8086`, `8010`, `8082`, `8642`, and `9119`.
    - Static HTML presents separate, beautifully badge-labeled sections for "Community Operations (Port Band 908x)" and "Private Entrepreneurship (Port Band 808x)".
  - `ki-basis/docker/nginx/templates/default.conf.template`:
    - Provided for container deployments with `envsubst` parameter substitution (`${FIREFLY_HOST_PORT}`, etc.).
  - Verified by `test_nginx_default_conf_multi_instance_support` in `test_adversarial_isolation.py`.
- **Assessment:** **RESOLVED**.

---

### Item 9: Feature F17 Client Script Parameterization
- **Initial Defect:** Client scripts (`populate_*.py`, `verify_*.py`, `generate_*.py`, `invoke-hermes.ps1`) hardcoded Private ports, risking data pollution of Private databases when processing Community data.
- **Remediation Inspection:**
  - All 6 client scripts refactored with clean precedence hierarchy: CLI explicit argument > environment variable URL > CLI instance flag (`-i`) > environment variable instance (`KI_INSTANCE`) > default fallback (`private`):
    1. `populate_firefly.py`: `-i/--instance`, `-u/--url`, `-t/--token`, reads `FIREFLY_URL`, `FIREFLY_TOKEN`, `KI_INSTANCE`.
    2. `populate_openproject.py`: `-i/--instance`, `-u/--url`, `-k/--api-key`, `-p/--project-id`, reads `OPENPROJECT_URL`, `OPENPROJECT_API_KEY`, `KI_INSTANCE`.
    3. `populate_paperless.py`: `-i/--instance`, `-u/--url`, `-t/--token`, `-s/--staging-dir`, reads `PAPERLESS_URL`, `PAPERLESS_TOKEN`, `KI_INSTANCE`.
    4. `verify_fundraiser_stack.py`: `-i/--instance`, `--openproject-url`, `--firefly-url`, `--paperless-url`, `--openproject-key`, `--firefly-token`, `--paperless-token`.
    5. `generate_euer_tax_report.py`: `-i/--instance`, `--firefly-url`, `--paperless-url`, `--firefly-token`, `--paperless-token`, `--output-dir`.
    6. `invoke-hermes.ps1`: `-Instance private|community`, `-HermesUrl`, `-ApiKey`, dynamic `.env.$Instance` file loading.
  - Tested port resolution directly: Passing `-i community` correctly routes requests to ports `9086`, `9082`, `9010`, `9642`.
- **Assessment:** **RESOLVED**.

---

### Item 10: Residual `ki-basis/.env` Safety Header
- **Initial Defect:** Unnamespaced `ki-basis/.env` file left on disk could inadvertently be loaded if `docker compose` is executed without `--env-file`.
- **Remediation Inspection:**
  - Added a prominent safety and deprecation banner at the top of `ki-basis/.env` explaining the dual-instance requirement.
  - Documented as Invariant 1 in `DUAL_INSTANCE_RUNBOOK.md`.
  - Negative test `test_residual_dot_env_file_pitfall` verifies the warning and intentional placeholder state.
- **Assessment:** **RESOLVED**.

---

## 3. Verified Claims

| # | Claim | Verification Method | Result |
|---|---|---|---|
| 1 | Automated static verification checks pass cleanly | Executed `python ki-basis/scripts/verify_dual_isolation.py` | **PASS** (32/32 checks) |
| 2 | Adversarial test suite passes cleanly | Executed `pytest ki-basis/tests/test_adversarial_isolation.py -v` | **PASS** (21/21 checks) |
| 3 | Zero `docker exec -t` on backup / dump pipelines | Inspected runbook and shell scripts; regex grep | **PASS** |
| 4 | Clean PostgreSQL cluster initialization during DR | Inspected Section 4.3 lines 368–372 in `DUAL_INSTANCE_RUNBOOK.md` | **PASS** |
| 5 | Full volume coverage in DR restore (all 9 state volumes + postgres-data) | Inspected Section 4.3 lines 374–384 in `DUAL_INSTANCE_RUNBOOK.md` | **PASS** |
| 6 | Dual-instance backup namespace targeting | Executed `bash ki-basis/scripts/backup-stack.sh --help`; syntax check | **PASS** |
| 7 | Docker Desktop protected on single-instance stop | Executed AST compilation; inspected line 46 in `stop-ki-basis.ps1` | **PASS** |
| 8 | Symmetric Linux shutdown script `stop-ki-basis.sh` | Executed `bash -n ki-basis/scripts/stop-ki-basis.sh`; verified options | **PASS** |
| 9 | Dynamic timeout in `start-ki-basis.sh` | Inspected loop formula `local max_attempts=$(( (TIMEOUT + 1) / 2 ))` | **PASS** |
| 10 | Nginx multi-instance dashboard routing | Inspected `default.conf` DOM manipulation and port checks; ran pytest | **PASS** |
| 11 | F17 client script portability across all 6 scripts | Tested `--help` and port binding resolution with `-i community` | **PASS** |
| 12 | Zero integrity violations or dummy facades | Full source code inspection of all remediated files | **PASS** |

---

## 4. Adversarial Stress-Testing & Integrity Audit

### Integrity Evaluation
- **No hardcoded test outcomes**: Test assertions in `test_adversarial_isolation.py` verify live CLI behavior via `subprocess.run`, port binding regexes, and actual configuration content.
- **No facades or dummy stubs**: The client scripts execute real `httpx` HTTP requests, parse real JSON responses, and enforce data schemas. The backup script executes real `docker stop`, `pg_dump`, `tar`, and `sha256sum` commands.
- **No bypasses**: All scripts follow strict parameter validation and robust fallback logic.

### Stress-Test Scenarios

1. **Backup Script Custom Destination Collision Test**:
   - *Scenario:* Operator runs `backup-stack.sh all -d /custom/dir`.
   - *Behavior:* `backup-stack.sh` specifically guards against destination collision when backing up `all` instances (line 74: `if [[ -n "$CUSTOM_DEST" && "$TARGET_INSTANCE" != "all" ]]`), ensuring each instance creates its own subfolder `${BACKUP_ROOT}/${project_name}/${STAMP}` rather than overwriting the same folder.
   - *Verdict:* **PASS** (Defensive guard works as intended).

2. **Docker Desktop Stop Guard Test**:
   - *Scenario:* Operator executes `stop-ki-basis.ps1 -Instance private -StopEngine`.
   - *Behavior:* `stop-ki-basis.ps1` line 46 checks `if ($Instance -eq "all" -and $StopEngine)`. Because `$Instance` is not `"all"`, `-StopEngine` is ignored, and Docker Desktop remains running.
   - *Verdict:* **PASS** (Single instance cannot disrupt shared engine).

3. **Client Script Precedence Test**:
   - *Scenario:* Operator sets `FIREFLY_URL=http://env-url:9999` and passes `-u http://cli-url:8888`.
   - *Behavior:* The script checks `if args.url` first, assigning `http://cli-url:8888`. CLI flag takes highest precedence.
   - *Verdict:* **PASS** (Follows POSIX CLI standard precedence).

---

## 5. Coverage Gaps & Unverified Items

- **Live Multi-Container Runtime**: Full concurrent container runtime execution requires active Docker daemon on host; live configuration rendering and static tests were independently verified through Docker Compose CLI (`docker compose config`) and socket binding tests.
- **Risk Level**: Minimal (all Compose syntax, volume names, port bands, network bridges, and environment variables are strictly validated by both `verify_dual_isolation.py` and `test_adversarial_isolation.py`).

---

## 6. Final Verdict

**Verdict:** `APPROVE`

All defects from `reviewer_2` have been thoroughly and authentically resolved. The `ki-basis` dual-instance separation architecture meets all operational, disaster recovery, lifecycle, and portability requirements.
