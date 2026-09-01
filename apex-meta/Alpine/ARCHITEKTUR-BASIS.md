# ki-basis — Platform-Architektur (Startpunkt)

> **Startpunkt-Diagramm** für den Full-Stack. ki-basis ist die **gemeinsame Platform**,
> auf der Domain-Stacks wie [ki-pm](~/dev/ki-pm) aufsetzen.
> Full-Stack-Architektur (ki-basis + ki-pm, **alles via MCP**): siehe
> [`~/dev/ki-pm/docs/FULL-STACK-ARCHITEKTUR.md`](~/dev/ki-pm/docs/FULL-STACK-ARCHITEKTUR.md).

```mermaid
flowchart TB
    subgraph edge [KI-BASIS — HTTP-Edge]
        NGX[Platform-nginx<br/>127.0.0.1:3003 · 10200 · 8086 · 8084]
    end

    subgraph core [KI-BASIS — Kern-Services]
        ANYTHING[AnythingLLM<br/>Chat-UI · RAG · Agent · MCP-Host]
        VALKEY[(Valkey<br/>Shared Redis)]
        PG[(Postgres + pgvector<br/>Multi-DB Plattform)]
        PSONO[Psono<br/>Passwort-Tresor]
    end

    subgraph domain [Domain — Belegstack]
        FIREFLY[Firefly III<br/>Beleg-/Buchhaltung<br/>firefly-iii:8080]
    end

    subgraph svc [KI-BASIS — Dienste]
        ENVOY[Envoy + Semantic Router<br/>LLM-Front-Door :8801]
        OMLX[(oMLX<br/>:8000 · Multi-Model)]
        OLLAMA[(Ollama · Fallback)]
        SPEACH[Speaches<br/>STT / SSE / TTS]
        AUTH[Authentik<br/>SSO / IdP]
    end

    subgraph db [Postgres — je Tool eine DB]
        DB1[(anythingllm db)]
        DB3[(openproject db)]
        DB4[(authentik db)]
        DB5[(psono db)]
        DB6[(firefly db)]
    end

    PG --> DB1
    PG --> DB3
    PG --> DB4
    PG --> DB5
    PG --> DB6

    ANYTHING -->|"LLM /v1"| ENVOY
    ENVOY --> OMLX
    ANYTHING -.->|"Fallback"| OLLAMA
    ANYTHING --> DB1
    SPEACH -.->|"Voice-Chat (Profil)"| ENVOY
    AUTH -->|"REDIS"| VALKEY
    FIREFLY -->|"REDIS"| VALKEY

    NGX --> ANYTHING
    NGX --> PSONO
    NGX --> FIREFLY
    AUTH -.->|"SSO optional"| ANYTHING
```

> **Kern-Service-Linie (`bash docker/scripts/start-basis.sh`):**
> `postgres`, `valkey`, `anythingllm`, `psono`, `authentik`, `semantic-router`, `envoy`, `nginx`;
> optional per Profil `ollama` (+`--ollama`), `speaches`.
> Firefly III: Domain `belegstack` (nicht Kern) — siehe [FIREFLY.md](FIREFLY.md).
>
> **LLM-Default:** Host-natives **oMLX** (Metal) — optional hinter **Envoy + Semantic Router** in Compose.
> Chat-Clients: `http://envoy:8801/v1` oder direkt `http://host.docker.internal:8000/v1`.
> Host-Port `:8000` für oMLX und lokale Healthchecks — siehe [DEC-0031](knowledge/decisions/dec-0031-semantic-router-compose-front-door.md).

### Betreffende Doku
- [docs/DOCKER.md](DOCKER.md) · [docs/NGINX.md](NGINX.md)
- [docs/SPEACHES.md](SPEACHES.md)
- [docs/PSONO.md](PSONO.md) · [docs/FIREFLY.md](FIREFLY.md) · [docs/DATENBANK.md](DATENBANK.md)
- [docs/ANYTHINGLLM.md](ANYTHINGLLM.md) (Workspaces, RAG, MCP `autoStart`)
- [config/semantic-router/README.md](../config/semantic-router/README.md) · [DEC-0031](knowledge/decisions/dec-0031-semantic-router-compose-front-door.md)
