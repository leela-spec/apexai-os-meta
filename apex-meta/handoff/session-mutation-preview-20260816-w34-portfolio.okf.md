```okf
okf:
  id: "session-mutation-preview-20260816-w34-portfolio"
  version: 1.0
  status: awaiting_operator_confirmation_under_current_session_contract
  document_role: apex_session_batch_mutation_preview
  created: 2026-08-16
  repository: leela-spec/apexai-os-meta
  branch: main
  source_basis:
    - apex-meta/handoff/weekly-project-management-next-steps-handover-20260816.okf.md
    - apex-meta/handoff/plan-packets/portfolio-project-capture-index-20260816-2026-W34.md
    - apex-meta/handoff/plan-packets/apex_plan_packet-20260816-leela-core-interaction-development-v2.md
    - apex-meta/handoff/plan-packets/apex_plan_packet-20260816-leela-product-decisions.md
    - apex-meta/handoff/plan-packets/apex_plan_packet-20260816-leela-project-management-cleanup.md
    - apex-meta/handoff/plan-packets/apex_plan_packet-20260816-masterofarts-website-definition.md
    - apex-meta/handoff/plan-packets/apex_plan_packet-20260816-transendance-concept.md
    - apex-meta/handoff/plan-packets/apex_plan_packet-20260816-business-invoicing.md
    - apex-meta/handoff/plan-packets/apex_plan_packet-20260816-apex-kb-evolution.md
    - apex-meta/handoff/plan-packets/apex_plan_packet-20260816-investment-intelligence-automation.md
    - apex-meta/handoff/plan-packets/apex_plan_packet-20260816-apartment-improvements.md
    - operator approval in current workflow

session_mutation_preview:
  mutation_type: create_new_canonical_project_state

  before:
    canonical_epics_root: apex-meta/epics/
    existing_epics_observed:
      - narm-support-knowledgebase
    approved_portfolio_slugs_already_present: []
    collision_detected: false

  after:
    new_epics: 9
    new_tasks: 54
    total_new_files: 63

  canonical_convention:
    epic_file: epic.md
    task_files: zero_padded_three_digit_ids

  invariants:
    - all newly created tasks start with status open
    - preserve packet priorities exactly
    - preserve null due dates
    - preserve explicit depends_on values
    - preserve blocked_by and unresolved review flags
    - preserve source references
    - do not resolve open operator questions
    - do not create Dating tasks
    - do not duplicate existing Apex weekly-flow or PM-infrastructure initiatives
    - do not invent deadlines priorities task completion or operator answers

  create_manifest:

    leela-core-interaction-development:
      directory: apex-meta/epics/leela-core-interaction-development/
      epic:
        file: epic.md
        title: Leela Core Interaction Development
        status: open
        priority: high
      tasks:
        - {file: 001.md, title: Verify Home runtime against current Home screen contract}
        - {file: 002.md, title: Verify bounded spatial Skill Tree runtime}
        - {file: 003.md, title: Promote bounded cluster to primary Skill Tree navigation}
        - {file: 004.md, title: Make canonical ScopeSelection handoff origin-aware}
        - {file: 005.md, title: Quarantine fake and legacy scope-resolution state from the integrated path}
        - {file: 006.md, title: Reconcile ResolutionRequest and ResolutionContext with current Home and Skill Tree contracts}
        - {file: 007.md, title: Build Home request adapter into frozen resolution context}
        - {file: 008.md, title: Validate Home to Skill Tree to frozen resolution-context vertical slice}
      semantic_boundary: >
        Start from the existing Home and bounded spatial Skill Tree implementations.
        Do not model this as greenfield Home or Skill Tree development.

    leela-product-decisions:
      directory: apex-meta/epics/leela-product-decisions/
      epic:
        file: epic.md
        title: Close Leela Decisions and Questions
        status: open
        priority: high
      tasks:
        - {file: 001.md, title: Reconcile stale decision-ledger state against authoritative decision records}
        - {file: 002.md, title: Prepare and close QA-02 and QA-11 resolution-profile decisions}
        - {file: 003.md, title: Prepare and close QA-100 Home override persistence}
        - {file: 004.md, title: Close QA-138 spatial accessibility fallback policy after bounded-cluster verification}
        - {file: 005.md, title: Close QA-73 Harmonization ownership and namespace disposition}
        - {file: 006.md, title: Evidence-sweep and close Sequencing and Builder decision cluster}
        - {file: 007.md, title: Evidence-sweep and close Path Stats and policy decision cluster}
        - {file: 008.md, title: Reconcile source-integrity and stale-plan decision debt}
        - {file: 009.md, title: Create operator-facing decision batches and closure cadence}
      preserved_operator_gates:
        - QA-02_and_QA-11_actual_choice
        - QA-100_actual_choice
        - QA-138_global_policy_choice
        - QA-73_architectural_status_choice

    leela-project-management-cleanup:
      directory: apex-meta/epics/leela-project-management-cleanup/
      epic:
        file: epic.md
        title: Leela Project Management Cleanup
        status: open
        priority: medium
      tasks:
        - {file: 001.md, title: Inventory and classify Leela project-control artifacts}
        - {file: 002.md, title: Define and publish one current Leela project-control authority map}
        - {file: 003.md, title: Retire or annotate stale Spatial Opus control instructions}
        - {file: 004.md, title: Consolidate active Leela projects into central Apex project records}
        - {file: 005.md, title: Reconcile runtime Micro packets with Apex project task identity}
        - {file: 006.md, title: Verify decluttered Leela restart path}
      semantic_boundary: preserve_history_and_do_not_mass_delete

    masterofarts-website-definition:
      directory: apex-meta/epics/masterofarts-website-definition/
      epic:
        file: epic.md
        title: MasterOfArts Website Definition
        status: open
        priority: medium
      tasks:
        - {file: 001.md, title: Locate and establish current website-definition source}
        - {file: 002.md, title: Reconcile website purpose audience and primary conversion outcomes}
        - {file: 003.md, title: Define website information architecture and page responsibilities}
        - {file: 004.md, title: Define page-level content and interaction requirements}
        - {file: 005.md, title: Review website definition for consistency and implementation readiness}
      preserved_review_flags:
        - source_baseline_missing

    transendance-concept:
      directory: apex-meta/epics/transendance-concept/
      epic:
        file: epic.md
        title: TransenDance Concept
        status: open
        priority: medium
      tasks:
        - {file: 001.md, title: Distill TransenDance core promise and experiential arc}
        - {file: 002.md, title: Define TransenDance module set and module purposes}
        - {file: 003.md, title: Define event progression timing logic and transitions}
        - {file: 004.md, title: Define facilitation and safety boundaries for the concept draft}
        - {file: 005.md, title: Assemble TransenDance concept draft with modules and timeline}
      semantic_boundary:
        - do_not_invent_event_duration
        - do_not_invent_audience_venue_pricing_or_commercialization_model
        - do_not_make_ungrounded_therapeutic_or_medical_claims

    business-invoicing:
      directory: apex-meta/epics/business-invoicing/
      epic:
        file: epic.md
        title: Business Invoicing
        status: open
        priority: medium
      tasks:
        - {file: 001.md, title: Create and send Martial Arts invoice}
        - {file: 002.md, title: Create and send AkiiByte invoice}
        - {file: 003.md, title: Create and send AI Consulting invoice}
        - {file: 004.md, title: Verify invoice ledger and numbering after all three invoices}
      semantic_boundary:
        - no_ranking_among_three_invoices_invented
        - exact_commercial_fields_must_come_from_source_or_operator

    apex-kb-evolution:
      directory: apex-meta/epics/apex-kb-evolution/
      epic:
        file: epic.md
        title: ApexKB Alternatives or Upgrade
        status: open
        priority: medium
      tasks:
        - {file: 001.md, title: Re-baseline current ApexKB implementation and contract}
        - {file: 002.md, title: Build operator-value and retrieval benchmark for ApexKB}
        - {file: 003.md, title: Evaluate cheapest credible ApexKB upgrade path}
        - {file: 004.md, title: Evaluate current ApexKB alternatives and hybrid options}
        - {file: 005.md, title: Run controlled ApexKB versus alternative comparison}
        - {file: 006.md, title: Decide ApexKB continue freeze replace or hybrid direction}
        - {file: 007.md, title: Pilot chosen ApexKB evolution path before broad migration}
      semantic_boundary:
        - do_not_assume_custom_upgrade_is_preferred
        - task_006_requires_operator_decision

    investment-intelligence-automation:
      directory: apex-meta/epics/investment-intelligence-automation/
      epic:
        file: epic.md
        title: Investment Intelligence and Decision Automation
        status: open
        priority: medium
      tasks:
        - {file: 001.md, title: Define investment video-discovery contract}
        - {file: 002.md, title: Configure and test OpenClaw Cron video-search job}
        - {file: 003.md, title: Define investment alert contract and signal thresholds}
        - {file: 004.md, title: Implement and test investment alert loop}
        - {file: 005.md, title: Define portfolio and trading decision-feedback record}
        - {file: 006.md, title: Automate decision-feedback collection and review}
        - {file: 007.md, title: Validate integrated investment intelligence loop}
      semantic_boundary:
        - three_workstreams_equal_operator_priority
        - no_autonomous_trade_execution_authority
        - do_not_invent_topics_thresholds_delivery_channels_or_positions

    apartment-improvements:
      directory: apex-meta/epics/apartment-improvements/
      epic:
        file: epic.md
        title: Apartment Improvements
        status: open
        priority: medium
      tasks:
        - {file: 001.md, title: Resolve apartment art item}
        - {file: 002.md, title: Resolve washing machine item}
        - {file: 003.md, title: Resolve plumbing item}
      semantic_boundary:
        - exact_outcomes_remain_unknown_until_execution
        - no_ranking_or_deadline_invented

  explicit_non_mutations:
    dating:
      action: none
      reason: weekly_capacity_input_only
    first-real-weekly-flow:
      action: none
      reason: existing_FEE2_weekly_orchestration_initiative
    first-apex-plan-sync-session-project-management:
      action: none
      reason: existing_project_management_infrastructure_initiative
    apex-gate-policy-redesign:
      action: none
      reason: separate_independent_validation_handover_not_part_of_this_portfolio_mutation

next_sequence_after_confirmation:
  - apply exact canonical epic and task writes represented by this preview
  - refresh Apex Session H6 handoff and planning feed as required by current contract
  - run Apex Sync deterministic validation on canonical task files
  - route structural corrections through the correct Plan or Session authority
  - generate artifacts/weekly-plans/project-status-overview-20260816.md
  - collect week-specific W34 inputs
  - run PreCap Week G1
  - stop at G1 operator gate

current_gate:
  authority: apex-session
  required_under_current_contract: explicit operator confirmation of this exact preview
  accepted_confirmation_token: confirmed
  mutation_applied: false
```
