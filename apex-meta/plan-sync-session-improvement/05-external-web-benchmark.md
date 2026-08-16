# Apex Gate Policy Redesign — External Web Benchmark

Date: 2026-08-16
Original branch: `validation/gate-policy-20260816`
Purpose: independently cross-check the proposed authorization redesign against current public production patterns, official framework documentation, open-source examples, and recent primary research before any Apex skill edits.

## Source hierarchy

This benchmark intentionally prioritizes:

1. current official production/framework documentation;
2. official reference implementations and repositories;
3. official platform design guides;
4. recent primary research when it directly tests the failure mode.

Blog summaries and secondary SEO material were not used as design authority.

## External systems inspected

### 1. OpenAI Agents SDK — human-in-the-loop approvals

Primary docs:
- https://openai.github.io/openai-agents-python/human_in_the_loop/
- https://openai.github.io/openai-agents-python/guardrails/
- https://github.com/openai/openai-agents-python/blob/main/docs/human_in_the_loop.md
- https://github.com/openai/openai-agents-python/blob/main/examples/agent_patterns/human_in_the_loop_stream.py

Observed pattern:
- approval is evaluated on a concrete tool call, not on an abstract parent task;
- a pending call carries tool name and arguments;
- execution state is serializable and resumable;
- a per-call approval is bound to a specific call id;
- broader `always_approve` is explicitly bounded to future calls to the same tool during the same run;
- tool input guardrails can run before approval and are re-run immediately before execution after approval.

APEX implication:
- authorization should be action/payload scoped;
- prior approval should be revalidated immediately before durable mutation;
- authorization lifetime must be explicit rather than assumed indefinitely;
- deterministic guardrails should run even when an approval already exists.

### 2. LangGraph — interrupts and durable HITL

Primary docs:
- https://docs.langchain.com/oss/python/langgraph/interrupts
- https://docs.langchain.com/oss/python/langchain/human-in-the-loop
- https://github.com/langchain-ai/langgraphjs/blob/main/docs/docs/agents/human-in-the-loop.md

Observed pattern:
- workflows checkpoint state and pause at explicit interrupts;
- approval is placed before sensitive actions such as API calls, database changes, financial transactions, or external sends;
- execution resumes from durable state rather than conversational memory;
- code around an interrupt can be re-executed on resume;
- side effects before interrupts therefore need to be idempotent or moved after the interrupt/separated into their own node.

APEX implication:
- the gate must sit immediately before the protected side effect, not merely earlier in planning;
- Session/application steps need idempotency or exact-write checks so crash/retry/resume cannot duplicate mutations;
- persisted authorization state and receipts are more reliable than chat-memory approval.

### 3. Temporal — durable orchestration and side-effect isolation

Primary docs/guides:
- https://docs.temporal.io/
- https://go.temporal.io/platform-hub/ai-engineering
- https://go.temporal.io/platform-hub/ai-engineering/ai-reference-architecture
- https://go.temporal.io/platform-hub/ai-engineering/ai-patterns

Observed pattern:
- Workflows orchestrate; Activities execute non-deterministic I/O and side effects;
- workflow state is durable across failures and long waits;
- human-in-the-loop is expressed through durable messaging primitives rather than polling chat state;
- write-side Activities are at-least-once and therefore should use idempotency keys;
- retries, timeouts, and observability are configured per action/tool rather than by one global workflow risk label.

APEX implication:
- keep authorization/orchestration separate from the action executor;
- bind an idempotency key / mutation identity to any durable write or external action;
- preserve resumable workflow state independently of the AI window;
- action-specific policy is a stronger primitive than task-wide gate inheritance.

### 4. GitHub Actions environments — protected action boundary

Primary docs:
- https://docs.github.com/en/actions/reference/workflows-and-actions/deployments-and-environments
- https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/control-deployments
- https://docs.github.com/en/actions/how-tos/deploy/configure-and-manage-deployments/review-deployments

Observed pattern:
- normal build/test work can run without repeated approval;
- approval is attached to the protected environment/job boundary;
- environment secrets are withheld until protection rules have passed;
- automated protection rules can approve/reject based on external evidence;
- branch restrictions, manual reviewers, automated checks, and non-bypassable rules compose at the same boundary.

APEX implication:
- internal low-risk work can proceed through an approved workflow while specific protected actions remain gated;
- protected resources/actions should stay unavailable until the relevant authorization check passes;
- C1 (keep Sync non-dry-run registry writes explicitly protected) matches a mature deployment pattern.

### 5. Claude Code — deterministic permission policy plus runtime hooks

Primary docs:
- https://code.claude.com/docs/en/permissions
- https://code.claude.com/docs/en/agent-sdk/permissions
- https://code.claude.com/docs/en/permission-modes

Observed pattern:
- permissions are scoped to tools and optional specifiers such as command/path patterns;
- deny / ask / allow are evaluated deterministically with explicit precedence;
- runtime hooks can block or force prompting before execution;
- broad modes are only baselines; specific rules still constrain concrete tool calls;
- locked-down automation can pre-approve an explicit tool set and deny everything else.

APEX implication:
- do not make an LLM semantic classifier the primary authorization engine;
- implement a deterministic authorization validator for scope/action/digest/validity;
- explicit deny/manual rules must override inherited or reusable authorization;
- optional human/LLM semantic review can be an additional layer, not the only layer.

### 6. Anthropic Agent Skills — skill authoring and progressive disclosure

Primary docs/repository:
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
- https://github.com/anthropics/skills
- https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md

Observed pattern:
- `SKILL.md` is a compact control plane, with detailed policy/reference material loaded on demand;
- deterministic/repetitive logic belongs in scripts instead of long natural-language instructions;
- references should stay one level deep from `SKILL.md`;
- concrete examples and evaluations are part of skill quality;
- critical operations need explicit verification/validation steps;
- skill descriptions should clearly define what the skill does and when it triggers.

APEX implication:
- authorization policy should not be duplicated as prose across Plan, Session, Sync, Weekly Orchestrator, and executor skills;
- create one canonical authorization-policy reference / deterministic validator and have affected skills reference it;
- keep each skill's entrypoint concise and authority-specific;
- retain scenario/eval fixtures like the current gate-policy simulator as regression tests.

### 7. Web-search tool design — current official patterns

Primary docs:
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool
- https://platform.claude.com/docs/en/agents-and-tools/tool-use/server-tools
- https://openai.github.io/openai-agents-python/tools/
- https://github.com/openai/openai-agents-python/blob/main/examples/tools/web_search.py

Observed pattern:
- web search is a grounding tool for current or external information, not a default replacement for stable local knowledge;
- domain filters / trusted-source restrictions are first-class controls;
- complex research may use iterative/multiple searches while simple lookups remain bounded;
- search-result filtering reduces irrelevant context before reasoning;
- provenance/citations stay attached to source-backed claims;
- location/freshness/search-context controls belong to the search invocation, not buried in generic agent prose.

APEX implication for research/web-search skills:
- encode search policy explicitly: trigger conditions, source hierarchy, domain constraints, query/search budget, freshness requirement, conflict rule, citation requirement, and stop/escalation conditions;
- prefer primary sources for technical contract validation;
- separate retrieval/filtering from synthesis;
- preserve source references so later Plan/Session decisions can re-open the evidence.

### 8. Recent primary research — commit-time authorization

Primary paper:
- https://arxiv.org/abs/2607.10487
- "Temporary Authority, Permanent Effects: Commit-Time Authorization for LLM Agents" (2026)

Observed result:
- earlier authority evidence can become stale before a durable effect commits;
- prompt caution and single-condition checks were insufficient in the reported controlled invalidation suite;
- successful defenses refreshed/rebound/refused at the durability boundary based on witness freshness, dependency, binding, and eligibility.

APEX implication:
- a pinned approval record is necessary but not sufficient;
- authorization must be revalidated at commit time against current basis, scope, target/action and validity;
- this is the strongest external reason to refine A1 from "reuse prior approval" into "reuse only after commit-time authorization validation."

This paper is recent preprint research, not production standard. It is corroborative evidence, not the sole basis for the design.

## Cross-system convergence

The independent systems converge on the following architecture:

1. **Plan/reason freely inside a bounded scope.**
2. **Represent protected actions explicitly.**
3. **Persist workflow state so pauses/restarts do not depend on chat memory.**
4. **Apply deterministic permission/guardrail checks before the action.**
5. **If human approval is required, bind it to the concrete pending action/payload or a narrowly defined run-scoped class.**
6. **Revalidate authorization immediately before the durable side effect.**
7. **Execute the side effect idempotently.**
8. **Persist a receipt/audit record.**
9. **Resume the workflow without asking again for unrelated already-authorized low-risk work.**

This is materially closer to the proposed A1 model than to either unconditional Session confirmation or task-wide inherited `gate_mode`.

## Updated recommendation for A1

Rename the conceptual model from merely `pinned_action_scoped_authorization` to:

`commit_time_action_authorization`

Candidate minimal fields:

```yaml
authorization:
  authorization_id: <stable id>
  authority_ref: <operator decision / approved packet ref>
  basis_digest: <digest of approved semantic basis>
  allowed_actions: []
  target_scope: []
  constraints: []
  issued_at: <timestamp>
  expires_at: <timestamp-or-null>
  status: active | revoked | expired
```

Candidate commit-time check, in fixed order:

```yaml
commit_authorization_check:
  1_hard_denies_and_manual_overrides: pass
  2_authorization_active_and_not_expired: pass
  3_basis_digest_still_matches: pass
  4_action_class_is_allowed: pass
  5_target_scope_matches: pass
  6_payload_or_mutation_digest_matches_if_bound: pass
  7_deterministic_constraints_and_required_evidence_pass: pass
  8_no_source_conflict_or_duplicate_merge_exception: pass
  9_optional_semantic_delta_reviewer: pass_or_escalate
  10_apply_idempotently_and_write_receipt: execute
```

Important: step 9 is deliberately late and advisory/escalatory. Steps 1-8 should be deterministic wherever possible.

## Updated decisions

### A — authorization representation

**External benchmark strengthens A1, with modification:**

A1 becomes **commit-time action authorization** rather than a passive reusable approval reference.

Confidence: high.

### B — irreversible/external actions

**B1 remains the recommended first rollout.**

OpenAI HITL, LangGraph HITL, and GitHub protected environments all use explicit approval/protection around high-impact side effects. Later B2 pre-authorization can be considered only when the exact action/payload is bound, time-limited, idempotent, and receipted.

Confidence: high.

### C — Apex Sync registry write

**C1 remains recommended.**

The registry non-dry-run boundary is analogous to a protected deployment/resource boundary. The core Plan->Session double-gate fix does not require weakening it.

Confidence: high.

## Skill-design recommendations for Apex

Do not spread the full gate algorithm as repeated prose across all affected skills.

Preferred structure:

```text
.claude/skills/
  apex-plan/SKILL.md
  apex-session/SKILL.md
  apex-session/references/authorization-policy.md   # canonical policy contract
  apex-session/scripts/validate_authorization.py    # only if deterministic implementation is justified
  apex-session/evals/...                            # concrete regression scenarios
```

Other skills should reference the canonical policy only at the exact boundary where they pass or consume authorization evidence.

Whether the canonical policy belongs physically under `apex-session/` or a small shared backbone policy package is still an operator/architecture choice; do not create a new package unless cross-skill use proves it necessary.

### Keep in SKILL.md

- role and authority boundary;
- concise procedure;
- when authorization must be checked;
- failure/route behavior;
- pointers to policy/evals.

### Move out of SKILL.md

- long authorization schema;
- exhaustive exception matrix;
- scenario fixtures;
- deterministic validation code;
- migration detail.

## Web-search / research-skill recommendation

For future Apex research skills, use an explicit research contract rather than generic "search the web" instructions:

```yaml
research_contract:
  search_when:
    - current_or_time_sensitive
    - external_verification_required
    - niche_or_uncertain_fact
  source_priority:
    - primary_official_documentation
    - first_party_repository_or_spec
    - primary_research
    - high_quality_secondary_only_if_needed
  domain_policy: task_specific_allowlist_or_preference
  freshness_policy: explicit_when_material
  search_budget: proportional_to_question_complexity
  retrieval_mode: iterative_search_then_filter
  citation_required: true
  conflict_rule: preserve_disagreement_and_do_not_silently_reconcile
  stop_rule: stop_when_load_bearing_claims_have_primary_support_or_report_gap
```

This mirrors current web-search tool capabilities and reduces hallucination by making evidence policy observable and testable.

## What this benchmark rejects

- task-wide inherited gate level as the sole authorization mechanism;
- relying on an LLM to decide semantic equivalence without deterministic scope/digest/evidence checks;
- storing approval only in conversational memory;
- side effects before the approval/commit check;
- retryable external writes without idempotency identity;
- copying the same large policy prose into every skill;
- generic web research without source/freshness/citation rules.

## Next safe step

No production skill should be edited from this benchmark alone.

Recommended next implementation-preparation artifact:
- a small proposed `authorization-policy.md` contract;
- 10-20 concrete eval fixtures based on both the prior local simulator and the external patterns above;
- a compatibility map showing exactly which current Plan/Session/Weekly fields can carry the authorization witness without adding a new package.

Only after reviewing that concrete contract should the actual Apex skills be changed.
