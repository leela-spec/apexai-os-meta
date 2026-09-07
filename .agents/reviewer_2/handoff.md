# 5-Component Handoff Report: Reviewer 2 (Operations, Runbooks & Lifecycle)

**Worker/Reviewer:** `reviewer_2`  
**Parent Orchestrator:** `orchestrator_1` (ID: `96367b83-1fd0-4e20-8a61-cc9640b72e38`)  
**Timestamp:** 2026-09-07T08:46:50Z  
**Target Scope:** Operations Runbooks, Migration Guide, Daily Operations, Backup/Restore, Lifecycle Scripts  
**Handoff Type:** Hard Handoff (Review Complete)  
**Verdict:** `REQUEST_CHANGES`

---

## 1. Observation

1. **Binary Dump Corruption via PTY Allocation in `DUAL_INSTANCE_RUNBOOK.md`**:
   - `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md`:
     - Line 64: `docker exec -t ki-basis-postgres pg_dumpall -U postgres > "${BACKUP_DIR}/postgres_full_dump.sql"`
     - Line 68: `docker exec -t ki-basis-postgres pg_dump -U postgres -d "$db" -Fc > "${BACKUP_DIR}/${db}_custom.dump"`
     - Line 248: `docker exec -t "ki-basis-${INSTANCE}-postgres" pg_dumpall -U postgres > "${BACKUP_ROOT}/postgres_all.sql"`
     - Line 252: `docker exec -t "ki-basis-${INSTANCE}-postgres" pg_dump -U postgres -d "$db" -Fc > "${BACKUP_ROOT}/${db}.dump"`
   - By contrast, legacy `ki-basis/scripts/backup-stack.sh` lines 23–24 explicitly ran without `-t`:
     `docker exec -i=false ki-basis-postgres pg_dumpall ...`
     `docker exec -i=false ki-basis-postgres pg_dump -U "$PGUSER" -Fc "$db" ...`

2. **Flawed Disaster Recovery Restore Procedure in `DUAL_INSTANCE_RUNBOOK.md` (Section 4.3)**:
   - Line 277: `docker compose -p "ki-basis-${INSTANCE}" --env-file ".env.${INSTANCE}" down` leaves the `postgres-data` volume intact on the host.
   - Lines 280–288: The volume recreation loop only recreates `paperless-media`, `openproject-assets`, `firefly-upload`, and `hermes-data`. It omits `postgres-data`, `paperless-data` (SQLite and index state), `hermes-workspaces`, `valkey-data`, `paperless-export`, and `paperless-consume`.
   - Line 291: Starts postgres using the intact, populated `postgres-data` volume.
   - Line 300: `docker exec -i "ki-basis-${INSTANCE}-postgres" psql -U postgres < "${BACKUP_ARCHIVE_DIR}/postgres_all.sql"` pipes a full cluster dump into an active, already-populated database, causing unique constraint and existing table collisions.

3. **Untransformed and Broken `backup-stack.sh`**:
   - `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md` lines 233–236 states:
     ```bash
     # Backup Community Stack
     ./scripts/backup-stack.sh community
     # Backup Private Stack
     ./scripts/backup-stack.sh private
     ```
   - In `ki-basis/scripts/backup-stack.sh`:
     - Line 10: `DEST="${1:-$BACKUP_ROOT/$STAMP}"` treats `community` as the destination directory, not the instance name.
     - Line 4: `ENV_FILE="${ENV_FILE:-.env}"` fails to find an active `.env` and defaults to `.env.example`.
     - Line 15: `HELPER_IMAGE="$(docker inspect ki-basis-valkey --format '{{.Config.Image}}' | tr -d '\r\n')"` fails because the running containers are `ki-basis-private-valkey` and `ki-basis-community-valkey`. Running `./scripts/backup-stack.sh community` exits with:
       `Could not determine backup helper image`.
     - Lines 22, 23, 24, 35–43, 52: Hardcode legacy container names (`ki-basis-hermes`, `ki-basis-postgres`) and volume names (`ki-basis-valkey-data`).

4. **Migration Volume Cloning Password Desynchronization**:
   - `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md` Step 3 clones `ki-basis-postgres-data` to `ki-basis-community-postgres-data`.
   - When PostgreSQL boots in Step 5 from this existing volume, PostgreSQL's entrypoint skips `01-init-databases.sh` and leaves the legacy database passwords active.
   - `.env.community` lines 27, 32, 38, 48 specify new passwords (`comm_pg_sec_...`, `comm_ff_db_...`, `comm_pl_db_...`, `comm_op_db_...`).
   - Consequently, Firefly, Paperless, and OpenProject fail database authentication upon startup.

5. **`stop-ki-basis.ps1` Docker Desktop Shutdown on Single-Instance Stop**:
   - `ki-basis/scripts/stop-ki-basis.ps1` lines 32–43:
     ```powershell
     if (-not $KeepDockerDesktopRunning) {
         Stop-Process -Name "Docker Desktop", "com.docker.backend" -Force ...
     }
     ```
   - Running `.\scripts\stop-ki-basis.ps1 -Instance private` terminates the host Docker Desktop daemon by default, crashing the running Community stack.

6. **Hardcoded Nginx Dashboard Links Pointing to Private Ports**:
   - `ki-basis/docker/nginx/default.conf` line 15:
     ```html
     <li><a href="http://127.0.0.1:8086">Firefly III (Finance) — :8086</a></li>
     <li><a href="http://127.0.0.1:8010">Paperless-ngx (Documents) — :8010</a></li>
     <li><a href="http://127.0.0.1:8082">OpenProject (Projects) — :8082</a></li>
     <li><a href="http://127.0.0.1:8642">Hermes Dashboard (AI) — :8642</a></li>
     ```
   - Mounted into `ki-basis-community-nginx` (:9084). Community operators clicking dashboard links are sent to Private stack services.

7. **Client Scripts Unparameterized (F17 Skipped)**:
   - `populate_firefly.py` line 10: `FIREFLY_URL = "http://127.0.0.1:8086"`
   - `populate_openproject.py` line 10: `OPENPROJECT_URL = "http://127.0.0.1:8082"`
   - `populate_paperless.py` line 10: `PAPERLESS_URL = "http://127.0.0.1:8010"`
   - `generate_euer_tax_report.py` lines 15, 29: hardcoded 8086, 8010
   - `verify_fundraiser_stack.py` lines 13, 16, 30: hardcoded 8082, 8086, 8010
   - `invoke-hermes.ps1` line 12: requires `ki-basis\.env` (does not exist); line 54: hardcoded `:8642`.
   - Running these scripts against Community data targets Private ports by default.

---

## 2. Logic Chain

1. **From Observation 1**:
   Because `-t` allocates a pseudo-TTY, any binary data emitted by `pg_dump -Fc` undergoes newline conversion (`0x0A` -> `0x0D 0x0A`), corrupting the zlib archive signature and internal page framing. Any backup or pre-migration snapshot taken following lines 68 or 252 will be completely un-restorable via `pg_restore`.
2. **From Observation 2**:
   Because `docker compose down` leaves volumes intact and `postgres-data` is not reset prior to restore, PostgreSQL boots with existing tables. Piping `postgres_all.sql` directly into a populated cluster triggers duplicate key constraints and existing relation errors, rendering the documented DR procedure inoperable. Furthermore, omitting `paperless-data` loses document indices and machine-learning classification models.
3. **From Observation 3**:
   Because `backup-stack.sh` was never rewritten to inspect namespaced containers or load instance `.env` files, invoking `./scripts/backup-stack.sh community` crashes on container inspection, contradicting the runbook's operational claims.
4. **From Observation 4**:
   Because PostgreSQL skips initialization scripts when mounting an existing data directory, the cloned Community volume retains legacy passwords. Since `.env.community` defines new passwords, all application services will enter crash loops due to `password authentication failed`.
5. **From Observation 5**:
   Because `stop-ki-basis.ps1` unconditionally triggers Docker Desktop termination unless `$KeepDockerDesktopRunning` is explicitly passed, executing a single-instance stop destroys the multi-tenant isolation principle by taking down both instances.
6. **From Observation 6 & 7**:
   Because Nginx and client scripts hardcode Private port bindings (808x), Community users are either redirected to Private services or script executions contaminate Private databases with Community records, violating isolation and skipping Feature F17.

---

## 3. Caveats

- The core Docker Compose parameterization (`compose.yaml`) and environment files (`.env.private`, `.env.community`) are well structured and passed all 32 checks of `verify_dual_isolation.py`.
- PowerShell and Bash script syntax was verified without syntax errors.
- The issues identified are operational, procedural, and behavioral logic defects that will manifest during actual migration, backup/restore, and multi-tenant daily use.

---

## 4. Conclusion

**Verdict: `REQUEST_CHANGES`**

The dual-instance infrastructure cannot be certified for production operations until the operational runbooks and lifecycle scripts are remediated:
1. Remove `-t` from all `pg_dump` and `pg_dumpall` commands in `DUAL_INSTANCE_RUNBOOK.md`.
2. Rewrite the Disaster Recovery restore runbook to clean target volumes and handle database restoration safely without collision.
3. Refactor `backup-stack.sh` to support `-i private|community` and dynamically target namespaced resources.
4. Add database password reconciliation (`ALTER USER`) to the migration runbook.
5. Fix `stop-ki-basis.ps1` so stopping one instance never terminates the shared Docker Desktop daemon.
6. Parameterize Nginx dashboard links to eliminate cross-stack redirects.
7. Parameterize client scripts (`populate_*`, `verify_*`, `invoke-hermes.ps1`) to satisfy Milestone M4 Feature F17.

---

## 5. Verification Method

To independently reproduce and verify these findings:

1. **Verify PTY Corruption Risk**:
   Review lines 64, 68, 248, 252 of `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md` against Docker CLI documentation regarding pseudo-TTY allocation on binary streams.
2. **Verify `backup-stack.sh` Failure**:
   ```bash
   bash ki-basis/scripts/backup-stack.sh community
   # Observation: Fails with "Could not determine backup helper image" due to looking for legacy "ki-basis-valkey"
   ```
3. **Verify `stop-ki-basis.ps1` Blast Radius**:
   Inspect lines 32–43 of `ki-basis/scripts/stop-ki-basis.ps1`. Notice that calling `.\scripts\stop-ki-basis.ps1 -Instance private` calls `Stop-Process` on Docker Desktop unless `-KeepDockerDesktopRunning` is passed.
4. **Verify Nginx Hardcoded Links**:
   Inspect line 15 of `ki-basis/docker/nginx/default.conf`. Notice hardcoded links `http://127.0.0.1:8086`, `:8010`, `:8082`, `:8642`.
5. **Verify F17 Script Portability Omission**:
   Inspect line 10 in `ki-basis/scripts/populate_firefly.py`, `populate_openproject.py`, `populate_paperless.py`.
