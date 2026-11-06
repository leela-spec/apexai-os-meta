---
type: Reference
id: REF-KI-BASIS-RESET-BACKUP-20261104
title: ki-basis reset backup and recovery evidence
description: Verified backup coverage, restore-test results, limitations, and controlled reset procedure for the current WSL stack.
status: current
tags: [ki-basis, backup, recovery]
---

# ki-basis reset backup and recovery evidence

Backup created: `C:\ki-basis-backups\2026-11-04-pre-mac-minimal`.

The directory name identifies the source package being analysed. The preserved environment is the existing x86-64 WSL stack.

The backup preserves the pre-upgrade baseline. Original running and stopped container states were restored after backup. The subsequent authorized application deployment is recorded in [deployment result](05-deployment-result.md).

## Coverage

| Artifact | Contents |
|---|---|
| Ubuntu.tar | WSL Linux filesystem, Docker/containerd storage, images, container definitions and writable layers, named volumes, /root/.hermes, /root/workspaces, Linux configuration and secrets. |
| windows/ki-basis | Windows-hosted private stack source/configuration, including .env.shared-db and nginx mounts. |
| windows/ki-basis-shared | Shared database compose configuration and .env. |
| windows/leela-op178 | Private project-management stack source/configuration and existing backup material. |
| windows/lika-community | Community source/configuration and environment files. |
| windows/.wslconfig and wsl-keepalive.vbs | WSL resource settings and Windows startup helper. |
| windows/openproject-credentials | Existing Windows-hosted credential configuration. |
| databases/globals.sql | PostgreSQL cluster roles and global objects. |
| databases/*.dump | All eight non-template databases, in custom dump format. |
| evidence/ | Container/network/volume inventories, original state, checksums, copy checks, archive coverage, SQL restore results and health results. |

Access control: Backup inheritance is disabled. Explicit full-control entries are Apex\gehma and NT AUTHORITY\SYSTEM. The backup contains secrets; keep it outside repositories and shared folders.

## Consistency and interruption

1. Record all containers, mounts, networks, volumes and the original running set.
2. Copy the Windows-hosted stack trees and configuration.
3. Stop the running application writers and private Valkey.
4. Dump all non-template databases and globals without a pseudo-terminal.
5. Stop PostgreSQL, Docker and containerd; flush filesystem writes.
6. Run native WSL export.
7. Restart engine services, start PostgreSQL, wait for readiness, then start only the other originally running containers.

Quiesce began at 15:29:23 CET on 2026-11-04. The recorded running set was restored at 15:41:19 CET. The interruption window was approximately 11 minutes 56 seconds.

Original running set: ki-basis-hermes, ki-basis-valkey, ki-basis-shared-postgres, leela-op178-openproject. Private Paperless/Firefly/nginx and community containers remained stopped.

## Verification results

| Check | Result | Evidence under backup root |
|---|---|---|
| Native WSL export | Exit 0 | Executor output: operation completed successfully. |
| Export size | 71,206,389,760 bytes | evidence/archive-verification.json |
| Export SHA-256 | e08c1f33baea36a06b27adfe3a5992057e5deae378b631a784b1d74a008ce5c9 | evidence/Ubuntu-sha256.json |
| Tar structural scan | PASS; 1,229,069 members, including 933,404 regular files | evidence/archive-verification.json |
| Required filesystem coverage | /root/.hermes, /root/workspaces, /var/lib/docker, /var/lib/containerd and /etc present | evidence/archive-verification.json |
| Windows copies | 782 files checked; no content mismatches | evidence/windows-copy-verification.json |
| Required Windows settings/env files | All ten selected paths present | evidence/windows-required-files.json |
| SQL dump indexes | All eight readable by pg_restore -l | evidence/*-toc.txt |
| SQL restore rehearsal | All eight restored with exit 0 into a network-isolated temporary PG16 container | evidence/isolated-restore-results.json |
| Production running set | Exact match with recorded baseline | evidence/running-before.json and running-after.json |
| Cache/database health | Both healthy | evidence/services-after-health.json |
| Application HTTP recovery | Project-management health and Hermes dashboard returned 200 | evidence/http-after-health.json |

Isolated restore table counts: comm_firefly 81; comm_openproject 148; comm_paperless 74; ipos_activepieces 81; postgres 0; priv_firefly 81; priv_openproject 212; priv_paperless 74. These are restored table counts, not source-versus-restored row-count comparisons.

The SQL rehearsal used the existing pgvector PG16 image, --network none and temporary in-memory storage. It restored schema/data with --exit-on-error --no-owner --no-privileges. The temporary container was removed afterward.

Reproduction commands for the recorded checks:

```powershell
Get-FileHash -LiteralPath 'C:\ki-basis-backups\2026-11-04-pre-mac-minimal\Ubuntu.tar' -Algorithm SHA256
Get-Content -LiteralPath 'C:\ki-basis-backups\2026-11-04-pre-mac-minimal\evidence\isolated-restore-results.json'
Get-Content -LiteralPath 'C:\ki-basis-backups\2026-11-04-pre-mac-minimal\evidence\archive-verification.json'
```

## Controlled reset procedure

The deployed environment needs no reset. WSL import/restoration is excluded from the execution sequence; scoped recovery is available only if a later deployment fails.

For a later reset after deployment changes:

1. Stop changed application writers and preserve all post-backup data before restoring an older snapshot.
2. Choose a complete WSL recovery or a scoped application recovery. Match database state, application files, keys and image versions.
3. For full recovery, use an isolated/offline recovery workstation or environment. Prevent the Windows keepalive helper and automatic services from launching duplicate agents or binding production ports during preparation.
4. Preserve the existing Windows stack directories under separate names, then restore the four windows/ trees to their original C:\GitDev locations. Restore credentials and host settings to the recorded paths only where needed. Recreate the original mount paths before starting application containers.
5. If deployment fails, recover only the affected private applications using the matching database, files, keys and image versions. WSL import and restoration of the original environment are excluded from the execution sequence.

6. Compare inventories and running-state evidence, check database/cache readiness, and verify the recorded HTTP endpoints. Test accounts, document downloads, attachments and transactions before returning a recovered application to normal use.

For a scoped application reset, restore the original image/configuration, matching private database dump and matching document/upload files from the filesystem snapshot while its writers are stopped. Restore required roles/grants deliberately; do not replay globals over production indiscriminately. Do not restore the entire shared cluster to reset one private application, because that would also rewind other tenants.

WSL import/export semantics are documented in [Microsoft's WSL commands](https://learn.microsoft.com/en-us/windows/wsl/basic-commands#export-a-distribution).

## Verification limits and failure guards

- A complete WSL import-and-boot rehearsal has not been performed. The filesystem archive is structurally checked and hashed; SQL schema/data restoration is tested.
- SQL ownership, grants and globals replay were not exercised in the isolated logical restore. The full filesystem snapshot preserves the original cluster state.
- Application-level restoration of documents/attachments and exact row-count equivalence were not rehearsed. The source application volumes and binds are included in the archive.
- WSL export reported socket-file omissions. The export completed successfully; these runtime socket entries are not ordinary persistent document or database files.
- This is a local reset backup on the same physical Windows drive, not protection against failure or loss of that drive.
- The snapshot predates subsequent normal application writes. Refresh it before a future production migration, and preserve newer writes before any reset.
- Never unregister the original distro, delete production volumes, or boot the recovered agent environment on the production network as an incidental verification step.
