# Hermes Implementation Plan — Tool-Stack Control Surface

## Purpose
Hermes is the AI operating surface for Firefly, Paperless and OpenProject.

It is not the database, proxy, or replacement UI for those applications.

## Image
Use official pinned `nousresearch/hermes-agent:<version>`. Do not rebuild Hermes on Alpine.

## Persistence
Mount `~/.hermes` to `/opt/data`.

`/opt/data` owns config, secrets/env, sessions, memory, skills, profiles, logs and hooks.

Never run two gateway containers against the same data directory.

## Network
Join `ki-basis-net`.

Hermes should resolve:
- `firefly`
- `paperless`
- `openproject`
- `nginx`
- `postgres`
- `valkey`

Network visibility does not grant application credentials.

## Ports
Gateway/API: `8642`
Dashboard: `9119`

Host:
- `127.0.0.1:8642:8642`
- `127.0.0.1:9119:9119`

Internal API must bind to `0.0.0.0` and be protected by an API key if other containers need it.

## Required environment
Conceptually:
- `HERMES_DASHBOARD=1`
- `API_SERVER_ENABLED=true`
- `API_SERVER_HOST=0.0.0.0`
- `API_SERVER_KEY=<secret>`

## Repo access
Preserve the existing Hermes repo/workspace mounts and isolation model. This project adds networking only.

## Security
Do not mount `/var/run/docker.sock` in the first version.

Hermes controls applications through their APIs. Docker lifecycle remains host/operator Compose responsibility unless a separate privileged capability is later approved.

## Connector sequence
1. Firefly — `http://firefly:8080`
2. Paperless — `http://paperless:8000`
3. OpenProject — `http://openproject:80`

For each:
- dedicated credential;
- read-only smoke first;
- explicit write methods second;
- destructive operations separately governed.

## Validation
1. service-name DNS works;
2. HTTP connections work;
3. API authentication works;
4. invalid token is rejected;
5. restart Hermes;
6. `/opt/data` persists;
7. repo access still works;
8. no Docker socket is mounted.

## Acceptance
Hermes dashboard/API work, state persists, three read-only connectors work, and existing repo isolation remains unchanged.
