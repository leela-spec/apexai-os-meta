#!/usr/bin/env python3
"""Deterministically repair the Apex KB contract repair script itself.

This script only edits scripts/fix_apex_kb_package_contracts.py. It fixes the
over-broad collapsed-format validator and replaces the wiki template constant
with A-F templates so the package repair does not truncate valid template
sections.
"""

from __future__ import annotations

from pathlib import Path


SCRIPT = Path("scripts/fix_apex_kb_package_contracts.py")


WIKI_TEMPLATE_A_ONWARD = r'''# Template A - Summary Page

```markdown
---
title: "<Source or topic summary title>"
page_type: summary
kb_slug: "<kb-slug>"
summary_slug: "<source-or-topic-slug>"
source_refs:
  - source_id: "<source-id>"
    source_path: "<raw/source/path/or/pointer>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "raw_source | source_backed_summary | behavioral_inference | working_hypothesis | operator_question | practitioner_question"
status: "draft | active | needs_review | deprecated | superseded"
related_concepts:
  - "<concept-slug>"
related_entities:
  - "<entity-slug>"
review_flags: []
---

# <Source or Topic Summary Title>

## Core Summary

<Write a dense, source-grounded summary of the source or topic. Preserve structure, claims, mechanisms, and limitations. Do not generalize beyond evidence.>

## What This Source Adds to the KB

```yaml
adds:
  - "<Specific reusable knowledge contribution.>"
clarifies:
  - "<Concept, process, entity, or decision this source clarifies.>"
limits:
  - "<What this source does not establish.>"
```

## Key Claims

```yaml
key_claims:
  - claim_id: "C001"
    claim: "<Specific source-grounded claim>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    confidence: "high | medium | low"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "wiki/concepts/<concept-slug>.md"
```

## Open Questions

```yaml
open_questions:
  - question_id: "Q001"
    question: "<Open knowledge question>"
    proposed_handling: "audit_item | planning_task_candidate | leave_as_gap | ask_operator"
    source_pointer: "<source pointer or NA>"
```
```

# Template B - Concept Page

```markdown
---
title: "<Concept Label>"
page_type: concept
kb_slug: "<kb-slug>"
concept_slug: "<concept-slug>"
source_refs:
  - source_id: "<source-id>"
    source_path: "<raw/source/path/or/pointer>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "raw_source | source_backed_summary | behavioral_inference | working_hypothesis | operator_question | practitioner_question"
status: "draft | active | needs_review | deprecated | superseded"
aliases:
  - "<alias>"
related_concepts:
  - "<related-concept-slug>"
related_entities:
  - "<related-entity-slug>"
review_flags: []
---

# <Concept Label>

## Definition

<Define the concept using only source-grounded evidence. If sources disagree, present competing definitions instead of merging silently.>

## Source-Grounded Notes

```yaml
source_grounded_notes:
  - note_id: "N001"
    note: "<Specific note>"
    source_id: "<source-id>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    confidence: "high | medium | low"
    claim_label: "source_backed_summary"
```

## Relationships

```yaml
relationships:
  parent_concepts:
    - "[[<parent-concept-slug>]]"
  child_concepts:
    - "[[<child-concept-slug>]]"
  related_concepts:
    - "[[<related-concept-slug>]]"
  related_entities:
    - "[[<entity-slug>]]"
  source_summaries:
    - "[[<summary-slug>]]"
```

## Usage Patterns

```yaml
usage_patterns:
  - pattern_id: "P001"
    pattern: "<How this concept is used operationally or analytically>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    confidence: "high | medium | low"
    claim_label: "behavioral_inference | source_backed_summary | working_hypothesis"
```

## Applied Card

```yaml
applied_card:
  shortest_useful_summary: "<One or two sentences for fast practical use.>"
  when_this_pattern_appears:
    - "<Observable situation or cue.>"
  questions_to_ask:
    - "<Precise applied question.>"
  do_not_do:
    - "<Common misuse, overreach, or bypass.>"
  next_clean_action: "<Smallest practical action if this concept is active.>"
```

## Contradictions and Variants

```yaml
contradictions_and_variants:
  status: "none_detected | possible | confirmed"
  items:
    - item_id: "X001"
      type: "contradiction | variant | unresolved_tension"
      summary: "<What differs between sources>"
      source_refs:
        - "<source pointer A>"
        - "<source pointer B>"
      handling: "preserve_both | audit_item_needed | operator_review_needed"
```

## Open Questions

```yaml
open_questions:
  - question_id: "Q001"
    question: "<Open question>"
    blocks_use: false
    proposed_handling: "audit_item | ingest_more_sources | ask_operator | practitioner_review"
```
```

# Template C - Entity Page

```markdown
---
title: "<Entity Label>"
page_type: entity
kb_slug: "<kb-slug>"
entity_slug: "<entity-slug>"
entity_type: "person | organization | project | tool | framework | file | artifact | other"
source_refs:
  - source_id: "<source-id>"
    source_path: "<raw/source/path/or/pointer>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "raw_source | source_backed_summary | behavioral_inference | working_hypothesis | operator_question | practitioner_question"
status: "draft | active | needs_review | deprecated | superseded"
aliases: []
related_concepts: []
review_flags: []
---

# <Entity Label>

## Entity Summary

<Describe the entity only from source-grounded evidence.>

## Source-Grounded Facts

```yaml
source_grounded_facts:
  - fact_id: "F001"
    fact: "<Specific fact>"
    source_id: "<source-id>"
    source_pointer: "<source pointer>"
    confidence: "high | medium | low"
    claim_label: "source_backed_summary"
```
```

# Template D - Wiki Index

```markdown
---
title: "<KB Title> Index"
page_type: index
kb_slug: "<kb-slug>"
source_refs: []
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "mixed"
claim_label: "source_backed_summary"
status: "active"
review_flags: []
---

# <KB Title> Index

<!-- BEGIN AUTO-GENERATED INDEX -->

```yaml
machine_generated_index:
  generated_at: "YYYY-MM-DDTHH:MM:SSZ"
  generated_by: "apex_kb.py index"
  page_count: 0
  pages:
    summaries: []
    concepts: []
    entities: []
  detected_links: []
  orphan_pages: []
  stale_index_hash: "NA"
```

<!-- END AUTO-GENERATED INDEX -->

<!-- BEGIN LLM SUMMARY -->

## LLM Summary

<LLM-owned semantic overview. Do not overwrite the machine-generated section.>

<!-- END LLM SUMMARY -->
```

# Template E - Query Output

```markdown
---
title: "<Query Title>"
page_type: query_output
kb_slug: "<kb-slug>"
query_slug: "<query-slug>"
source_refs:
  - source_id: "<source-id-or-page-path>"
    source_path: "<wiki/page/path>"
    source_hash: "NA"
    source_pointer: "<section anchor>"
    source_storage_mode: "pointer_only"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "source_backed_summary | behavioral_inference | working_hypothesis"
status: "draft | active | needs_review"
review_flags: []
---

# <Query Title>

## Answer

<Answer from compiled KB pages and explicit source pointers. Preserve uncertainty.>

## Evidence Pages

```yaml
evidence_pages:
  - page_path: "wiki/<path>.md"
    relevant_sections:
      - "<section heading>"
    supports:
      - "<answer claim>"
```
```

# Template F - Audit Item

```markdown
---
title: "<Audit Item Title>"
page_type: audit_item
kb_slug: "<kb-slug>"
audit_id: "<audit-id>"
source_refs:
  - source_id: "<source-id-or-page-path>"
    source_path: "<source/page/path>"
    source_hash: "<sha256-or-NA>"
    source_pointer: "<heading/page/anchor/line/passage reference>"
    source_storage_mode: "pointer_only | copy_into_kb | snapshot_copy"
created_at: "YYYY-MM-DDTHH:MM:SSZ"
updated_at: "YYYY-MM-DDTHH:MM:SSZ"
confidence: "high | medium | low | mixed | unknown"
claim_label: "operator_question | practitioner_question | working_hypothesis"
status: "draft | active | needs_review | deprecated | superseded"
review_flags: []
---

# <Audit Item Title>

```yaml
audit_item:
  audit_id: "<audit-id>"
  type: "contradiction | quality | staleness | gap | naming | source_authority | broken_link | missing_source_pointer | duplicate_page | operator_note"
  severity: "low | medium | high"
  status: "open | resolved | deferred | rejected"
  target_path: "<wiki/page/path>"
  target_anchor: "<heading-or-anchor-or-NA>"
  source_ref: "<source pointer or NA>"
  created_at: "YYYY-MM-DDTHH:MM:SSZ"
```

## Summary

<Short description of the issue, feedback, contradiction, quality concern, or gap.>
```

# Completion Gate

```yaml
completion_gate:
  valid_wiki_page_templates_file:
    required:
      - summary_template_present
      - concept_template_present
      - entity_template_present
      - index_template_present
      - query_output_template_present
      - audit_item_template_present
      - shared_frontmatter_rules_present
      - source_pointer_policy_present
      - contradiction_visibility_present
      - claim_label_and_confidence_separated
```
'''


VALIDATE_TEXTS = r'''def validate_texts(texts: dict[Path, str]) -> list[str]:
    findings: list[str] = []
    collapsed_patterns = [
        r"(?m)^supporting_files:  - path:",
        r"(?m)^failure_modes:  \\w",
        r"(?m)^completion_gate:  valid_completion_requires:",
        r"(?m)^---title:",
        r"(?m)^page_type: .*kb_slug:",
        r"(?m)^  purpose: >    \\S",
        r"(?m)^  invocation_pattern: >    \\S",
        r"(?m)^    directory_hash_rule: >      \\S",
        r"(?m)^  required_read_sequence:    1:",
        r"(?m)^  audit_review_sequence:    1:",
        r"(?m)^completion_gates:  ingest_phase_1_complete:",
    ]
    for path, text in texts.items():
        for pattern in collapsed_patterns:
            if re.search(pattern, text):
                findings.append(f"{path}: collapsed formatting pattern remains: {pattern}")

    required = {
        SKILL_PATH: ["source_storage_modes:", "phase_gate_policy:", "claim_label:", "confidence_and_claim_label_not_conflated"],
        WIKI_TEMPLATES_PATH: ["claim_label_allowed:", "Applied Card", "Template F - Audit Item", "source_storage_mode"],
        SCRIPT_CONTRACT_PATH: ["--source-slug", "[global-options] <subcommand>", "JSON Output Compatibility Notes"],
        OP_RULES_PATH: ["source_storage_policy:", "epistemic_fields:", "phase_gate_policy:"],
    }
    for path, needles in required.items():
        for needle in needles:
            if needle not in texts.get(path, ""):
                findings.append(f"{path}: missing required content: {needle}")
    return findings
'''


PATCH_OPERATION_RULES = r'''def patch_operation_rules(text: str) -> str:
    if "source_storage_policy:" not in text:
        text = text.replace(
            "  ownership_split:\n",
            "  source_storage_policy:\n"
            "    allowed_modes:\n"
            "      - pointer_only\n"
            "      - copy_into_kb\n"
            "      - snapshot_copy\n"
            "    default_for_repo_internal_sources: pointer_only\n"
            "    default_for_external_or_uploaded_sources: copy_into_kb\n"
            "    generated_pages_must_record:\n"
            "      - source_storage_mode\n"
            "      - source_path\n"
            "      - source_hash\n\n"
            "  epistemic_fields:\n"
            "    confidence:\n"
            "      meaning: \"How strongly the KB should trust the page or claim.\"\n"
            "      allowed:\n"
            "        - high\n"
            "        - medium\n"
            "        - low\n"
            "        - mixed\n"
            "        - unknown\n"
            "    claim_label:\n"
            "      meaning: \"What kind of epistemic object the statement is.\"\n"
            "      allowed:\n"
            "        - raw_source\n"
            "        - source_backed_summary\n"
            "        - behavioral_inference\n"
            "        - working_hypothesis\n"
            "        - operator_question\n"
            "        - practitioner_question\n"
            "    rule: \"Do not place claim-label values inside the confidence field.\"\n\n"
            "  ownership_split:\n",
        )
    if "phase_gate_policy:" not in text:
        text = text.replace(
            "  phase_0_preflight:\n",
            "  phase_gate_policy:\n"
            "    normal_mode:\n"
            "      same_prompt_approval_allowed: false\n"
            "      requires_separate_operator_turn: true\n"
            "    explicit_test_mode:\n"
            "      same_prompt_approval_allowed: true\n"
            "      condition: \"Phase 1 artifacts must exist before Phase 2 generation begins.\"\n\n"
            "  phase_0_preflight:\n",
        )
    text = text.replace(
        '  required_read_sequence:    1: "Read wiki/index.md."    2: "Select likely relevant summaries, concepts, and entities."    3: "Read the selected pages."    4: "Answer from compiled KB pages."    5: "Report evidence pages, contradictions, confidence, and gaps."\n',
        '  required_read_sequence:\n'
        '    1: "Read wiki/index.md."\n'
        '    2: "Select likely relevant summaries, concepts, and entities."\n'
        '    3: "Read the selected pages."\n'
        '    4: "Answer from compiled KB pages."\n'
        '    5: "Report evidence pages, contradictions, confidence, and gaps."\n',
    )
    text = text.replace(
        '  audit_review_sequence:    1: "List open audit items."    2: "Group by target_path, type, and severity."    3: "Select one item or one target group for review."    4: "Read the target page and source pointers when available."    5: "Propose accept, partial, reject, or defer."    6: "Apply resolution only after operator decision."    7: "Move resolved item to audit/resolved/ while preserving history."\n',
        '  audit_review_sequence:\n'
        '    1: "List open audit items."\n'
        '    2: "Group by target_path, type, and severity."\n'
        '    3: "Select one item or one target group for review."\n'
        '    4: "Read the target page and source pointers when available."\n'
        '    5: "Propose accept, partial, reject, or defer."\n'
        '    6: "Apply resolution only after operator decision."\n'
        '    7: "Move resolved item to audit/resolved/ while preserving history."\n',
    )
    text = text.replace(
        'completion_gates:  ingest_phase_1_complete:    required:      - ingest_analysis_file_created      - source_identity_recorded      - source_summary_created      - concept_candidates_listed      - entity_candidates_listed      - contradiction_candidates_listed_or_none_recorded      - open_questions_recorded_or_none_recorded      - proposed_page_changes_listed      - operator_review_gate_present      - no_wiki_pages_written  ingest_phase_2_complete:    required:      - operator_confirmation_phrase_received      - approved_page_changes_applied      - generated_or_updated_pages_have_source_pointers      - contradictions_preserved_or_reviewed      - source_manifest_updated_or_failure_reported      - index_updated_or_stale_index_flagged      - postflight_report_created  query_complete:    required:      - index_read_first      - relevant_pages_read      - answer_grounded_in_pages      - evidence_pages_named      - contradictions_reported      - knowledge_gaps_reported      - confidence_stated  quick_lint_complete:    required:      - deterministic_findings_reported      - broken_links_reported      - orphan_pages_reported      - stale_index_status_reported      - missing_required_paths_reported  full_lint_complete:    required:      - quick_lint_completed      - semantic_review_flags_reported      - source_pointer_quality_checked      - recommended_next_action_present  audit_complete:    required:      - open_items_grouped      - selected_item_or_group_reviewed      - operator_decision_recorded_or_requested      - resolved_items_archived_when_approved      - unresolved_items_preserved\n',
        'completion_gates:\n'
        '  ingest_phase_1_complete:\n'
        '    required:\n'
        '      - ingest_analysis_file_created\n'
        '      - source_identity_recorded\n'
        '      - source_summary_created\n'
        '      - concept_candidates_listed\n'
        '      - entity_candidates_listed\n'
        '      - contradiction_candidates_listed_or_none_recorded\n'
        '      - open_questions_recorded_or_none_recorded\n'
        '      - proposed_page_changes_listed\n'
        '      - operator_review_gate_present\n'
        '      - no_wiki_pages_written\n'
        '  ingest_phase_2_complete:\n'
        '    required:\n'
        '      - operator_confirmation_phrase_received\n'
        '      - approved_page_changes_applied\n'
        '      - generated_or_updated_pages_have_source_pointers\n'
        '      - contradictions_preserved_or_reviewed\n'
        '      - source_manifest_updated_or_failure_reported\n'
        '      - index_updated_or_stale_index_flagged\n'
        '      - postflight_report_created\n'
        '  query_complete:\n'
        '    required:\n'
        '      - index_read_first\n'
        '      - relevant_pages_read\n'
        '      - answer_grounded_in_pages\n'
        '      - evidence_pages_named\n'
        '      - contradictions_reported\n'
        '      - knowledge_gaps_reported\n'
        '      - confidence_stated\n'
        '  quick_lint_complete:\n'
        '    required:\n'
        '      - deterministic_findings_reported\n'
        '      - broken_links_reported\n'
        '      - orphan_pages_reported\n'
        '      - stale_index_status_reported\n'
        '      - missing_required_paths_reported\n'
        '  full_lint_complete:\n'
        '    required:\n'
        '      - quick_lint_completed\n'
        '      - semantic_review_flags_reported\n'
        '      - source_pointer_quality_checked\n'
        '      - recommended_next_action_present\n'
        '  audit_complete:\n'
        '    required:\n'
        '      - open_items_grouped\n'
        '      - selected_item_or_group_reviewed\n'
        '      - operator_decision_recorded_or_requested\n'
        '      - resolved_items_archived_when_approved\n'
        '      - unresolved_items_preserved\n',
    )
    return text
'''


PATCH_WIKI_TEMPLATES = r'''def patch_wiki_templates(text: str) -> str:
    if "claim_label_allowed:" not in text:
        text = text.replace(
            "  confidence_allowed:\n"
            "    - high\n"
            "    - medium\n"
            "    - low\n"
            "    - mixed\n"
            "    - unknown\n",
            "  confidence_allowed:\n"
            "    - high\n"
            "    - medium\n"
            "    - low\n"
            "    - mixed\n"
            "    - unknown\n\n"
            "  claim_label_allowed:\n"
            "    - raw_source\n"
            "    - source_backed_summary\n"
            "    - behavioral_inference\n"
            "    - working_hypothesis\n"
            "    - operator_question\n"
            "    - practitioner_question\n",
        )
    if "    - claim_label\n" not in text:
        text = text.replace("    - confidence\n    - status\n", "    - confidence\n    - claim_label\n    - status\n")
    source_ref_start = text.find("  source_ref_shape:")
    source_ref_end = text.find("```", source_ref_start)
    if source_ref_start != -1 and source_ref_end != -1 and "source_storage_mode" not in text[source_ref_start:source_ref_end]:
        text = text.replace("    - source_pointer\n", "    - source_pointer\n    - source_storage_mode\n", 1)
    if "---title:" in text or "# Template D" not in text or "Template F - Audit Item" not in text:
        text = replace_from(text, "# Template A", WIKI_TEMPLATE_A_ONWARD)
    return text
'''


def replace_constant(text: str, name: str, value: str) -> str:
    start = text.index(f"{name} = '''")
    body_start = text.index("'''", start) + 3
    end = text.index("\n'''", body_start)
    return text[:body_start] + value + text[end:]


def replace_function(text: str, name: str, value: str) -> str:
    start = text.index(f"def {name}(")
    next_def = text.index("\ndef ", start + 1)
    return text[:start] + value.rstrip() + "\n\n" + text[next_def + 1:]


def main() -> int:
    text = SCRIPT.read_text(encoding="utf-8")
    text = replace_constant(text, "WIKI_TEMPLATE_A_ONWARD", WIKI_TEMPLATE_A_ONWARD)
    text = replace_function(text, "patch_wiki_templates", PATCH_WIKI_TEMPLATES)
    text = replace_function(text, "patch_operation_rules", PATCH_OPERATION_RULES)
    text = replace_function(text, "validate_texts", VALIDATE_TEXTS)
    SCRIPT.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
