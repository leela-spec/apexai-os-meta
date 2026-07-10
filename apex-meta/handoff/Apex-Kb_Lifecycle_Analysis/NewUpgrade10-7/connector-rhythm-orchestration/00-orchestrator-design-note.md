# Apex KB Connector-Native Compile Rhythm — Orchestrator Design Note

## Decision

The connector-native compile rhythm is viable for semantic authoring, but not for deterministic certification.

```yaml
verdict:
  connector_semantic_authoring: viable
  connector_self_validation: viable_as_precheck
  deterministic_certification: not_viable_without_terminal
  maximum_connector_state: compiled_unvalidated
  query_ready_without_terminal: false
```

## Governing boundary

```yaml
ownership:
  connector_llm:
    - create complete new semantic files
    - perform complete whole-file rewrites of files it owns
    - re-read and self-check each authored file
    - write one connector compile manifest
  terminal_python:
    - partial edits and machine-section updates
    - source manifest and hash mutation
    - wiki index generation
    - retrieval index generation
    - lint, quality, status, stale, and postflight evidence
```

A connector must never partially edit an existing artifact, append to `wiki/index.md`, update derived indexes, or claim deterministic completion.

## One-page rhythm

```yaml
per_page_loop:
  - read one bounded source slice
  - read canonical page contract and relevant template
  - author one complete page
  - re-read the page
  - run the mirrored reason-code self-check
  - write only after self-check passes
  - record result in connector compile manifest
  - move to next page
batching_rule: one_page_per_context_window
```

## Checklist authority

The terminal implementation is authoritative. The connector checklist is a mirrored authoring precheck, not a second quality contract.

```yaml
checklist_authority:
  source_of_truth: apex-meta/scripts/apex_kb.py quality reason codes
  connector_copy: .claude/skills/apex-kb/SKILL.md
  certification: terminal_quality_strict_only
  drift_rule: >
    Any quality reason-code change must update the connector checklist and its
    acceptance fixture in the same patch. A disagreement is a contract defect.
```

Generating the checklist dynamically was rejected for this wave because a connector-only executor cannot run the generator. The smallest executable design is a concise mirrored checklist with explicit terminal authority and a required equivalence fixture.

## Connector compile manifest

Adopt a minimal manifest because it directly prevents false completion and gives the terminal controller a diffable list of self-claims.

```yaml
manifest:
  path: log/connector-compile-<run-id>.json
  whole_file_only: true
  canonical_knowledge: false
  purpose:
    - enumerate authored pages
    - record create versus full rewrite
    - record self-check verdicts
    - state that no deterministic command ran
    - request exact terminal actions
```

This is not a new lifecycle engine. It is a bounded handoff packet.

## Implementation options

```yaml
options:
  a_capability_first_router:
    decision: adopt
    reason: prevents the observed capability-routing failure and removes most effective reading surface for connector executors

  b_consolidation_and_banners:
    decision: split
    adopt_now:
      - lifecycle-state-machine in-file deprecation banner
      - lifecycle-runbook example-only banner
    gated_second_wave:
      - canonical page-value contract consolidation
    reason: banners are noncontroversial; contract/template edits require operator confirmation under the handover

  c_cli_footgun_fixes:
    decision: defer
    reason: terminal-only ergonomics do not block the connector rhythm and would expand this wave

  d_aggregate_postflight_command:
    decision: defer_pending_research
    reason: useful only if it remains a thin command aggregator rather than a workflow engine
```

## Truthful terminal states

```yaml
states:
  semantic_files_written_but_no_terminal: compiled_unvalidated
  terminal_quality_or_lint_failed: repair_required
  terminal_postflight_passed_but_no_semantic_review: deterministically_validated
  deterministic_and_required_semantic_review_passed: query_ready
```

## Open operator decisions retained

- Whether Phase 1 and Phase 2 remain continuous by default.
- Which artifact defines target-query authority.
- How semantic-partial outputs are represented.
- Threshold calibration and valid concise exceptions.
- Minimum pointer granularity.
- Independent reviewer escalation threshold.
- Pointer-only custody rules.
- Phase 1 persistence policy.
- Whether to approve second-wave edits to `kb-contract.md` and `wiki-page-templates.md`.
