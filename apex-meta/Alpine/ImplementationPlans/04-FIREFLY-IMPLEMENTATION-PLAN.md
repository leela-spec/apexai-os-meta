# Firefly III Implementation Plan

## Purpose
Personal finance application in the shared stack.

## Image
Use official Firefly III image pinned to an exact tested version. Do not rebuild Firefly on Alpine.

## Network
Service: `firefly`
Internal port: `8080`
Network: `ki-basis-net`

Host mapping: `127.0.0.1:<FIREFLY_HOST_PORT>:8080`

## PostgreSQL
Use shared Postgres:

- `DB_CONNECTION=pgsql`
- `DB_HOST=postgres`
- `DB_PORT=5432`
- `DB_DATABASE=firefly`
- `DB_USERNAME=firefly_app`
- DB password from secret env.

## Valkey
Phase 1: keep simplest supported cache/session baseline.
Phase 2 optional: connect cache/session to `valkey:6379`.

## Persistence
Persist Firefly upload/storage volume. DB state remains in shared Postgres.

## Scheduled jobs
If required, include the official-style lightweight Firefly cron sidecar. Treat it as part of the Firefly logical module, not as another user-facing tool.

## Validation
1. app starts;
2. UI loads;
3. Postgres migration succeeds;
4. login works;
5. data survives restart;
6. read-only API call works;
7. cron succeeds if enabled.

## Hermes
Internal URL: `http://firefly:8080`

Create dedicated token/connector. Start with read-only accounts, transactions, budgets/reports. Add financial mutations only later under explicit authorization.

## Acceptance
UI + DB persistence + authenticated Hermes read-only API smoke all pass.
