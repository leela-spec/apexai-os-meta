---
class: trace
role: INTEGRATION_RANKING
surface: agent_kb_appendix
quality: proposed
scope: agent
purpose: rank new constant-failure prompt/workflow research for scaffold integration, appendix retention, and future research routing
dependencies: PROMPTFLOW_KB_BASE_BUILD.md | LEARNING_QUEUE.md | NewResearchBecauseOfConstantFailure/*
status: created
created_at: 2026-05-06
owner: special_ops__prompts_workflows
validator: meta_ops
---

# APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS

## Purpose

This appendix turns the `NewResearchBecauseOfConstantFailure/` source pack into a governed integration process for `special_ops__prompts_workflows`.

It answers three routing questions:

1. Which ideas, flows, processes, and files should be promoted into the compact F5 scaffold?
2. Which material should stay in appendices because it is detailed, evidentiary, operational, or source-specific?
3. Which material should be marked as future research or split into new appendix files before promotion?

## Scope lock

- **Working repo:** `leela-spec/MasterOfArts`
- **Target KB root:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/`
- **New source root:** `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/NewResearchBecauseOfConstantFailure/`
- **F5 scaffold:** `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, `TEMPLATES.md`, `LEARNING_QUEUE.md`
- **Default architecture:** thin scaffold, deep appendices
- **Execution mode:** ranking and process artifact only; no direct scaffold mutation in this pass

## Non-promotion warning

The new source pack contains strong operational material, but some claims in `ConstantAIFailureAnalysis.md` depend on external references and model/platform behavior. Those claims must not be promoted as accepted truth until separately verified.

Treat external model-behavior claims as research leads. Promote only source-local, reusable execution controls that remain valid without relying on unverified external claims.

## Integration decision model

Score each information unit from 1 to 5:

| Score | Meaning |
|---|---|
| `EVD` | Evidence/directness inside the repo source pack |
| `IMP` | Impact on recurring prompt/workflow failure prevention |
| `ACT` | Actionability as a reusable process, rule, or template |
| `REUSE` | Likelihood of reuse across prompt/workflow tasks |
| `FIT` | Fit to `special_ops__prompts_workflows` rather than another agent lane |
| `RSK` | Drift risk if promoted too broadly |

Routing rule:

```yaml
routing_rule:
  scaffold:
    use_when: EVD >= 4 and IMP >= 4 and ACT >= 4 and FIT >= 4 and RSK <= 3
    content_shape: compact behavioral rule, failure pattern, or reusable template
  appendix:
    use_when: EVD >= 3 and IMP >= 3 and detailed evidence or operational protocol is too dense for scaffold
    content_shape: source notes, examples, protocol catalog, ranking ledger, comparison table
  future_research:
    use_when: external verification, runtime implementation, cross-agent ownership, or schema validation is required
    content_shape: research question, validation plan, candidate appendix, or cross-lane handoff
```

## Ranked idea and process integration table

| Rank | Information unit | Primary source(s) | EVD | IMP | ACT | REUSE | FIT | RSK | Recommended route | Target / next action |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|---|
| 1 | **Atomic execution contract:** one task per call, no scope expansion, no implicit state inference, machine-readable output. | `00_SYSTEM_BOOTSTRAP.md`, `00_PROJECT_BOOTSTRAP.md` | 5 | 5 | 5 | 5 | 5 | 2 | scaffold + appendix | Add compact `BEST_PRACTICES.md` rule; deep protocol in `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`. |
| 2 | **State is explicit, not reconstructed from chat history.** Use `STATE_BLOCK` as the only continuity surface. | `02_STATE_BLOCK.md`, `04_STATE_BLOCK.md` | 5 | 5 | 5 | 5 | 5 | 2 | scaffold + template | Add `MISTAKES.md` failure for implicit history reconstruction; add `TEMPLATES.md` state-block template. |
| 3 | **Task payload must be atomic and reject compound scope.** Scope is one sentence; `AND/THEN` tasks split before execution. | `03_TASK_PAYLOAD.md` | 5 | 5 | 5 | 5 | 5 | 2 | scaffold + template | Add compact `BEST_PRACTICES.md` rule and `TEMPLATES.md` payload template. |
| 4 | **Gate check before execution.** A separate gate call verifies understood task type, scope, constraints, target, ambiguity, and readiness. | `08_GATE_CHECK.md` | 5 | 5 | 5 | 5 | 5 | 3 | scaffold + appendix | Add `TEMPLATES.md` preflight template; deep server rules stay appendix-level. |
| 5 | **HALT/CLARIFY beats guessing.** Ambiguity, stale state, patch failure, or constraint violation emits a control signal and stops downstream execution. | `09_CONTROL_SIGNALS.md` | 5 | 5 | 5 | 5 | 5 | 2 | scaffold + template | Add `MISTAKES.md` counterpattern and `TEMPLATES.md` control-signal template. |
| 6 | **Validated file output protocol.** File writes require scope confirmation, complete content field, line count, `scope_respected=true`, and validation before write. | `05_FILE_OUTPUT.md` | 5 | 5 | 5 | 4 | 5 | 3 | scaffold + appendix | Add `TEMPLATES.md` file-write schema; keep server write sequence in appendix. |
| 7 | **Task closure is a proof object.** Every completed artifact ends with scope status, output type, file name, and next suggested task. | `08_TASK_CLOSURE.md` | 5 | 4 | 5 | 5 | 5 | 2 | scaffold + template | Add compact task-closure template and completion-proof mistake cross-reference. |
| 8 | **Split protocol for output ceiling risk.** Large files must declare `SPLIT_REQUIRED` and continue at logical boundaries without summary substitution. | `05_SPLIT_SIGNAL.md`, `02_MULTI_FILE_SESSION.md` | 5 | 4 | 5 | 4 | 5 | 3 | scaffold + appendix | Add `TEMPLATES.md` split/multi-file session template; examples appendix should regression-test it. |
| 9 | **Patch transport must be chosen deliberately.** SEARCH/REPLACE blocks, unified diffs, and full-body replacement have different failure profiles. | `GPT_PATCH_WORKFLOW.md`, `06_DIFF_OUTPUT (1).md`, `SOURCE_CONFLICT_REPORT.md` | 4 | 5 | 5 | 5 | 5 | 3 | scaffold + appendix | Add/merge edit-mode chooser in `TEMPLATES.md`; create `APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`. |
| 10 | **No history-injection API mode.** System bootstrap stays clean; state and task payload are passed in user message; each call is stateless. | `01_API_CALL_STRUCTURE.md` | 5 | 5 | 4 | 4 | 4 | 4 | appendix + future | Keep as execution-control appendix; route runtime implementation to AI Handling/Routing and server architecture. |
| 11 | **Research output is schema-bound.** Recommendations, format, depth, sources, and split behavior are explicit. | `07_RESEARCH_OUTPUT.md`, `07_RESEARCH_BLOCK.md` | 5 | 4 | 4 | 4 | 5 | 3 | template + appendix | Add research-block template only if non-duplicate with existing templates. |
| 12 | **Project opener / project bootstrap for constrained sessions.** New sessions must declare project, session, task, output type, constraints, and state ref. | `03_PROJECT_OPENER.md`, `00_PROJECT_BOOTSTRAP.md` | 4 | 4 | 4 | 4 | 5 | 3 | appendix + examples | Use in `APPENDIX_KB_EXAMPLES.md`; promote only compact opener skeleton if needed. |
| 13 | **Generated template catalog.** `promptworkflowsAPI.py` encodes a reusable set of runtime templates and generated files. | `promptworkflowsAPI.py` | 4 | 4 | 3 | 4 | 4 | 4 | future appendix | Create `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`; validate against hand-authored templates before scaffold use. |
| 14 | **Model pinning, temperature zero, stream false, response_format JSON.** | `00_SYSTEM_BOOTSTRAP.md`, `01_API_CALL_STRUCTURE.md` | 4 | 4 | 4 | 4 | 3 | 5 | future research / adjacent lane | Route to `special_ops__ai_handling_routing`; do not harden in this lane as global runtime law. |
| 15 | **Claims about GPT-5.5 auto-switching, downgrades, RLHF drift, and output-token caps.** | `ConstantAIFailureAnalysis.md` | 2 | 4 | 2 | 3 | 3 | 5 | future research only | Create `APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md` before any doctrine promotion. |

## File-level ranking and disposition

| Rank | Source file | Function | Disposition | Reason |
|---:|---|---|---|---|
| 1 | `00_SYSTEM_BOOTSTRAP.md` | Runtime execution contract and authority hierarchy | **split: scaffold summary + execution-control appendix** | Highest-density source for no-scope-expansion, model/task control, machine output, authority hierarchy, and gate protocol. |
| 2 | `03_TASK_PAYLOAD.md` | Atomic task instruction schema | **scaffold + template** | Directly corrects compound-task drift and directory-scan overreach. |
| 3 | `08_GATE_CHECK.md` | Pre-execution gate schema | **template + appendix** | Converts vague preflight into a parseable control surface. |
| 4 | `02_STATE_BLOCK.md` | Explicit state replacement for chat history | **scaffold + template** | Directly addresses continuity hallucination and stale-state execution. |
| 5 | `09_CONTROL_SIGNALS.md` | HALT/CLARIFY signal contract | **scaffold + template** | Strongest stop-discipline artifact in the new pack. |
| 6 | `05_FILE_OUTPUT.md` | Validated file-write schema | **template + appendix** | Useful for repo-writing flows; too operational for scaffold except compact principle. |
| 7 | `GPT_PATCH_WORKFLOW.md` | Local search/replace patch application protocol | **appendix + template chooser** | Important but transport-specific; should not override all edit modes. |
| 8 | `08_TASK_CLOSURE.md` | Completion proof block | **template** | Lightweight, reusable, and low-drift. |
| 9 | `05_SPLIT_SIGNAL.md` | Continuation/splitting protocol | **template + examples appendix** | Prevents output collapse and summary substitution in long Markdown/file generation. |
| 10 | `02_MULTI_FILE_SESSION.md` | Multi-file manifest and one-file-at-a-time flow | **appendix + examples** | Valuable for session choreography; scaffold should only retain the one-artifact rule. |
| 11 | `01_API_CALL_STRUCTURE.md` | API request envelope and stateless execution | **appendix + future runtime implementation** | Critical for implementation, but partially belongs to routing/runtime rather than prompt/workflow doctrine. |
| 12 | `06_DIFF_OUTPUT (1).md` | Unified diff output contract | **appendix + edit-mode chooser** | Keep as one transport option, not universal law. |
| 13 | `07_RESEARCH_OUTPUT.md` / `07_RESEARCH_BLOCK.md` | Schema-bound research output | **template candidate** | Useful, but check overlap with existing research/QA templates before promotion. |
| 14 | `03_PROJECT_OPENER.md` / `00_PROJECT_BOOTSTRAP.md` | Chat/session opener protocols | **examples appendix** | Strong examples; may duplicate existing handoff/opening templates. |
| 15 | `promptworkflowsAPI.py` | Programmatic template generator | **future appendix** | Useful source inventory, but generated content must be reconciled with canonical Markdown docs. |
| 16 | `ConstantAIFailureAnalysis.md` | Failure analysis and external research synthesis | **future research only** | Good problem framing; claims require external verification and cross-lane review. |

## Scaffold integration candidates

These are the only compact ideas suitable for F5 promotion after validation:

| Candidate ID | Scaffold target | Proposed compact rule |
|---|---|---|
| `PW-CF-SC-001` | `BEST_PRACTICES.md` | Use machine-checkable execution contracts for high-failure promptflows: explicit state, atomic task payload, preflight gate, typed output, and closure proof. |
| `PW-CF-SC-002` | `BEST_PRACTICES.md` | Treat chat history as unreliable execution state; pass state explicitly or halt on stale/missing state. |
| `PW-CF-SC-003` | `MISTAKES.md` | Failure pattern: executing compound tasks or inferred scope instead of rejecting/splitting the payload. |
| `PW-CF-SC-004` | `MISTAKES.md` | Failure pattern: proceeding after ambiguity, stale state, patch-check failure, or output validation failure instead of emitting HALT/CLARIFY. |
| `PW-CF-SC-005` | `TEMPLATES.md` | Add execution gate, task payload, state block, control signal, file output, split signal, and task closure templates, using compact entries and appendix pointers. |
| `PW-CF-SC-006` | `ESSENCE.md` | Add one sentence: high-risk promptflows should be driven by explicit state, atomic tasks, machine-readable outputs, and stop signals, not by conversational memory. |
| `PW-CF-SC-007` | `LEARNING_QUEUE.md` | Add candidate entries for model pinning, API statelessness, template sidecars, and external model-behavior verification; do not promote as accepted truth yet. |

## Appendix integration candidates

Create or update appendices in this order:

| Order | Appendix target | Action | Contents |
|---:|---|---|---|
| 1 | `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` | create | System bootstrap, state block, task payload, gate check, control signals, file output, split signal, task closure. |
| 2 | `APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md` | create | Canonical template catalog derived from the hand-authored Markdown files and reconciled with `promptworkflowsAPI.py`. |
| 3 | `APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md` | create | SEARCH/REPLACE protocol, unified diff protocol, full-body replacement boundary, failure handling, dry-run requirements. |
| 4 | `APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md` | create | Source-by-source notes for the new folder, duplicate handling, verification status, and promotion constraints. |
| 5 | `APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md` | create | Before/after examples that test state drift, compound scope, no-op completion, output cap collapse, patch mismatch, and HALT/CLARIFY behavior. |
| 6 | `APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md` | future-create | Verification ledger for external claims in `ConstantAIFailureAnalysis.md`. |

## Future research queue

| ID | Research item | Priority | Owner suggestion | Reason |
|---|---|---|---|---|
| `PW-CF-RQ-001` | Verify external claims about model auto-switching, token caps, platform behavior, and drift mechanisms. | P1 | Prompts Workflows + AI Handling/Routing | Prevents turning unverified platform claims into KB law. |
| `PW-CF-RQ-002` | Decide which runtime controls belong to prompt/workflow doctrine versus AI routing/runtime implementation. | P1 | Prompts Workflows + AI Handling/Routing + MetaOps | Model pinning, temperature, streaming, and response-format enforcement cross lane boundaries. |
| `PW-CF-RQ-003` | Validate whether state keeper should be a separate agent role in the OpenClaw architecture. | P1 | MetaOps + Knowledge Bank | `state_keeper` appears in the source pack but may imply new architecture beyond this lane. |
| `PW-CF-RQ-004` | Build a formal patch transport chooser that reconciles SEARCH/REPLACE, unified diff, full-body replacement, and live edit. | P1 | Prompts Workflows + Hygiene | Current sources include multiple edit protocols that must not conflict. |
| `PW-CF-RQ-005` | Define safe output ceilings for in-chat Markdown/file generation versus API-native file writing. | P1 | Prompts Workflows + AI Handling/Routing | Important to prevent split failure and summary substitution, but limits may change by runtime. |
| `PW-CF-RQ-006` | Design machine-readable sidecars for templates and ranking ledgers. | P2 | Informatics Design + Knowledge Bank | Useful for retrieval, but schema should be validated before creating bureaucracy. |
| `PW-CF-RQ-007` | Regression-test gate-check, HALT, CLARIFY, task-closure, split-signal, and patch-failure flows. | P1 | Prompts Workflows + Hygiene | Converts advice into behavioral tests for future agents. |

## Recommended patch sequence

1. **Create appendix layer first.** Add `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`, then source notes and patch transport appendix.
2. **Add regression examples.** Add examples before scaffold changes so scaffold rules have test cases.
3. **Update `TEMPLATES.md`.** Add compact templates with pointers to the execution-control appendix.
4. **Update `MISTAKES.md`.** Add failure patterns for implicit state, compound scope, validation bypass, and post-failure continuation.
5. **Update `BEST_PRACTICES.md`.** Add only compact, reusable rules after template and mistake evidence exists.
6. **Update `ESSENCE.md` last.** Add only a compressed operating sentence and appendix pointer.
7. **Update `LEARNING_QUEUE.md`.** Capture cross-lane and externally verified items as candidates only.
8. **Fetch back all touched files.** Verify changed-file set, target root, no accidental global governance mutation, and no external claim promoted as accepted truth.

## Validation checklist for the next patch pass

```yaml
validation_checklist:
  repo_boundary: leela-spec/MasterOfArts only
  target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
  source_root_used: NewResearchBecauseOfConstantFailure/
  scaffold_mutation_requires:
    - appendix evidence exists
    - candidate route recorded
    - overlap checked against existing PW-BP, PW-MK, PW-TPL entries
    - meta_ops validation pending or complete
  forbidden_promotions:
    - unverified external model/platform claims
    - runtime configuration law owned by AI Handling/Routing
    - global KB placement doctrine owned by Knowledge Bank
    - QA severity doctrine owned by Hygiene/Meta Detective
  fetch_back_required:
    - every written file
    - changed-file set
    - grep for new candidate ids
    - grep for accidental apexai-os-meta target references
```

## Execution stop

This pass creates the ranking/process appendix only.

No accepted F5 scaffold file is mutated in this pass. The next safe action is to create `APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md` and then use it as evidence for template and mistake updates.
