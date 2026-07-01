---
class: trace
role: AUDIT
surface: agent_kb_appendix
quality: source_scoped
scope: agent
purpose: rank verified constant-failure research into Prompts Workflows scaffold, appendices, and future-research targets
dependencies: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/ConstantAIFailureAnalysis.md | ESSENCE.md | BEST_PRACTICES.md | MISTAKES.md | TEMPLATES.md | LEARNING_QUEUE.md
status: proposed_integration_ranking
source_file_count_verified: 1
generated_at: 2026-05-06
owner: special_ops__prompts_workflows
validator: meta_ops
---

# APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_RANKING

## Integrity note

This appendix is intentionally source-scoped.

Verified source folder:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/
```

Verified source file:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/ConstantAIFailureAnalysis.md
```

No other file in `NewResearchBecauseOfConstantFailure/` has been verified for this pass.

Do not import adjacent failure files from other folders unless an operator explicitly adds them to the source set.

## Purpose

Rank the ideas, flows, process changes, and possible file targets from `ConstantAIFailureAnalysis.md` into:

1. scaffold candidates,
2. appendix / evidence candidates,
3. future-research or new-appendix candidates.

This appendix creates the integration process. It does not by itself promote entries into accepted scaffold truth.

## Current KB baseline

The existing Prompts Workflows scaffold already contains strong general anti-drift doctrine:

- `ESSENCE.md` already requires target/source/output/stop locks, bounded execution, stage gates, authority-before-action, verification-before-trust, and out-of-mode capture.
- `BEST_PRACTICES.md` already accepts source/target freezing, bounded stage-gated execution, verification gates, clean handoffs, and durable QA appendices.
- `MISTAKES.md` already covers whole-document rewrite drift, source-summary overtrust, overloaded prompts, fluent-but-unverified completion, hidden governance, out-of-mode improvements, artifact/intent mismatch, and artifact-existence completion.
- `TEMPLATES.md` already includes one-file live edit contracts, research preflight, bounded repo execution preflight, promptflow stage gates, clean handoff, intent/artifact contract check, edit-mode chooser, and improvement capture.
- `LEARNING_QUEUE.md` already provides the candidate-only route and forbids self-promotion.

Therefore the new source should not trigger a broad rebuild. Its main value is a targeted patch plan for browser-based ChatGPT project execution, inline output discipline, and the named failure pattern of scope expansion disguised as compliance.

## Source extraction classes

| Class | Meaning | Promotion policy |
|---|---|---|
| `repo_observed_failure` | Failure pattern directly useful to this repo's promptflow work. | eligible for `MISTAKES.md`, `BEST_PRACTICES.md`, or `TEMPLATES.md` after meta_ops validation |
| `browser_operating_model` | Practical workflow for ChatGPT Business/Plus in a browser. | eligible for scaffold if phrased as local operating discipline, not platform fact |
| `output_contract` | File/content output formatting rule that reduces copy/paste and artifact ambiguity. | eligible for `TEMPLATES.md` and compact `BEST_PRACTICES.md` entry |
| `external_model_claim` | Claim about model downgrades, token limits, GPT-5.5 variants, API limits, or external tooling. | future research only until independently verified |
| `tooling_alternative` | API/direct-repo/external compute recommendations. | future appendix or cross-agent research; not accepted scaffold doctrine for browser workflow |

## Ranking model

| Axis | Meaning | Score range |
|---|---|---:|
| `SRC` | Direct support from `ConstantAIFailureAnalysis.md` | 1-5 |
| `FIT` | Fit for `special_ops__prompts_workflows` ownership | 1-5 |
| `NOV` | New value beyond current scaffold | 1-5 |
| `EXE` | Can be expressed as executable prompt/output contract | 1-5 |
| `RSK` | Drift risk if not integrated | 1-5 |
| `VAL` | Validation burden before scaffold promotion; 5 = low burden, 1 = high burden | 1-5 |

Routing rule:

```yaml
routing_rule:
  scaffold_candidate: total >= 25 and FIT >= 4 and EXE >= 4 and VAL >= 4
  appendix_candidate: total >= 22 and detail/evidence is too large for scaffold
  learning_queue_candidate: total >= 18 and VAL <= 3
  future_research: external claims, tooling claims, or total < 18
```

## Ranked integration candidates

| Rank | ID | Candidate | Class | SRC | FIT | NOV | EXE | RSK | VAL | Total | Target | Decision |
|---:|---|---|---|---:|---:|---:|---:|---:|---:|---:|---|---|
| 1 | `CF-SRC1-001` | Scope expansion disguised as compliance: a bounded file/output task is converted into broader governance/planning work and produces an adjacent-but-wrong artifact. | `repo_observed_failure` | 5 | 5 | 5 | 4 | 5 | 5 | 29 | `MISTAKES.md` + evidence appendix | scaffold_candidate |
| 2 | `CF-SRC1-002` | Process packs must be execution constraints, not design inspiration; gates must be checkable before output. | `repo_observed_failure` | 5 | 5 | 4 | 5 | 5 | 5 | 29 | `BEST_PRACTICES.md`, `TEMPLATES.md` | scaffold_candidate |
| 3 | `CF-SRC1-003` | Browser file-output ambiguity requires an explicit inline-output contract: complete file content, one code block, no prose outside, first line identifies file. | `output_contract` | 5 | 5 | 5 | 5 | 5 | 5 | 30 | `TEMPLATES.md`, `BEST_PRACTICES.md` | scaffold_candidate |
| 4 | `CF-SRC1-004` | One chat equals one atomic execution unit for browser business work; archive/stop after the task instead of continuing into a new task. | `browser_operating_model` | 5 | 5 | 4 | 4 | 5 | 4 | 27 | `BEST_PRACTICES.md`, `TEMPLATES.md` | scaffold_candidate |
| 5 | `CF-SRC1-005` | Use a Project-level execution gate for browser work: constraints first, task second, forbidden actions explicit. | `browser_operating_model` | 5 | 5 | 4 | 5 | 5 | 4 | 28 | `TEMPLATES.md`, `BEST_PRACTICES.md` | scaffold_candidate |
| 6 | `CF-SRC1-006` | Negative-space prompting: explicitly declare what must not happen, such as no summarization, no restructuring, no extra artifacts, no rewrite. | `output_contract` | 5 | 5 | 3 | 5 | 4 | 5 | 27 | `BEST_PRACTICES.md`, `TEMPLATES.md` | scaffold_candidate |
| 7 | `CF-SRC1-007` | Constraint reseeding / context anchors for long browser sessions. | `browser_operating_model` | 4 | 5 | 3 | 4 | 4 | 3 | 23 | `LEARNING_QUEUE.md`, appendix | appendix_candidate |
| 8 | `CF-SRC1-008` | STATE.md / task-state artifact for browser subscription workflow: current task, completed files, active constraints, forbidden actions. | `browser_operating_model` | 4 | 4 | 3 | 4 | 4 | 3 | 22 | appendix, `LEARNING_QUEUE.md` | appendix_candidate |
| 9 | `CF-SRC1-009` | Literal output examples should be included in high-risk browser prompts to reduce format drift. | `output_contract` | 4 | 5 | 3 | 5 | 4 | 5 | 26 | `TEMPLATES.md` | scaffold_candidate |
| 10 | `CF-SRC1-010` | Browser Projects should be used instead of raw chats for reusable business/workstream contexts. | `browser_operating_model` | 4 | 4 | 3 | 3 | 4 | 3 | 21 | `LEARNING_QUEUE.md`, possible appendix | learning_queue_candidate |
| 11 | `CF-SRC1-011` | Claims about model auto-routing/downgrades, GPT-5.5 variants, and token limits. | `external_model_claim` | 3 | 2 | 2 | 1 | 3 | 1 | 12 | future research | future_research |
| 12 | `CF-SRC1-012` | Claims about API/direct-repo/external compute tools as architectural fixes. | `tooling_alternative` | 3 | 2 | 2 | 2 | 3 | 1 | 13 | future research or cross-agent tooling appendix | future_research |

## Scaffold integration recommendations

### `ESSENCE.md`

Do not add long platform or model claims.

Optional compact doctrine after validation:

```markdown
- **Execution over diligence:** a promptflow fails if it expands a bounded output task into planning, governance, or adjacent artifact creation.
- **Browser output contracts:** browser-based file work requires explicit inline artifact contracts because "create a file" can be interpreted as prose or prompt text.
```

### `BEST_PRACTICES.md`

Recommended compact accepted-practice candidates:

| Candidate | Practice |
|---|---|
| `CF-SRC1-002` | Convert process-pack rules into pre-output gates, not prose advice. |
| `CF-SRC1-003` | For browser-based file creation, specify exact inline file-output format before generation. |
| `CF-SRC1-004` | Use one browser chat per atomic execution unit when producing repo-relevant artifacts. |
| `CF-SRC1-005` | Put constraints/forbidden actions before task context in Project or chat-level execution prompts. |
| `CF-SRC1-006` | Use negative-space constraints for high-risk drift tasks. |

### `MISTAKES.md`

Recommended compact failure-pattern candidates:

| Candidate | Pattern |
|---|---|
| `CF-SRC1-001` | Scope expansion disguised as compliance. |
| `CF-SRC1-003` | File-output ambiguity: model outputs a prompt/header/about-text instead of the file body. |
| `CF-SRC1-004` | Continuing long browser chats across execution units until context drift outranks the original contract. |

### `TEMPLATES.md`

Recommended template candidates:

1. `PW-TPL-BROWSER-PROJECT-GATE`
2. `PW-TPL-INLINE-FILE-OUTPUT-CONTRACT`
3. `PW-TPL-BROWSER-ATOMIC-TASK-SESSION`
4. `PW-TPL-NEGATIVE-SPACE-CONSTRAINT-BLOCK`
5. `PW-TPL-STATE-ANCHOR-FOR-BROWSER-WORK`

Minimum template: `PW-TPL-INLINE-FILE-OUTPUT-CONTRACT`

```markdown
# Inline File Output Contract

## Target

`<REPO_RELATIVE_FILE_PATH>`

## Output rule

Return exactly one Markdown code block containing the complete file body.

No explanation before the code block.
No explanation after the code block.
Do not output a prompt about the file.
Do not output a summary of the file.
Do not add extra artifacts.

## File sentinel

The first line inside the code block must be:

`# FILE: <REPO_RELATIVE_FILE_PATH>`

## Scope

Only produce the requested file body.
Do not redesign neighboring files, appendices, schemas, or workflow architecture.

## Completion check

After drafting internally, verify:

- target path matches the requested path
- one code block only
- complete file body present
- no prose outside the code block
- no unrelated additions
```

Minimum template: `PW-TPL-BROWSER-PROJECT-GATE`

```markdown
# Browser Project Execution Gate

```yaml
execution_gate:
  surface: ChatGPT browser Project
  workstream: <PROJECT_OR_REPO_NAME>
  atomic_task: <ONE_TASK_ONLY>
  target_artifact: <ONE_FILE_OR_ONE_REPORT>
  output_format: <complete_file_code_block | table | report | patch_text>
  forbidden:
    - scope expansion
    - extra planning artifact
    - adjacent governance rewrite
    - new taxonomy
    - hidden cleanup
    - multiple deliverables
  stop_conditions:
    - target path unclear
    - source authority unclear
    - output format cannot be satisfied
    - task requires repo write but browser-only output is requested
```

Write constraints first. Then task. Then sources. Then output.
```

### `LEARNING_QUEUE.md`

Queue these without accepting as truth:

| Candidate | Reason |
|---|---|
| `CF-SRC1-007` | Constraint reseeding is plausible but needs a crisp threshold and examples before scaffold promotion. |
| `CF-SRC1-008` | STATE.md/task-state anchor overlaps handoff templates; validate non-duplicate value. |
| `CF-SRC1-010` | Project-vs-raw-chat advice may be valid for browser workflow but should be checked against current ChatGPT Business capabilities. |
| `CF-SRC1-011` | Model routing/downgrade/token-limit claims require independent validation. |
| `CF-SRC1-012` | API/direct-repo/external compute alternatives are outside the browser-only operating scope and need separate tooling research. |

## Appendix recommendations

### Keep in this appendix

This appendix should remain the narrow routing control for `ConstantAIFailureAnalysis.md`.

### Create follow-up appendix files only if needed

| Priority | Appendix | Purpose | Trigger |
|---:|---|---|---|
| P1 | `appendices/APPENDIX_KB_BROWSER_WORKFLOW_OPERATING_MODEL.md` | Detailed browser-based Project/chat/session/output operating model. | Create if more than two browser-specific entries are promoted into scaffold. |
| P1 | `appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_AUDIT.md` | Evidence digest and quote map from `ConstantAIFailureAnalysis.md`. | Create if meta_ops asks for detailed evidence before scaffold promotion. |
| P2 | `appendices/APPENDIX_KB_MODEL_ROUTING_CONTEXT_RESEARCH.md` | Validate model-routing, token-limit, and context-window claims. | Create only with current verified sources. |
| P2 | `appendices/APPENDIX_KB_TOOLING_ALTERNATIVES_RESEARCH.md` | Assess API/direct-repo/external compute claims. | Create only if the operating mode expands beyond browser subscription workflow. |

## Process for integrating this source

### Phase 0: source proof

```yaml
phase: source_proof
required_source:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/ConstantAIFailureAnalysis.md
forbidden_source_expansion:
  - sibling failure folders
  - historical Apex promptfailure folders
  - Codex research elsewhere
  - external websites unless explicitly validated in a later research phase
stop_if:
  - source path cannot be fetched
  - additional sources are silently introduced
```

### Phase 1: classify claims

Every extracted idea must be classified as one of:

```yaml
claim_class:
  - repo_observed_failure
  - browser_operating_model
  - output_contract
  - external_model_claim
  - tooling_alternative
```

### Phase 2: overlap check

Before scaffold promotion, compare candidate against existing accepted entries:

- `PW-BP-002` target/source/output/stop freeze
- `PW-BP-003` bounded stage-gated execution
- `PW-BP-004` verification before trust
- `PW-BP-006` clean handoff
- `PW-MK-003` overloaded prompt
- `PW-MK-004` fluent-but-unverified completion
- `PW-MK-007` user intent vs artifact mismatch
- `PW-MK-008` artifact-existence completion
- `PW-TPL-003` bounded repo execution preflight
- `PW-TPL-006` intent/artifact contract check

Promote only the non-duplicate browser/output-specific delta.

### Phase 3: scaffold patch order

If approved, patch in this order:

1. `MISTAKES.md` — add scope-expansion and file-output ambiguity patterns.
2. `TEMPLATES.md` — add browser project gate and inline file-output contract.
3. `BEST_PRACTICES.md` — add compact practices pointing to the templates.
4. `LEARNING_QUEUE.md` — queue unverified platform/model/tooling claims.
5. `ESSENCE.md` — add at most one compact activation rule if still needed after the other patches.

### Phase 4: validation

Required final report:

```yaml
repo:
branch:
source_file_verified:
files_changed:
scaffold_entries_added:
appendices_created_or_updated:
learning_queue_entries_added:
external_claims_not_promoted:
future_research_items:
fetch_back_status:
changed_file_set_check:
open_questions:
```

## Stop conditions

- Stop if the run starts using unverified neighboring files as evidence.
- Stop if a model/platform claim is promoted without current validation.
- Stop if a broad rebuild is proposed instead of a narrow delta patch.
- Stop if a candidate duplicates an existing accepted practice without new browser/output-specific value.
- Stop if scaffold edits are proposed without appendix routing and meta_ops validation.

## Status

This file is a corrected, source-scoped integration-ranking artifact for `ConstantAIFailureAnalysis.md` only.

Recommended next step: validate this appendix with `meta_ops`, then run a small scaffold patch pass for `MISTAKES.md`, `TEMPLATES.md`, `BEST_PRACTICES.md`, and `LEARNING_QUEUE.md` only if approved.
