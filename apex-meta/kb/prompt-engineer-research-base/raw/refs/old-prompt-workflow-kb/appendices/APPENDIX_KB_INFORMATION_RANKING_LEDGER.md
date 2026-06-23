# APPENDIX_KB_INFORMATION_RANKING_LEDGER

## Purpose

Information ranking ledger for `special_ops__prompts_workflows` KB-base extraction.

## Ranking model

- `agent_relevance`: 1-5 fit to reusable prompt/workflow construction.
- `actionability`: 1-5 readiness for scaffold/template use.
- `evidence_strength`: 1-5 source convergence and directness.
- `reuse_frequency_likelihood`: 1-5 expected repeated use.
- `drift_risk`: 1-5 risk if misapplied or overgeneralized.

## Ranked information units

|info_id|source_path|source_role|source_section_or_candidate_id|information_unit|agent_relevance|actionability|evidence_strength|reuse_frequency_likelihood|drift_risk|recommended_target_file|appendix_pointer|scaffold_summary_needed|status|
|---|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|---|
|PW-INFO-001|`AIHowTo/BasicFiles4Agents/PromptDesign/PROMPT_DESIGN_80_20_BEST_PRACTICE.md`|primary doctrine|10 non-negotiable rules|Prompt design optimizes for target control, scope control, source authority, preservation invariants, integrity checks, and stop-after-artifact discipline.|5|5|5|5|2|`BEST_PRACTICES.md`|SRC-PW-006|yes|accepted_for_base|
|PW-INFO-002|`AIHowTo/BasicFiles4Agents/WorkflowResearch/WORKFLOW_80_20_ESSENCE.md`|primary doctrine|minimal operating sequence|Serious work should freeze objective, classify overload, bound scope, name authority, execute one deliverable, ground, verify, stop, and decide continue vs migrate.|5|5|5|5|2|`ESSENCE.md`, `BEST_PRACTICES.md`|SRC-PW-007|yes|accepted_for_base|
|PW-INFO-003|`AIHowTo/BasicFiles4Agents/WorkflowResearch/WORKFLOW_BEST_PRACTICES_RESEARCH.md`|primary synthesis|Tier A core doctrine|The strongest workflow model is bounded, stage-gated, artifact-centered execution rather than broad autonomy or one giant multi-phase pass.|5|5|5|5|3|`ESSENCE.md`, `BEST_PRACTICES.md`|SRC-PW-008|yes|accepted_for_base|
|PW-INFO-004|`AIHowTo/BasicFiles4Agents/WorkflowResearch/WorkflowResearchClaude.md`|supporting research output|Candidate Rule Inventory|One-artifact-per-step, stop-after-step, detect-before-correct, patch-before-rewrite, explicit source authority, verify-before-trust, and escalate-don't-guess are Tier A rules.|5|5|4|5|2|`BEST_PRACTICES.md`|SRC-PW-009|yes|accepted_for_base|
|PW-INFO-005|`AIHowTo/BasicFiles4Agents/WorkflowResearch/Prompt4WorkflowResearch.md`|supporting prompt specimen|Frozen target frame|Research prompts should freeze bounded work, one artifact, stop-after-step, detect-before-correct, patch-before-rewrite, source authority, and verification expectations.|5|4|4|4|2|`TEMPLATES.md`|SRC-PW-010|yes|accepted_for_base|
|PW-INFO-006|`AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md`|supporting doctrine|Source authority and verification gates|Source authority is the pre-step gate; verification escalation is the post-step gate. Do not trust output until evidence, diff, file state, or test verifies it.|5|5|5|5|3|`BEST_PRACTICES.md`, `MISTAKES.md`|SRC-PW-011|yes|accepted_for_base|
|PW-INFO-007|`AIHowTo/Codex/CODEX_GIT_EXECUTION_ESSENCE.md`|supporting execution doctrine|required preflight contract|Codex-style execution needs explicit mode, branch, root, closed target file set, allowed actions, forbidden actions, stop conditions, and Git-visible review.|5|5|5|5|4|`TEMPLATES.md`, `BEST_PRACTICES.md`|SRC-PW-012|yes|accepted_for_base|
|PW-INFO-008|`AIHowTo/Codex/CODEX_IMPLEMENTATION_INSTRUCTION_BOUNDED_EXECUTION_WITH_IMPROVEMENT_CAPTURE (1).md`|supporting execution prompt|out-of-mode improvement capture|Detection is allowed; out-of-mode execution is not. Improvements outside the current mode must be captured explicitly and not applied silently.|5|5|5|4|3|`BEST_PRACTICES.md`, `TEMPLATES.md`|SRC-PW-013|yes|accepted_for_base|
|PW-INFO-009|`OpenClaw/04_final-system-setup/Prompt4FinalHarmonization/Extended-thinking-harmonization-prompt-flow.md`|supporting promptflow example|Stages 0-8|Promptflows should source-lock, classify runtime/design split, check coverage, identify contradictions, freeze manifest, bind baselines, generate patchspecs, and hand off deterministically.|4|4|4|3|4|`TEMPLATES.md`|SRC-PW-014|yes|accepted_for_base|
|PW-INFO-010|`OpenClaw/04_final-system-setup/AdvancedUpdateProcess/clean_handover_openclaw_next_chat.md`|supporting handoff example|continuation logic|A clean handoff must state what is settled, what not to redo, exact next job, source priority, risks, and success condition.|5|5|4|4|2|`TEMPLATES.md`, `BEST_PRACTICES.md`|SRC-PW-015|yes|accepted_for_base|
|PW-INFO-011|`OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/KB_RANKINGS_BY_AGENT.md`|primary ledger|special_ops__prompts_workflows section|Top-ranked candidates include prompt/workflow rule inventory, promptflow examples, Codex execution safeguards, and anti-drift evidence.|5|4|4|4|3|appendices|SRC-PW-002|no|accepted_for_appendix|
|PW-INFO-012|`OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/SOURCE_INVENTORY_LEDGER.md`|primary ledger|prompts_workflows rows|Duplicate groups and repo-accessible representatives should prevent redundant source copying and same-filename drift.|4|4|4|3|3|appendices|SRC-PW-003|no|accepted_for_appendix|
|PW-INFO-013|`OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/FAILURE_AND_ANTI_DRIFT_LEDGER.md`|supporting/evidence ledger|KB-PROMPTS-WORKFLOWS rows|Prompt/workflow assets can become hidden runtime law or broad redesign if evidence is over-promoted; safeguards must remain explicit.|5|5|4|5|4|`MISTAKES.md`, anti-drift appendix|SRC-PW-005|yes|accepted_for_base|

## Target allocation summary

|target_file|included_units|allocation_reason|
|---|---|---|
|`ESSENCE.md`|PW-INFO-002, PW-INFO-003|Compresses core lane boundary and workflow doctrine.|
|`BEST_PRACTICES.md`|PW-INFO-001, PW-INFO-002, PW-INFO-003, PW-INFO-004, PW-INFO-006, PW-INFO-008, PW-INFO-010|Holds accepted reusable rules.|
|`MISTAKES.md`|PW-INFO-006, PW-INFO-013|Captures failure patterns and countermeasures.|
|`TEMPLATES.md`|PW-INFO-005, PW-INFO-007, PW-INFO-008, PW-INFO-009, PW-INFO-010|Holds reusable prompt/workflow/handoff/preflight structures.|
|`LEARNING_QUEUE.md`|Deferred variants and gap risks|Candidate-only queue for unvalidated variants.|
|Appendices|PW-INFO-011, PW-INFO-012, PW-INFO-013|Evidence, ledger, and source-manifest depth.|

## Scaffold density rule

Only the compact rule or pointer belongs in scaffold files. Detailed ranking, source rows, and evidence context stay here or in sibling appendices.
