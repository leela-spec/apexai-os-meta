# PostgreSQL / pgvector Implementation Plan

## Purpose
One shared database server with one isolated DB/user per application.

## Image
Because the platform architecture calls for pgvector, use a pinned official `pgvector/pgvector:pg<major>-...` image.

If pgvector is removed later, official PostgreSQL Alpine becomes an option.

## Network
Service: `postgres`
Internal port: `5432`
No host port.

## Persistence
`postgres_data`

## Databases
- `firefly` -> `firefly_app`
- `paperless` -> `paperless_app`
- `openproject` -> `openproject_app`

Each app gets a unique password and no superuser credentials.

## Initialization
Repo-controlled init scripts:
1. create roles;
2. create DBs;
3. set ownership/grants;
4. enable required extensions;
5. avoid real passwords in Git.

## Health
`pg_isready`

## Backup
Per-DB dumps plus role/ownership backup. Major PostgreSQL upgrades are separate migrations.

## Acceptance
- all DBs exist;
- each app user can access only its own DB;
- pgvector works where required;
- data survives recreation;
- no host port exposed.

## Hermes
Normal path is Hermes -> app API -> app -> PostgreSQL. No direct DB credential for routine Hermes operation.
