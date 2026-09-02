# Full Docker Stack (`ki-basis`) — Source Integration Acceptance Report [PRE-MIGRATION]

> [!NOTE]
> **Pre-Migration Source Record**: This report records the historical acceptance state of the `ki-basis` stack inside the legacy WSL2 Ubuntu source environment prior to migration. For live target environment acceptance on Windows Docker Desktop Hyper-V, refer to [TARGET-ACCEPTANCE-REPORT.md](file:///c:/GitDev/apexai-os-meta/apex-meta/Alpine/TARGET-ACCEPTANCE-REPORT.md).

**Date**: 2026-09-01  
**Source Environment**: Windows 11 + WSL2 (Ubuntu 26.04 x86_64, Linux kernel `6.18.33.2-microsoft-standard-WSL2`)  
**Network**: `ki-basis-net` (bridge)  
**Overall Verdict**: **PASS (Pre-Migration Source)**

---

## 1. Operator Acceptance Surface

| Tool / Service | Image | Host URL / Port | Internal Address | Persistence | Hermes Access | Health Status |
|---|---|---|---|---|---|---|
| **PostgreSQL + pgvector** | `pgvector/pgvector:pg16` | *None (Internal only)* | `postgres:5432` | `ki-basis-postgres-data` (`/var/lib/postgresql/data`) | DB network reachability | `healthy` |
| **Valkey** | `valkey/valkey:8.0-alpine` | *None (Internal only)* | `valkey:6379` | `ki-basis-valkey-data` (`/data`) | Cache network reachability | `healthy` |
| **Firefly III** | `fireflyiii/core:latest` | `http://127.0.0.1:8086` | `firefly:8080` | `ki-basis-firefly-upload` (`/var/www/html/storage/upload`) | Authenticated REST API (OAuth2 / PAT) | `healthy` |
| **Paperless-ngx** | `ghcr.io/paperless-ngx/paperless-ngx:latest` | `http://127.0.0.1:8010` | `paperless:8000` | `ki-basis-paperless-data`, `media`, `export`, `consume` | Authenticated REST API (Token Auth) | `healthy` |
| **OpenProject** | `openproject/openproject:14` | `http://127.0.0.1:8082` | `openproject:80` | `ki-basis-openproject-assets` (`/var/openproject/assets`) | Authenticated API v3 (API Key Auth) | `Up` (Puma Cluster) |
| **Nginx Edge** | `nginx:1.27-alpine` | `http://127.0.0.1:8084` | `nginx:80` | Read-only configuration bind mount | Edge reverse proxy routing | `healthy` |
| **Hermes Agent** | `nousresearch/hermes-agent:latest` | `http://127.0.0.1:8642` (Gateway)<br/>`http://127.0.0.1:9119` (Dashboard) | `hermes:8642`, `hermes:9119` | `/root/.hermes` $\rightarrow$ `/opt/data`<br/>`/root/workspaces` $\rightarrow$ `/root/workspaces` | Host Agent Execution Context | `Up` (s6-rc supervised) |

---

## 2. Deterministic Verification Evidence

1. **Compose Configuration**: `docker compose config` passes with zero validation errors or missing variables.
2. **IP Addressing**: No static or hard-coded container IP addresses; dynamic Docker DNS discovery utilized across all inter-service paths.
3. **Secret Hygiene**: Zero unencrypted real passwords tracked in Git; `.env.example` contains placeholder credentials.
4. **Internal Isolation**: Ports `5432` (PostgreSQL) and `6379` (Valkey) have zero host-port exposure (`docker ps` shows no published ports on host).
5. **Host Port Binding**: All browser/human-facing ports bind strictly to `127.0.0.1` (`8084`, `8086`, `8010`, `8082`, `8642`, `9119`), completely avoiding Windows host port conflicts on `8000` and `8080`.
6. **Critical Security Boundary**: `/var/run/docker.sock` is strictly **absent** from the Hermes container filesystem.

---

## 3. Docker-Network Crossing & Hermes Connector Evidence

All tests executed directly inside the `ki-basis-hermes` execution context against internal container DNS names:

- **H1 Firefly Connector**:
  - Target: `http://firefly:8080/api/v1/about`
  - Auth: `Bearer <PAT_TOKEN>`
  - Result: `HTTP 200 OK` $\rightarrow$ `{"data":{"version":"6.6.6","api_version":"6.6.6","php_version":"8.5.7","os":"Linux","driver":"pgsql"}}`
- **H2 Paperless Connector**:
  - Target: `http://paperless:8000/api/documents/1/`
  - Auth: `Token <API_TOKEN>`
  - Result: `HTTP 200 OK` $\rightarrow$ `{"id":1,"title":"Antigravity M5 Test Document","content":"Antigravity M5 Paperless Integration Document with keyword AlphaBravoCharlie99\r\n"...}`
- **H3 OpenProject Connector**:
  - Target: `http://openproject:80/api/v3/work_packages/37`
  - Auth: Basic `apikey:<API_KEY>`
  - Result: `HTTP 200 OK` $\rightarrow$ `{"_type":"WorkPackage","id":37,"subject":"Antigravity M6 Verification Work Package"...}`
- **Nginx Edge Proxy Routing**:
  - Target: `http://nginx:80/healthz`
  - Result: `HTTP 200 OK` $\rightarrow$ `ki-basis nginx edge proxy healthy`

---

## 4. Cold-Start Persistence Verification

Executed complete stack teardown and cold restart:
```bash
docker compose down && docker compose up -d
```
All stateful objects independently retrieved and verified post-restart:
- **Firefly**: Admin user account and PAT active and valid.
- **Paperless**: Ingested test document `1` (`Antigravity M5 Test Document`) and fulltext OCR index intact.
- **OpenProject**: Test Work Package `37` (`Antigravity M6 Verification Work Package`) retrieved via API v3.
- **Hermes**: Preserved all state databases, skills, profiles, and workspaces in `/opt/data`.

---

## 5. Deliberate Negative Test Suite

1. **Firefly Invalid Credential**: `curl -H "Authorization: Bearer invalid" http://firefly:8080/api/v1/about` $\rightarrow$ `{"message":"Unauthenticated."}` (`HTTP 401`)
2. **Paperless Invalid Credential**: `curl -H "Authorization: Token invalid" http://paperless:8000/api/documents/` $\rightarrow$ `{"detail":"Invalid token."}` (`HTTP 401`)
3. **OpenProject Invalid Credential**: `curl -u "apikey:invalid" http://openproject:80/api/v3/work_packages` $\rightarrow$ `{"errorIdentifier":"urn:openproject-org:api:v3:errors:Unauthenticated"}` (`HTTP 401`)
4. **PostgreSQL Role Separation**: `psql -U paperless_app -d firefly` $\rightarrow$ `FATAL: permission denied for database "firefly" (User does not have CONNECT privilege)`
5. **Nginx Syntax Invalidation**: `nginx -t -g "invalid_test_directive;"` $\rightarrow$ `[emerg] unknown directive "invalid_test_directive" in command line (configuration file test failed)`
6. **Host DB/Cache Port Blocking**: Connection attempts to `127.0.0.1:5432` and `127.0.0.1:6379` fail immediately (`Connection refused`).

---

## 6. Real Backup & Controlled Restore Verification

- **PostgreSQL Dumps**: Created `firefly.sql` (`b5f8bd32...`), `paperless.sql` (`160d333c...`), `openproject.sql` (`e0f61c93...`).
- **Hermes State Backup**: Created `hermes_state.tar.gz` (`a579c92f...`).
- **Controlled Restore**: Restored `paperless.sql` into disposable database `disposable_restore_test`.
- **Restored Data Verification**: `SELECT id, title, checksum FROM documents_document;` confirmed exact document ID `1` matching SHA256 checksum `807123bbec8170a13c33900340b38daee87f9944951fcb26a7264f73d775f5a7`.

---

## 7. Independent Service Lifecycle Check

Recreated `nginx` independently via `docker compose up -d --force-recreate nginx`. All 6 peer services (`postgres`, `valkey`, `firefly`, `paperless`, `openproject`, `hermes`) remained continuously running and healthy without downtime or data corruption.