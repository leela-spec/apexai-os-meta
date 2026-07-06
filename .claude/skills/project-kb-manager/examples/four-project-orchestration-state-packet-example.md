# Four-Project APEX Orchestration State Packet Example

```yaml
example_metadata:
  source_status: synthetic_example
  repo_verified: false
  purpose: test_fixture_for_PreCapWeek_and_PreCapNextDay_consumption
  warning: >
    This file contains synthetic but plausible data only. It is a test fixture
    for downstream consumption. Do not treat project names, phases, priorities,
    blockers, or flow candidates as verified project state.
```

## Packet Status

```yaml
packet_status:
  packet_id: apex_orchestration_state_packet_2026_07_06_four_project_fixture
  artifact_name: apex_orchestration_state_packet
  created_or_updated_at: 2026-07-06
  source_status: synthetic_example
  repo_verified: false
  purpose: test_fixture_for_PreCapWeek_and_PreCapNextDay_consumption
  validation_status: synthetic_example
```

**Packet role:** Compact synthetic handoff fixture for PreCapWeek and PreCapNextDay consumption tests.

**Synthetic warning:** Every project, phase, priority, focus candidate, blocker, and confidence note below is synthetic example data.

## Source Package Status

```yaml
source_package_status:
  apex_plan: verified_current
  project_kb_manager: verified_current
  ProjectStatus: verified_current
  apex_kb: verified_current
  apex_sync: extraction_report_only
  apex_session: extraction_report_only
```

- **Verified project records used:** none; this is synthetic example data.
- **Repo verification for project data:** false.
- **Candidate / unpromoted source packages:** apex-sync and apex-session are shown as extraction-report-only for fixture realism.
- **Synthetic data present:** yes; all project and planning content is synthetic.

## Operator Review First

```yaml
operator_review_first:
  review_needed: true
  highest_risk_flags:
    - synthetic_project_state_not_verified
    - apex_sync_and_apex_session_are_extraction_report_only_in_fixture
    - flow_candidate_order_is_test_fixture_not_final_policy
  decisions_needed:
    - Confirm whether this packet shape is narrow enough for PreCapWeek and PreCapNextDay consumption testing.
    - Confirm whether four-project flow candidates should remain example-only or become a future planning convention.
```

**Card 1 — Synthetic project state**
- **Owner:** operator
- **Why it matters:** The packet tests structure only and does not verify real project status.
- **Decision needed:** Do not promote fixture data into durable project records.

**Card 2 — Unpromoted sync/session packages**
- **Owner:** apex-sync / apex-session
- **Why it matters:** Computed focus and session deltas are not trusted as current unless those packages are promoted.
- **Decision needed:** Treat sync/session values as unavailable or candidate-only.

## Project KB Snapshot

```yaml
snapshot:
  owner: project-kb-manager
  source_state: synthetic
  source_refs:
    - synthetic_fixture:four_project_example
```

**Synthetic project candidates**

**P01 — AI Orchestration / APEX**
- **Domain type:** dev
- **Repo ref:** `leela-spec/apexai-os-meta`
- **Current phase:** state_handoff_template_buildout
- **Synthetic status summary for PreCap:** Build the compact state packet layer so weekly and daily planning can consume real project state later.
- **Operator review needed:** true

**P02 — Coaching Business**
- **Domain type:** business
- **Repo ref:** `<coaching-business-repo-placeholder>`
- **Current phase:** website_and_billing_foundation
- **Synthetic status summary for PreCap:** Create the website, offer, and billing foundation needed to convert project work into usable business infrastructure.
- **Operator review needed:** true

**P03 — Investment Dashboard**
- **Domain type:** investment
- **Repo ref:** `<investment-repo-placeholder>`
- **Current phase:** dashboard_information_architecture
- **Synthetic status summary for PreCap:** Define dashboard information architecture and source mapping before implementation work.
- **Operator review needed:** true

**P04 — Leka / LIKA Social Initiative**
- **Domain type:** business
- **Repo ref:** `<lika-repo-placeholder>`
- **Current phase:** accounting_tax_process_support
- **Synthetic status summary for PreCap:** Consolidate accounting and tax process support with explicit validation questions and documentation risk flags.
- **Operator review needed:** true

**Milestone summary**
- P01: synthetic milestone `M1` — state packet contract, template, example, and manifest index.
- P02: synthetic milestone `M1` — sitemap and offer/billing skeleton.
- P03: synthetic milestone `M1` — information architecture sketch and source inventory.
- P04: synthetic milestone `M1` — accounting/tax checklist and open validation questions.

**Next PreCap context**
- Use P01 first to stabilize the handoff layer, then test whether P02–P04 can be planned without inventing project state.

## Project Status Snapshot

```yaml
snapshot:
  owner: ProjectStatus
  source_state: synthetic
  source_refs:
    - synthetic_fixture:compact_project_status_digest
```

**Compact status snapshot**
- AI Orchestration / APEX — state packet glue layer active; schema-boundary risk high until packet is reviewed.
- Coaching Business — foundation phase; source detail missing; needs sitemap and billing skeleton before deeper planning.
- Leka / LIKA — compliance/documentation risk; needs checklist consolidation and validation questions.
- Investment Dashboard — useful but lower urgency; defer unless residual capacity exists.

**Ranked task digest**
1. AI Orchestration / APEX — build contract, template, and example fixture for state handoff.
2. Coaching Business — draft website sitemap and offer/billing skeleton.
3. Leka / LIKA — consolidate accounting/tax checklist and validation questions.
4. Investment Dashboard — sketch dashboard information architecture or defer.

**Unresolved unassigned digest**
- None in fixture; all synthetic items are assigned to one of the four projects.

**Status review flags**
- All ratings and rankings are synthetic.
- Flow candidate order is a fixture, not a final F1-F4 policy.

## Planning Snapshot

```yaml
snapshot:
  owner: apex-plan
  source_state: synthetic
  source_refs:
    - synthetic_fixture:planning_signal_digest
```

**Proposed task summary**
- Create the `apex_orchestration_state_packet` contract, blank template, and four-project example as a narrow bridge between existing package owners and downstream planning skills.

**Unresolved planning questions**
- Should the packet remain inside `project-kb-manager` as a reference/template layer or later become its own package?
- Should PreCapWeek and PreCapNextDay consume only the packet views or also read underlying project records when confidence is low?

**Qualitative focus signal**
- Prioritize P01 first because it reduces planning hallucination risk for every downstream weekly/daily planning run.

## Sync Snapshot

```yaml
snapshot:
  owner: apex-sync
  source_package_promotion_status: extraction_report_only
  source_state: candidate
  source_refs:
    - .claude/skills/apex-sync/apex-sync-final-extraction-report.md
```

**Sync status**
- Candidate-only in this fixture.

**Registry status**
- Not computed by this fixture.

**Drift flags**
- `fixture_uses_synthetic_priority_order`
- `computed_focus_candidates_not_verified`

**Computed focus candidates**
- Unavailable. The priority digest below is synthetic and qualitative, not apex-sync computation.

## Session Snapshot

```yaml
snapshot:
  owner: apex-session
  source_package_promotion_status: extraction_report_only
  source_state: candidate
  source_refs:
    - .claude/skills/apex-session/apex-session-final-extraction-report.md
```

**Latest session summary**
- Synthetic fixture assumes no verified latest session summary.

**Next session context ref**
- Missing in fixture.

**Pending mutation flags**
- None claimed; this file performs no mutations.

**Session delta summary**
- Unavailable. No session delta is created by this fixture.

## Evidence Snapshot

```yaml
snapshot:
  owner: apex-kb
  source_state: synthetic
  source_refs:
    - synthetic_fixture:evidence_snapshot
```

**Source map refs**
- No verified source map used for project data.

**Artifact index refs**
- This example file is the only artifact under test.

**KB query refs**
- None.

**Evidence confidence notes**
- Confidence in the packet structure: medium for testing.
- Confidence in project facts: low because project data is synthetic and repo_verified is false.

## Weekly Planning View

Consumed by: **PreCapWeek**

```yaml
weekly_planning_view:
  source_confidence_summary: low_for_project_facts_medium_for_template_structure
  weekly_priority_candidates:
    - AI Orchestration / APEX: finish state handoff packet buildout
    - Coaching Business: create website and billing foundation skeleton
    - Leka / LIKA: reduce accounting and tax process documentation risk
    - Investment Dashboard: keep as lower-risk architecture/source-mapping candidate
  active_project_candidates:
    - P01
    - P02
    - P04
    - P03
  cross_project_constraints:
    - Do not let PreCapWeek invent detailed project state from this fixture.
    - Treat source confidence as low until real project records are loaded.
  operator_decisions_needed:
    - Confirm project priority order before weekly plan creation.
    - Confirm whether Investment Dashboard should remain residual/deferred.
```

**Weekly planning cards**

**AI Orchestration / APEX**
- **Why this week:** Stabilizes the state handoff layer required by weekly and daily planning.
- **Source confidence:** low for facts, medium for template test value.
- **Owner source:** synthetic fixture referencing project-kb-manager packet structure.

**Coaching Business**
- **Why this week:** Website and billing foundation can turn project work into practical business infrastructure.
- **Source confidence:** low.
- **Owner source:** synthetic fixture.

**Leka / LIKA**
- **Why this week:** Accounting/tax process support has compliance and documentation risk.
- **Source confidence:** low.
- **Owner source:** synthetic fixture.

**Investment Dashboard**
- **Why this week:** Valuable but can start with lower-risk architecture and source mapping.
- **Source confidence:** low.
- **Owner source:** synthetic fixture.

## Priority Digest

```yaml
priority_digest:
  1:
    project: AI Orchestration / APEX
    reason: Build the glue packet so the orchestration system can plan from real state.
  2:
    project: Coaching Business
    reason: Website and billing foundation can convert project work into practical business infrastructure.
  3:
    project: Leka / LIKA
    reason: Accounting/tax process support has compliance and documentation risk.
  4:
    project: Investment Dashboard
    reason: Valuable but can start with lower-risk architecture and source mapping.
```

This is qualitative synthetic priority logic, not an apex-sync computed ranking.

## Next-Day Planning View

Consumed by: **PreCapNextDay**

```yaml
next_day_planning_view:
  source_confidence_summary: low_for_project_facts_medium_for_template_structure
  next_day_focus_candidates:
    - AI Orchestration / APEX: create apex_orchestration_state_packet contract and template
    - Coaching Business: draft website sitemap and offer/billing skeleton
    - Leka / LIKA: consolidate accounting/tax process checklist and open validation questions
    - Investment Dashboard: sketch dashboard information architecture or defer as residual
  flow_candidate_inputs:
    F1:
      candidate_project: AI Orchestration / APEX
      candidate_focus: create apex_orchestration_state_packet contract and template
    F2:
      candidate_project: Coaching Business
      candidate_focus: draft website sitemap and offer/billing skeleton
    F3:
      candidate_project: Leka / LIKA
      candidate_focus: consolidate accounting/tax process checklist and open validation questions
    F4:
      candidate_project: Investment Dashboard
      candidate_focus: sketch dashboard information architecture or defer as residual
  immediate_blockers:
    - Real project records are not loaded in this fixture.
    - apex-sync and apex-session are candidate/extraction-report-only in this fixture.
  prompt_or_workflow_preparation_needs:
    - Ask PreCapWeek and PreCapNextDay to consume this packet without inventing missing state.
    - Verify that downstream outputs preserve synthetic labels and confidence warnings.
  review_flags_for_daily_plan:
    - synthetic_project_state_not_verified
    - flow_candidate_order_is_test_fixture_not_final_policy
    - do_not_treat_fixture_as_durable_project_kb
```

**Important:** This is not the final F1-F4 policy. It is only a test fixture.

**F1 — AI Orchestration / APEX**
- **Candidate focus:** Create `apex_orchestration_state_packet` contract and template.
- **Inputs available:** synthetic project phase, repo placeholder, qualitative priority reason.
- **Missing / weak inputs:** real project KB record, verified latest status, verified session delta.
- **Review before planning:** yes; confirm synthetic fixture is acceptable for test run only.

**F2 — Coaching Business**
- **Candidate focus:** Draft website sitemap and offer/billing skeleton.
- **Inputs available:** synthetic phase and qualitative reason.
- **Missing / weak inputs:** real repo, source refs, verified active workstreams.
- **Review before planning:** yes; project state is placeholder-only.

**F3 — Leka / LIKA**
- **Candidate focus:** Consolidate accounting/tax process checklist and open validation questions.
- **Inputs available:** synthetic phase and risk reason.
- **Missing / weak inputs:** verified LIKA repo ref, current checklist source, validation owner.
- **Review before planning:** yes; compliance-sensitive project context needs real source refs.

**F4 — Investment Dashboard**
- **Candidate focus:** Sketch dashboard information architecture or defer as residual.
- **Inputs available:** synthetic phase and defer reason.
- **Missing / weak inputs:** verified repo, source map, investment dashboard requirements.
- **Review before planning:** yes; likely residual/deferred unless operator raises priority.

## Validation Gate

```yaml
validation_gate:
  packet_id_matches_format: true
  source_status_allowed_value: true
  source_package_status_present: true
  each_snapshot_has_owner: true
  project_schema_not_redefined: true
  ProjectStatus_not_replaced: true
  apex_plan_not_replaced: true
  sync_and_session_candidate_status_preserved_when_unpromoted: true
  PreCapWeek_consumption_view_present: true
  PreCapNextDay_consumption_view_present: true
  synthetic_data_labeled_when_present: true
  no_runtime_agents_cron_calendar_or_status_merge_created: true
  final_validation_status: synthetic_example
```

**Validation notes**
- This example creates no weekly plan, next-day plan, flow packet, flow prompt pack, FlowRecap output, status merge, runtime agent, cron job, or calendar write.
- All synthetic data is explicitly labeled.
- Downstream consumers must preserve low confidence and must not invent project state.
