# Patch Validation Report

The six patches were validated cumulatively in an isolated Git index and then applied to the promotion branch in manifest order. Intentional Markdown hard-break spaces were preserved byte-for-byte; whitespace diagnostics were ignored only for that known formatting.

```yaml
required_checks:
  source_step4_package_unchanged: true
  source_template_hashes_unchanged: true
  promoted_template_hashes_match_sources: true
  yaml_blocks_parse: true
  local_links_resolve: true
  no_duplicate_yaml_keys: true
  no_contract_files_changed: true
  no_step3_files_changed: true
  no_runtime_files_changed: true
  no_round6_patches_applied: true
  owner_manifests_reference_existing_files: true
  entrypoint_references_are_progressively_loaded: true
lifecycle_checks:
  J3_lighter_than_J4: true
  J4_links_to_J5_without_embedding_prompts: true
  J6_evidence_only: true
  J7_candidate_interpretation_only: true
  J9_decision_not_write_confirmation: true
  J10_write_result_evidence: true
  J11_confirmed_truth_only: true
  J12_advisory_until_operator_approval: true
validation_mode: clean_git_index_cumulative_apply
```
