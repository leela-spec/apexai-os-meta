# TEMPLATES

## Purpose

Accepted validated reusable AI Handling Routing templates.

Use these templates for advisory routing, model/tool fit notes, source authority checks, and bounded handoffs. Detailed evidence lives in `appendices/`.

## Template schema

```yaml
template_entry:
  id:
  status: accepted | deprecated
  use_when:
  template_body:
  evidence_refs:
  appendix_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  review_due:
```

## Accepted templates

### AIHR-TPL-001 — Routing decision card

- **Status:** accepted
- **Use when:** a request may require model/tool choice, specialist handoff, repo execution, research, or escalation.
- **Evidence refs:** `SingleGuide_Claude.md`; `WORKFLOW_BEST_PRACTICES_RESEARCH.md`; `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md`.
- **Appendix refs:** `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#AIHR-INFO-001`; `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#AIHR-INFO-012`.

```yaml
routing_decision_card:
  task:
  non_task:
  target_output:
  source_authority:
    primary:
    derived_or_supporting:
    missing_or_conflicting:
  overload_class: one_pass_safe | decompose_first | unsafe_in_one_pass
  recommended_surface: browser_chat | repo_execution | deep_research | review_only | manual_review
  recommended_mode:
  target_agent_or_tool:
  constraints:
  stop_conditions:
  fallback_path:
  validator:
  confidence: VERIFIED | PROBABLE | WEAK | UNSAFE
```

### AIHR-TPL-002 — Source authority card

- **Status:** accepted
- **Use when:** current instruction, repo file, summary, memory, prior chat, or external source may conflict.
- **Evidence refs:** `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md`.
- **Appendix refs:** `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#AIHR-INFO-004`.

```yaml
source_authority_card:
  decision_question:
  candidate_sources:
    - source:
      tier: PRIMARY | DERIVED | WORKING | SPECULATIVE | STALE
      authority_scope:
      freshness:
      conflict_notes:
  selected_authority:
  rejected_sources:
  required_verification:
  disposition: proceed | needs_input | escalate | refuse
```

### AIHR-TPL-003 — Model/tool fit card

- **Status:** accepted
- **Use when:** choosing between models, tools, browsing, repo connectors, artifact tools, or handoff surfaces.
- **Evidence refs:** promptflow target lock; source manifest gap-risk note.
- **Appendix refs:** `APPENDIX_KB_SOURCE_MANIFEST.md#Ranking-plausibility-check`; `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-011`.

```yaml
model_tool_fit_card:
  task_type:
  required_capabilities:
  freshness_needed: none | current_verification_required
  source_grounding_needed: none | file | repo | web | user_uploaded | connector
  write_action_needed: false
  irreversible_or_external_action: false
  candidate_options:
    - option:
      fit_reason:
      known_limit:
      current_verification_status: verified_current | needs_current_verification | not_needed
  recommendation:
  fallback:
  stop_for_manual_review: false
```

### AIHR-TPL-004 — Repo execution router

- **Status:** accepted
- **Use when:** advisory routing may become Codex-style or connector-backed repo mutation.
- **Evidence refs:** `CODEX_RESILIENT_MIGRATION_PROCESS.md`; `CODEX_EXECUTION_INSTRUCTION_RELIABLE_REPRODUCED.md`.
- **Appendix refs:** `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#AIHR-INFO-007`; `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-005`.

```yaml
repo_execution_router:
  repo:
  branch:
  target_root:
  operation_class: MOVE_ONLY | CREATE_ONLY | PATCH_PATHS_ONLY | CONTENT_DRAFT_ONLY | VALIDATE_ONLY | mixed_requires_split
  target_files:
    - path:
      action:
      current_sha_or_base_state:
  allowed_actions:
  forbidden_actions:
  required_pre_write_checks:
  required_post_write_checks:
  stop_conditions:
  commit_strategy: one_file_at_a_time | bounded_batch
```

### AIHR-TPL-005 — Specialist handoff note

- **Status:** accepted
- **Use when:** handing work to another agent, Codex, research surface, verifier, or manual review lane.
- **Evidence refs:** `SingleGuide_Claude.md`; `HARMONIZATION_RISK_REGISTER.md`.
- **Appendix refs:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-008`.

```yaml
specialist_handoff_note:
  target_agent_or_surface:
  role_requested:
  task:
  non_goals:
  source_authority:
  files_or_inputs:
  allowed_actions:
  forbidden_actions:
  expected_output:
  acceptance_criteria:
  fallback_or_stop_conditions:
  validator_or_review_owner:
```

### AIHR-TPL-006 — Config-impact stop note

- **Status:** accepted
- **Use when:** routing advice touches `openclaw.json`, runtime model registry, provider policy, permissions, or other config authority.
- **Evidence refs:** promptflow target lock; current seed boundary.
- **Appendix refs:** `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-010`.

```yaml
config_impact_stop_note:
  affected_surface:
  proposed_or_implied_change:
  why_advisory_lane_cannot_apply_it:
  required_review_surface: manual_review | governance_review | config_authority_review
  safe_advisory_output:
  blocked_actions:
  status: stopped_for_review
```

## Template-use rules

- **Rule:** Use the smallest template that makes the route reviewable.
- **Rule:** Mark current model/provider claims as `needs_current_verification` unless verified in the current run.
- **Rule:** Use `repo_execution_router` before any repo write path.
- **Rule:** Use `config_impact_stop_note` whenever advisory guidance touches runtime config authority.
