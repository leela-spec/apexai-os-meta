# APEX Orchestration State Packet

Use this template to create a compact state handoff from existing APEX project-management packages into PreCapWeek and PreCapNextDay.

Do not expose the full project database here. Use refs, short digests, confidence notes, and operator review flags.

## Packet Status

```yaml
packet_status:
  packet_id: apex_orchestration_state_packet_<YYYY_MM_DD>_<slug>
  artifact_name: apex_orchestration_state_packet
  created_or_updated_at: <YYYY-MM-DD>
  source_status: <verified_repo_sources|mixed_verified_and_synthetic|synthetic_example|partial_context|stale_context>
  validation_status: <valid|valid_with_warnings|synthetic_example|blocked_by_missing_state_source|operator_review_required>
```

**Packet role:** compact state handoff to PreCapWeek and PreCapNextDay.

**Source note:** <one or two sentences describing whether this packet is verified, partial, stale, or synthetic>

## Source Package Status

```yaml
source_package_status:
  apex_plan: <verified_current>
  project_kb_manager: <verified_current>
  ProjectStatus: <verified_current>
  apex_kb: <verified_current|missing>
  apex_sync: <verified_current|extraction_report_only|missing>
  apex_session: <verified_current|extraction_report_only|missing>
```

- **Verified sources used:** <short refs>
- **Missing sources:** <explicit missing source list or `none`>
- **Candidate / unpromoted sources:** <explicit list or `none`>
- **Synthetic data present:** <yes/no; if yes, label every synthetic section>

## Operator Review First

```yaml
operator_review_first:
  review_needed: <true|false>
  highest_risk_flags:
    - <flag or none>
  decisions_needed:
    - <decision or none>
```

### Review cards

**Card 1 — <flag title>**
- **Owner:** <source package or operator>
- **Why it matters:** <brief reason>
- **Decision needed:** <operator action or `none`>

**Card 2 — <flag title or remove>**
- **Owner:** <source package or operator>
- **Why it matters:** <brief reason>
- **Decision needed:** <operator action or `none`>

## Project KB Snapshot

```yaml
snapshot:
  owner: project-kb-manager
  source_refs:
    - <registry/project-record/next-precap-context ref>
  source_state: <verified|partial|stale|missing|synthetic>
```

**Active project record refs**
- `<project-id>` — <record ref or missing>

**Milestone summary**
- <compact milestone signal; no full milestone schema>

**Next PreCap context**
- <compact next_precap_context digest or missing-source note>

**Operator review needed flags**
- <flag or none>

## Project Status Snapshot

```yaml
snapshot:
  owner: ProjectStatus
  source_refs:
    - <current_project_status_overview ref>
  source_state: <verified|partial|stale|missing|synthetic>
```

**Compact status snapshot**
- <project/status digest>

**Ranked task digest**
- <ranked item 1>
- <ranked item 2>
- <ranked item 3>

**Unresolved unassigned digest**
- <unassigned item or none>

**Status review flags**
- <flag or none>

## Planning Snapshot

```yaml
snapshot:
  owner: apex-plan
  source_refs:
    - <apex_plan_packet ref or planning note ref>
  source_state: <verified|partial|stale|missing|synthetic>
```

**Proposed task summary**
- <compact qualitative planning signal>

**Unresolved planning questions**
- <question or none>

**Qualitative focus signal**
- <signal; do not compute exact next-task order>

## Sync Snapshot

```yaml
snapshot:
  owner: apex-sync
  source_package_promotion_status: <verified_current|extraction_report_only|missing>
  source_refs:
    - <sync package/ref or extraction report ref>
  source_state: <verified|candidate|missing|synthetic>
```

**Sync status**
- <status or `not available`>

**Registry status**
- <status or `not available`>

**Drift flags**
- <flag or none>

**Computed focus candidates**
- <candidate only if verified; otherwise mark unavailable/candidate>

## Session Snapshot

```yaml
snapshot:
  owner: apex-session
  source_package_promotion_status: <verified_current|extraction_report_only|missing>
  source_refs:
    - <session package/ref or extraction report ref>
  source_state: <verified|candidate|missing|synthetic>
```

**Latest session summary**
- <summary or missing>

**Next session context ref**
- <ref or missing>

**Pending mutation flags**
- <flag or none>

**Session delta summary**
- <summary or unavailable>

## Evidence Snapshot

```yaml
snapshot:
  owner: apex-kb
  source_refs:
    - <source map, artifact index, KB query, or retrieval ref>
  source_state: <verified|partial|stale|missing|synthetic>
```

**Source map refs**
- <ref or missing>

**Artifact index refs**
- <ref or missing>

**KB query refs**
- <ref or none>

**Evidence confidence notes**
- <confidence note or none>

## Weekly Planning View

Consumed by: **PreCapWeek**

```yaml
weekly_planning_view:
  source_confidence_summary: <high|medium|low|unknown>
  weekly_priority_candidates:
    - <candidate project / focus>
  active_project_candidates:
    - <project ref>
  cross_project_constraints:
    - <constraint or none>
  operator_decisions_needed:
    - <decision or none>
```

**Weekly planning cards**

**<Candidate 1>**
- **Why this week:** <reason>
- **Source confidence:** <high|medium|low|unknown>
- **Owner source:** <project-kb-manager|ProjectStatus|apex-plan|apex-sync|apex-session|apex-kb|synthetic>

## Next-Day Planning View

Consumed by: **PreCapNextDay**

```yaml
next_day_planning_view:
  source_confidence_summary: <high|medium|low|unknown>
  next_day_focus_candidates:
    - <candidate>
  flow_candidate_inputs:
    F1:
      candidate_project: <project>
      candidate_focus: <focus>
    F2:
      candidate_project: <project>
      candidate_focus: <focus>
    F3:
      candidate_project: <project>
      candidate_focus: <focus>
    F4:
      candidate_project: <project>
      candidate_focus: <focus>
  immediate_blockers:
    - <blocker or none>
  prompt_or_workflow_preparation_needs:
    - <need or none>
  review_flags_for_daily_plan:
    - <flag or none>
```

**Daily planning cards**

**F1 — <candidate_project>**
- **Candidate focus:** <focus>
- **Inputs available:** <short list>
- **Missing / weak inputs:** <short list or none>
- **Review before planning:** <yes/no + why>

**F2 — <candidate_project>**
- **Candidate focus:** <focus>
- **Inputs available:** <short list>
- **Missing / weak inputs:** <short list or none>
- **Review before planning:** <yes/no + why>

**F3 — <candidate_project>**
- **Candidate focus:** <focus>
- **Inputs available:** <short list>
- **Missing / weak inputs:** <short list or none>
- **Review before planning:** <yes/no + why>

**F4 — <candidate_project>**
- **Candidate focus:** <focus>
- **Inputs available:** <short list>
- **Missing / weak inputs:** <short list or none>
- **Review before planning:** <yes/no + why>

## Validation Gate

```yaml
validation_gate:
  packet_id_matches_format: <true|false>
  source_status_allowed_value: <true|false>
  source_package_status_present: <true|false>
  each_snapshot_has_owner: <true|false>
  project_schema_not_redefined: <true|false>
  ProjectStatus_not_replaced: <true|false>
  apex_plan_not_replaced: <true|false>
  sync_and_session_candidate_status_preserved_when_unpromoted: <true|false>
  PreCapWeek_consumption_view_present: <true|false>
  PreCapNextDay_consumption_view_present: <true|false>
  synthetic_data_labeled_when_present: <true|false>
  no_runtime_agents_cron_calendar_or_status_merge_created: <true|false>
  final_validation_status: <valid|valid_with_warnings|synthetic_example|blocked_by_missing_state_source|operator_review_required>
```

**Validation notes**
- <note or none>
