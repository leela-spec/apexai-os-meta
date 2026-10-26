---
type: Findings
title: Learnings — OpenProject Memory Optimization (Simulation F) & OpenProject 17.8 Architectural Inefficiencies
description: >
  Record of the Simulation F memory and worker optimizations applied to leela-op178-openproject and
  community-openproject, plus root-cause findings from live container and Ruby source inspection on
  Puma single-worker cluster overhead, jemalloc availability, ProjectType memcache staleness, and
  the missing is_default UI control in OpenProject 17.8.0.
tags: [findings, learnings, openproject, puma, memory, jemalloc, memcache, wsl2, docker]
created: 2026-10-08
status: current
canonical_current_state: ki-basis/docs/INFRASTRUCTURE.md
---

# Learnings: OpenProject Memory Optimization & OpenProject 17.8 Inefficiencies

## 1. Executed Changes & Verified Baseline (Simulation F — 2026-10-08)

Both OpenProject Compose stacks on the WSL2 Apex engine were updated to cap Puma/GoodJob workers, bound glibc memory arenas (`MALLOC_ARENA_MAX=2`), and enforce container memory limits (`mem_limit`), while preserving `SECRET_KEY_BASE` and the shared PostgreSQL databases (`priv_openproject`, `comm_openproject`).

| Instance | Compose File | Applied Settings | Memory Before | Memory After (Live Kernel PSS & cgroup) | Verification |
|---|---|---|---|---|---|
| **Private OpenProject 17.8** (`leela-op178-openproject`, service key `leela-openproject`) | [compose.shared-db.yaml](file:///C:/GitDev/leela-op178/compose.shared-db.yaml#L12-L35) | `OPENPROJECT_WEB_WORKERS: "0"` (single-mode)<br>`OPENPROJECT_WEB__MAX__THREADS: "4"`<br>`OPENPROJECT_GOOD__JOB__MAX__THREADS: "2"`<br>`USE_JEMALLOC: "true"`<br>`MALLOC_CONF: "narenas:2,dirty_decay_ms:1000,muzzy_decay_ms:0,background_thread:true"`<br>`MALLOC_ARENA_MAX: "2"`<br>`OPENPROJECT_COLLABORATIVE__EDITING__HOCUSPOCUS__URL: ""` + `disable-hocuspocus.sh` (Option 2A)<br>`mem_limit: 1536M` | `2.134 GiB / 15.62 GiB` (`2.37 GiB` peak, `145` PIDs) | **Post-boot:** `1.126 GiB` `anon` (`589.9 MiB` Puma PSS + `552.7 MiB` GoodJob PSS).<br>**Decayed idle steady-state:** **`925.9 MiB` (`0.904 GiB`) `anon` / `995.6 MiB` total `memory.current`** (`504.6 MiB` Puma PSS + `425.6 MiB` GoodJob PSS + `0.41 MiB` Hocuspocus sleep PSS; **`380–540 MiB` spike headroom**, `0 MiB` swap, `103` PIDs) | WSL & Windows `curl.exe` to `:8083/health_checks/default` → `200`; `/proc/161/environ` & `/proc/185/environ` confirm `LD_PRELOAD=libjemalloc.so.2` + `MALLOC_CONF` + `jemalloc_bg_thd` OS threads (`SPID 436,447,187,439`); `shared-db-net` aliases isolated |
| **Community OpenProject 14.x** (`community-openproject`; legacy v14 image, `ki-basis-openproject` retired per D-18) | [compose.wsl.yaml](file:///C:/GitDev/lika-community/compose.wsl.yaml#L111-L133) | `OPENPROJECT_WEB_WORKERS: 0` (single-mode)<br>`OPENPROJECT_BACKGROUND_WORKERS: 1`<br>`USE_JEMALLOC: "true"`<br>`MALLOC_CONF: "narenas:2,dirty_decay_ms:1000,muzzy_decay_ms:0,background_thread:true"`<br>`MALLOC_ARENA_MAX: "2"`<br>`mem_limit: 1792M` (Option 2B — full feature parity preserved) | `1.30 GiB / 15.62 GiB` | **`0 MiB`** in default `STOPPED` (`exited`, `restart: "no"`) state; **`~800 MiB / 1.75 GiB`** (`~950 MiB` spike headroom) when active | `:9082/` → `302` when tested; returned to default on-demand `exited` state |

---

## 2. Inefficiencies Discovered & Adopted Fixes (What the Builder Needs to Know)

### 2.1 Puma Single-Mode (`OPENPROJECT_WEB_WORKERS=0`), `jemalloc` `MALLOC_CONF` Tuning & Disabling Unused `hocuspocus` (`215 MiB` PSS)
- **What happens under `OPENPROJECT_WEB_WORKERS: "1"`:** Setting `OPENPROJECT_WEB_WORKERS: "1"` configures Puma (`config/puma.rb` → `workers OpenProject::Configuration.web_workers`) to run in **cluster mode with 1 worker** rather than single-process mode.
- **Why `OPENPROJECT_WEB_WORKERS=1` + unconfigured `jemalloc` + `hocuspocus` is inefficient:**
  1. **Puma cluster mode overhead:** Inside both `leela-op178-openproject` and `community-openproject`, `workers = 1` runs **both** a master process (~571 MB) and a forked cluster worker (~602 MB) with zero concurrency or feature gain over single-mode (`workers = 0`), prompting Puma 8.0.2 to log:
     `! WARNING: Detected running cluster mode with 1 worker. Running Puma in cluster mode with a single worker is often a misconfiguration. Consider running Puma in single-mode (workers = 0) in order to reduce memory overhead.`
  2. **Bundled `hocuspocus` server (`214.8 MiB` true kernel PSS vs. `321.1 MiB` gross summed RSS):** OpenProject 17.8's `/app/docker/prod/supervisord.conf.erb` unconditionally starts `[program:hocuspocus]` (`npm run start` → `node` + `tsx src/index.ts` + `esbuild`). Summing naive `VmRSS` across those 3 Node/TypeScript processes yields `321.1 MiB` (`69.9 + 58.9 + 192.3 MiB`) because shared `libnode`/V8 text segments are counted multiple times; reading kernel `/proc/<pid>/smaps_rollup` `Pss` (Proportional Set Size) shows the exact physical RAM footprint is **`214.8 MiB` PSS** (`56.3 + 43.7 + 114.9 MiB`) and 32 OS threads—even when `OPENPROJECT_COLLABORATIVE__EDITING__HOCUSPOCUS__URL` is set to `""`.
  3. **`USE_JEMALLOC=true` ignores `MALLOC_ARENA_MAX` & why `muzzy_decay_ms:0` is preferred under Linux cgroup v2:** Once `USE_JEMALLOC=true` exports `LD_PRELOAD=libjemalloc.so.2`, Ruby uses `jemalloc 5.3.0` instead of `glibc` `ptmalloc`. Without `MALLOC_CONF`, `jemalloc` on an 8-vCPU WSL2 VM defaults to **`33` arenas** (`opt.narenas: 32`), `dirty_decay_ms: 10000` (10s), and `background_thread: false` (so idle Ruby processes never purge decayed dirty pages). Furthermore, under Linux cgroup v2 (`memory.stat`), setting `muzzy_decay_ms > 0` causes `jemalloc` to release dirty pages via `madvise(MADV_FREE)` (`LazyFree`), which remain counted in cgroup `anon` and `memory.current` until `memory.max` triggers synchronous memcg reclaim—inflating reported memory usage and adding reclaim latency under burst load. Keeping `muzzy_decay_ms:0` (also `jemalloc 5.3.0`'s upstream default) forces `madvise(MADV_DONTNEED)` immediately after `dirty_decay_ms:1000`, unmapping physical pages asynchronously via `jemalloc_bg_thd`.
  4. **GoodJob thread pool:** `OPENPROJECT_BACKGROUND_WORKERS` is a legacy DelayedJob variable that is a no-op under GoodJob (`/app/config/application.rb` reads `OPENPROJECT_GOOD__JOB__MAX__THREADS`, defaulting to `20` threads).
- **Adopted Fix & Live Kernel `/proc` Verification:**
  1. **Private (`leela-op178/compose.shared-db.yaml` — Option 2A):**
     - `OPENPROJECT_WEB_WORKERS: "0"` (Puma single-mode), `OPENPROJECT_WEB__MAX__THREADS: "4"`, `OPENPROJECT_GOOD__JOB__MAX__THREADS: "2"`.
     - `USE_JEMALLOC: "true"` + `MALLOC_CONF: "narenas:2,dirty_decay_ms:1000,muzzy_decay_ms:0,background_thread:true"` (verified in live `/proc/161/environ`, `/proc/185/environ`, `/proc/161/maps` [`/usr/lib/x86_64-linux-gnu/libjemalloc.so.2`], and `ps -T` showing 2 `jemalloc_bg_thd` OS threads per Ruby daemon [`SPID 436, 447` in Puma; `SPID 187, 439` in GoodJob]). Puma PSS dropped from `707.6 MiB` → `589.9 MiB` (post-boot) → **`504.6 MiB`** (decayed steady-state); GoodJob PSS dropped from `599.6 MiB` → `552.7 MiB` (post-boot) → **`425.6 MiB`** (decayed steady-state).
     - Intentionally disabled unused `hocuspocus` collaborative editing via `OPENPROJECT_COLLABORATIVE__EDITING__HOCUSPOCUS__URL: ""` + `./disable-hocuspocus.sh:/app/docker/prod/hocuspocus:ro` (drops Hocuspocus PSS from `214.8 MiB` to **`0.41 MiB`**, bringing total container non-reclaimable `anon` heap down to **`1.126 GiB` post-boot / `925.9 MiB` (`0.904 GiB`) decayed steady-state** under the `1536M` ceiling).
  2. **Community (`lika-community/compose.wsl.yaml` + `.env.wsl` — Option 2B):**
     - Set `OPENPROJECT_WEB_WORKERS: 0` (Puma single-mode, eliminating the duplicate master process with zero feature or concurrency loss), preserved all Community services, enabled `USE_JEMALLOC: "true"` + `MALLOC_CONF: "narenas:2,dirty_decay_ms:1000,muzzy_decay_ms:0,background_thread:true"`, and set `mem_limit: 1792M` (`1.75 GiB`) for ~950 MiB spike headroom when woken on-demand.

### 2.2 Why `OPENPROJECT_RAILS__CACHE__STORE=memcache` Must Be Retained (Do Not Switch to `:memory_store`)
- **What was questioned:** Prior incident notes ([INCIDENT-cache-staleness-work-package-visibility.md](file:///C:/GitDev/apexai-os-meta/ki-basis/docs/openproject/INCIDENT-cache-staleness-work-package-visibility.md#L146-L150)) proposed switching `leela-op178-openproject` from `memcache` to `:memory_store` once capped to a single Puma process.
- **Why `:memory_store` is wrong here:** Even with `OPENPROJECT_WEB_WORKERS=0` or `1`, OpenProject runs `supervisord` with **two separate Ruby processes**: `./docker/prod/web` (`puma`) and `./docker/prod/worker` (`good_job start`). Switching `Rails.cache` to per-process `:memory_store` isolates cache state between `puma` and `good_job` and removes the ability to flush cache over localhost TCP without restarting the container.
- **Rule:** Keep `OPENPROJECT_RAILS__CACHE__STORE=memcache` (the in-container `memcached` daemon uses only ~5.7 MB RSS).

### 2.3 Root Cause of "Write Invisible Until Restart": `ProjectType` Missing `touch: true`
- **Symptom:** Enabling a work-package type on a project (e.g., via `Administration → Work packages → Types → Projects → Enable for all projects`) updates PostgreSQL immediately, but subsequent API v3 reads/creates still behave as if the type is disabled until container restart or cache expiry.
- **Root Cause (Verified in 17.8.0 Source):**
  - In `/app/app/models/project_type.rb`, the join model introduced for `type_variants` declares `belongs_to :project` and `belongs_to :type` **without `touch: true`**.
  - When `WorkPackageTypes::ProjectsTabController` invokes `Projects::Types::AddService`, `model.project_types.create!(...)` inserts rows into `project_types` **without updating `projects.updated_at` or `types.updated_at`**.
  - API v3 representers (`ProjectRepresenter`, `WorkPackageSchemaRepresenter`) include `API::Caching::CachedRepresenter` (`/app/lib/api/caching/cached_representer.rb`), which caches HAL+JSON payloads in `memcache` keyed by `[represented]` (`projects.updated_at`). Because `projects.updated_at` does not advance, `memcache` serves stale schema/type representations.
- **Operational Fix:** Flush in-container `memcached` over TCP immediately after admin type/project association changes (0s downtime vs. ~80s container restart):
  ```bash
  wsl -d Ubuntu -u root -- docker exec leela-op178-openproject \
    bash -lc "printf 'flush_all\r\n' | timeout 2 bash -c 'cat > /dev/tcp/127.0.0.1/11211'"
  ```

### 2.4 Root Cause of Missing "Active in New Projects" (`is_default`) UI Control in OpenProject 17.8.0
- **Symptom:** `Feature`, `Epic`, `User story`, and `Bug` cannot be marked "Active in new projects" via the OpenProject 17.8.0 admin UI (none of the 7 Type edit tabs has the checkbox, and the Types list column is read-only), nor via `PATCH /api/v3/projects/{id}` with `_links.types`.
- **Root Cause (Verified in 17.8.0 Source):**
  1. **API v3:** `/app/lib/api/v3/projects/project_representer.rb` defines `link :types` strictly as a read-only HAL navigation link; there is no writable `types` property or setter on `ProjectRepresenter`, so `PATCH /api/v3/projects/{id}` ignores `_links.types` and returns `200 OK`.
  2. **UI Regression (Feature-Flag Split):** Not an Enterprise edition gate. During OpenProject 17.8's `type_variants` refactoring, `check_box(name: :is_default)` was removed from `/app/app/forms/work_package_types/details_form.rb` and replaced with `make_default` / `remove_default` menu actions in `/app/app/components/work_package_types/types/type_actions_component.rb`. However, `/app/app/views/work_package_types/types/index.html.erb` only renders `GroupedListComponent` (which includes `TypeActionsComponent`) when `OpenProject::FeatureDecisions.type_variants_active?` is `true` (default `false`). When `false`, it renders the legacy `TableComponent` (`/app/app/components/work_package_types/types/row_component.rb`), which only outputs a static `checked_image model.is_default` icon and omits the action menu.
- **Builder Fix:** `WorkPackageTypes::MakeDefaultService` (`/app/app/services/work_package_types/make_default_service.rb`) is not gated by the feature flag. Run once via `rails runner` to permanently enable all 4 types for future projects:
  ```bash
  wsl -d Ubuntu -u root -- docker exec leela-op178-openproject bundle exec rails runner '
    Type.where(name: ["Feature", "Epic", "User story", "Bug"]).find_each do |t|
      WorkPackageTypes::MakeDefaultService.new(type: t, user: User.system).call
    end
  '
  ```

### 2.5 Resolved `shared-db-net` DNS Alias Collision & Runbook Unification
- **Resolved `openproject` service alias collision on `shared-db-net`:** Previously, both `leela-op178/compose.shared-db.yaml` and `lika-community/compose.wsl.yaml` named their Compose service key `openproject` and attached to `shared-db-net`. Because Docker Compose automatically registers the service key as a DNS alias on every network a container joins, starting both containers registered `openproject` for both IPs on `shared-db-net`. Renaming the service key in [leela-op178/compose.shared-db.yaml](file:///C:/GitDev/leela-op178/compose.shared-db.yaml#L12) from `openproject:` to `leela-openproject:` (while preserving `container_name: leela-op178-openproject`) updated its `shared-db-net` aliases to `["leela-op178-openproject", "leela-openproject"]`, completely eliminating the collision.
- **Runbook unification (`Downloads/RUNBOOK-openproject-17.8-operations.md` + [ki-basis/docs/openproject/RUNBOOK-openproject-17.8-operations.md](file:///C:/GitDev/apexai-os-meta/ki-basis/docs/openproject/RUNBOOK-openproject-17.8-operations.md)):** Merged the `2026-10-03` `Alex-App` working copy's cache backend diagnostics, readiness poll loop, `shared-db-net` pre-check, Known Landmines table (`R4/R5/R11/Status theatre`), and Verification checklist into the canonical repo runbook while preserving the `2026-09-28` repo runbook's `wsl-keepalive.vbs` (§4), `.wslconfig` & Puma/jemalloc bounds (§5), DB backup/restore (§6), and full port table (§7).

