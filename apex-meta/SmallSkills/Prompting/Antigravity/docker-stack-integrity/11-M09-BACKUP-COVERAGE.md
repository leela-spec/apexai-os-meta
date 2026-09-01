# M09 — Complete Backup Coverage for All Stateful Data

## Goal

Turn the prior partial backup proof into a reproducible backup procedure that covers every stateful component required to rebuild the accepted stack.

## Depends on

M07 PASS and M08 PASS.

## Required active context

Read only:

- correction control files;
- this module;
- `ki-basis/compose.yaml` volume/mount definitions;
- live `docker volume inspect` / mount state for the named stack volumes;
- existing backup artifacts/scripts if any;
- current official backup guidance only for Firefly, Paperless, OpenProject, PostgreSQL and Hermes state where product-specific consistency matters.

Do not load unrelated implementation plans.

## Current defect

The prior report proves PostgreSQL dumps and a Hermes state archive, but does not prove durable backups for all application filesystem data such as Firefly uploads, Paperless media/data/export/consume, and OpenProject assets.

## Required backup inventory

At minimum account for:

- PostgreSQL databases: `firefly`, `paperless`, `openproject` plus required roles/ownership metadata;
- Firefly persisted upload/storage data actually mounted by the current image;
- Paperless `data`, `media`, `export`, `consume` volumes where they contain required state;
- OpenProject persistent assets/attachments path(s) proven by M07;
- Hermes `/opt/data` or the approved persistent state path;
- repo-controlled stack configuration, excluding real secrets.

If one listed volume is demonstrably cache/transient and need not be backed up, document the upstream/runtime reason rather than archiving it blindly.

## Implementation

Create or patch a deterministic backup mechanism, preferably repo-controlled under `ki-basis/scripts/` if no canonical backup tool already exists.

Requirements:

- timestamped backup destination outside live volumes;
- no plaintext secret dump into Git;
- fail on command errors;
- database dumps use consistent supported PostgreSQL tooling;
- application volume backup must preserve file metadata needed by the app;
- output manifest records artifact path, source, size and full checksum;
- script must be safe to rerun without overwriting unrelated backups.

If a product requires quiescing/maintenance mode for a consistent file backup, follow current official guidance and keep downtime bounded.

## Verification

Positive:

1. run the actual backup procedure against the live stack;
2. confirm one artifact per required state source;
3. compute full SHA-256 checksums;
4. inspect archive listings/DB dump headers without exposing secrets;
5. confirm backup destination is not a live application volume.

Negative/adversarial:

- deliberately make one disposable backup target unwritable/missing and prove the procedure fails non-zero rather than reporting success;
- compare Compose named volumes against the backup manifest and fail on any unexplained stateful omission.

## Acceptance

PASS only when every required persistent data source is either backed up or explicitly proven non-required, and the backup procedure itself is reproducible from the repo.

Persist M09 result with the backup coverage matrix and checksum manifest path, update state, commit only backup tooling/docs/evidence, context-reset, continue M10.