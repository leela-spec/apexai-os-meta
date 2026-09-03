# Full Docker Stack (`ki-basis`) — Target Acceptance Report [DOCKER DESKTOP]

**Date**: 2026-09-02  
**Target Host**: Windows 11 Pro (Host Engine: Docker Desktop Linux VM / Hyper-V backend)  
**Target Docker Engine ID**: `e9c8ec3c-5306-43e3-8b37-a0803aa830d2`  
**Network**: `ki-basis-net` (bridge)  
**Overall Verdict**: **PASS (Target Environment)**

---

## 1. Target Operator Acceptance Surface

| Tool / Service | Image / Digest | Host URL / Port | Internal Address | Persistence | Hermes Access | Health Status |
|---|---|---|---|---|---|---|
| **PostgreSQL + pgvector** | `ki-basis-postgres` (`sha256:ccc6e83d6e35`) | *None (Internal only)* | `postgres:5432` | `ki-basis-postgres-data` (`/var/lib/postgresql/data`) | DB network reachability (`postgres:5432`) | `healthy` |
| **Valkey** | `ki-basis-valkey` (`sha256:f110e5df168d`) | *None (Internal only)* | `valkey:6379` | `ki-basis-valkey-data` (`/data`) | Cache network reachability (`valkey:6379`) | `healthy` |
| **Firefly III** | `fireflyiii/core:latest` (`sha256:ae69fdd95cde`) | `http://127.0.0.1:8086` | `firefly:8080` | `ki-basis-firefly-upload` (`/var/www/html/storage/upload`) | Authenticated REST API (OAuth2 / PAT) | `healthy` |
| **Paperless-ngx** | `ghcr.io/paperless-ngx/paperless-ngx:latest` (`sha256:5ab4f4f9bb09`) | `http://127.0.0.1:8010` | `paperless:8000` | `ki-basis-paperless-data`, `media`, `export`, `consume` | Authenticated REST API (Token Auth) | `healthy` |
| **OpenProject** | `openproject/openproject:14` (`sha256:73d4ee76fb3e`) | `http://127.0.0.1:8082` | `openproject:80` | `ki-basis-openproject-assets` (`/var/openproject/assets`) | Authenticated API v3 (API Key Auth) | `Up` (Puma Cluster) |
| **Nginx Edge** | `nginx:1.27-alpine` (`sha256:65645c7bb6a0`) | `http://127.0.0.1:8084` | `nginx:80` | Configuration bind mount (`./docker/nginx/default.conf:ro`) | Edge reverse proxy routing | `healthy` |
| **Hermes Agent** | `nousresearch/hermes-agent:latest` (`sha256:09d743f5e012`) | `http://127.0.0.1:8642` (Gateway)<br/>`http://127.0.0.1:9119` (Dashboard) | `hermes:8642`, `hermes:9119` | `ki-basis-hermes-data` (`/opt/data`)<br/>`ki-basis-hermes-workspaces` (`/root/workspaces`) | Target Agent Execution Context | `Up` (s6-rc supervised) |

---

## 2. Target Verification Matrix & Results

### M1: Multi-Database pgvector Validation
- **Requirement**: the pinned PostgreSQL service must be pgvector-capable, and the extension must be verified in the databases required by current workload/acceptance. Template databases are not application acceptance targets.
- **Result**: **PASS**
  - Acceptance databases: `postgres`, `firefly`, `paperless`, `openproject`. `template0`/`template1` are not treated as application acceptance targets.
  - Extension: `vector` version `0.8.6` installed and verified active in all target databases.

### M2: Port & Socket Isolation Verification
- **Requirement**: Core databases (`postgres` 5432, `valkey` 6379) must have zero host port publications. Hermes container must have no Docker socket mount.
- **Result**: **PASS**
  - `ki-basis-postgres`: Exposed internally to `ki-basis-net:5432`; Host Ports: `[]` (None).
  - `ki-basis-valkey`: Exposed internally to `ki-basis-net:6379`; Host Ports: `[]` (None).
  - `ki-basis-hermes`: `/var/run/docker.sock` mount is absent; host Docker daemon isolated.

### M3: Edge Proxy & Endpoint Health
- **Requirement**: Nginx edge proxy responds on `127.0.0.1:8084`, upstream services healthy.
- **Result**: **PASS**
  - Edge health probe: `GET http://127.0.0.1:8084/healthz` -> `HTTP 200 OK` (`nginx healthy`).
  - Firefly UI: `GET http://127.0.0.1:8086/` -> `HTTP 200 OK`.
  - Paperless UI: `GET http://127.0.0.1:8010/` -> `HTTP 200 OK`.
  - OpenProject Web: `GET http://127.0.0.1:8082/` -> `HTTP 200 OK`.
  - Hermes Dashboard: `GET http://127.0.0.1:9119/` -> `HTTP 200 OK`.

### M4: Paperless Negative & Positive Authentication Oracle
- **Requirement**: Token authentication must fail closed on invalid tokens (HTTP 401) and succeed on rotated token (HTTP 200) with document metadata + binary content SHA256 checksum matching.
- **Result**: **PASS**
  - Negative Auth: `GET /api/documents/` with revoked token -> `HTTP 401 Unauthorized` (`{"detail":"Invalid token."}`).
  - Positive Auth: `GET /api/documents/` with rotated token -> `HTTP 200 OK`.
  - Document Title: `Antigravity M5 Test Document` (ID: `1`).
  - Physical Document Download: `GET /api/documents/1/download/` -> `279 bytes`.
  - Document SHA256: `9fa30ebc25d8864f1d4eb61e38953150242278cb769a7c35868ab305e5542b82` (Exact match).

### M5: Target Backup Coverage & Manifest Validation
- **Requirement**: Backup script (`backup-stack.sh`) must back up all application databases and target named volumes (`ki-basis-hermes-data`, `ki-basis-hermes-workspaces`).
- **Result**: **PASS**
  - Backup target: `C:\Users\gehma\ki-basis-backups\20260902T203055Z`.
  - Database dumps: `globals.sql`, `firefly.dump`, `paperless.dump`, `openproject.dump`.
  - Volume archives: `valkey_data.tar.gz`, `firefly_upload.tar.gz`, `paperless_data.tar.gz`, `paperless_media.tar.gz`, `paperless_export.tar.gz`, `paperless_consume.tar.gz`, `openproject_assets.tar.gz`, `hermes_data.tar.gz`, `hermes_workspaces.tar.gz`.
  - Manifest coverage: 100% verified against running volume list.

### M6: Source Environment WSL Isolation
- **Requirement**: Legacy Ubuntu WSL distribution must be stopped and confirmed non-operational during target execution.
- **Result**: **PASS**
  - Command: `wsl.exe -l -v`
  - Output: `Ubuntu Stopped 2`
  - Target operates 100% inside Docker Desktop Hyper-V Linux VM.

---

## 3. Security & Integrity Audit Summary

- **C1 Token Rotation**: Leaked Paperless token sanitized in `apex-meta/Alpine/Iteration2/VerificationAG.md:156` (`0eb4dc56`); new token generated and active.
- **Secret Separation**: Real `.env` located outside version control; `.env.example` contains only template placeholders.
- **Fail-Closed Verification**: Scripts enforce non-empty `PAPERLESS_SECRET_KEY` and reject missing backup artifacts.