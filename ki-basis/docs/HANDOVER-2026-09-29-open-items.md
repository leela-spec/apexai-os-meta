---
type: Handover
title: ki-basis handover — what to test and change next (2026-09-29)
description: >
  Answers four specific open questions about the post-WSL2-consolidation ki-basis stack (OpenProject skill
  access, Hermes repo-clone workspaces, private-vs-community build differences) with live-verified evidence
  from this session, then gives one consolidated open-items checklist merging those findings with
  PerformanceEvaluation and the ranked failure register. Self-contained — no other file required to act on it.
created: 2026-09-29
okf_version: "0.2"
verified: "live docker ps / docker volume inspect / opCall.js calls on the WSL2 Apex engine, 2026-09-29"
see_also:
  - InstallationInsights.md — full timeline + ranked failure register (R1–R12) this handover assumes as background
  - PerformanceEvaluation/RAM-Optimization-Findings-2026-09-29.md, RamUseage.md — the RAM findings folded in below
  - ki-basis/docs/openproject/FUTURE-DEVELOPMENT-least-privilege-agent-identity.md
current_truth: ki-basis/docs/INFRASTRUCTURE.md
---

# ki-basis handover — 2026-09-29

**For the next chat.** This is a snapshot taken live today, after the WSL2 consolidation and after the
OpenProject skill's network fix. Read §1–4 for the four questions that were asked; read §5 for the single
merged checklist of what to test/change next. Nothing here requires opening another file to understand,
though sources are linked for anyone who wants to go deeper.

**Live state at time of writing** (`docker ps -a` on the WSL2 Apex engine):

| Container | Status |
|---|---|
| `ki-basis-shared-postgres`, `ki-basis-firefly`, `ki-basis-paperless`, `ki-basis-nginx`, `ki-basis-hermes` | Up 28h, healthy |
| `ki-basis-postgres` (old private-only Postgres, pre-shared-DB) | **Exited** 3 days ago — expected, superseded by `ki-basis-shared-postgres` |
| `leela-op178-openproject` (private OpenProject, separate compose project) | Up 28h |
| `community-firefly`, `community-paperless`, `community-nginx`, `community-openproject`, `community-hermes`, `community-valkey` | Up 28h, healthy |
| `hermes-d04f865b`, `hermes-d397cf57`, `hermes-preext-20260826` | **Exited**, 3–4 weeks old — leftover from earlier Hermes runtime experiments, candidates for pruning (see §5) |

---

## 1. Is the OpenProject skill-access problem solved by moving skills to `C:\GitDev\agent-skills\skills\openproject`?

**Partly — it fixed a different problem than the one that was actually blocking access, and that second
problem is now also fixed, separately, the same day.** Two distinct issues were both live at once:

**Problem A — skill duplication/drift.** The OpenProject skill had been copied into two product repos
(`Leela-Cloud-2026/.agents/skills/openproject` and `Investment/.agents/skills/openproject`), and the copies
had already drifted (`SKILL.md` 92 vs 123 lines — different content, same name). Fixed 2026-09-28: the skill
now lives in exactly one place, `C:\GitDev\agent-skills\skills\openproject` (its own git repo), linked into
every agent's discovery path via Windows junctions and WSL symlinks (`~/.claude/skills/openproject`,
`~/.agents/skills/openproject`, `~/.gemini/config/skills/openproject`) — zero copies. The API token also
moved out of any repo to `~/.config/openproject/op.env`. **This move only changed where the skill's code and
secret live. It did not touch networking.**

**Problem B — the skill couldn't actually reach OpenProject (register ID R11).** Separately, the skill's
Node client got `ECONNREFUSED 127.0.0.1:8083` when called from Windows, because WSL2's NAT networking never
forwards a container port published to `127.0.0.1` **inside** the VM out to Windows. This was fixed later
the same window: `leela-op178/compose.shared-db.yaml` now publishes the port as `0.0.0.0:8083:80`, with an
inline comment recording why:
```yaml
ports:
  # Published on all WSL interfaces so the Windows host can reach it via
  # localhost forwarding (WSL2 NAT does not forward a 127.0.0.1-only bind).
  # Windows-host access only is enforced by the Hyper-V firewall (default deny inbound).
  - "0.0.0.0:8083:80"
```

**Verified live, this session, from Windows:**
```
node client/opCall.js root    → 200, coreVersion "17.8.0"
node client/opCall.js whoami  → 200, login "admin", admin: true
```
So: the skill-location fix and the network fix are **both** done, and the skill **currently works** end to
end from Windows.

**Still open:**
- The authenticated identity is the **OpenProject built-in `admin` account**, not the "dedicated
  least-privilege Leela agent account" the skill's own `SKILL.md` calls for. A gap doc for this already
  exists: `ki-basis/docs/openproject/FUTURE-DEVELOPMENT-least-privilege-agent-identity.md`. Not yet created.
- ~~Paperless and Firefly were never re-audited for the same `127.0.0.1`-vs-`0.0.0.0` publish issue.~~
  **Resolved 2026-09-29:** all 12 agent-facing ports on both stacks (OpenProject/Firefly/Paperless/Nginx/
  Hermes-gateway/Hermes-dashboard × private+community) tested live with `curl` from Windows — all reachable,
  even the ones still bound to `127.0.0.1` in compose. WSL2's default `localhostForwarding` relays regardless
  of the container's internal bind address on this native-`dockerd` engine; `0.0.0.0` was the correct fix for
  OpenProject's specific case, not a universal requirement. (A first pass with a 3s timeout gave 2 false
  negatives — retest at ≥8s before calling a port broken.) Full finding:
  `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` §6 addendum; canonical record: `OPEN-ISSUES.md` I03.

---

## 2. Where are the local repo clones Hermes is supposed to work with — did they survive the rebuild?

**It depends on which Hermes — private and community use different storage, and only one currently has
clones in it.**

**Private Hermes (`ki-basis-hermes`)** mounts a **bind mount**, not a Docker volume:
```yaml
volumes:
  - /root/.hermes:/opt/data
  - /root/workspaces:/root/workspaces
```
`/root/workspaces` is a real directory on the WSL2 VM's own ext4 filesystem. Checked live this session
(`ls -la` + `du -sh` inside the VM) — **it survived the rebuild intact:**

| Repo | Size | Last modified |
|---|---|---|
| `apexai-os-meta` | 1.8 GB | Sep 7 |
| `MasterOfArts` | 1.7 GB | Sep 7 |
| `Investment` | 35 MB | Sep 23 |
| `acim-secular` | 17 MB | Aug 25 |

Owned by uid/gid `10000` (the container's internal `hermes` user) — expected, not a permissions problem.

**Community Hermes (`community-hermes`)** mounts a **Docker-managed named volume** instead:
```yaml
volumes:
  - hermes_workspaces:/root/workspaces
```
Checked live this session — resolved the volume to its real path and listed it:
```
docker volume inspect community_hermes_workspaces
  → Mountpoint: /var/lib/docker/volumes/community_hermes_workspaces/_data
  → CreatedAt: 2026-09-26T13:34:23+02:00   (the WSL2 cutover date)
ls -la <mountpoint>
  → empty (only . and ..)
```
**Community Hermes currently has zero repo clones.** The volume was created fresh at cutover and nothing has
been cloned into it since.

**Still open:**
- Confirm whether community Hermes is actually expected to operate on repo clones at all (check its
  `SOUL.md` / actual task scope in `lika-community/SOUL.md` before assuming this is a bug rather than
  by design — community's role may be Telegram/PM-facing only, not a code agent).
- If it is expected to have clones: decide which repos, then clone them into the volume (or bind-mount it
  the same way private does, for consistency — see §3 below for the tradeoff).

---

## 3. Why do the private and community stacks build differently, and what does that cost in performance/interaction?

Read directly from the compose files (`ki-basis/compose.yaml` + `compose.shared-db.yaml` vs.
`lika-community/compose.yaml` + `compose.wsl.yaml`). Four concrete differences, each with a consequence:

**a) Hermes storage type — bind mount (private) vs. named volume (community).**
Private: `/root/.hermes` and `/root/workspaces` are bind-mounted straight to VM-native ext4 paths. Community:
`hermes_data` and `hermes_workspaces` are Docker-managed named volumes. Both ultimately sit on the same VM's
ext4 (neither is on the slow `/mnt/c` 9P bridge), so **raw I/O performance is not meaningfully different**.
The real consequence is **operability and risk**: a bind mount is a plain directory you can `ls`, back up, or
`rsync` directly; a named volume is abstracted behind `docker volume inspect` and is easy to lose track of.
This exact mismatch — a compose file declaring one type while the live container actually used the other —
is what caused a near-data-loss incident on the private side (register ID R5: a plain `compose up` would
have wiped ~7.9 GB before the compose file was corrected to declare the bind mount explicitly). Community
avoided that specific incident only because its declaration and reality have stayed consistent so far.

**b) OpenProject placement — external project (private) vs. embedded service (community).**
Private `ki-basis/compose.yaml` deliberately has **no `openproject` service at all** — the real private
OpenProject (`leela-op178-openproject`) is a fully separate Compose project with its own compose file. A
comment in `compose.shared-db.yaml` explains why: including it once caused a real incident where a copied
service block resurrected a retired v14 OpenProject container that crash-looped against an already-migrated
schema. Community's compose, by contrast, embeds `openproject` directly as one of its own services.
**Consequence:** restarting or recreating the private `ki-basis` stack never touches OpenProject (it's a
separate blast radius); doing the same for community always restarts OpenProject with it, since they're one
Compose project.

**c) Worker/memory tuning — capped by default (community) vs. uncapped (private).**
Community's compose bakes in `OPENPROJECT_WEB_WORKERS=1`, `OPENPROJECT_BACKGROUND_WORKERS=1`, and
`PAPERLESS_WORKERS=1` (+ task/thread caps) as defaults. Private's compose sets no equivalent Paperless caps,
and the separate `leela-op178` OpenProject project has no worker caps either. This is exactly what
`PerformanceEvaluation/RAM-Optimization-Findings-2026-09-29.md` measured live on 2026-09-29: **the private
`leela-op178-openproject` uses 2.37 GiB (uncapped, defaults) vs. community-openproject's 1.36 GiB (capped)**
— a ~1 GB difference from two environment variables. That file ranks matching the private instance's env to
community's as the single highest-impact, lowest-risk fix available (see §5).

**d) A legacy risk still sits on disk, unused but present.**
Community's original, Docker-Desktop-era `compose.yaml` still binds a OneDrive-synced path directly into the
container: `C:/Users/gehma/OneDrive/Dokumente/Terminal/outputs/call-agenda-demo:/opt/data/call-agenda` — the
exact anti-pattern the failure register flags as R6 (a cloud-sync client can rewrite or lock files underneath
a running container). It is not currently live — the WSL2-native `compose.wsl.yaml` (the file actually in
use, per its own header comment and confirmed by the live `community_` — prefixed volume names) replaced
that bind with a proper named volume (`call_agenda`). The old file is kept only "as rollback reference," so
the risk returns only if someone runs it by mistake.

---

## 4. Consolidated open-items checklist

Merges §1–3 above with `PerformanceEvaluation/RAM-Optimization-Findings-2026-09-29.md` and the ranked
failure register in `InstallationInsights.md`. Ordered roughly by impact × effort.

| # | Item | Why | Suggested next step |
|---|---|---|---|
| 1 | Cap private `leela-op178-openproject` workers: `OPENPROJECT_WEB_WORKERS=1`, `OPENPROJECT_BACKGROUND_WORKERS=1`. | ~0.5–1.0 GB saving, low risk — community already does this. (§3c) | Add to `leela-op178/.env.shared-db`, recreate the container, measure with `docker stats`. |
| 2 | Add `MALLOC_ARENA_MAX=2` to both OpenProject instances (private + community). | ~10–30% of Ruby RSS, env-only, very low risk. | Same recreate-and-measure pattern as #1. |
| 3 | Re-audit Paperless and Firefly for the same `127.0.0.1`-vs-`0.0.0.0` publish issue that blocked OpenProject (R11). | Untested whether an agent skill hitting these from Windows would also get `ECONNREFUSED`. | `curl` each from Windows as-is; if it fails, apply the same `0.0.0.0:PORT:...` fix used for OpenProject. |
| 4 | Create the dedicated least-privilege OpenProject agent account; stop using the `admin` token for skill calls. | Skill currently authenticates as full OpenProject admin — works, but wider blast radius than intended. | Follow `ki-basis/docs/openproject/FUTURE-DEVELOPMENT-least-privilege-agent-identity.md`. |
| 5 | Decide whether community Hermes needs repo clones at all; if yes, populate `community_hermes_workspaces` (currently empty). | Confirmed empty live; private Hermes has 4 real clones (3.5 GB total), community has zero. | Check `lika-community/SOUL.md` / its actual task scope first — this may be by design, not a gap. |
| 6 | Cap private Paperless workers (`PAPERLESS_WORKERS=1`, `PAPERLESS_TASK_WORKERS=1`, `PAPERLESS_THREADS_PER_WORKER=1`) to match community. | Small (~0.1–0.2 GB) but free and already proven safe on the community side. | Add to `ki-basis/.env`, recreate. |
| 7 | Add per-container `mem_limit` to both OpenProject instances (e.g. 1.5 GB) and Paperless (e.g. 768 MB). | Bounds worst case; currently **no container in either stack has a memory limit** (all unlimited). | Add `mem_limit:` under each service in the relevant compose file. |
| 8 | Verify `leela-op178/compose.shared-db.yaml`'s inline `SECRET_KEY_BASE` is not committed to git in plaintext. | The register's R-finding pattern (a rotated secret re-leaking in a committed file) has recurred before; this file was read directly and has the value inline. | `git log --all -- leela-op178/compose.shared-db.yaml`; if committed, rotate and move to `.env.shared-db`. |
| 9 | Prune the 3 stale exited Hermes containers (`hermes-d04f865b`, `hermes-d397cf57`, `hermes-preext-20260826`), 3–4 weeks old. | Cosmetic/hygiene — confirmed exited, not referenced by any current compose project. | Confirm nothing depends on them, then `docker rm`. |
| 10 | Do **not** enable `.wslconfig`'s experimental `autoMemoryReclaim=gradual`. | Flagged in `RAM-Optimization-Findings` as medium–high risk specifically for a native `dockerd`-in-WSL2 setup (this one) — can break the engine (`microsoft/WSL#11066`). | Leave as-is; not a "to-do," a do-not. |
| 11 | Confirm community's legacy `compose.yaml` (with the OneDrive bind) is never run by accident. | Risk is dormant, not active — but the file still exists and still has the anti-pattern. | Consider renaming it `compose.yaml.docker-desktop-rollback-only` or adding a runtime guard. |
| 12 | Re-run the full R1–R10 install-script requirements as acceptance criteria if/when a from-scratch install is attempted. | Those are the baseline "don't repeat the last 3 months" rules; this handover only adds to them, doesn't replace them. | See `InstallationInsights.md` §2–3. |
