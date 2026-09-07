# Operations & Migration Runbook: ki-basis Dual-Instance Architecture

**Document Version:** 1.0.0  
**Date:** 2026-09-07  
**Status:** PRODUCTION OPERATIONAL RUNBOOK  
**Applies To:** `ki-basis-private` & `ki-basis-community`  
**Target Environment:** Windows 11 (PowerShell 7+ / WSL2 / Docker Engine)

---

## 1. Overview & Operational Principles

This runbook provides complete operational procedures for managing the separated `ki-basis` infrastructure across two distinct operational domains:
- **Private Entrepreneurship (`ki-basis-private`)**: Port Band 8080–8089 / 8642 / 9119.
- **Community Operations (`ki-basis-community`)**: Port Band 9080–9089 / 9642 / 9219.

### Key Operational Invariants
1. **Never use unqualified Compose commands**: Always specify the project namespace (`-p`) and explicit environment file (`--env-file`) when issuing Docker Compose commands. The root `ki-basis/.env` is a legacy single-instance placeholder; running `docker compose` without `--env-file` will mistakenly load this file, binding Private ports (808x) and using weak placeholder credentials.
2. **Never bind to 0.0.0.0**: All host-published ports must bind to `127.0.0.1` (loopback only).
3. **Never place persistent state on 9P**: Persistent databases and assets must remain in Docker named volumes on native ext4 storage.
4. **Independent Backup Lifecycles**: Backups must be generated, stored, and verified separately for Private and Community.
5. **Strict Binary Stream Integrity**: Never use `-t` (pseudo-TTY) with `docker exec` when piping `pg_dump`, `pg_dumpall`, or tar streams. Pseudo-TTY allocation injects CRLF byte corruption (`\r\n`) and terminal control codes into binary streams, rendering archives un-restorable. Always use `docker exec -i` (or `docker exec -i=false`).

---

## 2. Zero-Downtime / Zero-Data-Loss Migration Guide

This procedure migrates an existing single-instance `ki-basis` deployment (which currently contains community fundraiser/Equinox data) into the dual-instance architecture. Community receives the existing state; Private starts with a clean slate.

```
+---------------------------------------------------------------------------------------+
|                                  MIGRATION WORKFLOW                                   |
|                                                                                       |
|  [Step 1: Quiesce Stack] ──► Gracefully stop application writers                      |
|                                        │                                              |
|  [Step 2: Full Snapshot] ──► pg_dumpall + Tar all 10 legacy named volumes             |
|                                        │                                              |
|  [Step 3: Verification]  ──► Validate SHA256 checksums of backup archives              |
|                                        │                                              |
|  [Step 4: Provisioning]  ──► Migrate legacy volumes to ki-basis-community-*           |
|                                        │                                              |
|  [Step 5: Config Setup]  ──► Generate .env.community & .env.private                   |
|                                        │                                              |
|  [Step 6: Launch & Test] ──► Bring up Community, verify; Bring up Private, verify    |
+---------------------------------------------------------------------------------------+
```

### Step 1: Quiesce Application Writers
To prevent transactional writes during migration, gracefully stop the single-instance stack:
```powershell
cd C:\GitDev\apexai-os-meta\ki-basis

# Stop web applications while keeping PostgreSQL and Valkey alive for dumping
docker compose stop firefly paperless openproject hermes nginx
```

### Step 2: Full Pre-Migration Snapshot
Create a dedicated migration backup directory and dump all PostgreSQL databases:

> **CRITICAL TTY SAFETY INVARIANT**:
> Never use the `-t` (pseudo-TTY) flag with `docker exec` when piping output to files or stream pipelines (such as `pg_dumpall`, `pg_dump -Fc`, or tar pipelines). Pseudo-TTY allocation converts Unix newline bytes (`\n`, `0x0A`) to Carriage Return + Line Feed (`\r\n`, `0x0D 0x0A`) and can inject terminal escape sequences or line wrapping. For custom compressed binary archives (`-Fc`), this silently corrupts the archive header and compression frame, causing fatal errors on restore (`pg_restore: error: did not find expected signature in header; corrupted file or not a dump file`). Always use `docker exec -i` (interactive stdin pass-through) without `-t`.

```bash
MIGRATION_DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/tmp/ki-basis-migration-${MIGRATION_DATE}"
mkdir -p "${BACKUP_DIR}"

# 1. Logical PostgreSQL full cluster dump (strictly -i, no -t)
docker exec -i ki-basis-postgres pg_dumpall -U postgres > "${BACKUP_DIR}/postgres_full_dump.sql"

# 2. Individual compressed database dumps (strictly -i, no -t to avoid binary corruption)
for db in firefly paperless openproject; do
  docker exec -i ki-basis-postgres pg_dump -U postgres -d "$db" -Fc > "${BACKUP_DIR}/${db}_custom.dump"
done

# 3. Stop remaining data services
docker compose down
```

Archive legacy Docker named volumes using a lightweight helper container:
```bash
VOLUMES=(
  "ki-basis-postgres-data"
  "ki-basis-valkey-data"
  "ki-basis-firefly-upload"
  "ki-basis-paperless-data"
  "ki-basis-paperless-media"
  "ki-basis-paperless-export"
  "ki-basis-paperless-consume"
  "ki-basis-openproject-assets"
  "ki-basis-hermes-data"
  "ki-basis-hermes-workspaces"
)

for vol in "${VOLUMES[@]}"; do
  echo "Archiving volume: ${vol}..."
  docker run --rm \
    -v "${vol}:/source:ro" \
    -v "${BACKUP_DIR}:/backup" \
    alpine:3.20 tar -czf "/backup/${vol}.tar.gz" -C /source .
done

# Generate manifest checksums
cd "${BACKUP_DIR}" && sha256sum * > SHA256SUMS.txt
echo "[SUCCESS] Migration snapshot verified at ${BACKUP_DIR}"
```

### Step 3: Clone Named Volumes to Community Namespace
Since the single-instance stack contains Equinox and Safer Space e.V. records, clone its volumes directly into the `ki-basis-community` namespace:
```bash
for vol in "${VOLUMES[@]}"; do
  # Replace legacy 'ki-basis-' prefix with 'ki-basis-community-'
  TARGET_VOL=$(echo "$vol" | sed 's/^ki-basis-/ki-basis-community-/')
  echo "Cloning ${vol} -> ${TARGET_VOL}..."
  
  # Create new destination volume
  docker volume create "${TARGET_VOL}"
  
  # Restore data from archive
  docker run --rm \
    -v "${TARGET_VOL}:/target" \
    -v "${BACKUP_DIR}:/backup:ro" \
    alpine:3.20 sh -c "tar -xzf /backup/${vol}.tar.gz -C /target"
done
```

### Step 4: Synchronize PostgreSQL Credentials for Cloned Community Cluster
When PostgreSQL boots against an existing/cloned volume (`ki-basis-community-postgres-data`), the container entrypoint (`/docker-entrypoint-initdb.d/01-init-databases.sh`) is automatically skipped because the database cluster is already initialized. Therefore, all internal database user accounts (`openproject_app`, `firefly_app`, `paperless_app`, `postgres`) retain their legacy passwords from the single-instance deployment.

However, `.env.community` defines distinct, newly generated high-entropy passwords (`OPENPROJECT_DB_PASSWORD`, `FIREFLY_DB_PASSWORD`, `PAPERLESS_DB_PASSWORD`, `POSTGRES_PASSWORD`). Without password synchronization, application containers will fail database authentication upon startup and enter crash loops (`password authentication failed for user "openproject_app"`).

To synchronize the database users to match `.env.community`:

#### In Linux / WSL2 (Bash):
```bash
cd /c/GitDev/apexai-os-meta/ki-basis

# 1. Temporarily bring up community PostgreSQL only
docker compose -p ki-basis-community --env-file .env.community up -d postgres

# 2. Wait until PostgreSQL is ready to accept connections
until docker exec -i ki-basis-community-postgres pg_isready -U postgres; do
  echo "Waiting for community PostgreSQL..."
  sleep 2
done

# 3. Synchronize passwords directly from .env.community
source .env.community
docker exec -i ki-basis-community-postgres psql -U postgres <<EOSQL
ALTER USER postgres WITH PASSWORD '${POSTGRES_PASSWORD}';
ALTER USER openproject_app WITH PASSWORD '${OPENPROJECT_DB_PASSWORD}';
ALTER USER firefly_app WITH PASSWORD '${FIREFLY_DB_PASSWORD}';
ALTER USER paperless_app WITH PASSWORD '${PAPERLESS_DB_PASSWORD}';
EOSQL

echo "[SUCCESS] PostgreSQL credentials synchronized with .env.community"
```

#### In Windows (PowerShell 7+):
```powershell
cd C:\GitDev\apexai-os-meta\ki-basis

# 1. Temporarily bring up community PostgreSQL only
docker compose -p ki-basis-community --env-file .env.community up -d postgres

# 2. Wait until PostgreSQL is ready
do {
    Start-Sleep -Seconds 2
    $null = docker exec -i ki-basis-community-postgres pg_isready -U postgres 2>&1
} while ($LASTEXITCODE -ne 0)

# 3. Synchronize passwords from .env.community
$envMap = @{}
Get-Content .env.community | ForEach-Object {
    $line = $_.Trim()
    if ($line -and -not $line.StartsWith("#") -and $line.Contains("=")) {
        $k, $v = $line.Split("=", 2)
        $envMap[$k.Trim()] = $v.Trim().Trim('"').Trim("'")
    }
}

docker exec -i ki-basis-community-postgres psql -U postgres -c "ALTER USER postgres WITH PASSWORD '$($envMap['POSTGRES_PASSWORD'])';"
docker exec -i ki-basis-community-postgres psql -U postgres -c "ALTER USER openproject_app WITH PASSWORD '$($envMap['OPENPROJECT_DB_PASSWORD'])';"
docker exec -i ki-basis-community-postgres psql -U postgres -c "ALTER USER firefly_app WITH PASSWORD '$($envMap['FIREFLY_DB_PASSWORD'])';"
docker exec -i ki-basis-community-postgres psql -U postgres -c "ALTER USER paperless_app WITH PASSWORD '$($envMap['PAPERLESS_DB_PASSWORD'])';"

Write-Host "[SUCCESS] PostgreSQL credentials synchronized with .env.community" -ForegroundColor Green
```

### Step 5: Environment Configuration Verification
Ensure `.env.community` and `.env.private` are populated:
```powershell
# Ensure private and community environment files exist
Test-Path C:\GitDev\apexai-os-meta\ki-basis\.env.community
Test-Path C:\GitDev\apexai-os-meta\ki-basis\.env.private
```

### Step 6: Launch Community Stack and Verify Integrity
```powershell
cd C:\GitDev\apexai-os-meta\ki-basis

# Bring up Community stack
docker compose -p ki-basis-community --env-file .env.community up -d

# Wait for healthchecks to pass
docker compose -p ki-basis-community ps

# Verify Community endpoints on 908x
curl -fs -I http://127.0.0.1:9084/healthz
curl -fs -I http://127.0.0.1:9082/health_checks/default
```

### Step 7: Initialize Fresh Private Stack
```powershell
# Bring up Private stack (creates fresh ki-basis-private-* volumes automatically)
docker compose -p ki-basis-private --env-file .env.private up -d

# Wait for healthchecks to pass
docker compose -p ki-basis-private ps

# Verify Private endpoints on 808x
curl -fs -I http://127.0.0.1:8084/healthz
curl -fs -I http://127.0.0.1:8082/health_checks/default
```

---

## 3. Daily Operations Guide

### 3.1 Common CLI Commands

#### Starting Instances
```powershell
# Start Private Stack only:
docker compose -p ki-basis-private --env-file .env.private up -d

# Start Community Stack only:
docker compose -p ki-basis-community --env-file .env.community up -d

# Or use the automated PowerShell runner:
.\scripts\start-ki-basis.ps1 -Instance private
.\scripts\start-ki-basis.ps1 -Instance community
.\scripts\start-ki-basis.ps1 -Instance all
```

#### Stopping Instances
```powershell
# Gracefully stop Private Stack without deleting volumes:
docker compose -p ki-basis-private --env-file .env.private stop

# Gracefully stop Community Stack:
docker compose -p ki-basis-community --env-file .env.community stop

# Tear down containers and bridge network (leaves volumes intact):
docker compose -p ki-basis-private --env-file .env.private down
docker compose -p ki-basis-community --env-file .env.community down
```

#### Inspecting Status & Logs
```powershell
# View running status of Private containers:
docker compose -p ki-basis-private ps

# View running status of Community containers:
docker compose -p ki-basis-community ps

# Tail logs of a specific service:
docker compose -p ki-basis-private logs -f openproject
docker compose -p ki-basis-community logs -f hermes

# Resource consumption snapshot across all containers:
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.NetIO}}"
```

### 3.2 Service Access Map

| Institutional Domain | Service | Host URL | Authentication / Notes |
| :--- | :--- | :--- | :--- |
| **Private Entrepreneurship** | Edge Dashboard | `http://127.0.0.1:8084` | Links to all Private services |
| | OpenProject | `http://127.0.0.1:8082` | Admin / Configured user |
| | Paperless-ngx | `http://127.0.0.1:8010` | Admin credentials from `.env.private` |
| | Firefly III | `http://127.0.0.1:8086` | Site owner login |
| | Hermes Dashboard | `http://127.0.0.1:9119` | Basic Auth from `.env.private` |
| | Hermes REST API | `http://127.0.0.1:8642/v1/...` | `Authorization: Bearer $HERMES_API_SERVER_KEY` |
| **Community Operations** | Edge Dashboard | `http://127.0.0.1:9084` | Links to all Community services |
| | OpenProject | `http://127.0.0.1:9082` | Safer Space e.V. Work packages |
| | Paperless-ngx | `http://127.0.0.1:9010` | Event receipts & tax invoices |
| | Firefly III | `http://127.0.0.1:9086` | GLS Bank & 4-Sphere Accounting |
| | Hermes Dashboard | `http://127.0.0.1:9219` | Basic Auth from `.env.community` |
| | Hermes REST API | `http://127.0.0.1:9642/v1/...` | `Authorization: Bearer $HERMES_API_SERVER_KEY` |

---

## 4. Backup & Disaster Recovery Runbook

### 4.1 Automated Backup Script Usage
The backup script accepts the target instance as an argument (`private` or `community`):

```bash
# Backup Community Stack
./scripts/backup-stack.sh community

# Backup Private Stack
./scripts/backup-stack.sh private
```

### 4.2 Standard Backup Procedure (Manual Steps)

> **CRITICAL TTY SAFETY NOTE**: Always use `docker exec -i` (strictly no `-t`) when redirecting database dumps. PTY allocation injects CRLF (`\r\n`) sequences and terminal escape codes that corrupt binary archive streams (`pg_dump -Fc`).

```bash
INSTANCE="community"   # or "private"
DATE_TAG=$(date +%Y%m%d_%H%M%S)
BACKUP_ROOT="/backups/ki-basis-${INSTANCE}/${DATE_TAG}"
mkdir -p "${BACKUP_ROOT}"

# 1. Hot PostgreSQL cluster dump (strictly -i, no -t)
docker exec -i "ki-basis-${INSTANCE}-postgres" pg_dumpall -U postgres > "${BACKUP_ROOT}/postgres_all.sql"

# 2. Hot custom-format database dumps (strictly -i, no -t)
for db in firefly paperless openproject; do
  docker exec -i "ki-basis-${INSTANCE}-postgres" pg_dump -U postgres -d "$db" -Fc > "${BACKUP_ROOT}/${db}.dump"
done

# 3. Snapshot persistent asset and state volumes
VOL_PREFIX="ki-basis-${INSTANCE}"
VOL_NAMES=(
  "valkey-data"
  "firefly-upload"
  "paperless-data"
  "paperless-media"
  "paperless-export"
  "paperless-consume"
  "openproject-assets"
  "hermes-data"
  "hermes-workspaces"
)

for vol_suffix in "${VOL_NAMES[@]}"; do
  vol="${VOL_PREFIX}-${vol_suffix}"
  echo "Dumping ${vol}..."
  docker run --rm \
    -v "${vol}:/data:ro" \
    -v "${BACKUP_ROOT}:/backup" \
    alpine:3.20 tar -czf "/backup/${vol}.tar.gz" -C /data .
done

# 4. Generate SHA256 integrity manifest
cd "${BACKUP_ROOT}" && sha256sum * > SHA256SUMS.txt
echo "[SUCCESS] Backup completed: ${BACKUP_ROOT}"
```

### 4.3 Disaster Recovery / Restore Procedure

> **CRITICAL RECOVERY INVARIANT: CLEAN CLUSTER RE-INITIALIZATION**  
> Never pipe `postgres_all.sql` into an existing, populated PostgreSQL cluster. If target databases (`firefly`, `paperless`, `openproject`) already exist, `psql` will fail with duplicate key violations and relation collision errors. The PostgreSQL data volume must be wiped (`docker volume rm ...`) and initialized as a fresh, empty cluster before piping the SQL restore.
>
> In addition, ensure that search index and runtime state volumes (`paperless-data` containing SQLite/classifier state, and `hermes-workspaces` containing AI workspaces) are restored alongside document media and attachments.

```bash
INSTANCE="community"   # or "private"
BACKUP_ARCHIVE_DIR="/backups/ki-basis-${INSTANCE}/20260907_120000"
VOL_PREFIX="ki-basis-${INSTANCE}"

# 1. Quiesce the target instance and wipe containers & network
docker compose -p "ki-basis-${INSTANCE}" --env-file ".env.${INSTANCE}" down

# 2. Clean the postgres-data volume to avoid collision errors
echo "Re-initializing fresh PostgreSQL volume for clean cluster restore..."
docker volume rm "${VOL_PREFIX}-postgres-data" 2>/dev/null || true
docker volume create "${VOL_PREFIX}-postgres-data"

# 3. Re-create and populate all application state volumes from archive
RESTORE_VOLUMES=(
  "valkey-data"
  "firefly-upload"
  "paperless-data"
  "paperless-media"
  "paperless-export"
  "paperless-consume"
  "openproject-assets"
  "hermes-data"
  "hermes-workspaces"
)

for vol_suffix in "${RESTORE_VOLUMES[@]}"; do
  vol="${VOL_PREFIX}-${vol_suffix}"
  archive_path="${BACKUP_ARCHIVE_DIR}/${vol}.tar.gz"
  
  if [[ -f "${archive_path}" ]]; then
    echo "Restoring ${vol} from ${archive_path}..."
    docker volume rm "${vol}" 2>/dev/null || true
    docker volume create "${vol}"
    docker run --rm \
      -v "${vol}:/target" \
      -v "${BACKUP_ARCHIVE_DIR}:/backup:ro" \
      alpine:3.20 tar -xzf "/backup/${vol}.tar.gz" -C /target
  else
    echo "[SKIP] Archive not found for optional volume: ${archive_path}"
  fi
done

# 4. Start PostgreSQL and Valkey on the fresh cluster
docker compose -p "ki-basis-${INSTANCE}" --env-file ".env.${INSTANCE}" up -d postgres valkey

# Wait for PostgreSQL to become fully ready to accept queries
until docker exec -i "ki-basis-${INSTANCE}-postgres" pg_isready -U postgres; do
  echo "Waiting for postgres to accept connections..."
  sleep 2
done

# 5. Restore PostgreSQL cluster dump cleanly (without collisions)
echo "Restoring logical database cluster from ${BACKUP_ARCHIVE_DIR}/postgres_all.sql..."
docker exec -i "ki-basis-${INSTANCE}-postgres" psql -U postgres < "${BACKUP_ARCHIVE_DIR}/postgres_all.sql"

# 6. Bring up remaining application services
docker compose -p "ki-basis-${INSTANCE}" --env-file ".env.${INSTANCE}" up -d

# 7. Verify endpoints
docker compose -p "ki-basis-${INSTANCE}" --env-file ".env.${INSTANCE}" ps
echo "[SUCCESS] Disaster recovery completed for ${INSTANCE} instance."
```

---

## 5. Troubleshooting & Failure Recovery

### Symptom 1: Port Collision / `WSAEADDRINUSE` / `port is already allocated`
- **Error Output**:
  `Error response from daemon: driver failed programming external connectivity on endpoint ... Bind for 127.0.0.1:8082 failed: port is already allocated`
- **Root Cause**:
  Another process (or a zombie container from a prior test) is already listening on the requested port.
- **Diagnostic Command**:
  ```powershell
  # Find which PID owns the colliding port (e.g. 8082)
  Get-NetTCPConnection -LocalPort 8082 | Select-Object LocalAddress, LocalPort, OwningProcess, State
  Get-Process -Id (Get-NetTCPConnection -LocalPort 8082).OwningProcess
  ```
- **Remediation**:
  1. Check if the alternate stack is accidentally using the same port band in `.env`:
     Private must use 808x; Community must use 908x.
  2. Terminate zombie containers:
     `docker compose -p ki-basis-private down` and `docker compose -p ki-basis-community down`.

### Symptom 2: OpenProject Container Exits with `exit status 1`
- **Diagnostic Command**:
  `docker logs ki-basis-private-openproject --tail 100`
- **Checklist**:
  1. **Storage Substrate Check**:
     Confirm that `openproject_assets` is a Docker named volume and NOT a bind mount on `/mnt/c`:
     `docker inspect ki-basis-private-openproject --format '{{json .Mounts}}'`
  2. **Secret Key Check**:
     Ensure `OPENPROJECT_SECRET_KEY_BASE` is defined and has at least 64 hex characters in `.env.private` / `.env.community`.
  3. **Database Timeout**:
     Verify `PG_STARTUP_WAIT_TIME=60` is present.
  4. **Puma Concurrency**:
     Verify `OPENPROJECT_WEB_WORKERS=1` is present.

### Symptom 3: 350% Runaway CPU Usage on Host
- **Diagnostic Command**:
  `docker stats --no-stream`
- **Checklist**:
  1. **Identify High-CPU Container**: Check if any container exceeds 5% CPU at idle.
  2. **Audit Bind Mounts**: Verify no container has active 9P mounts on `/mnt/c` for database or asset storage:
     ```bash
     docker inspect $(docker ps -q) --format '{{.Name}}: {{range .Mounts}}{{.Source}} -> {{.Destination}}{{println}}{{end}}' | grep -E '/mnt/c'
     ```
     Only `./docker/postgres/init` and `./docker/nginx` should appear as read-only mounts.
  3. **Docker Desktop GUI**: Close the electron dashboard window (`Docker Desktop.exe`). The background service `com.docker.backend.exe` will continue executing headlessly.

### Symptom 4: Telegram API 409 Conflict Error
- **Error Output**:
  `telegram.error.Conflict: Conflict: terminated by other getUpdates request; make sure that only one bot instance is running`
- **Root Cause**:
  Both Private and Community stacks are attempting to poll the Telegram API using the identical `TELEGRAM_BOT_TOKEN`.
- **Remediation**:
  Leave `TELEGRAM_BOT_TOKEN` blank in `.env.private`. The Private stack Hermes operates strictly via loopback REST API (`http://127.0.0.1:8642`). The Community stack retains the active Telegram bot token for volunteer intake.

---

## 6. Audit & Verification Checklist

Before certifying any dual-instance deployment for production:
- [ ] Both `ki-basis-private` and `ki-basis-community` run concurrently (`docker ps` shows 14 containers).
- [ ] All 14 containers report `healthy` or running status with steady-state CPU < 5% aggregate.
- [ ] `docker volume ls` lists 20 distinct named volumes (10 `ki-basis-private-*` and 10 `ki-basis-community-*`).
- [ ] `netstat -ano` shows PostgreSQL (5432) and Valkey (6379) are NOT listening on host interfaces.
- [ ] All published web ports (808x and 908x) bind strictly to `127.0.0.1`.
- [ ] Cross-stack DNS lookup (`ki-basis-private-hermes` querying `community-paperless`) fails with `NXDOMAIN`.
- [ ] Automated verification script (`python scripts/verify_dual_isolation.py`) passes with 0 errors.
