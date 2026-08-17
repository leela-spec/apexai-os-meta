```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: all_project_status_packet
  gate: none
  packet_id: "all_project_status_packet-20260816-w34"
  produced_by: apex-project-status
  accountability: meta_ops
  lifecycle_stage: computed
  status: partial
  target_surface: none
  next_state: "W34-only operator context can be collected against the confirmed full-portfolio state."
  prerequisites:
    - apex-meta/handoff/planning-feed-20260816-w34.md
    - apex-meta/handoff/sync-reports/20260816-w34/next.json
    - apex-meta/handoff/sync-reports/20260816-w34/blockers.json
    - apex-meta/handoff/sync-reports/20260816-w34/score.json
  expected_action: "Collect the five W34-only operator inputs, then use this packet as the compact project-status input to PreCap Week G1."
  sources:
    - apex-meta/epics/
    - apex-meta/handoff/planning-feed-20260816-w34.md
    - apex-meta/handoff/sync-reports/20260816-w34/next.json
    - apex-meta/handoff/sync-reports/20260816-w34/blockers.json
    - apex-meta/handoff/sync-reports/20260816-w34/score.json
  uncertainties:
    - "Canonical tasks provide qualitative priority tiers but not 1-100 ProjectStatus priority ratings."
    - "No canonical task has a due_date; numeric urgency is therefore not directly evidenced."
    - "W34 category roles, explicit priority overrides, calendar/capacity constraints, and exclusions remain operator-owned."
    - "NARM is confirmed canonical state but its W34 inclusion is not operator-confirmed; it is represented under Residual as other non-fixed project material until the W34 exclusion question is answered."
  unresolved_risk: "ProjectStatus numeric ratings are provisional schema-compatible translations and must not be treated as W34 operator priority."
  stop_condition: "Do not create weekly direction, infer W34 priorities, mutate canonical task state, or run G1 before the W34-only operator inputs are collected."
  authority:
    state: candidate
    basis_digest: null
    verification_ref: null
  operator_validation: not_requested
```

# Current Project Status Overview — 2026-W34

```yaml
overview_metadata:
  artifact_name: current_project_status_overview
  schema_version: "0.1"
  created_or_updated_at: "2026-08-16"
  overview_status: operator_review_needed
  freshness: "confirmed Session planning feed and committed Sync reports generated 2026-08-16"
  confirmed_task_count: 62
  dependency_validation_review_flags: 0
  sync_next_candidate_count: 8
  ranking_rule: manual_override_then_deadline_first_priority_second_urgency_third
  rating_format: "[priority/urgency/date]"
  rating_basis:
    priority: "provisional translation for ProjectStatus compatibility: canonical high -> 80; canonical medium -> 50"
    urgency: "50 provisional/neutral because canonical due_date is null and no W34 urgency signal has yet been supplied"
    date: "NA because no canonical task has a known fixed due date"
    operator_review_required: true
  scope_rule: "Fixed weekly roster only: Leela, MasterOfArts, Apex, Investment, Residual. Canonical epics are represented as tasks; canonical task records are represented as subtasks."
```

# Project Sections

## Leela

- **core-interaction-development:** Leela Core Interaction Development [80/50/NA]
  --- **001:** Verify Home runtime against current Home screen contract [80/50/NA] — **SYNC NEXT CANDIDATE**; dependencies clear
  --- **002:** Verify bounded spatial Skill Tree runtime [80/50/NA] — **SYNC NEXT CANDIDATE**; dependencies clear
  --- **003:** Promote bounded cluster to primary Skill Tree navigation [80/50/NA] — waits on 001, 002
  --- **004:** Make canonical ScopeSelection handoff origin-aware [80/50/NA] — waits on 003
  --- **005:** Quarantine fake and legacy scope-resolution state from the integrated path [80/50/NA] — waits on 004
  --- **006:** Reconcile ResolutionRequest and ResolutionContext with current Home and Skill Tree contracts [80/50/NA] — waits on 004
  --- **007:** Build Home request adapter into frozen resolution context [80/50/NA] — waits on 005, 006
  --- **008:** Validate Home to Skill Tree to frozen resolution-context vertical slice [80/50/NA] — waits on 003, 004, 005, 006, 007

- **product-decisions:** Close Leela Decisions and Questions [80/50/NA]
  --- **001:** Reconcile stale decision-ledger state against authoritative decision records [80/50/NA] — **SYNC NEXT CANDIDATE**; dependencies clear
  --- **002:** Prepare and close QA-02 and QA-11 resolution-profile decisions [80/50/NA] — blocked: operator_answer_required
  --- **003:** Prepare and close QA-100 Home override persistence [80/50/NA] — blocked: operator_answer_required
  --- **004:** Close QA-138 spatial accessibility fallback policy after bounded-cluster verification [50/50/NA] — blocked: operator_answer_required_for_global_policy
  --- **005:** Close QA-73 Harmonization ownership and namespace disposition [50/50/NA] — blocked: operator_answer_required
  --- **006:** Evidence-sweep and close Sequencing and Builder decision cluster [80/50/NA] — waits on 001
  --- **007:** Evidence-sweep and close Path Stats and policy decision cluster [50/50/NA] — waits on 001
  --- **008:** Reconcile source-integrity and stale-plan decision debt [50/50/NA] — waits on 001
  --- **009:** Create operator-facing decision batches and closure cadence [50/50/NA] — waits on 001

- **project-management-cleanup:** Leela Project Management Cleanup [80/50/NA]
  --- **001:** Inventory and classify Leela project-control artifacts [80/50/NA] — **SYNC NEXT CANDIDATE**; dependencies clear
  --- **002:** Define and publish one current Leela project-control authority map [80/50/NA] — waits on 001
  --- **003:** Retire or annotate stale Spatial Opus control instructions [80/50/NA] — waits on 001, 002
  --- **004:** Consolidate active Leela projects into central Apex project records [80/50/NA] — waits on 002; explicit blocker preserved: operator_approval_of_project_packets
  --- **005:** Reconcile runtime Micro packets with Apex project task identity [50/50/NA] — waits on 002, 004
  --- **006:** Verify decluttered Leela restart path [50/50/NA] — waits on 002, 003, 004, 005

## MasterOfArts

- **website-definition:** MasterOfArts Website Definition [80/50/NA]
  --- **001:** Locate and establish current website-definition source [80/50/NA] — **SYNC NEXT CANDIDATE**; dependencies clear
  --- **002:** Reconcile website purpose audience and primary conversion outcomes [80/50/NA] — waits on 001
  --- **003:** Define website information architecture and page responsibilities [50/50/NA] — waits on 002
  --- **004:** Define page-level content and interaction requirements [50/50/NA] — waits on 003
  --- **005:** Review website definition for consistency and implementation readiness [50/50/NA] — waits on 004

- **transendance-concept:** TransenDance Concept [80/50/NA]
  --- **001:** Distill TransenDance core promise and experiential arc [80/50/NA] — **SYNC NEXT CANDIDATE**; dependencies clear
  --- **002:** Define TransenDance module set and module purposes [80/50/NA] — waits on 001
  --- **003:** Define event progression timing logic and transitions [80/50/NA] — waits on 002
  --- **004:** Define facilitation and safety boundaries for the concept draft [50/50/NA] — waits on 002
  --- **005:** Assemble TransenDance concept draft with modules and timeline [80/50/NA] — waits on 003, 004

- **business-invoicing:** Business Invoicing [50/50/NA]
  --- **001:** Create and send Martial Arts invoice [50/50/NA] — blocked: missing_fields_if_not_present_in_source
  --- **002:** Create and send AkiiByte invoice [50/50/NA] — blocked: missing_month_or_service_period_if_not_confirmed
  --- **003:** Create and send AI Consulting invoice [50/50/NA] — blocked: missing_fields_if_not_present_in_source
  --- **004:** Verify invoice ledger and numbering after all three invoices [50/50/NA] — waits on 001, 002, 003

## Apex

- **apex-kb-evolution:** ApexKB Alternatives or Upgrade [80/50/NA]
  --- **001:** Re-baseline current ApexKB implementation and contract [80/50/NA] — **SYNC NEXT CANDIDATE**; dependencies clear
  --- **002:** Build operator-value and retrieval benchmark for ApexKB [80/50/NA] — waits on 001
  --- **003:** Evaluate cheapest credible ApexKB upgrade path [50/50/NA] — waits on 001, 002
  --- **004:** Evaluate current ApexKB alternatives and hybrid options [50/50/NA] — waits on 001, 002
  --- **005:** Run controlled ApexKB versus alternative comparison [80/50/NA] — waits on 003, 004
  --- **006:** Decide ApexKB continue freeze replace or hybrid direction [80/50/NA] — waits on 005; blocked: operator_decision_required
  --- **007:** Pilot chosen ApexKB evolution path before broad migration [50/50/NA] — waits on 006

**Confirmed process context, not duplicated as canonical project tasks:** the First Real Weekly Flow / FEE2 initiative and the first Apex Plan-Sync-Session project-management lifecycle are already represented by current handoff/control artifacts and are the process currently producing this overview.

## Investment

- **investment-intelligence-automation:** Investment Intelligence and Decision Automation [50/50/NA]
  --- **001:** Define investment video-discovery contract [50/50/NA] — blocked: operator_specific_topics_and_sources_required_during_execution
  --- **002:** Configure and test OpenClaw Cron video-search job [50/50/NA] — waits on 001
  --- **003:** Define investment alert contract and signal thresholds [50/50/NA] — blocked: operator_specific_alert_conditions_required_during_execution
  --- **004:** Implement and test investment alert loop [50/50/NA] — waits on 003
  --- **005:** Define portfolio and trading decision-feedback record [50/50/NA] — blocked: operator_current_decision_process_required_during_execution
  --- **006:** Automate decision-feedback collection and review [50/50/NA] — waits on 005
  --- **007:** Validate integrated investment intelligence loop [50/50/NA] — waits on 002, 004, 006

**Operator constraint preserved:** the three Investment branches (video discovery, alerts, decision feedback) are equal; ProjectStatus does not rank one branch above another.

## Residual

- **apartment-improvements:** Apartment Improvements [50/50/NA]
  --- **001:** Resolve apartment art item [50/50/NA] — blocked: exact_desired_outcome_unknown
  --- **002:** Resolve washing machine item [50/50/NA] — blocked: exact_issue_or_desired_outcome_unknown
  --- **003:** Resolve plumbing item [50/50/NA] — blocked: exact_plumbing_issue_unknown

- **narm-support-knowledgebase:** NARM-Support Therapy Knowledgebase Infrastructure [80/50/NA]
  --- **001:** Define safety and scope boundaries for NARM-support system [80/50/NA] — **SYNC NEXT CANDIDATE**; dependencies clear
  --- **002:** Inventory and classify Therapy source files [80/50/NA] — waits on 001
  --- **003:** Design NARM theory index structure [80/50/NA] — waits on 001, 002
  --- **004:** Design personal psychological material index structure [80/50/NA] — waits on 001, 002
  --- **005:** Define cross-reference model between NARM theory and personal material [50/50/NA] — waits on 003, 004
  --- **006:** Design guided self-exploration flow templates [80/50/NA] — waits on 001, 003, 004, 005
  --- **007:** Design compact NARM therapist session-prep output format [80/50/NA] — waits on 001, 004, 005, 006
  --- **008:** Prepare operator-approved implementation handoff [50/50/NA] — waits on 002, 003, 004, 005, 006, 007

**W34 capacity input, not a project/task:** Dating / Meeting Women — reserve meaningful time only if confirmed in the W34 operator-capacity answer; no task backlog is created.

# Ranked Task View

```yaml
manual_override:
  pin: []
  promote: []
  demote: []
  freeze: []
ranking_note: >
  No fixed deadlines or W34 manual override exist yet. The ProjectStatus ranking therefore
  uses provisional numeric priority first, then provisional urgency, then existing project-section
  order. This ranking is not the Sync focus ordering and is not the W34 weekly plan.
sync_next_candidates:
  - narm-support-knowledgebase:001
  - apex-kb-evolution:001
  - leela-core-interaction-development:001
  - leela-core-interaction-development:002
  - leela-project-management-cleanup:001
  - leela-product-decisions:001
  - masterofarts-website-definition:001
  - transendance-concept:001
```

1. Leela / core-interaction-development: Leela Core Interaction Development [80/50/NA]
2. Leela / product-decisions: Close Leela Decisions and Questions [80/50/NA]
3. Leela / project-management-cleanup: Leela Project Management Cleanup [80/50/NA]
4. MasterOfArts / website-definition: MasterOfArts Website Definition [80/50/NA]
5. MasterOfArts / transendance-concept: TransenDance Concept [80/50/NA]
6. Apex / apex-kb-evolution: ApexKB Alternatives or Upgrade [80/50/NA]
7. Residual / narm-support-knowledgebase: NARM-Support Therapy Knowledgebase Infrastructure [80/50/NA]
8. MasterOfArts / business-invoicing: Business Invoicing [50/50/NA]
9. Investment / investment-intelligence-automation: Investment Intelligence and Decision Automation [50/50/NA]
10. Residual / apartment-improvements: Apartment Improvements [50/50/NA]

# Unassigned

```yaml
unassigned_items: []
```

# Operator Validation

```yaml
operator_validation:
  status: operator_review_needed
  review_flags:
    uncertain_ratings:
      - "All 1-100 priority values are provisional translations of canonical high/medium tiers, not operator W34 ratings."
      - "All urgency values are provisional neutral values because canonical due_date is null and the W34 urgency context has not yet been supplied."
      - "NARM is canonical and Sync-actionable, but its W34 inclusion is not yet confirmed; it is carried under Residual pending the W34 exclusion answer."
    invalid_ratings: []
    invalid_dates: []
    unresolved_unassigned_items: []
    possible_duplicates: []
    unclear_blockers: []
    ranking_conflicts: []
```
