# Hermes — Antigravity Implementation Module

## Target

Run the actual Hermes Agent container as the AI operating surface for the Docker tool stack while preserving the existing Hermes repository/workspace isolation model.

Hermes must be able to reach Firefly, Paperless and OpenProject through the internal Docker network and their supported APIs.

## Real target

Actual Hermes Agent must run. A generic chat UI, local HTTP client, fake Hermes endpoint, or script that directly calls application APIs does not count as Hermes integration.

## Image

Use a pinned official `nousresearch/hermes-agent:<version>` image after rechecking current official Hermes Docker guidance.

Do not rebuild Hermes on Alpine merely for image consistency.

## Persistence

Persist Hermes state at `/opt/data` using the existing approved host/state path.

Before changing mounts, inspect the current Hermes runtime from M0 and preserve:
- config;
- profiles;
- skills;
- memory;
- sessions;
- credentials/secrets;
- repo/workspace mounts.

Never run two Hermes gateways concurrently against the same persistent state directory.

## Network

Join the shared Docker network.

Hermes must resolve and reach:
- `firefly:8080`
- `paperless:8000`
- `openproject:80`
- `nginx:80`

Hermes may resolve `postgres` and `valkey` for diagnostics, but routine tool operation must go through application APIs rather than direct database/cache manipulation.

## Ports

Preserve verified host assignments. Expected logical ports:
- Hermes API/gateway: `8642`
- Hermes dashboard: `9119`

Bind host-facing ports to `127.0.0.1` unless M0 authority proves a deliberate LAN-access requirement.

## Critical security boundary

Do not mount `/var/run/docker.sock` into Hermes in this module.

Do not grant Hermes arbitrary Docker-host lifecycle authority as a side effect of connecting it to application APIs.

## Connector sequence

Implement/test one application connector at a time:

### H1 Firefly
Base URL: `http://firefly:8080`
Use a dedicated Firefly API token.
Initial capability: authenticated read-only account/transaction/budget/report inspection.

### H2 Paperless
Base URL: `http://paperless:8000`
Use dedicated Paperless token auth.
Initial capability: authenticated search/list/read metadata/content.

### H3 OpenProject
Base URL: `http://openproject:80`
Use dedicated OpenProject API credentials.
Initial capability: authenticated project/work-package reads via API v3.

Only add write operations after the read path is proven. Destructive/broad mutations remain separately authorized.

## Anti-facade rules

The following do not count:
- curl from the host presented as Hermes connectivity;
- a local Python script presented as a Hermes skill;
- hard-coded sample responses;
- direct application DB reads presented as API integration;
- generic HTTP reachability presented as authenticated tool operation.

## Proof

1. actual Hermes container starts;
2. dashboard and API/gateway respond on assigned ports;
3. `/opt/data` survives recreate;
4. existing repo/workspace mounts still work;
5. from the actual Hermes execution context, Docker service names resolve;
6. actual authenticated read-only call succeeds against Firefly;
7. actual authenticated read-only call succeeds against Paperless;
8. actual authenticated read-only call succeeds against OpenProject;
9. deliberate invalid credential fails for each connector;
10. inspect runtime mounts and prove Docker socket is absent.

## Human gates

If token creation/login requires browser/account action, Antigravity must prepare exact URLs, names, scopes and storage destination first, then request only the smallest required operator action.

## Acceptance

PASS only when actual Hermes runs with preserved state/isolation and performs real authenticated read-only API operations against all three named applications over the internal Docker network.

Commit only Hermes/connector-scoped changes and STOP.