# Skip Marker

**Skipped flow:** `{{FLOW_ID}}` - {{FLOW_TITLE}}  
**Execution day:** {{YYYY_MM_DD}}  
**Source flow:** [{{FLOW_CARD_LABEL}}]({{SOURCE_FLOW_PACKET_REF}}) - `{{SOURCE_FLOW_PACKET_REF}}`  
**Reason:** {{SPECIFIC_NON_EXECUTION_REASON}}  
**Plan impact:** {{NONE | LOW | MEDIUM | HIGH | BLOCKING | UNKNOWN}} - {{IMPACT_SUMMARY}}  
**Next handling:** {{ACTIONABLE_HANDLING_SUMMARY}}  
**Review:** {{OPERATOR_DECISION_OR_NONE}}

Use the full [Execution Evidence Handoff](J06-execution-evidence-handoff.md) instead if any work was performed, an artifact or decision was created, or blocker evidence must be preserved.

```yaml
skipped_flow_marker:
  marker_id: "{{MARKER_ID}}"
  artifact_name: "skipped_flow_marker"
  execution_day: "{{YYYY_MM_DD}}"
  flow_id: "{{FLOW_ID}}"
  source_flow_packet_ref:
    flow_packet_path_or_label: "{{SOURCE_FLOW_PACKET_REF}}"
    source_status: "{{AVAILABLE_OR_PARTIALLY_AVAILABLE_OR_MISSING_OR_UNKNOWN}}"
  skip_reason: "{{SPECIFIC_NON_EXECUTION_REASON}}"
  skip_type: "{{INTENTIONAL_SKIP_OR_TIME_CONSTRAINT_OR_BLOCKER_OR_ENERGY_CAPACITY_OR_DEPENDENCY_MISSING_OR_REPLACED_BY_OTHER_WORK_OR_UNKNOWN}}"
  impact_on_plan:
    impact_level: "{{NONE_OR_LOW_OR_MEDIUM_OR_HIGH_OR_BLOCKING_OR_UNKNOWN}}"
    impact_summary: "{{IMPACT_SUMMARY}}"
    affected_outputs:
      - "{{AFFECTED_OUTPUT_OR_NONE}}"
  recommended_next_handling:
    handling_type: "{{RESCHEDULE_SAME_FLOW_OR_COMPRESS_INTO_NEXT_PLAN_OR_CONVERT_TO_BLOCKER_REVIEW_OR_REPLACE_WITH_NEW_FLOW_OR_ARCHIVE_NO_FOLLOWUP_OR_ASK_OPERATOR_OR_UNKNOWN}}"
    recommendation: "{{ACTIONABLE_HANDLING_SUMMARY}}"
    recommended_owner: "{{OPERATOR_OR_NEXT_PRECAPNEXTDAY_OR_FLOWRECAP_OR_STATUS_MERGE_OR_PROJECT_KB_MANAGER_OR_UNKNOWN}}"
  validation_status: "{{VALID_OR_VALID_WITH_WARNINGS_OR_OPERATOR_REVIEW_RECOMMENDED_OR_LOW_CONFIDENCE_OR_BLOCKED_BY_MISSING_MINIMUM_EVIDENCE}}"
```

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/07-skip-marker-low-priority-design.okf.yaml"
  round6_overlay_intent_ref: null
  overlay_application_status: "not_applicable_to_this_template"
  domain_contract_refs:
    - ".claude/skills/raw-flow-dump-normalize/SKILL.md"
    - ".claude/skills/raw-flow-dump-normalize/references/skipped-flow-marker-contract.md"
    - ".claude/skills/PrecapNextDay/references/flow-packet-contract.md"
```

Example: [J06a Skip Marker](../examples/master-of-arts-example-fragments.md#j06a-skip-marker)
