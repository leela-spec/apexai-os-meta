# nginx — Antigravity Implementation Module

## Target

Provide the browser-facing reverse proxy/front door for the Docker stack without making nginx the internal service bus.

## Real target

Actual nginx runtime must participate. A local mock HTTP server or generated config without a running nginx process does not count.

## Image decision

Inspect the current repository first.

Choose exactly one:
1. reuse the existing justified custom Alpine nginx build if current modules/config require it;
2. otherwise use a pinned official `nginx:<version>-alpine` image.

Do not compile nginx from source merely to satisfy an Alpine preference.

## Network

Join the shared Docker network.

Upstream targets use Docker DNS:
- `firefly:8080`
- `paperless:8000`
- `openproject:80`

Do not proxy to host-mapped ports from inside Docker.

## Scope

- nginx Compose service;
- repo-controlled config;
- localhost host binding from verified port registry;
- health/config test;
- proxy routes for already-working application services only.

## Forbidden substitutes

- fixed container IP addresses;
- routing via host localhost to reach peer containers;
- fake proxy smoke that bypasses nginx;
- changing unrelated application architecture.

## Verification

1. `nginx -t` against the actual runtime/config;
2. deliberate invalid config must fail validation;
3. each configured route must traverse nginx and reach the named Docker service;
4. direct app port remains independently reachable if the meta plan still requires it;
5. restart nginx and repeat smoke.

## Acceptance

PASS only if actual nginx is running, configuration validates, Docker-name proxy routing works, and no fixed IP or secret is embedded.

Commit only nginx-scoped changes and STOP.