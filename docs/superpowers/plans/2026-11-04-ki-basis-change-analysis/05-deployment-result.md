---
type: Reference
id: REF-KI-BASIS-AMD64-DEPLOYMENT-20261104
title: ki-basis x86-64 deployment result
description: Current service access, preserved state, operating commands, and acceptance evidence for the deployed private tools.
status: current
tags: [ki-basis, amd64, deployment]
---

# ki-basis x86-64 deployment result

The private tools run on the existing x86-64 WSL Docker engine and shared PostgreSQL 16 cluster. Both custom application builds target linux/amd64. WSL import/reset is excluded from the execution sequence.

## Access and operation

| Product | Address | Deployment |
|---|---|---|
| Homepage | http://127.0.0.1:8082/ | Paperless, Firefly, Stirling and ASN tiles |
| ASN labels | http://127.0.0.1:8082/tools/asn-labels/ | Local Code 128 generator; 189 labels per sheet |
| Paperless | http://127.0.0.1:8010/ | Custom source 3.3.4 with orientation/pre-barcode hooks; existing users and document data |
| Firefly | http://127.0.0.1:8086/ | Custom 6.7.7 with DATEV; existing user, application key, uploads and OAuth keys |
| Stirling-PDF | http://127.0.0.1:8087/ | Version 3.2.2; persistent local admin account |
| Existing edge | http://127.0.0.1:8084/ | Existing endpoint retained |

Use the existing Paperless and Firefly accounts. The Stirling admin username is admin. Its generated password is stored in ignored ki-basis/.env.shared-db as STIRLING_ADMIN_PASSWORD and in the protected local file C:\ki-basis-backups\2026-11-04-pre-mac-minimal\execution\stirling-access.txt. Do not share that file or commit secrets.

All seven tools use restart: "no". Hermes and Valkey retain their always-on lifecycle. The tools are running after the verified sleep/wake cycle.

```powershell
wsl -d Ubuntu -u root -- /mnt/c/GitDev/apexai-os-meta/ki-basis/scripts/sleep-tools.sh
wsl -d Ubuntu -u root -- /mnt/c/GitDev/apexai-os-meta/ki-basis/scripts/wake-tools.sh
```

Compose operations require both compose.shared-db.yaml and compose.paperless-firefly-features.yaml. The start/stop PowerShell helpers include both. Runtime scripts, ASN assets and preserved OAuth key files bind from /root/builds/ki-basis-amd64-6757923f7dd; retain that versioned directory. Stirling account/settings state persists in ki-basis-stirling-configs.

The nightly Firefly cron schedule is 03:00 Europe/Berlin. Its token is generated in the existing ignored environment file. Tika and Gotenberg are internal-only.

## Preserved state

- Shared PostgreSQL 16 and private database/role names remain in use.
- Existing Paperless/Firefly encryption keys and original Firefly OAuth key hashes match the pre-upgrade values.
- Paperless retains two users and one original document. The original download matched the copied-data baseline.
- Firefly retains one user and zero transaction journals; no test financial records were added to production.
- Existing Paperless data/media/export/consume and Firefly upload named volumes remain attached.
- Hermes, Valkey, shared PostgreSQL, authoritative project-management and community container identities were preserved during deployment.
- The original reset backup remains available. Current private database migration checkpoints are saved under its protected execution/pre-upgrade directory. No full backup restore checks were repeated during this deployment.

## Verification evidence

Evidence directory: C:\ki-basis-backups\2026-11-04-pre-mac-minimal\execution.

| Product check | Verified result | Evidence |
|---|---|---|
| Custom builds | Both build commands exited 0; image architecture amd64 | paperless-build.log, firefly-build.log, built-images.json |
| Copied-data migrations | New applications started successfully on copied PG16 data | kb-amd64-test-paperless.log, kb-amd64-test-firefly.log |
| Original document | Live authenticated listing/download succeeded; original checksum matches baseline | live-original-document-check.json |
| Barcode and orientation | ASN 123 recognized; all four rotation variants consumed with extracted text | paperless-fixture-results.txt |
| Office conversion | DOCX consumed with extracted text through Tika/Gotenberg | office-conversion-result.txt |
| DATEV | Route registered; preflight passed; empty-data EXTF CSV generated | firefly-datev-route-check.json, firefly-datev-preflight.log, firefly-integration-check.json |
| Stirling | Admin login and authenticated merge returned 200; result is a PDF | stirling-merge-result.json, stirling-merged-smoke.pdf |
| ASN browser rendering | 189 SVG labels and 5,157 barcode bars rendered; Print Labels control available | Browser observation in executor output |
| Lifecycle | All seven tools stopped and woke; always-on services remained running | lifecycle-cycle.json |
| Isolation and preservation | Unrelated container identities retained; keys preserved | unrelated-container-identities-unchanged.json, original-firefly-oauth-sha256.json |
| Code review | No actionable findings in configuration/lifecycle review | Reviewer output in executor record |
| Existing infrastructure health | GREEN; reported PASS=31, FAIL=0, WARN=0 | infra-health-final.log |
| Existing account credentials | Both Paperless password hashes and the Firefly password hash preserved | account-credential-preservation.json |
| Final live invariants | HTTP, loopback bindings, cron configuration, original keys/volumes and Stirling login after restart passed | live-final-verification.json |
| Governed documentation | OKF/APEX validator passed without errors or warnings | governance-final.json |

## Verification limits

Real financial bookings and attachment-bearing transactions were not validated because the existing Firefly dataset has no journals. DATEV settings retain the supplied defaults. Physical label printing was not exercised. The first scheduled 03:00 cron run has not yet occurred. A full WSL import-and-boot recovery is excluded and was not performed.

## Baseline check limitation

The guarded legacy start-ki-basis.sh and stop-ki-basis.sh files fail raw bash -n because of existing CRLF lines. Both the saved pre-upgrade copies and current files return exit 2. The active wake/sleep shell helpers and PowerShell entrypoints pass syntax checks and the live lifecycle cycle. These baseline line-ending defects were not expanded into unrelated repair work; evidence is shell-syntax-baseline-comparison.json.

Failure guard: Keep the matching private database/file snapshots, encryption keys and original image identifiers available before any later schema or application change. Use scoped recovery only if deployment fails; do not restore other tenants to reset one private tool.
