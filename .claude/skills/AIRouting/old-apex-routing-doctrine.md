# Old-Apex Routing Doctrine

## Purpose

```yaml
purpose:
  consumer: AIRouting skill when forming routing recommendations
  role: supplemental advisory doctrine distilled from the old-apex v1 routing role
  source_basis: apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__ai_handling_routing/
  scope: advisory model/surface routing only; never execution, config, or operator override
  citation_note: source files cited per item are evidence pointers, not live paths to load
```

## Best practices

- **Rule:** Freeze the task, non-task, target output, and success criteria before selecting a route. (`ESSENCE.md` core doctrine; `BEST_PRACTICES.md` AIHR-BP-001)
- **Rule:** Classify overload before routing: `one_pass_safe`, `decompose_first`, or `unsafe_in_one_pass`; split multi-target or multi-surface requests before recommending a surface. (`BEST_PRACTICES.md` AIHR-BP-004)
- **Rule:** Decide source-authority tier (`PRIMARY | DERIVED | WORKING | SPECULATIVE | STALE`) before trusting an input as routing basis or forwarding an output. (`BEST_PRACTICES.md` AIHR-BP-003)
- **Rule:** When missing information changes the route or its risk level, ask one focused question or mark the route `needs_input`; never guess silently. (`BEST_PRACTICES.md` AIHR-BP-002)
- **Rule:** Attach an explicit confidence state (`VERIFIED | PROBABLE | WEAK | UNSAFE`) to routing-relevant claims; `VERIFIED` requires evidence produced in the current run. (`MISTAKES.md` AIHR-MISTAKE-003; ranking ledger AIHR-INFO-005)
- **Rule:** Route atomic volatile claims to narrow current verification, not broad deep research; reserve deep-research surfaces for multi-source synthesis with explicit scope bounds and a freshness window. (`appendices/NewAppendices/APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` variant table)
- **Rule:** Before recommending a repo-affecting or code-agent execution route, require an explicit execution surface, operation mode, exact repo-relative target paths, a closed target set, and a post-write verification path. (`BEST_PRACTICES.md` AIHR-BP-005; `TEMPLATES.md` AIHR-TPL-004)
- **Rule:** For bounded file work, recommend minimal-patch discipline; whole-file or semantic-rewrite routing requires explicit rewrite authority. (`BEST_PRACTICES.md` AIHR-BP-006)
- **Rule:** Recommend delegation or handoff only with a handoff package: task, non-goals, source authority, allowed/forbidden actions, expected output, acceptance criteria, fallback, and validator. (`MISTAKES.md` AIHR-MISTAKE-007; `TEMPLATES.md` AIHR-TPL-005)
- **Rule:** A manual-review route needs a reviewable artifact, a named reviewer, acceptance criteria, and a resume condition — otherwise it adds latency without safety. (`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` variant table)
- **Rule:** Reserve refusal/stop for boundary, authority, or safety blocks; recoverable missing input routes to `needs_input` with a target surface instead. (`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` wrong-surface matrix)
- **Constraint:** Stop and flag for operator review when a routing recommendation would modify or imply modification of runtime configuration, provider policy, permissions, credentials, or model-registry authority; the routing lane may recommend, never apply. (`BEST_PRACTICES.md` AIHR-BP-008; `TEMPLATES.md` AIHR-TPL-006)
- **Constraint:** Treat write-capable and execution surfaces as `unsafe_in_one_pass` by default; they become routable only after context read, scope lock, and authorization are confirmed. (`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` route-state implications)

## Known failure modes

- **Avoid:** Routing before objective freeze — choosing model, surface, or handoff while task, non-task, or success criteria are still implicit. (`MISTAKES.md` AIHR-MISTAKE-001)
- **Avoid:** Silent source-authority substitution — treating a summary, prior chat, or memory as stronger than the current direct source. (`MISTAKES.md` AIHR-MISTAKE-002)
- **Avoid:** Verification theater — approving or forwarding output because it is fluent and structured, without evidence, read-back, diff, or source check. (`MISTAKES.md` AIHR-MISTAKE-003)
- **Avoid:** Advisory routing collapsing into execution — chat-side recommendation becoming file mutation without mode lock, exact targets, and post-write verification. (`MISTAKES.md` AIHR-MISTAKE-004)
- **Avoid:** Rewrite reflex — routing a small bounded defect into a broad rewrite or cleanup pass. (`MISTAKES.md` AIHR-MISTAKE-005)
- **Avoid:** Path drift — using a vague filename, guessed repository, or stale path as execution authority; stop on target ambiguity. (`MISTAKES.md` AIHR-MISTAKE-006)
- **Avoid:** Cold handoff — delegating before objective, scope, source authority, expected output, fallback, and validator are explicit, forcing the receiver to rediscover context. (`MISTAKES.md` AIHR-MISTAKE-007)
- **Avoid:** Over-research — routing an atomic fact lookup to a deep-research surface, paying latency and synthesis noise where atomic verification suffices. (`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` wrong-surface matrix)
- **Avoid:** Reasoning-as-evidence — treating a plausible reasoning chain as factual verification; reasoning may plan, source truth requires verification. (`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` wrong-surface matrix)
- **Avoid:** Rubber-stamp review — inserting a human gate with no criteria, reviewer role, or audit trail. (`APPENDIX_KB_MODE_TOOL_VARIANT_COMPARISON.md` wrong-surface matrix)

## Templates worth reusing

- **Template:** Routing decision card — adds `task`, `non_task`, `source_authority`, `overload_class`, `stop_conditions`, `validator`, and `confidence` fields on top of the current routing_decision contract. (`TEMPLATES.md` AIHR-TPL-001)

```yaml
routing_decision_card_extras:
  task:
  non_task:
  source_authority: { primary: , derived_or_supporting: , missing_or_conflicting: }
  overload_class: one_pass_safe | decompose_first | unsafe_in_one_pass
  stop_conditions:
  validator:
  confidence: VERIFIED | PROBABLE | WEAK | UNSAFE
```

- **Template:** Source authority card — for competing inputs, tier each candidate source and record the selected authority, rejected sources, and disposition (`proceed | needs_input | escalate | refuse`). (`TEMPLATES.md` AIHR-TPL-002)
- **Template:** Model/tool fit card — per candidate surface capture `freshness_needed`, `source_grounding_needed`, `write_action_needed`, `irreversible_or_external_action`, and per-option `current_verification_status`. (`TEMPLATES.md` AIHR-TPL-003)
- **Template:** Specialist handoff note — target surface, role requested, task, non-goals, source authority, allowed/forbidden actions, expected output, acceptance criteria, fallback/stop conditions, validator. (`TEMPLATES.md` AIHR-TPL-005)
- **Template:** Config-impact stop note — affected surface, proposed/implied change, why the advisory lane cannot apply it, required review surface, safe advisory output, blocked actions, `status: stopped_for_review`. (`TEMPLATES.md` AIHR-TPL-006)
