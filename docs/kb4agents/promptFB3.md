Done — I created the audit report as a downloadable Markdown file:

[Download the Agent Mode KB Factory Audit](sandbox:/mnt/data/Agent_Mode_KB_Factory_Audit.md)

## Executive verdict

**Partial pass / revise before review.** The package exists structurally, but it should **not** be promoted as live KB truth yet.

**Main reason:** the original prompt required the agent to use the ranked source index as binding authority, follow read modes, produce exact metadata/file structures, and stop or mark affected work when required sources failed. The produced package has the expected broad inventory, but the manifest itself admits skipped primary/supporting index files and missing source access.

## Most important findings

|Area|Finding|
|---|---|
|**Structure**|The repo output lists seven agents and thirty-five agent files, plus four control artifacts.|
|**Source discipline**|Key indexed files were not accessed, including the major KB ranking / inventory / role mapping ledgers.|
|**False inaccessible claim**|`SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md` was marked inaccessible, but a current repo fetch succeeds at the correct path.|
|**Metadata failure**|The cross-agent audit claims metadata compliance, but sample files violate the required schema: `workflow_process/AGENT_CARD.md` uses `class: card` and `role: PROFILE`, and `workflow_process/ESSENCE.md` uses `class: essence` and `role: ORIENTATION`.|
|**Evidence leakage**|The Hygiene / Clean best-practices file builds positive doctrine from the process-failure evidence file while admitting it lacks primary sources.|
|**Audit verdict mismatch**|The package’s own audit says `accept_for_human_review`, but the evidence supports `revise_before_review`.|
|**Zip integrity**|**ZIP NOT AVAILABLE:** only the repo output could be audited. No original downloaded zip was attached for file-count/checksum/path comparison.|

## Copy-ready improvement file block

```md
# SPECIAL_OPS_KB_IMPROVEMENT_BACKLOG

## 1. Evident strengths

- **Structural seed:** The five-file-per-agent model is strong: `BEST_PRACTICES`, `MISTAKES_FAILURES`, `LEARNING`, `AGENT_CARD`, and `ESSENCE`.
- **Agent coverage:** The seven initial agents cover the right lanes: information design, prompt design, workflow/process, AI handling/routing, hygiene/clean, Codex/Git execution, and research/API cost.
- **Source-slice concept:** Keep `source_slice` frontmatter; it is the right traceability mechanism.
- **Provisional labeling:** Weakly sourced agents are at least marked provisional.
- **Failure awareness:** Separate mistakes/failures files are valuable for anti-drift learning.

## 2. Group-of-agents KB improvements

### 2.1 Add `SPECIAL_OPS_SWARM_CONTRACT.md`

Include:

- **Agent boundary matrix:** each agent’s ownership, non-scope, and overlap boundaries.
- **Routing table:** task signal -> target agent -> required input -> expected output -> stop condition.
- **Handoff schema:** shared required fields for all agent-to-agent transfers.
- **Conflict rule:** source conflict, role conflict, or missing primary source blocks affected doctrine.
- **Review rule:** cross-agent audit may not approve itself when source coverage is incomplete.

### 2.2 Add `GROUP_SOURCE_AUTHORITY_MATRIX.md`

Use this table:

| Source | Agent(s) | Role | Read mode | Stable path | Status | Last verified | Notes |
|---|---|---|---|---|---|---|---|

Required rules:

- Replace opaque citation markers with stable repo paths.
- Track path hazards such as `&`, spaces, and parentheses.
- Mark missing primary sources as `blocked`, not merely “provisional,” when they are load-bearing.
- Keep `evidence_only` separate from `supporting`.

### 2.3 Add `SPECIAL_OPS_KB_ACCEPTANCE_TESTS.md`

Required tests:

- **Structure test:** every agent has exactly five required files.
- **Metadata test:** every file matches required class/role/surface values.
- **Source test:** every `read full` primary source is read or blocks affected output.
- **Evidence test:** evidence-only files appear only in failures, audits, or examples unless supported elsewhere.
- **Essence test:** every `ESSENCE.md` introduces no new rule, source, or scope.
- **Citation test:** every claim traces to a stable path or is marked provisional.
- **Self-audit test:** `CROSS_AGENT_AUDIT.md` cannot claim compliance when sample files violate schema.

## 3. Individual agent KB improvements

### Information Design Agent

- Add richer chunking, labeling, and source-slice examples.
- Add formal glossary integration rules.
- Add before/after examples of good and bad KB chunks.

### Prompt Design Agent

- Add destructive-rewrite prevention templates.
- Add prompt factories for audit, extraction, patch generation, repo-grounded synthesis, and verification.
- Add exact output-contract templates.

### Workflow / Process Agent

- Define decomposition triggers: deliverable count, token budget, file count, source count, ambiguity count.
- Add continuation vs migration criteria.
- Add stop/escalate decision tree.

### AI Handling / Routing Agent

- Rebuild using `SOURCE_AUTHORITY_VERIFICATION_ESCALATION_80_20_ESSENCE.md`.
- Add routing by risk level: low, medium, high, blocked.
- Add keep-local vs delegate thresholds.
- Add multi-agent overlap prevention rules.

### Hygiene / Clean Agent

- Do not base positive hygiene doctrine only on process-failure anecdotes.
- Locate or regenerate a real hygiene/anti-drift ledger.
- Add severity classes, closure rules, and artifact integrity checks.
- Add strict “cleaning is not rewriting” boundaries.

### Codex Git Execution Agent

- Add `git apply --check` and live-file preimage verification rules.
- Add patch-state taxonomy: `drafted`, `syntax-valid`, `target-checked`, `apply-checked`, `applied`, `rejected`.
- Add path quoting and special-character handling rules.
- Add one-file-at-a-time and no-global-rewrite guardrails.

### Research / API Cost Agent

- Split stable method from volatile data:
  - stable: model-selection framework, cost formula, fallback logic
  - volatile: model names, prices, context windows, rate limits
- Add freshness metadata and review cadence.
- Add “no stale pricing doctrine” rule.

## 4. Further research opportunities

- **Empirical agent tests:** Run each agent on 3-5 standardized tasks and score drift, completeness, source use, and verification.
- **Source coverage audit:** Compare every indexed source with actual source usage.
- **Artifact integrity study:** Compare generated folder, zip, repo folder, and extracted folder with checksums.
- **Citation reliability study:** Test whether generated citations survive outside the original ChatGPT environment.
- **Routing experiment:** Test whether the routing agent assigns ambiguous tasks without overlap.
- **Cost-refresh protocol:** Define refresh cadence for model/API pricing data.
- **Weak-agent resilience test:** Give the KB to a weak agent and measure whether it follows the intended process.

## 5. Risks to control before promotion

- **False acceptance risk:** Complete-looking package hides unread primary sources.
- **Self-certification risk:** The package audit approves files it did not inspect rigorously.
- **Evidence-to-doctrine risk:** Failure anecdotes become operating law without support.
- **Citation rot risk:** Opaque line markers become unusable outside the original session.
- **Path-handling risk:** Files with `&`, spaces, or parentheses are falsely marked inaccessible.
- **Provisional hardening risk:** Draft/provisional KB files later get treated as accepted truth.
- **Role-overlap risk:** Prompt, workflow, routing, and hygiene agents duplicate or contradict one another.
- **Stale market-data risk:** Model/cost recommendations become outdated quickly.
- **Token-compression risk:** Long source sets cause agents to skip sources while producing polished output.
- **Artifact-nesting risk:** Double folder nesting confuses future automation and zip/package comparison.
```