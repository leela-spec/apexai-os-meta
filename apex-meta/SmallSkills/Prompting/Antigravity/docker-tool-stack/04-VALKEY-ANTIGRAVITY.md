# Valkey — Antigravity Implementation Module

## Target

Run one shared Valkey service for supported broker/cache use, initially Paperless-ngx and optionally Firefly later.

## Real target

Actual Valkey must execute. A Python dict, fake Redis endpoint or local file cache does not count.

## Image

Use a pinned official Valkey Alpine image when current upstream support confirms it.

## Network

Service name: `valkey`
Internal port: `6379`
No host port.

## Persistence

Use the approved `valkey_data` volume if persistence is enabled by the selected configuration.

## Scope

1. recheck current official Valkey image/config guidance;
2. patch only Valkey Compose/config surfaces;
3. configure persistence/auth only where compatible with the consuming applications;
4. add real health check;
5. verify Paperless-compatible connection path.

## Proof

- actual `valkey-cli ping` returns `PONG`;
- deliberate connection to wrong password fails if auth is enabled;
- Compose inspection confirms no host port;
- restart/recreate preserves test key only if persistence is intentionally enabled;
- Paperless later must connect to `valkey:6379`, never a host-mapped port.

## Forbidden substitutes

- Redis-compatible facade that is not actual Valkey;
- host exposure for convenience;
- forcing OpenProject onto Valkey without upstream support;
- self-authored `healthy=true` as proof.

## Acceptance

PASS only when actual Valkey runs on the shared Docker network, no host port is exposed, and the intended persistence/auth behavior is independently verified.

Commit only Valkey-scoped changes and STOP.