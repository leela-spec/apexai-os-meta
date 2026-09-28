---
type: Findings
title: T10 — Hermes compose-drift — findings, research, and operator-gated recommendation
description: >
  Research-and-recommend deliverable for the T10 handover. Confirms the verified ground truth for BOTH
  Hermes instances live (2026-09-28), answers the §5 research assignment with cited sources, and delivers
  a least-change, data-safe, operator-gated recommendation with a tested backup/restore, verification,
  rollback, a required blind-spot analysis, and an explicit "community is unaffected" proof.
created: 2026-09-28
status: EXECUTED — Option A applied 2026-09-28 after operator go (backup verified, live unchanged). G2 lifecycle-script remediation still OPEN. See §9.
parent_handover: apex-meta/orchestration/architecture-improvements/05-program-closeout/HANDOVER-t10-hermes-compose-drift.md
authority_order: "LIVE runtime + code > accepted decisions/ADRs > handover/this doc. Conflicts are surfaced, not resolved unilaterally (see §2.0)."
implementation_authority: research-and-recommend ONLY. No compose up / recreate / volume change without an explicit, per-action operator OK.
---

# T10 — Hermes compose-drift: findings + recommendation (data-loss-critical)

## 1. TL;DR (read this, then §2.0)

- **The drift is real and confirmed live**: `ki-basis-hermes` runs on **bind mounts** (`/root/.hermes → /opt/data` 4.4 GB, `/root/workspaces → /root/workspaces` 3.5 GB ≈ **7.9 GB**), while the checked-in `ki-basis/compose.yaml` declares **named volumes** for Hermes. The live stack is created from `compose.shared-db.yaml` (which correctly declares the bind mounts). ✅ / ⚠️
- **🔴 NEW — the handover's key safety premise is FALSIFIED.** The handover §3 states *"It only triggers if someone brings up the wrong file … Today nothing does."* **That is not true.** The checked-in lifecycle scripts `scripts/start-ki-basis.{sh,ps1}` run `docker compose -f compose.yaml --env-file .env(.private) up -d`, and those env files force `COMPOSE_PROJECT_NAME=ki-basis`, which resolves `compose.yaml`'s `container_name` to the **live `ki-basis-hermes`**. Running the documented "start my stack" script is a wired path straight to the wipe. This is exactly the blind-spot the handover warned about — surfaced, per `authority_order`, not silently fixed.
- **The risk is fully armed, not dormant.** Live Docker Compose is **v2.40.3** (≥ v2.32.0), which actively detects a live-mount-vs-declared-volume mismatch and recreates the container (auto-proceeds under `--yes`/non-interactive). The drift's target named volumes (`ki-basis-hermes-data/-workspaces`) **do not exist**, so a recreate would create them empty and mount them — orphaning the 7.9 GB.
- **Community is provably unaffected** (separate project `community`, separate repo `lika-community`, separate file, networks, ports, and `community_*` named volumes). See §6.
- **Recommendation (least-change, data-safe):** back up first (tested), then apply **Option A** — edit *only* `compose.yaml`'s Hermes `volumes:` to the live bind mounts (+ warning comment). This removes the **irreversible** data-loss even if the stale script runs, and stays within "the private Hermes service definition" (handover §0 scope). **Separately surface** the stale-lifecycle-script problem for an explicit operator scope decision — do **not** fold it into the T10 edit. Full detail: §5.
- **"Leave parked + guard" is also acceptable and safe** (handover §7). If you prefer zero content change to the file, a fail-closed guard on the scripts is a legitimate alternative — §5, Option C.

## 2. Verified ground truth — BOTH Hermes (captured read-only 2026-09-28)

### 2.0 Conflict surfaced (per `authority_order`, not resolved unilaterally)
The **live runtime + code** (start scripts wired to `compose.yaml`) **contradicts the handover's** written premise
that "today nothing brings up the wrong file." Per the handover's own authority order (LIVE > ADR > handover)
and §0 ("if your plan touches more than the private Hermes service definition … stop and reconsider"), this
finding is **surfaced for an operator decision** rather than absorbed into a wider unilateral fix. The minimal
data-safe action (§5 Option A) stays in scope; the script remediation is a **separate, operator-gated** item.

### 2.1 One engine
WSL2-native "Apex" engine (`Ubuntu` distro `dockerd`); Docker Desktop retired (ADR-002, `DUAL_INSTANCE_ARCHITECTURE.md` §6).
Run docker as `wsl -d Ubuntu -u root -- docker …`. Live `docker compose version` = **2.40.3**.

### 2.2 Private Hermes — `ki-basis-hermes`
| Attribute | Live value (2026-09-28 `docker inspect`) | Source-of-record file |
|---|---|---|
| Created | `2026-09-26T12:24:53Z`, `State=running`, `restart=unless-stopped` | — |
| Config file label | `…/ki-basis/compose.shared-db.yaml`, project `ki-basis` | `compose.shared-db.yaml` ✅ |
| Mount 1 | **bind** `/root/.hermes → /opt/data` (4.4 GB) | shared-db L173 ✅ / `compose.yaml` L184 declares **named** `hermes_data` ⚠️ |
| Mount 2 | **bind** `/root/workspaces → /root/workspaces` (3.5 GB) | shared-db L174 ✅ / `compose.yaml` L185 declares **named** `hermes_workspaces` ⚠️ |
| Config binds | none (persona/config live *inside* `/root/.hermes`) | — |
| `HERMES_HOME` | `/opt/data`; `HERMES_DISABLE_LAZY_INSTALLS=1` | shared-db L152–155 |

- The **creation-date discrepancy** the handover flagged (D-16 says 2026-09-01; inspect says 2026-09-26) is
  **resolved**: the container was **recreated during the 2026-09-26 consolidation cutover** from
  `compose.shared-db.yaml` (confirmed by the `config_files` label). D-16's "2026-09-01" is the *original*
  pre-consolidation container; the current one is the re-created successor on the same bind paths. No data moved.
- **Only Hermes drifted.** D-16 records that all other private services (nginx/firefly/paperless/valkey) were
  checked and match their declarations; re-confirmed consistent with today's soak.

### 2.3 Community Hermes — `community-hermes` — different by design, no drift
| Attribute | Live value (2026-09-28) | Source-of-record |
|---|---|---|
| Project / repo | `-p community` / `C:\GitDev\lika-community` | `compose.wsl.yaml` |
| Data mounts | **named volumes** `community_hermes_data → /opt/data`, `community_hermes_workspaces → /root/workspaces`, `community_call_agenda → /opt/data/call-agenda` | compose.wsl L189–190, L196 ✅ |
| Config mounts | **read-only binds** from `/mnt/c/GitDev/lika-community`: `SOUL.md`, `scripts/`, `skills/equinox-intake`, `skills/call-agenda`, `docker/hermes/run.py` | compose.wsl L191–195 ✅ |
| Ports | `9642` gateway / `9219` dashboard | compose.wsl L155–156 |

Live inspect matches the file exactly → **community has NO drift** (expected per handover; verified, not assumed).

### 2.4 Why the two differ (history, not an ideal to normalize)
Private Hermes predates the migration and carried live state; during consolidation it was **recreated preserving
its existing bind mounts** to avoid data loss (D-16). Community was migrated **fresh onto WSL named volumes**
(D-14). The asymmetry is a consequence of safely migrating a live, stateful container — **do not "harmonize."**
Note also: community keeps its persona/skills as **read-only repo binds** (git-tracked), while private keeps them
**inside `/opt/data`** — a second real asymmetry, same reasoning.

## 3. The risk, named precisely (revised with the wired-script finding)

This is a **data-LOSS** risk (orphaning ~7.9 GB of live state), not a data-leak. It triggers whenever the
`ki-basis-hermes` container is **recreated against a definition that declares the (empty, non-existent) named
volumes** instead of the live bind paths. Concrete trigger paths, in order of likelihood:

1. **🔴 Wired script (new):** `scripts/start-ki-basis.sh` (inside WSL, where `docker` is on PATH) →
   `docker compose -p ki-basis-private -f compose.yaml --env-file .env.private up -d`. `.env.private` sets
   `COMPOSE_PROJECT_NAME=ki-basis`, so `compose.yaml`'s `container_name: ${COMPOSE_PROJECT_NAME:-ki-basis}-hermes`
   = **`ki-basis-hermes`** (the live container) and its volume `name:` = `ki-basis-hermes-data` (empty). Compose
   ≥ 2.32 recreates on the mount mismatch → **wipe**.
2. **Manual `docker compose -f compose.yaml -p ki-basis up`** with `.env`/`.env.private` (both set the same
   project name) — same outcome.
3. Any future automation copying the `compose.yaml` hermes block.

**Fragile accidental safety-nets (do NOT rely on):** `start-ki-basis.ps1` (Windows) tries to launch
`Docker Desktop.exe` when `docker` is unresponsive; Docker Desktop is uninstalled and `docker.exe` is off PATH
(soak 2026-09-28), so the **PowerShell** path likely throws before `up`. The **bash** path in WSL has no such
guard. `.env.community` is absent, so `-Instance community/all` throws — but `-Instance private` (the dangerous
one) proceeds.

## 4. Research assignment (§5 of the handover) — answered with sources

### 4.1 How Hermes persists state — what lives in `/opt/data` and `/root/workspaces`
Per Nous Research's official Hermes docs, `HERMES_HOME` (`/opt/data`) is the single directory holding **all**
user/agent state:

| Path under `/opt/data` | Contents |
|---|---|
| `state.db` | **SQLite** session/agent DB, **WAL mode** by default |
| `sessions/` | conversation history |
| `memories/` | persistent memory store |
| `skills/` | installed skills |
| `cron/` | scheduled job definitions |
| `hooks/` | event hooks |
| `profiles/` | per-profile dirs (multi-agent: `default`, `investment`, `research-strategist`, …) |
| `home/` | per-profile HOME for tool subprocesses |
| `logs/`, `skins/`, `installs/` | runtime logs, CLI skins, opt-in backend SDK installs |
| `config.yaml`, `.env`, `SOUL.md` | configuration, secrets, agent identity |

`/root/workspaces` = the **live repos Hermes operates on** (per ADR Diagram A: `apexai-os-meta`, `Investment`
+ Karakeep custody, `MasterOfArts`, `acim-secular`) — 3.5 GB of working files with direct ext4 access.
**What breaks if lost/reset:** all conversation history, persistent memory, installed skills, scheduled cron
jobs, event hooks, agent identity/persona, and stored credentials are gone; workspace working-copies are gone.
This is unrecoverable except from backup. (Sources: Hermes Docker docs; Hermes configuration docs.)

### 4.2 Bind mounts vs named volumes — for THIS case, precisely
- **Recreate behavior:** `docker compose up` recreates a container when its resolved config differs from the
  running container. Historically a *volume-only* change did **not** force recreation (docker/compose #10060);
  **v2.32.0** (Dec 2024, PR #12363) added active **mismatch detection**: Compose notices "the mounted volume is
  not the expected one," prompts, and with `--yes`/non-interactive **drops and recreates** onto the declared
  volume. Live engine is **2.40.3** → this behavior is active. Independently, `compose.yaml` differs from the
  live container in *many* fields (local `postgres`, no `shared-db-net`, no OpenProject rewire), so a recreate
  would happen regardless of the volume-diff feature.
- **On recreate:** a **bind mount** re-attaches the same host path → **state survives**. A **named volume** that
  doesn't exist is **created empty** → prior state is **orphaned** (still on disk at the old bind path, but the
  new container can't see it). Anonymous/named volumes from a prior container **cannot be auto-re-attached**
  (no VolumeRename API — PR #12363).
- **Performance on WSL2 ext4:** identical. Both `/root/.hermes` (bind) and `/var/lib/docker/volumes/*` (named)
  live on the **native ext4** VHDX — the ADR's ~80–300× 9P penalty applies only to `/mnt/c` binds, which these
  are **not**. (Community's *config* binds are on `/mnt/c` but are tiny read-only files, so the penalty is
  irrelevant there too.) → **Performance is not a deciding factor.**
- **Backup ergonomics:** bind mounts are *easier* here — plain `tar` of a known host path, no helper container
  needed. Named volumes need a `--volumes-from` helper container to reach `/var/lib/docker/volumes`.
- **Failure modes:** the dominant one is exactly this drift — a declaration that doesn't match the live mount,
  silently wiping on recreate. SQLite WAL adds a second: a **hot** copy of `state.db` can capture an
  inconsistent WAL state (see §5 backup). (Sources: docker/compose #10060, PR #12223, PR #12363; Docker Compose
  volumes reference; Docker storage docs.)

### 4.3 Options to remove the drift — least-change first → see §5 (recommendation)

### 4.4 Backup/restore that is actually tested → see §5.3

### 4.5 Community spillover → see §6

### 4.6 Blind-spot pass → see §7

## 5. Recommendation (least-change, data-safe) — operator-gated, NOT executed

### 5.0 Standing safety net — BACKUP FIRST (applies to every option, do before any mutation)
Even the recommended text edit is a mutation; and the wired-script risk means a verified backup must exist
regardless. **A backup you have not restored is not a backup.** See §5.3 for the exact, tested procedure.

### 5.1 Options compared
| | Change | Removes 7.9 GB data-loss? | Scope vs handover §0 | Residual risk | Effort/risk |
|---|---|---|---|---|---|
| **A — file matches reality** (edit `compose.yaml` Hermes `volumes:` → the two live bind mounts, + comment) | text edit, Hermes stanza only | **Yes** — recreate re-attaches real bind paths | ✅ within "the private Hermes service definition" | Stale script would still recreate *other* private services onto retired local-postgres topology (an **outage, recoverable**, not 7.9 GB loss) | Lowest that satisfies the PLAN acceptance criterion (`compose config` hermes mounts == live) |
| **B — migrate bind → named volumes** | back up, `tar` 7.9 GB into new named volumes, verify, switch file + recreate | Yes, if done perfectly | ⚠️ requires a real recreate of the live bot | High: any slip wipes/orphans state; needs downtime | Highest — **not recommended**; no benefit here (perf identical, backup easier on binds) |
| **C — leave file, neutralize the path** | fail-closed guard in `start-/stop-ki-basis.*` (and/or rename `compose.yaml` + update its 5 script/back-up refs) | Yes (blocks the trigger) | ⚠️ touches scripts (wider than Hermes stanza) → operator scope call | Doesn't correct the file's content; rename breaks refs unless all updated | Low behavioral change; **legitimate "keep parked" outcome** |

### 5.2 Recommended: **Option A now (minimal, in-scope) + surface Option C as a separate operator decision**
- **Why A:** it removes the only **irreversible** risk (the 7.9 GB) with the smallest possible change, keeps the
  edit inside "the private Hermes service definition" (honoring §0's anti-overcorrection scope), and satisfies
  the parent-plan acceptance criterion (`docker compose config` shows Hermes mounts == live; a dry run changes
  no volume). After A, even the wired script cannot wipe Hermes.
- **Why not silently also fix the scripts:** doing so goes **wider than the Hermes service definition**, which
  §0 explicitly says means "stop and reconsider." The stale-script problem (recreating firefly/paperless/
  openproject onto the retired local-postgres topology) is a **real but recoverable outage**, separate from
  T10's data-loss mandate. It deserves its own operator-scoped ticket (recommend: repoint the lifecycle scripts
  to `compose.shared-db.yaml` + `.env.shared-db` + `-p ki-basis`, or add a fail-closed guard). **Surfaced, not
  executed.**

#### Exact operator-gated steps for Option A (after backup §5.3 is verified)
1. Edit `ki-basis/compose.yaml`, `hermes.volumes:` only — replace
   ```yaml
       volumes:
         - hermes_data:/opt/data
         - hermes_workspaces:/root/workspaces
   ```
   with the **live bind mounts** (mirroring `compose.shared-db.yaml` L173–174), plus a comment explaining why:
   ```yaml
       volumes:
         # Live ki-basis-hermes runs on BIND mounts (see D-16 / FINDINGS-t10). Named volumes here
         # would make `compose up` recreate hermes onto EMPTY volumes and orphan ~7.9 GB of state.
         - /root/.hermes:/opt/data
         - /root/workspaces:/root/workspaces
   ```
   (Optionally also delete the now-unused top-level `hermes_data:` / `hermes_workspaces:` volume declarations
   L23–26 — still within the Hermes definition; confirm nothing else references them first.)
2. **No `docker compose up`.** Validate statically only: `docker compose -f compose.yaml config --quiet` (parse
   check; makes no runtime change).
3. Verify acceptance: `docker compose -f compose.yaml --env-file .env.private -p ki-basis config` now shows
   Hermes `volumes` as the two bind paths == live inspect. Confirm `docker inspect ki-basis-hermes` is unchanged
   (still running, same mounts) — the edit touched a file, not the container.

#### Verification (Option A)
- `git diff` shows only the Hermes `volumes:` block (and optionally the two orphaned volume decls) changed.
- `docker compose -f compose.yaml config` Hermes mounts == `docker inspect ki-basis-hermes` mounts.
- Live container untouched: same `Created`, `State=running`, same 7.9 GB.

#### Rollback (Option A)
- It's a single-file text edit under git: `git checkout -- ki-basis/compose.yaml` restores the prior file. No
  runtime state is involved, so rollback carries **zero data risk**.

### 5.3 Tested backup + restore (do FIRST; required regardless of option)
Because `/opt/data` holds a **WAL-mode SQLite** (`state.db`), a naive hot `tar` can capture an inconsistent DB.
Two acceptable procedures — pick per tolerance for a brief bot pause:

**Procedure 1 — consistent (brief stop, recommended for the DB):** all inside `wsl -d Ubuntu -u root`:
1. `docker stop ki-basis-hermes` (a manual stop survives daemon restarts under `unless-stopped` — verified D-18).
2. `tar -C /root -czf /root/backups/hermes-data-2026-09-28.tgz .hermes` and
   `tar -C /root -czf /root/backups/hermes-workspaces-2026-09-28.tgz workspaces`
   (write archives to **ext4** `/root/backups`, never `/mnt/c`, to avoid 9P corruption while writing).
3. `docker start ki-basis-hermes`; confirm `:8642/health` → 200.

**Procedure 2 — hot (no downtime):** keep the container running; back up the DB with a live-safe snapshot:
`docker exec ki-basis-hermes sqlite3 /opt/data/state.db ".backup '/opt/data/state.backup.db'"`, then `tar` the
trees as above (the consistent `state.backup.db` is inside the archive; ignore the live `state.db`/`-wal` on
restore).

**Prove the restore (mandatory — this is what makes it a backup):**
1. Extract into a throwaway dir: `mkdir -p /root/restore-test && tar -C /root/restore-test -xzf /root/backups/hermes-data-2026-09-28.tgz`.
2. `sqlite3 /root/restore-test/.hermes/state.db 'PRAGMA integrity_check;'` → expect **`ok`**
   (or run it on `state.backup.db` if Procedure 2).
3. Spot-check counts vs live: `ls /root/restore-test/.hermes/{sessions,memories,skills,cron} | wc -l` compared to
   the live container's same dirs.
4. (Optional strongest proof) boot a **throwaway** hermes container on an **isolated** project/network/port,
   read-only-ish, pointed at the restored copy, and hit its `/health` — then remove it. Never point it at the
   live bind paths or reuse project `ki-basis`.
5. Record sizes/hashes + the `integrity_check=ok` result as evidence before any file edit.

## 6. Community is unaffected — explicit proof
The recommended change edits **only** `C:\GitDev\apexai-os-meta\ki-basis\compose.yaml` (and, if the operator
later scopes it, `ki-basis/scripts/*`). None of that is referenced by the community stack:
- **Separate compose project** `community` (live label confirmed) vs `ki-basis`.
- **Separate repo/file** `C:\GitDev\lika-community\compose.wsl.yaml` + `.env.wsl` — not touched.
- **Separate networks** (`internal` + `shared-db-net`) and **ports** (`9642`/`9219`) — no overlap with private.
- **Separate named volumes** `community_hermes_data` / `community_hermes_workspaces` / `community_call_agenda`
  (live `docker volume ls` confirmed) — the private edit references neither; the drift's target
  `ki-basis-hermes-data` is a *different* name and doesn't even exist.
- `start-ki-basis.ps1 -Instance community` cannot run (no `.env.community`); community is started by its own
  repo's flow.
- The only shared object is the Postgres cluster + `shared-db-net`, and **private Hermes is not on
  `shared-db-net`** at all — so nothing about the Hermes fix can cross tenants.

**Conclusion:** the chosen option changes **no** community behavior, container, volume, network, or file.

## 7. Blind-spot analysis (required) — assumptions and what breaks if each is wrong
| # | Assumption behind the recommendation | If wrong → what breaks | How to detect / guard |
|---|---|---|---|
| 1 | Live `ki-basis-hermes` was created from `compose.shared-db.yaml` | a different file/topology may be authoritative | Confirmed via `config_files` label 2026-09-28; re-run `docker inspect … Config.Labels` before acting |
| 2 | `compose.yaml` is only *edited* (no `compose up`) so the live container is untouched | any `up`/`recreate` risks the wipe | Hard rule: no compose lifecycle verb; validate with `config` only |
| 3 | 🔴 Nothing auto-runs `compose.yaml` | **FALSE** — `start-/stop-ki-basis.*` do; surfaced in §3 | Fixed premise; Option A neutralizes the *data-loss* part; scripts flagged separately |
| 4 | Named volumes `ki-basis-hermes-data/-workspaces` don't exist | if they exist later, a recreate mounts them empty | `docker volume ls`; confirmed absent 2026-09-28 |
| 5 | A manual `docker stop` for backup stays stopped across daemon restart | if not, an unexpected auto-start mid-backup | Verified behavior in D-18 (`unless-stopped` honors manual stop) |
| 6 | Private Hermes is on `ki-basis-net` only, not `shared-db-net` | a wider blast radius touching shared PG | Confirmed in `compose.shared-db.yaml` L179–180; edit doesn't touch networks |
| 7 | Nothing `depends_on` Hermes | stopping it for backup could cascade | `compose.shared-db.yaml`: hermes depends on others, nothing depends on hermes |
| 8 | Editing `compose.yaml` won't disturb firefly/paperless data | those still live in named/shared volumes | The edit is Hermes-only; other services' data volumes/DBs untouched |
| 9 | D-17 alias-collision won't recur from this change | a rename (Option C) could tempt a hand-run of the stale file | Prefer edit over rename; if renaming, update all 5 refs in one pass |
| 10 | Secrets stay out of scope | leaking `.env` values | This doc reads env **key names only** (`COMPOSE_PROJECT_NAME`, `KI_NETWORK_NAME`), never secret values |

## 8. Definition of done / operator go-no-go
Operator has an evidence-backed, minimal, data-safe plan. **Nothing has been changed on the live system.**
To proceed, the operator must explicitly choose, per action:
- [ ] **G0** — run the backup (§5.3) and confirm `integrity_check=ok` + spot-check counts. *(required first)*
- [ ] **G1** — apply **Option A** text edit (§5.2) — OR choose **"keep parked + guard"** (Option C) — OR defer.
- [ ] **G2** — decide scope of the **separate** stale-lifecycle-script remediation (repoint to
      `compose.shared-db.yaml` / add fail-closed guard) — tracked apart from T10.

Recommended answer: **G0 → G1 (Option A) now; G2 as a separate ticket.** "Keep parked + guard" is an equally
data-safe, welcome outcome — the bar is data-safety, not tidiness.

## 9. Execution record (2026-09-28, operator-approved)
Operator selected **G0 (backup) → G1 (Option A)** via the "hot, no downtime" backup method. All steps were
read-only or additive; the **live `ki-basis-hermes` container was never stopped, recreated, or `compose up`-ed.**

**G0 — verified backup (safety net):**
- Hot `tar` (no container stop) → `/root/backups/t10-20260928/` on ext4:
  - `hermes-data.tar` 4,565,790,720 B — `sha256 22c0413876a2e19dc73664259f98e0f6c4163e0213291c6c3d9eeca8df40f31c`
  - `hermes-workspaces.tar` 3,615,068,160 B — `sha256 b1212ca7b007d2aeb132f4cb53c734c0f3fee06b9d31ff465febf38820874004`
  - hashes also in `SHA256SUMS.txt`. Both tar exit 0 (clean, no torn WAL — `state.db-wal` was 0 B).
- **Restore proven** (extracted to throwaway `/root/restore-test`, since removed): `PRAGMA integrity_check = ok`,
  `quick_check = ok`, 60 objects in `sqlite_master`; restored↔live counts matched exactly
  (sessions 10, memories 4, skills 16, cron 4, hooks 0, profiles 5). Note: no `sqlite3` CLI on host or in the
  container — integrity checked via `python3`'s stdlib `sqlite3` module.

**G1 — Option A applied to `ki-basis/compose.yaml`:**
- File-level rollback copy: `ki-basis/compose.yaml.t10-bak-20260928` (also under git, working tree was clean).
- Deterministic CRLF-preserving patch (each block asserted to match exactly once before writing):
  (1) removed the unused top-level `hermes_data`/`hermes_workspaces` named-volume declarations;
  (2) Hermes service `volumes:` → the live bind mounts `/root/.hermes:/opt/data` + `/root/workspaces:/root/workspaces`
  with an explanatory comment.
- Verified: `docker compose … config --quiet` = **PARSE OK**; rendered `services.hermes.volumes` = the two
  **bind** mounts == live inspect (meets the PLAN acceptance criterion); top-level volume list no longer
  contains `hermes_*`; `docker inspect ki-basis-hermes` unchanged (running, `Created=2026-09-26T12:24:53Z`,
  same two binds).
- **Not committed** — left as a reviewable working-tree change for the operator. Rollback:
  `git checkout -- ki-basis/compose.yaml` (or restore the `.t10-bak-20260928` copy).

**Still OPEN — G2 (separate scope, NOT done here):** `scripts/start-ki-basis.{sh,ps1}` / `stop-ki-basis.*` still
target the stale `compose.yaml` + `.env.private`/`.env` (pre-ADR-002 topology: local `postgres`, no
`shared-db-net`, no OpenProject rewire). After Option A they can no longer **wipe** Hermes, but running them
would still recreate the private stack onto the retired topology — a **recoverable outage**. Recommend a
separate operator-scoped fix: repoint the scripts to `compose.shared-db.yaml` + `.env.shared-db` + `-p ki-basis`,
or add a fail-closed guard. Community lifecycle is unaffected (`.env.community` absent; community runs from its
own repo/project).
