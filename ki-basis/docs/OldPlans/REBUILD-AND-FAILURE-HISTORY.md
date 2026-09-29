---
type: Failure History
title: ki-basis architecture — rebuild & failure history (ranked, for a correct install script)
description: >
  A truthful, ranked reconstruction of ~2 months of ki-basis architecture rebuilds and failures — from git
  commits AND out-of-git artifacts (the 27 Jun "Docker-Fließband" runbook, the manual Docker Desktop build,
  the live WSL2 cutover). Purpose: document what went wrong and why, honestly, so a NEW installation script
  lets another user reach the current architecture WITHOUT the rebuilds and wrong runbooks. Current truth:
  ki-basis/docs/INFRASTRUCTURE.md.
created: 2026-09-29
sources: "git log (apexai-os-meta, 2026-04-29 → 2026-09-29, 1549 commits); 03-wsl2-native-stack-consolidation/02-decisions-log.md (D-01…D-18); OldPlans/INDEX.md; DUAL_INSTANCE_ARCHITECTURE.md §6 (ADR-002); operator-supplied 27-Jun screenshot"
honesty_note: "Some work happened OUTSIDE git (the 27-Jun PDF could not be located/read; the manual Docker Desktop build and the live cutover were hand-run). Those are reconstructed from the decision ledger + commit trail and are marked [out-of-git]."
---

# ki-basis architecture — rebuild & failure history

**Why this exists.** We rebuilt this architecture repeatedly for ~2 months. Docker Desktop was a wrong
foundation; the "airtight separation / two databases" model was over-engineered; several runbooks were
hypothesised, not verified, and caused live incidents. This file records those failures **truthfully and
diligently** so a future **installation script** takes the shortest correct path and no one repeats the
rebuilds. The end state it should install is described in [`../INFRASTRUCTURE.md`](../INFRASTRUCTURE.md).

## 1. The arc (chronological — git + out-of-git)
| When | Milestone | Source |
|---|---|---|
| **2026-06-27** | "Docker-Fließband, noch in Arbeit" — first Docker assembly-line runbook (8 pp, incomplete) | **[out-of-git]** (operator screenshot; file not recoverable) |
| 2026-08-08 | Hermes V2 platform research begins | git |
| 2026-08-10/11 | OpenClaw **local-LLM executor** architecture locked → **abandoned**: local 8B not viable + **GPU failure** (Intel Arc 140V Vulkan device-lost) | git (`FEE/…CORRECTION`, `GPU_Failure/`) |
| 2026-08-24 | Hermes **multi-repo v2** epic (Antigravity, P00–P18), WSL workspace-migration plan → **impl never authorized / deferred**; "Docker concurrency incident cluster" recorded | git |
| 2026-08-25 | Hermes **WSL/DrvFs git-performance** package (ARCH-IMP-01) → later found to carry **wrong file-count data** (corrected) | git |
| 2026-08-26 | **ARCH-IMP-02 single-container** Hermes migration + **containerd downgrade** plan → **failed** (repeated ❌ workarounds; folder later "Inbetween_Delete") | git |
| **2026-09-01** | Full ki-basis Docker stack built **M1–M9** (postgres/firefly/paperless/openproject/nginx/hermes) **on Docker Desktop**; a "**13-module docker stack integrity correction program**" ships the same day | git + **[out-of-git]** manual build |
| 2026-09-02/03 | "migration to **Docker Desktop Hyper-V**" verified; finalization program (security/backup/restore/auth) — all on Docker Desktop | git |
| 2026-09-07 | Dual KI-basis **audit dossier** + `new_final_v4` (the verbatim-duplicated dossier) | git |
| **2026-09-25/26** | **THE BIG PIVOT** — Docker Desktop's LinuxKit VM proved a 2nd RAM-hungry layer that crashed (`'DockerDesktopVM' unable to allocate 8192 MB`). **ADR-002**: retire Docker Desktop → **one WSL2-native engine + one shared PostgreSQL**; community backed up & restored; OpenProject **17.8 fresh** (`leela-op178`), v14 retired→deleted | **[out-of-git]** live cutover + git (`03-`/`ADR-002`) |
| 2026-09-26 | Cutover incidents fixed live (D-13…D-18): DNS ambiguity, resurrected v14, restore quirks, volume drift | git ledger |
| 2026-09-28/29 | Close-out: **T10** Hermes volume-drift data-loss fix; **infra-docs remediation R1–R7**; this history | git |

## 2. Ranked failure / rebuild register
Ranked by **cost + preventability** — i.e. what most needs to NOT happen to the next installer. Each entry:
what happened → root cause → the wrong runbook/instruction → the install-script requirement it implies.

| # | Failure / rebuild | Root cause | Wrong runbook/instruction | → Install-script requirement |
|---|---|---|---|---|
| **R1 — CRITICAL** | Built the **entire stack on Docker Desktop (Sep 1–7), then ripped it out** for WSL2-native (Sep 26). | Docker Desktop's LinuxKit VM = a **second RAM-hungry VM** on a shared-memory host; it crashed (couldn't allocate 8 GB). The engine choice was left ambiguous (ADR-001) and defaulted to Desktop. | The whole `ImplementationPlans/*-ANTIGRAVITY` + `2026-09-03-finalization` set + "migration to Docker Desktop Hyper-V" | **Install on WSL2-native `dockerd` ("Apex", Ubuntu) from the start. Never Docker Desktop.** Assert `docker context` is the WSL engine; fail if Docker Desktop is present. |
| **R1b — HIGH (foundational, co-#1 with R1)** | **9P (`/mnt/c`) filesystem bottleneck** — running DB/container state or git repos on the Windows drive over WSL2's 9P bridge caused ~80–1400× slowdowns, **350% runaway CPU**, D-state (uninterruptible) locks, git stalls, and OpenProject `chown`/`fcntl` crash-loops. | State/repos placed on `/mnt/c` (9P/`v9fs` over the hypervisor) instead of the VM's native ext4. | Early plans put workspaces/data on `/mnt/c`; the **DrvFs git-performance package** (ARCH-IMP-01, 2026-08-25) diagnosed it but its modules 00–05 carried **wrong file-count data** (corrected in `06-VERIFICATION-AND-CORRECTED-SOLUTION`). | **All DBs / container state / git repos on native ext4** (`/var/lib/docker/volumes`, `/root/…`). Only read-only static config may bind from `/mnt/c`. **Never run a database or a git repo off `/mnt/c`.** |
| **R2 — CRITICAL** | **Over-engineered isolation**: "airtight dual-instance, zero shared DBs, two separate Postgres" (ADR-001) → **reversed** to ONE shared Postgres (D-07, ADR-002). | Isolation treated as an absolute; recreated a Strategy-B split it had itself warned against; doubled tuning/backup surface. | ADR-001 §3.4 "no shared … database connections"; `DUAL_INSTANCE_RUNBOOK.md` (two-postgres) | **One shared PostgreSQL cluster** (`ki-basis-shared`), per-tenant `priv_*`/`comm_*` DBs + roles, `REVOKE CONNECT` for isolation. Don't stand up two clusters. |
| **R3 — HIGH** | **Hermes containerization thrash (Aug)**: single-container Arch-3 + containerd **downgrade** failed; multi-repo v2 epic (huge) never authorized. | Chasing container-in-container / downgrade hacks before deciding the runtime model. | `02-hermes-single-container-runtime/G0.2`, `HERMES-OPTION2-DOCKER-DOWNGRADE-PLAN`, `hermes-multi-repo-orchestration-v2/*` | **Fix the Hermes model up front:** one `hermes-agent` container, state on **ext4 bind mounts** (`/root/.hermes`, `/root/workspaces`), gateway mode. No downgrades, no nested containers. |
| **R4 — HIGH** | **Copy-verbatim compose caused live incidents (D-17)**: an orphaned old `postgres` also aliased `postgres` → firefly/openproject crash-looped on the wrong DB; a **retired v14 OpenProject was resurrected** by a copied service block and crash-looped on an already-migrated schema. | Reusing service blocks without re-verifying **container identity**; two things sharing the `postgres` network alias. | `compose.shared-db.yaml` openproject block copied from `compose.yaml`; old `ki-basis-postgres` left running | **Never run two containers aliased `postgres` on one network. Verify identity before reusing a block. Use `leela-op178-openproject` by container name.** Script must stop/remove the old local postgres, never `--remove-orphans` blindly. |
| **R5 — HIGH** | **Volume drift → data-loss landmine (D-16 → T10)**: `compose.yaml` declared **named volumes** for Hermes while the live container ran **bind mounts**; a `compose up` would wipe ~7.9 GB. Old start-scripts were wired to that file. | Checked-in file drifted from reality; nobody re-applied; drift-prone rollback file left runnable. | `ki-basis/compose.yaml` (drifted) + `start-ki-basis.{sh,ps1}` | **Declared volume type MUST match reality (bind for Hermes). Pin it explicitly; never leave a drift-prone file wired into start scripts.** Add a pre-`up` mount-vs-declaration check. |
| **R6 — MEDIUM** | **OneDrive bind under a container data path (D-11)**: community Hermes had `…/OneDrive/…/call-agenda → /opt/data/call-agenda` — a cloud-sync layer under live state. | Convenience mount to a cloud-synced folder. | original community `compose.yaml` | **Never bind container state to a cloud-synced (OneDrive/Dropbox) path. Use ext4 named volumes.** |
| **R7 — MEDIUM** | **Restore quirks nearly bit (D-15)**: `pgvector` (`vector`) is not a "trusted" extension → `--role` restore fails without a superuser pre-create; OpenProject's **embedded PG17** dump needs a **pg17** client (pg16 can't read it). | Assuming one uniform restore command for all DBs. | (implicit in migration steps) | **Restore step must: pre-create `vector` as superuser before role-scoped restore; match `pg_restore` major version to each dump (pg17 client for the OpenProject dump).** |
| **R8 — MEDIUM** | **Local-LLM executor dead-end**: OpenClaw local 8B executor planned then found non-viable (capability + GPU device-lost). | Betting on local-model execution on unsuitable hardware. | `FEE/OpenClaw…Implementation Plan` | **Do not include a local-LLM executor.** Hermes routes to hosted models; the install script omits OpenClaw. |
| **R9 — MEDIUM** | **Runbooks were hypothesised, not verified**: the "13-module integrity correction program" shipped the same day as the build; the DrvFs package carried wrong file-count data; multiple "doc-truth correction" passes. | Plans written ahead of a real run; corrections chased after. | `docker-stack-integrity/*`, `01-hermes-wsl-drvfs…`, `06-DOCUMENTATION-TRUTH-CORRECTION` | **The install script must be validated against a real end-to-end run (health-tested), not shipped as an untested runbook.** |
| **R10 — LOW** | **Doc scatter & hazards** (fixed in R1–R7 remediation, 2026-09-28/29): 6 overlapping "current" docs, an agent-routing chain into the retired topology, an inline secret. | No single source of truth; superseded docs left unbannered. | see `../INFRASTRUCTURE.md` history / `05-program-closeout` | **One source of truth (`INFRASTRUCTURE.md`) + one install script; ship no competing runbooks.** |

## 3. Distilled requirements for the new installation script
A correct, first-time install of the current architecture (see [`../INFRASTRUCTURE.md`](../INFRASTRUCTURE.md)):
1. **Engine:** WSL2-native `dockerd` on Ubuntu ("Apex"). Refuse to proceed if Docker Desktop is the active context. (R1)
2. **Shared network + DB first:** `docker network create shared-db-net`; bring up `ki-basis-shared` (one PostgreSQL 16 + pgvector); create `priv_*`/`comm_*` DBs + roles; `REVOKE CONNECT` cross-tenant. (R2, R4)
3. **Extensions/restore:** pre-create non-trusted `vector` as superuser; use a pg-major-matched client per dump. (R7)
4. **Private stack** (`-p ki-basis`, `compose.shared-db.yaml`): valkey/firefly/paperless/nginx/hermes; **Hermes on ext4 bind mounts** `/root/.hermes` + `/root/workspaces`; volume declarations must match. (R3, R5)
5. **Community stack** (separate repo `lika-community`, `-p community`): named volumes, no cloud-synced binds. (R6)
6. **Private OpenProject:** `leela-op178` 17.8 fresh install on `shared-db-net` + `ki-basis-net`; wire Hermes to it **by container name**; never revive a v14. (R4)
7. **No:** Docker Desktop, two Postgres clusters, single-container/downgrade Hermes hacks, OneDrive binds, local-LLM executor, `--remove-orphans` on a mixed engine. (R1–R8)
8. **Keepalive + memory:** `.wslconfig` 16 GB; Startup `wsl-keepalive.vbs` (holds a `wsl` session so the VM doesn't idle-sleep). (D-06/D-10)
9. **Verify, don't assume:** run the health test ([`../../../apex-meta/orchestration/architecture-improvements/05-program-closeout/tests/infra-health-test.sh`](../../../apex-meta/orchestration/architecture-improvements/05-program-closeout/tests/infra-health-test.sh)) at the end; the script is "done" only when it's GREEN. (R9)

## 4. Evidence & links
- Current target architecture: [`../INFRASTRUCTURE.md`](../INFRASTRUCTURE.md) (+ `DUAL_INSTANCE_ARCHITECTURE.md` §6 / ADR-002).
- Incident ledger (authoritative): `apex-meta/orchestration/architecture-improvements/03-wsl2-native-stack-consolidation/02-decisions-log.md` (D-01…D-18).
- The failed/old plans themselves: [`INDEX.md`](INDEX.md).
- Close-out (T10 + infra-docs remediation): `apex-meta/orchestration/architecture-improvements/05-program-closeout/`.
- **Out-of-git, not recoverable:** the 2026-06-27 "Docker-Fließband" runbook PDF (recorded from operator screenshot only). If you still have the file, drop it into `OldPlans/` and it can be indexed properly.
