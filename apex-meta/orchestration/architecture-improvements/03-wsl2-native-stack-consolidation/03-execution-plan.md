---
type: Runbook
title: Execution plan — consolidate onto WSL2-native with a shared PostgreSQL
description: Safely-ordered, rollback-pointed migration runbook to move the community stack onto the WSL2 "Apex" engine, run both stacks against one shared PostgreSQL (separate databases), and retire Docker Desktop.
tags: [runbook, migration, docker, wsl2, postgres, backup, docker-desktop]
status: draft
generated: { by: "claude/opus-4.8", at: "2026-09-26" }
stale_after: "2026-10-31"
sources:
  - id: migration-research
    resource: "process:subagent-web-research/consolidation-best-practice/2026-09-26"
    title: Migration best-practice research (cited inline)
  - id: decisions
    resource: /02-decisions-log.md
    title: Decision ledger
---

# Execution plan

> **Gate:** Do **not** start until [Q1–Q3](04-open-questions.md) are answered — especially whether a
> shared Postgres is accepted (D-P1) and what "stop 172.18" (D-P3) means. Steps 0–5 are
> non-destructive and reversible; the community engine stays intact and startable until Step 9.
> Each step names its rollback. Commands assume you run `docker` inside the WSL2 "Apex" engine
> unless noted; replace passwords/paths with real values kept in `.env` (never committed).

## Preconditions to verify first

- [ ] Q1 (shared Postgres accepted, isolation trade understood), Q2 (which 172.18 to stop), Q3
      ("remove docker from ubuntu" = retire Docker **Desktop**) answered in [Q&A](04-open-questions.md).
- [ ] Both community DBs are on `pg16` (they are, per current images) — logical dump/restore works
      regardless, but confirm no major-version surprise.
- [ ] Free disk for dumps + volume tarballs (check OpenProject assets + Paperless media sizes).

## Phase 0 — Prepare the WSL2 engine as the single home
1. Ensure systemd + docker autostart (already true here: `/etc/wsl.conf [boot] systemd=true`,
   `systemctl is-enabled docker` = enabled). Confirm `docker context use default` (native socket).
2. Confirm `.wslconfig` memory ceiling is right for **two stacks + shared Postgres** — 12 GB may be
   tight; research suggests up to ~20 GB with `autoMemoryReclaim=gradual` (see [Q7](04-open-questions.md#q7)).
   *Rollback:* revert `/etc/wsl.conf` / `.wslconfig`; no data touched.

## Phase 1 — Stand up the shared PostgreSQL (infra project)
Pattern: a small `infra` compose owns the shared Postgres on an **external** docker network; each
stack joins that network *for DB access only* and keeps its own private bridge.
```bash
docker network create shared-db-net
# infra/compose.yaml: pgvector/pgvector:pg16 on shared-db-net, named volume pgdata, POSTGRES_PASSWORD from .env
docker compose -p infra up -d
```
Create one role + one database per app, deny cross-DB connect:
```sql
CREATE ROLE openproject LOGIN PASSWORD '...' CONNECTION LIMIT 40;
CREATE ROLE firefly     LOGIN PASSWORD '...' CONNECTION LIMIT 20;
CREATE ROLE paperless   LOGIN PASSWORD '...' CONNECTION LIMIT 30;
CREATE DATABASE openproject OWNER openproject;  -- repeat firefly, paperless
REVOKE CONNECT ON DATABASE openproject FROM PUBLIC;  -- repeat; then GRANT CONNECT to its own role
```
Size the cluster to the **sum** of all app pools (not per-app): start `max_connections=200`,
`shared_buffers≈2GB`, `effective_cache_size≈4–6GB`, `maintenance_work_mem≈512MB–1GB` (pgvector index
builds). *Rollback:* `docker compose -p infra down -v` removes it cleanly.

> If D-P1 is **rejected** (keep per-stack Postgres), skip the shared cluster; instead run each stack's
> own postgres service on the WSL2 engine on isolated networks. The rest of the plan is unchanged
> except restores target each stack's own postgres.

## Phase 2 — Back up the community stack (D-P2) — **primary rollback artifact**
While the community Postgres is still running on Docker Desktop:
```bash
# roles/passwords once, then per-DB custom-format dumps (set encoding explicitly)
docker exec -t ki-basis-community-postgres pg_dumpall -U postgres --globals-only > globals.sql
for db in openproject firefly paperless; do
  docker exec -t ki-basis-community-postgres pg_dump -U postgres -Fc --encoding=UTF8 "$db" > "community_$db.dump"
done
```
Verify each: `pg_restore -l community_openproject.dump | head` (TOC lists), non-zero sizes.
Back up non-DB volumes (stop the writer first) via the `tar --volumes-from` pattern:
```bash
docker run --rm -v ki-basis-community-openproject_assets:/data -v "$PWD":/backup \
  busybox tar czf /backup/community_openproject_assets.tgz -C /data .
# repeat: paperless media/consume/export, firefly upload
```
*Rollback:* archives on disk; community engine untouched.

## Phase 3 — Freeze community writes
```bash
# on Docker Desktop context
docker compose -p ki-basis-community stop
```
*Rollback:* `docker compose -p ki-basis-community start` brings the old stack back instantly.

## Phase 4 — Restore into the shared cluster (WSL2)
```bash
docker exec -i <shared_pg> psql -U postgres < globals.sql
docker exec -i <shared_pg> pg_restore -U postgres -d openproject --no-owner --role=openproject < community_openproject.dump
# repeat firefly, paperless
```
Extensions (confirmed from the 2026-09-26 backup TOC): **OpenProject's DB uses `btree_gist` and
`pg_trgm`**; the pgvector DB uses `vector`. All ship in `pgvector/pgvector:pg16` (contrib + pgvector),
so the binaries are present — the dumps' `CREATE EXTENSION` runs at restore; if ordering errors appear,
create the DB, run `CREATE EXTENSION ...;` as superuser, then restore. This resolves the prior
[UNVERIFIED] item: OpenProject needs those two extensions but **not** a shared-cluster superuser. Restore non-DB volumes into fresh
named volumes on WSL2 (reverse of the Phase 2 tar). *Rollback:* drop restored DBs and re-restore;
community originals intact.

## Phase 5 — Bring the community stack up on WSL2 against the shared DB
New compose project `-p community`: app services join `shared-db-net` (for DB) **and** a private
`internal` bridge (intra-stack); nginx/valkey stay on `internal` only. Point connection strings at
`postgres:5432` on `shared-db-net`:
- OpenProject `DATABASE_URL=postgres://comm_openproject_app:<pw>@postgres:5432/comm_openproject`
- Firefly `DB_HOST=postgres DB_DATABASE=comm_firefly DB_USERNAME=comm_firefly_app`
- Paperless `PAPERLESS_DBHOST=postgres PAPERLESS_DBNAME=comm_paperless PAPERLESS_DBUSER=comm_paperless_app`
- Passwords from `C:\GitDev\ki-basis-shared\.env` (the `comm_*` DBs/roles already exist from Phase 1).
- **Eliminate the OneDrive bind (D-11):** replace the community Hermes mount
  `…/OneDrive/…/call-agenda-demo → /opt/data/call-agenda` with a **local Docker named volume**
  `community_call_agenda`; seed it from the backup `lika-bot/call-agenda-demo.tgz`; delete the OneDrive
  path from the compose. Verify the agenda skill still reads/writes.
Use distinct host ports (keep community 90xx; watch the 9119/9219 Hermes-dashboard near-collision).
*Rollback:* `docker compose -p community down` on WSL2; Docker Desktop stack still restartable.

## Phase 6 — Verify (soak before destroying anything)
- Each app loads + authenticates; OpenProject/Firefly finish startup migrations; Paperless reindexes;
  Hermes reaches its apps; `pg_stat_activity` stays within per-role `CONNECTION LIMIT`.
- Prove isolation still holds: app role A **cannot** `\c` app B's database (`REVOKE CONNECT`).
- Re-run the private read/write proof against its OpenProject.
- **Also cut the PRIVATE stack onto the shared Postgres** (same restore pattern for its DBs) if D-P1
  is accepted, or leave private on its own postgres if not.
*Rollback:* if anything fails, resume the Docker Desktop community stack (Phase 3 restart).

## Phase 7 — Resolve the Hermes → OpenProject gap (#1)
Private `ki-basis-hermes` still points at the retired v14. Decide (Q6): point it at the 17.8 instance
(put Hermes and the target OpenProject on a shared network + set `OPENPROJECT_API_URL` + a token), or
leave Hermes without OpenProject. Do the equivalent for community Hermes if its OpenProject moved.

## Phase 8 — Stop the old community engine containers
Only after Phase 6 holds for a soak period, stop the Docker Desktop community containers for good.
*Rollback:* still possible — Desktop app + data remain until Phase 9.

## Phase 9 — Retire Docker Desktop (point of no easy return)
1. `wsl -l -v` — confirm the separate `docker-desktop` distro exists distinct from `Ubuntu-*`.
2. Confirm the WSL2 "Apex" engine runs standalone with Docker Desktop stopped (`docker ps`).
3. Uninstall Docker Desktop via Windows **Installed apps** (removes the `docker-desktop` distro; does
   **not** touch the Ubuntu distro / its `/var/lib/docker`). Then clean stale `~/.docker` context in
   Ubuntu (`docker context use default`).
4. `wsl -l -v` — only `Ubuntu-*` should remain.
5. **Remove the empty `ki-basis` duplicate (D-12)** — uninstalling Docker Desktop already removes it
   (it lived in that VM). To remove it independently/earlier (safe — it is stopped/empty):
   `docker compose -p ki-basis down` on the Docker Desktop context (removes the 7 Exited containers +
   the empty `ki-basis-net`). Does **not** touch the WSL2 private stack of the same name.
Do **not** uninstall Docker Desktop until Phases 6–8 are solid and the Phase 2/4 backups are retained.
> Note on D-P3/"stop 172.18": once community is on WSL2 and Docker Desktop is retired, the only
> remaining `172.18.0.0/16` network is the **private** ki-basis stack on WSL2. Stopping *that* means
> stopping the private stack — confirm this is intended (Q2) before running any `stop`.

## Post-migration hardening
- Automate the Phase-2 `pg_dump`/`pg_dumpall` on a schedule (cron in the distro or Windows Task
  Scheduler → `wsl …`); periodically test-restore (row counts + `CREATE EXTENSION` present).
- Keep the logon keepalive + memory cap (D-06); disable WSL idle shutdown for an always-on server
  distro (`instanceIdleTimeout=-1`).

**Key sources (accessed 2026-09-26):** Docker PostgreSQL networking guide; Docker Compose external
networks; PostgreSQL 17 `pg_dump`/`pg_restore` docs; pgvector restore notes; OpenProject external-DB
config; Firefly III Docker; Paperless-ngx configuration; Microsoft WSL advanced-config; "Docker in
WSL2 without Docker Desktop" (Janetakis). Full URLs in the migration-research source.[^migration-research]

[^migration-research]: Web research subagent, 2026-09-26 — official Docker/PostgreSQL/OpenProject/Firefly/Paperless/Microsoft-WSL docs plus named community guides; two items flagged UNVERIFIED there (OpenProject DB privilege/extension needs; some sizing/boot recommendations are reasoned, tune from live metrics).
