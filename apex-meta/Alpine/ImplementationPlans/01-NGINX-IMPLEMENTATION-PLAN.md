# nginx Implementation Plan

## Purpose
Browser-facing edge/reverse proxy. Not the internal Docker communication bus.

## Image
1. Reuse existing `ki-basis/docker/nginx/Dockerfile` if custom modules are still required.
2. Otherwise use a pinned official `nginx:<version>-alpine`.

## Network
Join `ki-basis-net`.

Targets:
- `http://firefly:8080`
- `http://paperless:8000`
- `http://openproject:80`

## Ports
Internal: `80`, later `443`.
Host: preserve existing Homepage nginx port, bound to `127.0.0.1`.

## Steps
1. Inspect current nginx config/build.
2. Decide `reuse-custom` vs `official-alpine`.
3. Attach to shared network.
4. Add one proxy target at a time.
5. Run `nginx -t`.
6. Start/restart and verify routes.

## Acceptance
- `nginx -t` passes.
- Proxy targets use Docker service names, never fixed IPs.
- Direct app ports still work.
- No routing loop.
- Config remains repo-controlled.

## Hermes
No special nginx control API required. Hermes may inspect health and propose config changes; privileged reload/lifecycle remains separately governed.
