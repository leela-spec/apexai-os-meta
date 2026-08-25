# Transcript-to-Knowledge V3 — Architecture

**Status:** AUTHORITATIVE  
**Date:** 2026-08-19  
**Supersedes:** V2.1 recommended architecture and S00-S14 orchestration

## 1. Target

The target is a **working, repeatable transcript-to-knowledge product**, not an orchestration framework:

`real video/audio/transcript -> source-faithful structured knowledge -> traceable evidence -> useful operator artifact`

The architecture must maximize:

1. product fidelity and important-insight retention;
2. reuse of proven infrastructure;
3. resilience and recoverability;
4. simplicity and low maintenance burden;
5. token/runtime efficiency;
6. multilingual EN/DE viability.

## 2. Architectural correction from V2.1

V2.1 had promising component research, but froze a bespoke 15-stage production architecture before proving that existing end-to-end systems could not solve most of the use case. It also placed the operator between ChatGPT and a CLI executor after every small stage.

V3 keeps useful component hypotheses but changes the architecture from **stage-first implementation** to **evidence-first selection**.

The sequence is now:

```text
find proven systems
    -> run them
    -> compare real products
    -> identify actual gaps
    -> benchmark only the components needed for those gaps
    -> integrate the smallest winning composition
    -> prove it on 3 real videos
```

## 3. Two-plane architecture

### 3.1 Control plane

```text
ChatGPT
  architecture + product review
      |
      | Git/main work package
      v
OpenClaw
  thin relay + process supervision only
      |
      | agy process
      v
Antigravity CLI
  autonomous bounded executor
      |
      v
Git/main
  durable state, artifacts, commits
```

**ChatGPT responsibilities**

- define the target and bounded module;
- maintain V3 authority files;
- review remote Git evidence at the three macro gates;
- make architecture/product decisions when evidence is sufficient;
- stop drift when repair work stops advancing the product.

**OpenClaw responsibilities**

- read the current module/work package;
- launch Antigravity CLI in the repository;
- monitor exit/output/input-wait state;
- relay deterministic input only when explicitly authorized;
- terminate/restart a failed process once when appropriate;
- report process/commit state.

OpenClaw must **not** decide whether output quality is good, redesign the pipeline, choose components, or invent a repair plan.

**Antigravity responsibilities**

- execute one module in a fresh/bounded context;
- research/run/inspect/implement/test as the module requires;
- perform normal local repair loops without returning after every failure;
- stop on hard blocker, operator decision, or two-strike approach failure;
- commit useful module-scoped work directly to `main`.

**Git/main responsibilities**

- source of truth for current module, evidence, artifacts, and implementation;
- no chat transcript required for reconstruction;
- commit is the primary handoff; compact module result is secondary.

### 3.2 Product plane

V3 does **not** assume the V2.1 component graph is the final product. The product plane is selected through evidence.

Preference order:

1. adopt a proven near-complete existing system;
2. lightly fork/adapt one proven system;
3. compose 2-4 proven components;
4. retain/customize existing TTK pieces only where a measured gap remains;
5. new custom framework only when a benchmark proves no existing option fills the gap.

A plausible composition from prior research remains available as a **challenger**, not authority:

```text
yt-dlp / ffmpeg
    -> faster-whisper or Parakeet
    -> optional WhisperX
    -> TTK custody/windowing if needed
    -> LangExtract / direct strong CLI extraction
    -> optional Instructor for typed output
    -> direct strong CLI or DocETL synthesis
    -> deterministic/source-grounding checks
    -> knowledge compiler
    -> DeepEval + human/product baselines off-path
```

Every box must earn its place.

## 4. Current externally verified capabilities — 2026-08-19

These are implementation facts, not permanent assumptions. Module M00/Mxx records the **installed version actually used**.

### OpenClaw

Current OpenClaw documentation exposes `exec` with `pty: true`, background sessions, and a `process` tool capable of polling/logging, detecting likely input waits, writing stdin, sending keys, submitting, pasting, and killing sessions. Background process state is in-memory, so Git remains the durable recovery boundary.

OpenClaw ACP currently documents supported external harnesses including Claude Code, Codex, Gemini CLI, Cursor, Copilot and others, but **Antigravity is not a documented ACPX target**. Therefore V3 does not build a custom Antigravity ACP adapter.

### Antigravity CLI

Current official Antigravity docs identify CLI v1.1.11 and a fine-grained `deny > ask > allow` permission engine. The official changelog shows substantial recent fixes to `--print`/headless behavior. However, current open issues still document headless permission-scope limitations.

Therefore V3 uses **capability detection**, not a frozen transport assumption:

1. inspect installed `agy --version`;
2. run a bounded non-mutating headless smoke that proves stdout/stderr/exit behavior;
3. run a bounded workspace mutation/test smoke only if permission policy is safe;
4. if all required checks pass, headless mode is allowed;
5. otherwise use normal `agy` in an OpenClaw PTY session;
6. never use `--dangerously-skip-permissions` as the default architecture.

## 5. OpenClaw relay failure policy

The relay gets **one repair cycle**.

- First relay defect: repair the smallest transport/config issue and rerun M00.
- Second relay defect before a real product-advancing module completes: **stop building orchestration** and use direct operator launch of Antigravity with the same module file.

No OpenClaw daemon, custom queue, new state database, custom ACP adapter, browser ChatGPT relay, or task framework is required for V3 initial success.

Browser-mediated automatic ChatGPT relay is deferred until the product pipeline works.

## 6. Module/context architecture

V3 uses 8 product-level modules rather than 15 micro-stages.

Each module is a fresh Antigravity context and has:

- one target;
- explicit inputs;
- allowed research/code scope;
- observable acceptance;
- hard stop conditions;
- one compact result file.

Inside a module, Antigravity may iterate normally.

### Two-strike rule inside a module

If the same subsystem/approach needs two corrective iterations **without measurable product advancement**, do not perform correction #3. Emit `APPROACH_SUSPECT` with:

- attempted approach;
- observed failures;
- why it blocks the target;
- existing alternative to try;
- recommendation to replace/simplify/abandon.

## 7. Review architecture

Independent ChatGPT review happens at **meaningful choice boundaries**, not after every command.

### Gate R1 — after M01

Question: can a proven near-complete system be adopted/forked, or are component benchmarks actually necessary?

### Gate R2 — after M05

Question: what is the smallest production composition justified by real output evidence?

### Gate R3 — after M07

Question: does the selected production system work repeatedly on the 3-source corpus and produce the target knowledge product?

M02-M04 are modular fresh contexts but do not require human relay between them unless a hard decision is reached.

## 8. Benchmark corpus

### Required selection corpus

1. `P-h5WSQG1Sw` — EN long science interview, multi-speaker/long-context stress;
2. `CygwqaNg2PY` — EN technical finance, named/technical term stress;
3. `vFTuLylvYnA` — DE finance, multilingual/numeric/domain stress.

### Optional holdout

`oZIsMX6WgFs` — EN technical procedure/market cycles.

The holdout runs only when the three-source result is ambiguous, a specific procedural-recall hypothesis needs it, or final confidence warrants a fourth source.

## 9. Product-first gates

Before first working vertical slice, fix only:

- execution blockers;
- source/product corruption;
- fake/substituted execution;
- experiment-invalidating defects;
- material safety/data-loss risks.

Defer bookkeeping imperfections unless they directly invalidate the result.

Every module must answer:

1. Did we run something real?
2. Did we learn something about actual product quality or eliminate a demonstrated blocker?
3. Are we materially closer to the target?

If fewer than two answers are YES, the work is drift and must stop.

## 10. Custom-code authorization test

Before creating a new abstraction, record:

```text
Existing solution tried:
Observed failure:
Why configuration/adaptation is insufficient:
Smallest custom addition:
```

No observed failure => no new abstraction.

## 11. Definition of success

V3 succeeds when the repository contains a selected, reproducible system that:

- consumes real source media/transcripts;
- produces useful structured source-specific knowledge;
- preserves timestamp/text/source traceability;
- retains important claims, mechanisms, procedures, caveats and uncertainty;
- avoids fake semantics and cross-source contamination;
- works on EN and DE;
- reruns without manual surgery;
- is demonstrably simpler because proven infrastructure replaced custom invention;
- has three-source benchmark evidence supporting the choice.
