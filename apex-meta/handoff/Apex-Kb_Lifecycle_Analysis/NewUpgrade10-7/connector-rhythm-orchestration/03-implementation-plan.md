# Apex KB Connector Rhythm — Implementation Plan

## Wave 1 — Ready

```yaml
scope:
  - .claude/skills/apex-kb/SKILL.md
  - .claude/skills/apex-kb/references/lifecycle-state-machine.md
  - .claude/skills/apex-kb/examples/lifecycle-runbook.md
patches:
  - patches/001-skill-capability-router.patch
  - patches/002-lifecycle-state-machine-deprecation.patch
  - patches/003-lifecycle-runbook-example-only.patch
```

### Expected effect

- Connector-only executors branch before reading terminal-only material.
- One-page-per-context compile rhythm becomes explicit.
- Whole-file-only mutation boundary becomes operational.
- Connector output truthfully caps at `compiled_unvalidated`.
- Stale lifecycle documents no longer appear authoritative.

## Wave 2 — Research-gated

```yaml
required_inputs:
  - R06 checklist equivalence result
  - operator approval for kb-contract.md and wiki-page-templates.md edits
possible_scope:
  - .claude/skills/apex-kb/references/kb-contract.md
  - .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
  - .claude/skills/apex-kb/templates/wiki-page-templates.md
  - .claude/skills/apex-kb/references/acceptance-tests.md
```

Goal: one canonical Phase 2 value contract, reference-only copies elsewhere, and one equivalence fixture.

## Wave 3 — Optional terminal ergonomics

Proceed only if R07 recommends it.

```yaml
possible_scope:
  - apex-meta/scripts/apex_kb.py
  - .claude/skills/apex-kb/references/script-command-contract.md
  - .claude/skills/apex-kb/references/acceptance-tests.md
```

## Apply policy

- Work directly on `main`.
- Re-read each target from live `main` before application.
- Apply patches in numeric order.
- No manual equivalent edits after a failed patch.
- Commit and push only after all validation passes.
