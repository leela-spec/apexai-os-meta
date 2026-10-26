---
okf_version: "0.2"
type: runbook
title: OpenProject 17.8 (leela-op178) — operations runbook
description: Start/stop/health, keepalive, memory config, backup/recovery, ports, and known gaps for the private Leela OpenProject 17.8 instance on the WSL2 Apex engine.
tags: [openproject, leela, runbook, wsl2, operations]
status: current
date: 2026-09-28
updated: 2026-10-08
scope: "private OpenProject 17.8 instance `leela-op178-openproject`; the Leela PM authority"
---

# OpenProject 17.8 operations runbook — `leela-op178`

The private Leela PM instance. **OpenProject 17.8.0**, container `leela-op178-openproject`, its own
Compose project (`-p leela-op178`), pointed at `priv_openproject` on the shared WSL2 Postgres cluster.
Reachable from the Windows host at **http://127.0.0.1:8083**.

> All `docker` commands run on the single WSL2-native "Apex" engine:
> `wsl -d Ubuntu -u root -- docker …`. Docker Desktop is retired (ADR-002).

## 1. Key facts
| | |
|---|---|
| Container | `leela-op178-openproject` (Compose service key: `leela-openproject`) |
| Image | `openproject/openproject:17.8.0` |
| Compose file | `C:\GitDev\leela-op178\compose.shared-db.yaml` (project `leela-op178`, `--env-file .env.shared-db`) |
| URL (host) | http://127.0.0.1:8083 (published `0.0.0.0:8083:80`; Hyper-V firewall default-deny inbound = host-only) |
| Health endpoint | http://127.0.0.1:8083/health_checks/default |
| Cache | `OPENPROJECT_RAILS__CACHE__STORE=memcache` (in-container `memcached` on `127.0.0.1:11211`) |
| Database | `priv_openproject` on `ki-basis-shared-postgres` (`postgres:5432`), role `priv_openproject_app` |
| Networks | `default`, `shared-db-net` (external; aliases `leela-op178-openproject`, `leela-openproject`), `ki-basis-net` (external — lets `ki-basis-hermes` reach it by name) |
| API token | `~/.config/openproject/op.env` (= `C:\Users\<you>\.config\openproject\op.env`; auto-loaded by the skill) — **secret, never print/commit**. Migration source `C:\GitDev\leela-op178\op.env` retained. |
| DB password | `OPENPROJECT_DB_PASSWORD` via `.env.shared-db` — **secret** |

## 2. Start / stop / restart
```bash
# Prerequisite: ensure external shared-db-net exists before stack bring-up
wsl -d Ubuntu -u root -- docker network inspect shared-db-net >/dev/null 2>&1 \
  || wsl -d Ubuntu -u root -- docker network create shared-db-net

# Start (idempotent)
wsl -d Ubuntu -u root -- sh -lc 'cd /mnt/c/GitDev/leela-op178 && MSYS_NO_PATHCONV=1 docker compose -f compose.shared-db.yaml --env-file .env.shared-db -p leela-op178 up -d'
# Stop (keeps data; container + volumes preserved)
wsl -d Ubuntu -u root -- docker stop leela-op178-openproject
# Restart
wsl -d Ubuntu -u root -- docker restart leela-op178-openproject

# Poll until HTTP answers (cold WSL boot ~80s, warm container restart ~35s)
wsl -d Ubuntu -u root -- bash -lc '
  for i in $(seq 1 40); do
    code=$(curl -sS -o /dev/null -w "%{http_code}" --max-time 2 http://127.0.0.1:8083/health_checks/default || true)
    echo "try $i -> $code"
    case "$code" in 200) exit 0;; esac
    sleep 2
  done
  echo "TIMEOUT"; exit 1
'
```
`restart: unless-stopped` — a manual `stop` is honoured across daemon/VM restarts (it will NOT auto-start
until you `start`/`up` it again).

> ⚠️ **Do not** run `docker compose down -v` — `-v` would delete the `pgdata`/`assets` volumes. (The `pgdata`
> volume is currently *unused* — `DATABASE_URL` points at the shared cluster — but `assets` holds uploaded
> attachments. `down` without `-v` is safe; `down -v` is destructive.)
>
> ⚠️ **Do not** pass `--remove-orphans` to `docker compose` on the shared WSL2 engine (R4/R5 guard).

## 3. Health, version & cache diagnostics
```bash
# Quick health from WSL (expect HTTP 200)
wsl -d Ubuntu -u root -- sh -lc 'curl -s -o /dev/null -w "%{http_code}\n" --max-time 8 http://127.0.0.1:8083/health_checks/default'
# Reachability from WSL (expect 302 -> /login when healthy but unauthenticated)
wsl -d Ubuntu -u root -- sh -lc 'curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8083/'
# Version (image ref is authoritative)
wsl -d Ubuntu -u root -- docker inspect leela-op178-openproject --format 'image={{.Config.Image}}'
# Rails cache backend check (when debugging staleness; expect OPENPROJECT_RAILS__CACHE__STORE=memcache)
wsl -d Ubuntu -u root -- docker exec leela-op178-openproject env | grep -i CACHE
wsl -d Ubuntu -u root -- docker exec leela-op178-openproject bash -lc "ps aux | grep -i memcached | grep -v grep"
```
```powershell
# Mandatory reachability check from Windows host (guards against R11 WSL2 localhost forwarding drop):
curl.exe -sS -o NUL -w "%{http_code}`n" --max-time 5 http://127.0.0.1:8083/health_checks/default
```
Helper scripts in `C:\GitDev\leela-op178\`: `check.sh` (5× consecutive health + restart count),
`version.sh` (image + in-container version + API root), `wait.sh` (poll `/health_checks/default`).

## 3.1 Standard Procedure: Memcache TCP Flush (After Project / Type Admin Changes)
In OpenProject 17.8.0, `ProjectType` (`/app/app/models/project_type.rb`) does not declare `touch: true` on `belongs_to :project`. Enabling or disabling work-package types on a project updates PostgreSQL immediately but leaves `projects.updated_at` unchanged, so `API::Caching::CachedRepresenter` serves stale representations from in-container `memcached` (`127.0.0.1:11211`).

Whenever project/type associations are modified in the UI or via `rails runner`, flush in-container `memcached` over TCP (0s downtime, no 80s container restart required):
```bash
wsl -d Ubuntu -u root -- docker exec leela-op178-openproject \
  bash -lc "printf 'flush_all\r\n' | timeout 2 bash -c 'cat > /dev/tcp/127.0.0.1/11211'"
```

## 3.2 Default Work-Package Types for New Projects (`is_default`)
All 7 work-package types (`Task`, `Milestone`, `Summary task`, `Feature`, `Epic`, `User story`, `Bug`) are permanently configured with `is_default: true` ("Active in new projects") via `WorkPackageTypes::MakeDefaultService`. Because OpenProject 17.8.0's legacy `TableComponent` omits the UI toggle when `type_variants_active?` is `false`, any future custom type can be marked default for new projects via:
```bash
wsl -d Ubuntu -u root -- docker exec leela-op178-openproject bundle exec rails runner '
  Type.where(name: ["Feature", "Epic", "User story", "Bug"]).find_each do |t|
    WorkPackageTypes::MakeDefaultService.new(type: t, user: User.system).call
  end
'
```

## 4. Keepalive (cold-boot avoidance)
WSL2 idle-sleeps its VM; a cold boot costs **~80 s** before OpenProject answers. A Windows-held
`wsl.exe` session is what resets the idle timer (in-VM processes do not).

- Keepalive: `%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup\wsl-keepalive.vbs` — runs hidden at
  login, holds `wsl.exe -d Ubuntu -u root --exec /bin/sleep infinity`, and self-heals (relaunches within
  5 s if the VM restarts). **To disable:** delete that `.vbs`.
- If the instance is slow on first hit after a reboot, confirm the keepalive session is running:
  `wsl -d Ubuntu -u root -- pgrep -af "sleep infinity"`.

## 5. Memory / WSL & Puma Config
- **Host WSL ceiling:** `C:\Users\gehma\.wslconfig`: `memory=16GB`, `swap=4GB` (ceiling, not reservation — idle ~1 GB). Changing `.wslconfig` requires `wsl --shutdown` to take effect (stops ALL stacks — operator-gated). Verify live ceiling: `wsl -d Ubuntu -u root -- docker info --format '{{.MemTotal}}'` (~15.62 GiB = 16 GB cap).
- **Container memory, allocator & service tuning (`compose.shared-db.yaml` — Option 2A):**
  - `OPENPROJECT_WEB_WORKERS: "0"` (Puma single-mode — master serves requests directly without forking a second 600 MB cluster worker process)
  - `OPENPROJECT_WEB__MAX__THREADS: "4"` and `OPENPROJECT_GOOD__JOB__MAX__THREADS: "2"` (caps Puma from 16 threads to 4 and GoodJob from 20 threads to 2; `OPENPROJECT_BACKGROUND_WORKERS` is a legacy no-op under GoodJob)
  - `USE_JEMALLOC: "true"` (`LD_PRELOAD=libjemalloc.so.2` via `entrypoint.sh`) + `MALLOC_CONF: "narenas:2,dirty_decay_ms:1000,muzzy_decay_ms:0,background_thread:true"` (caps `jemalloc 5.3.0` from 33 arenas to 2 and enables `jemalloc_bg_thd` background purging; `muzzy_decay_ms:0` forces `madvise(MADV_DONTNEED)` instead of `MADV_FREE` so Linux cgroup v2 immediately unmaps freed pages from `anon` and `memory.current`; `MALLOC_ARENA_MAX: "2"` retained for non-preloaded helper binaries)
  - **Collaborative Editing (`hocuspocus`) intentionally disabled on Private:** `OPENPROJECT_COLLABORATIVE__EDITING__HOCUSPOCUS__URL: ""` + `- ./disable-hocuspocus.sh:/app/docker/prod/hocuspocus:ro` disables the bundled `hocuspocus` Node/tsx/esbuild real-time WebSocket server (`~214.8 MiB` kernel PSS / `~321.1 MiB` gross summed RSS and `32` threads). Standard work-package and document editing work normally; only simultaneous multi-user live-cursor co-editing is disabled. To re-enable if ever needed: remove `OPENPROJECT_COLLABORATIVE__EDITING__HOCUSPOCUS__URL` and the `disable-hocuspocus.sh` volume line from `compose.shared-db.yaml` and run `docker compose -f compose.shared-db.yaml up -d` (raise `mem_limit` to `1792M` first).
  - `mem_limit: 1536M` (non-reclaimable anonymous heap `anon` is `1.13 GiB` right after boot and decays to **`~926 MiB` `anon` / `~996 MiB` total `memory.current`** [`504.6 MiB` Puma PSS + `425.6 MiB` GoodJob PSS] at idle steady-state, leaving **`380–540 MiB`** of true spike headroom before OOM/swap)
  - Full rationale and live benchmarks: `apex-meta/orchestration/architecture-improvements/05-program-closeout/FINDINGS-openproject-memory-and-178-inefficiencies-2026-10-08.md`.

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
- **Resolved (2026-10-08) — `shared-db-net` DNS alias collision:** `leela-op178/compose.shared-db.yaml` now uses Compose service key `leela-openproject` (`Aliases: ["leela-op178-openproject", "leela-openproject"]`), eliminating the duplicate `openproject` DNS alias with `community-openproject` on `shared-db-net`.
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

## 9. Known landmines (do not re-learn)
| ID | Risk | Rule |
|---|---|---|
| DNS alias | `leela-op178-openproject` and `community-openproject` colliding on `openproject` alias on `shared-db-net` | Keep `leela-op178` service key as `leela-openproject` (`compose.shared-db.yaml`); always address container by `leela-op178-openproject` |
| R4 | Copy-paste compose resurrects old OP / wrong DB | Reference container by **name** `leela-op178-openproject`; never introduce a second `postgres` alias |
| R5 | Hermes volume drift | Pre-`up` check mount type vs compose before restarting `ki-basis` |
| R11 | Windows `ECONNREFUSED :8083` | Prove reachability **from Windows** (`curl.exe`), not only from inside WSL |
| Status theatre | "Preflight DONE" without live curl | Live HTTP health check + skill `doctor` / read = definition of done |
| `ProjectType` cache | `ProjectType` omits `touch: true` on `belongs_to :project` in 17.8.0 | Run §3.1 `flush_all` over `/dev/tcp/127.0.0.1/11211` after project/type changes |
| GoodJob threads | `OPENPROJECT_BACKGROUND_WORKERS` does not cap threads in 17.8 | Use `OPENPROJECT_GOOD__JOB__MAX__THREADS` and `OPENPROJECT_WEB__MAX__THREADS` (§5) |
| Hocuspocus disabled | Real-time multi-user Collaborative Editing is intentionally disabled on Private via `./disable-hocuspocus.sh:/app/docker/prod/hocuspocus:ro` | Do not troubleshoot missing real-time co-editing on Private unless re-enabled; on major OP image upgrades (`17.8` → `18.x`), verify `/app/docker/prod/supervisord.conf.erb` still invokes `./docker/prod/hocuspocus` |

## 10. Verification checklist (after any OP change)
- [ ] `docker ps` shows `leela-op178-openproject` Up
- [ ] `curl` from WSL to `http://127.0.0.1:8083/health_checks/default` returns `200`
- [ ] `curl.exe` from **Windows** to `http://127.0.0.1:8083/health_checks/default` returns `200`
- [ ] Canonical skill check (`doctor`, `project.list`, `type.list`) succeeds via `C:\GitDev\agent-skills\skills\openproject\client\opCall.js`
- [ ] Live Puma `/proc/<pid>/environ` & `jemalloc_bg_thd` verified: `wsl -d Ubuntu -u root -- docker exec -u app leela-op178-openproject bash -lc 'pid=$(pgrep -f "puma.*8080"); xargs -0 -n1 -a /proc/$pid/environ | grep -E "LD_PRELOAD|MALLOC_CONF"; ps -T -p $pid -o pid,spid,comm'`
- [ ] If types/admin changed: run §3.1 memcache TCP flush and verify via API v3 without container restart
- [ ] If DNS/compose touched: `docker inspect leela-op178-openproject --format '{{json .NetworkSettings.Networks}}'` confirms no ambiguous `openproject` alias on `shared-db-net`

