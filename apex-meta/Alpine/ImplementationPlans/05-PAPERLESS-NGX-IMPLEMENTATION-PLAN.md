# Paperless-ngx Implementation Plan

## Purpose
Document ingestion, OCR, classification and search.

## Image
Use official `ghcr.io/paperless-ngx/paperless-ngx:<version>`. Do not rebuild Paperless on Alpine.

## Network
Service: `paperless`
Internal port: `8000`
Network: `ki-basis-net`

Host mapping: `127.0.0.1:<PAPERLESS_HOST_PORT>:8000`

## PostgreSQL
Use shared Postgres:
- `PAPERLESS_DBENGINE=postgresql`
- `PAPERLESS_DBHOST=postgres`
- `PAPERLESS_DBPORT=5432`
- DB `paperless`
- user `paperless_app`

## Valkey
`PAPERLESS_REDIS=redis://valkey:6379` plus credentials if enabled.

## Persistence
- `paperless_data`
- `paperless_media`
- `paperless_export`
- `paperless_consume`

## Localization
Set `PAPERLESS_TIME_ZONE=Europe/Berlin`. Add only actually needed OCR language packs.

## Validation
1. UI loads;
2. Postgres connects;
3. Valkey connects;
4. create superuser;
5. upload one non-sensitive test PDF;
6. OCR/consumption completes;
7. document is searchable;
8. restart stack;
9. document remains;
10. API token can list/search documents.

## Hermes
Internal URL: `http://paperless:8000`

Use Paperless token auth. Start with search/read/list operations. Add upload/tag/edit later. Deletion/bulk changes stay separately authorized.

## Acceptance
UI, OCR, persistence and Hermes API search all pass.
