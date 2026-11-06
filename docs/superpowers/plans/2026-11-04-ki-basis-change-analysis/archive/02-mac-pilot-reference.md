---
type: Plan
id: PLAN-KI-BASIS-MAC-PILOT-20261104
title: ki-basis isolated Mac pilot and migration plan
description: Ordered installation, compatibility, acceptance, and reset steps for the supplied Mac package without replacing shared WSL infrastructure.
status: proposed
tags: [ki-basis, migration, planning]
---

# ki-basis isolated Mac pilot implementation plan

> For agentic workers: Use the executing-plans skill to implement this plan task by task after implementation is authorized.

Goal: Validate the supplied Paperless/Firefly package on an isolated Apple Silicon Mac and establish whether existing private data can migrate safely.

Architecture: Preserve the existing WSL engine and shared PG16 cluster. Install an independent Mac project with separate source directories, credentials, ports and volumes. Migrate copies before considering any cutover.

Tech stack: Docker Compose, ParadeDB PG18, Valkey, custom Paperless/Firefly builds, nginx, Tika, Gotenberg and Stirling.

## Global constraints

- Installation and migration are proposed work, not completed or authorized by this analysis.
- Use an independent --dest and --data-root.
- Preserve source application encryption keys when transferring existing databases.
- Do not change community, Hermes, project-management, or other shared-cluster databases to deploy this narrower package.
- Do not delete production containers, volumes, source data, or the reset backup.
- Keep optional Zettelrobbe disabled until its missing dependencies have a separate acceptance case.

## Decision before implementation

| Choice | Mechanism and grounding | Raw I/E/R estimates, 1–100 | Assessment |
|---|---|---|---|
| Separate Mac pilot | Execute the supplied native Mac path with independent storage; matches INSTALL.md and explicit arm64 declarations. | I90/E75/R20 | Recommended. It tests the delivered product while preserving the current environment. |
| Port selected features into WSL | Adapt platform/build settings, shared-database wiring, storage and lifecycle; do not execute install-mac.sh. | I75/E40/R60 | Defer: a separate integration design is needed before production changes. |
| Replace the whole existing stack | Retire services absent from the package and change the shared database architecture. | I25/E20/R90 | Reject for this scope: package functionality does not cover the current stack. |

I estimates outcome value; E estimates ease of execution; R estimates disruption/data risk. These are engineering judgments, not measured results.

The operator must identify the actual Mac and choose fresh installation versus transfer of existing private application data. These choices do not block the completed analysis or source backup.

## Task 1: Establish target readiness

Files read: package REQUIREMENTS.txt, FETCH.txt, images.lock, MANIFEST.txt and INSTALL.md.

- [ ] Confirm Apple Silicon, macOS version, installed Docker version, available memory and disk.
- [ ] Verify the supplied zip hash, if using the original zip: 4ba7f934f4b901dd42b261c46fbd5d794ebae12f1f92922ea0be666c29f3d49b.
- [ ] Inspect listeners on 8012, 8081, 8082 and 8087.
- [ ] Confirm destination and data-root are new dedicated directories.
- [ ] Confirm the reset backup passes the checks in [backup and reset](03-backup-and-reset.md).

Deliverable: A named target host, available resources and conflict-free destination. Stop if the target is the current Windows host; select the WSL-port route instead.

## Task 2: Install the isolated fresh pilot

Files created on the Mac: ~/ki-mac-minimal/{ki-basis,paperless-stack,firefly-stack,zettelrobbe}; profile .env; ~/ki-mac-minimal-data/ki-mac-minimal bind directories; Docker-managed named volumes.

Run on the selected Mac from the unpacked package:

```bash
umask 077
touch ~/ki-mac-minimal-install.log
chmod 600 ~/ki-mac-minimal-install.log
set -o pipefail
BUILDKIT_PROGRESS=plain bash firstparty/ki-basis/docker/scripts/install-mac.sh \
  --from "$PWD" --profile paperless-firefly \
  --dest ~/ki-mac-minimal --data-root ~/ki-mac-minimal-data \
  2>&1 | tee ~/ki-mac-minimal-install.log
```

- [ ] Save generated credentials in the password manager.
- [ ] Render the effective compose configuration and inspect ports, mounts, platform and image references.
- [ ] Check every default service reaches its expected running/healthy state; preserve logs for failures.
- [ ] Create the first Paperless account using docker exec -it kmm-paperless python3 manage.py createsuperuser.
- [ ] Create the first Firefly account only for a fresh pilot.
- [ ] Remove the generated-secret section before sharing installation logs.

Deliverable: A working empty pilot with no production data changes.

## Task 3: Establish application compatibility before copying data

Files read: source image metadata/version output, source database extension inventory, target Dockerfiles, application migration definitions and effective compose configuration.

- [ ] Compare exact source Paperless/Firefly versions against target builds; reject unsupported downgrades.
- [ ] Inventory extensions, roles, ownership and encoding in priv_paperless and priv_firefly.
- [ ] Confirm target PG18 supports required extensions and application migrations.
- [ ] Select and document database-to-role mapping: priv_paperless to paperless; priv_firefly to firefly.
- [ ] Preserve the source Firefly APP_KEY and Paperless secret key in the migration environment; rotate database passwords separately.
- [ ] Record application row counts, document/file counts and sample records while the final source writers are stopped.

Deliverable: A tested mapping and supported version path. Do not infer compatibility from a successful empty installation.

## Task 4: Rehearse migration of copies

Files consumed: priv_paperless.dump, priv_firefly.dump, source Paperless data/media/export/consume directories, Firefly upload files, and source application keys from the protected backup.

- [ ] Stop pilot application writers and cron before importing.
- [ ] Restore logical databases into the target application's databases with explicit ownership/grant mapping.
- [ ] Copy Paperless files to the corresponding bind directories with target-compatible ownership.
- [ ] Restore Firefly uploads into ki-mac-minimal-firefly-upload.
- [ ] Apply supported application migrations and start pilot applications.
- [ ] Compare captured counts and representative original documents, archived documents, attachments and transactions.
- [ ] Confirm source accounts work; do not create replacement administrators to hide failed account migration.

Deliverable: An accepted migration rehearsal. The PG16 physical data volume remains on the source engine.

## Task 5: Exercise the delivered product

- [ ] Open the four homepage tiles at http://127.0.0.1:8082/.
- [ ] Import a representative rotated scan and a German/English document; check extraction, orientation and barcode/ASN handling.
- [ ] Print an ASN label through the browser and scan it back through the document workflow.
- [ ] Create a Firefly transaction with an attachment and inspect DATEV output.
- [ ] Verify the cron endpoint using the protected configured token and inspect execution logs.
- [ ] Exercise Stirling with representative PDFs under the permitted usage terms.
- [ ] Measure idle and document-processing memory, CPU and disk consumption.
- [ ] Restart the Mac pilot and verify data persists in both bind mounts and named volumes.

Deliverable: Recorded functional results and resource measurements, with failures resolved before cutover.

## Task 6: Cut over only after acceptance

- [ ] Refresh the source backup after stopping final application writers.
- [ ] Repeat the rehearsed data transfer and checks.
- [ ] Update approved bookmarks and integrations to the selected target URLs.
- [ ] Keep the old private applications stopped and the preserved shared infrastructure available.
- [ ] Back up the Mac profile secrets, source/configuration, Paperless binds and all three named data volumes.
- [ ] Demonstrate recovery into an isolated environment before treating the new backup process as accepted.

Reset: Stop target writers, preserve target-only writes, and resume the source application set with original source data and keys. Use the filesystem reset only if the original environment was modified. Never discard target-only writes silently.

Failure guard: Abort cutover on missing documents, incompatible migrations, failed key-based decryption, or an unverified reset path.
