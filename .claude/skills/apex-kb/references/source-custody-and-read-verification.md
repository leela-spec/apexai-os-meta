# Apex KB Source Custody and Read Verification

```yaml
source_custody_policy:
  artifact_name: apex_kb_source_custody_and_read_verification
  file_role: hardening_policy_for_real_source_copies_and_actual_file_reading
  package_path: ".claude/skills/apex-kb/references/source-custody-and-read-verification.md"
  status: active
  applies_when:
    - ingesting sources for skill-generation KBs
    - ingesting large research-base KBs
    - operator flags pointer-only, memory-based, summary-only, or pseudo-validation risk
    - source corpus contains nested packages, scripts, references, assets, or copied external repos
  non_goal: >
    This file does not define the content domain of any downstream KB. It only hardens
    Apex KB source custody and source-reading behavior.
```

## 1. Problem Statement

```yaml
problem_statement:
  name: pseudo_validation_and_pointer_laziness_failure
  summary: >
    Agents can falsely treat a manifest entry, source pointer, prior summary, path name,
    or previous chat memory as if the underlying source file was actually copied, opened,
    read, and semantically ingested. This creates false-positive validation and weak KBs.
  severity: high
  affected_modes:
    - source_intake_lock
    - ingest_phase_1
    - ingest_phase_2
    - query
    - lint
  core_distinction:
    raw_refs_are_evidence_custody: true
    manifest_is_registration_not_understanding: true
    ingest_analysis_is_source_comprehension: true
    wiki_is_compiled_reusable_knowledge: true
    final_skill_is_distilled_runtime_interface: true
```

## 2. Decision and Change Log

Scores use 1-100, where higher `impact` means higher quality gain, higher `evidence` means stronger support from observed failures and skill-design guidance, and higher `risk` means higher implementation or misuse risk.

```yaml
decision_change_log:
  - id: D001
    title: "Introduce skill_generation source custody profile"
    problem: "Repo-internal sources default to pointer_only, allowing lazy source handling for critical skill research bases."
    alternatives:
      - option: keep_pointer_only_default
        tradeoff: "Lowest storage overhead, highest false-validation risk."
      - option: force_snapshot_copy_for_all_kbs
        tradeoff: "Strongest evidence custody, but overkill for lightweight KBs."
      - option: add_profile_based_override
        tradeoff: "Keeps normal KBs lightweight while making skill-generation KBs strict."
    recommendation: add_profile_based_override
    change: "For skill_generation and research_base KBs, critical sources default to snapshot_copy; pointer_only requires explicit exception."
    impact: 96
    evidence: 94
    risk: 24

  - id: D002
    title: "Require one source-intake lock instead of several control reports"
    problem: "Separate source-universe, acquisition, hash, and completeness files can become bureaucratic and over-engineered."
    alternatives:
      - option: many_specialized_reports
        tradeoff: "Maximum traceability, high process overhead."
      - option: no_control_report
        tradeoff: "Low overhead, repeats the original ambiguity."
      - option: one_source_intake_lock
        tradeoff: "Good traceability with limited file count."
    recommendation: one_source_intake_lock
    change: "Use log/source-intake-lock.md as the human-readable scope, custody, inventory, and exception record."
    impact: 88
    evidence: 91
    risk: 18

  - id: D003
    title: "Promote nested source corpora to first-class source IDs"
    problem: "Important sub-corpora can be buried under a broad parent folder and then skipped or summarized vaguely."
    alternatives:
      - option: keep_parent_only_source_id
        tradeoff: "Simpler manifest, weak authority ranking and missing-file detection."
      - option: promote_every_subfolder
        tradeoff: "Too many sources; noisy ingest plan."
      - option: promote_blueprint_or_package_subcorpora
        tradeoff: "Best balance for sources that carry independent design logic."
    recommendation: promote_blueprint_or_package_subcorpora
    change: "Any nested package/corpus with its own SKILL.md, README, references, scripts, assets, or distinct authority role gets its own source_id."
    impact: 92
    evidence: 89
    risk: 22

  - id: D004
    title: "Add actual file read ledger to Phase 1 analysis"
    problem: "Phase 1 can claim source analysis while only reading metadata or a summary."
    alternatives:
      - option: trust_agent_claim
        tradeoff: "No overhead, weak evidence."
      - option: require_full_verbatim_extraction
        tradeoff: "Too expensive and copyright/token risky."
      - option: require_file_read_ledger
        tradeoff: "Records enough proof without dumping source text."
    recommendation: require_file_read_ledger
    change: "Phase 1 analysis must list files opened/read, sections inspected, skipped files, and reason for skips."
    impact: 97
    evidence: 96
    risk: 20

  - id: D005
    title: "Treat manifest validation as structural only"
    problem: "Manifest presence was treated as evidence that content was read and integrated."
    alternatives:
      - option: manifest_proves_integration
        tradeoff: "False confidence."
      - option: manifest_only_for_registration
        tradeoff: "Requires separate ingest evidence."
    recommendation: manifest_only_for_registration
    change: "Manifest proves custody/registration only; Phase 1 analysis and read ledger prove comprehension."
    impact: 90
    evidence: 93
    risk: 12

  - id: D006
    title: "Gate Phase 2 on source custody and Phase 1 read proof"
    problem: "Wiki pages can be generated from incomplete or weak evidence."
    alternatives:
      - option: phase2_after_manifest_only
        tradeoff: "Fast but unsafe."
      - option: phase2_after_complete_phase1_with_read_ledger
        tradeoff: "Slightly slower but source-grounded."
    recommendation: phase2_after_complete_phase1_with_read_ledger
    change: "For strict profiles, Phase 2 requires copied/snapshotted source plus Phase 1 read ledger unless operator explicitly overrides."
    impact: 95
    evidence: 92
    risk: 25

  - id: D007
    title: "Keep final skill lean; keep evidence in Apex KB"
    problem: "Raw research corpora inside final skills would bloat context and confuse routing."
    alternatives:
      - option: embed_full_kb_in_skill
        tradeoff: "Maximum local package completeness, high context and routing cost."
      - option: keep_only_distilled_references_in_skill
        tradeoff: "Lean runtime, requires repo KB when deep evidence is needed."
    recommendation: keep_only_distilled_references_in_skill
    change: "Apex KB owns raw/refs and wiki; final skills contain compact SKILL.md, references, scripts, assets, and optional KB pointers."
    impact: 86
    evidence: 95
    risk: 15
```

## 3. Source Custody Profiles

```yaml
source_custody_profiles:
  standard:
    default_for_repo_internal_sources: pointer_only
    default_for_external_or_uploaded_sources: copy_into_kb
    pointer_only_allowed: true
    use_when: "Small KBs, stable repo-internal sources, or low-risk reference material."

  skill_generation:
    default_for_repo_internal_sources: snapshot_copy
    default_for_external_or_uploaded_sources: snapshot_copy
    pointer_only_allowed: false
    use_when: "KB will generate or repair Claude/Agent skill packages or other operational packages."
    pointer_only_exception_requires:
      - explicit_operator_approval
      - no_copy_reason
      - stable_source_path
      - source_hash_or_no_hash_reason
      - future_read_access_confirmed
      - exception_recorded_in_source_intake_lock

  research_base:
    default_for_repo_internal_sources: snapshot_copy
    default_for_external_or_uploaded_sources: snapshot_copy
    pointer_only_allowed: false
    use_when: "KB is intended as a durable research base for future synthesis, generation, or evaluation."
    pointer_only_exception_requires:
      - explicit_operator_approval
      - no_copy_reason
      - stable_source_path
      - source_hash_or_no_hash_reason
      - future_read_access_confirmed
      - exception_recorded_in_source_intake_lock
```

## 4. Minimal Strict Intake Process

```yaml
minimal_strict_intake_process:
  step_1_source_intake_lock:
    purpose: >
      Decide accepted source universe, copy/snapshot accepted source files into raw/refs,
      register manifest entries, record source inventory, and record pointer-only exceptions.
    required_writes:
      - "raw/refs/<source-id>/*"
      - "manifests/source-manifest.json"
      - "log/source-intake-lock.md"
    optional_only_if_needed:
      - "separate completeness audit"
      - "separate hash report"
      - "separate reconciliation report"

  step_2_ingest_phase_1:
    purpose: "Read actual raw/refs files and produce one source-grounded analysis artifact."
    required_writes:
      - "ingest-analysis/<source-id>.analysis.md"
    required_evidence:
      - source_access_ledger
      - skipped_file_ledger
      - custody_verdict
    forbidden_writes:
      - "wiki/concepts/*"
      - "wiki/entities/*"
      - "wiki/summaries/*"

  step_3_operator_gate:
    required_phrase: "approve ingest"

  step_4_ingest_phase_2:
    purpose: "Generate compiled wiki pages from approved Phase 1 analysis."
    requires:
      - completed_phase_1_analysis
      - source_access_ledger
      - source_intake_lock_or_operator_override
      - operator_confirmation_phrase
```

## 5. Actual File Read Ledger Requirement

Use this structure inside Phase 1 analysis for strict profiles.

```yaml
source_access_ledger:
  custody_profile: "standard | skill_generation | research_base"
  custody_verdict: "copied_or_snapshotted | pointer_exception_approved | insufficient_custody"
  source_root_examined: "apex-meta/kb/<kb-slug>/raw/refs/<source-id>/"
  files_opened_and_read:
    - path: "<relative path under raw/refs or preserved source path>"
      read_depth: "full | targeted_sections | metadata_only"
      sections_or_ranges: []
      why_read: "<reason this file matters>"
      evidence_contribution: "<what this file contributed to analysis>"
  files_seen_but_not_read:
    - path: "<relative path>"
      reason_not_read: "binary | duplicate | irrelevant | too_large | deferred | inaccessible"
      blocks_phase_2: false
  missing_expected_files:
    - expected_path_or_pattern: "<path or pattern>"
      reason_expected: "<why it should exist>"
      blocks_phase_2: true
  anti_pseudo_validation_check:
    manifest_only_used_as_evidence: false
    prior_chat_memory_used_as_source: false
    path_name_used_as_content_evidence: false
    summary_substituted_for_source: false
```

## 6. Failure Responses

```yaml
failure_responses:
  pointer_only_without_exception:
    response: "Stop strict ingest. Request operator approval for pointer-only exception or copy/snapshot the source into raw/refs."
  manifest_overtrust_detected:
    response: "Downgrade confidence. State that manifest proves registration only, not comprehension."
  source_read_ledger_missing:
    response: "Do not run Phase 2. Create or repair Phase 1 analysis with actual file read ledger."
  nested_source_buried:
    response: "Promote nested package/corpus to first-class source_id or record explicit defer/exclude decision."
  raw_refs_missing_for_strict_profile:
    response: "Stop and perform source_intake_lock before ingest_phase_1."
```
