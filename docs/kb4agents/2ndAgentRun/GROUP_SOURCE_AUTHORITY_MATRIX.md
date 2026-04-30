# GROUP_SOURCE_AUTHORITY_MATRIX

## Purpose

This matrix summarises the primary and supporting sources for each Special Ops agent cluster, clarifying their roles and read modes. Reviewers can use it to confirm that doctrine derives from the correct authority level.

|Cluster|Primary sources|Supporting sources|Evidence sources|Notes|
|---|---|---|---|---|
|special_ops__informatics_design|INFORMATION_DESIGN_80_20_ESSENCE.md|—|—|Core 80/20 rules for information design.|
|special_ops__prompts_workflows|PROMPT_DESIGN_80_20_BEST_PRACTICE.md; WORKFLOW_80_20_ESSENCE.md; WORKFLOW_BEST_PRACTICES_RESEARCH.md|CODEX_GIT_EXECUTION_ESSENCE.md; CODEX_RESILIENT_MIGRATION_PROCESS.md|—|Provides prompt and workflow doctrine as well as codex execution guidance.|
|special_ops__ai_handling_routing|SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md|SingleGuide_Claude.md; SingleGuide_GPT.md|—|Primary source missing; cluster remains blocked until recovered.|
|special_ops__hygiene_clean|FAILURE_AND_ANTI_DRIFT_LEDGER.md|—|prob – prompt design & process failure.md|Primary ledger missing; doctrine provisional or blocked.|
|special_ops__research_api_cost|Research Agent API Calls Performance & Cost.md|—|—|Manual file describing model performance and cost assumptions.|

## Interpretation

- **Primary sources** hold the highest authority and must be read fully before use.
- **Supporting sources** supplement primary files but cannot override them.
- **Evidence sources** supply concrete examples of failures; they inform mistakes/failures sections without generating positive doctrine.