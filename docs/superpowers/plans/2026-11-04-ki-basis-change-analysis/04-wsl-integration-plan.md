---
type: Plan
id: PLAN-KI-BASIS-WSL-INTEGRATION-20261104
title: ki-basis WSL feature integration plan
description: Primary x86-64 integration plan for the package capabilities, preserving the existing shared database and lifecycle contracts.
status: current
tags: [ki-basis, wsl, integration]
---

# ki-basis WSL feature integration implementation plan

> The authorized integration is deployed. This file retains the plan; use [deployment result](05-deployment-result.md) for current operation, completed checks and remaining verification limits.

Goal: Add the desired Paperless/Firefly/ASN/Stirling capabilities to the existing Windows/WSL stack without replacing unrelated services.

Architecture: Keep the native WSL Docker engine, existing private application identities, named data volumes, application keys and shared-database isolation. Reuse the package's application builds and overlays through a dedicated integration overlay. Prove database compatibility on copies before touching production.

Tech stack: Existing Docker/Compose and pgvector PG16; package application sources; optional Tika/Gotenberg, cron, nginx assets and Stirling.

## Global constraints

- The operator selected the existing x86-64 Windows/WSL host. The deployed application images target linux/amd64.
- Do not run install-mac.sh on the Windows host or inside WSL.
- Do not install another engine or replace the shared cluster as an incidental dependency.
- Do not force linux/arm64 on this host; inspect the native architecture and image manifest support first.
- Preserve original application keys, private database/role names, ports and mounted data unless an approved requirement changes them.
- Preserve the existing on-demand lifecycle for peripheral tools.

## Proposed file surface

| File or artifact | Proposed purpose |
|---|---|
| ki-basis/compose.shared-db.yaml | Existing canonical base; retain service identities and storage. |
| ki-basis/compose.paperless-firefly-features.yaml, new | Minimal overlay for tested builds, OCR helpers, feature mounts and optional services. |
| ki-basis/.env.shared-db | Preserve existing keys; add only feature settings required by accepted services. |
| WSL ext4 source checkouts for packaged paperless-stack/firefly-stack | Build from the supplied pins without copying over existing checkouts. |
| ki-basis/docker/nginx configuration and homepage/ASN assets | Add routes/assets only if homepage and ASN are selected. |
| ki-basis/scripts/wake-tools.sh and sleep-tools.sh | Include accepted on-demand helper services without waking unrelated stacks. |
| ki-basis/docs/INFRASTRUCTURE.md | Update only after the accepted deployment is verified live. |

The overlay and lifecycle integration are applied. The deployment result identifies the current runtime configuration and preserved data.

## x86-64 build contract

Build Paperless and Firefly from the supplied source pins for linux/amd64. Use the current x86-64 engine as the native builder; cross-compilation is needed only if a different-architecture builder is selected. Do not run the package's arm64 service declarations unchanged.

Inspect every pinned runtime and build-base manifest for linux/amd64 support. A multi-platform digest may remain valid; an ARM-only digest must be replaced with a verified amd64 digest. Record resolved digests in the integration build evidence.

Build command shape from the isolated ext4 source root:

```bash
docker buildx build --platform linux/amd64 --load \
  -t ki-basis-paperless:6757923f7dd-amd64 \
  --build-context docker.io/node:24-trixie-slim=docker-image://docker.io/node:24-trixie-slim@sha256:54f84b4cf8432b21aaffd5d3ce8d41e12cea0d10d33c09d2f3c9879d49d6b446 \
  -f paperless-stack/vendor/paperless-ngx/Dockerfile paperless-stack/vendor/paperless-ngx

docker buildx build --platform linux/amd64 --load \
  -t ki-basis-firefly:6757923f7dd-amd64 \
  --build-arg FIREFLY_BASE_IMAGE=fireflyiii/core:version-6.7.7@sha256:ed8c739cb73eed94da07d1249cef6d1a29507c406eafd48f2aa880ca5285709a \
  --build-context composer:2=docker-image://composer:2@sha256:22844d23aacc7140fccf24992829ae98bc2c92e0240ccca3b35716bf5d82ed70 \
  -f firefly-stack/docker/firefly/Dockerfile firefly-stack
```

Registry checks found linux/amd64 variants for all ten package indexes; [images.amd64.lock](images.amd64.lock) records the resolved pins. The pinned ghcr.io/astral-sh/uv base also exposes an amd64 variant (sha256:dfed1dea9beb0eab0390c3841cf09fc9ed49969e4eacec41c4a88fb07d126cb4). Evidence is in the protected backup's evidence/amd64-registry-manifests.json and evidence/amd64-uv-manifest.json.

The commands above use verified amd64 Firefly/Composer pins and the existing multi-platform Node index. Both builds completed successfully and produced amd64 images. Copied-data and live product checks are recorded in the deployment result. Architecture metadata alone does not establish application behavior.

Docker documents native builds, explicit platform selection, and manifest-based architecture selection in [multi-platform builds](https://docs.docker.com/build/building/multi-platform/).

## Task 1: Rehearse on isolated copies

- [ ] Verify the backup evidence and preserve the original image IDs and running-state ledger.
- [ ] Inspect native CPU architecture and target-image manifest support.
- [ ] Determine exact source and target application versions and supported upgrade paths.
- [ ] Restore copied private databases and application files into an isolated test project with distinct ports and volumes.
- [ ] Compare existing functionality against a captured document/transaction sample.

Deliverable: A working copy of the current application state, independent of production.

## Task 2: Establish the smallest database requirement

- [ ] Test the custom application builds against the isolated PG16 copies.
- [ ] Inspect application migrations and required database extensions.
- [ ] Retain shared PG16 if the applications and required features pass.
- [ ] Treat any demonstrated PG18/ParadeDB dependency as a separate database decision; do not upgrade all tenants to satisfy an unproven dependency.

Grounding: The package pins PG18 in its compose file, but its Paperless initialization explicitly creates only vector (05-paperless-db.sh:18). Firefly initialization creates its role/database and schema grants (06-firefly-db.sh:11-14). This evidence supports testing PG16 compatibility; it does not prove compatibility.

Deliverable: Measured compatibility result and an explicit database decision.

## Task 3: Add Paperless capabilities to the isolated copy

- [ ] Build the supplied Paperless source for the host architecture.
- [ ] Mount the packaged orientation script and prebarcode overlay read-only.
- [ ] Add Tika/Gotenberg and correct endpoint aliases on the private application network.
- [ ] Retain source keys and all four existing storage mappings.
- [ ] Test scans at 0/90/180/270 degrees, barcode/ASN capture, original/archive downloads and German/English extraction.

Deliverable: Accepted document workflow using production-shaped copied data.

## Task 4: Add Firefly capabilities to the isolated copy

- [ ] Build the pinned 6.7.7/DATEV source for the host architecture after excluding an unsupported downgrade.
- [ ] Retain the existing APP_KEY, private database mapping and upload-volume contents.
- [ ] Retain existing private cache settings; coordinate any authentication change with all current consumers before enabling it.
- [ ] Add cron only with a protected token and an explicit lifecycle policy.
- [ ] Test existing accounts, balances, transactions, attachments, DATEV output and scheduled work.

Deliverable: Accepted financial workflow without data or decryption regressions.

## Task 5: Add the selected user interfaces

- [ ] Serve the packaged homepage and local ASN generator from the existing nginx configuration or a distinct accepted endpoint.
- [ ] Add Stirling only after license and native-image compatibility checks.
- [ ] Verify loopback bindings, available ports and resource limits.
- [ ] Test browser label printing and representative PDF operations.

Deliverable: Working selected interfaces with measured resource use.

## Task 6: Deploy the tested overlay

- [ ] Obtain implementation authorization for the selected feature set and tested database route.
- [ ] Refresh the consistent source backup immediately before changing production.
- [ ] Stop only affected private application writers; preserve all existing stopped states.
- [ ] Apply the rehearsed image/configuration changes and supported migrations.
- [ ] Run the same document and financial acceptance cases against production.
- [ ] Update lifecycle helpers and current infrastructure documentation to the verified deployment.

Reset: Stop changed applications, restore original images/configuration and the matching database/file snapshot, then restore the recorded running-state set. Image rollback alone is insufficient after a schema migration.

Failure guard: Stop on unsupported native images, incompatible application downgrades, failed migrations, missing files, or invalid application keys. Resolve the demonstrated blocker before widening the change.
