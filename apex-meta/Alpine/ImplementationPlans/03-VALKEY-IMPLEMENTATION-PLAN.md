# Valkey Implementation Plan

## Purpose
Shared broker/cache service.

Initial consumer: Paperless-ngx.
Optional later consumer: Firefly III.

## Image
Pinned official `valkey/valkey:<stable>-alpine`.

## Network
Service: `valkey`
Internal port: `6379`
No host port.

## Persistence
`valkey_data`

## Security
Use password/ACL when compatible. Never expose Valkey to LAN/internet.

## App connections
Paperless: `redis://valkey:6379`
Firefly later: `REDIS_HOST=valkey`, `REDIS_PORT=6379`

Do not force OpenProject onto Valkey.

## Health
`valkey-cli ping` -> `PONG`

## Acceptance
- healthy;
- Paperless connects;
- no host port;
- persistence/restart behavior proven.

## Hermes
Not a user-facing Hermes tool. Direct Valkey access only for diagnostics/administration.
