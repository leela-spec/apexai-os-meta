# Old Agent KB Migration Decision Packet

## 1. Executive Decision

- Carry forward now: source-authority-before-verification, validator-executor-separation, verification-verdict-packet, routing-decision-card, repo-execution-router, exact-span-before-rewrite, and phase-gated-knowledge-promotion as current Apex/Claude-native guardrails.
- Carry forward now: the five-file-agent-kb-scaffold as a reusable doctrine pattern, not as a mandatory physical file layout for every current capability.
- Carry forward now: compact-essence-activation-surface plus scaffold-appendix-split as a general retrieval architecture: small activation pages first, deep evidence pages second.
- Carry forward now: candidate-only-learning-queue discipline. Candidate material must never be treated as runtime truth until promoted by owner/validator gate.
- Carry forward later: owner-validator-agent-kb-model for persistent current agents only after Apex decides which agents are durable enough to justify their own KB roots.
- Carry forward later: selected Meta Detective internal modes as possible future subagent candidates only if repeated use proves that checklist/workflow form is insufficient.
- Preserve as wiki doctrine only: old role names, old OpenClaw runtime/config paths, historical local Windows paths, and old score-scale examples.
- Do not carry forward: automatic recreation of every old role as a permanent current agent.
- Do not carry forward: approval-by-fluency, summary-elevation, advisory-routing-collapse, path-drift, learning queue as runtime truth, or stale current provider/model/cost claims.
- Implementation stance: build a small set of reusable skills, workflows, deterministic lints, and operator gates before adding any new permanent agents.

## 2. Carry-Forward Matrix

| Pattern / Role / Artifact | Source Wiki Page | Carry Forward? | Target Form | Priority | Rationale | Risks |
|---|---|---|---|---|---|---|
| five-file-agent-kb-scaffold | summaries/old-agent-kb-architecture.md; concepts/agent-doctrine-and-promotion-patterns.md | Yes | workflow | P1 | Useful as a doctrine architecture for durable role/capability memory: essence, practices, mistakes, templates, learning queue. | Overfitting current Claude-native artifacts to old file names. |
| compact-essence-activation-surface | summaries/old-agent-kb-architecture.md; concepts/agent-doctrine-and-promotion-patterns.md | Yes | checklist | P0 | Keeps activation and boundary doctrine small enough for token-efficient retrieval. | If too compact, it can hide evidence or unresolved tensions. |
| candidate-only-learning-queue | summaries/old-agent-kb-architecture.md; entities/reusable-artifact-families.md | Yes | operator_gate | P0 | Prevents candidate material from becoming runtime truth without promotion. | Operators may still copy candidate content into active prompts without gate discipline. |
| owner-validator-agent-kb-model | summaries/old-agent-kb-architecture.md; concepts/agent-doctrine-and-promotion-patterns.md | Later | workflow | P2 | Valuable for durable agents, but premature before deciding current persistent-agent set. | Could create agent KB sprawl before agent set is stabilized. |
| scaffold-appendix-split | summaries/old-agent-kb-architecture.md; summaries/reusable-old-agent-kb-patterns.md | Yes | workflow | P1 | Supports compact retrieval surfaces plus deeper evidence/QA ledgers. | Appendix sprawl without index-first retrieval. |
| internal-mode-not-agent | summaries/old-agent-role-system.md; entities/meta-detective-internal-modes.md | Yes | wiki_doctrine_only | P0 | Key anti-agent-sprawl principle: modes are validation lenses, not agents by default. | Useful modes may be underpowered if left only as doctrine. |
| negative-ownership-boundary | summaries/old-agent-role-system.md; entities/old-agent-roles.md | Yes | checklist | P0 | Strong anti-drift mechanism; every current role/skill/workflow should define not-owned surfaces. | Boundaries can become stale if not updated after architecture changes. |
| validator-executor-separation | summaries/handoff-validation-and-risk-doctrine.md; concepts/validation-and-routing-guardrails.md | Yes | operator_gate | P0 | Validators should return findings, gaps, stop conditions, and owner routes; they should not patch/self-approve. | Slows small tasks if applied too broadly; needs risk threshold. |
| source-authority-before-verification | summaries/handoff-validation-and-risk-doctrine.md; concepts/validation-and-routing-guardrails.md | Yes | skill | P0 | Source authority classification must precede verification, handoff, approval, or repo write. | Can become ceremonial unless tied to concrete source classes and stop conditions. |
| verification-verdict-packet | summaries/handoff-validation-and-risk-doctrine.md; concepts/validation-and-routing-guardrails.md | Yes | skill | P0 | High-risk outputs need verdict, evidence gap, stop condition, next owner/validator route. | Packet bloat if required for every small task. |
| routing-decision-card | summaries/handoff-validation-and-risk-doctrine.md; concepts/validation-and-routing-guardrails.md | Yes | workflow | P0 | Converts ambiguous advisory routing into explicit owner, operation class, allowed/forbidden actions. | May duplicate repo-execution-router unless scoped. |
| repo-execution-router | summaries/handoff-validation-and-risk-doctrine.md; concepts/validation-and-routing-guardrails.md | Yes | deterministic_script_or_lint | P0 | Repo-affecting work requires paths, operation class, checks, stop conditions, commit strategy before writes. | A deterministic lint cannot judge all semantic intent; keep LLM gate too. |
| approval-by-fluency | summaries/handoff-validation-and-risk-doctrine.md | No | deprecated_do_not_carry_forward | P0 | Explicit failure pattern: polished text is not proof. | None; must be blocked. |
| summary-elevation | summaries/handoff-validation-and-risk-doctrine.md | No | deprecated_do_not_carry_forward | P0 | Summaries must not become source truth without source checks. | Easy to reappear in chat handovers. |
| advisory-routing-collapse | summaries/handoff-validation-and-risk-doctrine.md | No | deprecated_do_not_carry_forward | P0 | Advisory routing must not silently become repo execution or final approval. | High if connectors/tools are available and instructions are vague. |
| path-drift | summaries/handoff-validation-and-risk-doctrine.md; concepts/migration-safety-patterns.md | No | deterministic_script_or_lint | P0 | Old/local/current paths must not be confused; exact repo-relative paths required before writes. | Lint needs allowlists for historical source mentions. |
| phase-gated-knowledge-promotion | summaries/reusable-old-agent-kb-patterns.md; concepts/agent-doctrine-and-promotion-patterns.md | Yes | operator_gate | P0 | Maintains source -> candidate -> accepted doctrine -> runtime truth separation. | Gate fatigue if every small edit requires manual approval. |
| appendix-first-evidence-architecture | summaries/reusable-old-agent-kb-patterns.md | Yes | workflow | P1 | Preserves evidence, rankings, examples, QA traces behind compact summaries. | Evidence appendices can become unreadable if not chunked. |
| exact-span-before-rewrite | summaries/migration-to-claude-native-orchestration.md; concepts/migration-safety-patterns.md | Yes | checklist | P0 | Prevents broad rewrite drift; required before editing existing doctrine or specs. | Slower for obvious small copy edits. |
| retrieval-isolation-chunking-rule | summaries/reusable-old-agent-kb-patterns.md; concepts/agent-doctrine-and-promotion-patterns.md | Yes | workflow | P1 | Small self-contained knowledge units improve KB retrieval and reduce hallucination. | Too much fragmentation can hide cross-page dependencies. |
| constant-frame-control | summaries/handoff-validation-and-risk-doctrine.md; summaries/migration-to-claude-native-orchestration.md | Yes | workflow | P1 | Prevents promptflow drift and task expansion. | Can overconstrain exploratory synthesis if not relaxed intentionally. |
| old OpenClaw runtime paths | summaries/migration-to-claude-native-orchestration.md; concepts/migration-safety-patterns.md | No | deprecated_do_not_carry_forward | P0 | Historical source evidence only; not current runtime authority. | High if copied into implementation prompts. |
| old role roster as current agent set | summaries/old-agent-role-system.md; entities/old-agent-roles.md | No | deprecated_do_not_carry_forward | P0 | Role roster is useful evidence but not current authorization. | Agent sprawl; duplicated ownership. |
| validation templates | entities/reusable-artifact-families.md | Yes | checklist | P1 | Can become checklists/operator gates without creating new agents. | Needs consolidation to avoid template overlap. |
| mistakes/failure pattern files | entities/reusable-artifact-families.md | Yes | wiki_doctrine_only | P2 | Useful anti-pattern corpus for current skills/workflows. | Can become negative folklore unless tied to countermeasures. |
| Alfred | summaries/old-agent-role-system.md; entities/old-agent-roles.md | Partial | workflow | P1 | Intake and bounded handoff are useful; not enough reason to recreate old Alfred as permanent agent from this KB alone. | Losing a simple operator-facing front door if no replacement exists. |
| Meta Ops | summaries/old-agent-role-system.md; entities/old-agent-roles.md | Partial | workflow | P1 | Orchestration/sequencing patterns are useful; execution control must map to current workflow surfaces. | Could become overly broad executor if made permanent. |
| Meta Strategy | summaries/old-agent-role-system.md; entities/old-agent-roles.md | Partial | checklist | P2 | Option framing and recommendation packets are reusable, but not necessarily a persistent agent. | Strategy authority drift into implementation. |
| Meta Detective | summaries/old-agent-role-system.md; entities/meta-detective-internal-modes.md | Yes | skill | P0 | Adversarial validation is high-value and maps well to source-authority/verdict packet skill. | If too broad, becomes blocking meta-review for all work. |
| Special Ops Knowledge Bank | entities/old-agent-roles.md; entities/reusable-artifact-families.md | Partial | workflow | P1 | KB lifecycle routing and candidate ledgers are useful as Apex KB workflows. | Confusion with canonical apex-kb skill ownership. |
| Special Ops Informatics Design | entities/old-agent-roles.md | Partial | checklist | P2 | Taxonomy/chunking/retrieval clarity can become KB design checklist. | Might duplicate KB contract/template rules. |
| Special Ops Hygiene Clean | summaries/handoff-validation-and-risk-doctrine.md; entities/old-agent-roles.md | Yes | deterministic_script_or_lint | P0 | Pointer integrity, stale-state checks, closure safety map to deterministic lint/audit. | Semantic quality cannot be fully linted. |
| Special Ops Prompts Workflows | entities/old-agent-roles.md; summaries/reusable-old-agent-kb-patterns.md | Partial | workflow | P1 | Prompt structures and handoff templates are useful in workflow library. | Prompt template sprawl. |
| Special Ops AI Handling Routing | summaries/handoff-validation-and-risk-doctrine.md; entities/old-agent-roles.md | Partial | checklist | P2 | Advisory tool/model posture is useful, but runtime provider/config authority must not migrate. | Advisory-routing-collapse; stale current model/provider facts. |

## 3. Recommended Current Architecture Mapping

```yaml
current_architecture_mapping:
  five-file-agent-kb-scaffold:
    current_surface: workflow
    decision: "Generalize into a capability-doctrine scaffold for durable agents/skills/workflows: essence, practices, mistakes, templates, learning queue. Do not require every current capability to physically use old filenames."

  compact-essence-activation-surface:
    current_surface: checklist
    decision: "Create a compact activation checklist for any persistent agent or high-value skill: purpose, owns, not_owns, trigger, source authority, failure modes, escalation."

  candidate-only-learning-queue:
    current_surface: operator_gate
    decision: "Formalize a learning-queue promotion gate: candidate -> reviewed candidate -> accepted doctrine -> runtime instruction."

  owner-validator-agent-kb-model:
    current_surface: workflow
    decision: "Use as a workflow for durable role/capability KBs. Do not instantiate separate owner/validator agents until the current agent roster is decided."

  scaffold-appendix-split:
    current_surface: workflow
    decision: "Use in Apex KB page design: compact wiki pages for retrieval; appendices/deep pages for evidence, rankings, ledgers, examples, QA traces."

  internal-mode-not-agent:
    current_surface: wiki_doctrine_only
    decision: "Preserve as default doctrine. Promote internal modes only by explicit operator decision after repeated usage proves checklist/workflow insufficiency."

  negative-ownership-boundary:
    current_surface: checklist
    decision: "Add required 'does_not_own' section to current skill/workflow/agent artifacts."

  validator-executor-separation:
    current_surface: operator_gate
    decision: "High-risk reviews must separate validator findings from executor patching and final approval."

  source-authority-before-verification:
    current_surface: skill
    decision: "Create a reusable source authority + verification posture skill or subroutine used before accepting handovers, research, validation, or repo writes."

  verification-verdict-packet:
    current_surface: skill
    decision: "Create a standard verdict packet format: verdict, evidence read, source authority class, gaps, risks, stop condition, next owner."

  routing-decision-card:
    current_surface: workflow
    decision: "Use when routing between LLM chat, Codex/local agent, GitHub connector, deterministic scripts, and operator gates."

  repo-execution-router:
    current_surface: deterministic_script_or_lint
    decision: "Create a repo-write preflight checklist and optional lint that flags missing exact paths, operation class, allow/forbid list, postflight, and commit strategy."

  approval-by-fluency:
    current_surface: deprecated_do_not_carry_forward
    decision: "Block as an anti-pattern. Require evidence, read-back, diff, test, schema, or acceptance criterion."

  summary-elevation:
    current_surface: deprecated_do_not_carry_forward
    decision: "Block as an anti-pattern. Summaries may guide retrieval but cannot replace source-backed wiki pages or raw sources where precision matters."

  advisory-routing-collapse:
    current_surface: deprecated_do_not_carry_forward
    decision: "Block. Advisory route recommendations are not execution authority."

  path-drift:
    current_surface: deterministic_script_or_lint
    decision: "Use path checks and exact-span-before-rewrite discipline before modifying repo files."

  phase-gated-knowledge-promotion:
    current_surface: operator_gate
    decision: "Adopt as current Apex KB and orchestration doctrine: source/candidate/accepted/runtime layers remain separate."

  appendix-first-evidence-architecture:
    current_surface: workflow
    decision: "Use for complex doctrine where compact pages need backing evidence. Pair with retrieval-isolation chunking."

  exact-span-before-rewrite:
    current_surface: checklist
    decision: "Before rewriting existing artifacts, require exact target span, reason, replacement, expected diff, and rollback strategy."

  retrieval-isolation-chunking-rule:
    current_surface: workflow
    decision: "Design wiki pages and doctrine files so each retrieved chunk is self-contained and source-labeled."

  constant-frame-control:
    current_surface: workflow
    decision: "Use in long promptflows and multi-chat handovers to prevent scope drift. Include mission, non-goals, allowed writes, stop conditions, and final report shape."
```

## 4. Role Migration Decisions

```yaml
roles:
  - old_role: "alfred"
    keep_as_current_agent: false
    target_form: "workflow"
    rationale: "Old Alfred's operator intake, constraint capture, and bounded handoff framing are useful as an intake/routing workflow. The KB does not justify recreating Alfred as a permanent current agent by itself."
    risks:
      - "Operator-facing entrypoint may become fragmented if no current surface replaces it."
      - "Handoff framing can become final strategy if boundaries are weak."
    required_next_artifact: "operator-intake-and-bounded-handoff.workflow.md"

  - old_role: "meta_ops"
    keep_as_current_agent: false
    target_form: "workflow"
    rationale: "Meta Ops contains orchestration, specialist activation, sequencing, and bounded synthesis patterns. These should become workflow rules before any persistent executor agent is created."
    risks:
      - "Executor-like role could swallow strategy, validation, and config authority."
      - "Permanent agent form may create coordination overhead."
    required_next_artifact: "orchestration-execution-boundary.workflow.md"

  - old_role: "meta_strategy"
    keep_as_current_agent: false
    target_form: "checklist"
    rationale: "Option framing, scenario comparison, timing analysis, leverage analysis, and recommendation packets are reusable as strategy checklist sections. Current persistent-agent need is unproven."
    risks:
      - "Strategy recommendations may be mistaken for implementation approval."
      - "Could duplicate product/project planning layers."
    required_next_artifact: "strategy-recommendation-packet.checklist.md"

  - old_role: "meta_detective"
    keep_as_current_agent: false
    target_form: "skill"
    rationale: "Meta Detective's source-authority challenge, contradiction surfacing, drift challenge, risk review, and verdict packets are high-value as a reusable validation skill. Keep agent creation deferred."
    risks:
      - "Overuse can become blocking meta-review."
      - "Validator may be asked to implement fixes unless separation is explicit."
    required_next_artifact: "source-authority-and-verdict-packet.skill.md"

  - old_role: "special_ops__knowledge_bank"
    keep_as_current_agent: false
    target_form: "workflow"
    rationale: "Source manifesting, candidate ledgering, appendix architecture, and KB lifecycle routing belong in Apex KB workflows and templates, not a separate current agent by default."
    risks:
      - "Could conflict with canonical apex-kb ownership."
      - "Candidate ledgering can become runtime truth without gate."
    required_next_artifact: "kb-candidate-to-canon-promotion.workflow.md"

  - old_role: "special_ops__informatics_design"
    keep_as_current_agent: false
    target_form: "checklist"
    rationale: "Taxonomy, terminology stability, chunking, and retrieval clarity should become a KB/page design checklist."
    risks:
      - "Checklist may overlap with kb-contract and wiki templates."
      - "Terminology decisions may become domain truth without source authority."
    required_next_artifact: "retrieval-isolated-page-design.checklist.md"

  - old_role: "special_ops__hygiene_clean"
    keep_as_current_agent: false
    target_form: "deterministic_script_or_lint"
    rationale: "Structural QA, pointer integrity, stale-state checks, and closure safety are best implemented as lint/audit checks plus a closure checklist."
    risks:
      - "Not all semantic defects are lint-detectable."
      - "False positives if historical-source paths are not exempted."
    required_next_artifact: "repo-and-kb-hygiene-lint-spec.md"

  - old_role: "special_ops__prompts_workflows"
    keep_as_current_agent: false
    target_form: "workflow"
    rationale: "Prompt structures, workflow-stage patterns, handoff templates, and anti-drift promptflows should become a reusable workflow library."
    risks:
      - "Prompt-template sprawl."
      - "May bypass source-authority gates if templates are too execution-oriented."
    required_next_artifact: "constant-frame-control-and-handoff.workflow.md"

  - old_role: "special_ops__ai_handling_routing"
    keep_as_current_agent: false
    target_form: "checklist"
    rationale: "Advisory model/tool posture and handoff readiness are useful, but provider policy, runtime config, and final approval authority must not migrate from old role doctrine."
    risks:
      - "Stale provider/model/cost claims."
      - "Advisory routing collapse into execution/config mutation."
    required_next_artifact: "ai-tool-routing-readiness.checklist.md"
```

## 5. Internal Mode Migration

```yaml
internal_modes:
  - mode: "evidence_source_verifier"
    target: "skill_subroutine"
    rationale: "Directly supports source-authority-before-verification and verdict packet generation."
    not_promoted_to_agent_by_default: true
    risk: "Can become slow if invoked for trivial claims."

  - mode: "contradiction_logic_auditor"
    target: "checklist_section"
    rationale: "Best as a required section inside validation/verdict workflows: contradictions, inference jumps, unsupported claims."
    not_promoted_to_agent_by_default: true
    risk: "May be skipped unless embedded in a standard packet."

  - mode: "boundary_authority_guardian"
    target: "workflow_step"
    rationale: "Useful before promotion, repo writes, config changes, or role/scope expansions."
    not_promoted_to_agent_by_default: true
    risk: "Boundary review can become subjective without an owns/not-owns table."

  - mode: "risk_failure_mode_red_teamer"
    target: "future_subagent_candidate"
    rationale: "Could justify a future subagent for high-risk architecture changes, but starts as workflow/checklist logic."
    not_promoted_to_agent_by_default: true
    risk: "Premature subagent form increases coordination cost."

  - mode: "verdict_escalation_synthesizer"
    target: "skill_subroutine"
    rationale: "Needed to standardize verdict, confidence, evidence gap, escalation, and next-owner output."
    not_promoted_to_agent_by_default: true
    risk: "Can sound authoritative unless evidence and limits are mandatory fields."
```

## 6. Immediate Build Queue

```yaml
immediate_build_queue:
  skills_to_create_or_update:
    - name: "source-authority-and-verdict-packet"
      target_path_or_surface: ".claude/skills/source-authority-and-verdict-packet/SKILL.md"
      source_wiki_pages:
        - "wiki/summaries/handoff-validation-and-risk-doctrine.md"
        - "wiki/concepts/validation-and-routing-guardrails.md"
        - "wiki/entities/meta-detective-internal-modes.md"
      why_now: "Highest leverage carry-forward: blocks approval-by-fluency and enforces source-authority-before-verification plus validator-executor separation."
      acceptance_criteria:
        - "Defines trigger conditions for high-risk validation, handoffs, repo writes, and migration decisions."
        - "Outputs verdict, source authority class, evidence read, evidence gaps, risks, stop conditions, and next owner."
        - "Explicitly forbids implementing fixes or self-approving its own reviewed artifact."
        - "Includes compact examples for PASS, PASS_WITH_WARNINGS, FAIL, and NEEDS_OPERATOR_DECISION."

    - name: "kb-candidate-to-canon-promotion"
      target_path_or_surface: ".claude/skills/apex-kb/references/knowledge-promotion-rules.md or Apex KB workflow surface"
      source_wiki_pages:
        - "wiki/summaries/old-agent-kb-architecture.md"
        - "wiki/concepts/agent-doctrine-and-promotion-patterns.md"
        - "wiki/entities/reusable-artifact-families.md"
      why_now: "Prevents learning queues, Phase 0 navigation hints, or summaries from becoming runtime doctrine."
      acceptance_criteria:
        - "Defines source, candidate, accepted doctrine, and runtime truth states."
        - "Requires owner/validator review before promotion."
        - "Specifies demotion/deprecation path for rejected candidate material."
        - "Can be used inside Apex KB and current orchestration doctrine."

  workflows_to_create:
    - name: "constant-frame-control-and-handoff"
      target_path_or_surface: ".claude/workflows/constant-frame-control-and-handoff.md"
      source_wiki_pages:
        - "wiki/summaries/handoff-validation-and-risk-doctrine.md"
        - "wiki/summaries/migration-to-claude-native-orchestration.md"
      why_now: "Reduces promptflow drift in multi-chat/agent/Codex handoffs."
      acceptance_criteria:
        - "Includes mission, non-goals, source hierarchy, allowed writes, forbidden writes, stop conditions, final report shape."
        - "Requires exact current state and next phase instead of lifecycle recreation."
        - "Requires explicit operator gates where applicable."

    - name: "orchestration-execution-boundary"
      target_path_or_surface: ".claude/workflows/orchestration-execution-boundary.md"
      source_wiki_pages:
        - "wiki/summaries/old-agent-role-system.md"
        - "wiki/entities/old-agent-roles.md"
      why_now: "Converts old Meta Ops/Alfred role boundaries into current workflow boundaries without recreating permanent agents."
      acceptance_criteria:
        - "Defines intake, route, execute, validate, approve, and escalate ownership."
        - "Includes negative ownership boundaries."
        - "Prevents validators from patching and advisors from mutating config."

  deterministic_scripts_or_lints_to_create:
    - name: "repo-execution-router-lint"
      target_path_or_surface: "apex-meta/scripts/apex_repo_execution_router_lint.py or integrated deterministic lint command"
      source_wiki_pages:
        - "wiki/concepts/validation-and-routing-guardrails.md"
        - "wiki/concepts/migration-safety-patterns.md"
      why_now: "Repo-affecting work repeatedly needs exact paths, allowed/forbidden writes, checks, and commit strategy."
      acceptance_criteria:
        - "Flags missing repo-relative paths in execution handovers."
        - "Flags missing operation class, allowed writes, forbidden writes, postflight checks, and stop conditions."
        - "Flags old OpenClaw/local Windows paths unless marked historical source evidence."
        - "Runs read-only by default."

    - name: "historical-path-authority-lint"
      target_path_or_surface: "apex-meta/scripts/apex_historical_path_authority_lint.py or integrated KB lint rule"
      source_wiki_pages:
        - "wiki/summaries/migration-to-claude-native-orchestration.md"
        - "wiki/concepts/migration-safety-patterns.md"
        - "audit/semantic-open-questions.md"
      why_now: "Prevents old runtime/config/local paths from being imported as current authority."
      acceptance_criteria:
        - "Differentiates historical source mentions from current target paths."
        - "Requires explicit marker for non-binding legacy paths."
        - "Reports candidate drift without modifying files."

  operator_gates_to_formalize:
    - name: "candidate-to-canon-promotion-gate"
      target_path_or_surface: "Apex KB operator gate doctrine"
      source_wiki_pages:
        - "wiki/concepts/agent-doctrine-and-promotion-patterns.md"
        - "wiki/entities/reusable-artifact-families.md"
      why_now: "Current architecture needs a reusable way to promote lessons without contaminating runtime truth."
      acceptance_criteria:
        - "Requires source refs or source-backed rationale."
        - "Requires owner and validator route."
        - "Records explicit operator decision for runtime-impacting promotion."

    - name: "validator-executor-separation-gate"
      target_path_or_surface: "Repo/KB high-risk operation gate"
      source_wiki_pages:
        - "wiki/summaries/handoff-validation-and-risk-doctrine.md"
        - "wiki/concepts/validation-and-routing-guardrails.md"
      why_now: "High-risk validation must not self-execute or self-approve."
      acceptance_criteria:
        - "Defines when separation is mandatory."
        - "Defines exceptions for low-risk edits."
        - "Requires final approval owner distinct from executor on high-risk changes."

  wiki_doctrine_to_keep_only:
    - name: "old-agent-role-names-as-historical-entities"
      target_path_or_surface: "KB wiki doctrine"
      source_wiki_pages:
        - "wiki/entities/old-agent-roles.md"
        - "audit/semantic-open-questions.md"
      why_now: "Avoids accidental recreation of old roster."
      acceptance_criteria:
        - "Role pages state historical/non-authorizing status."
        - "Current mappings point to skills/workflows/checklists unless separately approved."

    - name: "meta-detective-internal-modes-default-doctrine"
      target_path_or_surface: "KB wiki doctrine"
      source_wiki_pages:
        - "wiki/entities/meta-detective-internal-modes.md"
      why_now: "Preserves anti-sprawl default."
      acceptance_criteria:
        - "Each mode has target as checklist/workflow/subroutine unless future subagent is explicitly approved."

  deprecated_items_to_block:
    - name: "old-openclaw-runtime-authority"
      target_path_or_surface: "Migration lint/checklist"
      source_wiki_pages:
        - "wiki/summaries/migration-to-claude-native-orchestration.md"
        - "wiki/concepts/migration-safety-patterns.md"
      why_now: "High contamination risk in implementation prompts."
      acceptance_criteria:
        - "Historical paths cannot appear as current targets without explicit operator override."
        - "Provider/model/config authority must require current verification."

    - name: "approval-by-fluency-and-summary-elevation"
      target_path_or_surface: "Validation skill anti-pattern section"
      source_wiki_pages:
        - "wiki/summaries/handoff-validation-and-risk-doctrine.md"
      why_now: "Common failure mode in LLM synthesis and handovers."
      acceptance_criteria:
        - "Validation packet requires concrete evidence beyond polish."
        - "Summaries are explicitly not source truth when source precision matters."
```

## 7. Open Decisions for Operator

```yaml
operator_decisions:
  - decision: "Whether old role names remain historical entities only or become generalized Claude-native concepts."
    options:
      - "Keep old role names only as historical entities; create generalized concept names for current architecture."
      - "Keep old names as aliases for current concepts but not agents."
      - "Promote selected old names into current agent/subagent/skill names."
    recommended_default: "Keep old role names as historical entities; create generalized current concepts and artifact names."
    impact_if_wrong: "If old names are promoted too early, Apex imports old OpenClaw semantics and agent sprawl. If abstracted too aggressively, useful historical doctrine becomes harder to trace."

  - decision: "How to normalize or preserve mixed EVD/IMP/RSK score scales."
    options:
      - "Preserve both score conventions as historical evidence and mark unresolved."
      - "Normalize to one current scale after operator decision."
      - "Deprecate numeric scores and replace with categorical risk/confidence bands."
    recommended_default: "Preserve unresolved for now; do not normalize 1-100 and 1-5 scales silently."
    impact_if_wrong: "Silent normalization can corrupt risk meaning and produce false precision. No normalization can keep old doctrine harder to operationalize."

  - decision: "Whether Meta Detective internal modes should ever become subagents."
    options:
      - "All remain checklist/workflow/skill subroutine doctrine."
      - "Only risk_failure_mode_red_teamer becomes a future subagent candidate for high-risk architecture reviews."
      - "Promote multiple modes into subagents."
    recommended_default: "Keep all as checklist/workflow/skill subroutines; mark risk_failure_mode_red_teamer as future subagent candidate only."
    impact_if_wrong: "Premature subagents increase coordination cost and role drift. Underpromotion may underuse specialized adversarial review for risky changes."

  - decision: "Which patterns become skills versus workflows versus deterministic checks."
    options:
      - "Skills for source authority/verdict packets; workflows for frame control and orchestration boundaries; deterministic checks for path/lint/stale/pointer integrity; operator gates for promotion and validator-executor separation."
      - "Implement most patterns as skills."
      - "Implement most patterns as workflows/checklists and avoid new skills."
    recommended_default: "Use the mixed mapping: skills for reusable LLM judgment procedures, workflows for process sequences, deterministic checks for file/path/schema facts, operator gates for authority changes."
    impact_if_wrong: "Too many skills create fragmentation; too many workflows lack activation power; too many lints create false precision; missing gates allows authority drift."

  - decision: "Which old agent KB roots should receive deeper source-specific expansion."
    options:
      - "Expand only roots tied to immediate build queue."
      - "Expand all old role roots."
      - "Do no expansion; rely on compiled summary/concept/entity pages."
    recommended_default: "Expand only roots tied to immediate build queue after first implementation artifact exposes gaps."
    impact_if_wrong: "Expanding all roots wastes effort and can revive old roster. Expanding none may leave source gaps in high-risk migration decisions."

  - decision: "How old OpenClaw runtime/config references should be marked in future artifacts."
    options:
      - "Require explicit historical-source-evidence marker on every old runtime/config reference."
      - "Move old runtime/config references into separate deprecated appendix."
      - "Delete old runtime/config references from current-facing pages."
    recommended_default: "Require explicit historical-source-evidence marker, with optional deprecated appendix for dense path lists."
    impact_if_wrong: "Weak marking risks current-runtime contamination. Deletion damages source custody and traceability."
```

## 8. Final Recommended Next Step

Create the first current Apex skill artifact for `source-authority-before-verification` + `validator-executor-separation` + `verification-verdict-packet`, using the compiled wiki pages `summaries/handoff-validation-and-risk-doctrine.md`, `concepts/validation-and-routing-guardrails.md`, and `entities/meta-detective-internal-modes.md` as source doctrine.
