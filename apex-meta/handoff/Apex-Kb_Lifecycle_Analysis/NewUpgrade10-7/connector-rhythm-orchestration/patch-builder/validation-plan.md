# Apex KB Connector Routing and Postflight Validation Plan

Run from repository root on `main`.

## 1. Confirm baseline and target-file contents

```bash
git checkout main
git pull --ff-only origin main
test "$(git rev-parse HEAD)" = "dbf5bf066cca939abbc1d6a3471cad74c7749db5"
git show dbf5bf066cca939abbc1d6a3471cad74c7749db5:.claude/skills/apex-kb/SKILL.md > /dev/null
git show dbf5bf066cca939abbc1d6a3471cad74c7749db5:apex-meta/scripts/apex_kb.py > /dev/null
git show dbf5bf066cca939abbc1d6a3471cad74c7749db5:.claude/skills/apex-kb/references/script-command-contract.md > /dev/null
git show dbf5bf066cca939abbc1d6a3471cad74c7749db5:.claude/skills/apex-kb/references/acceptance-tests.md > /dev/null
git show dbf5bf066cca939abbc1d6a3471cad74c7749db5:.claude/skills/apex-kb/package-manifest.md > /dev/null
git show dbf5bf066cca939abbc1d6a3471cad74c7749db5:.claude/skills/apex-kb/references/lifecycle-state-machine.md > /dev/null
git show dbf5bf066cca939abbc1d6a3471cad74c7749db5:.claude/skills/apex-kb/examples/lifecycle-runbook.md > /dev/null
```

## 2. Individual patch checks

```bash
git apply --check apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/001-apex-kb-skill-capability-routing.patch
git apply --check apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/002-apex-kb-postflight-runtime.patch
git apply --check apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/003-apex-kb-postflight-command-contract.patch
git apply --check apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/004-apex-kb-acceptance-fixtures.patch
git apply --check apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/005-apex-kb-package-authority-alignment.patch
git apply --check apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/006-apex-kb-state-machine-deprecation-banner.patch
git apply --check apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/007-apex-kb-runbook-banner-and-postflight.patch
```

## 3. Cumulative patch check in manifest order

```bash
git apply --check \
  apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/001-apex-kb-skill-capability-routing.patch \
  apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/002-apex-kb-postflight-runtime.patch \
  apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/003-apex-kb-postflight-command-contract.patch \
  apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/004-apex-kb-acceptance-fixtures.patch \
  apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/005-apex-kb-package-authority-alignment.patch \
  apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/006-apex-kb-state-machine-deprecation-banner.patch \
  apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/007-apex-kb-runbook-banner-and-postflight.patch
```

## 4. Apply in manifest order

```bash
git apply apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/001-apex-kb-skill-capability-routing.patch
git apply apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/002-apex-kb-postflight-runtime.patch
git apply apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/003-apex-kb-postflight-command-contract.patch
git apply apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/004-apex-kb-acceptance-fixtures.patch
git apply apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/005-apex-kb-package-authority-alignment.patch
git apply apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/006-apex-kb-state-machine-deprecation-banner.patch
git apply apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/patch-builder/007-apex-kb-runbook-banner-and-postflight.patch
```

## 5. Compile scripts

```bash
python -m py_compile apex-meta/scripts/apex_kb.py
python -m py_compile apex-meta/scripts/apex_kb_retrieval.py
```

## 6. Verify postflight help and global-flag placement

```bash
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-smoke postflight --help
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-smoke --json postflight
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-smoke postflight --json
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-smoke --allow-write --dry-run --json postflight
```

## 7. Direct-command regressions

```bash
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-smoke --json index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/apex-kb-smoke --json build-index
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-smoke --json lint --strict
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-smoke --json quality --strict
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-smoke --json audit
python apex-meta/scripts/apex_kb.py --kb-root apex-meta/kb/apex-kb-smoke --json status
python apex-meta/scripts/apex_kb_retrieval.py --kb-root apex-meta/kb/apex-kb-smoke --json stale
```

## 8. Reason-code/checklist/fixture synchronization

Unresolved command: the repository contract specifies the equality assertion but does not provide a committed executable test runner. Implement or identify the existing repository test command before claiming this validation complete.

Required assertion: the runtime registry, `SKILL.md` connector checklist, and acceptance-fixture reason-code set are exactly equal to the eleven-code contract.

## 9. Quality fixtures

Execute the PowerShell fixture procedure under `Phase 2 thin-but-structurally-complete regression fixtures` and `Connector checklist and postflight regression fixtures` in `.claude/skills/apex-kb/references/acceptance-tests.md`.

Unresolved command: no single repository-native automated fixture command is defined in the current contract.

## 10. Postflight fixtures

Execute all dry-run, `--allow-write --dry-run`, successful write, lint failure, quality failure, retrieval-build failure, missing/unreadable metadata, shared-root, path-safety, schema, stage-order, dependency-skip, evidence-preservation, status, and exit-code fixtures defined in `.claude/skills/apex-kb/references/acceptance-tests.md`.

Unresolved command: no single repository-native automated fixture command is defined in the current contract.

## 11. Documentation/runtime alignment

```bash
grep -n "postflight\|compiled_unvalidated\|quality --strict\|apex.kb.postflight.v1" .claude/skills/apex-kb/SKILL.md .claude/skills/apex-kb/references/script-command-contract.md .claude/skills/apex-kb/references/acceptance-tests.md .claude/skills/apex-kb/examples/lifecycle-runbook.md apex-meta/scripts/apex_kb.py
```

Confirm manually that documentation describes only implemented runtime behavior.

## 12. Confirm exactly seven target files changed

```bash
git diff --name-only
```

Expected set:

```text
.claude/skills/apex-kb/SKILL.md
apex-meta/scripts/apex_kb.py
.claude/skills/apex-kb/references/script-command-contract.md
.claude/skills/apex-kb/references/acceptance-tests.md
.claude/skills/apex-kb/package-manifest.md
.claude/skills/apex-kb/references/lifecycle-state-machine.md
.claude/skills/apex-kb/examples/lifecycle-runbook.md
```
