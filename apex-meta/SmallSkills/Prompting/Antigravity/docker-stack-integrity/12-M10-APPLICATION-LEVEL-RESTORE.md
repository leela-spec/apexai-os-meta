# M10 — Prove Restore Through the Actual Application Interface

## Goal

Close the restore-proof gap by restoring real application state into a disposable target and verifying the restored object through the actual product interface/API, not only through direct SQL inspection.

## Depends on

M09 PASS.

## Required active context

Read only:

- correction control files;
- this module;
- M09 backup coverage result and manifest;
- current Paperless backup artifact selected for the restore proof;
- Paperless service/dependency sections of `ki-basis/compose.yaml`;
- current official Paperless restore/backup documentation as needed.

Do not load Firefly/OpenProject backup details unless Paperless cannot provide a safe disposable restore proof.

## Current defect

The prior acceptance report restored a Paperless SQL dump into a disposable database and verified data with direct SQL. The integration plan required verification through the actual application interface.

## Default proof target

Use Paperless because a known non-sensitive test document already exists and the product exposes a REST API.

If live state no longer contains a suitable non-sensitive proof object, create a fresh disposable test document before backup and record its identifier/checksum.

## Restore design

Use a disposable restore target that cannot corrupt the live stack. Acceptable patterns include:

- temporary Paperless service + disposable restored database + disposable copied media/data volumes on an isolated Compose project/network; or
- another officially supported isolated restore arrangement with equivalent separation.

Do not restore over the live production-like Paperless DB/volumes merely to prove the test.

The restore must include every data component needed for the chosen proof object, not just the database if the file/media content lives in a volume.

## Verification

Positive:

1. restore the backed-up Paperless DB and required filesystem data into the disposable environment;
2. start the actual Paperless application against the restored state;
3. authenticate through Paperless's real supported API/UI;
4. retrieve the restored document by ID/search;
5. verify title/metadata and content/checksum against the pre-backup fixture;
6. if feasible, download/read the restored document through Paperless itself.

Negative/adversarial:

- omit or point the disposable app at an intentionally empty media volume and prove the application-level verification detects the missing file/content;
- invalid API token must still fail;
- confirm no live stack volume/database was modified by the restore exercise.

## Cleanup

After evidence is captured, remove only the disposable restore environment. Do not delete backup artifacts needed for future recovery.

## Acceptance

PASS only when restored data is proven through the actual running Paperless interface/API and the live stack remains untouched.

Persist M10 result with disposable target identity, restored object identity and API-level evidence, update state, commit only restore tooling/docs/evidence, context-reset, continue M11.