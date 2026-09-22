---
type: Playbook
title: Lika Community Operations Stack — Agent Handover & Operating Guide
description: Standalone operational handover guide for AI agents operating exclusively on the Lika Community stack (Safer Space e.V., Equinox 2026 fundraiser, Paperless receipt staging, and Telegram bot @LikasSlave_bot).
tags: [lika, community, handover, openproject, paperless, telegram, hermes, okf-0.2]
generated: { by: antigravity/gemini-3.7-flash, at: 2026-09-15T13:35:00Z }
sources:
  - id: env-community
    resource: ki-basis/.env.community
    title: Community Operations Environment Configuration
  - id: compose-spec
    resource: ki-basis/compose.yaml
    title: Docker Compose Multi-Instance Specification
  - id: startup-script
    resource: ki-basis/scripts/start-ki-basis.ps1
    title: KI-Basis Dual-Instance Startup Script
  - id: soul-spec
    resource: ki-basis/SOUL.md
    title: Telegram Bot Persona & Bratty Intake Specification
status: stable
---

# Lika Community Operations Stack — Agent Handover & Operating Guide

## 1. Mission & Operational Scope

You are operating exclusively as the infrastructure and automation manager for the **Lika Community Operations Stack** (Safer Space e.V. / Equinox 2026 Fundraiser).

> [!IMPORTANT]
> **Strict Boundary Constraint:**
> * You manage **ONLY Port Band 908x** (`ki-basis-community`).
> * You have **ZERO jurisdiction** over the Private Entrepreneurship stack (Port Band `808x` / `.env.private`).
> * You have **ZERO jurisdiction** over the meta-orchestration frameworks in `apex-meta/orchestration/`.

---

## 2. Active Service Endpoints & Port Band (908x)

| Service | Container Name | Local Endpoint | Purpose in Lika Stack |
| :--- | :--- | :--- | :--- |
| **OpenProject** | `ki-basis-community-openproject` | `http://127.0.0.1:9082` | Project #3: Equinox Fundraiser & volunteer task tracking |
| **Paperless-ngx** | `ki-basis-community-paperless` | `http://127.0.0.1:9010` | Ingesting & OCRing event receipts (Tag: `STAGED-FOR-REVIEW`) |
| **Firefly III** | `ki-basis-community-firefly` | `http://127.0.0.1:9086` | Safer Space e.V. GLS Bank accounts & event budgets |
| **Nginx Edge** | `ki-basis-community-nginx` | `http://127.0.0.1:9084` | Health endpoint: `http://127.0.0.1:9084/healthz` |
| **Hermes Gateway** | `ki-basis-community-hermes` | `http://127.0.0.1:9642` (API)<br>`http://127.0.0.1:9219` (UI) | Frontline AI routing & Telegram intake engine |
| **Telegram Bot** | `@LikasSlave_bot` | *LikasKinkyBot* | Public volunteer receipt & ideation intake channel |
| **PostgreSQL DB** | `ki-basis-community-postgres` | Internal `:5432` | Community relational database (`postgres_data`) |
| **Valkey Queue** | `ki-basis-community-valkey` | Internal `:6379` | Background task queue for Paperless & OCR |

---

## 3. Ground-Truth Configuration & Code Files

* **Environment Configuration:** `ki-basis/.env.community`
* **Docker Compose Definition:** `ki-basis/compose.yaml` (Project Name: `ki-basis-community`)
* **Telegram Persona & Rules:** `ki-basis/SOUL.md`
* **Intake Python Bridge:** `ki-basis/scripts/hermes_telegram_intake.py`
* **Startup / Shutdown Scripts:** `ki-basis/scripts/start-ki-basis.ps1` & `ki-basis/scripts/stop-ki-basis.ps1`

---

## 4. Standard Operational Commands

### Start the Community Stack:
```powershell
powershell -ExecutionPolicy Bypass -File .\ki-basis\scripts\start-ki-basis.ps1 -Instance community
```

### Stop the Community Stack:
```powershell
powershell -ExecutionPolicy Bypass -File .\ki-basis\scripts\stop-ki-basis.ps1 -Instance community
```

### Check Community Stack Health:
```powershell
docker compose -p ki-basis-community -f .\ki-basis\compose.yaml --env-file .\ki-basis\.env.community ps
Invoke-WebRequest -Uri "http://127.0.0.1:9084/healthz" -UseBasicParsing
```

### Verify Telegram Bot Connection:
```powershell
docker logs --tail 30 ki-basis-community-hermes
```

---

## 5. Security & Autonomy Rules

1. **Tiered Autonomy Model:** Hermes acts as frontline intake and staging only. Incoming receipts must be tagged `STAGED-FOR-REVIEW`. No direct or autonomous mutation of Firefly III ledger balances is permitted.
2. **Network Isolation:** The Community stack operates on `ki-basis-community-net`. It must never be bridged to the private business network.
3. **Tailscale Exposure:** Only Community ports (`9082` for OpenProject, `9010` for Paperless) may be shared via Tailscale.
