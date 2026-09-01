# Firefly III — Antigravity Implementation Module

## Target

Run the actual Firefly III application in the shared Docker stack, backed by the shared PostgreSQL service and exposed on the verified Homepage port.

## Real target

Actual Firefly III must run. A local finance API, mock UI, adapter or database script presented as Firefly does not count.

## Image

Use the pinned official Firefly III image. Do not rebuild Firefly on Alpine unless current official upstream support explicitly makes that the appropriate image.

## Network

Service name: `firefly`
Internal port: `8080`
Network: shared stack network.
Host mapping: verified M0 Homepage port -> `8080`, bound to `127.0.0.1`.

## Database

Use:
- host `postgres`
- port `5432`
- DB `firefly`
- user `firefly_app`

Real credentials come from ignored env/secrets, never Git.

## Valkey

Do not add Valkey merely because it exists. Keep the simplest officially supported baseline first. Add Firefly cache/session integration only if deliberately required and verified.

## Persistence

Persist all upstream-required Firefly upload/storage paths. Preserve any existing Firefly data discovered in M0.

## Scheduled helper

If the official Firefly deployment requires its cron endpoint/helper, implement the supported helper as part of this logical module. It may be a second physical container; do not fake a one-container topology.

## Proof

1. actual Firefly container starts;
2. actual UI responds on assigned localhost port;
3. Firefly performs DB migrations against `postgres:5432`;
4. create one non-sensitive test record through Firefly itself;
5. restart/recreate application container;
6. test record persists;
7. generate/use a dedicated Firefly API token;
8. authenticated read-only API request returns actual Firefly data;
9. invalid token is rejected.

## Forbidden substitutes

- direct database writes used as proof that Firefly works;
- local REST facade presented as Firefly API;
- app connected to host-mapped PostgreSQL instead of Docker service name;
- deleting existing Firefly state without explicit approval.

## Acceptance

PASS only when actual Firefly UI, database persistence and authenticated API read are independently proven.

Commit only Firefly-scoped changes and STOP.