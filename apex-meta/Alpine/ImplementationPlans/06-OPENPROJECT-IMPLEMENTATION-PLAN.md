# OpenProject Implementation Plan

## Purpose
Project-management application exposed as one logical tool to the operator and Hermes.

## Image
Use official pinned OpenProject image. Do not rebuild on Alpine.

## Deployment choice
OpenProject supports:
1. all-in-one container — simplest for local/personal pilot;
2. official multi-process Compose — recommended upstream for production.

Recommended rollout:
- Phase 1: simplest official arrangement that works with shared PostgreSQL.
- Phase 2: promote to official multi-process Compose only if long-running production requirements justify it.

The operator still sees one OpenProject tile/port either way.

## Network
Logical service: `openproject`
Internal web port: `80`
Network: `ki-basis-net`

Host mapping: `127.0.0.1:<OPENPROJECT_HOST_PORT>:80`

## PostgreSQL
`DATABASE_URL=postgres://openproject_app:<secret>@postgres:5432/openproject`

## Cache
Do not automatically replace OpenProject's supported cache with Valkey. Preserve upstream-supported caching architecture.

## Persistence
Persist `openproject_assets`. DB lives in shared Postgres.

## Secrets
Persist `SECRET_KEY_BASE`, DB password and API credential outside Git.

## Health
Use:
- `/health_checks/default`
- `/health_checks/database`

## Validation
1. app starts;
2. database health passes;
3. UI opens;
4. admin account secured;
5. create test project/work package;
6. restart stack;
7. data remains;
8. API v3 read succeeds;
9. health checks remain green.

## Hermes
Internal URL: `http://openproject:80`
API: `/api/v3`

Start with list/read projects/work packages. Then controlled create/update/comment operations. Deletion and broad restructuring remain separately authorized.

## Acceptance
Stable browser port + shared Postgres + persistent assets + Hermes API v3 read all pass.
