# APEX Deep Research Synthesis — Repository-Grounded, Read-Only

**Research sources read completely**

- [`deep-research-report (12).md`](sandbox:/mnt/data/deep-research-report%20%2812%29.md)
    
- [`deep-research-report (11)(2).md`](sandbox:/mnt/data/deep-research-report%20%2811%29%282%29.md)
    

**Repository authority:** `leela-spec/apexai-os-meta`, branch `main`  
**Mutation performed:** none

---

# Part 1 — Executive synthesis

```yaml
executive_synthesis:
  reports_read_completely: true
  repository_checked_live: true
  significant_recommendations_found: 14

  classification_counts:
    adopt: 5
    adapt: 4
    defer: 4
    reject: 1

  strongest_research_contribution:
    recommendation: >
      Separate deterministic validation, transformation, rendering, and state
      mutation instead of treating all automation as one capability.
    reason: >
      This clarifies what can safely be automated without weakening APEX's
      operator-approval and no-silent-mutation boundaries.

  most_overengineered_recommendation:
    recommendation: >
      Replace the artifact family with a universal canonical structured schema
      and automatically generate every human and machine view from it.
    reason: >
      APEX already has contract-backed artifact authorities and twelve distinct
      operator jobs. A universal replacement would create a second architecture,
      blur ownership, and reopen verified J1-J12 decisions.

  most_important_unresolved_question:
    question: >
      Should APEX formalize a small deterministic validation layer now, or leave
      validation entirely inside individual skill contracts until the operator
      templates are stable?

  overall_verdict: >
    The reports add useful external support for progressive disclosure, compact
    provenance, deterministic checking, accessible headings and links, and
    generated secondary views. They do not justify replacing the current APEX
    artifact family. Most of their strongest interface principles are already
    present in Step 2 and Step 3. Their genuinely new contribution is a clearer
    boundary between harmless deterministic assurance and operator-gated state
    mutation.
```

The live repository is further ahead than either report could verify. Step 2 is explicitly operator-verified and locked for Step 3, including result-card-first presentation, first-ten-seconds usefulness, cards over wide tables, operator decision language, and no silent mutation.

Step 3 already formalizes progressive disclosure, compact provenance, minimal machine handoffs, candidate-state visibility, references instead of duplicated schemas, and conditional validation detail.

The Round 3 execution architecture is also settled: the Flow Execution Card is the primary workspace; prompts are simple linked files with a lightweight index; evidence normalization is conditional; and the skip marker is minimal. Three large repetitive operator documents were explicitly rejected.

---

# Part 2 — Research synthesis matrix

|ID|Recommendation|Class|Current repo state|APEX judgment|Decision needed now?|
|---|---|---|---|---|---|
|R01|Result-card-first progressive disclosure|**adopt**|Already verified and designed|Keep as shared rule; no redesign|No|
|R02|Minimum machine handoff plus linked detail|**adopt**|Already implemented in Step 3 design|Preserve and apply per artifact|No|
|R03|Candidate state visibly separate from accepted state|**adopt**|Locked across root and Step 2/3|Essential safety boundary|No|
|R04|Compact provenance, freshness, confidence, and assumptions|**adopt**|Mostly designed|Keep compact and decision-relevant|No|
|R05|Deterministic structural validation and linting|**adopt**|Rules exist; dedicated operator-output scripts not found|Useful assurance without mutation|**Yes**|
|R06|One canonical source with human/machine projections|**adapt**|Contract-backed artifacts already act as authorities|Apply per artifact, not globally|No|
|R07|Reusable shared components|**adapt**|Shared anatomy already exists|Reuse anatomy, not universal schema|No|
|R08|Deterministic transformation and rendering|**adapt**|Minimal handoffs defined; generated views absent|Narrow to read-only projections|Later|
|R09|Event/candidate/accepted-state and diff model|**adapt**|Candidate/accepted boundary exists|Add only diff semantics that serve approval|**Yes**|
|R10|HTML or web operator view|**defer**|Markdown/OKF design source is sufficient now|Secondary generated view only after stability|**Yes**|
|R11|Automatic indexes, link resolution, and cross-file navigation|**defer**|Direct refs and prompt mappings already designed|Useful after paths and templates stabilize|No|
|R12|Prompt caching and token-budget automation|**defer**|Outside current output-design ownership|Runtime/provider optimization, not present need|No|
|R13|Runtime agents, schedulers, and autonomous processing|**defer**|Explicitly outside current mechanism|Reconsider only after manual loop proves stable|No|
|R14|Universal structured schema replacing J1-J12|**reject**|Conflicts with artifact family and schema owners|Creates duplicate architecture and schema drift|No|

---

# Part 3 — Detailed assessments

## A. Operator interface

### R01 — Result-card-first progressive disclosure

```yaml
research_assessment:
  id: R01
  recommendation: >
    Put a compact result or state card first, followed by actions, essential
    context, provenance, machine handoff, and technical validation.
  report_sources:
    - "deep-research-report (12).md — Progressive disclosure rule"
    - "deep-research-report (11)(2).md — Operator output design system"

  classification: adopt

  external_value:
    problem_addressed: cognitive overload and slow orientation
    expected_benefit: faster resumption, clearer decisions, less re-reading

  repository_comparison:
    current_repository_state: >
      Fully present as the first-ten-seconds contract, result-card-first rule,
      and progressive-disclosure order.
    exact_evidence_paths:
      - apex-meta/operator-output-design/step2-operator-user-stories/02-macro-loop-and-value-frame.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/02-shared-card-and-brief-anatomy.okf.yaml
    already_implemented: true
    conflicts_with_verified_decision: false
    duplicates_existing_authority: true

  apex_judgment:
    reason: >
      This is valuable external confirmation, but not a new architecture proposal.
    applicable_scope:
      - shared_design_rule
      - J1-J12
    risk_if_adopted:
      - none_if_treated_as_confirmation
      - duplication_if_rewritten_as_a_second_rule_set
    smallest_useful_form: keep_current_Step3_rules

  operator_decision:
    required_now: false
```

The repository already requires the first screen to show result/current state, exact next action, review needs, and material blockers.

---

### R02 — Minimum machine handoff and linked detail

```yaml
research_assessment:
  id: R02
  recommendation: >
    Put only downstream-required fields in a compact machine handoff and link to
    detail rather than copying the complete human narrative.
  report_sources:
    - "deep-research-report (12).md — Smallest coherent target architecture"
    - "deep-research-report (11)(2).md — Shared Compact Machine Handoff"

  classification: adopt

  external_value:
    problem_addressed: duplicated context and token waste
    expected_benefit: lower drift, smaller downstream context, clearer ownership

  repository_comparison:
    current_repository_state: >
      Step 3 requires minimum sufficient downstream payloads and forbids copied
      authoritative schemas and duplicated full human narratives.
    exact_evidence_paths:
      - apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/02-shared-card-and-brief-anatomy.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/08-round3-cross-artifact-relationship.okf.yaml
    already_implemented: true
    conflicts_with_verified_decision: false
    duplicates_existing_authority: true

  apex_judgment:
    reason: >
      Directly compatible and already encoded as an APEX design rule.
    applicable_scope:
      - shared_design_rule
      - cross_artifact_handoffs
    risk_if_adopted:
      - under_specification_if_handoff_becomes_too_small
    smallest_useful_form: artifact_specific_minimum_payload_plus_contract_reference

  operator_decision:
    required_now: false
```

Step 3 explicitly places machine payloads after the human layer and limits them to downstream-required fields.

---

### R03 — Candidate state versus accepted state

```yaml
research_assessment:
  id: R03
  recommendation: >
    Make candidate, accepted, rejected, deferred, conflicting, and unresolved
    states explicit; require approval before durable mutation.
  report_sources:
    - "deep-research-report (12).md — Candidate and accepted state boundary"
    - "deep-research-report (11)(2).md — State model"

  classification: adopt

  external_value:
    problem_addressed: silent mutation and automation overreach
    expected_benefit: auditability, reversibility, operator trust

  repository_comparison:
    current_repository_state: >
      Root constraints forbid state overwrite, and Step 2/3 require durable
      changes to remain visible candidates until accepted.
    exact_evidence_paths:
      - .claude/Claude.md
      - apex-meta/operator-output-design/step2-operator-user-stories/00-package-manifest.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml
    already_implemented: true
    conflicts_with_verified_decision: false
    duplicates_existing_authority: true

  apex_judgment:
    reason: >
      Essential but already locked. External review-system analogies do not
      require a new APEX state architecture.
    applicable_scope:
      - J7
      - J9
      - J10
      - durable_state_boundaries
    risk_if_adopted:
      - approval_fatigue_if_low_impact_information_is_over_gated
    smallest_useful_form: visible_state_label_plus_existing_operator_gate

  operator_decision:
    required_now: false
```

The root forbids overwriting state, while Step 3 requires all proposed durable changes to expose their state classification.

---

### R04 — Compact provenance, freshness, confidence, and assumptions

```yaml
research_assessment:
  id: R04
  recommendation: >
    Show sources, freshness, confidence, consequential assumptions, and material
    conflicts without exposing a large evidence inventory by default.
  report_sources:
    - "deep-research-report (12).md — Provenance model"
    - "deep-research-report (11)(2).md — Confidence and Provenance Block"

  classification: adopt

  external_value:
    problem_addressed: unclear evidence boundaries and overconfidence
    expected_benefit: calibrated trust and faster review

  repository_comparison:
    current_repository_state: >
      Shared anatomy already includes main sources, freshness, confidence,
      consequential assumptions, and compact default visibility.
    exact_evidence_paths:
      - apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/02-shared-card-and-brief-anatomy.okf.yaml
    already_implemented: partial
    conflicts_with_verified_decision: false
    duplicates_existing_authority: false

  apex_judgment:
    reason: >
      The reports validate the current design. A five-field universal provenance
      object should not be mandatory when fewer fields are sufficient.
    applicable_scope:
      - shared_design_rule
      - state_and_review_artifacts
      - planning_inputs
    risk_if_adopted:
      - evidence_inventory_bloat
      - false_precision_from_generic_confidence_labels
    smallest_useful_form: >
      main_sources + freshness + decision_relevant_confidence +
      consequential_assumptions

  operator_decision:
    required_now: false
```

Step 3 already hides full inventories and technical traces while exposing decision-relevant source and confidence information.

---

### R13 — Interruption recovery and resumability

This research theme is retained inside R01 rather than classified separately. The current `next_action`, `review_needed`, blocker, direct prompt link, visible path fallback, and one-primary-workspace rules already provide the practical recovery cues the reports recommend.

---

## B. Artifact and schema architecture

### R06 — Contract-backed canonical artifact with projections

```yaml
research_assessment:
  id: R06
  recommendation: >
    Maintain one authoritative source per artifact and derive operator and
    machine projections from it.
  report_sources:
    - "deep-research-report (12).md — Canonical source and rendered view relationship"
    - "deep-research-report (11)(2).md — Target architecture"

  classification: adapt

  external_value:
    problem_addressed: source-of-truth ambiguity
    expected_benefit: less duplication and projection drift

  repository_comparison:
    current_repository_state: >
      APEX already has distinct contract-backed artifact authorities and a
      presentation layer that references rather than replaces them.
    exact_evidence_paths:
      - apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/04-flow-execution-card-design.okf.yaml
    already_implemented: partial
    conflicts_with_verified_decision: false
    duplicates_existing_authority: false

  apex_judgment:
    reason: >
      The useful principle is one authority per artifact. The reports' stronger
      version—one structured source generating all views—may not fit artifacts
      whose operator view is itself the normal authored output.
    applicable_scope:
      - per_artifact_design
      - future_read_only_projection_tooling
    risk_if_adopted:
      - schema_drift
      - extra_generation_layer
      - loss_of_directly_editable_operator_artifacts
    smallest_useful_form: >
      retain_current_contract_owner; permit read_only projections per artifact
      where they demonstrably reduce duplication

  operator_decision:
    required_now: false
```

The repository explicitly says existing skill contracts remain authoritative and Step 3 owns presentation, not domain schema.

---

### R07 — Shared components without a replacement schema

```yaml
research_assessment:
  id: R07
  recommendation: >
    Reuse result cards, action blocks, decision controls, provenance blocks,
    warnings, and machine handoffs across artifacts.
  report_sources:
    - "deep-research-report (11)(2).md — Operator output design system"
    - "deep-research-report (12).md — Shared result-card anatomy"

  classification: adapt

  external_value:
    problem_addressed: inconsistent interfaces
    expected_benefit: predictable scanning and lower design effort

  repository_comparison:
    current_repository_state: >
      Step 3 already provides one reusable shared anatomy across J1-J12 while
      requiring artifact-specific actions and content.
    exact_evidence_paths:
      - apex-meta/operator-output-design/step3-output-design-system/02-shared-card-and-brief-anatomy.okf.yaml
    already_implemented: true
    conflicts_with_verified_decision: false
    duplicates_existing_authority: true

  apex_judgment:
    reason: >
      Keep component grammar, but do not turn every component into mandatory
      universal fields.
    applicable_scope:
      - shared_design_rule
      - J1-J12
    risk_if_adopted:
      - homogeneous_cards
      - approval_fatigue
      - irrelevant_empty_sections
    smallest_useful_form: common_layer_order_plus_artifact_specific_required_fields

  operator_decision:
    required_now: false
```

---

### R09 — Event, candidate, accepted-state, and diff model

```yaml
research_assessment:
  id: R09
  recommendation: >
    Distinguish observations from candidate changes and accepted state, and show
    diffs instead of rewriting full state.
  report_sources:
    - "deep-research-report (11)(2).md — State model"
    - "deep-research-report (12).md — Candidate and accepted state boundary"

  classification: adapt

  external_value:
    problem_addressed: unclear change history and expensive full-state reviews
    expected_benefit: safer approvals and more compact review

  repository_comparison:
    current_repository_state: >
      Candidate versus accepted state is already locked. A universal append-only
      event store is not established and is not required by the present design.
    exact_evidence_paths:
      - .claude/Claude.md
      - apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/09-round3-decision-and-verification-record.okf.yaml
    already_implemented: partial
    conflicts_with_verified_decision: false
    duplicates_existing_authority: false

  apex_judgment:
    reason: >
      Diff presentation is useful for J9/J10. Full event-sourcing architecture
      would add complexity beyond current needs.
    applicable_scope:
      - J9_Status_Merge
      - J10_Project_KB_Update
    risk_if_adopted:
      - second_state_system
      - event_log_complexity
      - unclear_ownership
    smallest_useful_form: candidate_diff_against_current_accepted_state

  operator_decision:
    required_now: true
    decision_question: >
      Should approval become invalid automatically whenever the candidate diff
      changes materially?
```

---

### R14 — Universal schema replacing the artifact family

```yaml
research_assessment:
  id: R14
  recommendation: >
    Use one universal canonical structured schema as the source for all J1-J12
    artifacts and their projections.
  report_sources:
    - "deep-research-report (11)(2).md — Central architectural conclusion"
    - "deep-research-report (11)(2).md — Target architecture"

  classification: reject

  external_value:
    problem_addressed: cross-artifact inconsistency
    expected_benefit: theoretical uniformity and common rendering

  repository_comparison:
    current_repository_state: >
      J1-J12 represent different operator jobs and existing skills retain schema
      authority. Shared presentation rules already provide consistency.
    exact_evidence_paths:
      - apex-meta/operator-output-design/step2-operator-user-stories/06-output-jobs-and-artifact-family.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/09-round3-decision-and-verification-record.okf.yaml
    already_implemented: false
    conflicts_with_verified_decision: true
    duplicates_existing_authority: true

  apex_judgment:
    reason: >
      A universal replacement schema would override skill contracts, flatten
      meaningful differences, and recreate precisely the second-architecture
      problem Step 3 avoids.
    applicable_scope:
      - none_as_replacement_architecture
    risk_if_adopted:
      - schema_drift
      - duplicate_source_of_truth
      - ownership_conflict
      - unnecessary_migration
    smallest_useful_form: shared_presentation_anatomy_only

  operator_decision:
    required_now: false
```

The twelve jobs are explicitly distinct, while Step 3 says it must not redefine their domain schemas.

---

## C. Provenance, confidence, and review

R03 and R04 cover the retained recommendations in this group.

The reports’ proposals for full evidence inventories, universal provenance objects, and always-visible confidence should be narrowed. Current APEX rules correctly show confidence only when below high or materially relevant, and hide full source inventories by default.

---

## D. Deterministic validation and rendering

### R05 — Deterministic structural validation

```yaml
research_assessment:
  id: R05
  recommendation: >
    Use deterministic checks for required fields, links, references, manifest
    consistency, state labels, and contract-boundary violations.
  report_sources:
    - "deep-research-report (12).md — Deterministic script opportunities"
    - "deep-research-report (11)(2).md — Deterministic processing and validation"

  classification: adopt

  external_value:
    problem_addressed: mechanical drift and malformed handoffs
    expected_benefit: reliable outputs without extra semantic review work

  repository_comparison:
    current_repository_state: >
      Acceptance checks and validation rules exist throughout Step 3, but the
      report-proposed operator-output scripts were not found in the live repo.
    exact_evidence_paths:
      - apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/02-shared-card-and-brief-anatomy.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/04-flow-execution-card-design.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/09-round3-decision-and-verification-record.okf.yaml
    already_implemented: partial
    conflicts_with_verified_decision: false
    duplicates_existing_authority: false

  apex_judgment:
    reason: >
      Mechanical checks fit APEX because they do not decide priorities, interpret
      evidence, approve changes, or mutate state.
    applicable_scope:
      - shared_design_validation
      - future_template_validation
    risk_if_adopted:
      - validator_becoming_second_schema_authority
      - false_blocking_on_noncritical_formatting
    smallest_useful_form: >
      read_only checks derived directly from existing contracts and Step 3
      acceptance rules

  operator_decision:
    required_now: true
    decision_question: >
      Should deterministic validation be a formal requirement of the output
      design, while script implementation remains outside the current step?
```

---

### R08 — Deterministic transformation and rendering

```yaml
research_assessment:
  id: R08
  recommendation: >
    Deterministically extract compact handoffs and generate human projections
    from authoritative artifacts.
  report_sources:
    - "deep-research-report (11)(2).md — Target architecture"
    - "deep-research-report (11)(2).md — Render pipeline"
    - "deep-research-report (12).md — Deterministic assurance layer"

  classification: adapt

  external_value:
    problem_addressed: repeated rewriting and projection inconsistency
    expected_benefit: repeatable read-only views and smaller AI context

  repository_comparison:
    current_repository_state: >
      Handoff content is defined, but generated projections are not a verified
      current requirement.
    exact_evidence_paths:
      - apex-meta/operator-output-design/step3-output-design-system/02-shared-card-and-brief-anatomy.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/08-round3-cross-artifact-relationship.okf.yaml
    already_implemented: partial
    conflicts_with_verified_decision: false
    duplicates_existing_authority: false

  apex_judgment:
    reason: >
      Read-only extraction can be useful per artifact. Requiring every operator
      view to be generated from machine structure would be premature.
    applicable_scope:
      - compact_machine_handoff
      - optional_read_only_views
    risk_if_adopted:
      - generated_source_confusion
      - reduced_manual_editability
      - premature_tooling
    smallest_useful_form: >
      deterministic extraction only where the authoritative contract already
      defines the required fields

  operator_decision:
    required_now: false
```

---

### R10 — Generated HTML or web view

```yaml
research_assessment:
  id: R10
  recommendation: >
    Generate a lightweight HTML operator view while retaining Markdown as the
    repository source or fallback.
  report_sources:
    - "deep-research-report (12).md — Canonical source and rendered view relationship"
    - "deep-research-report (11)(2).md — Presentation and navigation model"

  classification: defer

  external_value:
    problem_addressed: inconsistent Markdown rendering and accessibility
    expected_benefit: stronger layout control, navigation, and focus order

  repository_comparison:
    current_repository_state: >
      Current design uses Markdown/OKF structures, cards, short sections, and
      relative prompt links. Stable final templates are not yet complete.
    exact_evidence_paths:
      - apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/04-flow-execution-card-design.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/05-prompt-file-and-index-design.okf.yaml
    already_implemented: false
    conflicts_with_verified_decision: false
    duplicates_existing_authority: false

  apex_judgment:
    reason: >
      HTML may become useful as a secondary generated view, but it adds little
      value before templates and navigation are stable.
    applicable_scope:
      - future_operator_view
    risk_if_adopted:
      - two_visible_versions
      - rendering_maintenance
      - premature_design_system_work
    smallest_useful_form: generated_secondary_view_never_canonical

  operator_decision:
    required_now: true
    decision_question: >
      Should HTML remain explicitly deferred until Markdown templates pass
      operator testing?
```

---

### Deterministic state mutation

Automated state mutation is **not** adopted. The reports correctly distinguish a state-merge guard from validation, but any actual application of status or KB changes remains under existing operator-gated owners. Root constraints and Step 3 candidate-state rules take precedence.

---

## E. Context and token efficiency

### R11 — Automatic indexes and link generation

```yaml
research_assessment:
  id: R11
  recommendation: >
    Generate indexes, validate relative links, and maintain parent/child
    navigation deterministically.
  report_sources:
    - "deep-research-report (11)(2).md — Deterministic processing and validation"
    - "deep-research-report (12).md — Deterministic script opportunities"

  classification: defer

  external_value:
    problem_addressed: broken navigation and manual index drift
    expected_benefit: easier artifact discovery and fewer stale links

  repository_comparison:
    current_repository_state: >
      Direct relative prompt links, visible path fallbacks, and lightweight prompt
      mappings are already defined.
    exact_evidence_paths:
      - apex-meta/operator-output-design/step3-output-design-system/04-flow-execution-card-design.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/05-prompt-file-and-index-design.okf.yaml
    already_implemented: partial
    conflicts_with_verified_decision: false
    duplicates_existing_authority: false

  apex_judgment:
    reason: >
      Link checking is useful, but index generation should wait until actual
      template paths and package structure stabilize.
    applicable_scope:
      - future_tooling
    risk_if_adopted:
      - tooling_against_transitional_paths
      - generated_index_churn
    smallest_useful_form: read_only_broken_link_check

  operator_decision:
    required_now: false
```

---

### R12 — Prompt caching and token-budget automation

```yaml
research_assessment:
  id: R12
  recommendation: >
    Use stable cached prompt context and automatic size/token budgets.
  report_sources:
    - "deep-research-report (11)(2).md — Efficiency argument"
    - "deep-research-report (11)(2).md — Implementation guidance"

  classification: defer

  external_value:
    problem_addressed: repeated context cost and prompt bloat
    expected_benefit: lower API usage and faster repeated runs

  repository_comparison:
    current_repository_state: >
      APEX already minimizes repetition through references, one prompt per file,
      and lightweight indexes. Runtime caching is outside current output design.
    exact_evidence_paths:
      - apex-meta/operator-output-design/step3-output-design-system/05-prompt-file-and-index-design.okf.yaml
      - apex-meta/operator-output-design/step3-output-design-system/08-round3-cross-artifact-relationship.okf.yaml
    already_implemented: partial
    conflicts_with_verified_decision: false
    duplicates_existing_authority: false

  apex_judgment:
    reason: >
      The design principle is relevant, but provider caching and strict token
      budgets belong to future runtime and Prompt Engineering/AI Routing work.
    applicable_scope:
      - future_prompt_tooling
      - future_runtime
    risk_if_adopted:
      - provider_specific_coupling
      - arbitrary_size_limits
      - content_quality_loss
    smallest_useful_form: preserve_reference_instead_of_repeat_rule

  operator_decision:
    required_now: false
```

---

## F. Future runtime or automation

### R13 — Runtime agents and scheduling

```yaml
research_assessment:
  id: R13
  recommendation: >
    Extend deterministic processing into runtime agents, scheduled checks, or
    increasingly autonomous orchestration.
  report_sources:
    - "deep-research-report (11)(2).md — Agent architecture and implementation guidance"
    - "deep-research-report (12).md — Future package skeleton and tooling"

  classification: defer

  external_value:
    problem_addressed: repetitive manual execution
    expected_benefit: eventual automation and recurring assurance

  repository_comparison:
    current_repository_state: >
      The verified mechanism is Claude skill-only, manually triggered, with no
      automatic scheduling, agents, calendar writes, or state mutation.
    exact_evidence_paths:
      - .claude/Claude.md
      - apex-meta/operator-output-design/step2-operator-user-stories/02-macro-loop-and-value-frame.okf.yaml
    already_implemented: false
    conflicts_with_verified_decision: true
    duplicates_existing_authority: false

  apex_judgment:
    reason: >
      Potentially useful later, but outside the present operator-output design
      stage and dependent on a proven manual loop.
    applicable_scope:
      - future_runtime_only
    risk_if_adopted:
      - premature_autonomy
      - hidden_mutation
      - ownership_blur
      - operational_complexity
    smallest_useful_form: none_in_current_stage

  operator_decision:
    required_now: false
```

The current mechanism is explicitly manual and forbids automatic scheduling and silent mutation.

---

# Part 4 — What the reports got wrong or could not verify

|Report claim or assumption|Verification result|Live repo evidence|Consequence|
|---|---|---|---|
|Live repository could not be inspected|**Correct limitation of the reports, no longer true for this synthesis**|Repository and named files were fetched from `main`|Their repo descriptions and scores cannot be treated as authority|
|Step 2 and Step 3 state was unknown|**Now verified**|Step 2 manifest is `verified_by_operator`; Round 3 record is accepted|Recommendations must respect these decisions|
|Current architecture lacks progressive disclosure|**Incorrect**|Step 3 defines exact disclosure order|Treat as already implemented, not a new recommendation|
|Compact machine handoff is absent|**Incorrect**|Shared anatomy defines it; Round 3 defines exact handoffs|No new universal handoff schema needed|
|Provenance/freshness/confidence block is absent|**Incorrect or overstated**|Step 3 already defines compact sources, freshness, confidence, assumptions|Only artifact-specific refinement may remain|
|Candidate and accepted state are insufficiently separated|**Mostly incorrect**|Root and Step 3 make the boundary explicit|Event sourcing is unnecessary as a replacement architecture|
|Flow context may still be duplicated across large prompt packs|**Superseded**|Round 3 rejects the large pack and adopts simple prompt files|Do not reopen J4-J5|
|Evidence normalization may be mandatory|**Superseded**|J6 explicitly makes normalization conditional|Report recommendation is already implemented|
|Skip marker needs a first-class card/template architecture|**Overengineered**|Skip marker is low priority, inline or tiny|Preserve minimal record|
|One canonical structured source should replace the system|**Conflicts with repo authority**|Existing contracts remain schema owners; Step 3 is presentation only|Reject universal replacement schema|
|HTML should be the default operator view|**Unverified product assumption**|Markdown and relative links are current verified design|Defer until operator value is demonstrated|
|Report architecture scores `72 → 91`|**Not authoritative**|Scores were produced without live repo inspection|Exclude from decision-making|
|Proposed file trees and scripts reflect current repository needs|**Candidate only**|Proposed operator-output scripts were not found; exact package tree differs|Evaluate scripts individually, not as a package mandate|
|J11 should perhaps be per-project rather than portfolio|**Conflicts with verified J11 job**|J11 is the cross-project active landscape|Do not reopen without Marco explicitly changing J11|
|Missing prompt should block execution with no fallback prompt|**Too absolute**|Current design exposes degraded/missing prompt state but existing skill contracts retain authority|Handle through owning prompt/flow contract, not a universal rule|
|Approval should become stale whenever a diff changes|**Useful but not yet verified**|Candidate-state visibility exists; stale-approval semantics are not locked|Genuine candidate decision, not current fact|
|FlowRecap result-card design in the current template proves acceptance|**False due to contamination**|Commit `973a...` is unauthorized candidate material|Do not use current template as operator acceptance evidence|
|Current realistic FlowRecap example proves accepted output design|**False due to contamination**|Commit `443c...` is unauthorized candidate material|Treat example content as test material only|
|The unauthorized changes reflect Step 3 Round 4 completion|**False**|The commits themselves describe partial/incomplete work|They cannot advance verified design state|

## Unauthorized-commit impact

### Commit `973a137...`

The commit changed the FlowRecap template from a schema-forward packet into a result-card-first operator projection. That direction is compatible with the locked Step 2/3 principles, but compatibility is not acceptance. Its diff must be treated as candidate design evidence only.

### Commit `443c15b...`

The commit replaced the minimal synthetic example with a realistic partial-execution result card and even preselected an operator approval checkbox. It is useful as a stress-test candidate, but it cannot establish an accepted workflow, accepted state update, or completed Round 4 design.

Neither file was reverted or modified.

---

# Part 5 — Research-derived candidate decisions for Marco

## D1 — Deterministic validation as a design requirement

```yaml
operator_decision:
  id: D1
  question: >
    Should every future operator template be required to support read-only,
    deterministic checks for required fields, references, links, and candidate
    state labels?
  why_it_matters: >
    This prevents mechanical drift without handing semantic judgment or state
    mutation to scripts.
  research_support: >
    Both reports identify structural validation as high-value and low-risk.
  repository_context: >
    Step 3 already defines acceptance checks, but no shared operator-output
    validation layer was verified.
  recommended_default: change
  options:
    A: >
      Make deterministic structural validation a shared design requirement,
      derived from existing contracts.
    B: >
      Keep validation entirely inside each skill and defer a shared requirement.
  no_decision_consequence: >
    Step 3 can continue, but future templates may implement validation unevenly.
```

## D2 — Stale approval after candidate changes

```yaml
operator_decision:
  id: D2
  question: >
    When a candidate status or KB diff changes materially after operator review,
    should the previous approval automatically become invalid?
  why_it_matters: >
    It prevents changed content from inheriting approval given to an older
    proposal.
  research_support: >
    The reports derive this from modern review and protected-change practices.
  repository_context: >
    Candidate and accepted state are already separate, but stale-approval
    semantics are not explicitly locked.
  recommended_default: investigate
  options:
    A: >
      Invalidate approval after any material candidate diff change.
    B: >
      Preserve approval unless a high-impact field changes.
  no_decision_consequence: >
    Existing explicit approval remains safe, but the handling of edited approved
    candidates stays ambiguous.
```

## D3 — HTML as a generated secondary view

```yaml
operator_decision:
  id: D3
  question: >
    Should lightweight HTML remain explicitly deferred until the Markdown
    templates have been operator-tested and stabilized?
  why_it_matters: >
    Early HTML work could create a second presentation system before the content
    and navigation have proven useful.
  research_support: >
    The reports find HTML potentially useful for accessibility and layout
    consistency, but neither verified current operator need.
  repository_context: >
    Current design already supports cards, short sections, headings, direct
    relative links, and visible path fallbacks in Markdown.
  recommended_default: defer
  options:
    A: >
      Keep Markdown canonical and defer HTML until stable templates exist.
    B: >
      Prototype an HTML projection during template validation.
  no_decision_consequence: >
    The operator-design work continues normally in Markdown with no lost
    functionality.
```

Only these three questions represent current product-direction choices. The remaining report ideas are either already locked, safely narrowed by existing ownership, or clearly later-stage tooling.

---

# Part 6 — No-change conclusions

The following research ideas require **no repository redesign** because APEX already implements or locks them:

- **Result card first.**
    
- **Usefulness within the first ten seconds.**
    
- **What changed/current, what next, what needs review.**
    
- **Human-readable operator view before machine payload.**
    
- **Cards, short lists, and compact sections instead of wide-table-first output.**
    
- **Progressive disclosure.**
    
- **Compact provenance and confidence on demand.**
    
- **Candidate state visibly separate from accepted state.**
    
- **Explicit approval before durable change.**
    
- **Existing skill contracts remain schema authority.**
    
- **One primary Flow Execution Card per flow.**
    
- **One simple file per prompt.**
    
- **Lightweight prompt index.**
    
- **Prompt content owned by Prompt Engineering.**
    
- **Routing rationale owned by AI Routing.**
    
- **References instead of repeated context.**
    
- **Evidence normalization only when evidence complexity requires it.**
    
- **Simple structured evidence can go directly to FlowRecap.**
    
- **FlowRecap remains the interpretation and candidate-delta owner.**
    
- **Skip marker stays minimal and low priority.**
    
- **No runtime, agents, schedulers, automatic calendar work, or silent state mutation in the current mechanism.**
    

The Round 3 record is especially decisive: it verifies the simplified J4-J6 relationship and rejects the large repetitive alternative.

```yaml
completion_gate:
  both_reports_read_completely: true
  live_repo_used_as_current_state_authority: true
  operator_verified_decisions_preserved: true
  unauthorized_commits_not_treated_as_accepted_design: true
  report_repo_claims_independently_verified: true
  significant_recommendations_deduplicated: true
  every_recommendation_classified: true
  every_classification_has_repository_evidence: true
  universal_schema_proposal_evaluated_critically: true
  deterministic_validation_rendering_and_mutation_separated: true
  no_repository_mutation_performed: true
  no_implementation_or_patch_created: true
  no_more_than_five_operator_decisions: true
```