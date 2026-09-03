# Comprehensive AI Handover & Architectural Review Dossier (`ki-basis`)

**Role**: AI Engineering Handover & Integrity Control Dossier  
**Stack**: `ki-basis` (PostgreSQL + pgvector, Valkey, Firefly III, Paperless-ngx, OpenProject, Nginx Edge, Hermes Agent)  
**Host Target**: Windows 11 Pro (Docker Desktop Hyper-V Linux VM backend)  
**Timestamp**: 2026-09-03T08:38:00+02:00  
**Status**: All 8 Correction Modules (C1–C8) Executed; 17/17 Independent Auditor PASS; repository-state claims must be verified against live Git; this dossier is tracked and must not be used as no-push evidence.

---

## Part 1: External Runtime State Manifest (State Outside Git)

This section details all external runtime states, host environments, secrets, and validation receipts that cannot be seen solely by inspecting the Git tree.

### 1.1 Docker Engine & Host Environment
* **Target Docker Engine ID**: `e9c8ec3c-5306-43e3-8b37-a0803aa830d2`
* **Docker Client / Server Version**: `29.7.2` (API `1.55`)
* **Host OS**: Windows 11 Pro (OS Build 26100.x)
* **Docker Host Pipe**: `npipe:////./pipe/docker_engine`
* **Target VM Hypervisor**: Hyper-V Linux VM (`7.0.12-linuxkit x86_64`)
* **Source WSL Status**: `wsl.exe -l -v` confirmed as `Ubuntu Stopped 2` (Zero background CPU/RAM usage; pure cold rollback archive).

### 1.2 Untracked Real Secrets & Configuration (`ki-basis/.env`)
* **File Path**: `C:\GitDev\apexai-os-meta\ki-basis\.env` (Strictly untracked; excluded via `.gitignore`).
* **Paperless API Token (Rotated in C1)**: `<REDACTED_PAPERLESS_API_TOKEN>`
* **Paperless Secret Key**: High-entropy secret key configured; verified non-empty fail-closed.
* **Internal Database Credentials**: `POSTGRES_PASSWORD`, `FIREFLY_DB_PASSWORD`, `PAPERLESS_DB_PASSWORD`, `OPENPROJECT_DB_PASSWORD` set to unique random 32-character hex strings.
* **OpenProject Secret Key Base**: 64-character random hex string.

### 1.3 Verified Host Backup Artifacts
* **Host Backup Directory**: `C:\Users\gehma\ki-basis-backups\20260902T203055Z`
* **Artifacts on Host**:
  1. `manifest.txt` (Coverage and timestamp manifest)
  2. `compose-snapshot.yaml` (Running Compose spec)
  3. `postgres/globals.sql` (Global roles and cluster definitions)
  4. `postgres/firefly.dump` (PostgreSQL custom format dump)
  5. `postgres/paperless.dump` (PostgreSQL custom format dump)
  6. `postgres/openproject.dump` (PostgreSQL custom format dump)
  7. `volumes/valkey_data.tar.gz` (Valkey cache dump)
  8. `volumes/firefly_upload.tar.gz` (Firefly user uploads)
  9. `volumes/paperless_data.tar.gz` (Paperless search index & SQLite meta)
  10. `volumes/paperless_media.tar.gz` (Paperless original & archive PDFs)
  11. `volumes/paperless_export.tar.gz` (Paperless export storage)
  12. `volumes/paperless_consume.tar.gz` (Paperless consumption intake)
  13. `volumes/openproject_assets.tar.gz` (OpenProject attachments)
  14. `volumes/hermes_data.tar.gz` (`ki-basis-hermes-data` volume)
  15. `volumes/hermes_workspaces.tar.gz` (`ki-basis-hermes-workspaces` volume)

### 1.4 Real-Product Paperless Document Verification Receipt
* **Document ID**: `1`
* **Document Title**: `Antigravity M5 Test Document`
* **Physical File Size**: `279 bytes`
* **Verified Document SHA256**: `9fa30ebc25d8864f1d4eb61e38953150242278cb769a7c35868ab305e5542b82`
* **Negative Auth Test**: Request with revoked token returned `HTTP 401 Unauthorized` (`{"detail":"Invalid token."}`).
* **Positive Auth Test**: Request with rotated token returned `HTTP 200 OK` with binary download payload matching the exact SHA256 digest.

### 1.5 Local Git Commit History
* **Starting Commit**: `251768b1eed96c748bee6372cbada522b77dc04e`
* **Commit 1 (`0eb4dc56`)**: `fix(security): sanitize exposed Paperless verification token` (Redacted exposed token in `apex-meta/Alpine/Iteration2/VerificationAG.md:156`).
* **Commit 2 (`ac5e1c83`)**: `fix(ki-basis): harden target scripts and record Docker Desktop acceptance report` (Updated `backup-stack.sh`, `restore-test-paperless.sh`, `verify-stack.sh`, labeled `INTEGRATION-ACCEPTANCE-REPORT.md`, added `TARGET-ACCEPTANCE-REPORT.md`).
* **Remote Status**: Historical no-push intent is superseded. Verify current branch/remote state with live Git; this dossier itself is tracked and therefore is not evidence that no push occurred.

---

## Part 2: Self-Check of Workflow Inefficiencies & Root-Cause Lessons

During this operational cycle, multiple platform-specific edge cases and friction points were identified and resolved:

### 2.1 The Windows Named Pipe / Stdin Pipe Stall Trap
* **Symptom**: Commands like `cat dump.sql | docker exec -i container psql` or `cat volume.tar.gz | docker run -i ...` hung indefinitely in Git Bash / PowerShell on Windows.
* **Root Cause**: On Windows, when standard input is piped across the MSYS/Cygwin bridge into the native `docker.exe` Windows binary communicating over `\\.\pipe\docker_engine`, the Windows named-pipe client does not cleanly propagate the EOF (End-Of-File) signal when the upstream command finishes. As a result, `docker exec -i` waits indefinitely for more stdin bytes.
* **Resolution & Best Practice**: 
  1. Eliminate stdin piping for data ingestion.
  2. Use native `docker cp "$LOCAL_FILE" "${CONTAINER}:/tmp/file"` (which uses Docker Engine’s internal HTTP/REST streaming mechanism, completely bypassing OS stdin pipes).
  3. Execute commands with `docker exec -i=false ${CONTAINER} command /tmp/file`.
  4. Cleanup temporary container files afterwards.

### 2.2 Carriage Return (`\r`) Subshell Poisoning
* **Symptom**: Bash subshells like `cid=$(docker create ...)` or `PG_IMAGE=$(docker inspect ...)` produced container IDs or image names that caused subsequent `docker` commands to hang or fail with path errors.
* **Root Cause**: Native Windows binaries output CRLF (`\r\n`). In a Bash subshell `$(...)`, the `\n` is stripped by POSIX rules, but the trailing `\r` remains attached to the string. When Bash passes `xyz\r` as a container name or path, the Windows Docker client treats the carriage return as part of the argument.
* **Resolution & Best Practice**: Always strip carriage returns explicitly when capturing output from native Windows CLI tools:
  ```bash
  cid="$(docker create ... | tr -d '\r\n[:space:]')"
  ```

### 2.3 Path Translation Mismatch: MSYS `/c/` vs Windows `C:/`
* **Symptom**: `docker cp /c/Users/...` failed with `GetFileAttributesEx C:\c: The system cannot find the file specified`.
* **Root Cause**: MSYS/Git Bash uses POSIX mount paths (`/c/Users/...`), but `docker.exe` is a native Windows binary that expects Win32 drive formats (`C:\Users\...` or `C:/Users/...`). Passing `/c/` causes Docker to interpret `/c` as a directory on `C:\`.
* **Resolution & Best Practice**: Separate bash path variables from Windows path variables:
  ```bash
  BACKUP_DIR_BASH="$(cd "$BACKUP_DIR" && pwd)"
  BACKUP_DIR_WIN="$(cygpath -m "$BACKUP_DIR_BASH" 2>/dev/null || echo "$BACKUP_DIR_BASH")"
  ```

### 2.4 Alpine Helper Image Entrypoint Hijacking
* **Symptom**: `docker start -a "$cid"` hung when using `valkey/valkey:8.0.2-alpine` as a temporary tarball extraction helper.
* **Root Cause**: The default Docker image entrypoint for `valkey` is `docker-entrypoint.sh`. When arguments `sh -c "tar ..."` were appended, the entrypoint launched `valkey-server` in daemon mode instead of running `sh`.
* **Resolution & Best Practice**: When using utility/service images as extraction helpers, explicitly override the entrypoint:
  ```bash
  docker create --entrypoint sh -v "$vol:/dst" "$HELPER_IMAGE" -c "tar -C /dst -xzf /tmp/vol.tar.gz"
  ```

### 2.5 `DOCKER_API_VERSION` Downgrade Failures
* **Symptom**: Forcing `export DOCKER_API_VERSION=1.47` or `1.45` caused the Docker 29.7.2 daemon to return `500 Internal Server Error` on API version queries.
* **Resolution & Best Practice**: Do not hardcode or downgrade `DOCKER_API_VERSION`. Allow the Docker client and daemon to negotiate the highest mutually supported API version automatically.

### 2.6 Windows Shell Handle Bloat (`explorer.exe`)
* **Symptom**: Laptop UI becomes unresponsive; left/right clicks, folder opening, and browser interactions experience a 2–5 second freeze despite low CPU and 13+ GB free RAM.
* **Root Cause**: Extensive file operations, Git commits, and container activity across an 18+ hour uptime caused `explorer.exe` to accumulate **9,557 open handles** and **205 background threads**. Context menu queries synchronously iterated over these handles, causing input queue delay.
* **Resolution & Best Practice**: Periodically restart `explorer.exe` (`Stop-Process -Name explorer -Force`) or reboot the host OS.

---

## Part 3: Researched Best Practices & Future Optimization Architecture

Based on industry standards for multi-tier microservice stacks on Windows Docker environments, the following enhancements are recommended for future iterations:

### 3.1 Container-Level Hard Resource Ceilings (`compose.yaml`)
Currently, containers run without hard memory/CPU caps. While lightweight at idle, background workers (Ruby Puma, OCR, Celery) can spike under load. Adding explicit `deploy.resources.limits` prevents any single container from monopolizing RAM:

```yaml
services:
  postgres:
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '1.0'

  valkey:
    deploy:
      resources:
        limits:
          memory: 256M
          cpus: '0.5'

  paperless:
    deploy:
      resources:
        limits:
          memory: 1024M
          cpus: '1.5'
    environment:
      - PAPERLESS_WORKERS=1
      - PAPERLESS_THREADS=1

  openproject:
    deploy:
      resources:
        limits:
          memory: 1536M
          cpus: '2.0'
    environment:
      - OPENPROJECT_WEB_WORKERS=1

  firefly:
    deploy:
      resources:
        limits:
          memory: 512M
          cpus: '0.5'

  nginx:
    deploy:
      resources:
        limits:
          memory: 128M
          cpus: '0.25'

  hermes:
    deploy:
      resources:
        limits:
          memory: 1024M
          cpus: '1.5'
```

### 3.2 Worker Concurrency Optimization
* **Paperless-ngx**: Tesseract OCR and ImageMagick can exhaust CPU and memory during multi-page PDF ingestion. Setting `PAPERLESS_WORKERS=1` and `PAPERLESS_THREADS=1` guarantees serial document processing with predictable low memory consumption.
* **OpenProject**: The Puma web server defaults to multiple worker processes. Setting `OPENPROJECT_WEB_WORKERS=1` halves OpenProject's base RAM usage (~1.2 GB down to ~600 MB) while remaining fully responsive for single-operator workloads.

### 3.3 PostgreSQL & Valkey Buffer Sizing
* **PostgreSQL**: Configure `shared_buffers = 128MB` and `work_mem = 16MB` in custom postgres configuration to prevent Postgres from caching excessive pages.
* **Valkey**: Set `maxmemory 128mb` and `maxmemory-policy allkeys-lru` to enforce a hard ceiling on cache retention.

---

## Part 4: 17-Point Audit Matrix Quick Reference

| # | Verification Gate | Verdict | Evidence Anchor |
|---|---|:---:|---|
| **1** | Target Engine ID `e9c8ec3c-5306-43e3-8b37-a0803aa830d2` | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:5` |
| **2** | Target Backend (Docker Desktop Hyper-V VM) | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:4` |
| **3** | WSL Source Isolation (`Ubuntu Stopped 2`) | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:69-71` |
| **4** | Single Compose Project `ki-basis` | **PASS** | `ki-basis/compose.yaml:1` |
| **5** | 7 Running & Healthy Containers | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:13-21` |
| **6** | Port Isolation (DB 5432 & Cache 6379 Internal Only) | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:34-37` |
| **7** | Docker Socket Isolation (Hermes has no docker.sock) | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:38` |
| **8** | Network Topology (`ki-basis-net` bridge) | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:6` |
| **9** | pgvector acceptance scope (current designated/application DB checks; template DBs are not an application requirement) | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:27-32` |
| **10** | Valkey PING / PONG Healthcheck | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:16` |
| **11** | Nginx Edge Health (`GET :8084/healthz` -> HTTP 200) | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:43` |
| **12** | Application UIs (8086, 8010, 8082, 9119 -> HTTP 200) | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:44-47` |
| **13** | Paperless Negative Auth (Revoked Token -> HTTP 401) | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:52` |
| **14** | Paperless Positive Auth & Checksum (SHA256 Match) | **PASS** | `TARGET-ACCEPTANCE-REPORT.md:53-56` |
| **15** | Target Backup Script Coverage (Hermes Named Volumes) | **PASS** | `ki-basis/scripts/backup-stack.sh:32-33` |
| **16** | Security Sanitization (`VerificationAG.md:156` Clean) | **PASS** | `0eb4dc56` (`VerificationAG.md:156`) |
| **17** | Documentation Truth (Pre-Migration vs Target Reports) | **PASS** | `ac5e1c83` |