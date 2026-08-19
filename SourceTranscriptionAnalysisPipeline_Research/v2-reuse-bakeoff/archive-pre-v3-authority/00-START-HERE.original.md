---
title: "START HERE — Transcript-to-Knowledge V2.1"
doc_type: implementation_handover
updated: 2026-08-19
status: modular_stage_execution_authority
repository: leela-spec/apexai-os-meta
branch_policy: main_only_unless_operator_explicitly_changes_it
---

# 1. Current architecture line

The active architecture is **V2.1**.

V1 is historical and must not be used to select current components or implementation strategy. Archive it using `13-V1-ARCHIVE-CLI-INSTRUCTIONS.md`.

The repository history explains why this matters: V2 was a benchmark-driven candidate architecture, while the V2.1 patch was mainly a cross-cutting Trial-1 transport override. It did not originally regenerate one fully consolidated V2.1 recommendation. See `12-V2.1-PATCH-INTEGRATION-ROOT-CAUSE.md`.

# 2. Architecture layers

Use these layers for understanding, not as one giant execution prompt:

1. `01-ARCHITECTURE-ANALYSIS.md` — V2 macro options/research and component rationale.
2. `06-TRIAL1-TRANSPORT-LOCK.yaml` — authoritative Trial-1 AI transport policy.
3. `10-V2.1-RECOMMENDED-END-TO-END-ARCHITECTURE.md` — current macro recommendation from trigger to final knowledge product.
4. `11-V2.1-STAGE-BY-STAGE-IMPLEMENTATION-PLAN.md` — detailed cross-stage reference/overview.
5. `execution-modules/` — **direct execution authority: one file per stage/session.**

The product target remains `09-V2.1-TARGET-FIRST-EXECUTION-BRIEF.md`.

# 3. Direct execution rule

Do **not** hand one CLI AI the whole V2/V2.1 corpus and ask it to execute everything.

The first implementation is modular:

```text
operator
  -> gives CLI exactly one Sxx module
  -> CLI loads only module-declared context
  -> CLI implements/tests/saves that stage
  -> CLI writes Sxx handoff
  -> CLI commits/pushes stage-scoped work when appropriate
  -> CLI STOPS
  -> operator returns handoff to orchestrator
  -> orchestrator verifies remote truth
  -> orchestrator either ACCEPTS, REPAIRS SAME STAGE, or BLOCKS
  -> only after ACCEPT does operator start next Sxx module
```

The execution AI may never advance itself to the next module.

# 4. What to give a CLI session

For the first stage, give it:

- `execution-modules/00-ORCHESTRATOR-GUIDE.md`;
- `execution-modules/S00-TRIGGER-AND-RUN-INITIALIZATION.md`;
- the source/request you want to use.

For each later stage, give it only:

- the matching `execution-modules/Sxx-*.md` file;
- the previous stage handoff;
- the exact input artifacts named in that handoff/module;
- only the code/contracts/component entry explicitly named by the module.

Do not preload V1, all benchmark files, all failed-run reports, future stage files, or the complete research corpus.

# 5. Module sequence

```text
S00 Trigger / run initialization
S01 Source acquisition
S02 ASR + bounded ASR selection
S03 Conditional alignment / diarization
S04 TTK canonical custody
S05 TTK processing windows
S06 Optional local pre-extraction
S07 Grounded real-CLI semantic Map
S08 Structured output / retry seam
S09 Deterministic Map validation + evidence ledger
S10 Advisory source-support checks
S11 Real-CLI global Reduce / synthesis
S12 Selective external verification
S13 Deterministic compile + product QA
S14 Product evaluation + production handover + regression gate
```

The full module index is `execution-modules/README.md`.

# 6. Authority order for a module session

When instructions conflict:

1. current explicit operator instruction;
2. `06-TRIAL1-TRANSPORT-LOCK.yaml` where semantic transport is involved;
3. `10-V2.1-RECOMMENDED-END-TO-END-ARCHITECTURE.md` for macro architecture;
4. `execution-modules/00-ORCHESTRATOR-GUIDE.md` for session protocol;
5. the **single active Sxx module** for implementation details;
6. previous stage handoff and named owning code/contracts;
7. `11-V2.1-STAGE-BY-STAGE-IMPLEMENTATION-PLAN.md`, component registry, benchmark spec, or V2 option architecture only when the active module explicitly needs a deeper reference;
8. older history only for evidence.

A failed implementation's generated `PASS`, `FINAL-REPORT.yaml`, or handover never outranks these authorities merely because it is newer.

# 7. Non-negotiable semantic boundary

Trial 1 strong semantic work uses only:

- Claude Code subscription CLI;
- Codex CLI authenticated through the ChatGPT plan;
- Antigravity CLI only after a real headless `agy` subprocess smoke PASS.

The coding agent/internal subagent, regex, templates, `antigravity_agent`, API-key/pay-as-you-go routes, browser AI, and Gemini CLI may not substitute for those semantic workers in Trial 1.

# 8. First implementation scope

Build **one real vertical slice** through S00-S14 first. Inspect the actual final knowledge product.

Only after S14 is accepted should the orchestrator schedule the same production chain for:

- four-source regression;
- fresh English E2E;
- fresh German E2E;
- unchanged-run resume proof;
- targeted Map invalidation/resume proof.

Those are repeated acceptance runs of the production chain, not another architecture implementation.
