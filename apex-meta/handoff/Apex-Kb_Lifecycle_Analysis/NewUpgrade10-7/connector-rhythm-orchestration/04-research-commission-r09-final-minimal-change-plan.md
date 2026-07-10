# Research Commission R09 — Final Minimal Change Plan

Execute the full read-only investigation now. Do not stop at access checks, a plan, or a summary of prior reports.

```yaml
research_job:
  id: R09
  repo: leela-spec/apexai-os-meta
  branch: main
  question: >
    What is the smallest final change set that implements the accepted connector
    capability route, connector checklist, and aggregate postflight command without
    reopening unrelated Apex KB architecture?
  target: >
    Produce one implementation-ready patch plan against current main. Do not create
    patch files and do not modify target files.
  constraints:
    - current main only
    - no repository mutation
    - no patch generation
    - no new workflow engine
    - no broad documentation cleanup
    - no quality-threshold redesign
    - no retrieval-ranking changes
    - no CLI cleanup unrelated to postflight
```

## Read the decisions first

1. `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/architecture-analysis-and-connector-rhythm-handover.md`
   - Why: defines the governing whole-file semantic-authoring boundary.
   - Expect: the accepted target and explicit non-targets.

2. `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/00-orchestrator-design-note.md`
   - Why: records the current orchestration decisions.
   - Expect: accepted capability routing, checklist authority, manifest role, and truthful states.

3. R06 final report supplied with this research run.
   - Why: establishes the connector-readable checklist and its limits.
   - Expect: exact reason codes, checklist text, equivalence fixture, and drift contract.

4. R07 final report supplied with this research run.
   - Why: establishes whether and how to add aggregate postflight.
   - Expect: exact stage order, blocking behavior, dry-run behavior, output schema, and target files.

5. R08 final report supplied with this research run.
   - Why: establishes the exact connector and terminal routes.
   - Expect: the minimal `SKILL.md` change map and banner decisions.

If an R06, R07, or R08 final report is not supplied, stop and name the missing report. Do not reconstruct it from prompt files.

## Then inspect only current target files

1. `.claude/skills/apex-kb/SKILL.md`
   - Why: apply the R08 routing decision and the R06 connector checklist at the primary entrypoint.
   - Expect: exact sections to replace rather than append duplicative procedure text.

2. `apex-meta/scripts/apex_kb.py`
   - Why: place the R07 thin postflight aggregator using existing command functions and parser dispatch.
   - Expect: exact existing delegates, argument shapes, dispatch location, and exit handling.

3. `.claude/skills/apex-kb/references/script-command-contract.md`
   - Why: document only the implemented postflight command and its evidence limits.
   - Expect: one bounded command contract, not a lifecycle rewrite.

4. `.claude/skills/apex-kb/references/acceptance-tests.md`
   - Why: add the minimum fixtures required by R06 and R07.
   - Expect: checklist-equivalence and aggregate-postflight behavior checks.

5. `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md`
   - Why: include the connector authoring precheck only if R06 or R08 requires operational placement here.
   - Expect: either one concise alignment change or no change.

6. `.claude/skills/apex-kb/package-manifest.md`, `.claude/skills/apex-kb/references/lifecycle-state-machine.md`, and `.claude/skills/apex-kb/examples/lifecycle-runbook.md`
   - Why: apply only the authority or banner decisions from R08.
   - Expect: no change unless explicitly required by R08.

Do not inspect unrelated files. Add a target file only when a supplied report requires it and the current file proves the change belongs there.

## Produce

1. One exact target-file list.
2. One ordered change specification per target file.
3. Exact functions or sections affected.
4. What must remain unchanged.
5. Dependencies between file changes.
6. Acceptance checks for each change.
7. Patch grouping: one patch per target file unless one file must contain several cohesive changes.
8. A minimal patch-builder execution order.
9. A minimal terminal applier validation order.
10. A list of requested changes rejected as drift.

## Return

```yaml
research_report:
  id: R09
  verdict: ready_for_patch_building|blocked
  blocking_missing_inputs: []
  target_files:
    - path: ""
      reasons: []
      exact_symbols_or_sections: []
      ordered_changes: []
      preserve_unchanged: []
      dependencies: []
      acceptance_checks: []
      patch_file_name: ""
  excluded_files:
    - path: ""
      reason: ""
  patch_build_order: []
  cumulative_validation_order: []
  terminal_apply_and_validation_order: []
  drift_rejected: []
  unresolved_questions_that_block_patch_building: []
```

Return one final plan, not alternative plans. Every target file must trace to R06, R07, or R08 evidence.