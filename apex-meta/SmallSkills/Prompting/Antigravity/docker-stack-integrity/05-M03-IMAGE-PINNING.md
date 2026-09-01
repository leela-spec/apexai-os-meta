# M03 — Pin Tested Container Images

## Goal

Replace floating image tags with reproducible, tested image references without turning this correction into a broad upgrade campaign.

## Depends on

M02 PASS.

## Required active context

Read only:

- correction control files;
- this module;
- `ki-basis/compose.yaml`;
- live `docker inspect` image metadata for the currently accepted containers;
- current official release/tag documentation only for the seven named images.

Do not load unrelated repo history or old implementation reports.

## Images in scope

- `pgvector/pgvector`
- `valkey/valkey`
- `fireflyiii/core`
- `ghcr.io/paperless-ngx/paperless-ngx`
- `openproject/openproject`
- `nginx`
- `nousresearch/hermes-agent`

## Current defect

The current Compose uses floating/broad tags including `latest`, major-only or minor-only references. This does not meet the prior acceptance requirement for exact tested versions/digests.

## Implementation approach

For each running service:

1. inspect the exact currently running image ID/digest and product version;
2. check current official upstream tag/release conventions;
3. select the narrowest stable reference that reproduces the currently accepted runtime;
4. prefer immutable digest pinning where practical, optionally paired with a readable version tag;
5. do not upgrade to a newer major/minor merely because one exists;
6. record the chosen version/digest in M03 evidence.

If an upstream registry does not expose a stable immutable digest through the installed tooling, pin the exact supported version tag and record the limitation.

## Forbidden behavior

- no `latest` after this module unless upstream technically provides no alternative and the limitation is explicitly proven;
- no silent product upgrade;
- no Alpine rebuild of complex vendor applications;
- no unrelated Compose refactor.

## Verification

Positive:

- `docker compose config` succeeds;
- every service image resolves/pulls;
- recreated services start and pass their existing health/API smoke checks;
- image references in rendered Compose match the intended pins.

Negative/adversarial:

- search rendered Compose and tracked Compose for `:latest` and unapproved broad tags;
- demonstrate that changing a pin to a nonexistent tag/digest causes pull/recreate failure rather than silent fallback.

## Acceptance

PASS when all seven service images are reproducibly pinned to the tested runtime or an explicit evidence-backed exception is recorded.

Persist M03 result with a compact image/version/digest table, update state, commit only image-reference changes, context-reset, continue M04.