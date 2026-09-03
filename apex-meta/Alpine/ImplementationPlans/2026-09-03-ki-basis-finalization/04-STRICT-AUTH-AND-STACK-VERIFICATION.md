# Module 04 — Strict Authentication and Stack Verification

## Target

Make final stack verification fail closed and verify the actual product boundaries without expanding architecture.

## Scope

Primary target: `ki-basis/scripts/verify-stack.sh` and only tiny supporting fixtures if necessary.

## Required behavior

When `STRICT_AUTH=1`:

- missing `FIREFLY_API_TOKEN` -> FAIL;
- missing `PAPERLESS_API_TOKEN` -> FAIL;
- missing `OPENPROJECT_API_KEY` -> FAIL;
- authenticated read to each actual product must succeed from the Hermes execution context;
- deliberately invalid credential for each product must be rejected.

The script must continue to verify:

- exactly the seven canonical Compose services;
- all seven attached to `ki-basis-net`;
- Postgres 5432 not host-published;
- Valkey 6379 not host-published;
- Hermes has no Docker socket;
- Hermes has no legacy WSL host bind mounts;
- real Windows localhost endpoints;
- nginx syntax.

## pgvector anti-overengineering rule

Do not create/install the `vector` extension in every database merely to satisfy a test.

First identify which current workload actually consumes pgvector. If no current application DB uses it, final acceptance should prove:

- the pinned PostgreSQL image is pgvector-capable; and
- the extension works in the designated database used for the platform smoke test.

Template databases are not application acceptance targets.

If a real current consumer requires pgvector in a specific DB, verify that DB explicitly.

## nginx routes

`/firefly/`, `/paperless/`, and `/openproject/` currently exist in nginx config.

Test them as real user surfaces. If an upstream app does not support its subpath correctly, do not create a fake response or brittle rewrite to make the test green. Either configure the product's supported base-path mechanism or remove the unsupported route and retain direct localhost access.

## Anti-facade proof

A mere TCP connect, health endpoint, configured URL, or environment variable is not authenticated product integration proof.

## Acceptance

`STRICT_AUTH=1` must be incapable of returning PASS while any of the three authenticated product checks is skipped.

## Commit boundary

One local verifier commit. No push. STOP.
