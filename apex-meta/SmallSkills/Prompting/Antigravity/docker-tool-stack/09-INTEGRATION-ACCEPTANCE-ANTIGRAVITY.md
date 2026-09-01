# Full Docker Stack — Antigravity Integration & Acceptance Module

## Target

Prove the complete local Docker tool stack works as one integrated system without relying on self-authored PASS labels.

## Preconditions

Run only after nginx, PostgreSQL/pgvector, Valkey, Firefly, Paperless, OpenProject and Hermes modules are individually accepted.

Read:
- `00-START-HERE.md`
- `01-META-IMPLEMENTATION-PLAN-ANTIGRAVITY.md`
- module result/commit evidence for every accepted service

Do not reopen accepted module architecture unless integration evidence shows an actual incompatibility.

## Required integrated topology

One Compose project with one shared internal Docker network.

Human-facing services retain verified localhost ports.
PostgreSQL and Valkey remain internal-only.
Hermes reaches application APIs over Docker DNS.

## Deterministic checks

1. `docker compose config` succeeds;
2. no fixed container IPs;
3. no unresolved variables;
4. no real secrets tracked in Git;
5. no PostgreSQL/Valkey host ports;
6. intended human-facing ports bind to `127.0.0.1` unless explicitly approved otherwise;
7. Docker socket is not mounted into Hermes;
8. named persistent volumes/mounts exist.

## Runtime checks

Prove actual service state, not declared Compose intent:

- PostgreSQL healthy;
- Valkey returns real PONG;
- Firefly UI/API healthy;
- Paperless UI/API + worker/OCR path healthy;
- OpenProject UI/API/health endpoints healthy;
- nginx actual proxy routes healthy;
- Hermes dashboard/API healthy.

## Docker-network crossing proof

From the actual Hermes execution context, prove:
- `firefly:8080` resolves/reaches the real Firefly product;
- `paperless:8000` resolves/reaches real Paperless;
- `openproject:80` resolves/reaches real OpenProject.

Then prove authenticated application-level reads through the Hermes connectors.

A host-side curl does not count as Hermes integration proof.

## Persistence test

Create or identify one non-sensitive proof object per stateful application:
- Firefly test record;
- Paperless test document;
- OpenProject test work package;
- Hermes persistent test state appropriate to its supported state model.

Record identifiers.

Restart/recreate the complete Compose stack without deleting volumes.

After restart, independently retrieve every proof object through the actual application/Hermes interfaces.

## Deliberate negative tests

At minimum:
- invalid Firefly API credential fails;
- invalid Paperless token fails;
- invalid OpenProject credential fails;
- deliberate wrong DB credential for a bounded disposable test fails rather than silently falling back;
- deliberate invalid nginx config fails `nginx -t` and is then reverted;
- attempt to reach PostgreSQL/Valkey through an unconfigured host port fails.

Do not damage production-like persistent state to create a negative test; use bounded/disposable checks.

## Backup proof

Create real backups of:
- PostgreSQL application DBs;
- application persistent volumes/data according to supported procedures;
- Hermes `/opt/data` or the approved Hermes persistent state path;
- stack configuration excluding plaintext secrets.

Record exact artifact paths/hashes where practical.

## Restore proof

A backup is not accepted merely because files exist.

Perform one controlled restore test using disposable target state/environment where needed. Verify the restored application data through the actual application interface, not just by inspecting archive contents.

## Upgrade independence check

Demonstrate at least one low-risk service can be recreated/upgraded independently without rebuilding or destroying unrelated services. Do not perform an unnecessary major-version upgrade just to satisfy this check.

## Operator acceptance surface

Provide a compact final table:

| Tool | Host URL/port | Internal address | Persistence | Hermes access | Status |
|---|---|---|---|---|---|

Include Firefly, Paperless, OpenProject, nginx, Hermes, PostgreSQL and Valkey.

## PASS definition

PASS requires actual runtime evidence for all required crossings, persistence after full-stack restart, real authenticated Hermes reads, no forbidden host exposure, and one proven restore path.

`PASS_WITH_LIMITATIONS` is allowed only for explicitly non-core optional functionality.

If a named actual product cannot perform the required capability, report `BLOCKED_HUMAN_GATE`, `UNSUPPORTED`, `CORRECTION_REQUIRED`, or `FAIL`; do not create a facade.

## Final boundary

After acceptance evidence is written:
1. run an independent Antigravity verifier/auditor using the existing instruction-orchestrator doctrine;
2. verify actual branch head and changed-file scope;
3. commit only the integration/acceptance artifacts and necessary bounded fixes;
4. STOP.
