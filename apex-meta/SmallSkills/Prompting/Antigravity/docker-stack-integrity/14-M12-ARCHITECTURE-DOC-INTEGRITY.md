# M12 — Reconcile Architecture Documentation with Implemented Truth

## Goal

Make the architecture documentation truthful about the stack that actually exists after M01-M11, without erasing useful historical design input.

## Depends on

M01-M11 PASS.

## Required active context

Read only:

- correction control files;
- this module;
- current `ki-basis/compose.yaml` after M01-M11;
- current `ki-basis/.env.example` only for public/non-secret port/service names;
- current nginx config only for operator-facing routes;
- `apex-meta/Alpine/ARCHITEKTUR-BASIS.md`;
- final result summaries for M03, M04, M07, M08, M11;
- current implementation-plan canonical manifest from M06.

Do not load all prior implementation history or old chat context.

## Current defect

`ARCHITEKTUR-BASIS.md` currently presents an older platform containing services such as AnythingLLM, Psono, Authentik, Envoy, oMLX, Ollama and Speaches as though it were the active stack, while the implemented `ki-basis` stack now centers on PostgreSQL/pgvector, Valkey, Firefly, Paperless, OpenProject, nginx and Hermes.

## Required decision

First determine what `ARCHITEKTUR-BASIS.md` is supposed to be:

- current canonical architecture; or
- historical/source input retained for provenance.

Use repository references and file framing to decide. Do not silently repurpose a historical document if other files still depend on it as source evidence.

## Preferred correction

If the file is meant to be current authority:

- minimally patch it to describe the real implemented stack, current service boundaries, internal Docker DNS, host-facing ports, persistence and Hermes API-control role;
- remove or explicitly mark unimplemented legacy services as future/historical rather than active.

If the file is historical/source input:

- add an unmistakable status banner such as `HISTORICAL INPUT / SUPERSEDED FOR CURRENT RUNTIME`;
- create one concise current architecture document in `apex-meta/Alpine/` that points to `ki-basis/compose.yaml` as runtime authority;
- link both directions so future agents cannot confuse them.

## Required current architecture facts

Document only facts supported by current Git/runtime:

- one Compose project / shared bridge network;
- actual service names;
- internal service addresses;
- localhost-only human-facing ports after M04;
- PostgreSQL and Valkey internal-only;
- actual persistent volumes/mounts after M07;
- Hermes as AI operating surface using durable connectors from M08;
- nginx routes actually retained after M11;
- Alpine used only where the actual image choice warrants it.

Do not claim future services or MCP integrations as current unless runtime evidence proves them.

## Verification

Positive:

- compare every service/port/volume in the current architecture doc against rendered Compose and accepted module results;
- all links resolve;
- historical vs current authority is explicit.

Negative/adversarial:

- search the current-architecture path for active claims about services absent from Compose/runtime;
- ask a fresh verifier to identify which file is current architecture authority without extra explanation. Ambiguity is failure.

## Acceptance

PASS when future agents can distinguish historical input from current runtime architecture and all current claims match the implemented stack.

Persist M12 result with the final authority map, update state, commit only architecture/status/link documentation, context-reset, continue M13.