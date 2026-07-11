# Project State Success Card - {{PORTFOLIO_OR_SCOPE}}

> **Planning readiness:** {{USABLE_FOR_WEEKLY_PLANNING | USABLE_FOR_NEXT_DAY_PLANNING | REVIEW_NEEDED | BLOCKED}}  
> **Outcome:** {{ONE_TO_THREE_SENTENCE_PORTFOLIO_STATE_SUMMARY}}  
> **Next action:** {{USE_AS_CONTEXT | EDIT_CONTEXT | REQUEST_EVIDENCE | MARK_STALE | REJECT_CONTEXT}}  
> **Review needed:** {{HIGHEST_IMPACT_REVIEW_QUESTION_OR_NONE}}  
> **Warning:** {{MATERIAL_STALE_CONFLICTING_OR_MISSING_CONTEXT_OR_REMOVE_LINE}}

## Operator decision

- [ ] Use this state as context for weekly planning.
- [ ] Use this state as context for next-day planning.
- [ ] Edit the identified project context before planning.
- [ ] Request the exact missing evidence named below.
- [ ] Mark the affected project state stale or reject it.

**Decision or instruction:** {{OPERATOR_DECISION_OR_PENDING}}

## Portfolio snapshot

**State as of:** {{DATE_TIME_OR_SOURCE_FRESHNESS_POINT}}  
**Projects represented:** {{COUNT}}  
**Ready for planning:** {{COUNT_OR_NAMES}}  
**Blocked or review-needed:** {{COUNT_OR_NAMES}}  
**Main planning constraint:** {{CONSTRAINT_OR_NONE}}

## Project - {{PROJECT_NAME}} (repeat per represented project)

**Current phase:** {{CURRENT_PHASE}}  
**Current goal:** {{CURRENT_GOAL}}  
**Planning status:** {{USABLE | REVIEW_NEEDED | BLOCKED | STALE}}  
**Accepted priorities:**

- {{ACCEPTED_PRIORITY}}

**Active work:**

- {{ACTIVE_WORK_ITEM_OR_WORKSTREAM_SUMMARY}}

**Next-action candidates:**

- {{CANDIDATE_ACTION_WITHOUT_COMMITTING_THE_WEEK_OR_DAY}}

**Blockers:** {{BLOCKERS_OR_NONE}}  
**Stale or conflicting information:** {{ISSUE_OR_NONE}}  
**Important artifact references:**

- [{{DESCRIPTIVE_ARTIFACT_LABEL}}]({{RELATIVE_OR_CANONICAL_REF}}) - `{{VISIBLE_REF_OR_PATH}}`

## Planning handoff

**Safe context to carry forward:**

- {{CONFIRMED_PROJECT_SIGNAL}}

**Do not carry forward without review:**

- {{STALE_CONFLICTING_OR_UNSUPPORTED_SIGNAL_OR_NONE}}

**Ready for:** {{WEEKLY_COMMAND_BRIEF | PRECAP_NEXT_DAY_BRIEF | REVIEW_BEFORE_PLANNING}}

## Review flags (include when material)

### {{FLAG_TITLE}}

- **Issue:** {{MISSING_STALE_CONFLICTING_OR_LOW_CONFIDENCE_CONTEXT}}
- **Why it matters:** {{EFFECT_ON_PLANNING}}
- **Operator action:** {{ONE_RESOLVING_ACTION}}

## Provenance and confidence

**Main sources:** {{DECISIVE_PROJECT_STATE_REFS}}  
**Freshness:** {{CURRENT | MIXED | STALE | UNKNOWN_WITH_DETAIL}}  
**Confidence:** {{HIGH | MEDIUM | LOW_AND_WHY}}  
**Consequential assumptions:** {{ASSUMPTIONS_OR_NONE}}

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Project_State_Success_Card"
  artifact_ref: "{{ARTIFACT_REF}}"
  planning_readiness: "{{PLANNING_READINESS}}"
  represented_projects:
    - project_ref: "{{PROJECT_REF}}"
      project_state_ref: "{{PROJECT_STATE_REF}}"
      review_status: "{{REVIEW_STATUS}}"
  freshness: "{{FRESHNESS_STATUS}}"
  next_consumer: "{{WEEKLY_COMMAND_BRIEF_OR_PRECAP_NEXT_DAY_BRIEF_OR_OPERATOR_REVIEW}}"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/03-planning-artifact-designs.okf.yaml"
  round6_overlay_intent_ref: null
  overlay_application_status: "not_applicable_to_this_template"
  domain_contract_refs:
    - ".claude/skills/project-kb-manager/references/apex-orchestration-state-packet-contract.md"
  source_gap: "Dedicated live project-state-success owner entrypoint was not verified; do not infer additional schema."
```

Example: [J01 Project State Success Card](../examples/master-of-arts-example-fragments.md#j01-project-state-success-card)
