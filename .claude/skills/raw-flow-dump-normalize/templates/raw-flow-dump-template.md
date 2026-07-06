# Raw Flow Dump Template

Operator-facing template for one flow after work has ended. Use cards and short lists. Keep raw evidence separate from normalized interpretation.

```yaml
raw_flow_dump_metadata:
  artifact_name: normalized_raw_flow_dump
  dump_id: "raw_flow_dump_<date>_<flow_id>_<slug>"
  execution_day: "<YYYY-MM-DD>"
  flow_id: "<flow_id>"
  source_flow_packet_ref: "<source_flow_packet_ref>"
  flow_prompt_pack_ref: "<flow_prompt_pack_ref_or_missing>"
  completion_state: "<completed|partially_completed|skipped|blocked|abandoned|unknown>"
  normalization_confidence: "<high|medium|low|unknown>"
  validation_status: "<valid|valid_with_warnings|operator_review_recommended|low_confidence|blocked_by_missing_minimum_evidence>"
```

## 1. Flow Card

**Flow:** `<flow label>`

**Planned intent:** `<source plan intent>`

**Actual state:** `<completion_state>`

**Review flag:** `<none or reason>`

## 2. Source References

- **source_flow_packet_ref:** `<id/path/label>`
- **flow_prompt_pack_ref:** `<id/path/label/missing>`
- **other sources:** `<artifact or note labels>`
- **source gaps:** `<missing or unclear sources>`

## 3. Raw Evidence

Keep this section factual and uncleaned.

```text
<operator notes, prompt output excerpts, artifact notes, or other evidence>
```

## 4. Normalized Interpretation

**Summary:** `<compact factual summary>`

**Produced outputs:**

- `<output label>` — `<type>` — `<reference>` — confidence: `<high|medium|low|unknown>`

**Decisions made:**

- `<decision>` — source: `<source>` — confidence: `<high|medium|low|unknown>`

**Blockers or failures:**

- `<blocker>` — impact: `<none|low|medium|high|blocking|unknown>` — next handling: `<recommendation>`

**Open questions:**

- `<question>` — owner: `<operator|next_PreCapNextDay|FlowRecap|model_usage_log|status_merge|project_kb_manager|unknown>`

## 5. Model Usage Notes

Notes only. This file does not create a model usage delta.

- **Usage observed:** `<supplied|partially_supplied|not_supplied|unknown>`
- **Notes:** `<usage notes or none>`
- **Usage-log follow-up:** `<true|false>`

## 6. Skipped Flow Pointer

Use when the flow was skipped or evidence is too thin.

- **Better as skipped_flow_marker:** `<yes|no|unclear>`
- **Reason:** `<reason>`
- **skipped_flow_marker_ref:** `<id/path/label or not_created>`

## 7. Confidence and Gaps

- **Overall confidence:** `<high|medium|low|unknown>`
- **Reasons:** `<reason list>`
- **Gap flags:** `<gap list>`
- **Operator review recommended:** `<true|false>`

## 8. Completion Gate

```yaml
raw_flow_dump_completion_gate:
  metadata_block_complete: <true|false>
  raw_evidence_separated_from_interpretation: <true|false>
  source_flow_packet_ref_present: <true|false>
  completion_state_explicit: <true|false>
  uncertainty_preserved: <true|false>
  skipped_flow_section_checked: <true|false>
  model_usage_notes_are_notes_only: <true|false>
  no_FlowRecap_output_created: true
  no_status_merge_created: true
  no_calendar_write_created: true
```
