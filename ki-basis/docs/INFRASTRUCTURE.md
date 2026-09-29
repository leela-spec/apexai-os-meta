---
type: Infrastructure
title: ki-basis Infrastructure — current-state (single source of truth)
description: >
  THE description of what is running now: one WSL2-native Docker engine, one shared PostgreSQL cluster,
  and four compose stacks across four repos. Grounded in the live system (verified 2026-09-28) and ADR-002.
  This file says WHAT IS TRUE NOW; it links down to the ADR (why), the consolidation bundle (history), and
  the compose files (the actual runtime definitions) instead of duplicating them.
status: current
baseline: "Environment created 2026-09-26 (ADR-002 consolidation) + the optimizations that followed. Anything predating that which conflicts with this file is superseded history."
authority_order: "LIVE running system > this file > ADR-002 §6 (decision record) > older/superseded docs. If a doc disagrees with the live system, the doc is wrong."
verified: "2026-09-28 via tests/…/infra-health-test.sh (GREEN 29/29)"
canonical: "This is the single infra-description entrypoint. Superseded infra docs point here."
---

# ki-basis Infrastructure — current state

> **How to keep this current:** re-run `apex-meta/orchestration/architecture-improvements/05-program-closeout/tests/infra-health-test.sh`
> (read-only). If it disagrees with this file, **the live system wins** — update this file, not your mental model.
> Do not ground current architecture in older docs; superseded ones carry a banner pointing back here.

## 1. At a glance
- **One engine:** a single WSL2-native "Apex" Docker daemon (Ubuntu distro). **Docker Desktop is retired/uninstalled.** Compose v2.40.3.
- **One shared database:** a single PostgreSQL 16 cluster (`ki-basis-shared-postgres`) with per-tenant `priv_*`/`comm_*` databases + roles; cross-tenant `CONNECT` revoked.
- **Four compose stacks** (separate projects on the one engine):

| Stack | Compose project | Repo / compose file | Role |
|---|---|---|---|
| Private ki-basis | `ki-basis` | `apexai-os-meta/ki-basis/compose.shared-db.yaml` | private ops: valkey, firefly, paperless, nginx, **Hermes** |
| Community | `community` | `lika-community/compose.wsl.yaml` | community ops: valkey, firefly, paperless, openproject, nginx, **Hermes** |
| Private OpenProject | `leela-op178` | `leela-op178/compose.shared-db.yaml` | private PM authority — **OpenProject 17.8** |
| Shared PostgreSQL | `ki-basis-infra` | `ki-basis-shared/compose.yaml` | the one shared DB cluster |

## 2. Engine (WSL2 "Apex")
- Runs as the `Ubuntu` distro's native `dockerd`. Invoke: `wsl -d Ubuntu -u root -- docker …`.
- Docker Desktop uninstalled (ADR-002); `docker.exe` is not on the Windows PATH.
- Host memory cap: `C:\Users\gehma\.wslconfig` → `memory=16GB`, `swap=4GB` (changing it needs `wsl --shutdown` = stops ALL stacks → operator-gated).
- **Keepalive (cold-boot avoidance):** WSL2 idle-sleeps its VM (~80 s cold boot). Only a **Windows-held `wsl.exe` session** resets the idle timer. Held by `%APPDATA%\…\Startup\wsl-keepalive.vbs` (hidden, no admin, self-healing: relaunches a `sleep infinity` session within 5 s if it dies). A secondary in-VM systemd service `openproject-keepalive` pings OpenProject warm. To disable: delete the `.vbs`.

## 3. Shared data layer
- **Cluster:** `ki-basis-shared-postgres` (image `pgvector/pgvector:pg16`), compose project `ki-basis-infra`, repo `ki-basis-shared`. **Internal only** on the external `shared-db-net` bridge at `postgres:5432` — no host port. Volume `ki-basis-infra_shared_pgdata` (compose key `shared_pgdata`, project-prefixed). Secrets in `ki-basis-shared/.env` (never commit/print).
- **Databases / roles:** `priv_firefly|openproject|paperless`, `comm_firefly|openproject|paperless`, each with a matching `*_app` role.
- **Isolation:** cross-tenant `REVOKE CONNECT` — a tenant's app role cannot connect to the other tenant's DB (verified live). Role connection limits: firefly 20, paperless 30, openproject 40 (live usage ≤18%).
- **Network:** `shared-db-net` is `external: true` — a manually-created network owned by **no** compose project — create it once (`docker network create shared-db-net`) before any stack that joins it comes up.

## 4. The four stacks (live detail)

### 4.1 Private ki-basis — project `ki-basis`
- File: `apexai-os-meta/ki-basis/compose.shared-db.yaml` · env `.env.shared-db` · `-p ki-basis`.
  (`compose.yaml` in the same dir is a **superseded rollback file** — do not `up` it; see D-16/T10.)
- Services & host ports (loopback): firefly `8086`, paperless `8010`, nginx `8084`, **Hermes gateway `8642` + dashboard `9119`**. valkey internal.
- Networks: hermes/nginx/valkey on `ki-basis-net`; firefly/paperless also on `shared-db-net`.
- **Hermes storage = BIND mounts** (T10): `/root/.hermes → /opt/data` (~4.4 GB), `/root/workspaces → /root/workspaces` (~3.5 GB) on WSL2 ext4. Other services use named volumes.
- Private OpenProject is **not** in this stack — Hermes points at `leela-op178-openproject` (§4.3).

### 4.2 Community — project `community`
- File: `lika-community/compose.wsl.yaml` · env `.env.wsl` · `-p community` (separate repo).
- Services & host ports (loopback): firefly `9086`, paperless `9010`, openproject `9082`, nginx `9084`, **Hermes gateway `9642` + dashboard `9219`**. valkey internal.
- Networks: `community_internal`; firefly/paperless/openproject also on `shared-db-net`.
- **Hermes storage = named volumes** `community_hermes_data`/`community_hermes_workspaces` (+ `community_call_agenda`) plus read-only config binds from the `lika-community` repo (`SOUL.md`, `scripts/`, `skills/*`, `docker/hermes/run.py`). This asymmetry vs private is deliberate (community migrated fresh; private preserved its bind state — D-14/D-16). Do not "harmonize."

### 4.3 Private OpenProject — project `leela-op178`
- File: `leela-op178/compose.shared-db.yaml` · `-p leela-op178`. Image **OpenProject 17.8.0**; DB `priv_openproject` on the shared cluster.
- Host port `0.0.0.0:8083 → 80` (browse **`http://127.0.0.1:8083`**, not `localhost`, due to the host-check).
- Networks: `ki-basis-net` (so private Hermes reaches it by name) + `leela-op178_default` + `shared-db-net`.
- Named "leela" but it is **shared PM infrastructure** (hosts the org-wide project tree; private Hermes → `OPENPROJECT_API_URL=http://leela-op178-openproject:80`). The old v14 `ki-basis-openproject` was deleted (D-18).

### 4.4 Shared PostgreSQL — project `ki-basis-infra`
See §3.

## 5. Sibling-repo map (where infra lives on disk)
| Repo | Holds |
|---|---|
| `apexai-os-meta/ki-basis/` | private stack compose + env + scripts + **this file** + the ADR |
| `apexai-os-meta/apex-meta/orchestration/architecture-improvements/` | consolidation bundle (03), close-out (05), tests |
| `lika-community/` | community stack (own repo: compose, env, persona, skills) |
| `leela-op178/` | private OpenProject 17.8 (compose, `op.env`, backups) |
| `ki-basis-shared/` | the shared PostgreSQL cluster (compose + `.env`) |

## 6. Ports (host, all loopback except where noted)
| Service | Private (`ki-basis`) | Community | Shared / other |
|---|---|---|---|
| Firefly | 8086 | 9086 | — |
| Paperless | 8010 | 9010 | — |
| OpenProject | via leela-op178 → **8083** | 9082 | — |
| Nginx | 8084 | 9084 | — |
| Hermes gateway / dashboard | 8642 / 9119 | 9642 / 9219 | — |
| PostgreSQL | — | — | 5432 (internal only, no host port) |

## 7. Start / stop / health
- **Private stack:** `ki-basis/scripts/start-ki-basis-shared-db.ps1` / `stop-ki-basis-shared-db.ps1`
  (run from Windows; they route through WSL). The old `start-/stop-ki-basis.{sh,ps1}` are **fail-closed guarded** (they targeted the superseded `compose.yaml`).
- **Community:** managed from `lika-community` (`docker compose -f compose.wsl.yaml --env-file .env.wsl -p community up -d`).
- **Private OpenProject:** see `leela-op178` runbook (below).
- **Prerequisite for any stack that joins `shared-db-net`:** the `ki-basis-infra` (shared Postgres) project must be up first.
- **Health (read-only, re-runnable):** `…/05-program-closeout/tests/infra-health-test.sh`.

## 8. Links (single source → supporting layers)
- **Why / decisions:** `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` §6 (ADR-002) — the decision record.
- **How it got here / verified topology + D-01…D-18:** `apex-meta/orchestration/architecture-improvements/03-wsl2-native-stack-consolidation/`.
- **Close-out + T10 (Hermes drift) + this audit:** `apex-meta/orchestration/architecture-improvements/05-program-closeout/`.
- **Runtime definitions (authoritative for services/volumes/networks):** the four `compose*.yaml` in §1.
- **OpenProject 17.8 operations:** the `leela-op178` runbook at `ki-basis/docs/openproject/` (`RUNBOOK-openproject-17.8-operations.md`; the OpenProject infra cluster was moved here from the Leela repo 2026-09-29).
- **Tests:** `…/05-program-closeout/tests/` (`infra-health-test.sh`, `doc-integrity-lint.sh`).
