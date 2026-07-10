# Verification Handoff

```yaml
repo: leela-spec/apexai-os-meta
branch: main
patch_order:
  - patches/001-skill-capability-router.patch
  - patches/002-lifecycle-state-machine-deprecation.patch
  - patches/003-lifecycle-runbook-example-only.patch
```

## Required checks

```bash
git checkout main
git pull --ff-only origin main
git apply --check 001-skill-capability-router.patch
git apply --check 002-lifecycle-state-machine-deprecation.patch
git apply --check 003-lifecycle-runbook-example-only.patch
git apply 001-skill-capability-router.patch
git apply 002-lifecycle-state-machine-deprecation.patch
git apply 003-lifecycle-runbook-example-only.patch
git diff --check
git diff -- .claude/skills/apex-kb/SKILL.md .claude/skills/apex-kb/references/lifecycle-state-machine.md .claude/skills/apex-kb/examples/lifecycle-runbook.md
```

## Behavioral review

1. Start from `SKILL.md` as a simulated connector-only executor.
2. Confirm the router sends that executor only to the source slice, `kb-contract.md`, the Phase 1 template, and the relevant wiki template.
3. Confirm the connector path never requires script, retrieval, acceptance-test, state-machine, or PowerShell documentation.
4. Author one scratch Phase 2 page using the connector checklist.
5. Create the connector compile manifest.
6. Run terminal postflight against the scratch KB:

```bash
python apex-meta/scripts/apex_kb.py --kb-root <scratch-kb> index --allow-write --json
python apex-meta/scripts/apex_kb.py --kb-root <scratch-kb> lint --strict --json
python apex-meta/scripts/apex_kb.py --kb-root <scratch-kb> quality --strict --json
python apex-meta/scripts/apex_kb.py --kb-root <scratch-kb> status --json
python apex-meta/scripts/apex_kb_retrieval.py --kb-root <scratch-kb> build-index --allow-write --json
python apex-meta/scripts/apex_kb_retrieval.py --kb-root <scratch-kb> stale --json
```

Pass requires the authored page to pass `quality --strict`. Connector self-check alone is never sufficient.

## Final report

```yaml
final_report:
  verdict: PASS | FAIL
  live_main_sha: ""
  git_apply_check_each: PASS | FAIL
  git_diff_check: PASS | FAIL
  connector_simulation: PASS | FAIL
  checklist_quality_equivalence: PASS | FAIL
  unexpected_files_changed: []
  commit_sha: ""
  pushed_to_origin_main: true | false
  workarounds_used: false
```
