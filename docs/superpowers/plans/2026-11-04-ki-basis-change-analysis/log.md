---
type: Reference
id: LOG-KI-BASIS-ANALYSIS-20261104
title: ki-basis analysis artifact log
description: Dated creation record for the x86-64 analysis and backup evidence bundle.
status: current
tags: [ki-basis, log]
---

# Artifact log

2026-11-04: Created the package comparison, x86-64 integration/build plan, registry-derived amd64 lock, and reset-backup evidence. Preserved the initial Mac-path candidate in archive/02-mac-pilot-reference.md after the operator specified the existing x86 target. Created no application build or deployment.

2026-11-04: Executed the operator-authorized x86-64 integration and removed the WSL-import/reset action and its dependent startup commands. Built custom Paperless/Firefly images, retained PG16 and existing private data/keys, and deployed the feature overlay. Repeated full backup restore checks were omitted as requested. Product tests required writable preserved OAuth key mounts, explicit pre-barcode app registration, and persistent Stirling account storage with generated local credentials. The DOCX test exposed the package's Tika 4 API incompatibility; pinned verified amd64 Tika 3.3.1.0 after [Apache's endpoint migration record](https://github.com/apache/tika/blob/main/docs/modules/ROOT/pages/migration-to-4x/migrating-tika-server-4x.adoc) and the [Paperless compatibility report](https://github.com/paperless-ngx/paperless-ngx/issues/13755) confirmed the failure. Applied Gotenberg's anchored allow-list form. [Stirling's account configuration](https://docs.stirlingpdf.com/Configuration/Security/System%20and%20Security/) grounds initial admin setup. The live lifecycle cycle and focused configuration review passed; see [deployment result](05-deployment-result.md).
