# KI-Basis Operator Runbooks & Production Configuration Templates

**Document Version:** 2.0.0  
**Status:** Production Standard / Operational Runbook  
**Target Environments:**  
1. **Community Operations:** Safer Space e.V. / Equinox 2026 Fundraiser (`lika-community`, Port Band 908x)  
2. **Private Entrepreneurship:** Commercial Consulting & Private Accounting (`private-business`, Port Band 808x)  

---

## 1. Operational Philosophy & Minimalist Entrypoints

The dual-stack architecture eliminates the requirement for complex manual prompt engineering or intricate CLI flags. An operator—whether a non-technical volunteer coordinator or a commercial consultant—operates within a deterministic, 1-click workspace:

* **Zero Prompt Engineering:** Opening the designated workspace directory (`C:\GitDev\lika-community\` or `C:\GitDev\private-business\`) automatically scopes the AI agent via the local `AGENTS.md` and `SOUL.md`. The AI cannot view, index, or route to the other domain.
* **1-Click Execution:** The entire stack lifecycle is controlled via turnkey PowerShell scripts (`.\scripts\start.ps1` and `.\scripts\stop.ps1`). The scripts automatically verify Docker Desktop engine health, validate physical ext4 volume attachments inside `DockerDesktop.vhdx`, launch containers in detached mode, poll health endpoints, and print service URLs.
* **Failsafe Volume Security:** All volume mounts use `external: true`. Containers will fail closed immediately rather than initializing blank storage if an underlying volume is detached.

---

## 2. Community Operations Template Pack (`lika-community`)

### 2.1 Instruction Fence: `lika-community/AGENTS.md`
```markdown
# Lika Community Operations — Scoped AI Agent Rulebook

**Domain:** Safer Space e.V. / Equinox 2026 Fundraiser Operations  
**Active Port Band:** 908x  
**Persona:** `LikasKinkyBot` (`@LikasSlave_bot`) defined in `SOUL.md`  
**Container Stack:** `ki-basis-community`  

## 1. Strict Boundary Constraints
- **Jurisdiction:** You operate exclusively on the Community Operations stack (`ki-basis-community`).
- **Absolute Isolation:**
  - You have ZERO jurisdiction over, access to, or knowledge of any private commercial business stack.
  - Never attempt to inspect, route to, or search for files outside this repository root.
  - If queried about commercial consulting, corporate tax records, or private bank accounts, state clearly: "I only manage Safer Space e.V. and Equinox community operations."

## 2. Service Endpoints & Ports (Port Band 908x)
- **OpenProject (Equinox Tasks):** `http://127.0.0.1:9082` (Container: `ki-basis-community-openproject`)
- **Paperless-ngx (Volunteer Receipts):** `http://127.0.0.1:9010` (Container: `ki-basis-community-paperless`)
- **Firefly III (GLS Bank):** `http://127.0.0.1:9086` (Container: `ki-basis-community-firefly`)
- **Nginx Edge Proxy:** `http://127.0.0.1:9084` (Container: `ki-basis-community-nginx`)
- **Hermes Dashboard:** `http://127.0.0.1:9219` (Container: `ki-basis-community-hermes`)
- **Hermes Gateway API:** `http://127.0.0.1:9642`

## 3. Telegram Intake & Triage Protocols
- Incoming Telegram messages from volunteers and group `-1004343753692` are received via `@LikasSlave_bot`.
- **Receipt Ingestion:** Ingested receipts MUST be tagged with `STAGED-FOR-REVIEW` in Paperless-ngx.
- **Task Management:** File volunteer assignments and fundraiser milestones under OpenProject Project #3 (Equinox 2026).
- **Tiered Autonomy:** You have READ-ONLY visibility into Firefly III. NEVER autonomously create or modify ledger transactions. All financial postings require human treasurer approval.

## 4. Git & Data Safety
- NEVER commit `.env` or files containing volunteer phone numbers, addresses, or private contact details.
- Commits in this repository belong strictly to the community operations repository.
```

### 2.2 Docker Compose Specification: `lika-community/compose.yaml`
```yaml
name: ki-basis-community

networks:
  ki-basis-community-net:
    name: ki-basis-community-net
    driver: bridge

volumes:
  postgres_data:
    external: true
    name: ki-basis-community-postgres-data
  valkey_data:
    external: true
    name: ki-basis-community-valkey-data
  firefly_upload:
    external: true
    name: ki-basis-community-firefly-upload
  paperless_data:
    external: true
    name: ki-basis-community-paperless-data
  paperless_media:
    external: true
    name: ki-basis-community-paperless-media
  paperless_export:
    external: true
    name: ki-basis-community-paperless-export
  paperless_consume:
    external: true
    name: ki-basis-community-paperless-consume
  openproject_assets:
    external: true
    name: ki-basis-community-openproject-assets
  hermes_data:
    external: true
    name: ki-basis-community-hermes-data
  hermes_workspaces:
    external: true
    name: ki-basis-community-hermes-workspaces

services:
  postgres:
    image: pgvector/pgvector@sha256:ccc6e83d6e35e931dc7c5def2022729d5a6c370318d099181995567ff1fb4d6b
    container_name: ki-basis-community-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-postgres}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:?POSTGRES_PASSWORD is required}
      POSTGRES_DB: ${POSTGRES_DB:-postgres}
      FIREFLY_DB_USER: ${FIREFLY_DB_USER:-firefly_app}
      FIREFLY_DB_PASSWORD: ${FIREFLY_DB_PASSWORD:?FIREFLY_DB_PASSWORD is required}
      FIREFLY_DB_NAME: ${FIREFLY_DB_NAME:-firefly}
      PAPERLESS_DB_USER: ${PAPERLESS_DB_USER:-paperless_app}
      PAPERLESS_DB_PASSWORD: ${PAPERLESS_DB_PASSWORD:?PAPERLESS_DB_PASSWORD is required}
      PAPERLESS_DB_NAME: ${PAPERLESS_DB_NAME:-paperless}
      OPENPROJECT_DB_USER: ${OPENPROJECT_DB_USER:-openproject_app}
      OPENPROJECT_DB_PASSWORD: ${OPENPROJECT_DB_PASSWORD:?OPENPROJECT_DB_PASSWORD is required}
      OPENPROJECT_DB_NAME: ${OPENPROJECT_DB_NAME:-openproject}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./docker/postgres/init:/docker-entrypoint-initdb.d:ro
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-postgres}"]
      interval: 5s
      timeout: 5s
      retries: 5
      start_period: 10s
    networks:
      - ki-basis-community-net

  valkey:
    image: valkey/valkey@sha256:f110e5df168de4cdbd17afec848c6efe88e4b5e51c5b1ec6109de0c1b6a0c60b
    container_name: ki-basis-community-valkey
    restart: unless-stopped
    command: ["valkey-server", "--save", "60", "1", "--loglevel", "notice"]
    volumes:
      - valkey_data:/data
    healthcheck:
      test: ["CMD", "valkey-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5
      start_period: 5s
    networks:
      - ki-basis-community-net

  firefly:
    image: fireflyiii/core@sha256:ae69fdd95cdef9038cd7a460a5aec731f14813973e4f096511d5a4ea9ff0e972
    container_name: ki-basis-community-firefly
    restart: unless-stopped
    ports:
      - "127.0.0.1:${FIREFLY_HOST_PORT:-9086}:8080"
    environment:
      APP_KEY: ${FIREFLY_APP_KEY:?FIREFLY_APP_KEY is required}
      APP_URL: http://127.0.0.1:${FIREFLY_HOST_PORT:-9086}
      APP_ENV: local
      APP_DEBUG: "false"
      SITE_OWNER: admin@example.com
      TZ: Europe/Berlin
      DB_CONNECTION: pgsql
      DB_HOST: postgres
      DB_PORT: 5432
      DB_DATABASE: ${FIREFLY_DB_NAME:-firefly}
      DB_USERNAME: ${FIREFLY_DB_USER:-firefly_app}
      DB_PASSWORD: ${FIREFLY_DB_PASSWORD:?FIREFLY_DB_PASSWORD is required}
    volumes:
      - firefly_upload:/var/www/html/storage/upload
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - ki-basis-community-net

  paperless:
    image: ghcr.io/paperless-ngx/paperless-ngx@sha256:5ab4f4f9bb099a36bec3e092906ea3e611323c5f18dc5cc38c76a1d540bdca9c
    container_name: ki-basis-community-paperless
    restart: unless-stopped
    ports:
      - "127.0.0.1:${PAPERLESS_HOST_PORT:-9010}:8000"
    environment:
      PAPERLESS_WORKERS: "${PAPERLESS_WORKERS:-1}"
      PAPERLESS_TASK_WORKERS: "${PAPERLESS_TASK_WORKERS:-1}"
      PAPERLESS_THREADS_PER_WORKER: "${PAPERLESS_THREADS_PER_WORKER:-1}"
      PAPERLESS_REDIS: redis://valkey:6379
      PAPERLESS_DBENGINE: postgresql
      PAPERLESS_DBHOST: postgres
      PAPERLESS_DBPORT: 5432
      PAPERLESS_DBNAME: ${PAPERLESS_DB_NAME:-paperless}
      PAPERLESS_DBUSER: ${PAPERLESS_DB_USER:-paperless_app}
      PAPERLESS_DBPASS: ${PAPERLESS_DB_PASSWORD:?PAPERLESS_DB_PASSWORD is required}
      PAPERLESS_SECRET_KEY: ${PAPERLESS_SECRET_KEY:?PAPERLESS_SECRET_KEY is required}
      PAPERLESS_URL: http://127.0.0.1:${PAPERLESS_HOST_PORT:-9010}
      PAPERLESS_TIME_ZONE: Europe/Berlin
      PAPERLESS_OCR_LANGUAGE: deu+eng
      PAPERLESS_ADMIN_USER: ${PAPERLESS_ADMIN_USER:-admin}
      PAPERLESS_ADMIN_PASSWORD: ${PAPERLESS_ADMIN_PASSWORD:?PAPERLESS_ADMIN_PASSWORD is required}
    volumes:
      - paperless_data:/usr/src/paperless/data
      - paperless_media:/usr/src/paperless/media
      - paperless_export:/usr/src/paperless/export
      - paperless_consume:/usr/src/paperless/consume
    depends_on:
      postgres:
        condition: service_healthy
      valkey:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-fs", "-S", "--max-time", "2", "http://localhost:8000"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
    networks:
      - ki-basis-community-net

  openproject:
    image: openproject/openproject@sha256:73d4ee76fb3edb33b0eb1a3a2ddc036f0a45f9083459f445e3d0b634044cf8fb
    container_name: ki-basis-community-openproject
    restart: unless-stopped
    ports:
      - "127.0.0.1:${OPENPROJECT_HOST_PORT:-9082}:80"
    environment:
      OPENPROJECT_WEB_WORKERS: "${OPENPROJECT_WEB_WORKERS:-1}"
      OPENPROJECT_BACKGROUND_WORKERS: "${OPENPROJECT_BACKGROUND_WORKERS:-1}"
      PG_STARTUP_WAIT_TIME: "${PG_STARTUP_WAIT_TIME:-60}"
      OPENPROJECT_HTTPS: "false"
      OPENPROJECT_HOST__NAME: 127.0.0.1:${OPENPROJECT_HOST_PORT:-9082}
      OPENPROJECT_SECRET_KEY_BASE: ${OPENPROJECT_SECRET_KEY_BASE:?OPENPROJECT_SECRET_KEY_BASE is required}
      DATABASE_URL: postgres://${OPENPROJECT_DB_USER:-openproject_app}:${OPENPROJECT_DB_PASSWORD:?OPENPROJECT_DB_PASSWORD is required}@postgres:5432/${OPENPROJECT_DB_NAME:-openproject}
    volumes:
      - openproject_assets:/var/openproject/assets
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - ki-basis-community-net

  nginx:
    image: nginx@sha256:65645c7bb6a0661892a8b03b89d0743208a18dd2f3f17a54ef4b76fb8e2f2a10
    container_name: ki-basis-community-nginx
    restart: unless-stopped
    ports:
      - "127.0.0.1:${NGINX_HOST_PORT:-9084}:80"
    volumes:
      - ./docker/nginx:/etc/nginx/conf.d:ro
    depends_on:
      - firefly
      - paperless
      - openproject
    healthcheck:
      test: ["CMD", "wget", "-q", "-O", "/dev/null", "http://127.0.0.1:80/healthz"]
      interval: 5s
      timeout: 3s
      retries: 5
      start_period: 5s
    networks:
      - ki-basis-community-net

  hermes:
    image: nousresearch/hermes-agent@sha256:09d743f5e012e41503829d06ca129c7d3e87ea3f943f7228d520c5c53c6f7db5
    container_name: ki-basis-community-hermes
    restart: unless-stopped
    command: gateway run
    ports:
      - "127.0.0.1:${HERMES_GATEWAY_HOST_PORT:-9642}:8642"
      - "127.0.0.1:${HERMES_DASHBOARD_HOST_PORT:-9219}:9119"
    environment:
      HERMES_DASHBOARD: "1"
      HERMES_GATEWAY_EXTERNAL_SUPERVISOR: "1"
      HERMES_GATEWAY_BOOTSTRAP_STATE: "running"
      HERMES_DASHBOARD_BASIC_AUTH_USERNAME: ${HERMES_DASHBOARD_BASIC_AUTH_USERNAME:-admin}
      HERMES_DASHBOARD_BASIC_AUTH_PASSWORD: ${HERMES_DASHBOARD_BASIC_AUTH_PASSWORD:?HERMES_DASHBOARD_BASIC_AUTH_PASSWORD is required}
      HERMES_HOME: /opt/data
      HERMES_WRITE_SAFE_ROOT: /opt/data
      HERMES_DISABLE_LAZY_INSTALLS: "1"
      HERMES_LAZY_INSTALL_TARGET: /opt/data/lazy-packages
      API_SERVER_ENABLED: "true"
      API_SERVER_HOST: "0.0.0.0"
      API_SERVER_KEY: ${HERMES_API_SERVER_KEY:?HERMES_API_SERVER_KEY is required}
      FIREFLY_API_URL: http://firefly:8080
      PAPERLESS_API_URL: http://paperless:8000
      OPENPROJECT_API_URL: http://openproject:80
      TELEGRAM_BOT_TOKEN: ${TELEGRAM_BOT_TOKEN:-}
      TELEGRAM_ALLOW_ALL_USERS: "${TELEGRAM_ALLOW_ALL_USERS:-true}"
      GATEWAY_ALLOW_ALL_USERS: "${GATEWAY_ALLOW_ALL_USERS:-true}"
      TELEGRAM_OBSERVE_UNMENTIONED_GROUP_MESSAGES: "${TELEGRAM_OBSERVE_UNMENTIONED_GROUP_MESSAGES:-true}"
      TELEGRAM_GROUP_ALLOWED_CHATS: "${TELEGRAM_GROUP_ALLOWED_CHATS:--1004343753692}"
      TELEGRAM_ALLOWED_CHATS: "${TELEGRAM_ALLOWED_CHATS:--1004343753692}"
      TELEGRAM_FREE_RESPONSE_CHATS: "${TELEGRAM_FREE_RESPONSE_CHATS:--1004343753692}"
      TELEGRAM_HOME_CHANNEL: "${TELEGRAM_HOME_CHANNEL:--1004343753692}"
      PAPERLESS_TOKEN: ${PAPERLESS_API_TOKEN:-}
      PAPERLESS_URL: http://paperless:8000
      OPENPROJECT_KEY: ${OPENPROJECT_API_KEY:-}
      OPENPROJECT_URL: http://openproject:80
      OPENAI_API_KEY: ${OPENAI_API_KEY:-}
      ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:-}
      OPENROUTER_API_KEY: ${OPENROUTER_API_KEY:-}
    volumes:
      - hermes_data:/opt/data
      - hermes_workspaces:/root/workspaces
      - ./scripts:/opt/data/scripts:ro
      - ./SOUL.md:/opt/data/SOUL.md:ro
      - ./skills/equinox-intake:/opt/data/skills/equinox-intake:ro
    depends_on:
      - firefly
      - paperless
      - openproject
      - nginx
    networks:
      - ki-basis-community-net
```

### 2.3 1-Click Startup Runbook: `lika-community/scripts/start.ps1`
```powershell
<#
.SYNOPSIS
    1-Click Startup Script for Lika Community Operations (Port Band 908x).
.DESCRIPTION
    Performs fail-closed pre-flight validation on Docker Engine and named ext4
    volumes before launching the Safer Space e.V. / Equinox community stack.
#>
[CmdletBinding()]
param(
    [int]$TimeoutSeconds = 90
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Split-Path -Parent $ScriptDir

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "  Starting Lika Community Operations Stack (Port Band 908x)...   " -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan

Set-Location $RootDir

# 1. Environment file check
if (-not (Test-Path ".env")) {
    Write-Error "Missing .env file in $RootDir! Copy .env.example to .env and configure credentials."
}

# 2. Docker Desktop Engine Check
Write-Host "==> [PRE-FLIGHT] Checking Docker Engine accessibility..." -ForegroundColor Cyan
$ver = docker info --format "{{.ServerVersion}}" 2>$null
if (-not $ver) {
    Write-Host "Docker Desktop not responding. Launching Docker Desktop..." -ForegroundColor Yellow
    Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    $elapsed = 0
    while ($elapsed -lt $TimeoutSeconds) {
        Start-Sleep -Seconds 3
        $elapsed += 3
        $ver = docker info --format "{{.ServerVersion}}" 2>$null
        if ($ver) { break }
    }
    if (-not $ver) { throw "Timed out waiting for Docker Desktop engine." }
}
Write-Host "[PASS] Docker Engine active (Server Version: $ver)" -ForegroundColor Green

# 3. Fail-Closed Ext4 Volume Verification
Write-Host "==> [PRE-FLIGHT] Verifying physical ext4 named volumes..." -ForegroundColor Cyan
$RequiredVols = @(
    "ki-basis-community-postgres-data",
    "ki-basis-community-valkey-data",
    "ki-basis-community-firefly-upload",
    "ki-basis-community-paperless-data",
    "ki-basis-community-paperless-media",
    "ki-basis-community-paperless-export",
    "ki-basis-community-paperless-consume",
    "ki-basis-community-openproject-assets",
    "ki-basis-community-hermes-data",
    "ki-basis-community-hermes-workspaces"
)
foreach ($vol in $RequiredVols) {
    docker volume inspect $vol > $null 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "HALT: Required volume '$vol' not found in DockerDesktop.vhdx! Aborting startup to prevent uninitialized storage creation."
    }
}
Write-Host "[PASS] All 10 persistent ext4 volumes verified present." -ForegroundColor Green

# 4. Launch Containers
Write-Host "==> Launching Community containers via Docker Compose..." -ForegroundColor Cyan
docker compose -p ki-basis-community --env-file .env up -d --remove-orphans

# 5. Service Health Polling (Application Warmup & Edge Verification)
Write-Host "==> Polling backend services for healthy status (Paperless & OpenProject warmup)..." -ForegroundColor Yellow
$healthy = $false
for ($i = 0; $i -lt 30; $i++) {
    Start-Sleep -Seconds 3
    try {
        $edgeRes = Invoke-WebRequest -Uri "http://127.0.0.1:9084/healthz" -UseBasicParsing -TimeoutSec 2 -ErrorAction SilentlyContinue
        $pRes = Invoke-WebRequest -Uri "http://127.0.0.1:9010" -UseBasicParsing -TimeoutSec 2 -ErrorAction SilentlyContinue
        $opRes = Invoke-WebRequest -Uri "http://127.0.0.1:9082" -UseBasicParsing -TimeoutSec 2 -ErrorAction SilentlyContinue
        if ($edgeRes.StatusCode -eq 200 -and ($pRes.StatusCode -in 200, 301, 302) -and ($opRes.StatusCode -in 200, 301, 302)) {
            $healthy = $true
            break
        }
    } catch {}
}

# 6. Service Dashboard Display
Write-Host "`n=================================================================" -ForegroundColor Green
if ($healthy) {
    Write-Host "  Lika Community Operations Stack is HEALTHY and READY!          " -ForegroundColor Green
} else {
    Write-Host "  Stack started (services are completing warmup).                " -ForegroundColor Yellow
}
Write-Host "=================================================================" -ForegroundColor Green
Write-Host "  • OpenProject (Equinox Tasks): http://127.0.0.1:9082" -ForegroundColor White
Write-Host "  • Paperless-ngx (Receipts):    http://127.0.0.1:9010" -ForegroundColor White
Write-Host "  • Firefly III (GLS Bank):      http://127.0.0.1:9086" -ForegroundColor White
Write-Host "  • Nginx Edge Proxy:            http://127.0.0.1:9084" -ForegroundColor White
Write-Host "  • Hermes Dashboard:            http://127.0.0.1:9219" -ForegroundColor White
Write-Host "  • Telegram Bot:                ACTIVE (@LikasSlave_bot)" -ForegroundColor White
Write-Host "=================================================================`n" -ForegroundColor Green
```

### 2.4 1-Click Shutdown Runbook: `lika-community/scripts/stop.ps1`
```powershell
<#
.SYNOPSIS
    1-Click Graceful Shutdown Script for Lika Community Operations.
#>
[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Split-Path -Parent $ScriptDir

Set-Location $RootDir
Write-Host "==> Gracefully stopping Lika Community Operations Stack..." -ForegroundColor Yellow
docker compose -p ki-basis-community stop
Write-Host "[SUCCESS] Community containers stopped cleanly. All data preserved in ext4 volumes." -ForegroundColor Green
```

### 2.5 Edge Proxy Specification: `lika-community/docker/nginx/default.conf`
```nginx
server {
    listen 80;
    server_name localhost 127.0.0.1;

    # Edge healthcheck endpoint
    location = /healthz {
        access_log off;
        add_header Content-Type text/plain;
        return 200 'lika-community nginx edge proxy healthy\n';
    }

    # Community Operations Stack index page (Port Band 908x only)
    location = / {
        add_header Content-Type text/html;
        return 200 '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Lika Community Operations Platform Edge</title><style>body{font-family:system-ui,-apple-system,sans-serif;padding:2rem;background:#0f172a;color:#f8fafc;max-width:900px;margin:0 auto;}h1{color:#4ade80;margin-bottom:0.25rem;}h2{color:#94a3b8;font-size:1.1rem;margin-top:1.5rem;border-bottom:1px solid #334155;padding-bottom:0.4rem;}a{color:#4ade80;text-decoration:none;}a:hover{text-decoration:underline;}li{margin:0.6rem 0;}ul{list-style:none;padding:0;}.badge{display:inline-block;padding:0.25rem 0.5rem;border-radius:4px;font-size:0.8rem;font-weight:bold;margin-left:0.5rem;background:#166534;color:#bbf7d0;}.active-stack{background:#1e293b;border-radius:8px;padding:1.25rem;border:1px solid #4ade80;margin-bottom:1.5rem;}</style></head><body><h1>Lika Community Operations Edge</h1><div class="active-stack"><h2>Safer Space e.V. & Equinox Operations (Port Band 908x)</h2><ul><li><a href="http://127.0.0.1:9082">OpenProject (Equinox Tasks) — :9082</a> <span class="badge">Community</span></li><li><a href="http://127.0.0.1:9010">Paperless-ngx (Volunteer Receipts) — :9010</a> <span class="badge">Community</span></li><li><a href="http://127.0.0.1:9086">Firefly III (GLS Bank / 4-Sphere) — :9086</a> <span class="badge">Community</span></li><li><a href="http://127.0.0.1:9219">Hermes Dashboard (AI Web) — :9219</a> <span class="badge">Community</span></li><li><a href="http://127.0.0.1:9642">Hermes Gateway (AI API) — :9642</a> <span class="badge">Community</span></li></ul></div></body></html>\n';
    }
}
```

---

## 3. Private Entrepreneurship Template Pack (`private-business`)

### 3.1 Instruction Fence: `private-business/AGENTS.md`
```markdown
# Private Business Operations — Scoped AI Agent Rulebook

**Domain:** Commercial Ventures, Client Consulting, Accounting & Tax Operations  
**Active Port Band:** 808x  
**Persona:** `ExecutivePartner` defined in `SOUL.md`  
**Container Stack:** `ki-basis-private`  

## 1. Strict Boundary Constraints
- **Jurisdiction:** You operate exclusively on the Private Business stack (`ki-basis-private`).
- **Absolute Privacy & Confidentiality:**
  - All client billing, invoices, contracts, tax ledgers, and bank records are strictly confidential.
  - Telegram integration is DISABLED. Never attempt to connect to or poll Telegram.
  - You have ZERO jurisdiction over Safer Space e.V. or Equinox operations. Never query or link community boards.

## 2. Service Endpoints & Ports (Port Band 808x)
- **OpenProject (Client Projects & Timesheets):** `http://127.0.0.1:8082` (Container: `ki-basis-private-openproject`)
- **Paperless-ngx (Tax Invoices & Contracts):** `http://127.0.0.1:8010` (Container: `ki-basis-private-paperless`)
- **Firefly III (Commercial Bank & Ledger):** `http://127.0.0.1:8086` (Container: `ki-basis-private-firefly`)
- **Nginx Edge Proxy:** `http://127.0.0.1:8084` (Container: `ki-basis-private-nginx`)
- **Hermes Dashboard:** `http://127.0.0.1:9119` (Container: `ki-basis-private-hermes`)
- **Hermes Gateway API:** `http://127.0.0.1:8642`

## 3. Financial & Accounting Operational Standards
- **Tone & Demeanor:** Rigorous, analytical, concise, and professional. Zero roleplay, zero informal chatter.
- **Double-Entry Discipline:** Treat all financial figures with exact double-entry precision. All ledger entries must reconcile against verified bank exports.
- **EÜR & Tax Compliance:** Invoices and receipts must be verified against German tax requirements (UstG §14).

## 4. Git & Data Safety
- NEVER commit `.env`, client invoices, or confidential ledgers to public or shared remotes.
- Pushes from this repository belong strictly to the private commercial git remote.
```

### 3.2 Executive Persona Specification: `private-business/SOUL.md`
```markdown
---
name: ExecutivePartner
domain: private_business_operations
archetype: executive_chief_of_staff
spec: OKF-0.2
version: 1.0.0
---

# Soul: Executive Operations Partner

You are the dedicated, confidential Executive Operations Partner for Private Business, Corporate Consulting, and Financial Management.

## 1. Operating Principles
- **Absolute Confidentiality:** Zero leakage of commercial contracts, fee structures, tax data, or personal records.
- **Professional Demeanor:** Analytical, objective, and deterministic. No roleplay, no informal slang, and zero candy/spank memes.
- **Precision Accounting:** Treat all financial figures with strict double-entry accounting discipline. All ledger entries must reconcile against verified bank statements.

## 2. Execution Boundaries
- **Telegram Integration:** DISABLED. You operate exclusively via authenticated loopback API (:8642) and operator CLI.
- **Community Isolation:** You have zero jurisdiction over Safer Space e.V. or Equinox operations. Never attempt to query or link community project boards.

## 3. Communication Style
- Deliver crisp, structured summaries with executive bullet points.
- Highlight discrepancies, tax compliance deadlines, and cash flow forecasts proactively.
```

### 3.3 Docker Compose Specification: `private-business/compose.yaml`
```yaml
name: ki-basis-private

networks:
  ki-basis-private-net:
    name: ki-basis-private-net
    driver: bridge

volumes:
  postgres_data:
    external: true
    name: ki-basis-private-postgres-data
  valkey_data:
    external: true
    name: ki-basis-private-valkey-data
  firefly_upload:
    external: true
    name: ki-basis-private-firefly-upload
  paperless_data:
    external: true
    name: ki-basis-private-paperless-data
  paperless_media:
    external: true
    name: ki-basis-private-paperless-media
  paperless_export:
    external: true
    name: ki-basis-private-paperless-export
  paperless_consume:
    external: true
    name: ki-basis-private-paperless-consume
  openproject_assets:
    external: true
    name: ki-basis-private-openproject-assets
  hermes_data:
    external: true
    name: ki-basis-private-hermes-data
  hermes_workspaces:
    external: true
    name: ki-basis-private-hermes-workspaces

services:
  postgres:
    image: pgvector/pgvector@sha256:ccc6e83d6e35e931dc7c5def2022729d5a6c370318d099181995567ff1fb4d6b
    container_name: ki-basis-private-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-postgres}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:?POSTGRES_PASSWORD is required}
      POSTGRES_DB: ${POSTGRES_DB:-postgres}
      FIREFLY_DB_USER: ${FIREFLY_DB_USER:-firefly_app}
      FIREFLY_DB_PASSWORD: ${FIREFLY_DB_PASSWORD:?FIREFLY_DB_PASSWORD is required}
      FIREFLY_DB_NAME: ${FIREFLY_DB_NAME:-firefly}
      PAPERLESS_DB_USER: ${PAPERLESS_DB_USER:-paperless_app}
      PAPERLESS_DB_PASSWORD: ${PAPERLESS_DB_PASSWORD:?PAPERLESS_DB_PASSWORD is required}
      PAPERLESS_DB_NAME: ${PAPERLESS_DB_NAME:-paperless}
      OPENPROJECT_DB_USER: ${OPENPROJECT_DB_USER:-openproject_app}
      OPENPROJECT_DB_PASSWORD: ${OPENPROJECT_DB_PASSWORD:?OPENPROJECT_DB_PASSWORD is required}
      OPENPROJECT_DB_NAME: ${OPENPROJECT_DB_NAME:-openproject}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./docker/postgres/init:/docker-entrypoint-initdb.d:ro
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER:-postgres}"]
      interval: 5s
      timeout: 5s
      retries: 5
      start_period: 10s
    networks:
      - ki-basis-private-net

  valkey:
    image: valkey/valkey@sha256:f110e5df168de4cdbd17afec848c6efe88e4b5e51c5b1ec6109de0c1b6a0c60b
    container_name: ki-basis-private-valkey
    restart: unless-stopped
    command: ["valkey-server", "--save", "60", "1", "--loglevel", "notice"]
    volumes:
      - valkey_data:/data
    healthcheck:
      test: ["CMD", "valkey-cli", "ping"]
      interval: 5s
      timeout: 3s
      retries: 5
      start_period: 5s
    networks:
      - ki-basis-private-net

  firefly:
    image: fireflyiii/core@sha256:ae69fdd95cdef9038cd7a460a5aec731f14813973e4f096511d5a4ea9ff0e972
    container_name: ki-basis-private-firefly
    restart: unless-stopped
    ports:
      - "127.0.0.1:${FIREFLY_HOST_PORT:-8086}:8080"
    environment:
      APP_KEY: ${FIREFLY_APP_KEY:?FIREFLY_APP_KEY is required}
      APP_URL: http://127.0.0.1:${FIREFLY_HOST_PORT:-8086}
      APP_ENV: local
      APP_DEBUG: "false"
      SITE_OWNER: admin@example.com
      TZ: Europe/Berlin
      DB_CONNECTION: pgsql
      DB_HOST: postgres
      DB_PORT: 5432
      DB_DATABASE: ${FIREFLY_DB_NAME:-firefly}
      DB_USERNAME: ${FIREFLY_DB_USER:-firefly_app}
      DB_PASSWORD: ${FIREFLY_DB_PASSWORD:?FIREFLY_DB_PASSWORD is required}
    volumes:
      - firefly_upload:/var/www/html/storage/upload
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - ki-basis-private-net

  paperless:
    image: ghcr.io/paperless-ngx/paperless-ngx@sha256:5ab4f4f9bb099a36bec3e092906ea3e611323c5f18dc5cc38c76a1d540bdca9c
    container_name: ki-basis-private-paperless
    restart: unless-stopped
    ports:
      - "127.0.0.1:${PAPERLESS_HOST_PORT:-8010}:8000"
    environment:
      PAPERLESS_WORKERS: "${PAPERLESS_WORKERS:-1}"
      PAPERLESS_TASK_WORKERS: "${PAPERLESS_TASK_WORKERS:-1}"
      PAPERLESS_THREADS_PER_WORKER: "${PAPERLESS_THREADS_PER_WORKER:-1}"
      PAPERLESS_REDIS: redis://valkey:6379
      PAPERLESS_DBENGINE: postgresql
      PAPERLESS_DBHOST: postgres
      PAPERLESS_DBPORT: 5432
      PAPERLESS_DBNAME: ${PAPERLESS_DB_NAME:-paperless}
      PAPERLESS_DBUSER: ${PAPERLESS_DB_USER:-paperless_app}
      PAPERLESS_DBPASS: ${PAPERLESS_DB_PASSWORD:?PAPERLESS_DB_PASSWORD is required}
      PAPERLESS_SECRET_KEY: ${PAPERLESS_SECRET_KEY:?PAPERLESS_SECRET_KEY is required}
      PAPERLESS_URL: http://127.0.0.1:${PAPERLESS_HOST_PORT:-8010}
      PAPERLESS_TIME_ZONE: Europe/Berlin
      PAPERLESS_OCR_LANGUAGE: deu+eng
      PAPERLESS_ADMIN_USER: ${PAPERLESS_ADMIN_USER:-admin}
      PAPERLESS_ADMIN_PASSWORD: ${PAPERLESS_ADMIN_PASSWORD:?PAPERLESS_ADMIN_PASSWORD is required}
    volumes:
      - paperless_data:/usr/src/paperless/data
      - paperless_media:/usr/src/paperless/media
      - paperless_export:/usr/src/paperless/export
      - paperless_consume:/usr/src/paperless/consume
    depends_on:
      postgres:
        condition: service_healthy
      valkey:
        condition: service_healthy
    healthcheck:
      test: ["CMD", "curl", "-fs", "-S", "--max-time", "2", "http://localhost:8000"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s
    networks:
      - ki-basis-private-net

  openproject:
    image: openproject/openproject@sha256:73d4ee76fb3edb33b0eb1a3a2ddc036f0a45f9083459f445e3d0b634044cf8fb
    container_name: ki-basis-private-openproject
    restart: unless-stopped
    ports:
      - "127.0.0.1:${OPENPROJECT_HOST_PORT:-8082}:80"
    environment:
      OPENPROJECT_WEB_WORKERS: "${OPENPROJECT_WEB_WORKERS:-1}"
      OPENPROJECT_BACKGROUND_WORKERS: "${OPENPROJECT_BACKGROUND_WORKERS:-1}"
      PG_STARTUP_WAIT_TIME: "${PG_STARTUP_WAIT_TIME:-60}"
      OPENPROJECT_HTTPS: "false"
      OPENPROJECT_HOST__NAME: 127.0.0.1:${OPENPROJECT_HOST_PORT:-8082}
      OPENPROJECT_SECRET_KEY_BASE: ${OPENPROJECT_SECRET_KEY_BASE:?OPENPROJECT_SECRET_KEY_BASE is required}
      DATABASE_URL: postgres://${OPENPROJECT_DB_USER:-openproject_app}:${OPENPROJECT_DB_PASSWORD:?OPENPROJECT_DB_PASSWORD is required}@postgres:5432/${OPENPROJECT_DB_NAME:-openproject}
    volumes:
      - openproject_assets:/var/openproject/assets
    depends_on:
      postgres:
        condition: service_healthy
    networks:
      - ki-basis-private-net

  nginx:
    image: nginx@sha256:65645c7bb6a0661892a8b03b89d0743208a18dd2f3f17a54ef4b76fb8e2f2a10
    container_name: ki-basis-private-nginx
    restart: unless-stopped
    ports:
      - "127.0.0.1:${NGINX_HOST_PORT:-8084}:80"
    volumes:
      - ./docker/nginx:/etc/nginx/conf.d:ro
    depends_on:
      - firefly
      - paperless
      - openproject
    healthcheck:
      test: ["CMD", "wget", "-q", "-O", "/dev/null", "http://127.0.0.1:80/healthz"]
      interval: 5s
      timeout: 3s
      retries: 5
      start_period: 5s
    networks:
      - ki-basis-private-net

  hermes:
    image: nousresearch/hermes-agent@sha256:09d743f5e012e41503829d06ca129c7d3e87ea3f943f7228d520c5c53c6f7db5
    container_name: ki-basis-private-hermes
    restart: unless-stopped
    command: gateway run
    ports:
      - "127.0.0.1:${HERMES_GATEWAY_HOST_PORT:-8642}:8642"
      - "127.0.0.1:${HERMES_DASHBOARD_HOST_PORT:-9119}:9119"
    environment:
      HERMES_DASHBOARD: "1"
      HERMES_GATEWAY_EXTERNAL_SUPERVISOR: "1"
      HERMES_GATEWAY_BOOTSTRAP_STATE: "running"
      HERMES_DASHBOARD_BASIC_AUTH_USERNAME: ${HERMES_DASHBOARD_BASIC_AUTH_USERNAME:-admin}
      HERMES_DASHBOARD_BASIC_AUTH_PASSWORD: ${HERMES_DASHBOARD_BASIC_AUTH_PASSWORD:?HERMES_DASHBOARD_BASIC_AUTH_PASSWORD is required}
      HERMES_HOME: /opt/data
      HERMES_WRITE_SAFE_ROOT: /opt/data
      HERMES_DISABLE_LAZY_INSTALLS: "1"
      HERMES_LAZY_INSTALL_TARGET: /opt/data/lazy-packages
      API_SERVER_ENABLED: "true"
      API_SERVER_HOST: "0.0.0.0"
      API_SERVER_KEY: ${HERMES_API_SERVER_KEY:?HERMES_API_SERVER_KEY is required}
      FIREFLY_API_URL: http://firefly:8080
      PAPERLESS_API_URL: http://paperless:8000
      OPENPROJECT_API_URL: http://openproject:80
      TELEGRAM_BOT_TOKEN: ""  # Strictly disabled on Private
      PAPERLESS_TOKEN: ${PAPERLESS_API_TOKEN:-}
      PAPERLESS_URL: http://paperless:8000
      OPENPROJECT_KEY: ${OPENPROJECT_API_KEY:-}
      OPENPROJECT_URL: http://openproject:80
      OPENAI_API_KEY: ${OPENAI_API_KEY:-}
      ANTHROPIC_API_KEY: ${ANTHROPIC_API_KEY:-}
      OPENROUTER_API_KEY: ${OPENROUTER_API_KEY:-}
    volumes:
      - hermes_data:/opt/data
      - hermes_workspaces:/root/workspaces
      - ./scripts:/opt/data/scripts:ro
      - ./SOUL.md:/opt/data/SOUL.md:ro
      - ./skills:/opt/data/skills:ro
    depends_on:
      - firefly
      - paperless
      - openproject
      - nginx
    networks:
      - ki-basis-private-net
```

### 3.4 1-Click Startup Runbook: `private-business/scripts/start.ps1`
```powershell
<#
.SYNOPSIS
    1-Click Startup Script for Private Business Operations (Port Band 808x).
.DESCRIPTION
    Performs fail-closed pre-flight validation on Docker Engine and named ext4
    volumes before launching the Private Commercial stack.
#>
[CmdletBinding()]
param(
    [int]$TimeoutSeconds = 90
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Split-Path -Parent $ScriptDir

Write-Host "=================================================================" -ForegroundColor Cyan
Write-Host "  Starting Private Business Operations Stack (Port Band 808x)... " -ForegroundColor Cyan
Write-Host "=================================================================" -ForegroundColor Cyan

Set-Location $RootDir

# 1. Environment file check
if (-not (Test-Path ".env")) {
    Write-Error "Missing .env file in $RootDir! Copy .env.example to .env and configure credentials."
}

# 2. Docker Desktop Engine Check
Write-Host "==> [PRE-FLIGHT] Checking Docker Engine accessibility..." -ForegroundColor Cyan
$ver = docker info --format "{{.ServerVersion}}" 2>$null
if (-not $ver) {
    Write-Host "Docker Desktop not responding. Launching Docker Desktop..." -ForegroundColor Yellow
    Start-Process "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    $elapsed = 0
    while ($elapsed -lt $TimeoutSeconds) {
        Start-Sleep -Seconds 3
        $elapsed += 3
        $ver = docker info --format "{{.ServerVersion}}" 2>$null
        if ($ver) { break }
    }
    if (-not $ver) { throw "Timed out waiting for Docker Desktop engine." }
}
Write-Host "[PASS] Docker Engine active (Server Version: $ver)" -ForegroundColor Green

# 3. Fail-Closed Ext4 Volume Verification
Write-Host "==> [PRE-FLIGHT] Verifying physical ext4 named volumes..." -ForegroundColor Cyan
$RequiredVols = @(
    "ki-basis-private-postgres-data",
    "ki-basis-private-valkey-data",
    "ki-basis-private-firefly-upload",
    "ki-basis-private-paperless-data",
    "ki-basis-private-paperless-media",
    "ki-basis-private-paperless-export",
    "ki-basis-private-paperless-consume",
    "ki-basis-private-openproject-assets",
    "ki-basis-private-hermes-data",
    "ki-basis-private-hermes-workspaces"
)
foreach ($vol in $RequiredVols) {
    docker volume inspect $vol > $null 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "HALT: Required volume '$vol' not found in DockerDesktop.vhdx! Aborting startup to prevent uninitialized storage creation."
    }
}
Write-Host "[PASS] All 10 persistent ext4 volumes verified present." -ForegroundColor Green

# 4. Launch Containers
Write-Host "==> Launching Private containers via Docker Compose..." -ForegroundColor Cyan
docker compose -p ki-basis-private --env-file .env up -d --remove-orphans

# 5. Service Health Polling (Application Warmup & Edge Verification)
Write-Host "==> Polling backend services for healthy status (Paperless & OpenProject warmup)..." -ForegroundColor Yellow
$healthy = $false
for ($i = 0; $i -lt 30; $i++) {
    Start-Sleep -Seconds 3
    try {
        $edgeRes = Invoke-WebRequest -Uri "http://127.0.0.1:8084/healthz" -UseBasicParsing -TimeoutSec 2 -ErrorAction SilentlyContinue
        $pRes = Invoke-WebRequest -Uri "http://127.0.0.1:8010" -UseBasicParsing -TimeoutSec 2 -ErrorAction SilentlyContinue
        $opRes = Invoke-WebRequest -Uri "http://127.0.0.1:8082" -UseBasicParsing -TimeoutSec 2 -ErrorAction SilentlyContinue
        if ($edgeRes.StatusCode -eq 200 -and ($pRes.StatusCode -in 200, 301, 302) -and ($opRes.StatusCode -in 200, 301, 302)) {
            $healthy = $true
            break
        }
    } catch {}
}

# 6. Service Dashboard Display
Write-Host "`n=================================================================" -ForegroundColor Green
if ($healthy) {
    Write-Host "  Private Business Operations Stack is HEALTHY and READY!        " -ForegroundColor Green
} else {
    Write-Host "  Stack started (services are completing warmup).                " -ForegroundColor Yellow
}
Write-Host "=================================================================" -ForegroundColor Green
Write-Host "  • OpenProject (Client Projects): http://127.0.0.1:8082" -ForegroundColor White
Write-Host "  • Paperless-ngx (Tax Invoices):  http://127.0.0.1:8010" -ForegroundColor White
Write-Host "  • Firefly III (Commercial Bank): http://127.0.0.1:8086" -ForegroundColor White
Write-Host "  • Nginx Edge Proxy:              http://127.0.0.1:8084" -ForegroundColor White
Write-Host "  • Hermes Dashboard:              http://127.0.0.1:9119" -ForegroundColor White
Write-Host "  • Hermes Gateway API:            http://127.0.0.1:8642" -ForegroundColor White
Write-Host "  • Telegram Integration:          DISABLED (Confidentiality Fence)" -ForegroundColor White
Write-Host "=================================================================`n" -ForegroundColor Green
```

### 3.5 1-Click Shutdown Runbook: `private-business/scripts/stop.ps1`
```powershell
<#
.SYNOPSIS
    1-Click Graceful Shutdown Script for Private Business Operations.
#>
[CmdletBinding()]
param()

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$RootDir = Split-Path -Parent $ScriptDir

Set-Location $RootDir
Write-Host "==> Gracefully stopping Private Business Operations Stack..." -ForegroundColor Yellow
docker compose -p ki-basis-private stop
Write-Host "[SUCCESS] Private containers stopped cleanly. All data preserved in ext4 volumes." -ForegroundColor Green
```

### 3.6 Edge Proxy Specification: `private-business/docker/nginx/default.conf`
```nginx
server {
    listen 80;
    server_name localhost 127.0.0.1;

    # Edge healthcheck endpoint
    location = /healthz {
        access_log off;
        add_header Content-Type text/plain;
        return 200 'private-business nginx edge proxy healthy\n';
    }

    # Private Business Stack index page (Port Band 808x only)
    location = / {
        add_header Content-Type text/html;
        return 200 '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Private Business Operations Platform Edge</title><style>body{font-family:system-ui,-apple-system,sans-serif;padding:2rem;background:#0f172a;color:#f8fafc;max-width:900px;margin:0 auto;}h1{color:#38bdf8;margin-bottom:0.25rem;}h2{color:#94a3b8;font-size:1.1rem;margin-top:1.5rem;border-bottom:1px solid #334155;padding-bottom:0.4rem;}a{color:#38bdf8;text-decoration:none;}a:hover{text-decoration:underline;}li{margin:0.6rem 0;}ul{list-style:none;padding:0;}.badge{display:inline-block;padding:0.25rem 0.5rem;border-radius:4px;font-size:0.8rem;font-weight:bold;margin-left:0.5rem;background:#1e3a8a;color:#bfdbfe;}.active-stack{background:#1e293b;border-radius:8px;padding:1.25rem;border:1px solid #38bdf8;margin-bottom:1.5rem;}</style></head><body><h1>Private Business Operations Edge</h1><div class="active-stack"><h2>Commercial Consulting & Corporate Accounting (Port Band 808x)</h2><ul><li><a href="http://127.0.0.1:8082">OpenProject (Client Projects & Timesheets) — :8082</a> <span class="badge">Private</span></li><li><a href="http://127.0.0.1:8010">Paperless-ngx (Tax Invoices & Contracts) — :8010</a> <span class="badge">Private</span></li><li><a href="http://127.0.0.1:8086">Firefly III (Commercial Bank & Ledger) — :8086</a> <span class="badge">Private</span></li><li><a href="http://127.0.0.1:9119">Hermes Dashboard (AI Web) — :9119</a> <span class="badge">Private</span></li><li><a href="http://127.0.0.1:8642">Hermes Gateway (AI API) — :8642</a> <span class="badge">Private</span></li></ul></div></body></html>\n';
    }
}
```

---

## 4. Comprehensive Verification Checklist & Operator Test Battery

The following verification battery enables an operator, DevOps engineer, or QA auditor to validate that isolation and volume preservation hold across both environments:

```
┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                              OPERATIONAL ISOLATION TEST BATTERY                                        │
├──────┬────────────────────────────────────┬────────────────────────────────────────────────────────────┤
│ Step │ Verification Target                │ Verification Command / Procedure                           │
├──────┼────────────────────────────────────┼────────────────────────────────────────────────────────────┤
│ T-01 │ Automated 32-Point Test Suite      │ python ki-basis\scripts\verify_dual_isolation.py           │
│ T-02 │ Physical VHDX File Existence       │ Test-Path C:\ProgramData\DockerDesktop\vm-data\*.vhdx      │
│ T-03 │ 20 Ext4 Volume Registration        │ docker volume ls --filter "name=ki-basis"                  │
│ T-04 │ Port Band 808x Segregation         │ Test-NetConnection 127.0.0.1 -Port 8084                    │
│ T-05 │ Port Band 908x Segregation         │ Test-NetConnection 127.0.0.1 -Port 9084                    │
│ T-06 │ Zero Host DB Port Exposure         │ Test-NetConnection 127.0.0.1 -Port 5432 (Must FAIL)        │
│ T-07 │ Inter-Stack Network Disjointedness │ docker exec ki-basis-comm-hermes ping ki-basis-pvt-postgres│
│ T-08 │ Hermes Persona Divergence          │ docker exec <container> grep "name:" /opt/data/SOUL.md     │
│ T-09 │ Teardown Immunity                  │ docker compose down -v (Verify volumes skipped)            │
│ T-10 │ Git Status Directory Fence         │ git status --short (In standalone directories)             │
└──────┴────────────────────────────────────┴────────────────────────────────────────────────────────────┘
```

### Detailed Execution Commands

```powershell
# ------------------------------------------------------------------------------
# T-01: Execute Automated Dual Isolation Test Suite
# ------------------------------------------------------------------------------
python C:\GitDev\apexai-os-meta\ki-basis\scripts\verify_dual_isolation.py
# Expectation: "VERIFICATION VERDICT: [PASSED] (32 checks passed, 0 failures)"

# ------------------------------------------------------------------------------
# T-03: Verify Registration of all 20 Ext4 Volumes
# ------------------------------------------------------------------------------
$vols = docker volume ls --filter "name=ki-basis" --format "{{.Name}}"
if ($vols.Count -eq 20) {
    Write-Host "[PASS] Exactly 20 ki-basis volumes registered." -ForegroundColor Green
} else {
    Write-Host "[WARN] Found $($vols.Count) volumes registered." -ForegroundColor Yellow
}

# ------------------------------------------------------------------------------
# T-06: Confirm PostgreSQL (:5432) is NOT Exposed on Host
# ------------------------------------------------------------------------------
$pgPort = Test-NetConnection 127.0.0.1 -Port 5432 -WarningAction SilentlyContinue
if (-not $pgPort.TcpTestSucceeded) {
    Write-Host "[PASS] Host port 5432 is closed (Database internal only)." -ForegroundColor Green
} else {
    Write-Host "[FAIL] Host port 5432 is OPEN! Security boundary breached." -ForegroundColor Red
}

# ------------------------------------------------------------------------------
# T-07: Verify Inter-Stack Network Isolation
# ------------------------------------------------------------------------------
docker exec ki-basis-community-hermes ping -c 1 ki-basis-private-postgres 2>&1
# Expectation: "ping: bad address 'ki-basis-private-postgres'" (or 100% packet loss)

# ------------------------------------------------------------------------------
# T-08: Verify Hermes Persona Divergence
# ------------------------------------------------------------------------------
Write-Host "Community Persona:" -ForegroundColor Cyan
docker exec ki-basis-community-hermes grep -E "name:|handle:" /opt/data/SOUL.md
# Expectation: LikasKinkyBot / @LikasSlave_bot

Write-Host "Private Persona:" -ForegroundColor Cyan
docker exec ki-basis-private-hermes grep -E "name:|handle:" /opt/data/SOUL.md
# Expectation: ExecutivePartner
```
