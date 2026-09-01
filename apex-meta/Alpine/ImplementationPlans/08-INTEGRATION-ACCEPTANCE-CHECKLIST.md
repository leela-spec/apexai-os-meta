# Full Stack Integration & Acceptance Checklist

## Construction
- [ ] one Docker Compose project
- [ ] one shared network `ki-basis-net`
- [ ] no fixed container IPs
- [ ] service-name DNS works
- [ ] `.env.example` committed
- [ ] real `.env` ignored
- [ ] `docker compose config` passes

## Images
- [ ] nginx uses justified Alpine path
- [ ] PostgreSQL/pgvector uses supported upstream image
- [ ] Valkey uses official Alpine image
- [ ] Firefly uses official image
- [ ] Paperless uses official image
- [ ] OpenProject uses official image
- [ ] Hermes uses official image
- [ ] exact versions/digests pinned

## Network
From Hermes:
- [ ] `firefly:8080`
- [ ] `paperless:8000`
- [ ] `openproject:80`
- [ ] `nginx:80`

From apps:
- [ ] `postgres:5432`
- [ ] `valkey:6379` where required

## Host exposure
- [ ] Firefly localhost-only port
- [ ] Paperless localhost-only port
- [ ] OpenProject localhost-only port
- [ ] Hermes `9119` localhost-only
- [ ] Hermes `8642` localhost-only
- [ ] nginx localhost-only
- [ ] PostgreSQL not exposed
- [ ] Valkey not exposed

## Data
- [ ] separate DB/user per app
- [ ] persistent volumes exist
- [ ] full stack restart loses no data
- [ ] container recreation loses no data

## App tests
- [ ] Firefly UI + read API
- [ ] Paperless UI + test PDF OCR + API search
- [ ] OpenProject UI + test work package + API v3
- [ ] OpenProject health checks

## Hermes
- [ ] `/opt/data` persists
- [ ] dashboard works
- [ ] Firefly connector
- [ ] Paperless connector
- [ ] OpenProject connector
- [ ] no Docker socket
- [ ] existing repo/workspace access unchanged

## Backup
- [ ] PostgreSQL dumps
- [ ] application-volume backups
- [ ] Hermes `/opt/data` backup
- [ ] one restore test

## Operator experience
- [ ] Homepage links use intended ports
- [ ] every app opens
- [ ] Hermes can inspect supported app data
- [ ] stack restarts predictably
- [ ] one tool can be upgraded independently
