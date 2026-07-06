# Apex KB Lifecycle State Machine

```yaml
states:
  S0_source_access_precheck:
    entry: verify mandatory project resources or mounted package files
    success: S1_scaffold_ready
    failure: SOURCE_ACCESS_PRECHECK_FAILED

  S1_scaffold_ready:
    goal: create or validate apex-meta/kb/<kb-slug>/
    python_command: apex_kb.py scaffold
    success: S2_source_intake_ready

  S2_source_intake_ready:
    goal: preserve raw source or pointer, hash, storage mode, source manifest
    python_command: apex_kb.py source-intake
    success: S2b_source_payload_manifest_ready

  S2b_source_payload_manifest_ready:
    goal: write deterministic raw-payload custody ledger
    python_command: apex_kb.py generate-source-payload-manifest
    writes_only: manifests/source-payload-manifest.json
    success: S3_phase0_ready

  S3_phase0_ready:
    goal: deterministic pre-LLM navigation artifacts
    python_command: apex_kb.py phase0
    writes_only: manifests/phase0/
    success: S4_phase1_ready

  S4_phase1_ready:
    goal: source-grounded LLM ingest analysis
    python_command: apex_kb.py ingest-phase1 for shell/preflight only
    llm_output: ingest-analysis/<source-slug>.analysis.md
    success: S6_phase2_ready when selected output tier includes wiki output
    safe_mode_success: S5_operator_explicit_stop_before_wiki

  S5_operator_explicit_stop_before_wiki:
    applies_to: [analysis_only, phase1_only, operator_explicit_stop_before_wiki]
    optional_resume_phrase: approve ingest
    success: S6_phase2_ready on explicit resume
    failure: halt

  S6_phase2_ready:
    goal: compiled wiki pages implementing the Phase 2 page value contract (Adaptive Ranked Source Set, Macro / Meso / Micro synthesis, Key Claims with pointers, Routes Here, Uncertainty / Raw Source Reopen Triggers) along with source pointers, confidence, and claim labels
    llm_outputs:
      - wiki/summaries/*.md
      - wiki/concepts/*.md
      - wiki/entities/*.md
      - audit/*.md
      - log/*.md
    success: S7_index_validation

  S7_index_validation:
    goal: deterministic index and validation
    python_commands:
      - apex_kb.py index
      - apex_kb.py lint
      - apex_kb_retrieval.py build-index
      - apex_kb_retrieval.py stale
    success: S8_retrieval_ready

  S8_retrieval_ready:
    goal: local query/retrieval over compiled pages
    python_command: apex_kb_retrieval.py query
    success: S9_query_output_ready

  S9_query_output_ready:
    goal: save reusable cited query packet
    write_path: outputs/queries/
    success: S10_maintenance_ready

  S10_maintenance_ready:
    goal: expose health, audit items, uncertainties, repair actions
    python_commands:
      - apex_kb.py lint
      - apex_kb.py audit
      - apex_kb.py status
      - apex_kb.py health
    boundary: no Plan/Sync/Session/PreCap/FlowRecap/APSU mutation
```

## Invalid transitions

```yaml
invalid:
  phase0_to_wiki_generation: blocked
  phase1_to_phase2_when_output_tier_is_analysis_only_or_operator_explicit_stop_before_wiki: blocked
```

## Operator-facing v3 macro states

```yaml
operator_flow:
  A_prepare: preflight, scaffold, path validation, run profile selection
  B_ingest_and_compile: source intake, payload manifest, Phase 0, semantic analysis, and wiki compile if output tier includes wiki pages
  C_postflight: wiki index, retrieval index, lint, audit, status, quality / coverage report
  D_query_or_maintain: query packets, stale checks, source drift checks, repair backlog
  retrieval_to_task_mutation: blocked
  audit_to_silent_resolution: blocked
  kb_to_apex_plan_status_mutation: blocked
  kb_to_apex_sync_registry_rebuild: blocked
  kb_to_apex_session_handoff_write: blocked
```
