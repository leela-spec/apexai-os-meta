#!/usr/bin/env python3
"""
fix_apex_kb_package_contracts.py

Repo-local repair utility for the Apex KB skill package.

This script fixes the formatting and contract drift found in the first real
Codex execution test of `.claude/skills/apex-kb/`.

Safety policy:
- No network access.
- No email, comments, PRs, issues, reviewers, notifications, or external contact.
- No cross-repo writes.
- Only modifies the explicit files listed in TARGET_PATHS.
- Creates timestamped backups before writing.

Usage from repository root:
    python scripts/fix_apex_kb_package_contracts.py --check
    python scripts/fix_apex_kb_package_contracts.py --apply
    python scripts/fix_apex_kb_package_contracts.py --validate
"""

from __future__ import annotations

import argparse
import datetime as dt
import difflib
import re
import shutil
import subprocess
import sys
from pathlib import Path


SKILL_PATH = Path(".claude/skills/apex-kb/SKILL.md")
WIKI_TEMPLATES_PATH = Path(".claude/skills/apex-kb/templates/wiki-page-templates.md")
SCRIPT_CONTRACT_PATH = Path(".claude/skills/apex-kb/references/script-command-contract.md")
OP_RULES_PATH = Path(".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md")
APEX_KB_PY_PATH = Path("apex-meta/scripts/apex_kb.py")

TARGET_PATHS = [
    SKILL_PATH,
    WIKI_TEMPLATES_PATH,
    SCRIPT_CONTRACT_PATH,
    OP_RULES_PATH,
    APEX_KB_PY_PATH,
]


SUPPORTING_FILES_SECTION = '''# Supporting Files

```yaml
supporting_files:
  - path: "references/kb-contract.md"
    read_when:
      - validating_apex_kb_scope
      - scaffold_mode
      - checking_data_layout
      - routing_to_apex_plan_session_sync
      - validating_forbidden_behavior

  - path: "references/ingest-query-lint-audit-rules.md"
    read_when:
      - ingest_phase_1
      - ingest_phase_2
      - query_mode
      - lint_mode
      - audit_mode
      - checking_operator_review_gate
      - validating_semantic_vs_deterministic_ownership
      - checking_source_storage_mode

  - path: "references/script-command-contract.md"
    read_when:
      - scaffold_mode
      - lint_mode
      - index_rebuild_needed
      - hash_source_needed
      - audit_file_listing_needed
      - operator_asks_about_apex_kb_py
      - reconciling_cli_arguments

  - path: "templates/ingest-analysis-template.md"
    read_when:
      - writing_ingest_phase_1_analysis
      - operator_requests_blank_phase_1_template
      - phase_1_output_shape_is_unclear

  - path: "templates/wiki-page-templates.md"
    read_when:
      - creating_summary_page
      - creating_concept_page
      - creating_entity_page
      - checking_generated_page_shape
      - checking_claim_label_vs_confidence

  - path: "package-manifest.md"
    read_when:
      - operator_inspects_package_structure
      - validating_file_inventory
      - checking_v1_scope
```
'''


FAILURE_MODES_SECTION = '''# Failure Modes

```yaml
failure_modes:
  missing_kb_slug:
    response: "Stop and request a kb_slug before touching files."

  missing_kb_root:
    response: "Route to scaffold mode and propose the required KB root paths."

  missing_kb_schema:
    response: "Create or request kb-schema.md; do not substitute CLAUDE.md."

  missing_raw_source:
    response: "Stop. Do not infer source content from filename, title, or prior summaries."

  duplicate_source_hash:
    response: "Report prior ingest record and ask whether to skip, compare, or re-ingest as a new version."

  phase_2_without_approval:
    response: "Stop after Phase 1. Require the exact operator approval phrase before generating wiki pages."

  same_prompt_phase_2_approval_in_normal_mode:
    response: "Treat as not approved. Require a separate operator turn unless explicit test mode is declared."

  stale_index_detected:
    response: "Run or request Python index rebuild for the machine section before relying on index completeness."

  broken_links_or_orphans:
    response: "Return deterministic lint findings and keep semantic page repair separate."

  contradiction_detected:
    response: "Preserve the contradiction as a review flag or callout; do not silently collapse conflicting claims."

  source_authority_unclear:
    response: "Mark authority as uncertain in the ingest analysis and request operator review."

  source_storage_mode_unclear:
    response: "Default repo-internal durable sources to pointer_only; default external or uploaded sources to copy_into_kb."

  write_outside_kb_root_requested:
    response: "Require explicit operator approval and identify the exact target path before writing."

  external_contact_requested_or_implied:
    response: "Do not contact external authors, maintainers, contributors, recipients, or third parties."
```
'''


COMPLETION_GATE_SECTION = '''# Completion Gate

```yaml
completion_gate:
  valid_completion_requires:
    - requested_mode_identified
    - kb_slug_resolved
    - kb_root_policy_followed
    - source_storage_mode_resolved
    - raw_source_policy_followed_when_ingesting
    - deterministic_vs_semantic_ownership_respected
    - operator_gate_respected_for_ingest_phase_2
    - output_artifact_matches_requested_mode
    - confidence_and_claim_label_not_conflated
    - review_flags_returned_when_uncertainty_exists

  valid_outputs_by_mode:
    scaffold:
      - kb_root_scaffold_plan_or_created_paths
      - kb-schema.md
      - initial_wiki_index
      - initial_source_manifest

    ingest_phase_1:
      - ingest_analysis
      - operator_review_required

    ingest_phase_2:
      - generated_or_updated_wiki_pages
      - updated_manifest
      - updated_index_sections
      - postflight_review_flags

    query:
      - wiki_grounded_answer
      - evidence_pages
      - confidence
      - claim_label
      - knowledge_gaps
      - optional_saved_query_output

    lint:
      - deterministic_health_report
      - semantic_review_flags

    audit:
      - grouped_audit_items
      - proposed_accept_partial_reject_defer_actions
```
'''


SOURCE_POLICY_BLOCK = '''  source_policy:
    raw_sources_are_immutable: true
    preserve_exact_source_filename: true
    preserve_exact_source_path: true
    never_treat_missing_source_as_verified: true
    source_pointer_required_on_generated_pages: true
    source_storage_modes:
      pointer_only:
        use_when: "Source already exists durably inside this repository and should not be duplicated."
        required_fields:
          - source_path
          - source_hash
          - source_storage_mode
      copy_into_kb:
        use_when: "Source is external, uploaded, temporary, or not durably stored in this repository."
        required_fields:
          - source_path
          - source_hash
          - copied_to
          - source_storage_mode
      snapshot_copy:
        use_when: "Source may change and the KB requires a frozen evidence version."
        required_fields:
          - source_path
          - source_hash
          - snapshot_path
          - source_storage_mode
    default_for_repo_internal_sources: pointer_only
    default_for_external_or_uploaded_sources: copy_into_kb

  phase_gate_policy:
    normal_mode:
      same_prompt_approval_allowed: false
      requires_separate_operator_turn: true
    explicit_test_mode:
      same_prompt_approval_allowed: true
      condition: "Phase 1 artifacts must exist before Phase 2 generation begins."
    required_phrase: "approve ingest"

  epistemic_labels:
    confidence:
      allowed:
        - high
        - medium
        - low
        - mixed
        - unknown
    claim_label:
      allowed:
        - raw_source
        - source_backed_summary
        - behavioral_inference
        - working_hypothesis
        - operator_question
        - practitioner_question
'''


WIKI_TEMPLATE_A_ONWARD = '''# Template A - Summary Page

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


JSON_COMPATIBILITY_SECTION = '''

## JSON Output Compatibility Notes

```yaml
json_output_compatibility_notes:
  known_actual_fields:
    common:
      - artifact_name
      - status
      - kb_root
      - findings
    scaffold:
      - dry_run
      - writes_performed
      - created_paths
      - skipped_paths
    hash:
      - path
      - path_type
      - hash_algorithm
      - hash_value
      - file_count
      - bytes_total
    preflight:
      - source_path
      - source_slug
      - source_hash
      - existing_manifest_entry
      - existing_phase_1_analysis
      - index_status
    index:
      - index_path
      - dry_run
      - writes_performed
      - machine_index_section_present
      - llm_summary_section_preserved
      - semantic_content_generated_by_python
      - page_count
      - orphan_pages_count
    lint:
      - checks_run
      - missing_required_paths
      - malformed_frontmatter
      - broken_links
      - orphan_pages
      - missing_source_pointers
      - stale_index
      - manifest_issues
      - audit_shape_issues
    audit:
      - open_count
      - resolved_count
      - deferred_count
      - rejected_count
      - grouped_items
      - malformed_items
      - missing_targets

  compatibility_rule: >
    If this contract and actual apex_kb.py output diverge, update this contract
    or the script in a dedicated reconciliation patch before relying on tests as
    proof of package correctness.
```
'''


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def ensure_repo_root() -> None:
    missing = [str(path) for path in TARGET_PATHS if not path.exists()]
    if missing:
        raise SystemExit("Run from repo root. Missing required files:\n" + "\n".join(missing))


def replace_between(text: str, start_heading: str, end_heading: str, replacement: str) -> str:
    pattern = re.compile(
        re.escape(start_heading) + r".*?(?=" + re.escape(end_heading) + r")",
        flags=re.DOTALL,
    )
    if not pattern.search(text):
        raise RuntimeError(f"Could not locate section {start_heading!r} before {end_heading!r}")
    return pattern.sub(replacement.rstrip() + "\n\n", text)


def replace_from(text: str, start_heading: str, replacement: str) -> str:
    index = text.find(start_heading)
    if index == -1:
        raise RuntimeError(f"Could not locate section {start_heading!r}")
    return text[:index] + replacement.rstrip() + "\n"


def patch_skill(text: str) -> str:
    text = replace_between(text, "# Supporting Files", "# Procedure", SUPPORTING_FILES_SECTION)
    text = replace_between(text, "# Failure Modes", "# Completion Gate", FAILURE_MODES_SECTION)
    text = replace_from(text, "# Completion Gate", COMPLETION_GATE_SECTION)

    if "source_storage_modes:" not in text:
        text = re.sub(
            r"  source_policy:\n"
            r"    raw_sources_are_immutable: true\n"
            r"    preserve_exact_source_filename: true\n"
            r"    preserve_exact_source_path: true\n"
            r"    never_treat_missing_source_as_verified: true\n"
            r"    source_pointer_required_on_generated_pages: true\n",
            SOURCE_POLICY_BLOCK,
            text,
        )
    return text


def patch_wiki_templates(text: str) -> str:
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

def patch_script_contract(text: str) -> str:
    text = re.sub(
        r"  purpose: >\s+Define the deterministic Python interface used by apex-kb for scaffold,\s+source hashing, preflight validation, manifest checks, index structure\s+generation, link validation, orphan detection, stale-index detection, and\s+audit listing\. This contract does not define semantic extraction, page\s+drafting, contradiction interpretation, or query synthesis\.",
        "  purpose: >\n"
        "    Define the deterministic Python interface used by apex-kb for scaffold,\n"
        "    source hashing, preflight validation, manifest checks, index structure\n"
        "    generation, link validation, orphan detection, stale-index detection, and\n"
        "    audit listing. This contract does not define semantic extraction, page\n"
        "    drafting, contradiction interpretation, or query synthesis.",
        text,
    )
    text = re.sub(
        r"  invocation_pattern: >\s+python apex-meta/scripts/apex_kb\.py <subcommand> --kb-root apex-meta/kb/<kb-slug>/ \[options\]",
        "  invocation_pattern: >\n"
        "    python apex-meta/scripts/apex_kb.py [global-options] <subcommand> [subcommand-options]",
        text,
    )
    if '      - "--title"' not in text:
        text = text.replace('      - "--topic-title"\n', '      - "--title"\n      - "--topic-title"\n      - "--force"\n')
    if '      - "--source-slug"' not in text:
        text = text.replace('      - "--source"\n', '      - "--source"\n      - "--source-slug"\n')
    text = text.replace('      - "--algorithm"\n', "")
    text = re.sub(
        r"    directory_hash_rule: >\s+For a directory, hash each contained file deterministically, sort by\s+relative path, then hash the ordered path/hash manifest\.",
        "    directory_hash_rule: >\n"
        "      For a directory, hash each contained file deterministically, sort by\n"
        "      relative path, then hash the ordered path/hash manifest.",
        text,
    )
    if "## JSON Output Compatibility Notes" not in text:
        text = text.rstrip() + JSON_COMPATIBILITY_SECTION
    return text


def patch_operation_rules(text: str) -> str:
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

def patch_apex_kb_py(text: str) -> str:
    return text.replace(
        "- No shell-out except this script's own local validation when called externally.",
        "- No shell-out.",
    )


def build_patches() -> dict[Path, str]:
    return {
        SKILL_PATH: patch_skill(read(SKILL_PATH)),
        WIKI_TEMPLATES_PATH: patch_wiki_templates(read(WIKI_TEMPLATES_PATH)),
        SCRIPT_CONTRACT_PATH: patch_script_contract(read(SCRIPT_CONTRACT_PATH)),
        OP_RULES_PATH: patch_operation_rules(read(OP_RULES_PATH)),
        APEX_KB_PY_PATH: patch_apex_kb_py(read(APEX_KB_PY_PATH)),
    }


def validate_texts(texts: dict[Path, str]) -> list[str]:
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

def make_diff(path: Path, old: str, new: str) -> str:
    return "".join(
        difflib.unified_diff(
            old.splitlines(True),
            new.splitlines(True),
            fromfile=str(path),
            tofile=str(path) + " patched",
        )
    )


def backup(path: Path, backup_root: Path) -> None:
    dest = backup_root / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, dest)


def run_validation() -> int:
    commands = [
        [sys.executable, "apex-meta/scripts/apex_kb.py", "--help"],
        [
            sys.executable,
            "apex-meta/scripts/apex_kb.py",
            "--json",
            "scaffold",
            "--kb-root",
            "apex-meta/kb/apex-kb-contract-smoke",
            "--title",
            "Apex KB Contract Smoke",
        ],
    ]
    failed = False
    for command in commands:
        print(f"\n$ {' '.join(command)}")
        result = subprocess.run(command, text=True, capture_output=True)
        print(f"exit_code: {result.returncode}")
        if result.stdout:
            print(result.stdout[:4000])
        if result.stderr:
            print(result.stderr[:4000])
        if result.returncode != 0:
            failed = True
    return 2 if failed else 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Repair Apex KB package contract and formatting drift.")
    parser.add_argument("--check", action="store_true", help="Show changes without writing.")
    parser.add_argument("--apply", action="store_true", help="Apply changes with backups.")
    parser.add_argument("--validate", action="store_true", help="Run smoke validation commands only.")
    args = parser.parse_args()

    ensure_repo_root()

    if args.validate:
        return run_validation()
    if args.check == args.apply:
        parser.error("Use exactly one of --check or --apply, or use --validate.")

    patched = build_patches()
    findings = validate_texts(patched)
    if findings:
        print("Patch validation failed:")
        for finding in findings:
            print(f"  - {finding}")
        return 2

    changes: list[tuple[Path, str, str]] = []
    for path, new_text in patched.items():
        old_text = read(path)
        new_text = new_text.rstrip() + "\n"
        if old_text.rstrip() + "\n" != new_text:
            changes.append((path, old_text, new_text))

    if not changes:
        print("No changes needed.")
        return 0

    print(f"{len(changes)} file(s) will change.")
    for path, old_text, new_text in changes:
        print("\n" + "=" * 88)
        print(path)
        print("=" * 88)
        diff = make_diff(path, old_text, new_text)
        print(diff[:12000])
        if len(diff) > 12000:
            print("... diff truncated by repair script display ...")

    if args.check:
        return 1

    stamp = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    backup_root = Path(".repair-backups/apex-kb-contract-repair") / stamp
    backup_root.mkdir(parents=True, exist_ok=True)
    for path, _old_text, new_text in changes:
        backup(path, backup_root)
        write(path, new_text)

    print(f"\nApplied repairs. Backups written to: {backup_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
