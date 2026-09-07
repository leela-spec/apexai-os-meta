# Specification Report: ki-basis Dual-Instance Separation Architecture (R1, R2, R3)

**Author:** spec_miner_survey_1  
**Target:** ki-basis Infrastructure (Private Entrepreneurship vs. Community Operations)  
**Date:** 2026-09-07  
**Working Directory:** `C:\GitDev\apexai-os-meta`  
**Authoritative Sources:** `C:\GitDev\apexai-os-meta\.agents\ORIGINAL_REQUEST.md`, `C:\GitDev\apexai-os-meta\.agents\spec_miner_survey_1\DISPATCH.md`, `ki-basis/compose.yaml`, `ki-basis/STACK_ARCHITECTURE.md`, `ki-basis/AGENT-OPERATING-CONTEXT.md`, `ki-basis/CURRENT-STATE.md`, `ki-basis/SECURITY-GUIDANCE.md`, `apex-meta/Alpine/Iteration2/Performance_Problem.md`, `apex-meta/Alpine/research/Docker-Desktop-Windows.md`.

---

## 1. Executive Summary & Specification Scope

The `ki-basis` platform (Lika OS infrastructure) is currently deployed as a single, multi-service Docker Compose stack (`ki-basis`) comprising seven core services: PostgreSQL (with `pgvector`), Valkey (Redis-compatible broker), Firefly III, Paperless-ngx, OpenProject, Nginx edge proxy, and Hermes AI Agent.

The objective of this specification is to architect, benchmark, and evaluate a comprehensive **dual-instance separation** across two distinct institutional domains:
1. **Private Entrepreneurship (`ki-basis-private`)**: Commercial consulting, private ventures, proprietary invoices, private banking, and confidential projects.
2. **Community Operations (`ki-basis-community`)**: Non-profit operations (Safer Space e.V., Equinox 2026 event), Pretix ticketing, volunteer expense intake, community task boards, and statutory German tax compliance (4-sphere EÜR & ELSTER GemEUR).

This document formalizes the extraction of all functional requirements, non-functional requirements, architectural constraints, quantitative performance thresholds, acceptance criteria, and operational runbooks necessary to resolve observed WSL2/9P filesystem bottlenecks, eliminate OpenProject crash loops, prevent port collisions, and enforce airtight data and network isolation.

---

## 2. Authoritative Specification Sources

| Source Path | Authority Scope | Key Evidence Extracted |
|:---|:---|:---|
| `.agents/ORIGINAL_REQUEST.md` | Primary User Mandate | R1 (WSL2/9P bottleneck, 350% CPU, OpenProject exit status 1), R2 (dual namespaces, isolated networks, port bands, segregated state), R3 (Strategy A vs B comparison, `localhostForwarding`), Acceptance Criteria (idle CPU <5%, ext4-only, zero collisions). |
| `.agents/spec_miner_survey_1/DISPATCH.md` | Orchestrator Assignment | Specific focus areas: detailed breakdown of R1, R2, R3, validation metrics, structured tables for discovered features and edge cases. |
| `ki-basis/compose.yaml` | Runtime Truth (Single Stack) | 7 container definitions, volume naming conventions (`ki-basis-*`), internal network bridge (`ki-basis-net`), environment variable schemas, health checks, ports. |
| `ki-basis/.env.example` & `.env` | Configuration Schema | Port mappings (8010, 8082, 8084, 8086, 8642, 9119), DB usernames/passwords, API tokens, secret keys. |
| `ki-basis/STACK_ARCHITECTURE.md` | System Architecture & Data Flow | 3-tier autonomy model (Hermes triage -> Local CLI execution -> Human governance), 7 service roles, Pretix/Bank/Telegram intake pipelines. |
| `ki-basis/AGENT-OPERATING-CONTEXT.md` | Operational Doctrine & Boundaries | Loopback-only host binding, no Docker socket in Hermes, internal-only DBs, on-demand lifecycle, performance policy. |
| `ki-basis/SECURITY-GUIDANCE.md` | Security & Privacy Architecture | Frontline intake flexibility vs trusted execution enclave; zero DB write access from Hermes. |
| `apex-meta/Alpine/Iteration2/Performance_Problem.md` | Empirical Performance Telemetry | Breakdown of 1.4 GB container footprint vs host bottlenecks: Docker Desktop Electron/GPU overhead, DWM starvation (756 MB), Memory Compression (2.0 GB), Puma clustering. |
| `apex-meta/Alpine/research/Docker-Desktop-Windows.md` | Runtime Research & Optimization | Headless daemon operation, Puma worker reduction (`OPENPROJECT_WEB_WORKERS=1`), Compose resource limits (`mem_limit`), `.wslconfig` memory capping. |
| `ki-basis/scripts/backup-stack.sh` | Backup & State Persistence | DB dumps (`pg_dumpall`, `pg_dump -Fc`), volume archiving via helper containers, excluded secrets. |
| `ki-basis/scripts/verify-stack.sh` | Quality & Isolation Gates | Port exposure proofs, Docker socket absence proofs, negative token rejection proofs, loopback curl proofs. |

---

## 3. Detailed Requirements Breakdown

### Requirement 1 (R1): Performance Diagnosis & Storage Architecture

#### 1.1 Root Cause Analysis of Observed Bottlenecks
1. **The 9P Filesystem Protocol Latency on `/mnt/c`**:
   - In WSL2, accessing the Windows NTFS host filesystem via `/mnt/c/` routes through the Plan 9 (9P) network protocol / VirtIO-9P driver layer.
   - Relational databases (PostgreSQL write-ahead logging) and I/O-intensive web frameworks (Ruby on Rails assets in OpenProject, Paperless OCR processing, Python virtual environments in Hermes) execute high volumes of synchronous metadata calls (`stat`, `fstat`), file locks (`flock`, `fcntl`), and `fsync` flushes.
   - Over 9P, each I/O operation incurs cross-OS virtualization context switches, causing I/O latency to degrade by 10x–100x compared to native Linux block devices.
   - This latency causes Linux kernel worker threads to accumulate in unkillable uninterruptible sleep state (**D-state locks**), stalling Git operations, saturating vCPU scheduling, and producing the observed **350% runaway CPU usage**.

2. **OpenProject Crash Loop (`exit status 1`) Diagnosis**:
   - **POSIX File Locking Failure**: OpenProject utilizes Ruby on Rails with Puma clustering. On boot, Rails and Puma require atomic POSIX byte-range file locks for PID creation (`tmp/pids/puma.pid`) and cache synchronization. The 9P driver provides incomplete or erratic POSIX advisory locking, causing Puma to throw fatal startup exceptions (`Errno::ENOLCK` or `Errno::EOPNOTSUPP`) and immediately exit with status 1.
   - **File Permission & UID/GID Mismatch**: OpenProject executes as non-root user `openproject` (UID 1000). On `/mnt/c` 9P bind mounts, file permissions default to root or Windows ACL masks (777/755), and dynamic `chown` operations fail. When the container entrypoint attempts to configure `/var/openproject/assets`, permissions are denied, triggering `exit status 1`.
   - **Database Initialization & Startup Race**: OpenProject enforces a default database connection timeout (`PG_STARTUP_WAIT_TIME=30`). When PostgreSQL data is stored on a 9P mount, PostgreSQL cluster startup and WAL replay exceed 30 seconds. OpenProject's entrypoint migration script (`rails db:migrate`) times out and terminates with code 1.
   - **Puma Cluster Memory & vCPU Spikes**: By default, OpenProject spawns multiple cluster workers (`Puma workers = 2-4`) and background worker threads (`rake jobs:work`). When scheduled inside an unconstrained VM with 9P latency, thread contention spikes memory beyond allocated thresholds, prompting internal process crashes or OOM aborts.

3. **Host Windowing & Desktop Drag (DWM / Memory Compression)**:
   - Docker Desktop's default Electron GUI launches 5 separate host processes with hardware GPU acceleration hooks, starving the Windows Desktop Window Manager (`dwm.exe` ballooning to 750+ MB) and causing mouse stutter and window lag.
   - Uncapped dynamic VM allocations trigger aggressive Windows NT kernel **Memory Compression** (compressing 2.0+ GB of host RAM), introducing 2–4 second synchronous decompress freezes during desktop window switching.

#### 1.2 Storage Architecture Specification
- **Mandatory Native ext4 Storage**:
  - All database data (`postgres_data`), cache data (`valkey_data`), application media/assets (`paperless_data`, `paperless_media`, `openproject_assets`), and agent workspaces (`hermes_workspaces`, `hermes_data`) **MUST** reside on native Linux ext4 filesystems.
  - In Docker Desktop: Backed exclusively by Docker named volumes stored in the virtual disk (`ext4.vhdx`).
  - In native WSL2: Backed by named volumes in `/var/lib/docker/volumes/` or ext4 directory paths inside the distro root (`/root/workspaces/...`), strictly forbidding any bind mounts from `/mnt/c/` or `\\wsl$\` for persistence.
- **Read-Only Host Bind Mounts Restricted to Configuration**:
  - The only permitted bind mounts from the repository workspace are static, read-only configuration directories (e.g. `./docker/postgres/init:/docker-entrypoint-initdb.d:ro` and `./docker/nginx:/etc/nginx/conf.d:ro`).

#### 1.3 Headless Container Runtime Parameters
- **OpenProject Single-Worker Configuration**:
  - Set `OPENPROJECT_WEB_WORKERS=1` to eliminate multi-process Puma cluster overhead, reducing OpenProject base memory from ~900 MB to ~400–450 MB.
  - Set `OPENPROJECT_BACKGROUND_WORKERS=1` to serialize background jobs without scheduling thrashing.
  - Increase `PG_STARTUP_WAIT_TIME=60` to provide robust startup headroom during simultaneous multi-stack boots.
- **Explicit Resource Constraints (Deploy Limits per Service)**:
  - OpenProject: `limits.memory: 1.5G`, `reservations.memory: 512M`.
  - Paperless-ngx: `limits.memory: 768M`, `reservations.memory: 256M`.
  - Hermes Agent: `limits.memory: 512M`, `reservations.memory: 128M`.
  - PostgreSQL: `limits.memory: 512M`, `reservations.memory: 128M`.
  - Valkey: `limits.memory: 256M`, `reservations.memory: 64M`.
  - Firefly III: `limits.memory: 256M`, `reservations.memory: 64M`.
  - Nginx: `limits.memory: 64M`, `reservations.memory: 16M`.
- **Headless Host Daemon Operation**:
  - Docker Desktop GUI (`Docker Desktop.exe`) must not be kept open during headless CLI operations; only the background daemon services (`com.docker.backend.exe` / dockerd) remain active.
  - Automatic desktop GUI launch on Windows sign-in must be disabled.

---

### Requirement 2 (R2): Dual-Instance Isolation Architecture

#### 2.1 Project Namespaces & Configuration Topologies
- **Dual Compose Project Namespaces**:
  - Private Instance: `ki-basis-private` (`docker compose -p ki-basis-private ...`)
  - Community Instance: `ki-basis-community` (`docker compose -p ki-basis-community ...`)
- **Container Naming Conventions**:
  - Private containers: `ki-basis-private-postgres`, `ki-basis-private-valkey`, `ki-basis-private-firefly`, `ki-basis-private-paperless`, `ki-basis-private-openproject`, `ki-basis-private-nginx`, `ki-basis-private-hermes`.
  - Community containers: `ki-basis-community-postgres`, `ki-basis-community-valkey`, `ki-basis-community-firefly`, `ki-basis-community-paperless`, `ki-basis-community-openproject`, `ki-basis-community-nginx`, `ki-basis-community-hermes`.
- **Configuration Files**:
  - Dedicated configuration files: `.env.private` and `.env.community` (derived from an updated `.env.example` template supporting namespace prefixes and distinct port bands).

#### 2.2 Network Isolation & Inter-Stack Routing Prevention
- **Distinct Docker Bridge Networks**:
  - Private Stack Network: `ki-basis-private-net` (e.g. Subnet `172.28.0.0/16`)
  - Community Stack Network: `ki-basis-community-net` (e.g. Subnet `172.29.0.0/16`)
- **Zero Inter-Stack Routing**:
  - No container from `ki-basis-private` shall be attached to `ki-basis-community-net`, and vice-versa.
  - Containers use Docker internal DNS names (e.g., `postgres`, `valkey`, `firefly`, `paperless`, `openproject`), which resolve strictly within the local bridge network. Cross-stack DNS lookups (e.g. from `ki-basis-private-hermes` to `ki-basis-community-paperless`) must fail to resolve.
  - Negative firewall/bridge verification: Inter-stack TCP/UDP packet transmission between containers across the two subnets is prohibited.

#### 2.3 Non-Overlapping Port Assignment Schema
All host ports must be bound explicitly to the IPv4 loopback address (`127.0.0.1`). Binding to wildcard `0.0.0.0` is strictly forbidden.

| Service | Internal Port | Private Host Port Band (8080–8089, 864x, 911x) | Community Host Port Band (9080–9089, 964x, 921x) | Exposure Boundary |
|:---|:---|:---|:---|:---|
| **PostgreSQL** | 5432/tcp | *None (Unpublished)* | *None (Unpublished)* | Internal bridge network only |
| **Valkey** | 6379/tcp | *None (Unpublished)* | *None (Unpublished)* | Internal bridge network only |
| **Paperless-ngx** | 8000/tcp | `127.0.0.1:8010` (or `8080`) | `127.0.0.1:9010` (or `9080`) | Host Loopback Only |
| **OpenProject** | 80/tcp | `127.0.0.1:8082` | `127.0.0.1:9082` | Host Loopback Only |
| **Nginx Edge Proxy**| 80/tcp | `127.0.0.1:8084` | `127.0.0.1:9084` | Host Loopback Only |
| **Firefly III** | 8080/tcp | `127.0.0.1:8086` | `127.0.0.1:9086` | Host Loopback Only |
| **Hermes Gateway** | 8642/tcp | `127.0.0.1:8642` | `127.0.0.1:9642` | Host Loopback Only |
| **Hermes Dashboard**| 9119/tcp | `127.0.0.1:9119` | `127.0.0.1:9219` | Host Loopback Only |

#### 2.4 Complete Segregation of Persistent State & Credentials
- **Relational Databases (PostgreSQL)**:
  - Completely separate database container instances.
  - Private volume: `ki-basis-private-postgres-data`.
  - Community volume: `ki-basis-community-postgres-data`.
  - Zero shared tables, schemas, or database superusers. Separate initialization scripts.
- **Message Broker & Queue (Valkey)**:
  - Completely separate Valkey container instances.
  - Private volume: `ki-basis-private-valkey-data`.
  - Community volume: `ki-basis-community-valkey-data`.
  - Zero shared Celery/Redis task queues or caching keys.
- **Document Vault (Paperless-ngx)**:
  - Private named volumes: `ki-basis-private-paperless-data`, `-media`, `-export`, `-consume`.
  - Community named volumes: `ki-basis-community-paperless-data`, `-media`, `-export`, `-consume`.
  - Independent secret keys (`PAPERLESS_SECRET_KEY`), independent admin accounts, and segregated document archives.
- **Financial Accounting (Firefly III)**:
  - Private volume: `ki-basis-private-firefly-upload`.
  - Community volume: `ki-basis-community-firefly-upload`.
  - Independent application encryption keys (`APP_KEY`).
  - Private stack holds commercial bank accounts; Community stack holds non-profit GLS Bank accounts and 4-sphere tax configurations.
- **Project Management (OpenProject)**:
  - Private volume: `ki-basis-private-openproject-assets`.
  - Community volume: `ki-basis-community-openproject-assets`.
  - Independent `OPENPROJECT_SECRET_KEY_BASE`.
  - Zero cross-stack work packages or user visibility.
- **Hermes AI Operating Surface**:
  - Private volumes: `ki-basis-private-hermes-data`, `ki-basis-private-hermes-workspaces`.
  - Community volumes: `ki-basis-community-hermes-data`, `ki-basis-community-hermes-workspaces`.
  - Distinct `HERMES_API_SERVER_KEY` values.
  - Distinct `TELEGRAM_BOT_TOKEN` credentials (preventing Telegram API 409 conflict errors).

---

### Requirement 3 (R3): Multi-Engine vs. Multi-Project Strategy Evaluation

#### 3.1 Architectural Definitions
- **Strategy A: Dual Compose Projects on a Single Docker Engine**:
  - Both `ki-basis-private` and `ki-basis-community` run concurrently on one Docker Engine (either native WSL2 dockerd or Docker Desktop).
  - Isolation is achieved via Compose project names (`-p`), segregated named volumes, isolated bridge networks (`ki-basis-private-net` and `ki-basis-community-net`), and segregated port bands (808x vs 908x).
- **Strategy B: Dual Daemon Split Across WSL2 and Docker Desktop**:
  - `ki-basis-private` runs in Ubuntu WSL2 on a native `dockerd` daemon backed by ext4.
  - `ki-basis-community` runs in Windows Docker Desktop (Alpine LinuxKit or Docker Desktop WSL2 VM).
  - Controlled via distinct Docker CLI contexts (e.g. `docker --context wsl-native` vs `docker --context default`).

#### 3.2 Deep Evaluation Matrix

| Evaluation Dimension | Strategy A (Single Engine / Dual Projects) | Strategy B (Dual Daemon Split) | Evaluation & Tradeoff Assessment |
|:---|:---|:---|:---|
| **Architectural Complexity** | **Low**. Single Docker daemon lifecycle, unified CLI commands (`docker compose -p ...`), standard Compose constructs. | **High**. Requires managing two independent Docker daemons, systemd service in Ubuntu, two context configs, and dual daemon update schedules. | **Strategy A is substantially simpler** to maintain and less prone to configuration drift. |
| **WSL2 `localhostForwarding` Risk** | **Zero Risk**. Because all ports run on the same engine, Docker enforces standard port allocation and prevents duplicate bindings cleanly. | **Severe Conflict Risk**. WSL2's `localhostForwarding=true` forwards all ports bound in WSL2 to Windows `127.0.0.1`. If both daemons bind any overlapping port, `WSAEADDRINUSE` occurs or Windows routes traffic erratically. If `localhostForwarding` is disabled, accessing WSL2 private stack requires dynamic `eth0` IP which breaks static configs and bookmarks. | **Strategy A eliminates `localhostForwarding` collision risks**. |
| **Host Resource Footprint** | **Lean (~2.8–3.2 GB combined)**. One VM/daemon overhead. Shared container runtime memory; CPU idle is consolidated. | **Heavy (~4.5–6.0 GB combined)**. Two Linux VM kernels running concurrently (`vmmem` for WSL2 + Docker Desktop VM), two background daemon daemons, duplicate containerd layers. High probability of triggering Windows Memory Compression thrashing. | **Strategy A provides superior laptop responsiveness** on a 32 GB machine. |
| **Security & Process Isolation** | **High**. Docker bridge network namespace isolation, separate mount namespaces, and unexposed DB ports prevent cross-talk. | **Air-gap / Hypervisor level**. Kernel-level hypervisor separation between the two Docker engines. | Strategy B provides stronger theoretical process isolation, but Strategy A is fully adequate for non-adversarial dual-entity separation. |
| **Operational & Backup Workflows** | **Unified & Deterministic**. Scripts can loop over projects or target one project cleanly using `-p`. Single inspection command (`docker stats`). | **Fragmented**. Backup scripts must execute partially inside WSL2 bash and partially on Windows PowerShell/CMD, complicating automation. | **Strategy A streamlines daily maintenance** and automated backups. |

#### 3.3 Strategy Conclusion & Recommendation
**Strategy A (Dual Compose Projects on Single Engine)** is decisively recommended as the primary architecture. It completely satisfies the user's isolation criteria while avoiding the severe operational failure modes, `localhostForwarding` conflicts, and double-VM memory thrashing inherent in Strategy B.

---

## 4. Acceptance Criteria & Validation Metrics

### 4.1 Quantitative Performance & Stability Metrics
1. **Steady-State Idle CPU Threshold**:
   - Total steady-state CPU utilization across all 14 containers (7 Private + 7 Community) must be **< 5% at idle** on the host.
   - Measured via `docker stats --no-stream` 3 minutes post-startup.
2. **Memory Quotas**:
   - OpenProject single-worker footprint must remain **< 500 MB** at idle per instance, with hard ceiling capped at **1.5 GB**.
   - Total container memory for both stacks combined must remain **< 3.2 GB**.
3. **Filesystem Integrity**:
   - **0%** 9P filesystem mounts for data or databases (`/mnt/c` must not appear in any container volume mount).
   - **100%** of relational databases, queues, and document vaults must reside on native ext4 named Docker volumes.
4. **Healthcheck & Startup Reliability**:
   - OpenProject must achieve `healthy` status on `/health_checks/default` with **0 restart loops** and **zero `exit status 1` errors**.
   - Hermes, Paperless, Firefly, and Nginx must reach `healthy` status within standard startup timeouts (< 60s).

### 4.2 Isolation & Security Verification
1. **Concurrent Execution**:
   - Both `ki-basis-private` and `ki-basis-community` must start and run concurrently with **zero port binding collisions** (`0 error response from daemon: port is already allocated`).
2. **Zero Shared Storage**:
   - Verification command: `docker volume ls` must show 18 distinct named volumes (9 per stack).
   - Inspection proof: No volume name from `ki-basis-private` is mounted into any `ki-basis-community` service, and vice-versa.
3. **Zero Cross-Stack Network Routing & DNS Leakage**:
   - Negative connection proof: Running a TCP probe from `ki-basis-private-hermes` to `http://community-paperless:8000` or `http://172.29.0.x:8000` must result in DNS resolution failure or network timeout.
4. **Host Binding Restraint**:
   - Verification command: `docker port` must show that PostgreSQL (5432) and Valkey (6379) publish zero ports to the Windows host on both stacks.
   - All published web ports must bind strictly to `127.0.0.1`, never `0.0.0.0`.
5. **Telegram Bot Conflict Prevention**:
   - Private and Community Hermes configurations must specify distinct Telegram bot tokens or have community Telegram bot enabled while private is loopback-API only, avoiding API 409 conflict errors.

---

## 5. Discovered Features

| # | Category | Feature | Description | Inputs | Outputs | Error Behavior | Discovered Via |
|---|---|---|---|---|---|---|---|
| 1 | Storage & Runtime | Native ext4 Volume Mounts | Use Docker named volumes backed by ext4 virtual disk instead of 9P mounts on `/mnt/c`. | Named volume declarations in Compose file. | High-speed POSIX I/O, microsecond fsync flushes. | If host `/mnt/c` path is bound: D-state locks, 350% CPU, I/O timeouts. | R1 Spec & `compose.yaml` |
| 2 | Storage & Runtime | OpenProject Single-Worker Cap | Limit Rails Puma cluster to a single web worker and single background worker. | Env vars: `OPENPROJECT_WEB_WORKERS=1`, `OPENPROJECT_BACKGROUND_WORKERS=1`. | Puma runs single process; memory drops from ~900MB to ~450MB. | If omitted: Puma spawns 2-4 cluster workers, triggering memory thrashing and vCPU spikes. | `Performance_Problem.md` & `research/Docker-Desktop-Windows.md` |
| 3 | Storage & Runtime | Extended Database Startup Timeout | Increase OpenProject database connection wait time from 30s to 60s. | Env var: `PG_STARTUP_WAIT_TIME=60`. | OpenProject entrypoint waits up to 60s for Postgres to report healthy. | If set to 30s or lower during parallel dual-stack boot: timeout causes fatal `exit status 1`. | R1 Spec & `compose.yaml` |
| 4 | Storage & Runtime | Compose Resource Limits | Enforce hard memory limits (`limits.memory`) and reservations (`reservations.memory`) on all services. | `deploy.resources.limits` block per service in Compose. | Docker Engine enforces memory ceilings; prevents VM ballooning. | If service exceeds limit: container receives SIGKILL/OOM, preventing host freeze. | `Docker-Desktop-Windows.md` |
| 5 | Storage & Runtime | Headless Daemon Execution | Run Docker container engine in background without launching Electron GUI (`Docker Desktop.exe`). | Background daemon launch command; disable UI autostart. | GPU/Electron hooks eliminated; `dwm.exe` memory stabilizes at ~50-100MB. | If GUI runs: DWM memory balloons to 750MB+, causing cursor stutter and click delay. | `Performance_Problem.md` |
| 6 | Isolation | Dual Compose Namespaces | Run stacks under independent project names (`ki-basis-private` vs `ki-basis-community`). | Docker Compose `-p <project-name>` argument. | Fully scoped container, volume, and network namespace tags. | If same namespace is reused: containers are replaced or torn down on restart. | R2 Spec & Compose CLI standard |
| 7 | Isolation | Isolated Docker Bridge Networks | Assign each stack to an isolated bridge network with independent internal subnets. | Networks block: `ki-basis-private-net` vs `ki-basis-community-net`. | Complete network namespace segmentation; no cross-stack DNS or IP routing. | If containers share network: cross-stack data leaks and service discovery collisions occur. | R2 Spec & `compose.yaml` |
| 8 | Isolation | Non-Overlapping Host Port Bands | Map Private stack to 8080–8089/8642/9119 and Community to 9080–9089/9642/9219 on `127.0.0.1`. | Host port bindings in Compose file / `.env` variables. | Both stacks listen concurrently on Windows host loopback without overlap. | If overlapping ports are mapped: Docker daemon throws `bind: address already in use` error. | R2 Spec & `compose.yaml` |
| 9 | Isolation | Database Host Port Concealment | Keep PostgreSQL (5432) and Valkey (6379) unexposed to the host on both stacks. | Omission of `ports:` section on `postgres` and `valkey` services. | Database sockets accessible only via internal bridge network to authorized stack containers. | If exposed: port collisions on host and exposure of DB substrate to local Windows processes. | `AGENT-OPERATING-CONTEXT.md` & `verify-stack.sh` |
| 10 | Isolation | Segregated PostgreSQL Instances | Deploy two distinct PostgreSQL container instances backed by separate named volumes. | Services `ki-basis-private-postgres` and `ki-basis-community-postgres`. | Strict physical database file isolation; separate WAL, user tables, and vector stores. | If shared DB instance is used: potential accidental query leakage or schema collisions. | R2 Spec & `compose.yaml` |
| 11 | Isolation | Segregated Valkey Queue Brokers | Deploy two distinct Valkey container instances backed by separate named volumes. | Services `ki-basis-private-valkey` and `ki-basis-community-valkey`. | Independent in-memory task queues and document OCR dispatch pipelines. | If shared: Paperless worker in Community could pop document jobs from Private queue. | R2 Spec & `compose.yaml` |
| 12 | Isolation | Segregated Paperless Document Vaults | Run separate Paperless-ngx instances with distinct media/data volumes and encryption keys. | Independent volumes: `*-paperless-data`, `-media`, `-export`, `-consume`. | Independent OCR index, separate document tags, distinct API authentication tokens. | If volumes shared: commercial invoices mingled with non-profit event receipts. | R2 Spec & `compose.yaml` |
| 13 | Isolation | Segregated Firefly Ledgers | Run separate Firefly III instances with independent `APP_KEY` and upload volumes. | Independent volumes: `*-firefly-upload`; unique `APP_KEY` strings. | Private stack holds consulting accounts; Community stack holds Safer Space e.V. GLS accounts. | If shared: mixing private profit/loss with German non-profit tax spheres. | R2 Spec & `STACK_ARCHITECTURE.md` |
| 14 | Isolation | Segregated OpenProject Workspaces | Run separate OpenProject instances with distinct asset volumes and secret keys. | Independent volumes: `*-openproject-assets`; unique `OPENPROJECT_SECRET_KEY_BASE`. | Private project boards isolated from Equinox volunteer shift schedules and work packages. | If shared: volunteers could access private enterprise tasks or vice versa. | R2 Spec & `compose.yaml` |
| 15 | Isolation | Segregated Hermes Operating Surfaces | Run separate Hermes containers with distinct workspaces, API server keys, and Telegram bots. | Independent volumes: `*-hermes-data`, `*-hermes-workspaces`; unique `HERMES_API_SERVER_KEY`. | Community Hermes handles volunteer Telegram intake; Private Hermes handles confidential coding tasks. | If bot token shared: Telegram API throws 409 conflict and halts polling. | R2 Spec & `compose.yaml` |
| 16 | Isolation | Dedicated Nginx Edge Routing | Run independent Nginx edge proxies with instance-specific landing dashboards and health endpoints. | Port `8084` (Private) and Port `9084` (Community); distinct `default.conf`. | Quick visual status and direct links to the appropriate stack's web interfaces. | If shared: proxy routing confusion between identical upstream container names. | `compose.yaml` & `docker/nginx/default.conf` |
| 17 | Strategy Evaluation | Strategy A Single-Engine Orchestration | Run both namespaces on a single Docker Engine via `-p` flags and distinct `.env` files. | Compose commands: `docker compose -p ki-basis-private` & `-p ki-basis-community`. | Streamlined lifecycle, ~3 GB combined RAM, zero `localhostForwarding` issues. | Low failure risk; single engine crash impacts both stacks (mitigated by clean on-demand lifecycle). | R3 Spec |
| 18 | Strategy Evaluation | Strategy B Dual-Daemon Evaluation | Analyze running Private in WSL2 native dockerd and Community in Docker Desktop. | Context flags: `--context wsl-native` vs `--context default`. | Strong VM-level hypervisor boundary. | High failure risk: `localhostForwarding` port collisions, 5-6 GB RAM overhead, memory thrashing. | R3 Spec & `.wslconfig` docs |
| 19 | Operations & Backup | Namespace-Aware Stack Backup | Backup script parameterized by project namespace and target directory. | Parameter: `PROJECT_NAME` (`ki-basis-private` or `ki-basis-community`). | Independent database dumps (`pg_dumpall`, `pg_dump -Fc`) and tarred volume archives. | If unparameterized: backup script overwrites single target or dumps wrong database. | `backup-stack.sh` |
| 20 | Operations & Lifecycle | Graceful Dual-Stack Lifecycle | Start and stop scripts supporting individual stack targeting or coordinated dual shutdown. | Script arguments: `-Project [private|community|all]`, `-StopEngine`. | Safe sequential shutdown (apps stopped before DB, DB flushed before daemon exit). | If stopped ungracefully: PostgreSQL WAL corruption or dirty lock files on next boot. | `start-ki-basis.ps1` & `stop-ki-basis.ps1` |

---

## 6. Edge Cases & Failure Modes

| # | Feature | Input / Trigger Condition | Observed / Modeled Behavior | Mitigation / Required Design |
|---|---|---|---|---|
| 1 | OpenProject Storage | Declaring OpenProject assets as a host bind mount on `/mnt/c/` in WSL2. | Entrypoint script fails to set permissions for UID 1000; Puma cannot write PID file due to 9P lock failure; container crashes with `exit status 1`. | Mandate Docker named volume (`openproject_assets`) backed by native ext4 storage. |
| 2 | Host Port Allocation | Attempting to start Community stack when its port configuration duplicates Private stack ports (e.g. both using 8082). | Docker Engine returns fatal error: `driver failed programming external connectivity on endpoint ...: Bind for 127.0.0.1:8082 failed: port is already allocated`. | Strict port band segregation: Private on 8080–8089, Community on 9080–9089. Validate via config pre-flight. |
| 3 | Strategy B `localhostForwarding` | Running WSL2 native dockerd and Docker Desktop simultaneously with `localhostForwarding=true` in Windows `.wslconfig`. | WSL2 captures Windows port forward; when Docker Desktop attempts to publish port, Windows throws `WSAEADDRINUSE`, or outbound browser requests intermittently connect to the wrong daemon. | Recommend Strategy A. If Strategy B is tested, port bands must remain completely disjoint and loopback binding strictly enforced. |
| 4 | Database Parallel Boot | Executing `docker compose up -d` simultaneously for both stacks on system boot. | High disk I/O during dual PostgreSQL initialization (`initdb`) causes OpenProject in one stack to exceed `PG_STARTUP_WAIT_TIME=30`. | Increase `PG_STARTUP_WAIT_TIME=60` and implement dependent service health checks (`condition: service_healthy`). |
| 5 | Telegram Bot Polling Conflict | Reusing the same `TELEGRAM_BOT_TOKEN` in both `.env.private` and `.env.community`. | Telegram API returns HTTP 409 Conflict: `Conflict: terminated by other getUpdates request; make sure that only one bot instance is running`. Both instances fail polling. | Enforce distinct Telegram bot tokens in `.env.private` vs `.env.community`, or disable Telegram polling in private stack. |
| 6 | Cross-Stack Network Discovery | Application in Private stack attempts to resolve `postgres` or `paperless` using community network hostname or IP. | Linux network namespace drops packet; Docker embedded DNS returns `NXDOMAIN` (non-existent domain) for foreign stack services. | Independent bridge networks without inter-bridge links ensure air-tight DNS and routing isolation. |
| 7 | Host Sleep / Resume Hibernate | Windows laptop enters modern standby/sleep while 14 containers are running. | Docker Desktop / Hyper-V VM virtual network adapter stalls upon wake; engine CLI hangs indefinitely on `docker ps`. | Implement control-plane restart watchdog in lifecycle script; graceful stack stop before laptop sleep. |
| 8 | Heavy Concurrent Workload | Paperless in Community executes OCR on batch PDF receipts while OpenProject in Private precompiles assets. | CPU load spikes and memory pressure crosses threshold; Windows initiates aggressive Memory Compression (2 GB+), freezing desktop UI. | Enforce hard container limits (`mem_limit: 768M` for Paperless, `1.5G` for OpenProject) and cap OpenProject to 1 worker. |
| 9 | Volume Name Collisions | Omitting project prefix in volume names (e.g. declaring `postgres_data` without namespace prefix in named volume block). | Docker Compose may map both stacks to the same named volume if project name scoping is not declared in the volume definition. | Explicitly name volumes in compose files: `name: ${COMPOSE_PROJECT_NAME}-postgres-data` or define distinct volume names. |
| 10 | Unintended Docker Socket Exposure | Adding `/var/run/docker.sock` to Hermes container volumes in either stack. | Hermes LLM tool execution environment gains root control over the host Docker daemon, breaking container isolation across both stacks. | Strictly prohibit `/var/run/docker.sock` in Hermes compose definition. Verified by automated negative check in `verify-stack.sh`. |

---

## 7. Migration & Operational Runbook Requirements

### 7.1 Migration Runbook Requirements (Single-Instance to Dual-Instance)
1. **Pre-Migration Snapshot**:
   - Execute full bounded snapshot of the existing single `ki-basis` stack using `backup-stack.sh`.
   - Record SHA256 checksums of database dumps and volume archives.
2. **Data Classification & Segregation**:
   - Identify existing database contents: determine which OpenProject work packages, Paperless tags, and Firefly transactions belong to Community (Safer Space e.V. / Equinox) vs. Private.
   - For PostgreSQL: Restore baseline dumps into `ki-basis-community-postgres-data` (since existing stack contains Equinox data), while initializing a clean, fresh schema for `ki-basis-private-postgres-data`.
3. **Volume Renaming & Provisioning**:
   - Clone named volumes to new namespace conventions using Docker helper container or copy-volume scripts.
   - Ensure clean file permissions (`chown -R 1000:1000`) on ext4 volumes for Paperless and OpenProject.
4. **Configuration Generation**:
   - Generate `.env.private` with Port Band 8080–8089 and distinct secrets.
   - Generate `.env.community` with Port Band 9080–9089 and distinct secrets.

### 7.2 Daily Operations Runbook Requirements
1. **On-Demand Lifecycle Management**:
   - `start-ki-basis.ps1 -Project [private|community|all]`: Starts Docker engine headless if not running, brings up selected stack(s), waits for healthcheck endpoints.
   - `stop-ki-basis.ps1 -Project [private|community|all] -KeepDockerDesktopRunning`: Gracefully stops application writers first, flushes PostgreSQL, and optionally stops the Docker background daemon.
2. **Health Verification**:
   - Parameterized `verify-stack.sh` supporting `--project ki-basis-private` and `--project ki-basis-community`:
     - Checks all 7 containers running and attached to designated network.
     - Confirms PostgreSQL and Valkey have zero host-published ports.
     - Confirms Hermes Docker socket absence and absence of `/mnt/c` bind mounts.
     - Executes authenticated and negative-authorization API checks against Paperless, Firefly, and OpenProject.
3. **Automated Dual-Stack Backup**:
   - Parameterized `backup-stack.sh <project_name>`: Creates point-in-time logical database dumps and volume tarballs without cross-contaminating backup archives.

---

## 8. Summary of Extracted Specifications

| Requirement Area | Extracted Specification & Technical Decision |
|:---|:---|
| **Storage Substrate** | 100% ext4 Docker named volumes. Zero 9P bind mounts (`/mnt/c`) for state or databases. |
| **OpenProject Stability** | Single Puma web worker (`OPENPROJECT_WEB_WORKERS=1`), single background worker (`OPENPROJECT_BACKGROUND_WORKERS=1`), `PG_STARTUP_WAIT_TIME=60`. |
| **Runtime Mode** | Headless background daemon. Docker Desktop GUI closed; GPU/Electron hooks eliminated. |
| **Namespaces** | Two Compose projects: `ki-basis-private` and `ki-basis-community`. |
| **Network Isolation** | Two non-overlapping bridge networks (`ki-basis-private-net` and `ki-basis-community-net`). No cross-routing, no inter-stack DNS. |
| **Host Port Mapping** | Private on 8080–8089, 8642, 9119. Community on 9080–9089, 9642, 9219. Loopback only (`127.0.0.1`). |
| **Database Exposure** | PostgreSQL (:5432) and Valkey (:6379) unpublished on host in both stacks. |
| **Multi-Engine Evaluation** | **Strategy A (Dual Compose Projects on Single Engine)** selected over Strategy B due to lower RAM footprint (~3 GB vs 6 GB), zero `localhostForwarding` risk, and operational simplicity. |
| **Acceptance Criteria** | Idle CPU < 5%, zero port collisions, 100% ext4 persistence, zero shared volumes/DBs, complete runbooks. |
