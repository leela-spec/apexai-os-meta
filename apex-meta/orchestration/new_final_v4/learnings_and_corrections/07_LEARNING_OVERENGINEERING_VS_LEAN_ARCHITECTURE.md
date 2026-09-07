# Architectural Learning: Over-Engineering vs. Lean Single-Environment Architecture

**Document Version:** 1.0.0  
**Date:** 2026-09-07  
**Context:** Resolution of excessive Docker Compose micro-compartmentalization and establishment of the unified, low-overhead workstation standard.

---

## 1. Executive Summary: The Over-Engineering Anti-Pattern

During earlier architectural planning, a proposal was generated to strictly isolate every subsystem into its own dedicated Docker Compose project (e.g., separate `ipos-evidence`, `ipos-events`, `ki-basis-private`, `ki-basis-community`), each with independent bridge subnets, separate PostgreSQL databases, separate Valkey queues, and isolated port bands.

While this pattern mimics high-security enterprise microservices deployed across distinct cloud VPCs, applying it to a **single developer/operator workstation** is a textbook **over-engineering anti-pattern**.

### Why Micro-Isolation on a Single Host Fails:
1. **Memory & Resource Multiplication**:
   - Every independent PostgreSQL container allocates its own `shared_buffers`, background WAL writers, checkpointer processes, and autovacuum daemons (~50–100 MB RAM idle per container).
   - Running 3 to 4 distinct PostgreSQL and Valkey engines consumes **1.0 to 1.5 GB of RAM** in background noise.
2. **Network Friction & Broken Service Discovery**:
   - Docker bridge networks are isolated by default. Containers on separate networks cannot resolve each other by container name (e.g., `http://karakeep:3000` fails from Hermes).
   - Inter-service communication is forced to hairpin out to the host loopback (`127.0.0.1` / `host.docker.internal`), adding routing latency, requiring port publishing, and increasing attack surface.
3. **Operational Fatigue**:
   - 4 separate `compose.yaml` files in 4 different folders require multiple `cd` navigation steps, fragmented lifecycle scripts, and confusing backup routines.

---

## 2. The Verified Best-Practice Standard: Lean, Unified & Secure

Official Docker, 12-factor application, and Linux systems architecture establish the **Edge Gateway + Flat Internal Network** pattern as the battle-proven gold standard for local workstations and single-host servers.

```
+---------------------------------------------------------------------------------+
|                        Windows 11 Host / WSL2 Workstation                       |
|                                                                                 |
|  [Host Hermes CLI] --? Native ext4 Workspaces (/root/workspaces/*)             |
|                                                                                 |
|  +------------------------ Unified Docker Environment -----------------------+  |
|  |                                                                           |  |
|  |   [External Traffic / Host Browser]                                       |  |
|  |                ¦                                                          |  |
|  |                ?                                                          |  |
|  |     [Single Edge Gateway (Nginx / Caddy)] ?-- Only Public/Host Exposed    |  |
|  |                ¦                                                          |  |
|  |  --------------+--------------------------------------------------------  |  |
|  |                ¦  Internal Docker Bridge Network (No Host Ports Exposed)  |  |
|  |                ?                                                          |  |
|  |      +-----------------------------------------------------+              |  |
|  |      ¦   Paperless     ¦     Firefly     ¦    Karakeep     ¦              |  |
|  |      ¦  (Documents)    ¦    (Finances)   ¦    (Evidence)   ¦              |  |
|  |      +-----------------------------------------------------+              |  |
|  |               ¦                 ¦                 ¦                       |  |
|  |               +-----------------+-----------------¦                       |  |
|  |               ?                 ?                 ?                       |  |
|  |      +-----------------+               +-----------------+                |  |
|  |      ¦ Container Hermes¦               ¦  Shared Postgres¦                |  |
|  |      ¦ (API Gateway)   ¦               ¦(Multi-DB Engine)¦                |  |
|  |      +-----------------+               +-----------------+                |  |
|  |                                                                           |  |
|  +---------------------------------------------------------------------------+  |
+---------------------------------------------------------------------------------+
```

### Core Architecture Principles:

#### 1. One Unified Docker Environment & Internal Network
All companion services (Paperless, Firefly, Karakeep, Activepieces, Hermes daemon) run within **one unified Docker Compose environment** attached to a single standard internal bridge network.
* **Frictionless Communication**: Hermes communicates directly with Karakeep via `http://karakeep:3000` and Activepieces via `http://activepieces:8080`.
* **Zero Host Port Clutter**: Internal services do not need to bind host ports on `127.0.0.1`.

#### 2. Single Security Layer (Edge Gateway Pattern)
A single reverse proxy (Nginx or Caddy) serves as the security perimeter:
* It is the **only service** that publishes ports to the host (`127.0.0.1`).
* It terminates TLS, enforces authentication headers/tokens, and handles URL routing to backend services.
* Even if an internal service lacks built-in authentication, it remains safe because it is unreachable from the outside network.

#### 3. Consolidated Multi-Database Storage Engine
A single PostgreSQL instance provides multiple isolated logical databases:
* `CREATE DATABASE firefly;`
* `CREATE DATABASE paperless;`
* `CREATE DATABASE activepieces;`
* **Result**: Cuts database RAM usage by **60–75%**, unifies backup into a single `pg_dumpall` command, while preserving strict logical data separation via distinct database users and credentials.

#### 4. Clarity on Repositories vs. Containers (Push-Back & Clarification)
* **Code Repositories are NOT Containers**: The git clones (`apexai-os-meta`, `Investment`, `MasterOfArts`, `acim-secular`) are source code folders residing on the native ext4 filesystem at `/root/workspaces/`.
* **Host Hermes is a Native Process**: The primary Hermes CLI runs directly in Ubuntu WSL2 (`/usr/local/bin/hermes`) where it has instant filesystem access to all four repositories without container virtualization overhead.
* **Container Hermes is a Companion Service**: Inside Docker, `ki-basis-hermes` runs as a headless API service mounting `/root/workspaces` to bridge web/network events into the agent runtime.

---

## 3. Implementation Action Items

1. **Retire Artificial Silos**: Stop creating separate Compose files or network silos for Karakeep and Activepieces.
2. **Unified Service Definition**: Define Karakeep and Activepieces as standard services within the primary Compose environment.
3. **Internal DNS First**: Wire Hermes MCP connections directly to container hostnames (`karakeep:3000`), removing unnecessary loopback proxy hops.
