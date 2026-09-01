# PostgreSQL + pgvector — Antigravity Implementation Module

## Target

Run one shared PostgreSQL/pgvector service with isolated application databases/users for Firefly, Paperless and OpenProject.

## Real target

Actual PostgreSQL and pgvector must execute. A SQLite/local JSON substitute does not count.

## Image

Use a pinned official pgvector/PostgreSQL image compatible with the selected PostgreSQL major version. Do not force Alpine when that would diverge from the supported pgvector image path.

## Network

Service name: `postgres`
Internal port: `5432`
No host port by default.

## Persistent state

Use the approved persistent volume from the meta plan. Existing database state discovered in M0 must be preserved/migrated deliberately; never replace it blindly.

## Database isolation

Create separate DB/user pairs:
- `firefly` / `firefly_app`
- `paperless` / `paperless_app`
- `openproject` / `openproject_app`

Each application receives only its own credentials. Do not provide application services with the PostgreSQL superuser password.

## Required work

1. recheck current official PostgreSQL/pgvector image guidance;
2. inspect existing DB state from M0;
3. patch Compose/init/config only within approved scope;
4. initialize roles/databases/extensions deterministically for a clean install;
5. preserve existing state path for non-clean install;
6. add health check using `pg_isready`;
7. test application-role isolation.

## Independent/negative proof

- actual `SELECT version()` from PostgreSQL;
- actual `SELECT extversion FROM pg_extension WHERE extname='vector'` where enabled;
- each app user can access its own DB;
- deliberate cross-database/app-role access is rejected or lacks unintended privileges;
- host port scan/config confirms 5432 is not published;
- restart/recreate test preserves seeded test data.

## Forbidden substitutes

- one shared application DB/user for all apps;
- hard-coded PASS/healthy metadata;
- deleting existing database volumes without explicit migration approval;
- exposing PostgreSQL to LAN/host merely for convenience.

## Acceptance

PASS only when actual PostgreSQL+pgvector runs, data persists, app DBs are isolated, and the service is reachable from the Docker network as `postgres:5432`.

Commit only PostgreSQL/pgvector-scoped changes and STOP.