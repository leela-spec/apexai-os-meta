---
type: Performance Findings
title: RAM optimization — high-impact opportunities (live-measured + web-researched)
description: >
  Companion to RamUseage.md. Confirms the ~6 GB of "active" WSL memory is the containers, pinpoints the two
  OpenProject instances as ~60% of it, and ranks concrete, mostly env-only optimizations by impact/risk —
  grounded in live docker stats/inspect (2026-09-29) and current best-practice sources.
created: 2026-09-29
companion: ki-basis/docs/PerformanceEvaluation/RamUseage.md
verified: "live docker stats + docker inspect on the WSL2 Apex engine, 2026-09-29"
---

# RAM optimization — high-impact opportunities

Your `RamUseage.md` diagnosis is correct: the 16 GB is a ceiling, cache is reclaimable, and the stubborn part
is the **anonymous pages owned by running Linux processes** (~6 GB). This file answers the open question it
implies — *which processes, and can we shrink them* — with live numbers and researched fixes.

## 1. Where the ~6 GB actually is (live, 2026-09-29)
| Container | RAM | Note |
|---|---|---|
| **leela-op178-openproject** (private) | **2.37 GiB** | #1 consumer · **no memory-tuning env set** (defaults) · Ruby 4.0.6 |
| **community-openproject** | **1.36 GiB** | #2 · already has `OPENPROJECT_WEB_WORKERS=1` + `BACKGROUND_WORKERS=1` · Ruby 3.3.4 |
| community-paperless | 0.72 GiB | workers capped to 1 |
| ki-basis-paperless (private) | 0.68 GiB | **workers at default** (not capped) |
| ki-basis-hermes / community-hermes | 0.40 / 0.32 GiB | |
| ki-basis-shared-postgres | 0.17 GiB | |
| firefly ×2 / valkey ×2 / nginx ×2 | < 0.2 GiB total | negligible |
| **Total** | **≈ 6.2 GiB** | matches your "~6.3 GB active" exactly |

**Headline: the two OpenProject (Ruby/Puma) instances = 3.73 GiB ≈ 60% of the stack.** That is the target;
everything else is small. Also note **no container has a memory limit** (all unlimited).

## 2. Ranked opportunities (impact × risk)
| # | Opportunity | Expected saving | Risk | Evidence |
|---|---|---|---|---|
| **1 — HIGH, do first** | **Cap the private OpenProject workers.** `leela-op178-openproject` runs at **defaults** while `community-openproject` (with `OPENPROJECT_WEB_WORKERS=1` + `OPENPROJECT_BACKGROUND_WORKERS=1`) uses **~1 GB less**. Set the same two vars on the private instance. | **~0.5–1.0 GB** | Low — 1 worker is OpenProject's own documented small-instance setting (already used by community + by ADR §2.4). | OpenProject scaling docs; your own live delta |
| **2 — HIGH, env-only** | **`MALLOC_ARENA_MAX=2` on BOTH OpenProject** (and optionally firefly). Rails/Puma RSS bloats from glibc creating many memory arenas under threads; capping arenas is the classic fix. | **~10–30 % of Ruby RSS ≈ 0.4–1.0 GB** across the two | Very low — env var only; slight CPU trade-off. | Rails "Tuning Performance for Deployment"; Heroku default `MALLOC_ARENA_MAX=2`; Perham "Taming Rails memory bloat" |
| **3 — HIGH, stronger version of #2** | **jemalloc** for Ruby (`LD_PRELOAD=libjemalloc.so.2`) instead of glibc malloc — bigger, more reliable RSS cut than arena-capping. (The "jemalloc is unmaintained" advice is **outdated** — Meta recommitted to it.) Needs the allocator present in the image. | **often > #2** | Low–med — needs `libjemalloc2` in the image / a rebuild; verify it loads. | Rails guide (jemalloc = "highly recommended"); ruby-alloc-bench |
| **4 — MEDIUM, behavioral** | **Run community OpenProject on-demand**, not 24/7. If community PM isn't used daily, stopping it frees its **1.36 GiB** entirely; start it only when needed. | **~1.36 GB when stopped** | Low (operator choice) — community is a separate project; start/stop is clean. | your live stats |
| **5 — LOW/FREE** | **Cap private paperless workers** to match community (`PAPERLESS_WORKERS=1`, `PAPERLESS_TASK_WORKERS=1`, `PAPERLESS_THREADS_PER_WORKER=1`). | ~0.1–0.2 GB | Very low | ADR §2.4 already prescribes this |
| **6 — SAFETY, not a saving** | **Add per-container `mem_limit`** (e.g. OpenProject 1.5 GB, paperless 768 MB) so no single service can balloon and starve Windows/the iGPU. | bounds worst case | Low — set limits above steady state to avoid OOM-kills. | Docker Compose `mem_limit` |
| **7 — CAUTION, do NOT rush** | `[experimental] autoMemoryReclaim=gradual` in `.wslconfig` to return cache faster. | reclaims cache (already reclaimable under pressure) | ⚠️ **Med–HIGH for your setup** — reported to **break a natively-run `dockerd` inside WSL2** (exactly your engine) and to conflict with zswap. | microsoft/WSL #11066; WSL config docs |
| **8 — OPTIONAL** | Postgres `shared_buffers` is 1 GB allocated but the container only holds ~0.17 GiB resident; lowering to 256 MB trims *commit* a little. Low real impact. | small (commit only) | Low | pg tuning |

## 3. Why this is the right focus
- The reclaim/`.wslconfig` angle (your report's main axis) mostly touches the **7.7 GB reclaimable cache**,
  which Windows can already take back under pressure. The **6 GB anonymous** is the part that actually
  "sticks" — and it's dominated by two Ruby apps. Shrinking them is where the durable win is.
- **Opportunities #1 + #2 are env-only, reversible, and target the biggest consumer** — realistically
  **~1–1.5 GB** off a 6 GB footprint with near-zero risk and **no architecture change**. That's the
  high-impact move.
- Bigger structural saving exists (#4: don't run two full stacks 24/7) but that's a usage decision, not tuning.

## 4. How to apply (operator-gated — these touch live containers)
These edit compose env + require an OpenProject **container recreate** to take effect. Recreate is safe here
(OpenProject state lives in the DB + `openproject_assets` volume, not the container) **provided the DB URL /
SECRET_KEY_BASE are unchanged** — so it's a config-only recreate, no data migration. Suggested order:
1. **Backup posture:** OpenProject data is in `priv_openproject` / `comm_openproject` on the shared cluster +
   the assets volume — unaffected by an env-only recreate. (A DB dump beforehand is cheap insurance.)
2. **#1 + #2 together on `leela-op178`** (`leela-op178/compose.shared-db.yaml`, not git-tracked): add
   `OPENPROJECT_WEB_WORKERS=1`, `OPENPROJECT_BACKGROUND_WORKERS=1`, `MALLOC_ARENA_MAX=2`; `docker compose up -d`
   the openproject service; measure `docker stats` before/after.
3. **#2 on community** (`lika-community/compose.wsl.yaml`): add `MALLOC_ARENA_MAX=2`; recreate; measure.
4. **#5** private paperless caps; recreate.
5. Re-check with `docker stats --no-stream` and `free -h` inside WSL; keep the ones that helped.
6. **#3 (jemalloc)** only if #1/#2 aren't enough — first check whether the OpenProject image already ships
   `libjemalloc2` (`docker exec … ldconfig -p | grep jemalloc`); avoid rebuilding the image just for this.

**Measurement discipline:** change one lever at a time, `docker stats` before/after each, so the effect is
attributable (same rigor as the infra-health test). Nothing here changes the architecture; all reversible by
removing the env var + recreating.

## 5. Sources
- Ruby on Rails — Tuning Performance for Deployment (jemalloc, `MALLOC_ARENA_MAX=2`, Puma/threads).
- Heroku Dev Center — default `MALLOC_ARENA_MAX=2` for new Ruby apps.
- Mike Perham — "Taming Rails memory bloat"; dev.to — "Why Rails memory bloat happens (2025)"; ruby-alloc-bench.
- OpenProject — system requirements & scaling docs (web/background workers).
- microsoft/WSL #11066 + WSL config reference — `autoMemoryReclaim` modes and the native-dockerd caveat.
