# OpenProject — Antigravity Implementation Module

## Target

Run actual OpenProject as one logical tool in the shared Docker stack, using shared PostgreSQL and one stable browser entry point.

## Real target

Actual OpenProject must participate. A local project-management adapter, Markdown task database, fake API, or direct DB manipulation does not count.

## Image/topology

Use a pinned official OpenProject image/topology.

OpenProject may require more than one physical container in its officially supported production Compose topology. Preserve that supported topology when needed; the operator still experiences one logical OpenProject tool.

For the initial local/personal pilot, prefer the simplest official arrangement that works with external PostgreSQL. Promote to the upstream multi-process Compose layout only when required by the verified target or official guidance.

Do not rebuild OpenProject on Alpine.

## Network

Logical endpoint name: `openproject`
Internal web port: `80` for the exposed app/proxy endpoint selected by the official topology.
Host mapping: verified M0 Homepage port -> internal web endpoint, bound to `127.0.0.1`.

## Database

Use shared PostgreSQL:
`postgres:5432/openproject`
with `openproject_app` credentials from ignored env/secrets.

## Cache/process services

Do not force OpenProject onto Valkey. Preserve the current upstream-supported caching/process architecture unless current official documentation explicitly supports the intended alternative.

## Persistence

Persist upstream-required assets/attachments and preserve any existing OpenProject state found in M0.
Persist `SECRET_KEY_BASE` and all required credentials outside Git.

## Proof

1. actual OpenProject starts;
2. `/health_checks/default` succeeds;
3. `/health_checks/database` proves connection to shared PostgreSQL;
4. actual UI loads on assigned host port;
5. create one non-sensitive test project/work package through OpenProject;
6. restart/recreate application service(s);
7. test work package persists;
8. authenticated API v3 read returns the created real object;
9. invalid API credential is rejected.

## Forbidden substitutes

- direct DB writes as proof of OpenProject behavior;
- fake `/api/v3` adapter;
- replacing supported upstream process topology merely to force one container;
- forcing Valkey without official support;
- deleting existing OpenProject assets/data without explicit migration approval.

## Acceptance

PASS only when actual OpenProject UI, health endpoints, shared-DB persistence and API v3 read are independently proven.

Commit only OpenProject-scoped changes and STOP.