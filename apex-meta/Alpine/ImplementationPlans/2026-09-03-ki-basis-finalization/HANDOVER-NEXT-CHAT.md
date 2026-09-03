# Handover — Continue ki-basis Finalization

## Current target

The Docker migration is accepted at the architecture layer:

Windows 11 -> Docker Desktop Hyper-V Linux backend -> one `ki-basis` Compose project -> `ki-basis-net` -> seven services (Postgres/pgvector, Valkey, Firefly, Paperless, OpenProject, nginx, Hermes). Legacy Ubuntu WSL is rollback-only and should remain stopped.

At plan-authoring time, GitHub `main` was `b9d7a77c1b84aaed99093e42cea32a7d51c56f26`. Verify live before using this as authority.

## Important outstanding issue

The rotated Paperless token was exposed again in `apex-meta/Alpine/HANDOVER-REVIEWER-DOSSIER.md`, which is on GitHub main. It must be revoked again and the dossier sanitized. Never request the replacement value in chat.

## Main next capability

Turn Hermes into the real AI control surface. The recommended implementation is **local Hermes CLI + three version-controlled skills + supported internal product APIs + app-specific revocable credentials**.

Do not give Hermes the Docker socket or direct DB mutation ability just to avoid API tokens.

OpenRouter is a Hermes model provider, not a Docker service. Configure it through Hermes' interactive `hermes model` flow; store the key only in Hermes persistent `/opt/data/.env`.

For app credentials, each skill should declare `required_environment_variables`; the user enters secrets through the local Hermes CLI secure setup, which stores them in Hermes `.env` without exposing the raw value to the model.

Recommended skill source:

`ki-basis/hermes-skills/{paperless-local,firefly-local,openproject-local}/`

Configure Hermes `skills.external_dirs` to the target-local repo copy and turn `skills.write_approval: true` on.

Start skills read-only. Writes are a later explicit module.

## Program files

Read `plans/00-START-HERE.md`, then execute one module at a time.

Highest-value sequence:

1. M01 token rotation/sanitization.
2. M02 backup fail-close hardening.
3. M03 independent restore checksum.
4. Apply M06 documentation patch.
5. Apply M08 deferred-performance note.
6. M05 OpenRouter + Hermes skills with operator interaction.
7. M04 strict final product auth/topology verification.
8. M07 Windows reboot + second-copy backup.
9. M09 independent final closure.

## Key research conclusions

- Hermes officially recommends Skills for workflows that wrap external APIs/CLIs using terminal/scripts.
- Skills can declare required environment variables; local CLI securely prompts and saves them while hiding raw values from the model.
- Hermes in Docker persists all user state under `/opt/data`.
- `skills.external_dirs` supports version-controlled external skill trees.
- `skills.write_approval: true` stages skill changes for operator review.
- OpenRouter is natively supported by Hermes via `OPENROUTER_API_KEY`; no separate Docker service is needed.
- OpenProject MCP is a future candidate only: current official MCP arrived in OpenProject 17.2 and is an Enterprise add-on; current stack is pinned to OpenProject 14. Do not upgrade solely for MCP now.
- Local CLI operation does not remove app authentication. Tokens are lower privilege than giving the agent Docker-host access.
- Current backup shape is not overengineering; fail-open archive behavior is the defect. Full multi-app restore automation would be overengineering at current scale.
- Do not apply speculative container/worker/Valkey/Postgres tuning without measured bottlenecks.

## Execution style

Use Antigravity `/teamwork-preview` in DEVELOPMENT mode. Follow repository Antigravity prompting guidance. One module -> real proof -> adversarial test -> local commit -> STOP/reset. No push unless operator explicitly asks.
