# M08 — Persist Reproducible Hermes Connector Definitions

## Goal

Make the proven Firefly, Paperless and OpenProject Hermes integrations reproducible from Git rather than depending on opaque local `/root/.hermes` state or one-off curl commands.

## Depends on

M02 PASS and M04 PASS.

## Required active context

Read only:

- correction control files;
- this module;
- Hermes service section of `ki-basis/compose.yaml`;
- live `/root/.hermes` structure relevant to skills/connectors/config (filenames and non-secret definitions only);
- current official Hermes skill/tool/config loading documentation;
- existing repo conventions for Hermes skills/config that are already canonical;
- H1/H2/H3 evidence from the prior acceptance report only as a claim to reproduce.

Do not load unrelated APEX history or expose secret values.

## Current defect

The previous M8 Git commit persisted only service URLs in Compose. The acceptance report proves authenticated API calls from the Hermes execution context, but Git does not currently demonstrate the durable connector/skill definitions needed to reconstruct those capabilities from a clean clone plus secret provisioning.

## Required distinction

Network reachability is not a connector.

A valid durable connector must define, through the actual supported Hermes mechanism:

- product identity;
- internal base URL contract;
- authentication variable name/reference, never the secret value;
- allowed read operations;
- error/auth failure behavior;
- any write operations and authorization boundary if they already exist;
- enough instructions/schema for Hermes to invoke the real application API.

## Implementation approach

1. inspect current live Hermes connector/skill definitions that produced the accepted H1-H3 calls;
2. determine the current officially supported source-controlled Hermes customization mechanism;
3. persist only non-secret definitions in a canonical repo location;
4. make the Hermes container load/mount/sync those definitions through the supported mechanism;
5. leave real tokens/passwords in ignored local secret state;
6. document exact secret variable names in `.env.example` only as empty/placeholders, without working credentials.

Prefer three small product-specific connector/skill definitions over one generic unrestricted HTTP tool if that matches current Hermes best practice.

## Anti-facade rules

The following do not count:

- host-side curl;
- curl manually executed inside the container;
- a prompt that merely says "call this URL" without durable tool/skill integration;
- direct PostgreSQL reads;
- hard-coded sample responses;
- connector files containing real tokens.

## Verification

Positive:

1. recreate Hermes from the repo-controlled Compose/config plus existing secret state;
2. actual Hermes discovers the three persisted connectors/skills;
3. Firefly authenticated read succeeds;
4. Paperless authenticated read/search succeeds;
5. OpenProject API v3 authenticated read succeeds;
6. repo/workspace mounts and `/opt/data` persistence remain intact.

Negative/adversarial:

- invalid credential for each product must fail;
- temporarily deny/rename one connector definition and prove Hermes no longer claims that product integration;
- grep tracked files for token-like real secrets.

## Acceptance

PASS only when a clean checkout can reconstruct the non-secret Hermes integration layer deterministically and the real Hermes runtime uses it to reach all three actual products.

Persist M08 result including canonical connector paths and discovery proof, update state, commit only Hermes connector/config surfaces, context-reset, continue M09.