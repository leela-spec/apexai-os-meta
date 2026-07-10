# Apex KB Connector Routing and Postflight Patch Manifest v2

```yaml
repository: leela-spec/apexai-os-meta
branch: main
baseline_commit: dbf5bf066cca939abbc1d6a3471cad74c7749db5
mode: patch_artifacts_only
patch_format: anchored_apply_patch
target_files:
  - .claude/skills/apex-kb/SKILL.md
  - apex-meta/scripts/apex_kb.py
  - .claude/skills/apex-kb/references/script-command-contract.md
  - .claude/skills/apex-kb/references/acceptance-tests.md
  - .claude/skills/apex-kb/package-manifest.md
  - .claude/skills/apex-kb/references/lifecycle-state-machine.md
  - .claude/skills/apex-kb/examples/lifecycle-runbook.md
patches_in_order:
  - 001-apex-kb-skill-capability-routing.patch
  - 002-apex-kb-postflight-runtime.patch
  - 003-apex-kb-postflight-command-contract.patch
  - 004-apex-kb-acceptance-fixtures.patch
  - 005-apex-kb-package-authority-alignment.patch
  - 006-apex-kb-state-machine-deprecation-banner.patch
  - 007-apex-kb-runbook-banner-and-postflight.patch
excluded_files:
  - all runtime and documentation files outside the seven targets
source_pack_preserved: true
target_files_modified_on_main: false
```

## Independent derivation basis

| Patch | Verified intent |
|---|---|
| 001 | Capability-first routing and connector-only authoring boundary from R08; preventive checklist concepts from R06. |
| 002 | Immutable reason-code registry from R06 and bounded seven-stage in-process postflight from R07. |
| 003 | Runtime-aligned postflight command contract from R07. |
| 004 | Reason-code synchronization and postflight behavioral fixtures from R06/R07. |
| 005 | Sole operational authority alignment from R08. |
| 006 | State-machine deprecation banner from R08. |
| 007 | Terminal-example banner and preferred postflight interface from R08/R07. |

## Construction constraints

- Every patch uses `*** Begin Patch` / `*** Update File` / anchored `@@` sections / `*** End Patch`.
- Every patch affects exactly one manifest target file.
- No target file is modified by this package.
- No malformed hunk from the first pack is mechanically repaired or translated.
- The patches are re-expressed from baseline content and governing intent.
- Application and runtime execution remain the responsibility of the later patch applier.
