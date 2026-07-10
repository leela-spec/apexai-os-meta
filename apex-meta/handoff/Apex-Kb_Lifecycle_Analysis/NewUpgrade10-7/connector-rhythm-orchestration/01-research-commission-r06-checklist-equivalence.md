# Research Commission R06 — Connector Checklist Equivalence

Execute the full read-only investigation now. Do not stop at access checks or a plan.

```yaml
research_job:
  id: R06
  repo: leela-spec/apexai-os-meta
  branch: main
  question: >
    What is the smallest connector-readable authoring checklist that is equivalent
    to the current apex_kb.py quality --strict reason-code contract for Phase 2 pages?
  constraints:
    - do not modify files
    - do not invent a page score
    - do not add semantic judgments to deterministic quality
    - inspect current main only
```

Read only:

1. `apex-meta/scripts/apex_kb.py`: quality constants, helper functions, `quality_report`, `cmd_quality`.
2. `.claude/skills/apex-kb/references/kb-contract.md`: Phase 2 page contract.
3. `.claude/skills/apex-kb/references/acceptance-tests.md`: current quality fixtures.
4. The six R02 calibration pages or fixture equivalents already used to validate the quality engine.

Return:

```yaml
research_report:
  id: R06
  exact_reason_codes: []
  connector_observable_checks: []
  checks_not_reliably_connector_observable: []
  checklist_text_under_250_words: ""
  equivalence_fixture:
    passing_page: ""
    expected_quality_strict: pass
    failing_pages: []
  drift_prevention_contract: {}
  exact_files_likely_affected: []
  unresolved_questions: []
```
