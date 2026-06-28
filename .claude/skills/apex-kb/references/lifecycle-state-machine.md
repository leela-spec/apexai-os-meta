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
    success: S5_operator_gate

  S5_operator_gate:
    gate_phrase: approve ingest
    same_prompt_approval_allowed_normal_mode: false
    success: S6_phase2_ready
    failure: halt

  S6_phase2_ready:
    goal: compiled wiki pages with source pointers, confidence, claim labels, contradictions, questions
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
    goal: expose health, audit items, contradictions, repair actions
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
  phase1_to_phase2_without_approve_ingest: blocked
  retrieval_to_task_mutation: blocked
  audit_to_silent_resolution: blocked
  kb_to_apex_plan_status_mutation: blocked
  kb_to_apex_sync_registry_rebuild: blocked
  kb_to_apex_session_handoff_write: blocked
```
