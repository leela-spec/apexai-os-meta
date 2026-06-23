# APPENDIX_KB_SOURCE_MANIFEST

## Purpose

Source manifest for the `special_ops__prompts_workflows` KB base build.

## Execution lock

- **Working repo:** `leela-spec/MasterOfArts`
- **Target root:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/`
- **Agent:** `special_ops__prompts_workflows`
- **Build mode:** thin scaffold, deep appendices
- **Status:** `verified_base_build_manifest`

## Indexed source set

|source_id|source_path|role|read_mode|manifest_status|why included|
|---|---|---|---|---|---|
|SRC-PW-001|`agent_kb_source_indexes/SPECIAL_OPS_KB_BASE_BUILD_INDEX.md`|primary index|read full|used|Declares the exact source slice and target lock for this agent.|
|SRC-PW-002|`OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/KB_RANKINGS_BY_AGENT.md`|primary ledger|read relevant full section|used|Ranks top candidates for `special_ops__prompts_workflows` and adjacent validation agents.|
|SRC-PW-003|`OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/SOURCE_INVENTORY_LEDGER.md`|primary ledger|read relevant ledger slice|used|Confirms readable corpus, duplicate status, target agents, and triage decisions.|
|SRC-PW-004|`OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/ESSENCE_CANDIDATES.md`|supporting ledger|read relevant candidates|used|Provides compact doctrine candidates and scores.|
|SRC-PW-005|`OpenClaw/04_final-system-setup/NewFinals/ResourceScreeningLedgers/FAILURE_AND_ANTI_DRIFT_LEDGER.md`|supporting/evidence ledger|read relevant candidates|used|Provides anti-drift evidence and safeguard wording.|
|SRC-PW-006|`AIHowTo/BasicFiles4Agents/PromptDesign/PROMPT_DESIGN_80_20_BEST_PRACTICE.md`|primary doctrine|read full|used|Direct prompt-design rules for exact target, scope, authority, preservation, integrity checks, and stop rules.|
|SRC-PW-007|`AIHowTo/BasicFiles4Agents/WorkflowResearch/WORKFLOW_80_20_ESSENCE.md`|primary doctrine|read full|used|Compact workflow doctrine: bounded execution, one deliverable, grounding, verification, and migration decision.|
|SRC-PW-008|`AIHowTo/BasicFiles4Agents/WorkflowResearch/WORKFLOW_BEST_PRACTICES_RESEARCH.md`|primary research synthesis|read full|used|Evidence-weighted workflow tiers and anti-patterns.|
|SRC-PW-009|`AIHowTo/BasicFiles4Agents/WorkflowResearch/WorkflowResearchClaude.md`|supporting research output|read full|used|Candidate rule inventory and 80/20 work protocol table.|
|SRC-PW-010|`AIHowTo/BasicFiles4Agents/WorkflowResearch/Prompt4WorkflowResearch.md`|supporting prompt specimen|skim/read target frame|used|Shows frozen target frame and output contract for workflow research prompts.|
|SRC-PW-011|`AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md`|supporting doctrine|read full|used|Constrains source authority, verification, confidence, and stop/escalation behavior.|
|SRC-PW-012|`AIHowTo/Codex/CODEX_GIT_EXECUTION_ESSENCE.md`|supporting execution doctrine|read full|used|Bounded repo execution, mode locks, path discipline, one-file execution, and review gates.|
|SRC-PW-013|`AIHowTo/Codex/CODEX_IMPLEMENTATION_INSTRUCTION_BOUNDED_EXECUTION_WITH_IMPROVEMENT_CAPTURE (1).md`|supporting execution prompt|read full|used|Out-of-mode improvement capture, closed creation policy, and exact stop conditions.|
|SRC-PW-014|`OpenClaw/04_final-system-setup/Prompt4FinalHarmonization/Extended-thinking-harmonization-prompt-flow.md`|supporting promptflow example|skim|used|Stage model for source lock, contradiction matrix, manifest freeze, and handoff.|
|SRC-PW-015|`OpenClaw/04_final-system-setup/AdvancedUpdateProcess/clean_handover_openclaw_next_chat.md`|supporting handoff example|read full|used|Clean continuation and non-redesign handoff discipline.|

## Coverage check

|check|verdict|notes|
|---|---|---|
|Top-ranked workflow candidates represented|pass|Primary workflow, prompt-design, source-authority, and Codex-execution sources are included.|
|Role fit|pass|Selected content serves prompt/workflow construction, stage gates, bounded execution, handoff, and verification patterns.|
|Informatics-design source use bounded|pass|Informatics-design material is used only for file shape, retrieval clarity, and appendix/scaffold separation.|
|Failure/postmortem authority bounded|pass|Failure material is treated as evidence and safeguard input, not universal doctrine by itself.|
|Scaffold/appendix split|pass|Detailed evidence and rankings are routed to appendices; scaffold files stay compact and navigational.|
|No config/governance expansion|pass|This KB does not claim config authority, QA severity authority, or broad orchestration ownership.|

## Duplication handling

- **Decision:** Same-filename and exact-duplicate groups in the source inventory are represented once through repo-accessible canonical paths.
- **Decision:** Duplicate prompt/workflow essence files are used for convergence, not repeated as separate doctrine.
- **Decision:** Source rows from historical local paths are normalized to current repo-accessible paths when a matching file exists.

## Gap-risk register

|gap_id|missing_or_underused_source|risk|disposition|
|---|---|---|---|
|GAP-PW-001|Additional prompt-design ranking files outside the selected source slice|Medium: may contain useful phrasing variants.|Candidate-only. Capture in `LEARNING_QUEUE.md`; do not block base scaffold.|
|GAP-PW-002|WorkflowResearchGem and other duplicate workflow research variants|Low-medium: may supply alternative wording for the same high-confidence rules.|Not material because selected sources already converge on the same rules. Candidate-only for later validation.|
|GAP-PW-003|Promptflow/chat handover files listed as repo-accessible equivalents but not in the primary slice|Medium: may contain reusable handoff structures.|Represented through the clean handover and harmonization promptflow examples; deeper mining deferred.|
|GAP-PW-004|Failure files about blind long-document updating and promptflow drift not all read individually|Medium: anti-drift pattern is high value.|Represented through the failure ledger and existing scaffold entries; deeper source expansion deferred.|

## Material-gap disposition

- **Verdict:** no unresolved material gap blocks scaffold drafting.
- **Reason:** the indexed slice includes the primary 80/20 prompt and workflow doctrine, source-authority verification doctrine, Codex execution doctrine, and repo-local handoff/promptflow examples.
- **Constraint:** deferred sources remain candidate-only until separately validated.

## Authority-risk controls

- **Rule:** A prompt or template is not governance by itself.
- **Rule:** Failure evidence is not universal doctrine unless supported by high-confidence convergence.
- **Rule:** Broad orchestration doctrine is excluded unless it directly constrains handoff or stage gates.
- **Rule:** Candidate entries may be stored in `LEARNING_QUEUE.md`, but they do not become accepted scaffold doctrine without validation.

## Appendix pointers

- `APPENDIX_KB_INFORMATION_RANKING_LEDGER.md` — normalized information units and recommended targets.
- `APPENDIX_KB_CANDIDATE_LEDGER.md` — candidate capture and promotion status.
- `APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md` — reusable failure evidence and safeguards.
- `SOURCE_CONFLICT_REPORT.md` — bounded conflict handling for patch/rewrite and doctrine/template boundaries.
