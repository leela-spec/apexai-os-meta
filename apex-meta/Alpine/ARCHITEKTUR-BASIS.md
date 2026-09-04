# ki-basis — Current Platform Architecture

> **Current runtime authority:** `ki-basis/compose.yaml`.  
> This document describes the implemented local Docker stack on Windows 11 with Docker Desktop (Hyper-V backend). The older AnythingLLM/Psono/Authentik/Envoy/oMLX/Ollama/Speaches topology is superseded for the current runtime and remains available through Git history for provenance.

```mermaid
flowchart TB
    subgraph host [WINDOWS 11 — DOCKER DESKTOP HYPER-V BACKEND]
        subgraph edge [KI-BASIS — HTTP Edge]
            NGX[nginx<br/>127.0.0.1:8084<br/>nginx:80]
        end
        subgraph control [KI-BASIS — AI Operating Surface]
            HERMES[Hermes Agent<br/>host :8642 · :9119<br/>internal hermes:8642 · hermes:9119]
        end
        subgraph apps [KI-BASIS — Applications]
            FIREFLY[Firefly III<br/>127.0.0.1:8086<br/>firefly:8080]
            PAPERLESS[Paperless-ngx<br/>127.0.0.1:8010<br/>paperless:8000]
            OPENPROJECT[OpenProject<br/>127.0.0.1:8082<br/>openproject:80]
        end
        subgraph data [KI-BASIS — Shared Data Services]
            PG[(PostgreSQL + pgvector<br/>postgres:5432<br/>internal only)]
            VALKEY[(Valkey<br/>valkey:6379<br/>internal only)]
            DBF[(firefly DB)]
            DBP[(paperless DB)]
            DBO[(openproject DB)]
        end
    end
    PG --> DBF
    PG --> DBP
    PG --> DBO
    FIREFLY --> PG
    PAPERLESS --> PG
    PAPERLESS --> VALKEY
    OPENPROJECT --> PG
    HERMES -->|supported REST API| FIREFLY
    HERMES -->|supported REST API| PAPERLESS
    HERMES -->|API v3| OPENPROJECT
    NGX --> FIREFLY
    NGX --> PAPERLESS
    NGX --> OPENPROJECT
```

> **Current service line (`ki-basis/compose.yaml`):**
> `postgres`, `valkey`, `firefly`, `paperless`, `openproject`, `nginx`, `hermes`.
>
> **Target host/runtime:** Windows 11 with Docker Desktop's Hyper-V Linux-container backend and one Docker Engine. Routine operation is CLI-first/background-only: the Docker Dashboard is kept closed. Fully stopping Docker Desktop stops the current managed Linux runtime; a genuine no-Desktop Docker Engine would require a separate Linux-VM migration.
>
> **Network:** all services join `ki-basis-net` and use Docker service-name DNS. PostgreSQL and Valkey are internal-only.
>
> **Persistence:** PostgreSQL, Valkey, Firefly uploads, Paperless data/media/export/consume, OpenProject assets, and Hermes `/opt/data` are persisted into target-local Docker volumes.
>
> **Hermes role:** Hermes is the canonical local routing/execution plane for future application skills. heavy-reasoning CLI agents call Hermes through its authenticated loopback API server; Hermes then performs its own provider-backed routing/tool execution. The final product skill set is intentionally deferred until the real skills are supplied. Hermes does not mount a Docker socket or rely on Ubuntu WSL filesystem binds.
>
> **Alpine policy:** Alpine is an image choice, not the platform architecture. nginx and Valkey use Alpine-compatible upstream images; complex vendor applications retain supported upstream images.

### Deferred performance tuning — measure first

**Status:** future candidate / no runtime change now.

Do not add hard container CPU/RAM ceilings, reduce Paperless/OpenProject workers, or tune PostgreSQL/Valkey solely from generic recommendations. Open a dedicated tuning module only after measurements show a real bottleneck. Minimum evidence: `docker stats --no-stream` and product symptoms during idle, normal Hermes use, Paperless OCR, OpenProject use, backup, and restore. If no bottleneck is observed, the correct outcome is `NO_CHANGE_REQUIRED`. In particular, do not apply Valkey `allkeys-lru` eviction merely to cap memory because Valkey participates in Paperless' operational path.

### Current authority / evidence
- Runtime: [`../../ki-basis/compose.yaml`](../../ki-basis/compose.yaml)
- Stack environment template: [`../../ki-basis/.env.example`](../../ki-basis/.env.example)
- Current target acceptance: [`TARGET-ACCEPTANCE-REPORT.md`](TARGET-ACCEPTANCE-REPORT.md)
- Historical pre-migration source evidence: [`INTEGRATION-ACCEPTANCE-REPORT.md`](INTEGRATION-ACCEPTANCE-REPORT.md)
- Antigravity implementation authority: [`ImplementationPlans/00-START-HERE.md`](ImplementationPlans/00-START-HERE.md)
- Alpine image-build reference: [`2026-09-01-alpine-image-build.md`](2026-09-01-alpine-image-build.md)
- Docker Desktop/Windows performance research input (non-authoritative): [`research/Docker-Desktop-Windows.md`](research/Docker-Desktop-Windows.md)

