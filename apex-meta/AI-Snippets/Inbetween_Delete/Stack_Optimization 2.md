## **2. Implementation Plan (Prepared — Not Executed)**

### **Phase 1: Configure `jemalloc` (`MALLOC_CONF`) in `leela-op178`**

1. **Target File:** C:\GitDev\leela-op178\compose.shared-db.yaml
2. **Planned Change:** Add `MALLOC_CONF` alongside `USE_JEMALLOC: "true"` (and keep `MALLOC_ARENA_MAX: "2"` as a fallback for non-preloaded helper binaries):
    
    yaml
    
    environment:
    
      OPENPROJECT_WEB_WORKERS: "0"
    
      OPENPROJECT_BACKGROUND_WORKERS: "1"
    
      OPENPROJECT_WEB__MAX__THREADS: "4"
    
      OPENPROJECT_GOOD__JOB__MAX__THREADS: "2"
    
      MALLOC_ARENA_MAX: "2"
    
      USE_JEMALLOC: "true"
    
      MALLOC_CONF: "narenas:2,dirty_decay_ms:1000,muzzy_decay_ms:0,background_thread:true"
    

### **Phase 2: Address the `91%` Memory Ceiling (Choose Option 2A or 2B)**

- **If Option 2A (Disable `hocuspocus` — saves `~215 MiB`):**
    1. In `C:\GitDev\leela-op178\compose.shared-db.yaml`, set:
        
        yaml
        
        OPENPROJECT_COLLABORATIVE__EDITING__HOCUSPOCUS__URL: ""
        
    2. Create a minimal read-only script `C:\GitDev\leela-op178\disable-hocuspocus.sh` (`#!/bin/bash` →\rightarrow→ `exec sleep infinity` or `supervisorctl stop hocuspocus`) or mount `/app/docker/prod/hocuspocus` so `supervisord` does not spawn the `215 MiB` `npm`/`tsx`/`esbuild` tree while keeping `supervisord` happy (`exit 0` / no restart loop).
    3. Keep `mem_limit: 1536M` (usage drops to `~1.05–1.14 GiB`, leaving `~400 MiB` free headroom).
- **If Option 2B (Keep `hocuspocus` — raise ceiling for safety):**
    1. In `C:\GitDev\leela-op178\compose.shared-db.yaml`, change:
        
        yaml
        
        mem_limit: 1792M
        

### **Phase 3: Recreate & Verify Live Telemetry**

1. Recreate `leela-op178-openproject` via `docker compose -f compose.shared-db.yaml --env-file .env.shared-db -p leela-op178 up -d`.
2. **Verify `jemalloc` active parameters inside the running container:**
    - Run `docker exec -e LD_PRELOAD=libjemalloc.so.2 leela-op178-openproject ruby -e ...` with `stats_print` to confirm `opt.narenas: 2`, `opt.dirty_decay_ms: 1000`, `opt.muzzy_decay_ms: 0`, and `opt.background_thread: true`.
3. **Verify memory & health:**
    - Measure `docker stats --no-stream` and `/proc/<pid>/smaps_rollup` (`Pss`).
    - Run Windows `curl.exe` + `node opCall.js doctor --project 3`.

### **Phase 4: Sync Documentation & Health Oracle (`Zero Drift`)**

1. Update FINDINGS-openproject-memory-and-178-inefficiencies-2026-10-08.md, RUNBOOK-openproject-17.8-operations.md, and INFRASTRUCTURE.md `§4.3` with `MALLOC_CONF`, the true kernel `Pss` breakdown, and the final memory numbers.
2. Update INCIDENT-cache-staleness-work-package-visibility.md to clearly state that the upstream OP 17.8.0 bug (`ProjectType` missing `touch: true`) remains in the image and requires the TCP `memcached` flush after any future project-type change.
3. Update infra-health-test.sh check `7f` to verify `MALLOC_CONF` (and `mem_limit` if changed) and confirm `PASS=31 FAIL=0 WARN=0`.

---

### **Decision Needed Before Execution**

For **Phase 2**, which option do you prefer?

1. **Option 2A:** Disable `hocuspocus` (saves `~215 MiB` RAM, drops container to `~1.1 GiB / 1.5 GiB`), **or**
2. **Option 2B:** Keep `hocuspocus` running and raise `mem_limit` from `1536M` to `1792M` for spike headroom?

for private 2a for community 2b

Both **Option 2A** (for Private OpenProject `leela-op178-openproject`) and **Option 2B** (for Community OpenProject `community-openproject`), along with the `jemalloc` `MALLOC_CONF` tuning and documentation/test updates, have been applied and verified.

---

### **1. What Was Executed**

1. **Private OpenProject 17.8 (`leela-op178-openproject` — Option 2A):**
    
    - Updated C:\GitDev\leela-op178\compose.shared-db.yaml:
        - Added `MALLOC_CONF: "narenas:2,dirty_decay_ms:1000,muzzy_decay_ms:0,background_thread:true"` (reduced `jemalloc 5.3.0` from `33` arenas down to `2` configurable arenas + enabled background dirty-page purging).
        - Set `OPENPROJECT_COLLABORATIVE__EDITING__HOCUSPOCUS__URL: ""` and mounted C:\GitDev\leela-op178\disable-hocuspocus.sh over `/app/docker/prod/hocuspocus:ro` so `supervisord` sleeps instead of spawning the `215 MiB` Node/tsx/esbuild process tree.
    - Recreated `leela-op178-openproject` (`23e63da22393`).
2. **Community OpenProject 14.x (`community-openproject` — Option 2B):**
    
    - Updated C:\GitDev\lika-community\compose.wsl.yaml:
        - Kept all Community features intact, added `USE_JEMALLOC: "true"` and `MALLOC_CONF: "narenas:2,dirty_decay_ms:1000,muzzy_decay_ms:0,background_thread:true"`, and raised `mem_limit` from `1200M` to **`1792M` (`1.75 GiB`)** for `~650 MiB` of spike headroom when woken on-demand.
    - Applied the updated container spec while returning `community-openproject` to its default `exited` (`restart: "no"`, `0 MiB`) state.
3. **Documentation & Health Oracle Sync:**
    
    - Updated INCIDENT-cache-staleness-work-package-visibility.md and FUTURE-DEVELOPMENT-type-defaults-for-new-projects.md to `status: mitigated` (clarifying that the upstream OP 17.8.0 defects remain in the image and require the TCP `memcached` flush after future project-type changes).
    - Updated INFRASTRUCTURE.md, RUNBOOK-openproject-17.8-operations.md, FINDINGS-openproject-memory-and-178-inefficiencies-2026-10-08.md, and infra-health-test.sh.

---

### **2. Verified Live Results (`leela-op178-openproject`)**

|Metric|Before (with `hocuspocus` & default `jemalloc`)|After (Option 2A + `MALLOC_CONF`)|Improvement|
|---|---|---|---|
|**Puma (`web`) Kernel `Pss`** (`/proc/pid/smaps_rollup`)|`707.6 MiB`|**`589.9 MiB`** (`604,042 kB`)|**`-117.7 MiB`**|
|**GoodJob (`worker`) Kernel `Pss`**|`599.6 MiB`|**`552.7 MiB`** (`565,916 kB`)|**`-46.9 MiB`**|
|**Hocuspocus Kernel `Pss`**|`214.8 MiB` (`33` threads)|**`0.94 MiB`** (`963 kB`, `1` PID)|**`-213.9 MiB`** (`-32` PIDs)|
|**Total Non-Reclaimable Heap (`cgroup anon`)**|`~1.36 GiB` (`~140 MiB` headroom)|**`1.126 GiB`** (`1,209,499,648 B`)|**`~380 MiB` spike headroom** under `1536M` limit|
|**Container Processes / Threads (`PIDs`)**|`136` (down from `145` baseline)|**`103`**|**`-33` PIDs** (`-42` total from baseline)|
|**Health Oracle (`infra-health-test.sh`)**|—|**`PASS=31 FAIL=0 WARN=0` (`GREEN`)**|Windows & WSL HTTP `200`, Skill `doctor` `pass`|