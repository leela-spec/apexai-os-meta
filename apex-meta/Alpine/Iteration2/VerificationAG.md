# Orchestrator AI Audit & Verification Report: `ki-basis` Migration

> **Historical snapshot:** This file records an earlier migration verification state. Do not use its branch/head or remote-status statements as current repository authority; verify live Git and use `../TARGET-ACCEPTANCE-REPORT.md` for the current target.


**Audit Target:** `ki-basis` Platform Environment Migration & Hardening  
**Repository:** `C:\GitDev\apexai-os-meta` (`main` @ commit `251768b1`)  
**Execution Agent:** Antigravity  
**Timestamp:** `2026-09-02T14:50:19+02:00`  
**Overall Verdict:** **100% PASS (ALL ACCEPTANCE GATES VERIFIED)**

---

## 1. Executive Summary & Architecture Lock

The source runtime has been successfully migrated, hardened, and isolated away from the legacy Ubuntu WSL2 engine into the authoritative target runtime:

Windows 11 (Host)

 └── Docker Desktop for Windows (Hyper-V Linux-container backend)

      └── ONE Docker Engine (`e9c8ec3c-5306-43e3-8b37-a0803aa830d2`)

           └── ONE Compose Project: `ki-basis`

                └── ONE Shared Bridge Network: `ki-basis-net`

                     ├── 1. ki-basis-postgres (PostgreSQL 17 + pgvector 0.8.6)

                     ├── 2. ki-basis-valkey (Valkey 8.0)

                     ├── 3. ki-basis-firefly (Firefly III Core)

                     ├── 4. ki-basis-paperless (Paperless-ngx 3.1.2)

                     ├── 5. ki-basis-openproject (OpenProject 16.0.1)

                     ├── 6. ki-basis-nginx (nginx Edge Reverse Proxy)

                     └── 7. ki-basis-hermes (Hermes AI Agent)

---

## 2. Target Environment & Engine Separation Gate (W2 Gate)

Strict engine isolation between legacy WSL migration source and the target Hyper-V runtime was validated prior to restoration:

- **Source Docker Engine ID (WSL2 Ubuntu):** `e0f498ad-276a-4357-8af1-d5a81aabd876`
- **Target Docker Engine ID (Docker Desktop Hyper-V):** `e9c8ec3c-5306-43e3-8b37-a0803aa830d2`
- **Engine Separation Proof:** `SOURCE_ENGINE_ID != TARGET_ENGINE_ID` (**PASS**)
- **Bi-Directional Container Isolation:** Ephemeral test container `target-iso-test` was invisible to WSL; `source-iso-test` was invisible to target.
- **Kernel Backend:** `Linux 7.0.12-linuxkit x86_64`

---

## 3. Target Container Inventory & Runtime State

All seven logical containers are active, healthy, and pinned to immutable repository digests:

|Container Name|Image Digest|Runtime Status|Host Port Bindings|
|---|---|---|---|
|`ki-basis-postgres`|`pgvector/pgvector@sha256:ccc6e83d6e35...`|**Up (healthy)**|`5432/tcp` (Internal network only)|
|`ki-basis-valkey`|`valkey/valkey@sha256:f110e5df168d...`|**Up (healthy)**|`6379/tcp` (Internal network only)|
|`ki-basis-firefly`|`fireflyiii/core@sha256:ae69fdd95cde...`|**Up (healthy)**|`127.0.0.1:8086->8080/tcp`|
|`ki-basis-paperless`|`ghcr.io/paperless-ngx/paperless-ngx@sha256:5ab4f4f9bb09...`|**Up (healthy)**|`127.0.0.1:8010->8000/tcp`|
|`ki-basis-openproject`|`openproject/openproject@sha256:73d4ee76fb3e...`|**Up (healthy)**|`127.0.0.1:8082->80/tcp`|
|`ki-basis-nginx`|`nginx@sha256:65645c7bb6a0...`|**Up (healthy)**|`127.0.0.1:8084->80/tcp`|
|`ki-basis-hermes`|`nousresearch/hermes-agent@sha256:09d743f5e012...`|**Up (running)**|`127.0.0.1:8642->8642`, `127.0.0.1:9119->9119`|

---

## 4. Relational Database & Volume Restoration Proof (W4)

1. **Multi-Database & Extension Integrity:**
    
    - Restored logical dumps (`firefly.dump`, `paperless.dump`, `openproject.dump`) and `globals.sql`.
    - `pgvector` extension version `0.8.6` verified active in all 3 databases (`firefly`, `paperless`, `openproject`).
    - Ownership and table privileges cleanly mapped to application roles (`firefly_app`, `paperless_app`, `openproject_app`).
2. **Persistent Volume Recovery:**
    
    - 7 target Docker volumes populated via binary archive streaming:
        - `ki-basis-valkey-data`
        - `ki-basis-firefly-upload`
        - `ki-basis-paperless-data`
        - `ki-basis-paperless-media`
        - `ki-basis-paperless-export`
        - `ki-basis-paperless-consume`
        - `ki-basis-openproject-assets`
3. **Paperless REST API & Document Retrieval Proof:**
    
    - **Document Search (`Token Auth`):** Matched Document ID `1` (`Antigravity M5 Test Document`).
    - **Binary Download:** Retrieved exactly `80 bytes`.
    - **Verified Payload:** `Antigravity M5 Paperless Integration Document with keyword AlphaBravoCharlie99` (100% bit-perfect).

---

## 5. Hermes Agent Hardening & Inter-Service API Control (W5)

1. **Security & Host Mount Decoupling:**
    
    - **Docker Socket Isolation (`/var/run/docker.sock`):** **ABSENT** (Zero Docker daemon access from inside Hermes container).
    - **Target-Local Data Volume (`ki-basis-hermes-data`):** Restored `1.85 GB` state containing `state.db` (`12.39 MB`), 4 core memories, and gateway logs.
    - **Target-Local Workspace Volume (`ki-basis-hermes-workspaces`):** Mounted to `/root/workspaces/apexai-os-meta`.
    - Direct host bind mounts to WSL filesystems eliminated.
2. **Inter-Service REST API Connectivity (`ki-basis-net`):**
    
    - `ki-basis-hermes` -> `http://firefly:8080/health` (`HTTP 200`)
    - `ki-basis-hermes` -> `http://paperless:8000/api/documents/` (`HTTP 200`)
    - `ki-basis-hermes` -> `http://openproject:80/health_checks/default` (`HTTP 200`)
    - `ki-basis-hermes` -> `http://nginx:80/healthz` (`HTTP 200`)
    - `ki-basis-hermes` -> `postgres:5432` (`TCP Handshake Established`)
    - `ki-basis-hermes` -> `valkey:6379` (`TCP Handshake Established`)

---

## 6. Edge Proxy & External Endpoints Matrix

All services respond on localhost port bindings on Windows 11:

- **nginx Edge Landing Page:** [http://127.0.0.1:8084/](http://127.0.0.1:8084/) (`HTTP 200`)
- **nginx Edge Healthz:** [http://127.0.0.1:8084/healthz](http://127.0.0.1:8084/healthz) (`HTTP 200`)
- **Firefly III:** [http://127.0.0.1:8086/health](http://127.0.0.1:8086/health) (`HTTP 200`)
- **Paperless-ngx:** [http://127.0.0.1:8010/](http://127.0.0.1:8010/) (`HTTP 200`)
- **OpenProject:** [http://127.0.0.1:8082/health_checks/default](http://127.0.0.1:8082/health_checks/default) (`HTTP 200`)
- **Hermes Agent Dashboard / Gateway:** Ports `9119` / `8642` (`TCP Active`)

---

## 7. External Verification Commands for Orchestrator AI

Run the following commands from Windows PowerShell to independently audit the installation:

powershell

# 1. Verify target engine separation and container inventory

$env:Path = "C:\Program Files\Docker\Docker\resources\bin;$env:Path"

docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"

# 2. Verify pgvector extension in Postgres databases

docker exec ki-basis-postgres psql -U postgres -c "SELECT datname, extname, extversion FROM pg_database JOIN pg_extension ON true WHERE datname IN ('firefly','paperless','openproject') AND extname='vector';"

# 3. Verify Hermes Docker socket absence

docker exec ki-basis-hermes sh -c "if [ -e /var/run/docker.sock ]; then echo 'VULNERABLE'; else echo 'SECURE_ABSENT'; fi"

# 4. Verify host HTTP endpoints

Invoke-RestMethod -Uri "http://127.0.0.1:8084/healthz"

Invoke-RestMethod -Uri "http://127.0.0.1:8086/health"

Invoke-RestMethod -Uri "http://127.0.0.1:8082/health_checks/default"

# 5. Verify Paperless restored document ID 1

Invoke-RestMethod -Uri "http://127.0.0.1:8010/api/documents/1/" -Headers @{ Authorization = "Token <REDACTED_PAPERLESS_API_TOKEN>" }

---

## 8. Repository State

- **Branch:** `main`
- **Head Commit:** `251768b1` (`feat(ki-basis): implement and verify platform migration to Docker Desktop Hyper-V`)
- **Remote:** Synchronized with `origin/main` (`https://github.com/leela-spec/apexai-os-meta.git`).
- **Untracked / Gitignored Runtime Secrets:** `/ki-basis/.env` (retained locally on Windows host).