# M04 — Make Hermes Port Semantics Truthful Everywhere

## Goal

Resolve the current contradiction about which Hermes port is the dashboard and which is the gateway/API, then make Compose variables, `.env.example`, nginx labels, documentation and acceptance evidence consistent with the real runtime.

## Depends on

M03 PASS.

## Required active context

Read only:

- correction control files;
- this module;
- `ki-basis/compose.yaml`;
- `ki-basis/.env.example`;
- `ki-basis/docker/nginx/default.conf`;
- Hermes-specific section of `apex-meta/Alpine/INTEGRATION-ACCEPTANCE-REPORT.md`;
- live Hermes container listening endpoints/processes;
- current official Hermes Docker/dashboard/gateway documentation if semantics remain ambiguous.

Do not assume the old report or variable names are correct merely because they agree with one another.

## Current defect

Current files disagree about `8642` and `9119`: some label `8642` as dashboard and `9119` as gateway, while prior implementation plans/report prose describe the opposite.

## Required method

Determine semantics from the actual running Hermes product first:

1. inspect listening ports inside the real Hermes container;
2. request both endpoints and identify which product surface each serves;
3. verify against current official Hermes docs;
4. only then patch names/labels/configuration.

Do **not** swap port mappings merely to make prose match. Preserve working host ports unless there is a proven functional reason to change them.

## Scope

Patch only files containing Hermes port variable names, labels, links or acceptance text that are proven inconsistent.

Likely targets:

- `ki-basis/compose.yaml`
- `ki-basis/.env.example`
- `ki-basis/docker/nginx/default.conf`
- Hermes/current architecture or acceptance documentation if necessary

## Verification

Positive:

- each named variable resolves to the service it claims;
- browser/API smoke identifies the correct dashboard/gateway surface;
- nginx index label/link matches actual surface;
- Compose still binds only to `127.0.0.1`.

Negative/adversarial:

- explicitly test the opposite label assumption and show why it is false;
- grep tracked files for stale contradictory port descriptions.

## Acceptance

PASS only when one runtime-proven semantic mapping is consistently represented everywhere in the active configuration/docs.

Persist M04 result including actual endpoint evidence, update state, commit only port-semantic corrections, context-reset, continue M05.