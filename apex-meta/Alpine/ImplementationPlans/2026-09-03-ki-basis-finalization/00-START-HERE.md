# ki-basis Finalization Program — START HERE

**Date:** 2026-09-03  
**Repository:** `C:\GitDev\apexai-os-meta`  
**Branch:** `main`  
**Expected remote baseline when this plan was authored:** `b9d7a77c1b84aaed99093e42cea32a7d51c56f26` — verify live before execution.  
**Execution environment:** Google Antigravity, Teamwork `/teamwork-preview`, **DEVELOPMENT** integrity mode.

## Accepted architecture — do not reopen

Windows 11 -> Docker Desktop -> Hyper-V Linux backend -> one Docker Engine -> one Compose project `ki-basis` -> one bridge `ki-basis-net` -> PostgreSQL/pgvector, Valkey, Firefly III, Paperless-ngx, OpenProject, nginx, Hermes.

The legacy Ubuntu WSL Docker runtime is a cold rollback source only. Do not restart or redesign it unless a rollback is explicitly needed.

## Program purpose

Close the remaining security/evidence defects, then turn Hermes from a container that can reach the applications into the actual operator-facing AI control surface for the stack.

This is **not** another architecture migration.

## Current execution authority — one reasoning/routing logic

No earlier patch bundle from this chat has been applied. This program therefore defines the single current path directly from the existing baseline.

The final application skill sets will be supplied later.

Current canonical control path:

`heavy-reasoning CLI agent -> Hermes local API -> Hermes routing/skills -> product APIs`

Do not create a parallel permanent path where CLI agents independently implement Firefly/Paperless/OpenProject business logic.

Read before further execution:

1. `04A-DOCKER-BACKGROUND-RUNTIME.md`
2. `05A-CLI-REASONING-HERMES-ROUTING.md`

OpenRouter is intentionally configured as a Hermes routing/execution provider, while the upstream CLI agent may use its own model/provider for heavy reasoning.

Important: the upstream CLI agent does not literally replace Hermes' own inference model. Hermes still runs its own AIAgent for routing/tool execution.

The full product skill/bundle implementation in `05-HERMES-AI-CONTROL-STACK.md` is deferred until the real skill set is available.

## Antigravity authority

Before any module, read:

1. `apex-meta/SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/SKILL.md`
2. `apex-meta/SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/references/lessons-learned.md`
3. `apex-meta/SmallSkills/Prompting/Antigravity/antigravity-instruction-orchestrator/references/prompt-patterns.md`
4. this file
5. exactly one active module file

Do not load every module into the active implementation context.

## Execution law

For every module:

`LIVE PREFLIGHT -> PLAN -> PATCH/CONFIGURE -> REAL PRODUCT TEST -> ADVERSARIAL TEST -> EVIDENCE -> LOCAL COMMIT -> STOP/RESET`

Rules:

- One module at a time.
- Preserve accepted architecture unless the active module explicitly says otherwise.
- Use official current product documentation before install/auth/config commands.
- Product participation must be real; local facades do not count.
- Secrets are never pasted into Antigravity chat, Git, reports, command arguments, screenshots, or evidence.
- Operator-only secret/UI actions are `BLOCKED_HUMAN_GATE`; prepare everything first, then request the smallest exact action.
- No push unless the operator explicitly authorizes it.
- Do not reset/stash/commit unrelated work.
- Prefer bounded patches over full-file rewrites.

## Current state and remaining order

Already completed and retained:

1. M01 security / secret sanitation.
2. M02 backup fail-close hardening.
3. M03 independent Paperless restore SHA oracle.
4. M04 strict application-auth / topology verification.
5. M08 evidence-gated performance deferral.

Execute now:

1. `04A-DOCKER-BACKGROUND-RUNTIME.md`
2. `05A-CLI-REASONING-HERMES-ROUTING.md`
3. M06 only for concrete documentation/provenance updates created by this correction.
4. M07 lifecycle proof against the background runtime + Hermes bridge.
5. M09 independent closure of this bridge/platform phase.

Defer until the real skill set arrives:

- Firefly/Paperless/OpenProject Hermes skill implementation;
- `ki-basis-control` bundle;
- cross-application skill orchestration;
- selected write workflows.

Do not rerun M01-M04 for ceremony. Do not create placeholder skills or a direct-product CLI-agent architecture.

## Required status vocabulary

Return exactly one per module:

- `PASS`
- `PASS_WITH_LIMITATIONS`
- `CORRECTION_REQUIRED`
- `BLOCKED_HUMAN_GATE`
- `FAIL`

A generated report is not proof of its own PASS state.

## Research basis

Primary references used to design this program:

- Hermes Skills: https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/
- Hermes skill authoring: https://hermes-agent.nousresearch.com/docs/developer-guide/creating-skills
- Hermes Docker persistence: https://hermes-agent.nousresearch.com/docs/user-guide/docker
- Hermes security/approvals: https://hermes-agent.nousresearch.com/docs/user-guide/security
- Hermes providers: https://hermes-agent.nousresearch.com/docs/integrations/providers
- Docker Compose secrets: https://docs.docker.com/compose/how-tos/use-secrets/
- Docker volumes backup/restore: https://docs.docker.com/engine/storage/volumes/
- PostgreSQL logical backup: https://www.postgresql.org/docs/current/backup-dump.html
- Paperless API auth: https://docs.paperless-ngx.com/api/
- OpenProject API auth: https://www.openproject.org/docs/api/introduction/
- OpenProject MCP: https://www.openproject.org/docs/system-admin-guide/integrations/mcp-server/
- Firefly Data Importer CLI: https://docs.firefly-iii.org/how-to/data-importer/advanced/cli/
- OpenRouter privacy/routing: https://openrouter.ai/docs/guides/privacy/provider-logging and https://openrouter.ai/docs/guides/routing/provider-selection
