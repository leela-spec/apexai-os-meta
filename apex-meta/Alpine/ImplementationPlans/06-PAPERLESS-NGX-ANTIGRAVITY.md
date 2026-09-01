# Paperless-ngx — Antigravity Implementation Module

## Target

Run actual Paperless-ngx in the shared Docker stack with shared PostgreSQL + Valkey, persistent document storage, OCR ingestion, and one dedicated Homepage port.

## Real target

Actual Paperless-ngx must run. A local document indexer, OCR script, fake REST API or generated Markdown inventory does not count.

## Image

Use a pinned official `ghcr.io/paperless-ngx/paperless-ngx:<version>` image. Do not rebuild Paperless on Alpine; its Python/OCR/native stack is exactly the kind of workload for which forced musl migration adds unnecessary risk.

## Network

Service name: `paperless`
Internal port: `8000`
Host mapping: verified M0 Homepage port -> `8000`, bound to `127.0.0.1`.

Dependencies:
- PostgreSQL: `postgres:5432`
- Valkey: `valkey:6379`

## Persistence

Preserve upstream-required paths for:
- data;
- media;
- export;
- consume.

Do not store documents only in the ephemeral container layer.

## Configuration

Use the dedicated `paperless` DB/user from the shared PostgreSQL service.
Set timezone deliberately (`Europe/Berlin`).
Add only OCR languages actually required by operator documents.

## Human gate

If initial superuser creation or browser login requires operator input, prepare exact command/path/URL first and request only the smallest action.

## Proof

1. actual Paperless web UI loads;
2. actual Paperless connects to `postgres` and `valkey`;
3. create/secure initial user;
4. ingest one non-sensitive test PDF through Paperless's supported consume/upload path;
5. OCR task completes;
6. document becomes searchable in Paperless;
7. restart/recreate Paperless;
8. document remains;
9. dedicated API token performs actual authenticated search/list request;
10. invalid token is rejected.

## Forbidden substitutes

- direct DB insertion as Paperless ingestion proof;
- OCR output alone presented as Paperless success;
- local fake API;
- using host-mapped DB/cache ports internally;
- deleting current Paperless media/data without explicit migration approval.

## Acceptance

PASS only when actual Paperless UI, OCR ingestion, persistence and authenticated API search all work against the real running product.

Commit only Paperless-scoped changes and STOP.