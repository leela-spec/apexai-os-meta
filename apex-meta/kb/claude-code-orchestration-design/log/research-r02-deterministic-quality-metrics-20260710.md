# R02 — Deterministic Quality Metrics

```yaml
research:
  id: R02
  title: deterministic_quality_metrics
  repository: leela-spec/apexai-os-meta
  branch: main
  date: 2026-07-10
  mode: bounded_read_only_research_with_final_report_write
  repository_changes:
    - this_report_only
```

## Verdict

The smallest useful deterministic measurement set is **seven measurements plus page-type-aware reason rules**:

1. narrative word counts by required section, excluding frontmatter and fenced blocks;
2. Key Claims item count;
3. claim-to-pointer coverage;
4. pointer specificity distribution;
5. ranked-source count;
6. route count;
7. placeholder/template-text detection.

These measurements must remain separate. They must not be combined into a page-value score. A page becomes a repair candidate only through explicit reason-coded rules, normally conjunctions such as “broad summary signal + one ranked source” or “multiple claims + unmapped claim pointers.” Total length alone, prose style, semantic correctness, source relevance, and actual query-answer quality remain outside deterministic authority.

The current implementation misses the observed failure because `is_shell_page_candidate` requires both low density and a missing anchor. Once `source_refs`, `Key Claims`, and `Macro / Meso / Micro` exist, even a page with one generic claim, three one-sentence synthesis layers, and file-only pointers is not a shell candidate. `phase2_repair_candidates` likewise only captures missing headings or missing references.

## Evidence Summary by File

```yaml
evidence_summary:
  root_cause_report:
    path: apex-meta/kb/claude-code-orchestration-design/log/max-run-20260709-phase2-quality-failure-root-cause.md
    decisive_findings:
      - mandatory headings and source_refs were present while section depth remained shallow
      - representative failure had one claim and no line-level evidence
      - current candidate rules omit section counts, claim counts, and pointer specificity
      - acceptance tests cover a visibly empty shell, not a complete-looking thin page

  runtime:
    path: apex-meta/scripts/apex_kb.py
    inspected_symbols:
      - PHASE2_VALUE_HEADINGS
      - extract_source_refs
      - missing_value_headings
      - is_shell_page_candidate
      - quality_report
      - cmd_quality
    decisive_findings:
      - extract_source_refs collapses each source_ref object to one identifier and loses structured pointer detail
      - shell thresholds are 40 words or 200 characters after fenced-code removal
      - shell status additionally requires missing source_refs, Key Claims, or Macro/Meso/Micro
      - strict mode fails only for phase2_repair_candidates or shell_page_candidates

  kb_contract:
    path: .claude/skills/apex-kb/references/kb-contract.md
    decisive_findings:
      - source breadth must adapt to page scope
      - Micro must contain specific details anchored by pointers
      - every claim requires pointer, confidence, and label
      - Routes Here requires question routes and related-page routing
      - uncertainty items require pointer and handling

  wiki_templates:
    path: .claude/skills/apex-kb/templates/wiki-page-templates.md
    decisive_findings:
      - broad pages may require all materially relevant sources
      - narrow pages may validly use one source
      - summary, concept, and entity pages share the five value sections
      - template placeholders are mechanically recognizable

  acceptance_tests:
    path: .claude/skills/apex-kb/references/acceptance-tests.md
    decisive_findings:
      - current shell fixture has no source refs, no required sections, and only “Nothing much here.”
      - current positive retrieval fixture contains literal angle-bracket placeholders
      - neither fixture reproduces a page with all headings and one generic claim

  operational_rules:
    path: .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md
    decisive_findings:
      - quality is explicitly deterministic and structural
      - no LLM grading or page_value_score is allowed
      - report-only is the default; strict mode may block repair candidates
      - semantic review still owns unsupported-claim and source-conflict judgments
```

## Why the Current Algorithm Misses the Failure

```yaml
current_algorithm:
  shell_low_density:
    condition: narrative_words_below_40 OR narrative_chars_below_200
  additional_required_condition:
    any_of:
      - no_source_refs
      - missing_key_claims_heading
      - missing_macro_meso_micro_heading
  repair_candidate:
    any_of:
      - missing_required_heading
      - no_source_refs
  strict_failure:
    any_repair_or_shell_candidate: true
```

The false-negative path is therefore deterministic:

```yaml
false_negative:
  all_required_headings: true
  source_refs_present: true
  key_claims_heading_present: true
  macro_meso_micro_heading_present: true
  claim_count: 1
  synthesis_layers: one_sentence_each
  pointers: file_level_only
  shell_candidate: false
  phase2_repair_candidate: false
  strict_status: ok
```

The implementation also cannot measure claim-pointer coverage correctly because `extract_source_refs` returns source identifiers from frontmatter, not claim-level pointer records from the body.

## Pages Sampled and Decisive Measurements

Counts below are deterministic manual derivations from the bounded sample. Synthesis words exclude headings, frontmatter, and fenced YAML.

```yaml
sampled_pages:
  - id: P01
    path: wiki/summaries/max-run-20260709/claude-code-mechanism-decision-model.md
    category: known_thin_complete
    page_type: summary
    observed:
      synthesis_words: {macro: 10, meso: 27, micro: 12, total: 49}
      source_refs: 1
      ranked_sources: 3
      key_claims: 1
      claim_pointers: 1
      pointer_specificity: {file: 2, section: 0, line_or_span: 0}
      routes: 1
      uncertainty_items: 1
    decisive_result: repair_candidate
    reasons: [single_claim_summary, micro_under_experimental_floor, claim_pointer_file_only]

  - id: P02
    path: wiki/concepts/max-run-20260709/phase2-value-contract.md
    category: known_thin_complete
    page_type: concept
    observed:
      synthesis_words: {macro: 14, meso: 17, micro: 15, total: 46}
      source_refs: 2
      ranked_sources: 2
      key_claims: 1
      claim_pointers: 1
      pointer_specificity: {file: 2, section: 0, line_or_span: 0}
      routes: 1
      uncertainty_items: 1
      explicit_compression_statement: true
    decisive_result: repair_candidate
    reasons: [single_claim_concept, all_synthesis_layers_short, claim_pointer_file_only]

  - id: P03
    path: wiki/concepts/max-run-20260709/deterministic-executor-only-boundary.md
    category: thin_complete_comparator
    page_type: concept
    observed:
      synthesis_words: {macro: 13, meso: 26, micro: 9, total: 48}
      source_refs: 1
      ranked_sources: 1
      key_claims: 1
      claim_pointers: 1
      pointer_specificity: {file: 2, section: 0, line_or_span: 0}
      routes: 1
      uncertainty_items: 1
    decisive_result: repair_candidate
    reasons: [single_claim_concept, micro_under_experimental_floor, claim_pointer_file_only]

  - id: P04
    path: wiki/summaries/max-run-20260709/minimal-claude-orchestration-architecture.md
    category: strongest_sampled_summary
    page_type: summary
    observed:
      synthesis_words: {macro: 44, meso: 27, micro: 35, total: 106}
      source_refs: 4
      ranked_sources: 4
      key_claims: 3
      claim_pointers: 3
      pointer_specificity: {file: 4, section: 0, line_or_span: 0}
      routes: 2
      uncertainty_items: 2
    decisive_result: pass_candidate_rules_with_pointer_warning
    reasons: [only_file_level_pointers_report_only]

  - id: P05
    path: wiki/concepts/max-run-20260709/source-preserving-kb-compile.md
    category: strongest_available_concept_in_run
    page_type: concept
    observed:
      synthesis_words: {macro: 14, meso: 19, micro: 16, total: 49}
      source_refs: 2
      ranked_sources: 2
      key_claims: 1
      claim_pointers: 1
      pointer_specificity: {file: 2, section: 0, line_or_span: 0}
      routes: 1
      uncertainty_items: 1
    decisive_result: repair_candidate
    reasons: [single_claim_concept, all_synthesis_layers_short, claim_pointer_file_only]
    finding: no genuinely strong concept was found in the bounded max-run sample

  - id: P06
    path: wiki/entities/max-run-20260709/claude-code.md
    category: valid_narrow_entity
    page_type: entity
    observed:
      synthesis_words: {macro: 15, meso: 14, micro: 16, total: 45}
      source_refs: 1
      ranked_sources: 1
      key_claims: 1
      claim_pointers: 1
      pointer_specificity: {file: 2, section: 0, line_or_span: 0}
      routes: 1
      uncertainty_items: 1
    decisive_result: valid_concise_with_pointer_warning
    exception_basis: narrow_named_entity_single_primary_source

  - id: F01
    path: references/acceptance-tests.md#v3-repair-shell-page
    category: existing_negative_fixture
    page_type: concept
    observed:
      source_refs: 0
      required_headings: 0
      narrative: Nothing much here.
    decisive_result: strict_failure
    finding: catches obvious shells but not the observed complete-looking failure

  - id: F02
    path: references/acceptance-tests.md#retrieval-page
    category: existing_positive_fixture
    page_type: concept
    observed:
      key_claims: 1
      placeholder_text_detected: true
      uncertainty_items: 0
    decisive_result: should_not_be_positive_quality_fixture
    finding: literal placeholders make it suitable only for command smoke tests
```

## Recommended Minimum Measurements

```yaml
minimum_measurements:
  - id: M01
    name: section_narrative_word_counts
    definition: count word tokens per required section after removing frontmatter, headings, HTML comments, and fenced blocks
    use: candidate conjunction and reporting

  - id: M02
    name: key_claim_count
    definition: count structured list entries under Key Claims, accepting claim_id plus claim fields
    use: page-type-aware candidate rule

  - id: M03
    name: claim_pointer_coverage
    definition: claims with a non-placeholder source_pointer divided by parsed claims; also report unmapped claim ids
    use: strict-capable structural rule

  - id: M04
    name: pointer_specificity_distribution
    definition: classify every pointer as file, section, or line/span using deterministic syntax
    use: report-only by default; candidate conjunction for broad pages or multi-claim pages

  - id: M05
    name: ranked_source_count
    definition: count adaptive_ranked_sources entries with source plus non-placeholder rationale and coverage
    use: broad-scope candidate conjunction

  - id: M06
    name: route_count
    definition: count route entries containing question or related_page and a destination/relation
    use: strict only when zero; count otherwise report-only

  - id: M07
    name: placeholder_template_detection
    definition: detect angle-bracket template tokens, “LLM must fill,” “TODO/TBD,” empty required arrays, and template comments left as content
    use: strict-capable
```

All seven are implementable with `re`, `pathlib`, and existing minimal YAML parsing. Thresholds for short synthesis sections must remain experimental until calibrated with more accepted pages.

## Measurements Rejected

```yaml
rejected_metrics:
  - metric: universal_total_word_threshold
    reason: penalizes narrow pages and rewards padding

  - metric: single_page_value_score
    reason: hides reason codes and creates Goodhart pressure

  - metric: prose_quality_or_elegance
    reason: semantic/style judgment

  - metric: actual_query_answerability
    reason: requires query execution and semantic evaluation

  - metric: source_relevance_or_authority_score
    reason: source ranking quality is semantic

  - metric: uncertainty_count_minimum_greater_than_zero
    reason: a valid page may truthfully have no known uncertainty

  - metric: yaml_or_code_block_ratio_as_failure
    reason: structured sections are intentionally YAML; high ratio alone is not failure

  - metric: duplicate_sentence_detection_as_strict
    reason: useful boilerplate and repeated field labels create false positives

  - metric: source_ref_count_duplicate_of_ranked_source_count
    reason: frontmatter refs and ranked sources serve different purposes; neither count alone proves use

  - metric: macro_meso_micro_semantic_redundancy
    reason: lexical overlap can be reported experimentally but cannot establish semantic redundancy
```

## Page-Type Candidate Rules

Every numeric threshold below is **experimental**, except zero/missing structural conditions.

```yaml
page_type_profiles:
  summary:
    candidate_rules:
      - code: SUMMARY_SINGLE_CLAIM
        when: key_claim_count < 2 AND no concise_exception
      - code: SUMMARY_BROAD_SOURCE_BREADTH_LOW
        when: broad_scope_signal AND ranked_source_count < 2
      - code: SUMMARY_LAYERED_SYNTHESIS_THIN
        when: macro_words < 15 AND meso_words < 15 AND micro_words < 15
      - code: SUMMARY_MULTI_CLAIM_POINTERS_WEAK
        when: key_claim_count >= 2 AND line_or_section_pointer_count == 0

  concept:
    candidate_rules:
      - code: CONCEPT_SINGLE_CLAIM_THIN
        when: key_claim_count < 2 AND all_three_layers_below_experimental_floor
      - code: CONCEPT_MICRO_NOT_EVIDENCED
        when: micro_words < 15 AND specific_pointer_count == 0
      - code: CONCEPT_NO_ROUTE
        when: route_count == 0

  entity:
    candidate_rules:
      - code: ENTITY_NO_IDENTITY_OR_CLAIM
        when: key_claim_count == 0
      - code: ENTITY_MULTI_CLAIM_POINTERS_WEAK
        when: key_claim_count >= 2 AND claim_pointer_coverage < 1.0
      - code: ENTITY_THIN_WITH_BROAD_SIGNAL
        when: broad_scope_signal AND ranked_source_count < 2
    concise_policy: one claim and one source may be valid for a narrowly scoped named entity
```

## Valid Concise-Page Exceptions

```yaml
concise_exceptions:
  - code: NARROW_ENTITY_SINGLE_SOURCE
    requirements:
      - page_type == entity
      - exactly one primary identity scope
      - one ranked source with rationale and coverage
      - at least one claim with non-placeholder pointer
      - at least one usable route
      - no placeholder text

  - code: ATOMIC_CONCEPT_SINGLE_CLAIM
    status: experimental
    requirements:
      - page_type == concept
      - title and definition indicate one bounded rule or boundary
      - one claim only
      - claim pointer is section or line/span specific
      - Macro/Meso/Micro are nonempty and not duplicate text
      - explicit related-page route exists

  - code: SOURCE_SUMMARY_SINGLE_SOURCE
    status: experimental
    requirements:
      - summary explicitly represents one source rather than a broad topic
      - ranked source count equals one
      - source pointer coverage is complete
      - no broad-scope signal
```

Exceptions suppress only threshold-based reasons. They never suppress missing headings, placeholder content, zero routes, or missing claim pointers.

## Broad-Scope Signals

Use only deterministic metadata/title signals; do not infer breadth from prose meaning.

```yaml
broad_scope_signal:
  true_when_any:
    - page_type == summary AND source_refs_count >= 2
    - title contains architecture, model, system, lifecycle, framework, overview, comparison, or design
    - ranked source section already declares multiple source groups
    - frontmatter contains related_concepts or related_entities with two or more entries
  limitations:
    - report signal and triggering evidence
    - do not treat absence as proof of narrowness
```

## Source-Pointer Specificity Grammar

```yaml
pointer_specificity:
  placeholder:
    examples: ["<pointer>", "TODO", "TBD", "NA", ""]
    valid: false

  line_or_span:
    patterns:
      - "path#L12"
      - "path#L12-L24"
      - "path:12"
      - "path:12-24"
      - "path lines 12-24"
    specificity_rank: 3

  section:
    patterns:
      - "path#heading-slug"
      - "path## Heading"
      - "path::Section Name"
      - object with source_path plus source_section
    specificity_rank: 2

  file:
    patterns:
      - repository or KB-relative path without section/line suffix
      - directory path
    specificity_rank: 1

  unknown:
    treatment: report_invalid_or_unclassified
```

A directory pointer is file-level, not line/span-specific. Frontmatter source refs should be parsed as structured records instead of collapsed to one string.

## Repair Candidate Reason Codes

```yaml
reason_codes:
  structural_strict:
    - MISSING_SOURCE_REFS
    - MISSING_REQUIRED_VALUE_SECTION
    - PLACEHOLDER_CONTENT_PRESENT
    - KEY_CLAIM_WITHOUT_POINTER
    - NO_ROUTES

  calibrated_candidate:
    - SINGLE_CLAIM_SUMMARY
    - SINGLE_CLAIM_CONCEPT_THIN
    - ALL_SYNTHESIS_LAYERS_SHORT
    - MICRO_SHORT_WITHOUT_SPECIFIC_POINTER
    - BROAD_SUMMARY_SOURCE_BREADTH_LOW
    - MULTIPLE_CLAIMS_UNMAPPED_POINTERS
    - ONLY_FILE_LEVEL_POINTERS_FOR_BROAD_PAGE

  report_only:
    - TOTAL_NARRATIVE_WORDS_LOW
    - ONLY_FILE_LEVEL_POINTERS
    - EMPTY_UNCERTAINTY_LIST
    - HIGH_STRUCTURED_BLOCK_PROPORTION
    - REPEATED_BOILERPLATE
    - BROAD_SCOPE_SIGNAL
```

Machine-readable candidates should be objects, not path strings:

```yaml
candidate:
  path: wiki/...
  page_type: summary
  reasons: [SINGLE_CLAIM_SUMMARY, ONLY_FILE_LEVEL_POINTERS_FOR_BROAD_PAGE]
  measurements: {}
  experimental_thresholds_used: []
  concise_exception: null
```

## Strict Mode Contract

```yaml
strict_mode:
  always_fail:
    - missing source_refs on summary/concept/entity
    - missing mandatory section
    - placeholder/template content in required sections
    - parsed claim lacking a non-placeholder source_pointer
    - zero usable routes

  fail_after_calibration:
    - broad summary with one ranked source
    - multiple claims with no section/line pointers
    - all Macro/Meso/Micro layers below experimental floor
    - summary or concept below page-type claim minimum

  report_only:
    - total word count
    - file-level pointer usage by itself
    - uncertainty count
    - block proportion
    - boilerplate similarity

  compatibility:
    - keep existing output keys
    - add measurements_by_page and candidate_details
    - retain path-only candidate arrays during one deprecation cycle
    - default command remains nonblocking
```

## Acceptance Fixture Matrix

```yaml
fixtures:
  - fixture: all_headings_one_generic_claim_one_file_pointer
    expected: repair_candidate
    reasons: [SINGLE_CLAIM_SUMMARY_OR_CONCEPT, ONLY_FILE_LEVEL_POINTERS]

  - fixture: three_one_sentence_layers
    expected: repair_candidate_when_all_under_experimental_floor
    reasons: [ALL_SYNTHESIS_LAYERS_SHORT]

  - fixture: broad_summary_insufficient_source_breadth
    expected: repair_candidate
    reasons: [BROAD_SUMMARY_SOURCE_BREADTH_LOW]

  - fixture: valid_narrow_entity_one_source
    expected: pass_with_optional_file_pointer_report
    exception: NARROW_ENTITY_SINGLE_SOURCE

  - fixture: placeholder_filled_sections
    expected: strict_failure
    reasons: [PLACEHOLDER_CONTENT_PRESENT]

  - fixture: yaml_heavy_low_narrative
    expected: report_or_candidate_only_with_other_reason
    reasons: [HIGH_STRUCTURED_BLOCK_PROPORTION]

  - fixture: multiple_claims_without_claim_specific_pointers
    expected: strict_failure
    reasons: [KEY_CLAIM_WITHOUT_POINTER, MULTIPLE_CLAIMS_UNMAPPED_POINTERS]

  - fixture: strong_multi_source_concept
    expected: pass
    requirements:
      - at least two ranked sources
      - at least two claims
      - complete claim-pointer coverage
      - at least one section or line/span pointer
      - usable route
      - no placeholders

  - fixture: concise_valid_page_exception
    expected: pass
    requirements: satisfy one explicit exception profile

  - fixture: existing_missing_heading_shell
    expected: strict_failure
    reasons: [MISSING_SOURCE_REFS, MISSING_REQUIRED_VALUE_SECTION]
```

## Exact Function-Level Change Map

```yaml
change_map:
  apex-meta/scripts/apex_kb.py:
    - function: extract_source_refs
      change: preserve structured source_ref fields and pointer specificity instead of returning identifiers only
    - function: missing_value_headings
      change: retain behavior; optionally return section spans for downstream parsing
    - function: is_shell_page_candidate
      change: replace single boolean heuristic with reason-code evaluation over parsed measurements
    - function: quality_report
      change: add measurements_by_page, candidate_details, concise exceptions, and compatibility path arrays
    - function: cmd_quality
      change: fail strict mode only for strict-enabled reasons; expose experimental reasons separately
    - new_helpers:
        - split_markdown_sections
        - strip_non_narrative_content
        - parse_ranked_sources
        - parse_key_claims
        - parse_routes
        - parse_uncertainty_items
        - classify_source_pointer
        - detect_placeholders
        - detect_broad_scope_signal

  .claude/skills/apex-kb/references/kb-contract.md:
    change: define deterministic measurement boundary, pointer grammar, and concise exceptions without fixed universal counts

  .claude/skills/apex-kb/templates/wiki-page-templates.md:
    change: replace literal placeholder fixtures in acceptance use; clarify claim-specific pointers and narrow-page exception examples

  .claude/skills/apex-kb/references/acceptance-tests.md:
    change: add the complete-looking thin fixtures and a strong passing concept fixture

  .claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md:
    change: document reason-coded candidates, report-only metrics, and strict structural failures
```

## Unresolved Decisions

```yaml
unresolved_decisions:
  - exact experimental per-section floors require calibration against more operator-accepted pages
  - whether summaries require two claims by default or only when broad_scope_signal is true
  - whether section-level pointers are sufficient for broad multi-claim pages or one line/span pointer should be mandatory
  - whether directory pointers should be invalid or remain file-level warnings
  - whether placeholder detection should fail legacy pages immediately or after a compatibility period
  - whether atomic concept exceptions require an explicit frontmatter scope marker
```

## Final Minimum Metric Set

```yaml
final_minimum_metric_set:
  count: 7
  mandatory:
    - section_narrative_word_counts
    - key_claim_count
    - claim_pointer_coverage
    - pointer_specificity_distribution
    - ranked_source_count
    - route_count
    - placeholder_template_detection

  strict_now:
    - missing required section
    - missing source_refs
    - placeholder content in required sections
    - claim without pointer
    - zero usable routes

  candidate_after_calibration:
    - all three synthesis layers short
    - broad summary with insufficient ranked-source breadth
    - summary/concept single-claim thin pattern
    - multi-claim page with only file-level pointers

  report_only:
    - total narrative words
    - only file-level pointers by itself
    - uncertainty count
    - structured-block proportion
    - repeated boilerplate

  prohibited:
    - aggregate page quality score
    - semantic answer-quality judgment
    - universal page word minimum
    - prose-style grading
```

The recommended design catches the observed heading-complete thin pages through transparent, independently inspectable reasons while preserving valid concise entities and keeping semantic usefulness outside deterministic certification.
