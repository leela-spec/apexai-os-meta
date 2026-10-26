### **1. Community OpenProject (`community-openproject`): `OPENPROJECT_WEB_WORKERS=0` (Puma Single-Mode)**

- **Files updated:**
    - C:\GitDev\lika-community\compose.wsl.yaml (`OPENPROJECT_WEB_WORKERS: ${OPENPROJECT_WEB_WORKERS:-0}`)
    - C:\GitDev\lika-community.env.wsl (`OPENPROJECT_WEB_WORKERS=0`)
    - C:\GitDev\lika-community.env & C:\GitDev\lika-community.env.example (`OPENPROJECT_WEB_WORKERS=0`)
    - INFRASTRUCTURE.md & FINDINGS-openproject-memory-and-178-inefficiencies-2026-10-08.md
- **Live container verification:** Recreated `community-openproject` (`docker compose -p community --env-file .env.wsl -f compose.wsl.yaml up -d openproject && docker stop community-openproject`) and confirmed via `docker inspect` that `state=exited`, `restart=no`, `mem_limit=1792M` (`1879048192`), `OPENPROJECT_WEB_WORKERS=0`, `USE_JEMALLOC=true`, and `MALLOC_CONF=narenas:2,dirty_decay_ms:1000,muzzy_decay_ms:0,background_thread:true`.

### **2. Automated Hocuspocus & Community `WEB_WORKERS=0` Guard in infra-health-test.sh**

- **Check 7f** now asserts:
    1. `leela-op178-openproject` has `mem_limit=1536M` (`1610612736`), `OPENPROJECT_WEB_WORKERS=0`, and `USE_JEMALLOC=true`.
    2. `community-openproject` has `mem_limit=1792M` (`1879048192`) and `OPENPROJECT_WEB_WORKERS=0`.
    3. Live `/proc/<puma_pid>/environ` and `ps -T` inside `leela-op178-openproject` have `LD_PRELOAD=libjemalloc.so.2`, `MALLOC_CONF=narenas:2,dirty_decay_ms:1000,muzzy_decay_ms:0,background_thread:true`, and active `jemalloc_bg_thd` OS threads.
    4. `pgrep -f "node.*hocuspocus"` inside `leela-op178-openproject` is empty (`[ -z "$hp_node_running" ]`), preventing any future OpenProject image upgrade from silently re-enabling the `215 MiB` Hocuspocus server.
- **Live test suite result:**
    
    text
    
    [PASS] OpenProject bounds, live Puma /proc environ & hocuspocus-disabled guard active (priv 1536M WEB_WORKERS=0 jemalloc_bg_thd no-hocuspocus; comm 1792M WEB_WORKERS=0)
    
    [PASS] leela-op178-openproject shared-db-net aliases isolated (leela-op178-openproject leela-openproject )
    
    ================ RESULT: PASS=31  FAIL=0  WARN=0 ================
    
    OVERALL: GREEN (no failures)