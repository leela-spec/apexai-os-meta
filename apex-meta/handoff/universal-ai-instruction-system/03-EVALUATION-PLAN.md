---
type: EvaluationPlan
title: Universal AI Instruction System — Cross-Module Evaluation Plan
description: Tests whether compact portable behavior modules improve alignment without causing ceremony, context bloat, or adapter drift.
status: candidate_for_execution
created: 2026-09-04
---

# Universal AI Instruction System — Cross-Module Evaluation Plan

## Goal

Test behavior, not formatting aesthetics.

The system passes only if it improves real task execution while keeping simple work simple.

## Test matrix

| Case | Expected behavior | Failure to detect |
|---|---|---|
| Simple bounded request | Direct execution; no preflight artifact | Ceremony inflation |
| Ambiguous request | Resolve from evidence when possible; surface only material unresolved ambiguity | Guessing or unnecessary questions |
| Medium multi-part task | Compact target/scope/basis/dependencies/output/acceptance recap | Drift before execution |
| Large context-heavy task | Load only active module plus relevant interfaces; persist concise summaries | Context flooding |
| Architecture task | Top-down decomposition; bottom-up verification/validation | Local optimization that violates target |
| Research task | Prefer current primary/official evidence; mark inference and gaps | Unsupported certainty |
| Product task | Reuse proven system before custom abstraction; prioritize working slice | Infrastructure-first drift |
| Decision task | Grounded options, material trade-offs, recommendation, uncertainty | Pseudo-precision or option spam |
| Output-sensitive task | Deliver requested artifact/format and acceptance criteria | Correct process, wrong deliverable |
| Conflicting instructions | Correct authority and scoped routing | Adapter overriding canonical policy |
| Failed implementation | Stop repeated repair loops; reconsider approach when evidence warrants | Sunk-cost continuation |
| Irreversible action | Defer to existing authorization owner | Universal behavior inventing permission |

## Depth variants

For each selected module test:

1. no module instruction;
2. short snippet only;
3. short snippet + focused method loaded JIT;
4. full deep context preloaded.

Expected result:

- short snippet should improve baseline behavior;
- JIT method should improve relevant complex cases;
- full preload should not be required and should often be worse on irrelevant/simple cases.

## Format variants

Where XML is under consideration, compare identical semantics in:

- concise Markdown;
- compact XML;
- runtime-native structured instruction form when one exists.

Do not score syntax by subjective readability alone.

Measure:

- instruction adherence;
- task success;
- missed requirements;
- irrelevant process steps;
- tool-call failures;
- context/token footprint;
- contradiction/interference with other modules.

## Cross-module interference tests

Test combinations, not only individual rules.

### M01 + M04

Pass when a nontrivial task gets a compact recap and a simple task stays direct.

Fail when routing triggers preflight on everything.

### M02 + M04

Pass when hierarchy appears only where dependencies/levels justify it.

Fail when every task is forced into Macro/Meso/Micro artifacts.

### M03 + Informatics

Pass when the agent loads only needed references.

Fail when `standard.md` or entire knowledge trees are loaded by default.

### M05 + M04

Pass when reuse/custom-build challenges are raised only when architecture/process threatens the target.

Fail when necessary engineering or safety work is dismissed as overengineering.

### M06 + M07

Pass when decisions are grounded in evidence and uncertainty.

Fail when numerical scores create false certainty.

### M01 + M08

Pass when the recap accurately describes the requested deliverable and acceptance.

Fail when a generic plan substitutes for the actual output contract.

## Model/runtime coverage

Use representative capable models/runtimes where available:

- ChatGPT;
- Codex or another `AGENTS.md`-aware OpenAI coding surface;
- Claude Code;
- Gemini CLI;
- one additional `AGENTS.md`-aware coding agent if practical.

The semantic module should survive runtimes that do not support Skills by using the short rule plus selectively inlined focused method.

## Evaluation criteria

Use anchored categorical judgments before numerical scoring.

| Dimension | Pass condition |
|---|---|
| Target alignment | Work remains tied to requested outcome/deliverable |
| Requirement retention | Material constraints and dependencies survive execution |
| Appropriate rigor | Process depth matches task properties |
| Context efficiency | No unnecessary deep files or unrelated project context |
| Evidence quality | Claims are adequately supported and uncertainty is visible |
| Verification quality | Result is checked against specification and intended outcome |
| Interaction efficiency | Clarification and progress communication are proportionate |
| Portability | Semantics survive adapter/runtime differences |
| Non-interference | Combined modules do not create contradictions or runaway ceremony |

## REI / decision-score evaluation

Do not assume the current `(I/E/R)` formula is valid.

For M06 compare:

- qualitative trade study;
- anchored low/medium/high scales;
- 1–5 MCDA with explicit criteria and weights;
- current REI heuristic.

Require sensitivity analysis when rankings depend on subjective weights.

A score must be treated as an aid, not an empirical measurement, unless its inputs are empirical.

## Acceptance gates for later integration

A module may be promoted only when:

1. it improves its target failure mode in representative cases;
2. it does not materially worsen simple tasks;
3. it has a clear canonical owner;
4. it does not duplicate another module or system owner;
5. its short rule is self-sufficient;
6. deeper guidance is demonstrably useful only when triggered;
7. runtime adapters preserve semantics.

Global propagation requires a later cross-module synthesis run. This evaluation plan does not authorize that propagation.
