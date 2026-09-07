# Project: ki-basis Dual-Instance Separation Architecture

## Architecture
Airtight dual-instance isolation model separating Private Entrepreneurship (`ki-basis-private`) and Community Operations (`ki-basis-community`) under a unified high-performance single Docker engine (Strategy A):

```
                        Windows 11 Host (Headless Docker Desktop / Hyper-V Linux VM)
                                                    │
             ┌──────────────────────────────────────┴──────────────────────────────────────┐
             ▼                                                                             ▼
   [ki-basis-private]                                                            [ki-basis-community]
   Namespace: ki-basis-private                                                   Namespace: ki-basis-community
   Bridge Net: ki-basis-private-net (172.28.0.0/16)                              Bridge Net: ki-basis-community-net (172.29.0.0/16)
   Port Band: 127.0.0.1:8080-8089                                                Port Band: 127.0.0.1:9080-9089
   Services (7):                                                                 Services (7):
   - postgres (pgvector/pg16) [internal :5432]                                   - postgres (pgvector/pg16) [internal :5432]
   - valkey (valkey:8.0) [internal :6379]                                        - valkey (valkey:8.0) [internal :6379]
   - firefly (fireflyiii/core) [127.0.0.1:8086:8080]                            - firefly (fireflyiii/core) [127.0.0.1:9086:8080]
   - paperless (paperless-ngx) [127.0.0.1:8010:8000]                            - paperless (paperless-ngx) [127.0.0.1:9010:8000]
   - openproject (openproject:14) [127.0.0.1:8082:80]                            - openproject (openproject:14) [127.0.0.1:9082:80]
   - nginx (nginx:1.27-alpine) [127.0.0.1:8084:80]                               - nginx (nginx:1.27-alpine) [127.0.0.1:9084:80]
   - hermes (hermes-agent) [127.0.0.1:8642:8642, 9119:9119]                      - hermes (hermes-agent) [127.0.0.1:9642:8642, 9219:9119]
   Storage: 9 named ext4 volumes (ki-basis-private-*)                            Storage: 9 named ext4 volumes (ki-basis-community-*)
   Data isolation: 100% segregated (zero shared tables or volumes)               Data isolation: 100% segregated (zero shared tables or volumes)
```

## Feature Inventory
Every feature from the Survey phase is mapped to an assigned milestone:
| # | Feature | Description | Milestone | Source |
|---|---------|-------------|-----------|--------|
| 1 | F01-EXT4-STORAGE | 100% transition of all persistent state to native ext4 named Docker volumes; 0% 9P bind mounts | M1 | Survey (R1) |
| 2 | F02-OPENPROJECT-CRASH-FIX | Resolution of OpenProject exit status 1 (Puma permissions, PG_STARTUP_WAIT_TIME=60, secret key base) | M1 | Survey (R1) |
| 3 | F03-HEADLESS-RUNTIME | Headless container runtime parameters (worker caps, Celery concurrency, debug mode disabled) | M1 | Survey (R1) |
| 4 | F04-CPU-IDLE-OPTIMIZATION | Steady-state idle CPU stabilization (< 5% aggregate, < 1% per container) | M1 | Survey (R1/AC) |
| 5 | F05-COMPOSE-PARAM | Refactor compose.yaml to remove hardcoded container_name and volume names | M2 | Survey (R2) |
| 6 | F06-NAMESPACE-ISOLATION | Independent Compose project namespaces: ki-basis-private vs ki-basis-community | M2 | Survey (R2) |
| 7 | F07-NETWORK-ISOLATION | Isolated bridge networks preventing cross-stack routing and DNS discovery | M2 | Survey (R2) |
| 8 | F08-PORT-BAND-ALLOCATION | Deterministic port allocation: Private (8080-8089, 8642, 9119) vs Community (9080-9089, 9642, 9219) | M2 | Survey (R2) |
| 9 | F09-DB-VALKEY-SEGREGATION | Dedicated PostgreSQL and Valkey containers per stack with unexposed host ports | M2 | Survey (R2) |
| 10 | F10-DATA-STORAGE-SEGREGATION | 18 independent named ext4 volumes (9 per stack) with zero cross-mounting | M2 | Survey (R2) |
| 11 | F11-ENV-TEMPLATE-ISOLATION | Distinct .env.private and .env.community configuration files with unique secrets | M2 | Survey (R2) |
| 12 | F12-STRATEGY-A-EVALUATION | Architectural and empirical evaluation of Strategy A (Single Engine / Dual Compose) | M3 | Survey (R3) |
| 13 | F13-STRATEGY-B-EVALUATION | Failure mode analysis of Strategy B (Dual Daemon Split, localhostForwarding conflicts) | M3 | Survey (R3) |
| 14 | F14-ADR-DECISION-RECORD | Formal Architectural Decision Record (ADR) documenting Strategy A selection | M3 | Survey (R3) |
| 15 | F15-MIGRATION-RUNBOOK | Step-by-step data migration runbook from single ki-basis to dual-instance | M4 | Survey (Ops) |
| 16 | F16-DAILY-OPS-RUNBOOK | Daily operations, maintenance, startup/shutdown, and troubleshooting guide | M4 | Survey (Ops) |
| 17 | F17-SCRIPT-PORTABILITY | Parametrize client scripts (populate_*, verify_*, generate_*) to accept dynamic ports/URLs | M4 | Survey (Ops) |
| 18 | F18-CONCURRENCY-VALIDATION | Validation that both stacks run simultaneously with zero port collisions | M5 | Survey (AC) |
| 19 | F19-ZERO-LEAKAGE-AUDIT | Automated verification that zero volumes, networks, or DB tables are shared | M5 | Survey (AC) |
| 20 | F20-E2E-HEALTH-VERIFICATION | Full healthcheck and HTTP endpoint status verification across all 14 containers | M5 | Survey (AC) |

## Milestones
| # | Name | Scope | Dependencies | Status |
|---|------|-------|-------------|--------|
| M1 | Storage Architecture & Runtime Hardening | F01, F02, F03, F04 | none | DONE |
| M2 | Dual-Instance Isolation Architecture | F05, F06, F07, F08, F09, F10, F11 | M1 | DONE |
| M3 | Multi-Engine vs Multi-Project Strategy Evaluation | F12, F13, F14 | M1, M2 | DONE |
| M4 | Operational Runbooks & Script Portability | F15, F16, F17 | M2 | DONE |
| M5 | E2E Concurrency Validation & Forensic Integrity Audit | F18, F19, F20 | M1, M2, M3, M4 | DONE |

## Interface Contracts

### Network and Port Allocation
| Service | Private Stack (Port Band 8080-8089) | Community Stack (Port Band 9080-9089) | Host Loopback Binding |
|---|---|---|---|
| PostgreSQL | internal: 5432 (not published) | internal: 5432 (not published) | None |
| Valkey | internal: 6379 (not published) | internal: 6379 (not published) | None |
| Firefly III | 127.0.0.1:8086 -> 8080 | 127.0.0.1:9086 -> 8080 | Loopback only |
| Paperless-ngx | 127.0.0.1:8010 -> 8000 | 127.0.0.1:9010 -> 8000 | Loopback only |
| OpenProject | 127.0.0.1:8082 -> 80 | 127.0.0.1:9082 -> 80 | Loopback only |
| Nginx Reverse Proxy | 127.0.0.1:8084 -> 80 | 127.0.0.1:9084 -> 80 | Loopback only |
| Hermes Gateway | 127.0.0.1:8642 -> 8642 | 127.0.0.1:9642 -> 8642 | Loopback only |
| Hermes Dashboard | 127.0.0.1:9119 -> 9119 | 127.0.0.1:9219 -> 9119 | Loopback only |

### Volume Namespace Mapping
| Volume Purpose | Private Stack Volume Name | Community Stack Volume Name | Backend Driver |
|---|---|---|---|
| PostgreSQL Data | `ki-basis-private-postgres-data` | `ki-basis-community-postgres-data` | local (ext4 named volume) |
| Valkey Data | `ki-basis-private-valkey-data` | `ki-basis-community-valkey-data` | local (ext4 named volume) |
| Firefly Uploads | `ki-basis-private-firefly-upload` | `ki-basis-community-firefly-upload` | local (ext4 named volume) |
| Paperless Data | `ki-basis-private-paperless-data` | `ki-basis-community-paperless-data` | local (ext4 named volume) |
| Paperless Media | `ki-basis-private-paperless-media` | `ki-basis-community-paperless-media` | local (ext4 named volume) |
| Paperless Export | `ki-basis-private-paperless-export` | `ki-basis-community-paperless-export` | local (ext4 named volume) |
| Paperless Consume | `ki-basis-private-paperless-consume` | `ki-basis-community-paperless-consume` | local (ext4 named volume) |
| OpenProject Assets | `ki-basis-private-openproject-assets` | `ki-basis-community-openproject-assets` | local (ext4 named volume) |
| Hermes Data | `ki-basis-private-hermes-data` | `ki-basis-community-hermes-data` | local (ext4 named volume) |
| Hermes Workspaces | `ki-basis-private-hermes-workspaces` | `ki-basis-community-hermes-workspaces` | local (ext4 named volume) |

## Code Layout
- `ki-basis/compose.yaml`: Parameterized base compose definition supporting dynamic project namespaces, networks, and volume prefixing.
- `ki-basis/.env.example`: Updated example environment template with dual-instance parameterization.
- `ki-basis/.env.private`: Instance-specific environment configuration for Private Entrepreneurship.
- `ki-basis/.env.community`: Instance-specific environment configuration for Community Operations.
- `ki-basis/scripts/start-ki-basis.ps1` & `start-ki-basis.sh`: Dual-instance launch and lifecycle management scripts.
- `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md`: Complete architectural documentation, R1-R3 evaluation, and ADR.
- `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md`: Comprehensive migration and daily operations runbook.
- `ki-basis/scripts/verify_dual_isolation.py`: Automated verification harness confirming isolation and zero collisions.
