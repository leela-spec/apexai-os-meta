---
title: "START HERE — Transcript-to-Knowledge V2.1"
doc_type: implementation_handover
updated: 2026-08-19
status: ready_for_stage_scoped_execution
repository: leela-spec/apexai-os-meta
branch_policy: main_only_unless_operator_explicitly_changes_it
supersedes_for_current_architecture:
  - SourceTranscriptionAnalysisPipeline_Research/PIPELINE_ARCHITECTURE_OPTIONS_AND_V1_DECISION_2026-08-18.md
  - SourceTranscriptionAnalysisPipeline_Research/PIPELINE_DECISION_CONTRACT_2026-08-18.yaml
  - SourceTranscriptionAnalysisPipeline_Research/V1_IMPLEMENTATION_PLAN_CLI_SEMANTIC_WORKER_2026-08-18.md
preserve_history: true
---

# 1. Start here

The current architecture is **V2.1**, not V1.

The V1 files above remain historical evidence but must not be used to select current components or simplify the V2.1 pipeline.

The repository now separates three different levels deliberately:

1. **Macro options/research:** `01-ARCHITECTURE-ANALYSIS.md` — all important V2 stages, alternatives, hypotheses, and researched reusable components.
2. **Macro recommendation:** `10-V2.1-RECOMMENDED-END-TO-END-ARCHITECTURE.md` — the recommended V2.1 pipeline from trigger through final knowledge product, including which components are core, conditional, challenger, advisory, or evaluator.
3. **Detailed implementation:** `11-V2.1-STAGE-BY-STAGE-IMPLEMENTATION-PLAN.md` — one chapter per stage with exact `INPUT -> TOOL/WORK -> TEST -> OUTPUT -> NEXT INPUT` contracts.

The product target remains `09-V2.1-TARGET-FIRST-EXECUTION-BRIEF.md`.

---

# 2. Authority order

When instructions conflict, use:

1. current explicit operator instruction;
2. `06-TRIAL1-TRANSPORT-LOCK.yaml` for Trial-1 AI transport;
3. `10-V2.1-RECOMMENDED-END-TO-END-ARCHITECTURE.md` for the current recommended architecture;
4. `11-V2.1-STAGE-BY-STAGE-IMPLEMENTATION-PLAN.md` for current implementation details;
5. `09-V2.1-TARGET-FIRST-EXECUTION-BRIEF.md` for the product target and anti-substitution rule;
6. `07-DECIDED-FRAMEWORK-AND-TEST-EVALUATION-HANDOVER.yaml` for locked/open framework decisions;
7. `03-BENCHMARK-AND-TEST-SPEC.yaml`, `04-COMPONENT-REGISTRY.yaml`, and `01-ARCHITECTURE-ANALYSIS.md` for benchmark/candidate detail;
8. current `.claude/skills/transcript-to-knowledge/**` contracts/code for existing deterministic invariants;
9. older V1/research/history only for evidence.

A later failed implementation or generated PASS report does not outrank these architecture authorities merely because it is newer.

---

# 3. Do not load the whole repository into context

The previous execution instructions asked an AI to read too many large files before acting. V2.1 now uses **stage-scoped context**.

## At overall run start, read only

1. this file;
2. `06-TRIAL1-TRANSPORT-LOCK.yaml`;
3. `10-V2.1-RECOMMENDED-END-TO-END-ARCHITECTURE.md`;
4. `09-V2.1-TARGET-FIRST-EXECUTION-BRIEF.md`.

Do not immediately ingest every benchmark, historical report, old implementation plan, component README, and prior artifact tree.

## For the current stage, read only

- the matching chapter in `11-V2.1-STAGE-BY-STAGE-IMPLEMENTATION-PLAN.md`;
- the previous stage handoff and declared input artifacts;
- the relevant component-registry entry;
- the code/contracts that directly own that stage.

If a stage fails, expand context to its direct dependency/owning code only. Do not solve a local problem by reopening the entire architecture.

## Between stages

Write/use the compact stage handoff defined in `11-V2.1-STAGE-BY-STAGE-IMPLEMENTATION-PLAN.md`, then compact/reset working context before the next stage.

Pipeline state comes from files and hashes, not conversation memory.

---

# 4. Current recommended V2.1 chain

```text
S0  APEX/OpenClaw -> thin deterministic runner
S1  existing P1 + yt-dlp/ffmpeg acquisition
S2  calibrated faster-whisper reference + bounded Parakeet challenger
S3  WhisperX only when alignment/speaker attribution earns a conditional role
S4  TTK canonical custody
S5  TTK bounded processing windows
S6  optional GLiNER2 hints; NuExtract only if that role remains unmet
S7  recommended grounded Map: LangExtract + real allowed subscription-CLI provider
    control/fallback: direct real allowed subscription CLI
S8  native CLI schema + bounded retry + TTK validation
    Instructor only if the native seam proves brittle/duplicated
S9  TTK deterministic Map validation / evidence ledger
S10 mDeBERTa advisory support warnings; HHEM optional English comparator
S11 recommended Reduce: direct real subscription CLI over validated TTK ledger
    challenger: fixed DocETL route, optimizer off first
S12 TTK checkworthiness queue + allowed subscription-CLI external verification
S13 TTK compiler -> canonical machine knowledge + operator wiki
S14 product evaluation / stage-local selection / APEX handoff
```

This is not a requirement that every challenger run on every source. Challengers are tested **inside their own stage** and promoted only for material value.

---

# 5. Trial-1 semantic transport

Allowed:

- Claude Code subscription CLI;
- Codex CLI authenticated through the ChatGPT plan;
- Antigravity CLI only after a real headless `agy` subprocess smoke passes.

Not allowed in Trial 1:

- Gemini CLI;
- browser AI;
- API-key/pay-as-you-go/hosted model APIs;
- an internal coding agent/subagent creating semantic output and labeling it as external CLI output.

If LangExtract, DocETL, DeepEval, or another framework needs strong AI, it must use an allowed CLI through a bounded adapter or the experiment is `BLOCKED_FOR_TRIAL1`.

---

# 6. Non-negotiable product boundaries

- The product is the **knowledge artifact**, not a validator or PASS report.
- No regex/keyword/template pseudo-semantic path may replace real Map/Reduce reasoning.
- Fresh E2E means real newly acquired/materialized audio -> actual ASR -> actual semantic path.
- TTK remains canonical custody/state/coverage/compiler unless a measured replacement preserves all hard invariants and materially wins.
- Processing windows are not semantic Meso chapters.
- Factual/testable Micro claims require exact source evidence; non-factual semantic objects retain provenance without forced quote quotas.
- Source support and external-world truth remain separate.
- Actual source-specific artifact quality outranks schema validity or automated PASS labels.
- Resume reuses unchanged valid work and invalidates only dependent work.

---

# 7. Implementation progression

Do not begin by running all four sources.

Use:

```text
one real representative Map packet
  -> inspect actual semantic output
  -> one complete representative source S0-S13
  -> inspect actual final knowledge artifact
  -> bounded stage-local challenger comparisons
  -> select/promote only material winners
  -> four-source regression
  -> genuinely fresh EN + DE E2E
  -> real resume/idempotency demonstration
```

This is deliberately designed to catch wrong-target execution before spending large subscription quota.

---

# 8. Where to go next

For architecture rationale and options: read `01-ARCHITECTURE-ANALYSIS.md` **only when the current stage requires an option decision**.

For the recommended complete chain: read `10-V2.1-RECOMMENDED-END-TO-END-ARCHITECTURE.md`.

For implementation: open the current stage chapter in `11-V2.1-STAGE-BY-STAGE-IMPLEMENTATION-PLAN.md` and execute that stage from its declared input to its declared output.

Do not use the old V1 architecture as a shortcut.
