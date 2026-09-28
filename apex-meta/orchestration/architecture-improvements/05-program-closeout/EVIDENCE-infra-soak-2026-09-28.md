---
type: Evidence
title: Post-retirement soak + infra follow-up evidence (T08, T09, T10-inspect, T11)
date: 2026-09-28
method: read-only live checks against the WSL2-native "Apex" engine (`wsl -d Ubuntu -u root -- docker …`)
result: all green; no mutations performed
---

# Infra soak & follow-up evidence — 2026-09-28

All checks below are **read-only**. No container, compose, DB, or `.wslconfig` change was made.

## T11 — Post-retirement soak smoke test → ✅ GREEN

### Live containers (13 running)
Private: `ki-basis-hermes`, `ki-basis-paperless` (healthy), `ki-basis-firefly` (healthy), `ki-basis-nginx`
(healthy), `ki-basis-valkey` (healthy). Community: `community-hermes`, `community-paperless` (healthy),
`community-firefly` (healthy), `community-nginx` (healthy), `community-openproject`, `community-valkey`
(healthy). Shared: `leela-op178-openproject`, `ki-basis-shared-postgres` (healthy).
(hermes/openproject show `Up` without a healthcheck — expected, no healthcheck defined; not "unhealthy".)

### Correctly-stopped containers (not failures)
`ki-basis-postgres` Exited(0) 46h ago (kept stopped per D-18); old `hermes-*` temporaries Exited weeks ago.
The retired v14 `ki-basis-openproject` is **absent** — confirms D-18 deletion.

### Docker Desktop retired
`which docker.exe` → not on PATH ✓ (Docker Desktop uninstalled).

### OpenProject 17.8 reachable
`http://127.0.0.1:8083/` → **HTTP 302 → /login** (serving; auth-gated). Image tag
`openproject/openproject:17.8.0`. 9 live `priv_openproject_app` DB sessions → app is live.

### Hermes reachable
`http://127.0.0.1:8642/health` → **HTTP 200** ✓.

### Cross-DB isolation (REVOKE CONNECT) holds ✓
Via `has_database_privilege(...)` as `postgres` (no app passwords used):
- `priv_openproject_app` → `comm_openproject` CONNECT = **false**
- `comm_openproject_app` → `priv_openproject` CONNECT = **false**
- `comm_firefly_app` → `priv_firefly` CONNECT = **false**
- `priv_openproject_app` → `priv_openproject` CONNECT = **true** (same-stack sanity)

## T08 — WSL memory ceiling 16 GB → ✅ DONE
- `C:\Users\gehma\.wslconfig`: `memory=16GB`, `swap=4GB`.
- Live `docker info` MemTotal = 16,770,523,136 bytes (~15.62 GiB) — consistent with a 16 GB cap after VM overhead. No `wsl --shutdown` needed.

## T09 — Postgres connection baseline → ✅ RECORDED (monitor-only, no action)
Databases: `priv_firefly|openproject|paperless`, `comm_firefly|openproject|paperless`.
Role connection limits & live usage (from `pg_stat_activity`):

| Role | CONNECTION LIMIT | live now | % |
|---|---|---|---|
| priv_openproject_app | 40 | 9 | 23% |
| comm_openproject_app | 40 | 6 | 15% |
| priv_paperless_app | 30 | 2 | 7% |
| comm_paperless_app | 30 | 2 | 7% |
| priv_firefly_app | 20 | 0 | 0% |
| comm_firefly_app | 20 | 0 | 0% |

All well under the 80% threshold that would trigger tuning. No change.

## T10 — Hermes compose-drift (READ-ONLY inspection; still GATED/deferred)
Live `ki-basis-hermes` mounts (via `docker inspect`):
- `bind /root/.hermes -> /opt/data` (**4.4 GB**)
- `bind /root/workspaces -> /root/workspaces` (**3.5 GB**)
Total ~7.9 GB of live bot state on bind mounts, exactly as D-16 documents; `ki-basis/compose.yaml` still
declares **named volumes** for hermes. Drift unchanged. **Do NOT `docker compose up` on `compose.yaml`** —
it would recreate hermes onto empty named volumes and wipe this state. Fix remains operator-gated (T10).
No compose command was run.
