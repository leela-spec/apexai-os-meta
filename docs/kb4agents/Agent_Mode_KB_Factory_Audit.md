# Agent Mode KB Factory Audit

## Executive Verdict

**Verdict: partial pass / revise before review.**

The repo output is structurally present as a first draft: the package contains the four control artifacts and seven agent folders with five files each. However, the run does not satisfy the source-discipline, metadata, and audit-reliability standards required by the controlling prompt. The most serious issues are skipped primary sources, a falsely or prematurely marked inaccessible source, metadata schema violations, evidence-only material leaking into doctrine, opaque non-path citations, and an internal cross-agent audit that overstates compliance.

## Instruction vs Output

### What the prompt required

- Read `SPECIAL_OPS_KB_BASE_BUILD_INDEX.md` first and treat it as the binding source map.
- Use only indexed repo files and explicitly named manually attached files.
- Follow each indexed file's `read full`, `skim`, or `use as evidence only` instruction.
- Create the package layout with four control artifacts and per-agent folders.
- For each agent, create exactly five files: `BEST_PRACTICES.md`, `MISTAKES_FAILURES.md`, `LEARNING.md`, `AGENT_CARD.md`, `ESSENCE.md`.
- Preserve claim status and source/status boundaries.
- Stop affected work if primary source access fails or output would require guessing from silence.

### What the output contains

- **Present:** Four control artifacts: `SOURCE_USE_MANIFEST.md`, `SPECIAL_OPS_AGENT_REGISTRY.md`, `KB_PRODUCTION_MANIFEST.md`, and `CROSS_AGENT_AUDIT.md`.
- **Present:** Seven agent folders: `information_design`, `prompt_design`, `workflow_process`, `ai_handling_routing`, `hygiene_clean`, `codex_git_execution`, and `research_api_cost`.
- **Present:** Thirty-five per-agent files listed in the production manifest.
- **Problem:** The output is stored under a double-nested repo path: `docs/kb4agents/special_ops_kb_factory_output/special_ops_kb_factory_output/`.
- **Problem:** The package claims `accept_for_human_review`, but the audit evidence supports `revise_before_review`.

## Source Discipline Findings

1. **Primary source skipping:** The source manifest admits that important indexed files such as `KB_RANKINGS_BY_AGENT.md`, `SOURCE_INVENTORY_LEDGER.md`, `MASTER_IDEA_LEDGER.md`, and `ROLE_AND_KB_TARGET_MAP.md` were not accessed. These were not optional navigation files; the index listed them as primary/supporting sources.

2. **False or premature inaccessible-source claim:** The output manifest says `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md` was inaccessible. A current repo fetch succeeds at `AIHowTo/BasicFiles4Agents/Validation&Authority/SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md`. The previous agent likely mishandled the ampersand path or failed to recover from a connector/path encoding issue.

3. **Evidence-only leakage into doctrine:** The Hygiene / Clean `BEST_PRACTICES.md` file is built from `prob - prompt design & process failure.md` and states that guidelines are inferred from general failure patterns. That violates the source contract when an evidence file is supposed to support failure evidence rather than become positive doctrine.

4. **Stop-condition weakness:** The prompt said missing primary sources should stop affected work or mark it blocked/provisional. The output continues to produce full Hygiene / Clean and AI Handling / Routing doctrine while only marking them provisional. That may be acceptable for a draft seed, but not for an `accept_for_human_review` verdict.

5. **Opaque citation pollution:** Many KB files contain citation markers like `【173985281715767†L79-L120】` rather than stable repo paths or source slices. These markers are not useful in a durable repo KB unless the citation system that generated them remains available.

## Thinking Transcript Findings

The transcript shows a mixed process:

- The agent did read the controlling prompt and the index at the start.
- The agent then tried to fetch indexed repo files and encountered source-access friction.
- The transcript shows path-search behavior around `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md`, but the final manifest treated the file as inaccessible rather than resolving the path correctly.
- The transcript contains procedural confusion, including a mid-task statement that it was awaiting further instructions despite having a clear production contract.
- The transcript shows large `apply_patch` operations generating many files in broad batches, which is risky for the requested source-grounded KB package.
- The run contains signs of token-pressure compression and ad hoc manufacturing: skipped sources, later self-audit claims not fully aligned with produced metadata, and broad doctrine creation from thin source slices.

## Artifact / Zip Integrity

**ZIP NOT AVAILABLE: only repo output can be audited.**

No original downloaded zip was attached in this chat, so I could not extract and compare zip contents against the repo folder. The repo folder itself appears to preserve the package files, but the double nesting suggests artifact-path hygiene risk. A full zip integrity audit still requires the original downloaded zip.

## Structural Completeness

### Passes

- Seven agent folders are represented.
- The production manifest lists thirty-five agent files.
- Control artifacts are present.
- File naming is largely consistent.

### Fails / gaps

- `AGENT_CARD.md` metadata does not consistently match the specified schema. Example: `workflow_process/AGENT_CARD.md` uses `class: card` and `role: PROFILE` instead of the required `class: frame` and `role: ORCHESTRATION`.
- `ESSENCE.md` metadata does not consistently match the specified schema. Example: `workflow_process/ESSENCE.md` uses `class: essence` and `role: ORIENTATION` instead of `class: frame` and `role: INSTRUCTION_BLOCK`.
- Some required section labels are not followed exactly. Example: the required `AGENT_CARD.md` handoff table fields differ from the output table.
- The cross-agent audit claims metadata compliance, but sample files disprove that claim.

## Content Quality Risks

- **False completeness:** The output looks complete because all files exist, but source coverage is incomplete.
- **Self-audit overreach:** The final `CROSS_AGENT_AUDIT.md` asserts that no unsupported doctrine appears, which is too strong given the skipped sources and evidence-only leakage.
- **Provisional hardening:** Provisional agents are fully authored and may be mistaken later for accepted doctrine.
- **Citation fragility:** Non-path citations are not durable repo references.
- **Role overlap risk:** Workflow, Prompt Design, AI Handling, and Hygiene share overlapping concepts without a strong cross-agent boundary matrix.
- **Cost/research staleness:** The Research / API Cost agent depends on dated model and pricing data and should separate durable decision method from volatile market facts.

## Final Recommendation

Do not promote this KB package as live operational truth. Treat it as a useful first-draft scaffold. Run a targeted revision pass before human review:

1. Rebuild the source manifest from exact accessible paths.
2. Read the skipped primary files or explicitly block affected claims.
3. Rebuild AI Handling / Routing using the now-accessible source-authority file.
4. Rebuild Hygiene / Clean from real hygiene sources, or mark it blocked.
5. Normalize all metadata and file-section schemas.
6. Replace opaque citation markers with stable repo paths and source slices.
7. Change the cross-agent audit verdict to `revise_before_review` until the above are complete.

---

# Copy-Ready Improvement Block

```md
# SPECIAL_OPS_KB_IMPROVEMENT_BACKLOG

## 1. Evident strengths

- **Structural seed:** The five-file-per-agent model is strong: `BEST_PRACTICES`, `MISTAKES_FAILURES`, `LEARNING`, `AGENT_CARD`, and `ESSENCE` create a useful doctrine stack.
- **Agent coverage:** The first seven agents cover the right operational lanes: information design, prompt design, workflow/process, AI handling/routing, hygiene/clean, Codex/Git execution, and research/API cost.
- **Source-slice idea:** The frontmatter `source_slice` concept is valuable and should be kept.
- **Provisional labeling:** The package at least recognizes that weakly sourced agents are provisional, even if the final audit verdict overstates readiness.
- **Failure awareness:** Mistakes/failures files are the right mechanism for capturing known drift and destructive-edit patterns.

## 2. Group-of-agents KB improvements

### 2.1 Add a cross-agent swarm contract

Create `SPECIAL_OPS_SWARM_CONTRACT.md` with:

- **Agent boundary matrix:** what each agent owns, what it must not own, and where overlap requires handoff.
- **Routing table:** user/task signal -> agent -> required input -> expected output -> stop condition.
- **Handoff schema:** shared fields for all agent-to-agent transfers.
- **Authority rule:** no agent may convert draft KB into accepted truth without promotion.
- **Conflict rule:** source conflict, role conflict, or missing primary source blocks affected doctrine.
- **Review rule:** cross-agent audit may not approve itself when source coverage is incomplete.

### 2.2 Add a group source-authority matrix

Create `GROUP_SOURCE_AUTHORITY_MATRIX.md` with:

| Source | Agent(s) | Role | Read mode | Stable path | Status | Last verified | Notes |
|---|---|---|---|---|---|---|---|

Required improvements:

- Replace all opaque citation markers with stable repo paths and exact source slices.
- Track path-encoding hazards such as `&`, spaces, and parentheses.
- Mark missing sources as `blocked`, not merely `provisional`, when they are primary for the agent.
- Separate `evidence_only` from `supporting` in every output file.

### 2.3 Add cross-agent acceptance tests

Create `SPECIAL_OPS_KB_ACCEPTANCE_TESTS.md` with checklist tests:

- **Structure test:** every agent has exactly five required files.
- **Metadata test:** every file matches required class/role/surface values.
- **Source test:** every `read full` primary source is either read or blocks affected output.
- **Evidence test:** evidence-only files appear only in failures, audits, or examples unless supported elsewhere.
- **Essence test:** every `ESSENCE.md` introduces no new rule, source, or scope.
- **Citation test:** every claim can be traced to a stable path or declared provisional.
- **Self-audit test:** `CROSS_AGENT_AUDIT.md` cannot claim compliance when sample files violate schema.

### 2.4 Add a shared glossary and taxonomy spine

Create `SPECIAL_OPS_SHARED_GLOSSARY.md` with stable definitions for:

- source authority
- evidence-only
- provisional
- blocked
- doctrine
- failure evidence
- handoff
- promotion
- agent card
- essence
- bounded execution
- hygiene finding
- verification gate

## 3. Individual agent KB improvements

### 3.1 Information Design Agent

- Add richer examples for chunking, labels, source slices, and taxonomy.
- Add an anti-sprawl rule for when to split a new KB file versus extend an existing file.
- Add a formal glossary integration rule.
- Add before/after examples of good and bad KB chunks.

### 3.2 Prompt Design Agent

- Add a destructive-rewrite prevention pattern.
- Add prompt templates for: audit, extraction, patch generation, repo-grounded synthesis, and verification.
- Add explicit output-contract templates with required headings and tables.
- Add failure-mode examples from the process-failure transcript without turning evidence-only anecdotes into doctrine.

### 3.3 Workflow / Process Agent

- Define quantitative decomposition triggers: number of deliverables, token budget, file count, source count, ambiguity count.
- Add continuation vs migration criteria.
- Add batch-audit cadence rules.
- Add a stop/escalate decision tree.

### 3.4 AI Handling / Routing Agent

- Rebuild from the accessible `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md`.
- Add routing by task risk: low, medium, high, blocked.
- Add "keep local vs delegate" thresholds.
- Add multi-agent overlap prevention rules.
- Add escalation states: `needs_input`, `hold`, `blocked`, `revise`, `ready_for_review`.

### 3.5 Hygiene / Clean Agent

- Do not base positive hygiene doctrine only on process-failure anecdotes.
- Locate or regenerate a real hygiene/anti-drift ledger.
- Add hygiene severity classes and closure rules.
- Add artifact integrity checks: file count, path nesting, encoding, truncation, duplicate folders, broken links.
- Add a strict "cleaning is not rewriting" boundary.

### 3.6 Codex Git Execution Agent

- Add `git apply --check` and live-file preimage verification rules.
- Add patch-state taxonomy: `drafted`, `syntax-valid`, `target-checked`, `apply-checked`, `applied`, `rejected`.
- Add path quoting and special-character handling rules.
- Add one-file-at-a-time and no-global-rewrite guardrails.
- Add rollback and validation-record requirements.

### 3.7 Research / API Cost Agent

- Split stable method from volatile data:
  - stable: model-selection framework, cost calculation formula, fallback logic
  - volatile: model names, prices, context windows, rate limits
- Add freshness metadata and review cadence.
- Add "no stale pricing doctrine" rule.
- Add source-date fields for every pricing/model claim.

## 4. Further research opportunities

- **Empirical agent tests:** Run each agent on 3-5 standardized tasks and score drift, completeness, source use, and verification quality.
- **Source coverage audit:** Compare every indexed source with actual source usage and quantify skipped primary coverage.
- **Artifact integrity study:** Compare generated folder, zip, repo folder, and extracted folder using checksums.
- **Citation reliability study:** Test whether generated citations survive outside the original ChatGPT environment.
- **Routing experiment:** Test whether the routing agent correctly assigns ambiguous tasks without creating overlap.
- **Cost-refresh protocol:** Define how often API/model cost files must be refreshed and who may update them.
- **Weak-agent resilience test:** Give the KB to a weak agent and measure whether it follows the intended process without hidden inference.

## 5. Risks to control before promotion

- **False acceptance risk:** A complete-looking package may hide unread primary sources.
- **Self-certification risk:** The package audit may approve files it did not actually inspect rigorously.
- **Evidence-to-doctrine risk:** Failure anecdotes may become positive operating law without support.
- **Citation rot risk:** Opaque line markers may become unusable outside the original agent session.
- **Path-handling risk:** Files with `&`, spaces, or parentheses may be falsely marked inaccessible.
- **Provisional hardening risk:** Draft/provisional KB files may later be treated as accepted truth.
- **Role-overlap risk:** Prompt, workflow, routing, and hygiene agents may duplicate or contradict one another without a swarm contract.
- **Stale market-data risk:** Model/cost recommendations may become outdated quickly.
- **Token compression risk:** Long source sets can lead agents to skip sources while still producing polished output.
- **Artifact nesting risk:** Double folder nesting can confuse future automation and zip/package comparisons.
```
