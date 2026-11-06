---
type: Changelog
id: LOG-KI-BASIS-AMD64-20261104
title: Private ki-basis x86-64 update and verification
description: Execution record of the private tool upgrade, preserved infrastructure, tested outcomes, and outstanding acceptance checks.
status: current
created: 2026-11-04
tags: [architecture, ki-basis, amd64, deployment, verification]
---

# Private ki-basis x86-64 update and verification

Recorded on 2026-11-04. The authorized update is deployed and the existing infrastructure health check reports GREEN: PASS=31, FAIL=0, WARN=0. Verification covers the checks below; it does not certify untested financial workflows or disaster recovery.

Current operating truth: [INFRASTRUCTURE.md](../../../../ki-basis/docs/INFRASTRUCTURE.md). Detailed access and operating instructions: [deployment result](../../../../docs/superpowers/plans/2026-11-04-ki-basis-change-analysis/05-deployment-result.md).

## Delivered changes

- Adapted the supplied paperless-firefly Mac/ARM package to the existing Linux x86-64 host. Built native linux/amd64 Paperless source 3.3.4 and Firefly 6.7.7 images, including the DATEV extension.
- Added the [private feature overlay](../../../../ki-basis/compose.paperless-firefly-features.yaml), Tika/Gotenberg document conversion, pre-barcode/orientation hooks, homepage/ASN labels, Stirling-PDF 3.2.2, and Firefly's 03:00 Europe/Berlin cron schedule.
- Kept shared PostgreSQL 16, private database/role mappings, existing application keys, OAuth keys, account password hashes and application volumes.
- Preserved Hermes, Valkey, shared database, authoritative project-management and community container identities. No replacement engine or WSL environment was introduced.
- Integrated all seven private tools into sleep/wake and Compose entrypoints. They retain restart: "no"; core services stay running during tool sleep.
- Configured persistent Stirling account/settings storage and a generated local admin password. Credentials remain in local protected storage and are excluded from this record.

The package's Tika 4 pin failed the DOCX test because the bundled Paperless client calls the removed /tika/form/text endpoint. The deployed Tika 3.3.1.0 amd64 pin passed that test. Firefly required writable preserved OAuth key mounts for startup permission updates. The pre-barcode Django app was explicitly registered, and Gotenberg's allow-list was anchored.

## Verification record

The executor performed the tests; the operator requested a follow-up infrastructure check. The follow-up docker ps and existing health script both exited 0 and reproduced GREEN with PASS=31, FAIL=0, WARN=0. Community services remained stopped as intended.

The linked evidence files are byte-matched copies of the saved execution receipts. They contain no credentials, session tokens, database dumps or document contents.

| Check | Verified outcome | Evidence |
|---|---|---|
| Native builds | Both custom images report amd64 | [Image identities](evidence/2026-11-04-private-amd64/built-images.json) |
| Infrastructure health | Existing health script GREEN; reported 31 passes, no failures or warnings | [Health output](evidence/2026-11-04-private-amd64/infra-health-final.log) |
| Original Paperless document | Authenticated live download succeeded; checksum matches pre-upgrade baseline | [Original document check](evidence/2026-11-04-private-amd64/live-original-document-check.json) |
| Existing account credentials | Password hashes preserved for two Paperless accounts and one Firefly account | [Credential preservation](evidence/2026-11-04-private-amd64/account-credential-preservation.json) |
| Barcode and orientation | ASN 123 recognized; 0/90/180/270-degree fixtures consumed with extracted text | [Fixture results](evidence/2026-11-04-private-amd64/paperless-fixture-results.txt) |
| Office conversion | DOCX consumed through Tika/Gotenberg with extracted text | [DOCX result](evidence/2026-11-04-private-amd64/office-conversion-result.txt) |
| DATEV | Route/preflight checks passed; empty-data EXTF CSV generated | [DATEV export receipt](evidence/2026-11-04-private-amd64/firefly-integration-check.json) |
| Stirling | Admin login and authenticated merge returned HTTP 200 and produced a PDF | [Merge receipt](evidence/2026-11-04-private-amd64/stirling-merge-result.json) |
| Sleep/wake | All seven tools stopped and restarted; four always-on services remained running | [Lifecycle receipt](evidence/2026-11-04-private-amd64/lifecycle-cycle.json) |
| Live access and configuration | Application HTTP, loopback bindings, internal-only helpers, matching cron token and Stirling login after restart passed | [Final live checks](evidence/2026-11-04-private-amd64/live-final-verification.json) |
| Unrelated services | Original container identities retained | [Preservation receipt](evidence/2026-11-04-private-amd64/unrelated-container-identities-unchanged.json) |

Browser inspection also observed 189 generated SVG labels, 5,157 barcode bars and the Print Labels control. A focused read-only configuration review found no actionable issues. The deployment documentation bundle passed its existing OKF/APEX validator without errors or warnings.

Health-check reproduction in PowerShell:

```powershell
wsl -d Ubuntu -u root -- docker ps -a --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
$healthScript = Get-Content -Raw -LiteralPath 'C:\GitDev\apexai-os-meta\apex-meta\orchestration\architecture-improvements\05-program-closeout\tests\infra-health-test.sh'
$healthScript.Replace("`r", "") | wsl -d Ubuntu -u root -- bash
```

## Backup and execution boundary

The pre-upgrade reset backup is C:\ki-basis-backups\2026-11-04-pre-mac-minimal: a 71,206,389,760-byte WSL export, Windows-hosted stack/configuration copies, globals and eight database dumps. Earlier backup verification included archive/checksum checks and isolated SQL restores. The deployment reused that verified backup; full backup restore checks were not repeated.

See [backup coverage and verification limits](../../../../docs/superpowers/plans/2026-11-04-ki-basis-change-analysis/03-backup-and-reset.md). WSL import/reset was removed from the execution instructions at the operator's request and was not performed.

## Outstanding acceptance and optional follow-up

- Verify representative financial transactions and attachments, then DATEV export with the actual advisor/client/account settings. The deployment-time dataset had no journals; the verified export was an empty-data smoke test.
- Print a physical ASN label at 1:1 scale and scan it through the actual scanner workflow. Browser rendering and packaged barcode ingestion passed; physical printing was not tested.
- Inspect the first scheduled 03:00 cron execution. Its configuration/token match was verified; a scheduled execution has not been observed in this chat.
- Review and commit/push the deployment and this record when ready. The working tree on codex/ki-basis-amd64-features contains the changes; this logging task did not commit or push them.
- Optionally copy the verified backup off this physical drive. The existing local reset point does not protect against failure of that drive.
- The guarded legacy start/stop shell launchers retain pre-existing CRLF syntax failures. Active wake/sleep helpers and PowerShell entrypoints passed; legacy repair was outside this update.

A full WSL import-and-boot recovery rehearsal remains unperformed and explicitly outside the approved execution sequence. It is not an automatic next step.

Failure guard: Preserve matching data, keys, image identities and backup evidence before a later schema change. Do not infer verification of real financial results, printing hardware or full recovery from infrastructure health alone.
