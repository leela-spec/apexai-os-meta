round6_review:  
source_access:  
repository: leela-spec/apexai-os-meta  
branch: main  
files_read:  
- apex-meta/operator-output-design/step3-output-design-system/01-operator-output-design-principles.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/02-shared-card-and-brief-anatomy.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/04-flow-execution-card-design.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/05-prompt-file-and-index-design.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/06-execution-evidence-handoff-design.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/07-skip-marker-low-priority-design.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/08-round3-cross-artifact-relationship.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/09-round3-decision-and-verification-record.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/10-flow-recap-result-card-design.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/11-usage-learning-card-design.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/12-round4-cross-artifact-relationship.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/13-round4-decision-and-verification-record.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/14-status-merge-decision-card-design.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/15-project-kb-update-card-design.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/16-project-status-overview-design.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/17-ai-routing-card-design.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/18-round5-cross-artifact-relationships.okf.yaml  
- apex-meta/operator-output-design/step3-output-design-system/19-round5-decision-and-verification-record.okf.yaml  
missing_or_unresolved_paths:  
- expected: .claude/skills/ProjectStatus/references/project-status-overview-contract.md  
live_path_found: .claude/skills/ProjectStatus/project-status-overview-contract_v2_fixed.md  
status: design_reference_requires_path_correction  
- expected: .claude/skills/ai-routing-and-usage-tracking/SKILL.md  
live_path_found: .claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md  
status: live_folder_and_embedded_canonical_path_differ  
- expected: .claude/skills/ai-routing-and-usage-tracking/references/routing-recommendation-packet-contract.md  
live_package_location: .claude/skills/AIRouting/  
status: exact_reference_file_path_not_independently_fetched_in_this_review  
- absolute_checkout_path: unavailable  
contract_authorities_verified:  
ProjectStatus:  
actual_entrypoint_path: .claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md  
project_task_subtask_hierarchy: verified  
ranking_fields: "[priority/urgency/date]"  
ranking_order:  
- manual_override_if_present  
- deadline_first  
- priority_second  
- urgency_third  
unassigned_behavior: include_only_when_unresolved_items_exist  
operator_validation_flags: include_only_when_relevant  
no_workstreams_boundary: verified  
evidence: >  
The live entrypoint explicitly requires project → task → subtask,  
ranked task output, temporary Unassigned handling, relevant validation  
flags, and forbids workstreams.

```
  AIRouting:
    actual_live_package_path: .claude/skills/AIRouting/
    actual_entrypoint_path: .claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md
    embedded_canonical_path: .claude/skills/ai-routing-and-usage-tracking/SKILL.md
    routing_recommendation_contract_declared_path: references/routing-recommendation-packet-contract.md
    stable_surface_class_policy: verified
    exact_model_verification_policy: >
      Exact or volatile provider/model claims require current verification;
      otherwise stable abstract surface classes must be used.
    evidence: >
      The live skill requires stable surface classes, marks final model
      mapping as deferred, and requires current verification for volatile
      claims. Its routing decision requires selected_surface_class. 
      
      
  status_merge:
    actual_entrypoint_path: .claude/skills/status-merge/SKILL.md
    proposal_only_boundary: verified
    merge_confirmation_fields: >
      The current skill and design expose proposal and review classifications,
      but do not define a durable_write_confirmation_ref for displaying merged.
    accepted_vs_merged_state: >
      Candidate classifications may be accepted within the proposal, but
      durable state remains unwritten until project-kb-manager performs and
      confirms the write.
    evidence: >
      Status Merge produces proposal-only state views and explicitly leaves
      durable writes to project-kb-manager. 
      
      
  project_kb_manager:
    actual_entrypoint_path: .claude/skills/project-kb-manager/SKILL.md
    durable_write_owner: verified
    write_confirmation_or_update_result: update_result
    provenance_requirements: >
      Design requires provenance; live write rules require dated evidence,
      read-before-write, registry synchronization, idempotency and explicit
      operator validation.
    evidence: >
      The skill owns update mode and returns update_result with files changed,
      skipped records, flags and next-PreCap status. 
      
      
      Successful writes require registry synchronization, while uncertain
      fields retain operator review and explicit validation is required to
      clear that state. 
```

decision_matrix:  
R6_01_stale_artifact_names:  
evidence:  
- >  
File 02 still lists Tomorrow_Action_Brief, Flow_Prompt_Pack and  
Raw_Flow_Dump_or_Skip_Marker_Card.  
- >  
Later validated files name J3 PreCap_Next_Day_Brief, J5  
Prompt_Files_and_Index, J6 Execution_Evidence_Handoff, and the Skip  
Marker as a minimal subcase.

```
  proposed_resolution:
    - replace Tomorrow_Action_Brief with PreCap_Next_Day_Brief
    - replace Flow_Prompt_Pack with Prompt_Files_and_Index
    - replace Raw_Flow_Dump_or_Skip_Marker_Card with Execution_Evidence_Handoff
    - add Skip_Marker_as_minimal_subcase separately
  affected_files:
    - 02-shared-card-and-brief-anatomy.okf.yaml
  decision_requested: keep

R6_02_J3_J4_depth_overlap:
  evidence:
    - >
      J3 currently owns a full three-sprint plan including tasks, inputs,
      prompt refs, outputs, dependencies, done conditions and review
      conditions. 
    - >
      J4 independently owns the same full three-sprint execution depth and is
      explicitly the primary operator workspace. 
      
    - >
      The existing cross-artifact rule already permits J3 to summarize flow
      detail while J4 expands it, provided sprint structure remains visible.
      
  proposed_resolution:
    J3:
      role: compact_day_level_three_sprint_outline
      retain:
        - all_represented_flows
        - visible_S1_S2_S3_structure
        - sprint_goal_or_short_intent
        - execution_sequence
        - expected_day_outputs
        - flow_card_refs
      remove_from_primary_depth:
        - complete_task_lists
        - complete_input_lists
        - full_prompt_link_sets
        - detailed_dependencies
        - full_done_conditions
        - full_stop_or_review_conditions
    J4:
      role: complete_three_sprint_execution_workspace
      retain_full_depth: true
  affected_files:
    - 03-planning-artifact-designs.okf.yaml
  decision_requested: keep

R6_03_J11_ProjectStatus_alignment:
  evidence:
    - >
      J11 currently uses active_projects_or_workstreams and a project item
      view that does not expose the live task/subtask hierarchy or ranking
      fields. 
    - >
      The live ProjectStatus contract explicitly forbids workstreams and
      requires project → task → subtask with priority/urgency/date ratings,
      a ranked task view, temporary Unassigned and relevant validation flags.
      
      
      
  proposed_resolution:
    - replace active_projects_or_workstreams with project_task_subtask_projection
    - explicitly forbid workstream creation
    - add ranked_task_attention based on live ranking fields
    - preserve priority_urgency_date semantics
    - include Unassigned only when unresolved items exist
    - include operator validation flags only when relevant
    - preserve current missing/stale/conflicting status behavior
  affected_files:
    - 16-project-status-overview-design.okf.yaml
  decision_requested: keep

R6_04_J12_routing_alignment:
  evidence:
    - >
      J12 currently uses selected_surface_or_model_class and its machine
      handoff requires selected_surface_or_model, leaving exact-model use
      insufficiently constrained. 
      
    - >
      The live routing skill requires selected_surface_class, uses stable
      abstract surface classes and forbids volatile claims without current
      verification. 
      
      
  proposed_resolution:
    recommended_route_view:
      selected_surface_class: required
      verified_model_ref: optional
      exact_model_without_current_verification: forbidden
    compact_machine_handoff:
      replace_selected_surface_or_model_with:
        - selected_surface_class
        - optional_verified_model_ref
    contract_reference_policy:
      use_live_package_path: .claude/skills/AIRouting/
      routing_contract_relative_path: references/routing-recommendation-packet-contract.md
      unresolved_note: retain_path_warning_until_contract_file_is_fetched_and_verified
  affected_files:
    - 17-ai-routing-card-design.okf.yaml
  decision_requested: keep

R6_05_durable_write_confirmation_gap:
  evidence:
    - >
      J9 includes merged as visible state but defines no durable confirmation
      field; it only says unconfirmed execution must remain
      approved_for_merge. 
      
    - >
      J10 distinguishes update preparation from execution but its minimum
      handoff lacks a durable update result reference. 
    - >
      File 18 sends durably merged state directly from J9 to J11, while the
      live ownership chain places durable write execution in
      project-kb-manager/J10. 
      
  proposed_resolution:
    J9:
      merged_display_requires: durable_write_confirmation_ref
      without_confirmation: approved_for_merge
    J10:
      add_output_fields:
        - durable_update_result_ref
        - write_execution_status
        - effective_change
        - updated_freshness
      confirmation_source: project-kb-manager_update_result
    relationship:
      replace_direct_J9_to_J11_truth_path_with:
        - J9_to_J10
        - J10_to_J11
      J10_to_J11:
        condition: durable_KB_update_executed_and_confirmed
        provides:
          - durable_update_result_ref
          - accepted_status_ref
          - effective_change
          - updated_freshness
        rule: prepared_or_approved_update_is_not_overview_truth
  affected_files:
    - 14-status-merge-decision-card-design.okf.yaml
    - 15-project-kb-update-card-design.okf.yaml
    - 18-round5-cross-artifact-relationships.okf.yaml
  decision_requested: keep

R6_06_fragmented_relationship_authority:
  evidence:
    - >
      Planning relationships are embedded in file 03, execution relationships
      in file 08, recap relationships in file 12, and state/routing
      relationships in file 18. 
      
      
      
  proposed_resolution:
    preserve_local_relationship_files: true
    create_canonical_consolidation: 21-canonical-artifact-family-and-lifecycle-map.okf.yaml
    authority_rule: >
      File 21 owns the complete J1–J12 relationship projection. Local files
      remain historical and round-specific design authorities for their
      scoped relationships.
  affected_files:
    - new_file_21_only
  decision_requested: keep

R6_07_state_vocabulary:
  evidence:
    - >
      Shared anatomy uses partial, blocked and skipped. J7 uses completed,
      partially_completed, blocked, skipped, abandoned and unknown. J9 uses
      candidate, approved_for_merge, rejected, deferred, unresolved and
      merged. 
      
      
    - >
      These vocabularies represent different domains: generic presentation,
      flow execution outcome and durable-state review lifecycle.
  proposed_resolution:
    universal_enum: forbidden
    shared_lifecycle_concepts:
      - result_or_execution_state
      - candidate_state
      - approval_state
      - durable_write_state
      - overview_truth_state
    exact_allowed_values_owned_by:
      flow_result: flow-recap_contract
      status_review: status-merge_contract
      KB_write: project-kb-manager_contract
      overview_status: ProjectStatus_contract
      routing: AIRouting_contract
    cross_artifact_rule: >
      Translate through explicit handoff fields; do not normalize distinct
      domain states into one global enum.
  affected_files:
    - 20-round6-cross-cutting-consistency-resolution.okf.yaml
    - 21-canonical-artifact-family-and-lifecycle-map.okf.yaml
    - 00-package-manifest.okf.yaml
  decision_requested: keep

R6_08_missing_manifest:
  evidence:
    - >
      The package contains files 01–19 but no package-level manifest; earlier
      round records explicitly deferred manifest creation. 
    - >
      Live paths also contain unresolved naming and contract-reference drift,
      making a canonical index necessary.
  proposed_resolution:
    create: apex-meta/operator-output-design/step3-output-design-system/00-package-manifest.okf.yaml
    include:
      - package_identity
      - purpose_and_scope
      - current_status
      - complete_file_index
      - read_order
      - artifact_job_ownership_J1_to_J12
      - canonical_names
      - superseded_labels
      - local_relationship_files
      - canonical_relationship_file
      - decision_records
      - external_contract_authorities
      - unresolved_path_or_contract_refs
      - implementation_readiness
      - next_stage
  affected_files:
    - 00-package-manifest.okf.yaml
  decision_requested: keep
```

proposed_patch_set:  
exact_match_ready: false  
blocks:  
- target_file: apex-meta/operator-output-design/step3-output-design-system/02-shared-card-and-brief-anatomy.okf.yaml  
purpose: replace_stale_artifact_family_names  
patch_block_present: false  
blocker_if_absent: absolute_checkout_path_not_available  
- target_file: apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml  
purpose: separate_J3_day_outline_from_J4_execution_workspace  
patch_block_present: false  
blocker_if_absent: absolute_checkout_path_not_available  
- target_file: apex-meta/operator-output-design/step3-output-design-system/14-status-merge-decision-card-design.okf.yaml  
purpose: require_durable_write_confirmation_before_merged_display  
patch_block_present: false  
blocker_if_absent: absolute_checkout_path_not_available  
- target_file: apex-meta/operator-output-design/step3-output-design-system/15-project-kb-update-card-design.okf.yaml  
purpose: expose_confirmed_durable_update_result  
patch_block_present: false  
blocker_if_absent: absolute_checkout_path_not_available  
- target_file: apex-meta/operator-output-design/step3-output-design-system/16-project-status-overview-design.okf.yaml  
purpose: align_J11_with_live_ProjectStatus_contract  
patch_block_present: false  
blocker_if_absent: absolute_checkout_path_not_available  
- target_file: apex-meta/operator-output-design/step3-output-design-system/17-ai-routing-card-design.okf.yaml  
purpose: align_J12_with_stable_surface_class_and_verified_model_policy  
patch_block_present: false  
blocker_if_absent: absolute_checkout_path_not_available  
- target_file: apex-meta/operator-output-design/step3-output-design-system/18-round5-cross-artifact-relationships.okf.yaml  
purpose: replace_unconfirmed_J9_to_J11_truth_path_with_confirmed_J10_to_J11_path  
patch_block_present: false  
blocker_if_absent: absolute_checkout_path_not_available

proposed_new_files:  
- path: apex-meta/operator-output-design/step3-output-design-system/00-package-manifest.okf.yaml  
role: canonical_package_index  
- path: apex-meta/operator-output-design/step3-output-design-system/20-round6-cross-cutting-consistency-resolution.okf.yaml  
role: accepted_cross_round_corrections  
- path: apex-meta/operator-output-design/step3-output-design-system/21-canonical-artifact-family-and-lifecycle-map.okf.yaml  
role: canonical_J1_to_J12_relationship_and_lifecycle_map  
- path: apex-meta/operator-output-design/step3-output-design-system/22-round6-decision-and-verification-record.okf.yaml  
role: operator_approval_and_completion_record  
- path: apex-meta/operator-output-design/step3-output-design-system/23-step4-template-implementation-handoff.okf.md  
role: bounded_next_stage_handoff

validation_plan:  
phase_2_preconditions:  
- Marco_explicitly_accepts_phase_1_review  
- executor_absolute_checkout_path_is_known  
- AIRouting_routing_recommendation_contract_file_is_fetched_and_verified  
- each_old_block_is_copied_verbatim_from_live_checkout  
patch_validation:  
- require_one_change_per_patch_block  
- require_exact_old_match_count_equals_one  
- apply_only_accepted_blocks  
- fetch_each_changed_file_after_edit  
- report_exact_old_match_found  
- report_replacement_applied  
- report_post_edit_fetch_verified  
- do_not_create_file_22_until_all_accepted_edits_validate  
cross_round_acceptance:  
canonical_names_consistent: required  
J3_and_J4_depth_not_duplicated: required  
J11_matches_live_ProjectStatus_boundaries: required  
J12_uses_stable_surface_class_by_default: required  
exact_model_requires_verified_reference: required  
J9_merged_requires_durable_confirmation: required  
J10_to_J11_relationship_defined: required  
local_relationship_files_preserved: required  
one_canonical_relationship_map_exists: required  
state_vocabulary_references_domain_owners: required  
package_manifest_complete: required  
scope_gate:  
existing_skill_runtime_files_modified: false  
templates_created: false  
prompts_created: false  
workflow_executed: false  
project_state_mutated: false  
calendar_event_created: false  
autonomous_agent_or_scheduler_designed: false

decisions_requested:  
- keep_all  
- change_specific_items  
- reject_specific_items