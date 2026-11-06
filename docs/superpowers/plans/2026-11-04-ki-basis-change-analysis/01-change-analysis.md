---
type: Reference
id: REF-KI-BASIS-CHANGE-ANALYSIS-20261104
title: ki-basis laptop package change analysis
description: Evidence-based comparison of the existing WSL stack with the supplied paperless-firefly Mac package.
status: current
tags: [ki-basis, architecture, migration]
---

# ki-basis laptop package change analysis

The target is the operator's existing x86-64 Windows/WSL stack. The supplied package is a Mac/ARM source package; its applications need linux/amd64 builds and integration with the existing infrastructure. Its installer does not upgrade, copy, or migrate the existing stack automatically.

This comparison records the pre-upgrade baseline and supplied package examined on 2026-11-04. The authorized x86-64 integration is deployed; current operation and evidence are in the [deployment result](05-deployment-result.md).

## Current and proposed state

| Area | Existing stack | Supplied package | Consequence |
|---|---|---|---|
| Host | Ubuntu WSL2, native Docker 29.1.3, Compose 2.40.3 | macOS host prerequisites; services explicitly linux/arm64 | The installer is unsuitable for direct execution against this Windows stack. |
| Engine | One native Docker daemon | Installs/starts Docker Desktop through Mac host helpers | A Mac pilot adds a separate engine; it does not replace the WSL engine. |
| Scope | Private tools, Hermes, community tools, shared database, private project-management service | Paperless, Firefly, cron, Stirling, homepage/ASN, PostgreSQL, Valkey, Tika, Gotenberg | The package is a narrower product, not a full replacement for the current environment. |
| Database | Shared pgvector PostgreSQL 16 with eight non-template databases | Dedicated ParadeDB v0.26.2-pg18 with paperless/firefly databases | Existing files cannot simply become the PG18 data directory. A data migration requires logical transfer and compatibility checks. |
| Isolation | priv_* and comm_* roles/databases; shared-db-net | ki-mac-minimal project/network and kmm-* containers | Keep the existing shared cluster and tenant boundaries intact. |
| Paperless | Version 3.1.2 from live image metadata; port 8010; named data/media/export/consume volumes | Custom v3.3.4-derived build; port 8012; bind directories; barcode/orientation overlays; Tika/Gotenberg | This upgrades application/schema versions. Retain current ports/volumes in the WSL adaptation and test migrations on copies. |
| Firefly | Version 6.6.6 from live image metadata; port 8086; named upload volume | Custom build based on 6.7.7 with DATEV; port 8081; separate upload volume; daily cron | This upgrades application/schema versions. Preserve the encryption key and uploads; verify migrations and scheduled jobs. |
| Cache | Private Valkey with existing persisted state | Separate authenticated Valkey with named volume | Configure both applications with the new broker credentials; do not share cache state accidentally. |
| UI | Private nginx at 8084 | Homepage/ASN at 8082; Stirling at 8087 | Update bookmarks and integrations only after acceptance. |
| Lifecycle | Hermes/Valkey/database/project-management service running; private peripheral tools and community stopped | Default services restart unless-stopped; Zettelrobbe opt-in | More services remain active; measure actual resource consumption. |
| Secrets | Existing application keys, database passwords, tokens, and account state | Generates new credentials for a fresh installation | Fresh-install secrets are not a migration strategy. Preserve source keys for transferred encrypted data. |
| Storage | Docker named volumes plus /root/.hermes and /root/workspaces binds | Paperless bind directories plus Docker-managed PostgreSQL, Valkey and Firefly-upload volumes | Backing up only the selected --data-root directory would miss these named volumes. |

## Originating evidence

Package root: `C:\Quasi Desktop\thomas\ki-mac-minimal-paperless-firefly-6757923f7dd`.

| Claim | Origin |
|---|---|
| Package has no existing data, database dumps, filled secrets, or images | MANIFEST.txt:9-10 |
| Dedicated project; PG18; explicit arm64; named PostgreSQL/Valkey volumes | firstparty/ki-basis/docker/profiles/paperless-firefly/compose.yaml:10-50,66-72 |
| Included application compose definitions | Same compose.yaml:12-20 |
| Homepage/ASN binds and ports | Same compose.yaml:98-109 |
| Custom Paperless build, storage directories, OCR defaults, and overlays | firstparty/paperless-stack/docker/docker-compose.yml:23-26,40-43,80-103 |
| OCR backend network aliases survive container renaming | Same file:118-147 |
| Firefly 6.7.7 build and 03:00 Europe/Berlin cron | firstparty/ki-basis/docker/profiles/paperless-firefly/firefly.override.yaml:5-33 |
| Separate Firefly upload volume and application key | firstparty/firefly-stack/docker/firefly/docker-compose.yml:16-18,31-46 |
| New credential generation; existing env retained but root paths rewritten | firstparty/ki-basis/docker/scripts/install-mac.sh:781-811 |
| Copies four source trees, pulls images, creates network, builds and starts | Same installer:829-877 |
| Installer prints generated secrets | Same installer:886-888 |
| Existing topology, binds, shared storage and forbidden volume deletion | C:\GitDev\apexai-os-meta\ki-basis\docs\INFRASTRUCTURE.md:22-32,72-87,138-139 |
| Live state and exact mounts | C:\ki-basis-backups\2026-11-04-pre-mac-minimal\evidence\containers-before.json |
| Live databases | Same backup directory: evidence/databases.json |

## Installation effects in order

1. Create destination and data-root directories; perform resource checks.
2. Install/check Homebrew packages and Docker Desktop on the Mac.
3. Copy ki-basis, paperless-stack, firefly-stack and zettelrobbe with rsync -a into the destination.
4. Create the profile .env, generate missing keys/passwords/tokens, and set destination/data paths.
5. Pull digest-selected images and create the external ki-mac-minimal-net network.
6. Create application bind directories and initialize new PostgreSQL/Valkey volumes.
7. Build custom Paperless and Firefly images, then start the default services.
8. Print credentials; manually create the Paperless administrator and first Firefly account for a fresh installation.

These steps neither read nor import the current priv_* databases or existing application files. The package profile returns before the generic installer's separate data-seeding path (install-mac.sh:925-932 versus 949).

## Material limitations

- INSTALL.md explicitly marks the package as draft and not yet accepted. A successful real Mac installation is not established by source inspection.
- Re-running rsync may overwrite destination source files. Existing .env retention does not protect source customizations or guarantee unchanged paths.
- The final application startup uses up -d without --wait; an installer exit does not prove every application is ready.
- The template enables orientation/barcode overlays, but inherits PAPERLESS_OCR_MODE=off and language deu. Verify actual document extraction and English requirements with representative documents.
- Default published ports differ from the existing stack. Current Docker bindings do not collide with the proposed defaults; future target-host listeners still require inspection.
- Optional Zettelrobbe references GLiNER, absent from this package. Leave it disabled during the initial pilot.
- Stirling licensing needs target-use verification against its current license; PREMIUM_ENABLED=false alone is not evidence of usage rights.
- Digest-selected base images do not pin every Homebrew/apk dependency. Firefly cron installs packages at runtime.
- The supplied images.lock explicitly selects ARM child digests. Registry queries resolved amd64 variants for all ten indexes and the additional pinned uv base; see [x86-64 plan](04-wsl-integration-plan.md) and [amd64 lock](images.amd64.lock).
- Source image labels identify Paperless 3.1.2 and Firefly 6.6.6. Evidence: backup evidence/source-application-versions.json. The rendered package enables nine default services with --profile ocr; evidence/package-compose-config.json records the configuration, not an installation result.

## Database transfer constraint

PostgreSQL documents logical dump/restore or a supported upgrade process for major-version changes. Filesystem copies cannot directly transfer a PG16 cluster into PG18. See [PostgreSQL 18 upgrade documentation](https://www.postgresql.org/docs/18/upgrading.html).

Recommendation for the operator-selected x86-64 host: Follow the [WSL integration plan](04-wsl-integration-plan.md), build the custom applications for linux/amd64, and validate them against isolated copies. Keep PG16 unless testing demonstrates a required PG18 dependency. Preserve the existing shared cluster and application keys.

Failure guard: Never attach the production PG16 volume to ParadeDB PG18. Never run docker compose down -v against either production or the preserved reset environment.
