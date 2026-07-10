# APEX Step 2 -> Step 3 Handoff Brief

```yaml
handoff:
  id: apex-step2-to-step3-operator-output-design-handoff
  status: ready_for_step3
  created_date: 2026-07-10
  source_package: apex-meta/operator-output-design/step2-operator-user-stories/
  next_step: Step 3 - Define APEX operator-facing output design principles + artifact family
```

## 1. Step 2 result

Step 2 locked the operator user-story definition for the APEX weekly orchestration loop.

The verified source files are intentionally split into small machine-readable files:

```text
apex-meta/operator-output-design/step2-operator-user-stories/00-package-manifest.okf.yaml
apex-meta/operator-output-design/step2-operator-user-stories/01-verification-decisions.okf.yaml
apex-meta/operator-output-design/step2-operator-user-stories/02-macro-loop-and-value-frame.okf.yaml
apex-meta/operator-output-design/step2-operator-user-stories/03-planning-side-user-stories.okf.yaml
apex-meta/operator-output-design/step2-operator-user-stories/04-execution-recap-user-stories.okf.yaml
apex-meta/operator-output-design/step2-operator-user-stories/05-status-learning-user-stories.okf.yaml
apex-meta/operator-output-design/step2-operator-user-stories/06-output-jobs-and-artifact-family.okf.yaml
apex-meta/operator-output-design/step2-operator-user-stories/07-step3-handoff-brief.okf.md
```

## 2. Locked operator-value frame

Step 3 must preserve these confirmed rules:

```yaml
operator_value_frame:
  first_10_seconds:
    must_answer:
      - what_changed
      - what_next
      - what_needs_review
  result_card_first: true
  human_first_machine_second: true
  primary_human_surfaces:
    - cards
    - short_lists
    - compact_summaries
  avoid_as_primary_surface:
    - wide_schema_tables
    - implementation_noise
    - validation_noise_before_operator_value
  review_gate_language:
    - approve
    - edit
    - reject
    - defer
    - clarify
    - execute
    - skip
    - mark_blocked
  no_silent_mutation: true
  partial_context_rule: >
    Missing, stale, or conflicting inputs become confidence/review flags, not
    invented certainty.
```

## 3. Locked output jobs

Step 3 should design the output family for these jobs:

```yaml
output_jobs:
  - id: J1
    artifact: Project State Success Card
  - id: J2
    artifact: Weekly Command Brief
  - id: J3
    artifact: Tomorrow Action Brief
  - id: J4
    artifact: Flow Execution Card
  - id: J5
    artifact: Flow Prompt Pack
  - id: J6
    artifact: Raw Flow Dump / Skip Marker Card
  - id: J7
    artifact: FlowRecap Result Card
  - id: J8
    artifact: Usage Learning Card
  - id: J9
    artifact: Status Merge Decision Card
  - id: J10
    artifact: Project KB Update Card
  - id: J11
    artifact: Project Status Overview
  - id: J12
    artifact: AI Routing Card
```

## 4. Step 3 task

Step 3 should turn Step 2 into an operator-output design source package.

Recommended Step 3 outputs:

```yaml
step3_recommended_outputs:
  - output_design_principles.okf.yaml
  - card_anatomy_patterns.okf.yaml
  - artifact_family_spec.okf.yaml
  - review_gate_language_rules.okf.yaml
  - resilience_and_partial_context_rules.okf.yaml
  - template_acceptance_criteria.okf.yaml
  - deep_research_prompt_if_needed.okf.md
```

## 5. Boundaries

Step 3 must not:

```yaml
out_of_scope:
  - mutate existing skill runtime files
  - execute PreCapWeek
  - execute PreCapNextDay
  - run FlowRecap
  - merge project state
  - create calendar events
  - design autonomous agents or schedulers
  - replace schema authority from existing skill reference contracts
```

## 6. Practical instruction for next run

Start by reading:

1. `00-package-manifest.okf.yaml`
2. `02-macro-loop-and-value-frame.okf.yaml`
3. `06-output-jobs-and-artifact-family.okf.yaml`
4. the relevant story file for the artifact family being designed

Then produce Step 3 as small iterative files, not as one large handover.
