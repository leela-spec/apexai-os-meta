# APEX Minimal Raw Flow Dump Example

Synthetic example for `raw-flow-dump-normalize`. One APEX flow only. This is not a FlowRecap packet, not a status merge, and not a model usage delta.

```yaml
raw_flow_dump_metadata:
  artifact_name: normalized_raw_flow_dump
  dump_id: raw_flow_dump_2026-07-06_F3_skill_interface_seed
  execution_day: "2026-07-06"
  flow_id: F3
  source_flow_packet_ref: "flow_packet_2026-07-06_F3_APEX_raw_dump_interface"
  flow_prompt_pack_ref: "flow_prompt_pack_2026-07-06_F3_APEX_raw_dump_interface"
  completion_state: partially_completed
  normalization_confidence: medium
  validation_status: operator_review_recommended
```

## 1. Flow Card

**Flow:** APEX raw-flow-dump-normalize interface seed

**Planned intent:** Create the first interface files for a minimal package that can normalize messy operator evidence after planned APEX flows.

**Actual state:** partially_completed

**Review flag:** Source best-practice guide path was not verified in repo; one package-level manifest decision is still pending.

## 2. Source References

- **source_flow_packet_ref:** `flow_packet_2026-07-06_F3_APEX_raw_dump_interface`
- **flow_prompt_pack_ref:** `flow_prompt_pack_2026-07-06_F3_APEX_raw_dump_interface`
- **other sources:** `.claude/Claude.md`, `.claude/skills/PrecapNextDay/SKILL.md`, PrecapNextDay reference contracts
- **source gaps:** Claude skill best-practice guide was requested as repo source but not found at the tested root path.

## 3. Raw Evidence

```text
Operator requested creation of the minimal interface package for raw-flow-dump-normalize.
The first two reference contracts were created/normalized.
The raw-flow-dump operator template was added after simplifying the initial attempted template.
The package is interface-only and must not run FlowRecap, merge status, execute work, or create calendar events.
```

## 4. Normalized Interpretation

**Summary:** Work started on the APEX `raw-flow-dump-normalize` minimal interface package. The package now has a normalized raw flow dump contract, a skipped flow marker contract, and an operator-facing raw flow dump template. The work is partial because the example, manifest, and SKILL.md are still being created in sequence.

**Produced outputs:**

- `raw-flow-dump-contract.md` — reference contract — `.claude/skills/raw-flow-dump-normalize/references/raw-flow-dump-contract.md` — confidence: high
- `skipped-flow-marker-contract.md` — reference contract — `.claude/skills/raw-flow-dump-normalize/references/skipped-flow-marker-contract.md` — confidence: high
- `raw-flow-dump-template.md` — operator template — `.claude/skills/raw-flow-dump-normalize/templates/raw-flow-dump-template.md` — confidence: medium

**Decisions made:**

- Create package at canonical lowercase path — source: operator request and PreCap manifest path policy — confidence: high
- Treat model usage as notes only, not a model usage delta — source: ownership boundary — confidence: high
- Keep skipped flow handling in a separate marker contract — source: package ownership boundary — confidence: high

**Blockers or failures:**

- Missing repo-root best-practice source — impact: low — next handling: keep in source_gap_register unless the operator provides a path.
- Package manifest not yet created — impact: medium — next handling: create `package-manifest.md` later in the sequence.

**Open questions:**

- Should `.claude/Claude.md` eventually be updated to point to `SKILL.md` instead of `Skill_raw-flow-dump-normalize.md`? — owner: operator
- Should the first package version include only Markdown interfaces, or also a future optional validation script placeholder? — owner: operator

## 5. Model Usage Notes

Notes only. This example does not create a model usage delta.

- **Usage observed:** partially_supplied
- **Notes:** Work was performed through the GitHub connector in the current chat; no token or quota totals were captured.
- **Usage-log follow-up:** false

## 6. Skipped Flow Pointer

- **Better as skipped_flow_marker:** no
- **Reason:** The flow was partially completed and has real produced outputs.
- **skipped_flow_marker_ref:** not_created

## 7. Confidence and Gaps

- **Overall confidence:** medium
- **Reasons:** Main output references are concrete; source authority was mostly inspected; one requested best-practice repo source was missing at the tested path.
- **Gap flags:** missing best-practice source path; package manifest and SKILL.md not yet created.
- **Operator review recommended:** true

## 8. Completion Gate

```yaml
raw_flow_dump_completion_gate:
  metadata_block_complete: true
  raw_evidence_separated_from_interpretation: true
  source_flow_packet_ref_present: true
  completion_state_explicit: true
  uncertainty_preserved: true
  skipped_flow_section_checked: true
  model_usage_notes_are_notes_only: true
  no_FlowRecap_output_created: true
  no_status_merge_created: true
  no_calendar_write_created: true
```
