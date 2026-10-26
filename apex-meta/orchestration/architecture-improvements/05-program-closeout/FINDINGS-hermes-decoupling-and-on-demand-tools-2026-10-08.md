---
type: Findings
title: Architectural Learning — Decoupling Agent Gateways from Optional Peripheral HTTP Tools
description: >
  Architectural learning on why Hermes was wrongly coupled to Paperless, Firefly, and Nginx via
  depends_on and restart: unless-stopped, and how decoupling them to on-demand sleep (restart: "no")
  with wake-tools.sh / sleep-tools.sh establishes a lean 24/7 baseline.
tags: [findings, learnings, hermes, paperless, firefly, nginx, docker, lifecycle, on-demand]
created: 2026-10-08
status: current
canonical_current_state: ki-basis/docs/INFRASTRUCTURE.md
---

## Architectural Learning: Decoupling Agent Gateways from Optional Peripheral HTTP Tools

### 1. What Was Wrongly Defined in the Architecture
In [compose.shared-db.yaml](file:///C:/GitDev/apexai-os-meta/ki-basis/compose.shared-db.yaml), the `hermes` service was configured with a hard orchestration dependency (`depends_on: [firefly, paperless, nginx]`), and the peripheral application containers (`paperless`, `firefly`, and `nginx`) were configured with `restart: unless-stopped`.

### 2. Why It Was Wrong
- **Confusing Runtime Tool Reachability with Boot-Time Infrastructure Dependency:** `depends_on` in Docker Compose is meant for hard boot-time prerequisites (such as a database or cache that a service cannot start without). However, `hermes` is an AI agent gateway that interacts with Paperless-ngx (`PAPERLESS_API_URL`) and Firefly III (`FIREFLY_API_URL`) purely as optional, on-demand HTTP tools. Hermes does not require them to boot, stay healthy, or handle unrelated tasks.
- **Forced Resource Wake-Up:** Because of `depends_on`, starting or updating `hermes` via `docker compose up -d hermes` forced Docker to start `paperless` (~710 MB RAM), `firefly` (~122 MB RAM), and `nginx` (~10 MB RAM) every time.
- **Always-On Idle Memory Drain:** Setting `restart: unless-stopped` on infrequently used peripheral applications treated batch/on-demand document and finance tools as 24/7 core infrastructure, permanently consuming ~840 MB of WSL2 memory even when no document filing or bookkeeping was taking place.

### 3. What Was Changed
1. **Removed `depends_on` from `hermes`** in [compose.shared-db.yaml](file:///C:/GitDev/apexai-os-meta/ki-basis/compose.shared-db.yaml#L138-L174) so Compose no longer starts `firefly`, `paperless`, or `nginx` when starting or recreating `hermes`.
2. **Changed `restart: unless-stopped` to `restart: "no"`** on `firefly` ([line 58](file:///C:/GitDev/apexai-os-meta/ki-basis/compose.shared-db.yaml#L58)), `paperless` ([line 83](file:///C:/GitDev/apexai-os-meta/ki-basis/compose.shared-db.yaml#L83)), and `nginx` ([line 121](file:///C:/GitDev/apexai-os-meta/ki-basis/compose.shared-db.yaml#L121)), while keeping `restart: unless-stopped` on core services (`hermes` and `valkey`).
3. **Stopped the peripheral containers immediately** (`ki-basis-paperless`, `ki-basis-firefly`, `ki-basis-nginx`) and dropped the Linux page cache while leaving all persistent volumes (`paperless_data`, `paperless_media`, `firefly_upload`) and `shared-db-net` untouched.
4. **Added explicit lifecycle scripts** ([wake-tools.sh](file:///C:/GitDev/apexai-os-meta/ki-basis/scripts/wake-tools.sh) and [sleep-tools.sh](file:///C:/GitDev/apexai-os-meta/ki-basis/scripts/sleep-tools.sh)) to start and stop the peripheral tools on demand.

### 4. Why These Changes Were Made
- **Enforce a Lean 24/7 Baseline:** Only core, continuously needed services (`ki-basis-hermes`, `leela-op178-openproject`, `ki-basis-shared-postgres`, and `ki-basis-valkey`) run 24/7.
- **Graceful Degradation by Design:** Because HTTP tool integrations are loosely coupled over REST APIs, keeping peripheral containers stopped has zero impact on Hermes's stability—only an explicit tool call to Paperless or Firefly while they are sleeping will return a connection error.
- **Explicit On-Demand Lifecycle:** Moving peripheral tools to `restart: "no"` with explicit `wake-tools.sh` / `sleep-tools.sh` scripts reclaims ~840 MB of RAM during normal operations while allowing one-command activation whenever document or finance workflows are needed.
