# Phase 2 Rerun Compile Report — old-apex-full-orchestration-agent-kb

```yaml
phase2_rerun_compile_report:
  verdict: PASS_WITH_WARNINGS
  kb_slug: old-apex-full-orchestration-agent-kb
  kb_root: apex-meta/kb/old-apex-full-orchestration-agent-kb/
  generated_at: "2026-07-06T22:45:00+02:00"
  executor: LLM_semantic_layer_via_github_connector
  approval:
    phrase: approve ingest
    status: approved_for_this_rerun
  deterministic_baseline_verified: true
  phase1_replaced: true
  phase2_replaced: partial
  deterministic_postflight_run: false
```

## Files Replaced

```yaml
phase1_replaced:
  - ingest-analysis/batch01-agent-kb-architecture.analysis.md
  - ingest-analysis/batch02-agent-roles-and-doctrine.analysis.md
  - ingest-analysis/batch03-handoffs-validation-and-risk.analysis.md
  - ingest-analysis/batch04-reusable-patterns-and-migration.analysis.md
phase1_added:
  - ingest-analysis/phase1-rerun-completion-report.md
phase2_replaced:
  - wiki/summaries/old-agent-kb-architecture.md
  - wiki/summaries/old-agent-role-system.md
  - wiki/summaries/handoff-validation-and-risk-doctrine.md
  - wiki/summaries/reusable-old-agent-kb-patterns.md
  - wiki/summaries/migration-to-claude-native-orchestration.md
  - wiki/concepts/agent-doctrine-and-promotion-patterns.md
  - wiki/concepts/validation-and-routing-guardrails.md
  - wiki/concepts/migration-safety-patterns.md
  - wiki/entities/old-agent-roles.md
  - wiki/entities/reusable-artifact-families.md
  - audit/semantic-open-questions.md
```

## Connector-Blocked Updates

```yaml
blocked_updates:
  reason: "GitHub connector safety layer blocked these content updates after repeated narrowing. Existing pages remain present in the repo."
  paths:
    - wiki/summaries/deterministic-execution-safety-after-lint-closure.md
    - wiki/concepts/repo-execution-routing-safety.md
    - wiki/entities/meta-detective-internal-modes.md
    - wiki/index.md
```

## Semantic Result

The rerun replaced the main Phase 1 semantic analysis set and most Phase 2 retrieval pages with pages using the Apex KB page-value sections: ranked source set, macro synthesis, meso synthesis, micro claims, route map, and raw-source reopen triggers.

The old source paths remain historical source evidence only. Current Apex implementation decisions still require current repo verification.

## Required Deterministic Postflight

```text
KB_ROOT=apex-meta/kb/old-apex-full-orchestration-agent-kb
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --allow-write index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB_ROOT" --allow-write build-index
python apex-meta/scripts/apex_kb_retrieval.py --kb-root "$KB_ROOT" stale
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --json lint
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --json audit
python apex-meta/scripts/apex_kb.py --kb-root "$KB_ROOT" --json status
```

This connector run could not execute local Python commands. Do not treat the deterministic index, retrieval index, lint, audit, or status as refreshed until the postflight above is run in Codex or a local checkout.
