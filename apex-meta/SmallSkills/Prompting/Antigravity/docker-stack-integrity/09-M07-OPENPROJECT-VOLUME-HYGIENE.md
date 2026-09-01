# M07 — OpenProject Volume Hygiene

## Goal

Resolve the declared-but-unused `openproject_data` volume without risking OpenProject data loss.

## Depends on

M03 PASS.

## Required active context

Read only:

- correction control files;
- this module;
- OpenProject service + volume sections of `ki-basis/compose.yaml`;
- live OpenProject container mounts;
- current official OpenProject Docker persistence documentation for the exact pinned image/runtime.

Do not load unrelated service plans.

## Current defect

`openproject_data` is declared as a named volume but is not mounted by the current OpenProject service. `openproject_assets` is mounted at `/var/openproject/assets`.

## Required method

Do not assume the unused declaration is safe to remove until live runtime and current upstream persistence requirements are checked.

1. inspect actual OpenProject mounts and writable persistence paths;
2. confirm the external PostgreSQL DB owns database state;
3. verify which filesystem path(s) the pinned OpenProject image requires for durable attachments/assets;
4. determine whether `openproject_data` is dead configuration or a missing mount.

## Implementation

Choose exactly one evidence-backed correction:

- remove `openproject_data` if it is truly unused and unnecessary; or
- wire it to the upstream-required persistent path if the current configuration is missing real state persistence.

Do not create a new persistence topology that upstream does not document.

## Verification

Positive:

- `docker compose config` succeeds;
- live OpenProject starts after recreate;
- existing test project/work package remains available;
- attachments/assets persistence path is correct for the pinned image.

Negative/adversarial:

- search rendered Compose for orphaned OpenProject volumes;
- if removing `openproject_data`, prove no live container uses that volume;
- if mounting it, create a disposable non-sensitive persistence proof and verify it survives recreate.

## Acceptance

PASS when every declared OpenProject volume has a real documented consumer and required application state survives recreate.

Persist M07 result, update state, commit only OpenProject volume/config changes, context-reset, continue M08.