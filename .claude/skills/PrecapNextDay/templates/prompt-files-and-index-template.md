# Prompt Files and Index - {{FLOW_OR_PACKAGE_LABEL}}

> **Prompt access state:** {{READY | READY_WITH_DEGRADED_ITEMS | PARTIAL | BLOCKED}}  
> **Outcome:** {{PROMPT_FILES_AVAILABLE_AND_MISSING_IN_ONE_TO_THREE_SENTENCES}}  
> **Next action:** {{OPEN_NEXT_PROMPT | FIX_DEGRADED_PROMPT | CONFIRM_ROUTE | RETURN_TO_FLOW_CARD}}  
> **Review needed:** {{PROMPT_OR_ROUTE_DECISION_OR_NONE}}

## Operator actions

- [ ] Open the prompt file required by the active sprint.
- [ ] Fix a missing or degraded prompt before execution.
- [ ] Confirm the referenced route when approval is still pending.
- [ ] Return to the Flow Execution Card for work context.

**Flow Execution Card:** [Open execution workspace]({{FLOW_EXECUTION_CARD_REF}}) - `{{FLOW_EXECUTION_CARD_REF}}`

## Prompt index

### Flow `{{FLOW_ID}}` (repeat per flow when the index covers more than one)

| Sprint | Prompt file | Recommended surface | Use when | Status |
|---|---|---|---|---|
| `{{SPRINT_ID}}` | [{{PROMPT_TITLE}}]({{PROMPT_FILE_REF}})<br>`{{PROMPT_FILE_REF}}` | {{TARGET_SURFACE}} | {{SHORT_USE_WHEN}} | {{READY | DEGRADED | MISSING | NOT_REQUIRED}} |

**Routing reference:** [{{ROUTING_LABEL}}]({{ROUTING_REF}}) - `{{ROUTING_REF}}`

## Missing or degraded prompt items (include when material)

### {{PROMPT_TITLE_OR_SPRINT}}

- **Issue:** {{MISSING_CONTENT_STALE_ROUTE_OR_QUALITY_GAP}}
- **Execution impact:** {{WHAT_CANNOT_SAFELY_PROCEED}}
- **Required action:** {{FIX_OR_REVIEW_ACTION}}

## Reusable single-prompt-file template

Copy this block into one file per prompt. The prompt file presents final prompt content; it does not restate the flow plan or routing analysis.

```markdown
# {{PROMPT_TITLE}}

**Recommended surface:** {{STABLE_SURFACE_OR_VERIFIED_MODEL}}  
**Use when:** {{TRIGGER_OR_SPRINT_NEED}}  
**Expected return artifact:** {{RETURN_ARTIFACT_LABEL}}  
**Routing reference:** [{{ROUTING_LABEL}}]({{ROUTING_REF}}) - `{{ROUTING_REF}}`

> **Degraded warning:** {{WARNING_OR_REMOVE_LINE}}

## Prompt

{{FULL_COPYABLE_PROMPT_BODY}}
```

## Prompt-file quality check

- [ ] The prompt states the task and desired return clearly.
- [ ] Required context and hard constraints appear once.
- [ ] Approval, stop, or review boundaries are explicit when consequential.
- [ ] The prompt does not request private chain-of-thought.
- [ ] The prompt file does not duplicate J4 tasks, dependencies, or execution sequence.
- [ ] The recommended surface is backed by a routing reference or marked unverified.

## Compact downstream handoff

```yaml
presentation_handoff:
  artifact_type: "Prompt_Files_and_Index"
  artifact_ref: "{{ARTIFACT_REF}}"
  flow_id: "{{FLOW_ID}}"
  prompt_files:
    - sprint: "{{SPRINT_ID}}"
      title: "{{PROMPT_TITLE}}"
      file: "{{PROMPT_FILE_REF}}"
      target_surface: "{{TARGET_SURFACE}}"
      routing_ref: "{{ROUTING_REF}}"
      use_when: "{{SHORT_USE_WHEN}}"
      degraded_flag: "{{TRUE_OR_FALSE}}"
  review_status: "{{REVIEW_STATUS}}"
  next_consumer: "operator_execution"
```

## Template authority

```yaml
template_authority:
  source_design_ref: "apex-meta/operator-output-design/step3-output-design-system/05-prompt-file-and-index-design.okf.yaml"
  round6_overlay_intent_ref: "canonical_name_projection_from_00-package-manifest.okf.yaml"
  overlay_application_status: "presentation_name_used_without_repository_mutation"
  domain_contract_refs:
    - ".claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md"
    - ".claude/skills/AIRouting/routing-recommendation-packet-contract.md"
  source_gap: "Expected Prompt Engineering entrypoint was not verified; final prompt doctrine remains externally owned."
```

Example: [J05 Prompt Files and Index](../examples/master-of-arts-example-fragments.md#j05-prompt-files-and-index)
