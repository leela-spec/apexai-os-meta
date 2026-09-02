# Docker Tool Stack — Antigravity START HERE

Repository: `leela-spec/apexai-os-meta`
Branch: `main`
Executor: Google Antigravity

## Purpose

This folder adapts the Docker stack implementation plans to the proven Antigravity operating doctrine already stored in this repository.

Before any stack work, read in this order:

1. `../../SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/SKILL.md`
2. `../../SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/references/lessons-learned.md`
3. `../../SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/references/prompt-patterns.md`
4. `01-META-IMPLEMENTATION-PLAN-ANTIGRAVITY.md`
5. exactly one active tool/module plan from this folder

Do not load all tool plans into the active implementation context unless the current module explicitly needs them.

## Target

One Docker Compose stack with one shared internal Docker network connecting these logical tools:

- nginx
- PostgreSQL + pgvector
- Valkey
- Firefly III
- Paperless-ngx
- OpenProject
- Hermes

Hermes is the AI operating surface. Firefly, Paperless and OpenProject are controlled through their supported APIs over the internal Docker network.

## Interpretation rules

- One logical tool does not always mean exactly one physical container. Preserve upstream-required workers, cron helpers, caches or process containers when the actual product requires them.
- Alpine is not mandatory for every image. Use Alpine only where the actual upstream product supports it well or where an existing justified Alpine image already exists.
- Do not invent local facades for named products.
- Do not mount the Docker socket into Hermes in the initial implementation.
- Do not expose PostgreSQL or Valkey to the host unless a later explicit requirement demands it.
- Use Docker service names for internal communication; never fixed container IPs.

## Program law

`PREFLIGHT -> ONE MODULE -> IMPLEMENT -> TEST -> ADVERSARIAL VERIFY -> COMMIT -> STOP/NEXT AUTHORIZATION`

The first run is M0 inventory/preflight only. It must not mutate the Docker environment.

## Module order

1. M0/M1: `01-META-IMPLEMENTATION-PLAN-ANTIGRAVITY.md`
2. PostgreSQL/pgvector: `03-POSTGRES-PGVECTOR-ANTIGRAVITY.md`
3. Valkey: `04-VALKEY-ANTIGRAVITY.md`
4. Firefly: `05-FIREFLY-ANTIGRAVITY.md`
5. Paperless: `06-PAPERLESS-NGX-ANTIGRAVITY.md`
6. OpenProject: `07-OPENPROJECT-ANTIGRAVITY.md`
7. nginx: `02-NGINX-ANTIGRAVITY.md`
8. Hermes: `08-HERMES-ANTIGRAVITY.md`
9. Full integration: `09-INTEGRATION-ACCEPTANCE-ANTIGRAVITY.md`

STOP after M0 and return the observed machine/repository state before implementing any service.