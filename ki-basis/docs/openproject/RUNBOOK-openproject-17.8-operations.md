---
okf_version: "0.2"
type: runbook
title: OpenProject 17.8 (leela-op178) — operations runbook
description: Start/stop/health, keepalive, memory config, backup/recovery, ports, and known gaps for the private Leela OpenProject 17.8 instance on the WSL2 Apex engine.
tags: [openproject, leela, runbook, wsl2, operations]
status: current
date: 2026-09-28
scope: "private OpenProject 17.8 instance `leela-op178-openproject`; the Leela PM authority"
---

# OpenProject 17.8 operations runbook — `leela-op178`

The private Leela PM instance. **OpenProject 17.8.0**, container `leela-op178-openproject`, its own
Compose project (`-p leela-op178`), pointed at `priv_openproject` on the shared WSL2 Postgres cluster.
Reachable from the Windows host at **http://127.0.0.1:8083**.

> All `docker` commands run on the single WSL2-native "Apex" engine:
> `wsl -d Ubuntu -u root -- docker …`. There is no Docker Desktop.

## 1. Key facts
| | |
|---|---|
| Container | `leela-op178-openproject` |
| Image | `openproject/openproject:17.8.0` |
| Compose file | `C:\GitDev\leela-op178\compose.shared-db.yaml` (project `leela-op178`, `--env-file .env.shared-db`) |
| URL (host) | http://127.0.0.1:8083 (published `0.0.0.0:8083:80`; Hyper-V firewall default-deny inbound = host-only) |
| Health endpoint | http://127.0.0.1:8083/health_checks/default |
| Database | `priv_openproject` on `ki-basis-shared-postgres` (`postgres:5432`), role `priv_openproject_app` |
| Networks | `default`, `shared-db-net` (external), `ki-basis-net` (external — lets `ki-basis-hermes` reach it by name) |
| API token | `~/.config/openproject/op.env` (= `C:\Users\<you>\.config\openproject\op.env`; auto-loaded by the skill) — **secret, never print/commit**. Migration source `C:\GitDev\leela-op178\op.env` retained. |
| DB password | `OPENPROJECT_DB_PASSWORD` via `.env.shared-db` — **secret** |

## 2. Start / stop / restart
```bash
# Start (idempotent)
wsl -d Ubuntu -u root -- sh -lc 'cd /mnt/c/GitDev/leela-op178 && MSYS_NO_PATHCONV=1 docker compose -f compose.shared-db.yaml --env-file .env.shared-db -p leela-op178 up -d'
# Stop (keeps data; container + volumes preserved)
wsl -d Ubuntu -u root -- docker stop leela-op178-openproject
# Restart
wsl -d Ubuntu -u root -- docker restart leela-op178-openproject
```
`restart: unless-stopped` — a manual `stop` is honoured across daemon/VM restarts (it will NOT auto-start
until you `start`/`up` it again).

> ⚠️ **Do not** `docker compose down -v` — `-v` would delete the `pgdata`/`assets` volumes. (The `pgdata`
> volume is currently *unused* — `DATABASE_URL` points at the shared cluster — but `assets` holds uploaded
> attachments. `down` without `-v` is safe; `down -v` is destructive.)

## 3. Health & version
```bash
# Quick health (expect HTTP 200)
wsl -d Ubuntu -u root -- sh -lc 'curl -s -o /dev/null -w "%{http_code}\n" --max-time 8 http://127.0.0.1:8083/health_checks/default'
# Reachability (expect 302 -> /login when healthy but unauthenticated)
wsl -d Ubuntu -u root -- sh -lc 'curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8083/'
# Version (image ref is authoritative)
wsl -d Ubuntu -u root -- docker inspect leela-op178-openproject --format 'image={{.Config.Image}}'
```
Helper scripts in `C:\GitDev\leela-op178\`: `check.sh` (5× consecutive health + restart count),
`version.sh` (image + in-container version + API root).

## 4. Keepalive (cold-boot avoidance)
WSL2 idle-sleeps its VM; a cold boot costs **~80 s** before OpenProject answers. A Windows-held
`wsl.exe` session is what resets the idle timer (in-VM processes do not).

- Keepalive: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\wsl-keepalive.vbs` — runs hidden at
  login, holds `wsl.exe -d Ubuntu -u root --exec /bin/sleep infinity`, and self-heals (relaunches within
  5 s if the VM restarts). **To disable:** delete that `.vbs`.
- If the instance is slow on first hit after a reboot, confirm the keepalive session is running:
  `wsl -d Ubuntu -u root -- pgrep -af "sleep infinity"`.

## 5. Memory / WSL config
`C:\Users\gehma\.wslconfig`: `memory=16GB`, `swap=4GB` (ceiling, not reservation — idle ~1 GB).
Changing `.wslconfig` requires `wsl --shutdown` to take effect (stops ALL stacks — operator-gated).
Verify live ceiling: `wsl -d Ubuntu -u root -- docker info --format '{{.MemTotal}}'` (~15.62 GiB = 16 GB cap).

## 6. Backup / recovery
- DB backup: `C:\GitDev\leela-op178\backup-private-dbs.sh` (dumps `priv_*` incl. `priv_openproject`).
- DB restore: `restore-private-dbs.sh` / `finish-priv-restore.sh` (see decision D-15 in the apexai-os-meta
  `03-wsl2-native-stack-consolidation` bundle for the per-dump extension/role handling — `priv_openproject`
  needs a **pg17-capable** `pg_restore`).
- Instant config rollback to the embedded DB: remove `DATABASE_URL` + `compose.shared-db.yaml`, revert to
  `compose.yaml`; the embedded `pgdata` is untouched (see the file header comment).
- Attachments live in the `assets` volume — include it in any full-restore plan.

## 7. Ports (WSL2 Apex engine, host-forwarded)
| Service | Host port |
|---|---|
| **OpenProject 17.8 (this instance)** | **8083** |
| Community OpenProject | 9082 |
| ki-basis nginx / firefly / paperless | 8084 / 8086 / 8010 |
| ki-basis Hermes gateway / dashboard | 8642 / 9119 |
| community nginx / firefly / paperless | 9084 / 9086 / 9010 |
| community Hermes gateway / dashboard | 9642 / 9219 |
| shared Postgres | 5432 (internal) |

## 8. Known gaps / follow-ups
- **`SECRET_KEY_BASE` is a hardcoded literal** in `compose.shared-db.yaml` — should move to the `.env`
  file like the DB password. (File is outside the git repos, so not committed, but still a hygiene gap.)
- **Admin token still in use** — the pilot uses an admin API token in `op.env`. Replacing it with a scoped
  non-admin identity is **deferred by operator decision (2026-09-28)** → see
  [`FUTURE-DEVELOPMENT-least-privilege-agent-identity.md`](FUTURE-DEVELOPMENT-least-privilege-agent-identity.md)
  (program T13). Revisit when agents run more autonomously or the instance is exposed/shared.
- **Write-autonomy policy is provisional** (all mutations require `--confirmed`) → program **T16**.
- **Host-only reachability**: only from the Windows host via localhost forwarding; not exposed to LAN
  (Hyper-V firewall default-deny inbound). Remote access would need a deliberate, separate decision.
- Agent skill for operating this instance: canonical `C:\GitDev\agent-skills\skills\openproject\`, linked into each agent's global dir (portable Node API-v3 client). See `agent-skills/README.md`.
