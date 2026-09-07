# Independent Quality & Adversarial Review Report: ki-basis Dual-Instance Operations & Lifecycle

**Reviewer:** `reviewer_2` (Operations, Runbooks & Lifecycle Reviewer)  
**Parent Orchestrator:** `orchestrator_1` (ID: `96367b83-1fd0-4e20-8a61-cc9640b72e38`)  
**Target Review Artifacts:**
- `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md`
- `ki-basis/scripts/start-ki-basis.ps1`
- `ki-basis/scripts/start-ki-basis.sh`
- `ki-basis/scripts/stop-ki-basis.ps1`
- `ki-basis/scripts/backup-stack.sh`
- `ki-basis/docker/nginx/default.conf`
- Client & integration scripts in `ki-basis/scripts/`
**Date:** 2026-09-07T08:46:00Z  

---

## 1. Review Summary

**Verdict:** `REQUEST_CHANGES`

While the core Docker Compose parameterization (`ki-basis/compose.yaml`), project namespacing, port band allocation (808x vs 908x), and the static verification harness (`verify_dual_isolation.py`) are solidly architected and verified, an adversarial evaluation of the operational runbooks and lifecycle scripts revealed **three critical data-loss/restore flaws** and **four major operational and isolation defects**. Most notably, backup and migration instructions rely on pseudo-TTY commands (`docker exec -t`) that silently corrupt binary database dumps, the disaster recovery procedure fails against active database instances, the documented backup script (`backup-stack.sh`) was never transformed for dual-instance, and stopping a single instance abruptly kills the entire host Docker daemon.

---

## 2. Review Findings

### [Critical] Finding 1: Silent Binary Dump Corruption via `docker exec -t` in Migration and Backup Runbooks
- **What:** The runbook prescribes using `docker exec -t` when executing `pg_dumpall` and `pg_dump -Fc` for backups and pre-migration snapshots.
- **Where:** `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md`, lines 64, 68, 248, and 252.
- **Why (Mechanics):** 
  The `-t` flag instructs Docker to allocate a pseudo-TTY (PTY). PTY line disciplines automatically convert Unix newline characters (`\n`, `0x0A`) to Carriage Return + Line Feed (`\r\n`, `0x0D 0x0A`) and may inject terminal control escape codes or column wrapping. For logical SQL dumps (`pg_dumpall`), this introduces unwanted Windows CRLF line endings. For compressed binary custom-format archives (`pg_dump -Fc`), this **fatally corrupts the binary stream**.
  When an operator attempts to restore from a dump generated with `-t` via `pg_restore`, PostgreSQL will abort with:
  `pg_restore: error: did not find expected signature in header; corrupted file or not a dump file`.
  The legacy script `backup-stack.sh` specifically used `-i=false` and omitted `-t` (lines 23–24) to avoid this exact failure mode.
- **Suggestion:**
  Remove `-t` and use `docker exec -i` (or `docker exec -i=false`) for all `pg_dump` and `pg_dumpall` commands in `DUAL_INSTANCE_RUNBOOK.md`:
  ```bash
  # Correct logical dump command:
  docker exec -i "ki-basis-${INSTANCE}-postgres" pg_dumpall -U postgres > "${BACKUP_ROOT}/postgres_all.sql"
  # Correct binary dump command:
  docker exec -i "ki-basis-${INSTANCE}-postgres" pg_dump -U postgres -d "$db" -Fc > "${BACKUP_ROOT}/${db}.dump"
  ```

---

### [Critical] Finding 2: Disaster Recovery Restore Procedure Restores into Populated DB & Skips Essential Volumes
- **What:** The disaster recovery restore procedure in Section 4.3 cannot successfully restore databases and omits vital application volumes.
- **Where:** `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md`, Section 4.3 (lines 270–305).
- **Why (Mechanics):**
  1. **Volume Omissions:** The volume restoration loop (lines 280–288) only restores `paperless-media`, `openproject-assets`, `firefly-upload`, and `hermes-data`. It completely omits `ki-basis-${INSTANCE}-paperless-data` (which contains Paperless SQLite search index and document classifier state), `ki-basis-${INSTANCE}-hermes-workspaces`, `ki-basis-${INSTANCE}-valkey-data`, `paperless-export`, and `paperless-consume`.
  2. **Database Collision:** In Step 1, `docker compose down` is run without `-v`, leaving the `ki-basis-${INSTANCE}-postgres-data` volume intact. In Step 3, PostgreSQL starts up pointing to this existing, populated data directory. In Step 4, the runbook attempts:
     `docker exec -i "ki-basis-${INSTANCE}-postgres" psql -U postgres < "${BACKUP_ARCHIVE_DIR}/postgres_all.sql"`
     Because the target database already exists and contains tables, `psql` triggers a cascade of fatal errors: `ERROR: database "firefly" already exists`, `ERROR: relation "..." already exists`, and `ERROR: duplicate key value violates unique constraint` across all primary keys. The restore completely fails or leaves the database in an inconsistent state.
- **Suggestion:**
  In Section 4.3:
  1. Include `postgres-data`, `paperless-data`, and `hermes-workspaces` in the volume restoration list.
  2. For a clean database restore, wipe `ki-basis-${INSTANCE}-postgres-data` (`docker volume rm ki-basis-${INSTANCE}-postgres-data`) so PostgreSQL starts as a fresh cluster before importing `postgres_all.sql`, or drop existing databases before restoring.

---

### [Critical] Finding 3: `backup-stack.sh` Was Never Updated for Dual-Instance (Untransformed Legacy Script)
- **What:** Section 4.1 of `DUAL_INSTANCE_RUNBOOK.md` directs operators to use `./scripts/backup-stack.sh community` and `./scripts/backup-stack.sh private`. However, `backup-stack.sh` was never updated to support dual-instance architecture.
- **Where:** `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md` lines 228–237 and `ki-basis/scripts/backup-stack.sh`.
- **Why (Mechanics):**
  1. `backup-stack.sh` line 10 defines `DEST="${1:-$BACKUP_ROOT/$STAMP}"`. Passing `community` or `private` as `$1` causes the script to treat the instance name as the output directory path (`./community` or `./private`).
  2. Line 4 hardcodes `ENV_FILE="${ENV_FILE:-.env}"` and defaults to `.env.example`, having no knowledge of `.env.private` or `.env.community`.
  3. Line 15 runs `docker inspect ki-basis-valkey`. In dual-instance, this container does not exist (they are `ki-basis-private-valkey` and `ki-basis-community-valkey`). The script crashes immediately on line 16 with `Could not determine backup helper image`.
  4. Lines 22, 23, 24, 35–43, and 52 hardcode legacy container names (`ki-basis-hermes`, `ki-basis-postgres`) and legacy volume names (`ki-basis-valkey-data`, etc.).
- **Suggestion:**
  Refactor `backup-stack.sh` to accept `-i private|community`, dynamically load `.env.${INSTANCE}`, query `ki-basis-${INSTANCE}-valkey`, and archive `ki-basis-${INSTANCE}-*` volumes.

---

### [Major] Finding 4: Migration Volume Cloning Leaves Database Credentials Desynchronized
- **What:** Cloning the legacy `ki-basis-postgres-data` volume into `ki-basis-community-postgres-data` (Migration Step 3) creates a password mismatch with `.env.community`.
- **Where:** `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md`, Step 3 (lines 103–120) & Step 5 (lines 130–144).
- **Why (Mechanics):**
  The PostgreSQL entrypoint container only executes `/docker-entrypoint-initdb.d/01-init-databases.sh` when `PGDATA` is completely empty. When PostgreSQL boots from the cloned volume, it recognizes an existing database cluster and **skips user creation and password initialization**.
  Consequently, the internal database users (`firefly_app`, `paperless_app`, `openproject_app`, `postgres`) retain their legacy passwords from the old deployment. However, `.env.community` defines new, distinct, high-entropy passwords (`OPENPROJECT_DB_PASSWORD`, etc.). When Community application containers start in Step 5, all three applications fail database authentication with `password authentication failed`, causing crash loops.
- **Suggestion:**
  Add an explicit password reconciliation step to Migration Step 3:
  ```bash
  # After bringing up postgres temporarily, synchronize passwords to match .env.community:
  docker exec -i ki-basis-community-postgres psql -U postgres -c "ALTER USER openproject_app WITH PASSWORD '${OPENPROJECT_DB_PASSWORD}';"
  docker exec -i ki-basis-community-postgres psql -U postgres -c "ALTER USER firefly_app WITH PASSWORD '${FIREFLY_DB_PASSWORD}';"
  docker exec -i ki-basis-community-postgres psql -U postgres -c "ALTER USER paperless_app WITH PASSWORD '${PAPERLESS_DB_PASSWORD}';"
  ```

---

### [Major] Finding 5: Nginx Default Dashboard Hardcodes Private Ports for Both Instances
- **What:** The Nginx landing page serves identical links pointing exclusively to Private ports (808x) even when running inside the Community stack (port 9084).
- **Where:** `ki-basis/docker/nginx/default.conf` line 15, mounted via `compose.yaml` line 174.
- **Why (Mechanics):**
  Both `ki-basis-private-nginx` and `ki-basis-community-nginx` mount `./docker/nginx:/etc/nginx/conf.d:ro`. Line 15 of `default.conf` hardcodes:
  ```html
  <a href="http://127.0.0.1:8086">Firefly III</a>
  <a href="http://127.0.0.1:8010">Paperless-ngx</a>
  <a href="http://127.0.0.1:8082">OpenProject</a>
  <a href="http://127.0.0.1:8642">Hermes Dashboard</a>
  ```
  When an operator accesses the Community Edge Dashboard at `http://127.0.0.1:9084/`, clicking any service link sends them directly to the **Private Entrepreneurship** stack (8086, 8010, 8082, 8642). This contradicts Runbook Table 3.2 ("Links to all Community services") and creates a cross-tenant data access risk.
- **Suggestion:**
  Parameterize `default.conf` using Nginx environment variable templates (`/etc/nginx/templates/default.conf.template`) so Docker dynamically injects `${FIREFLY_HOST_PORT}`, `${PAPERLESS_HOST_PORT}`, `${OPENPROJECT_HOST_PORT}`, and `${HERMES_DASHBOARD_HOST_PORT}`.

---

### [Major] Finding 6: `stop-ki-basis.ps1` Forcibly Kills Host Docker Daemon on Single-Instance Shutdown
- **What:** Executing `.\scripts\stop-ki-basis.ps1 -Instance private` terminates the host Docker Desktop daemon by default.
- **Where:** `ki-basis/scripts/stop-ki-basis.ps1` lines 32–43.
- **Why (Mechanics):**
  Lines 32–43 evaluate:
  ```powershell
  if (-not $KeepDockerDesktopRunning) {
      Stop-Process -Name "Docker Desktop", "com.docker.backend" -Force ...
  }
  ```
  Because `$KeepDockerDesktopRunning` defaults to `$false`, stopping a single instance (e.g. `stop-ki-basis.ps1 -Instance private`) immediately executes `Stop-Process` against Docker Desktop and `com.docker.backend`. This violently shuts down the Community stack, kills running background jobs, and disrupts all other Docker workloads on the Windows host.
- **Suggestion:**
  Only kill Docker Desktop when `$Instance -eq "all"` and an explicit switch `-ShutdownEngine` is provided:
  ```powershell
  if ($Instance -eq "all" -and $ShutdownEngine) {
      # stop Docker Desktop
  }
  ```

---

### [Major] Finding 7: Client Integration Scripts Omitted Parameterization (F17 Skipped)
- **What:** Client scripts in `ki-basis/scripts/` remain hardcoded to Private ports 8082, 8086, 8010, and 8642, skipping Milestone M4 feature F17 (`F17-SCRIPT-PORTABILITY`).
- **Where:**
  - `ki-basis/scripts/populate_firefly.py` (line 10: `FIREFLY_URL = "http://127.0.0.1:8086"`)
  - `ki-basis/scripts/populate_openproject.py` (line 10: `OPENPROJECT_URL = "http://127.0.0.1:8082"`)
  - `ki-basis/scripts/populate_paperless.py` (line 10: `PAPERLESS_URL = "http://127.0.0.1:8010"`)
  - `ki-basis/scripts/generate_euer_tax_report.py` (lines 15 & 29: ports 8086 and 8010)
  - `ki-basis/scripts/verify_fundraiser_stack.py` (lines 13, 16, 30: ports 8082, 8086, 8010)
  - `ki-basis/scripts/invoke-hermes.ps1` (line 12: requires non-existent `ki-basis\.env`; line 54: hardcoded `:8642`)
- **Why (Mechanics):**
  All of these scripts process **Community Operations** data (Safer Space e.V., Equinox 2026 fundraiser, German non-profit 4-sphere tax reporting). Because they lack URL parameterization, running any of them against the separated environment will either fail (if Private is down) or inadvertently inject Community non-profit records into the Private Entrepreneurship database!
- **Suggestion:**
  Update each client script to check environment variables (`FIREFLY_URL`, `OPENPROJECT_URL`, `PAPERLESS_URL`) or CLI arguments, defaulting to Community ports (9086, 9082, 9010) when running in Community context. Update `invoke-hermes.ps1` to accept `-Instance private|community`.

---

### [Minor] Finding 8: `TIMEOUT` Parameter in `start-ki-basis.sh` Is Dead Code
- **What:** `start-ki-basis.sh` defines and parses `-t TIMEOUT` (lines 8, 20), but the variable is never used.
- **Where:** `ki-basis/scripts/start-ki-basis.sh` lines 58–64.
- **Why:** The health check loop hardcodes `for ((i=0; i<15; i++)); do ... sleep 2; done` (30 seconds total), ignoring the user-supplied timeout.
- **Suggestion:** Derive loop iterations dynamically: `local max_attempts=$((TIMEOUT / 2))`.

---

### [Minor] Finding 9: Missing `stop-ki-basis.sh` for Linux / WSL2
- **What:** While `start-ki-basis.sh` was provided for Linux/WSL2, there is no corresponding `stop-ki-basis.sh`.
- **Where:** `ki-basis/scripts/`.
- **Why:** Linux operators must manually write multi-argument `docker compose -p ... -f ... --env-file ... stop` commands.
- **Suggestion:** Provide `ki-basis/scripts/stop-ki-basis.sh` supporting `-i private|community|all`.

---

## 3. Verified Claims

| Claim | Source | Verification Method | Result |
|---|---|---|---|
| Compose YAML parses cleanly under both `.env.private` and `.env.community` | `worker_impl_1` handoff | `python verify_dual_isolation.py` & YAML inspection | **PASS** |
| Zero container name collisions between stacks | `worker_impl_1` handoff | `python verify_dual_isolation.py` check 2 | **PASS** |
| Fully disjoint bridge networks (`ki-basis-private-net` vs `ki-basis-community-net`) | `worker_impl_1` handoff | Network name assertion in `verify_dual_isolation.py` | **PASS** |
| Strict loopback host binding (`127.0.0.1`) with zero `0.0.0.0` exposure | `worker_impl_1` handoff | Port binding regex in `verify_dual_isolation.py` | **PASS** |
| PostgreSQL (:5432) and Valkey (:6379) unexposed to host | `worker_impl_1` handoff | Port extraction check in `verify_dual_isolation.py` | **PASS** |
| Zero shared named volumes (20 distinct ext4 volumes across stacks) | `worker_impl_1` handoff | Volume set disjointness assertion | **PASS** |
| OpenProject stability (`WEB_WORKERS=1`, `PG_STARTUP_WAIT_TIME=60`) | `worker_impl_1` handoff | Environment variable assertion | **PASS** |
| Distinct cryptographic secrets and credentials | `worker_impl_1` handoff | Secret entropy and uniqueness check | **PASS** |
| PowerShell script syntax | `start-ki-basis.ps1`, `stop-ki-basis.ps1` | `[scriptblock]::Create()` in PowerShell | **PASS** |
| Bash script syntax | `start-ki-basis.sh` | `bash -n` execution | **PASS** |

---

## 4. Coverage Gaps & Unverified Items

- **`backup-stack.sh` execution with dual instances:** Could not be verified because the script is hardcoded to single-instance resources and crashes immediately.
- **Disaster Recovery live test:** Live recovery of `postgres_all.sql` into an existing cluster cannot succeed due to duplicate key / existing object errors.
- **F17 Script Portability:** All 6 data population and verification scripts were left untouched and were not verified for dual-instance portability.

---

## 5. Adversarial Challenge Report

### Overall Risk Assessment: **HIGH**

### Key Attack Scenarios & Blast Radii

1. **The Corrupted Backup Trap:**
   - *Scenario:* Operator follows `DUAL_INSTANCE_RUNBOOK.md` Step 2 before performing routine maintenance, running `docker exec -t ki-basis-postgres pg_dump -U postgres -d openproject -Fc > openproject_custom.dump`.
   - *Failure Mode:* The `-t` flag injects PTY carriage returns into the binary dump. The backup appears complete (file size > 0), but is cryptographically and structurally corrupted.
   - *Blast Radius:* Irrecoverable total data loss of OpenProject or Firefly when restore is attempted during a disaster.

2. **The Shared Docker Engine Kill:**
   - *Scenario:* Operator finishes private consulting work for the day and runs `.\scripts\stop-ki-basis.ps1 -Instance private`.
   - *Failure Mode:* `stop-ki-basis.ps1` kills `Docker Desktop.exe` and `com.docker.backend.exe`.
   - *Blast Radius:* Community stack (Equinox ticket intake, Safer Space e.V. services) is abruptly terminated with zero warning.

3. **Cross-Tenant UI Leaks:**
   - *Scenario:* Safer Space e.V. volunteer opens the Community dashboard at `http://127.0.0.1:9084/` and clicks "Firefly III".
   - *Failure Mode:* The link targets `http://127.0.0.1:8086` (Private Entrepreneurship).
   - *Blast Radius:* Volunteer accesses commercial accounting or encounters authentication friction, breaking institutional separation.

4. **Community Script Pollution of Private DB:**
   - *Scenario:* Operator runs `python scripts/populate_firefly.py` to seed Equinox tickets while both stacks are running.
   - *Failure Mode:* Script connects to default port `8086` instead of `9086`.
   - *Blast Radius:* Safer Space e.V. ticket revenue transactions are written directly to the commercial consulting ledger in the Private instance.

---

## 6. Actionable Recommendations for Remediation

1. **Fix `DUAL_INSTANCE_RUNBOOK.md`**:
   - Change `docker exec -t` to `docker exec -i` for all `pg_dump` and `pg_dumpall` instructions.
   - Fix Section 4.3 (DR Restore) to include `postgres-data`, `paperless-data`, and `hermes-workspaces`, and ensure `ki-basis-${INSTANCE}-postgres-data` is reinitialized cleanly before piping `postgres_all.sql`.
   - Add database user password synchronization (`ALTER USER`) to Migration Step 3.
2. **Update `backup-stack.sh`**:
   - Add `-i private|community` flag.
   - Read `.env.${INSTANCE}` and dynamically target `ki-basis-${INSTANCE}-*` containers and volumes.
3. **Fix `stop-ki-basis.ps1`**:
   - Ensure Docker Desktop is NOT terminated when stopping individual instances (`private` or `community`).
4. **Fix `ki-basis/docker/nginx/default.conf`**:
   - Parameterize dashboard service links to respect instance port bands.
5. **Implement F17 Portability**:
   - Parameterize `populate_*.py`, `verify_fundraiser_stack.py`, `generate_euer_tax_report.py`, and `invoke-hermes.ps1` with environment variables or CLI flags for dynamic host ports.
