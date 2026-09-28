---
type: Handover
title: Continuation handover — WSL2-native stack consolidation
description: Migration is COMPLETE (runbook Phases 0-9 done, ADR-002 written). This handover covers only the remaining non-blocking follow-up items, each with an exact command to run and an exact command to verify it worked.
tags: [handover, docker, wsl2, postgres, migration, consolidation, follow-up]
status: draft
generated: { by: "claude/sonnet-5", at: "2026-09-26" }
stale_after: "2026-10-31"
sources:
  - id: index
    resource: /index.md
    title: Bundle index
  - id: decisions
    resource: /02-decisions-log.md
    title: Decision ledger
  - id: log
    resource: /log.md
    title: Dated change log
---

# Continuation handover — follow-up items only

## Mission (done — this is not a "resume the migration" handover)
The WSL2-native stack consolidation is **complete**. Both stacks (private `ki-basis` + community
`lika-community`) run on the single WSL2-native "Apex" engine against one shared PostgreSQL
(`comm_*`/`priv_*` databases, isolation via `REVOKE CONNECT`, verified live). Docker Desktop is
uninstalled. `ADR-002` is written (`ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` §6, mirrored to its two
duplicate copies). Read [index.md](index.md) once for orientation and [02-decisions-log.md](02-decisions-log.md)
D-01 through D-18 if you need the *why* behind anything below — do not re-run the migration or
re-investigate topology; it's done and verified.

**What this handover is for:** four small, independent, non-blocking follow-up items were left open.
Each one below has an exact command to run and an exact command to verify it worked — so whoever picks
this up (a fresh chat, possibly you) can tell pass/fail without re-deriving anything.

> Private (`ki-basis`) is **live production** with real data (38 real OpenProject work packages).
> Community is also live. Treat both as live systems: reread/verify after any write, same as the
> discipline that ran through the whole migration (see [[verify-before-destructive-infra-actions]] if
> that memory exists in your session — otherwise just: confirm before anything destructive, check
> actual state after every command, don't trust a clean exit code alone).

---

## Item 1 — Raise WSL2 memory ceiling 12 GB → 16 GB (D-10, non-blocking)

**Why:** both stacks + shared Postgres now run on one WSL2 distro instead of being split across two
engines; the original 12 GB ceiling was sized before consolidation. Confirmed current setting:

```powershell
# RUN — check current value (already confirmed 2026-09-26: memory=12GB, swap=4GB)
Get-Content "$env:USERPROFILE\.wslconfig"
```

**Run:**
```powershell
# Edit $env:USERPROFILE\.wslconfig — change `memory=12GB` to `memory=16GB`, keep `swap=4GB` and the
# existing comment. Then restart WSL for it to take effect (THIS STOPS ALL RUNNING CONTAINERS —
# confirm with the operator before running `wsl --shutdown`, it is a real interruption, not read-only):
wsl --shutdown
# wait a few seconds, then anything that touches WSL will auto-start it again, e.g.:
wsl -d Ubuntu -u root -- docker ps
```

**Test — did it work:**
```powershell
wsl -d Ubuntu -u root -- cat /proc/meminfo | Select-String "MemTotal"
# Expect: MemTotal around 16 GB (16777216 kB), not ~12 GB (12582912 kB)
```
```powershell
# All containers should come back up on their own (restart: unless-stopped) — verify nothing's missing:
wsl -d Ubuntu -u root -- docker ps --format "table {{.Names}}\t{{.Status}}"
# Expect: all 13 containers from before (ki-basis-*, community-*, leela-op178-openproject,
# ki-basis-shared-postgres) — same list as log.md's last status check. If any are missing, check
# `restart: unless-stopped` is set in that service's compose file and start it manually.
```

---

## Item 2 — Tune per-role `CONNECTION LIMIT` / `max_connections` / `shared_buffers` from live metrics

**Why:** current values are Phase-1 starting points, never tuned from real usage. Baseline captured
2026-09-26 (right after full migration, light load):

| Role | Active connections | `CONNECTION LIMIT` |
|---|---|---|
| `comm_openproject_app` | 4 | 40 |
| `comm_paperless_app` | 2 | 30 |
| `priv_openproject_app` | 4 | 40 |
| `priv_paperless_app` | 2 | 30 |
| `comm_firefly_app` / `priv_firefly_app` | 0 (Laravel connects on-demand, doesn't hold idle) | 20 each |
| Cluster `max_connections` | — | 200 |
| Cluster `shared_buffers` | — | 1GB |

**Run — recapture the same baseline (compare against the table above, or a more recent capture):**
```bash
wsl -d Ubuntu -u root -- docker exec ki-basis-shared-postgres psql -U postgres -tAc "SELECT usename, count(*) AS active, (SELECT rolconnlimit FROM pg_roles WHERE rolname=usename) AS limit FROM pg_stat_activity WHERE usename IS NOT NULL GROUP BY usename ORDER BY usename;"
```

**Test — is tuning actually needed:** only act if a role is consistently near its `CONNECTION LIMIT`
(e.g. sustained > 80% of limit) or the cluster is near `max_connections=200` in aggregate. If not, this
item can stay open indefinitely — it's monitoring, not a fix waiting to happen. If it IS needed:
```sql
-- example only — adjust the specific role/value that's actually under pressure, don't apply blindly
ALTER ROLE comm_openproject_app CONNECTION LIMIT 60;
```
Then re-run the same capture query above and confirm the new `limit` column reflects the change.

---

## Item 3 — Follow up on the spawned Hermes compose-drift fix (D-16)

**Why:** `ki-basis/compose.yaml`'s checked-in file declares named volumes for the `hermes` service, but
the live container actually runs on bind mounts (`/root/.hermes`, `/root/workspaces`) — a plain
`docker compose up` on that file would silently wipe Hermes's real 4.4G+ of bot state. A follow-up task
was spawned for this (`task_95c691df`, title "Fix ki-basis/compose.yaml hermes volume drift") but its
completion status is **not known from this session** — the spawn_task tool doesn't report back when
picked up.

**Run — check if it's been fixed:**
```bash
wsl -d Ubuntu -u root -- docker inspect ki-basis-hermes --format '{{range .Mounts}}{{.Type}} {{.Source}} -> {{.Destination}}{{"\n"}}{{end}}'
```
```bash
grep -A2 "hermes_data\|hermes_workspaces" "/c/GitDev/apexai-os-meta/ki-basis/compose.yaml" | head -20
```

**Test — did it work:** the live `docker inspect` mounts and the `compose.yaml` declaration should now
**agree** (either both say bind-mount paths, or the file was changed to named volumes AND a deliberate
data migration happened — check for a `tar`/`docker cp` history if so). If they still disagree the way
they did on 2026-09-26 (file says `volume`, live container says `bind`), the task hasn't been picked up
yet — leave it alone, don't fix it inline unless the operator asks; it was deliberately spawned as a
separate task so it gets proper attention, not a rushed inline patch.

---

## Item 4 — Final post-Docker-Desktop-retirement soak check (smoke test, not a to-do — just verify nothing regressed since)

**Why:** Docker Desktop was uninstalled via `winget` after its own engine crashed and wouldn't restart.
Everything was verified clean immediately afterward, but no extended soak period has been observed
since. This is a "run this once to make sure nothing drifted" check, not an action item.

**Run:**
```bash
wsl -d Ubuntu -u root -- docker ps --format "table {{.Names}}\t{{.Status}}"
```

**Test — expected result (13 containers, all healthy or with no healthcheck defined, none restarting):**
```
ki-basis-hermes            Up ... 
ki-basis-nginx             Up ... (healthy)
ki-basis-paperless         Up ... (healthy)
ki-basis-firefly           Up ... (healthy)
ki-basis-valkey            Up ... (healthy)
leela-op178-openproject    Up ...
community-hermes           Up ...
community-nginx            Up ... (healthy)
community-paperless        Up ... (healthy)
community-firefly          Up ... (healthy)
community-openproject      Up ...
community-valkey           Up ... (healthy)
ki-basis-shared-postgres   Up ... (healthy)
```
If any container shows `Restarting` or has an unusually low uptime (much less than the others), check
its logs (`docker logs <name> --tail 50`) before assuming it's fine — that's exactly the pattern that
caught two real incidents during the migration (D-17).

```powershell
# Also confirm Docker Desktop really is gone (should error, not silently succeed):
docker version
# Expect: 'docker' is not recognized (or similar) — if this WORKS, Docker Desktop or its CLI got
# reinstalled somehow; flag to operator, don't investigate further without asking.
```

---

## Safety boundaries (still apply — condensed from the full migration handover)
- Both stacks are live production. Confirm before anything destructive (stop/restart/recreate/uninstall).
- Reread/verify after every write — don't trust a clean exit code alone (see D-17 for why).
- Never start `ki-basis-postgres` or `ki-basis-openproject` (both intentionally stopped, superseded by
  the shared cluster and by `leela-op178-openproject` respectively) without a specific reason and
  operator awareness.
- If you touch `ki-basis-hermes` for any reason before Item 3 above is resolved, re-verify its actual
  live mounts first (`docker inspect --format '{{range .Mounts}}...'`) — do not trust the checked-in
  `compose.yaml`.

## Immediate next action
None of Items 1–4 are blocking or urgent. If the operator hasn't specified which one to pick up, ask —
don't default to Item 1 (WSL restart) without confirming, since it briefly interrupts both live stacks.
