# Meta Implementation Plan — Shared Docker Tool Stack with Hermes Control Surface

**Status:** implementation-ready design  
**Scope:** nginx, PostgreSQL/pgvector, Valkey, Firefly III, Paperless-ngx, OpenProject, Hermes  
**Stack model:** one Docker Compose project, one shared bridge network, persistent named volumes, per-service localhost ports.

## Critical architecture correction

The desired topology is valid, but **Alpine is not the mandatory base image for every tool**.

| Tool | Image policy | Alpine? |
|---|---|---|
| nginx | reuse existing ki-basis Alpine build if required; otherwise official nginx Alpine image | Yes |
| PostgreSQL + pgvector | official pgvector image when pgvector is required | No by default |
| Valkey | official Valkey Alpine image | Yes |
| Firefly III | official Firefly III image | Do not rebuild on Alpine |
| Paperless-ngx | official Paperless-ngx image | Do not rebuild on Alpine |
| OpenProject | official OpenProject image | Do not rebuild on Alpine |
| Hermes | official `nousresearch/hermes-agent` image | Do not rebuild on Alpine |

## Target topology

```text
Browser / Homepage
   |
   | localhost host ports
   v
Docker host
┌───────────────────────────────────────────────────────────────┐
│ Docker Compose project — network: ki-basis-net              │
│                                                               │
│ nginx        Hermes        Firefly     Paperless  OpenProject │
│ :80/:443     :8642/:9119   :8080       :8000      :80         │
│                              |          |           |          │
│                              +----------+-----------+          │
│                                         |                     │
│                         PostgreSQL/pgvector :5432              │
│                                         |                     │
│                                  Valkey :6379                  │
└───────────────────────────────────────────────────────────────┘
```

Inside the Docker network, service names are hostnames:

- `postgres:5432`
- `valkey:6379`
- `firefly:8080`
- `paperless:8000`
- `openproject:80`
- `hermes:8642`
- `nginx:80`

Do not use `localhost` for container-to-container communication.

## Host-port rule

Human-facing UIs get localhost-only ports. Exact host-side numbers must be copied from the existing Homepage/port registry before implementation.

```text
127.0.0.1:<FIREFLY_HOST_PORT>     -> firefly:8080
127.0.0.1:<PAPERLESS_HOST_PORT>   -> paperless:8000
127.0.0.1:<OPENPROJECT_HOST_PORT> -> openproject:80
127.0.0.1:9119                    -> hermes:9119
127.0.0.1:8642                    -> hermes:8642
127.0.0.1:<NGINX_HOST_PORT>       -> nginx:80
```

PostgreSQL and Valkey are not published to the host by default.

## nginx role

nginx is the browser-facing edge/reverse proxy. It can provide friendly URLs/TLS later. It is **not** the internal communication bus; Docker DNS already handles internal communication.

## Hermes role

Hermes is the AI operating surface. It joins `ki-basis-net` and reaches:

- `http://firefly:8080`
- `http://paperless:8000`
- `http://openproject:80`

Network reachability is only transport. Actual tool control requires a dedicated connector/skill plus an API credential.

Hermes should control Firefly, Paperless and OpenProject through their application APIs. It should not routinely manipulate PostgreSQL or Valkey directly.

**Do not mount `/var/run/docker.sock` into Hermes in the first version.**

## Shared data services

One PostgreSQL/pgvector server, separate DB + user per application:

```text
firefly database     owner: firefly_app
paperless database   owner: paperless_app
openproject database owner: openproject_app
```

One Valkey service. Paperless uses it immediately. Firefly may use it later for cache/session. Do not force OpenProject onto Valkey.

## Persistence

- PostgreSQL: `postgres_data`
- Valkey: `valkey_data`
- Firefly: `firefly_upload`
- Paperless: data/media/export/consume volumes
- OpenProject: assets/attachments
- Hermes: `/opt/data`

`docker compose down` must not delete volumes.

## Secrets

Commit `.env.example`, never the real `.env`. Unique DB credentials and API keys per application.

## Recommended repository layout

```text
ki-basis/
├── compose.yaml
├── .env.example
├── docker/
│   ├── nginx/
│   ├── postgres/init/
│   ├── valkey/
│   ├── firefly/
│   ├── paperless/
│   ├── openproject/
│   └── hermes/
└── scripts/
    ├── validate-stack.sh
    ├── health-stack.sh
    ├── backup-stack.sh
    └── restore-test.sh
```

## Implementation order

### M0 — Inventory current state
Record current containers, volumes, networks, Homepage ports, architecture, data to preserve, and installed versions.

### M1 — Compose skeleton
Create project, shared network, volumes, `.env.example`, port variables. Run `docker compose config`.

### M2 — PostgreSQL/pgvector
Create DB/users. Verify health, isolation, pgvector.

### M3 — Valkey
Deploy internal-only Valkey. Verify `PING`, persistence and app connectivity.

### M4 — Firefly
Official image, shared PostgreSQL, assigned host port, persistence, optional cron sidecar.

### M5 — Paperless
Official image, shared PostgreSQL + Valkey, assigned host port, OCR/persistence.

### M6 — OpenProject
Official image, shared PostgreSQL, assigned host port. Start simple; promote to upstream multi-process Compose only if required.

### M7 — nginx
Reuse existing justified Alpine build or official nginx Alpine image. Add proxy routes after apps work directly.

### M8 — Hermes
Official image, persistent `/opt/data`, network membership, dashboard/API on localhost.

### M9 — Hermes connectors
One connector at a time: Firefly -> Paperless -> OpenProject. Start read-only, then add controlled mutations.

### M10 — Full integration test
All services healthy, host ports correct, Docker DNS works, app data persists, Hermes read-only API smoke passes, DB/cache are not host-exposed.

### M11 — Backup/restore proof
Back up DBs, volumes and Hermes state; perform one actual restore test.

## Final acceptance

The stack is done when the operator can open Homepage, reach each application, open Hermes, ask Hermes to inspect supported data in Firefly/Paperless/OpenProject, restart the stack without data loss, and upgrade one tool independently.
