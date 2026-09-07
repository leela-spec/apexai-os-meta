# Handoff Report: Codebase & Service Survey (`ki-basis`)

**Agent:** explorer_survey_2  
**Working Directory:** `C:\GitDev\apexai-os-meta\.agents\explorer_survey_2`  
**Parent Orchestrator:** orchestrator_1 (`96367b83-1fd0-4e20-8a61-cc9640b72e38`)  
**Date:** 2026-09-07  
**Status:** Hard Handoff (Task Complete)

---

## 1. Observation

1. **Top-Level Stack Topology (`ki-basis/compose.yaml`)**:
   - `name: ki-basis` (line 1).
   - Single bridge network `ki-basis-net` parameterized as `name: ${KI_NETWORK_NAME:-ki-basis-net}` (lines 4–6).
   - 10 named volumes with hardcoded global names (lines 8–29):
     - `postgres_data` -> `name: ki-basis-postgres-data` (lines 9–10)
     - `valkey_data` -> `name: ki-basis-valkey-data` (lines 11–12)
     - `firefly_upload` -> `name: ki-basis-firefly-upload` (lines 13–14)
     - `paperless_data` -> `name: ki-basis-paperless-data` (lines 15–16)
     - `paperless_media` -> `name: ki-basis-paperless-media` (lines 17–18)
     - `paperless_export` -> `name: ki-basis-paperless-export` (lines 19–20)
     - `paperless_consume` -> `name: ki-basis-paperless-consume` (lines 21–22)
     - `openproject_assets` -> `name: ki-basis-openproject-assets` (lines 23–24)
     - `hermes_data` -> `name: ki-basis-hermes-data` (lines 25–26)
     - `hermes_workspaces` -> `name: ki-basis-hermes-workspaces` (lines 27–28)
   - 7 defined services with hardcoded container names (lines 31–216):
     - `postgres`: `container_name: ki-basis-postgres` (line 33), image `pgvector/pgvector@sha256:ccc6e83d...` (line 32)
     - `valkey`: `container_name: ki-basis-valkey` (line 62), image `valkey/valkey@sha256:f110e5df...` (line 61)
     - `firefly`: `container_name: ki-basis-firefly` (line 78), image `fireflyiii/core@sha256:ae69fdd9...` (line 77)
     - `paperless`: `container_name: ki-basis-paperless` (line 105), image `ghcr.io/paperless-ngx/paperless-ngx@sha256:5ab4f4f9...` (line 104)
     - `openproject`: `container_name: ki-basis-openproject` (line 144), image `openproject/openproject@sha256:73d4ee76...` (line 143)
     - `nginx`: `container_name: ki-basis-nginx` (line 164), image `nginx@sha256:65645c7b...` (line 163)
     - `hermes`: `container_name: ki-basis-hermes` (line 185), image `nousresearch/hermes-agent@sha256:09d743f5...` (line 184)

2. **Published Host Ports in `compose.yaml`**:
   - `firefly`: `"127.0.0.1:${FIREFLY_HOST_PORT:-8086}:8080"` (line 81)
   - `paperless`: `"127.0.0.1:${PAPERLESS_HOST_PORT:-8010}:8000"` (line 108)
   - `openproject`: `"127.0.0.1:${OPENPROJECT_HOST_PORT:-8082}:80"` (line 147)
   - `nginx`: `"127.0.0.1:${NGINX_HOST_PORT:-8084}:80"` (line 167)
   - `hermes`: `"127.0.0.1:${HERMES_GATEWAY_HOST_PORT:-8642}:8642"` (line 189) and `"127.0.0.1:${HERMES_DASHBOARD_HOST_PORT:-9119}:9119"` (line 190)
   - `postgres` (5432) and `valkey` (6379): zero published host ports (internal bridge only).

3. **Hardcoded Port References Across Scripts and Configurations**:
   - `ki-basis/docker/nginx/default.conf` lines 14–15: hardcodes links to `8086` (Firefly), `8010` (Paperless), `8082` (OpenProject), and `8642` (Hermes).
   - `ki-basis/scripts/populate_openproject.py` line 10: `OPENPROJECT_URL = "http://127.0.0.1:8082"`.
   - `ki-basis/scripts/populate_paperless.py` line 10: `PAPERLESS_URL = "http://127.0.0.1:8010"`.
   - `ki-basis/scripts/populate_firefly.py` line 10: `FIREFLY_URL = "http://127.0.0.1:8086"`.
   - `ki-basis/scripts/verify_fundraiser_stack.py` lines 13, 16, 30: `8082`, `8086`, `8010`.
   - `ki-basis/scripts/generate_euer_tax_report.py` lines 15, 29: `8086`, `8010`.
   - `ki-basis/scripts/invoke-hermes.ps1` line 54: `http://127.0.0.1:8642/v1/chat/completions`.
   - `ki-basis/scripts/start-ki-basis.ps1` line 62: `http://127.0.0.1:8642/`.
   - `ki-basis/scripts/backup-stack.sh` lines 22–24: hardcoded container names (`ki-basis-hermes`, `ki-basis-firefly`, `ki-basis-paperless`, `ki-basis-openproject`, `ki-basis-postgres`, `ki-basis-valkey`).

4. **PostgreSQL Database Schema & User Initialization (`ki-basis/docker/postgres/init/01-init-databases.sh`)**:
   - Single cluster initialization: lines 17–25 create users `firefly_app`, `paperless_app`, `openproject_app` and databases `firefly`, `paperless`, `openproject` in the single postgres container.
   - Line 27 creates extension `vector` in `$POSTGRES_DB`.

5. **Historical Performance & Crash Evidence**:
   - `apex-meta/Alpine/Iteration2/Performance_Problem.md` lines 15–33: 7 containers idle at **~1,410 MB** (Postgres: 49.2 MB, Valkey: 5.6 MB, Firefly: 9.7 MB, Paperless: 244.6 MB, OpenProject: 891.9 MB, Hermes: 206.4 MB, Nginx: 3.1 MB).
   - Lines 41–58: Docker Desktop 5-process Electron GUI triggers `dwm.exe` memory ballooning to **756.5 MB** and Windows Kernel Memory Compression thrashing (**1,999.3 MB compressed RAM**), creating 2–4s mouse stutter and window freezes.
   - `apex-meta/Alpine/Maybe3rdIt/SoFarNotLean.md` lines 5–20: OpenProject Puma cluster + GoodJob (20 worker threads, 16 cron jobs, 17 postgres connections) consumes 1.8–2.5 GB at cold boot, triggering OOM kills (`exit 137`) and disk swap thrashing at 1.81 GB/s when constrained to a 2048 MB VM ceiling.
   - `ki-basis/compose.yaml` line 153: `PG_STARTUP_WAIT_TIME: "30"` causes OpenProject entrypoint crash (`exit status 1`) when database startup exceeds 30 seconds during high disk I/O.

---

## 2. Logic Chain

1. **Volume & Container Collision Mechanism**:
   - From Observation 1, `compose.yaml` explicitly hardcodes `container_name` and top-level volume `name: ki-basis-*`.
   - When Docker Compose evaluates a project namespace `-p`, custom `container_name` and `volume.name` declarations override the automatic `-p` prefixing.
   - *Inference*: Attempting to execute `docker compose -p ki-basis-community up -d` alongside `ki-basis-private` will fail with container name conflicts or corrupt data through shared volumes unless parameterized.

2. **9P Filesystem Bottleneck & OpenProject Crash Loop**:
   - From Observations 1, 3, and 5, mounting PostgreSQL data or OpenProject assets across WSL2's 9P `/mnt/c` bridge subjects synchronous database writes and Puma process locks (`puma.pid`) to severe 9P translation latency.
   - Synchronous threads accumulate in kernel D-state locks, driving CPU usage to 350% as vCPUs spin on locks.
   - When database readiness exceeds 30 seconds due to 9P I/O latency, OpenProject hits `PG_STARTUP_WAIT_TIME="30"` and crashes with `exit status 1`.
   - *Inference*: Achieving stable < 5% idle CPU and eliminating crash loops requires 100% native ext4 named volumes, increasing `PG_STARTUP_WAIT_TIME` to >= 60, and capping OpenProject workers via `OPENPROJECT_WEB_WORKERS=1`.

3. **Port Collisions in Dual-Instance Deployment**:
   - From Observations 2 and 3, both instances attempting to bind default ports (`8082`, `8086`, `8010`, `8084`, `8642`, `9119`) on `127.0.0.1` will fail with TCP bind errors (`address already in use`).
   - All automation scripts currently assume single-instance default ports.
   - *Inference*: Dual-instance architecture requires:
     - Non-overlapping port bands (Private on 8080–8089, Community on 9080–9089).
     - Environment variable overrides in all client scripts (e.g. `OPENPROJECT_URL = os.environ.get("OPENPROJECT_URL", "http://127.0.0.1:8082")`).

4. **Multi-Engine Evaluation (Strategy A vs. Strategy B)**:
   - Strategy B (Private in WSL2 Ubuntu dockerd on ext4, Community in Docker Desktop Alpine LinuxKit) runs two full virtual machines simultaneously.
   - Observation 5 establishes that a single VM running the 7 containers requires ~1.4–2.5 GB RAM. Running two VMs requires 4.5–6.0 GB host RAM, triggering severe Windows Memory Compression.
   - Furthermore, WSL2 default `localhostForwarding=true` forwards WSL2 port bindings onto the Windows host loopback, directly colliding with Docker Desktop's port publications.
   - Strategy A (Dual Compose Projects on Single Engine) runs both stacks in one Docker daemon, completely avoids `localhostForwarding` conflicts, shares hypervisor memory dynamically, and allows simple orchestration via `-p ki-basis-private` and `-p ki-basis-community`.
   - *Inference*: Strategy A is technically superior, simpler, and significantly more resource-efficient.

---

## 3. Caveats

1. **No Live Container Mutations**: In accordance with the Explorer read-only role, no live containers were stopped, started, or created during this survey.
2. **Untracked Secrets**: `ki-basis/.env` was inspected locally for structure and variable naming; actual high-entropy production tokens must remain untracked and excluded from version control.
3. **Third-Party Product Skills**: Product-specific Hermes skills for Firefly and OpenProject are not yet implemented in `ki-basis/skills/` (only `equinox-intake` exists); this does not affect infrastructure separation.

---

## 4. Conclusion

The repository contains an established, fully articulated single-instance Docker stack (`ki-basis`) with 7 core services, 10 named volumes, 1 bridge network, and extensive test/fixture assets.

To implement airtight dual-instance separation (Private vs. Community) and satisfy Acceptance Criteria R1–R3:
1. **Compose Parameterization**: Refactor `compose.yaml` to remove static `container_name` fields and parameterize top-level volume names with `${COMPOSE_PROJECT_NAME:-ki-basis}`.
2. **Network & Port Isolation**: Parameterize `KI_NETWORK_NAME` (`ki-basis-private-net` vs `ki-basis-community-net`) and allocate Private to port band 8080–8089 and Community to 9080–9089.
3. **Storage Architecture**: Retain 100% Docker named volumes backed by native ext4 (`ext4.vhdx`). Prohibit any host bind mounts on `/mnt/c` for database or application state.
4. **Stability Hardening**: Set `OPENPROJECT_WEB_WORKERS=1`, `PG_STARTUP_WAIT_TIME=60`, and run Docker Desktop in headless background mode (`04A`) to maintain idle CPU < 5% and eliminate crash loops.
5. **Script Portability**: Refactor client scripts (`populate_*.py`, `verify_*.py`, `generate_*.py`) to read service base URLs from environment variables rather than hardcoded constants.

---

## 5. Verification Method

To independently verify all findings:
1. **Audit Compose Parameterization & Hardcoded Values**:
   ```powershell
   Select-String -Path "C:\GitDev\apexai-os-meta\ki-basis\compose.yaml" -Pattern "container_name:", "name: ki-basis-"
   ```
2. **Audit Script Port Hardcodings**:
   ```powershell
   Get-ChildItem -Path "C:\GitDev\apexai-os-meta\ki-basis\scripts\*.py" | Select-String -Pattern "http://127.0.0.1:"
   ```
3. **Inspect Performance & Telemetry Records**:
   - View `C:\GitDev\apexai-os-meta\apex-meta\Alpine\Iteration2\Performance_Problem.md`
   - View `C:\GitDev\apexai-os-meta\apex-meta\Alpine\Maybe3rdIt\SoFarNotLean.md`
   - View `C:\GitDev\apexai-os-meta\apex-meta\Alpine\HANDOVER-REVIEWER-DOSSIER.md`
4. **Invalidation Condition**:
   - If `compose.yaml` already supported dynamic volume names without `ki-basis-` prefix, or if client scripts already read dynamic URLs, this conclusion would be invalidated. Direct line-by-line inspection confirms hardcoded values are present.
