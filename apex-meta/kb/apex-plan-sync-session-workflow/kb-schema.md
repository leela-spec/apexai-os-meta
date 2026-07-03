# KB Schema — Apex Plan Sync Session Workflow

```yaml
kb_schema:
  kb_slug: apex-plan-sync-session-workflow
  kb_topic_title: Apex Plan / Apex Sync / Apex Session Workflow Boundary
  source_authority_policy:
    primary:
      - .claude/skills/apex-plan/SKILL.md
      - .claude/skills/apex-sync/SKILL.md
      - .claude/skills/apex-session/SKILL.md
      - .claude/skills/apex-plan/package-manifest.md
      - .claude/skills/apex-sync/package-manifest.md
      - .claude/skills/apex-session/package-manifest.md
    secondary:
      - .claude/skills/*/references/*.md
      - .claude/skills/*/templates/*.md
    excluded:
      - recovery backup folders unless explicitly needed
      - stale .dr/.pro/.v1 variants unless used for historical comparison
  source_storage_policy:
    default_mode: pointer_only
    reason: sources already live in the same repository and should not be duplicated into raw snapshots for this Phase 1 run
  concept_taxonomy_top_level:
    - skill_boundary
    - handoff_interface
    - operator_gate
    - deterministic_computation
    - session_mutation
    - task_record_contract
    - status_enum
    - dependency_policy
    - dry_run_policy
    - H6_handoff
  entity_taxonomy_top_level:
    - apex-plan
    - apex-sync
    - apex-session
    - apex-meta/epics
    - apex-meta/registry
    - apex-meta/handoff
    - scripts/apex_sync.py
  claim_policy:
    each_claim_requires_source_pointer: true
    allowed_confidence:
      - high
      - medium
      - low
      - mixed
      - unknown
    allowed_claim_labels:
      - raw_source
      - source_backed_summary
      - working_hypothesis
      - operator_question
  phase_policy:
    phase1_outputs_path: ingest-analysis/
    phase2_outputs_path: wiki/
    phase2_allowed: false
    phase2_requires_exact_operator_phrase: approve ingest
  forbidden_phase1_behavior:
    - create_wiki_pages
    - mutate_skill_folders
    - mutate_task_or_session_state
    - run_apex_sync_script
    - infer_source_contents_from_names_only
```

## Interpretation rule

This KB treats the three skill folders as a coordinated workflow surface, not as a request to execute planning, sync, or session mutation behavior.
