---
okf_schema: apex.okf.report-projection.v1
report_id: apex-kb.phase0-stats.v2
canonical_machine_file: manifests/phase0/phase0-stats.json
render_policy: generated_not_authored
---

# Phase 0 Corpus Intelligence Report

## Run

| Field | Value |
|---|---|
| Run ID | `{{RUN_ID}}` |
| Configuration hash | `{{CONFIG_HASH}}` |
| Source roots | {{SOURCE_ROOTS}} |
| Primary topic | `{{TOPIC_ID}}` |

## Corpus statistics

| Metric | Count |
|---|---:|
| Total files observed | {{TOTAL_FILES}} |
| Included files | {{INCLUDED_FILES}} |
| Explicitly excluded files | {{EXCLUDED_FILES}} |
| Unreadable or unsupported files | {{UNREADABLE_FILES}} |
| Total bytes | {{TOTAL_BYTES}} |
| Total headings | {{HEADING_COUNT_TOTAL}} |
| Exact duplicate groups | {{EXACT_DUPLICATE_GROUPS}} |
| Possible version families | {{POSSIBLE_VERSION_FAMILIES}} |

## Files by extension

{{FILE_COUNT_BY_EXTENSION_TABLE}}

## Headings by level

{{HEADING_COUNT_BY_LEVEL_TABLE}}

## Per-topic candidate statistics

| Topic | All candidates | Filename/title | H1 | Heading | Body strong | Body weak | Linked/context | Duplicates collapsed | Work pack | Held in custody | Zero signal |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
{{TOPIC_STATS_ROWS}}

## Locked question coverage signals

This is not a semantic answerability verdict. It only shows whether Phase 0 found candidate evidence signals for each locked question.

{{QUESTION_EVIDENCE_TABLE}}

## Extraction warnings

{{EXTRACTION_WARNING_TABLE_OR_NONE}}

## What the semantic AI will receive

The AI will not receive this entire report as an unbounded prompt. The instruction generator extracts only the current topic's locked questions, bounded source batch, candidate reasons, unresolved signal gaps, and exact output contract.
