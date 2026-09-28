# Directory Update Log

## 2026-09-26
* **Creation** — bundle initialized (OKF 0.2). Added [index](index.md),
  [01-architecture-and-gaps](01-architecture-and-gaps.md),
  [02-decisions-log](02-decisions-log.md), [03-execution-plan](03-execution-plan.md),
  [04-open-questions](04-open-questions.md).
* **Inputs** — verified current-state topology from three read-only runtime/config investigators
  (2026-09-26); migration best-practice from a web-research subagent (official Docker/PostgreSQL/
  OpenProject/Firefly/Paperless/Microsoft-WSL docs); OKF 0.2 structure from the spec + repo usage.
* **Status** — draft, machine-authored (claude/opus-4.8). Nothing executed yet.
* **Ratified (operator)** — Q1–Q8 answered: **one shared PostgreSQL** for both stacks (D-07);
  **retire Docker Desktop, keep WSL2 native** (D-09); community **data preserved**, **17.8
  authoritative**, **Hermes re-wired**, memory **12→16 GB**, superseding ADR pending (D-10).
  Conflicts C-1/C-2 resolved. Execution authorized to begin at the non-destructive backup (Phase 2/3).
* **Phase 2 (backup) — DONE.** Community fully saved (non-destructive) to
  `C:\GitDev\leela-op178\backups\community-2026-09-26\`: DB dumps (globals + openproject/firefly/
  paperless, TOCs validated, real data), all non-DB volumes (incl. 87 MB hermes-data = Lika bot state),
  and the Lika bot + agenda skill (config, `.env` secrets copied, OneDrive `call-agenda` data) +
  `BACKUP-MANIFEST.md`. Confirmed community OpenProject data lives in the external DB (56 WPs); the
  mounted embedded pgdata volume is empty.
* **Phase 1 (shared Postgres) — DONE.** `ki-basis-shared-postgres` (pgvector pg16) up + healthy on the
  WSL2 "Apex" engine, external `shared-db-net`, internal-only (no host port), tuned
  (max_connections=200 / shared_buffers=1GB). Community roles + DBs created with a `comm_` prefix
  (`comm_openproject`/`comm_firefly`/`comm_paperless`), each owned by its own least-priv role, cross-DB
  `CONNECT` revoked — isolation verified. Infra + creds at `C:\GitDev\ki-basis-shared\` (`.env` local,
  uncommitted). Running community stack untouched.
* **Surgical additions (2026-09-26).** Recorded **D-11** (eliminate the unintended OneDrive bind on
  community Hermes → local named volume; gap #7) and **D-12** (explicitly remove the empty Docker
  Desktop `ki-basis` duplicate). Runbook Phase 5 updated (correct `comm_*` connection strings +
  OneDrive-elimination step) and Phase 9 (explicit duplicate removal). Added
  [05-handover](05-handover.md) for another chat to continue.
* **Next = first DESTRUCTIVE gate** (Phase 3+): freeze community → restore into `comm_*` DBs + volumes
  on WSL2 → bring community up against shared Postgres → eliminate OneDrive bind → verify → private stack
  (17.8 authoritative) → re-wire private Hermes → remove empty duplicate → retire Docker Desktop.
  Awaiting operator go-ahead.

## 2026-09-26 (continuation session)
* **Phase 3 (freeze community) — DONE.** Operator confirmed; ran `docker compose -p ki-basis-community
  stop` from `C:\GitDev\lika-community`. All 7 containers Exited (not removed) — rollback via `start`
  intact. Reread confirmed: private stack + shared Postgres untouched, still healthy.
* **D-13 recorded** — Phase 4 restore deliberately skips `globals.sql` (unprefixed roles from the old
  standalone community Postgres); restores per-DB dumps directly into the already-created `comm_*_app`
  owners instead. See [02-decisions-log](02-decisions-log.md#ratified-by-operator--2026-09-26). Operator
  verified before execution.
* **Phase 4 DB restore — DONE (data only; non-DB volumes still pending).** Script at
  `C:\GitDev\leela-op178\restore-community-dbs.sh` restored `community_{openproject,firefly,paperless}.dump`
  into `comm_openproject`/`comm_firefly`/`comm_paperless` via `pg_restore --no-owner --role=comm_*_app`.
  Reread/verified: `comm_openproject.work_packages` = 56 rows (matches manifest exactly).
  `comm_paperless.documents_document` = 2 rows. `comm_firefly` restored only lookup/config tables
  (migrations/configuration/currencies/roles) — **`users`/`accounts`/`transactions`/`transaction_journals`
  = 0 rows, verified this is the pre-existing source-dump state (checked `community_firefly.dump`'s
  own COPY blocks directly, no live DB touched), not a restore defect.** The community Firefly instance
  had no real financial data at backup time despite the manifest's "real financial tables" wording (that
  referred to schema/ownership, not populated rows) — **operator should know Firefly data did not
  regress, there simply wasn't any.**
* **D-14 recorded** — new WSL2 "community" compose project design (compose.wsl.yaml + .env.wsl as
  siblings of the original, dropped local postgres + unused openproject_pgdata, split
  internal/shared-db-net networking). Caught in passing: `call-agenda-demo.tgz` needed
  `--strip-components=1` (wraps content in a `call-agenda-demo/` dir, unlike the `./`-rooted volume
  tarballs) — fixed before restoring, verified post-restore the volume root has the files directly.
* **Phase 4 volume restore + Phase 5 bring-up — DONE.** All 10 volumes
  (`community_{valkey_data,firefly_upload,paperless_{data,media,export,consume},openproject_assets,
  hermes_{data,workspaces},call_agenda}`) created + populated from the Phase 2 backup. Stack brought up
  via `docker compose -f compose.wsl.yaml --env-file .env.wsl -p community up -d` on WSL2 Apex.
  Verified: all 6 containers running, `valkey`/`firefly`/`nginx` report healthy, `paperless` mid
  start_period (logs clean — migrations applied, Redis+Postgres connected, existing admin user found =
  restored data present, not fresh), `openproject` logs confirm "using an external database. Not
  initializing a local database cluster." `nginx /healthz` returns 200 from the Windows host (port
  forwarding confirmed). Hermes started, connecting to Telegram; one WARNING in its logs about a prior
  unclean shutdown is a pre-existing note baked into the restored `hermes_data` volume (from 2026-09-22,
  before this session), not caused by this migration.
* **Phase 6 verify (community side, non-destructive) — DONE.** All 6 containers healthy after soak
  (`paperless` cleared `health: starting` → healthy). `pg_stat_activity` per role well within
  `CONNECTION LIMIT` (openproject 4/40, paperless 2/30). **Isolation proven**: `comm_firefly_app`
  correctly gets `permission denied for database "comm_openproject" / User does not have CONNECT
  privilege` when attempting `\c comm_openproject` — `REVOKE CONNECT` holds under the real shared
  cluster, not just in the setup script. Hermes reaches all three apps over the `internal` network
  (firefly/paperless → 302 as expected; openproject → 400 with curl's default Host header, confirmed
  benign — OpenProject's `OPENPROJECT_HOST__NAME` host-check, unchanged from the pre-migration config;
  with the expected `Host:` header it also returns 302). Private stack re-checked: `leela-op178-openproject`
  (17.8) still responds 200 on `:8083`, untouched throughout.
* **Private-stack DB migration prep — DONE (non-destructive; live containers not yet touched).**
  Operator confirmed cutting the private stack onto the shared Postgres is the correct next runbook
  step (Phase 6 fork point, D-07 already accepted it in principle).
  - Created `priv_{firefly,paperless,openproject}` roles/DBs on the shared cluster (isolation proven,
    same as `comm_*`).
  - Backed up private DBs live (`C:\GitDev\leela-op178\backups\private-2026-09-26\`): globals +
    firefly/paperless from `ki-basis-postgres`, and openproject from **leela-op178-openproject's
    embedded PostgreSQL 17** (it's a fully self-contained instance, not part of ki-basis-postgres).
  - Restored all three into `priv_*` — see **D-15** for the restore-mechanics gotchas hit along the way
    (pgvector's non-trusted extension needing superuser pre-staging; needing a throwaway `postgres:17`
    client container to read the PG17-format openproject dump against the pg16 shared server). Row
    counts: firefly 0 accounts (same as community — genuinely unused), paperless 1 document,
    **openproject 38 real work packages**. Ownership verified correct (`priv_*_app`, not `postgres`).
  - **Found in passing (D-16):** `ki-basis/compose.yaml` has drifted from the live `ki-basis-hermes`
    container — file says named volumes, container actually runs on bind mounts
    (`/root/.hermes`, `/root/workspaces`) since 2026-09-01. A plain `docker compose up` on the current
    file would silently recreate hermes onto empty volumes and wipe its real state. Worked around (new
    compose variant matches the live bind mounts, not the drifted file); root cause **not fixed** —
    flagged as a separate follow-up task, out of scope here.
  - Drafted `compose.shared-db.yaml` for both `ki-basis` (drops local `postgres` service, firefly/
    paperless/openproject join `shared-db-net`, nginx/valkey/hermes stay `ki-basis-net`-only) and
    `leela-op178` (adds `DATABASE_URL` → `priv_openproject`, keeps its embedded `pgdata` volume mounted
    but unused for instant rollback). Both validate (`docker compose config --quiet`).
* **`ki-basis` cutover — done, after fixing two real incidents (see D-17).** Operator confirmed go;
  first `up` recreated all 6 containers (switching compose files changes Compose's tracked config-hash
  for every service, not just changed ones). **Incident 1:** the orphaned `ki-basis-postgres` was still
  aliased `postgres` on `ki-basis-net`, colliding with the shared cluster's same alias on `shared-db-net`
  — firefly/openproject crash-looped on auth failure (wrong target), paperless's apparent success was
  luck (DNS resolution was confirmed non-deterministic per-query). Fixed: stopped `ki-basis-postgres`
  (data untouched), recreated firefly/paperless/openproject. **Incident 2:** the `openproject` service
  in `compose.shared-db.yaml` was copied verbatim from the original file without checking identity —
  it's the retired v14 duplicate (D-05, meant to stay stopped), not the real private OpenProject. Its
  DATABASE_URL pointed at `priv_openproject`'s restored 17.8-schema data; the old binary crash-looped
  trying to recreate existing tables. Fixed: stopped `ki-basis-openproject` again, **removed the
  `openproject` service from the compose file entirely** (with a warning comment against re-adding it).
  Verified after both fixes: `priv_openproject` data unchanged (38 work_packages, 241 schema_migrations
  — transactional rollback confirmed, not corrupted); firefly/paperless now resolve `postgres`
  unambiguously to the shared cluster and show clean logs. `ki-basis-nginx`/`ki-basis-hermes`/
  `ki-basis-valkey` were recreated too (file-switch side effect) but unaffected — Hermes's real
  bind-mount data (4.4G) confirmed intact post-recreate (this is exactly what D-16's workaround was
  for). **`ki-basis-postgres` and `ki-basis-openproject` are now both stopped** (data/volumes intact,
  instant rollback via `docker start` + reverting to `compose.yaml`).
* **leela-op178 cutover — NOT yet run.** Given two incidents just happened on the same-engine private
  stack, pausing before touching the actual authoritative private OpenProject rather than continuing
  straight through. Awaiting operator input.
* Phases 7 (Hermes↔OpenProject re-wire — note gap #1 is unchanged: private Hermes still points at the
  dead `ki-basis-openproject` v14, same as before this session), 8 (stop old Docker Desktop community
  containers for good), 9 (retire Docker Desktop) all still pending.
* **[05-handover](05-handover.md) rewritten** to reflect all of the above for a fresh chat/agent to
  resume from — supersedes the earlier-session handover. Leads with D-15/D-16/D-17 as required reading
  before touching the private stack again, and states plainly that the `leela-op178` cutover command is
  drafted + validated but not yet run.
* **`leela-op178` cutover — DONE, clean this time.** Applied the D-17 lesson before running: checked
  `shared-db-net` and `leela-op178_default` for alias collisions first (none — `leela-op178_default`
  only had `leela-op178-openproject` itself; `shared-db-net` had exactly one `postgres`-aliased
  container). Ran `docker compose -f compose.shared-db.yaml --env-file .env.shared-db -p leela-op178
  up -d`. Verified: `getent hosts postgres` from inside the container → `172.20.0.2` (correct, shared
  cluster) on the first try. Logs clean (apache2/web/worker/hocuspocus/memcached all RUNNING, GoodJob
  scheduler started, Puma workers booted, zero errors — unlike the `ki-basis-openproject` incident,
  this is genuinely the same 17.8 instance the dump came from, so no schema mismatch was possible).
  `priv_openproject_app` shows 2 active connections; `work_packages` still 38 rows. `http://127.0.0.1:8083`
  returned a transient 503 for a few seconds (Apache gating until Puma's workers finished booting, not
  an error) then 200. **The private stack's full database migration onto the shared cluster is now
  complete** (firefly, paperless, openproject all on `priv_*`). Old `leela-op178`'s embedded pgdata
  volume stays mounted-but-unused for instant rollback.
* **Phase 7 (re-wire private Hermes → 17.8 OpenProject) — DONE.** Applied the D-17 lesson: targets
  `leela-op178-openproject` by **container name** (globally unique, collision-proof) rather than the
  generic `openproject` alias that caused the earlier incident — even if the retired v14 duplicate is
  ever mistakenly started again, Hermes can't be confused by it. Steps: live `docker network connect
  ki-basis-net leela-op178-openproject` (additive, no restart, verified with `getent hosts` +
  authenticated API call before touching Hermes); reused the existing valid `OPENPROJECT_TOKEN` from
  `leela-op178/op.env` (no new token minted) as `OPENPROJECT_API_KEY` in `ki-basis/.env.shared-db`;
  updated `OPENPROJECT_API_URL` + added `OPENPROJECT_KEY` to Hermes's env in `compose.shared-db.yaml`
  (the original `ki-basis/compose.yaml` never had `OPENPROJECT_KEY` at all — this is a genuinely new
  capability, not a fix to something previously working); recreated only `ki-basis-hermes` (verified
  its 4.4G real bind-mount data intact post-recreate, per D-16). Also added `ki-basis-net` to
  `leela-op178/compose.shared-db.yaml` so the network attachment survives a future recreate, not just
  the live `docker network connect`. **Verified working end-to-end:** authenticated
  `GET /api/v3` from inside `ki-basis-hermes` → `200`, `coreVersion: 17.8.0`, `user: OpenProject Admin`.
  Gap #1 (private Hermes → dead OpenProject) is now genuinely closed, not just documented as known.
* **Phases 8 + 9 (retire Docker Desktop) — DONE, via an unplanned path.** Docker Desktop's engine
  crashed mid-session (`DockerDesktopVM` — turns out it's **Hyper-V-backed, not WSL2-backed**;
  `wsl -l -v` never showed a `docker-desktop` distro — unable to allocate 8 GB RAM alongside the now
  fully-loaded WSL2 Apex engine) and would not restart. Since its engine couldn't be reached at all,
  Phase 8's planned `docker compose stop`/`down` on the frozen originals was impossible — operator
  decided (given the Phase 2 backup was re-verified intact: TOC counts unchanged, 1395/717/758 entries)
  to skip straight to uninstalling Docker Desktop entirely (`winget uninstall --id
  Docker.DockerDesktop`), which removes its VM and everything in it — the frozen community originals and
  the empty `ki-basis` duplicate (D-12) — in one action. **Verified clean:** Windows `docker.exe` no
  longer exists at all (full removal); `wsl -l -v` still shows only `Ubuntu` (confirms Docker Desktop
  was never a WSL distro here, so removing it could not touch Ubuntu/Apex by construction); all 13
  containers across both stacks on the WSL2 Apex engine (`ki-basis-*`, `community-*`,
  `leela-op178-openproject`, `ki-basis-shared-postgres`) still running, completely unaffected.
* **Runbook Phases 0–9 are now all complete.** Remaining items are the non-blocking tuning/documentation
  ones already tracked under "Still open" in [05-handover](05-handover.md) (superseding ADR write-up,
  connection-limit tuning from live metrics, WSL memory cap 12→16 GB) plus the separately-spawned
  Hermes-volume-drift follow-up task (D-16) — none of these block calling the migration itself done.
* **Retired v14 `ki-basis-openproject` fully deleted (D-18)**, per operator request, going beyond D-17's
  "stopped" state: container + its `ki-basis-openproject-assets` volume removed; its `openproject`
  database + `openproject_app` role dropped from the (still otherwise-stopped) old `ki-basis-postgres`
  (briefly started for this, then stopped again — confirmed stopped afterward); `openproject`
  service/volume/env-vars/depends_on stripped from the historical `ki-basis/compose.yaml`, including
  fixing `docker/postgres/init/01-init-databases.sh`'s fail-closed `OPENPROJECT_DB_*` requirement so a
  future fresh-volume bootstrap doesn't break firefly/paperless too. `firefly`/`paperless` DBs inside
  `ki-basis-postgres` and all backup files were deliberately left untouched. Noted in passing: the whole
  Docker engine restarted on its own mid-session (likely WSL2 idle-shutdown) — `ki-basis-postgres`
  correctly stayed stopped through it (confirms `restart: unless-stopped` honors manual stops across a
  daemon restart), and live data was spot-checked unaffected (`priv_openproject` 38 rows, `comm_openproject`
  56 rows, unchanged).
* **ADR-002 written** (D-10 closed) — see the previous log entries above for detail; mirrored to both
  duplicate copies of the file on operator request, verified byte-identical.
* **[05-handover](05-handover.md) rewritten again** — migration is done, so this version drops the
  "resume the migration" framing entirely and instead gives each of the four remaining non-blocking
  follow-up items an exact run-command + exact verify-command pair (WSL memory ceiling raise,
  connection-limit tuning with a captured baseline, checking whether the spawned Hermes-drift task
  landed, and a post-Docker-Desktop-retirement smoke test). Captured a fresh connection/config baseline
  for Item 2 while writing it: `max_connections=200`, `shared_buffers=1GB`, all roles well under their
  `CONNECTION LIMIT` (4/40, 2/30 for openproject/paperless on both tenants; firefly roles show 0 active
  — consistent with the already-documented "genuinely unused" finding, not a new concern).
