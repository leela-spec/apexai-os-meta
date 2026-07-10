# Apex KB Connector Routing and Postflight Patch Manifest

```yaml
repository: leela-spec/apexai-os-meta
branch: main
baseline_commit: dbf5bf066cca939abbc1d6a3471cad74c7749db5
mode: patch_artifacts_only
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
excluded_files: []
known_unvalidated_claims:
  - git apply check not executed by connector
  - Python compilation not executed by connector
  - acceptance tests not executed by connector
  - runtime behavior not certified by connector
```

## Decision trace

| Patch | Governing decision |
|---|---|
| 001 | R08 capability-first routing; R06 preventive checklist equivalence |
| 002 | R07 fixed seven-stage postflight aggregate; R06 reason-code registry synchronization |
| 003 | R07 command contract and R06 terminal quality authority |
| 004 | R06 reason-code fixtures and R07 postflight behavior fixtures |
| 005 | R08 authority alignment |
| 006 | R08 sole operational authority decision |
| 007 | R08 execution-surface banner and R07 preferred postflight interface |

All patches are authored against the same recorded baseline. They are artifacts only and have not been applied.