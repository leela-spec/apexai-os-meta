# Research Commission R08 — Capability-First Execution Routing

Execute the full read-only investigation now. Do not stop at access checks, a plan, or a source list.

```yaml
research_job:
  id: R08
  repo: leela-spec/apexai-os-meta
  branch: main
  question: >
    What is the smallest capability-first routing change that lets a connector-only
    executor follow the Apex KB semantic compile path without reading or inferring
    terminal-only lifecycle work?
  target: >
    Produce one exact routing design for connector-only and terminal-backed execution.
    Do not redesign the Apex KB lifecycle.
  constraints:
    - read current main only
    - do not modify repository files
    - do not design patches
    - do not add new lifecycle states unless an existing state cannot express the result
    - do not reopen quality thresholds, retrieval behavior, or Phase 2 content design
    - keep connector completion capped at compiled_unvalidated
```

## Read only

1. `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/architecture-analysis-and-connector-rhythm-handover.md`
   - Why: authoritative handover for the observed capability-routing failure and the whole-file-only connector boundary.
   - Expect: the accepted connector rhythm, terminal ownership, and unresolved routing questions.

2. `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/NewUpgrade10-7/connector-rhythm-orchestration/00-orchestrator-design-note.md`
   - Why: records the adopted capability-first direction and rejected scope expansion.
   - Expect: the intended connector state, checklist authority, manifest role, and deferred work.

3. `.claude/skills/apex-kb/SKILL.md`
   - Why: current operator-facing procedure that every executor receives.
   - Expect: where one shared procedure forces connector executors to infer which steps are impossible.

4. `.claude/skills/apex-kb/package-manifest.md`
   - Why: identifies current lifecycle-authority and navigation files.
   - Expect: which documents are authoritative, duplicated, example-only, or deprecated.

5. `.claude/skills/apex-kb/references/lifecycle-state-machine.md`
   - Why: test whether it conflicts with or duplicates the active procedure.
   - Expect: whether an in-file deprecation banner is sufficient.

6. `.claude/skills/apex-kb/examples/lifecycle-runbook.md`
   - Why: test whether examples can be mistaken for required universal procedure.
   - Expect: whether an example-only banner is sufficient.

Do not inspect scripts, quality internals, retrieval internals, or unrelated skill files. R06 and R07 already cover those targets.

## Determine

1. The exact capability check needed before procedure routing.
2. The connector-only procedure, limited to semantic whole-file authoring, readback, checklist precheck, compile-manifest creation, and terminal handoff.
3. The terminal-backed procedure, referencing existing deterministic commands rather than restating them.
4. The minimum completion labels for each route.
5. The exact text or sections in `SKILL.md` that should be added, replaced, shortened, or removed.
6. Whether the lifecycle-state-machine and lifecycle-runbook need only banners or any further change.
7. Any current instruction that would still cause a connector executor to attempt partial edits, indexes, hashes, lint, quality, status, stale checks, or terminal certification.

## Return

```yaml
research_report:
  id: R08
  verdict: accept|reject|revise
  routing_failure_confirmed: true|false
  minimal_capability_check: {}
  connector_route:
    allowed_actions: []
    forbidden_actions: []
    procedure: []
    maximum_completion_state: compiled_unvalidated
    handoff_requirements: []
  terminal_route:
    procedure_references: []
    completion_requirements: []
  skill_md_change_map:
    add: []
    replace: []
    shorten_or_remove: []
  banner_decisions:
    lifecycle_state_machine: none|deprecation_banner
    lifecycle_runbook: none|example_only_banner
  exact_files_likely_affected: []
  rejected_scope_expansion: []
  unresolved_questions_that_block_implementation: []
```

The report must choose one minimal design. Do not return multiple architecture options.