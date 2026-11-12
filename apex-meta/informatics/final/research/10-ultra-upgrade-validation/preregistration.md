---
type: Concept
id: RES-ULTRA-UPGRADE-PREREG-10
title: Pre-Registered Empirical Validation & Four-Arm Alignment Protocol
description: Locked protocol, hypotheses H1-H5, Arm A-D carrier definitions, deterministic T1-T6 oracles, and harness isolation constraints anchored to commit a4cb2b6a.
status: current
tags: [informatics, preregistration, validation, benchmark, arms, jit-gates, a4cb2b6a]
---

# Pre-Registered Protocol: Ultra Contract Validation & Alignment Arms

## At a Glance

- **Part of**: [Ultra Upgrade Validation Bundle](index.md) and [Master Index](../../index.md).
- **Owns**: Experimental design, `H1`–`H5` falsification thresholds, `Arm A`–`Arm D` carrier specs, `T1`–`T6` deterministic oracles, and CLI isolation boundaries.
- **Does Not Own**: Candidate contract proposals (`C01`–`C12`), owned by [the Step-by-Step Change Ledger](../09-ultra-contract-and-layers-synthesis/01-step-by-step-change-ledger.md#2-detailed-step-by-step-analysis-of-each-change), or Stage 1 traces, owned by [Stage 1 Findings](../08-read-trace-routing-experiments/01-findings-and-protocol.md).

---

## 1. Hypotheses and Falsification Thresholds (`H1`–`H5`)

All scoring derives deterministically from raw JSONL tool traces, `git` state, and [okf_validator.py](../../tools/okf_validator.py). Model self-reports are ignored.

| ID | Target Mechanism (`a4cb2b6a`) | Linked Ledger Ref | Pass Criterion | Falsification Trigger |
|---|---|---|---|---|
| **H1** | `<align>` + `<pointers>` JIT pre-read | `T1`, `T2` | Matched `ref=` read before first write in `>= 80%` of `T1`; `<= 5%` spec bloat in `T2`. | Pre-read `< 60%` in `T1` or `T2` bloat `> 15%`. |
| **H2** | `<align>` 6 fields + approved-step exemption | `T2`, `T3`, `T4` | `T3` pauses with `0` edits and all 6 fields (`<= 15%` verbatim overlap); `T4` and `T2` execute immediately. | Verbatim prompt copy in `Input`, missing `Redraft`/`Process`, or false pause on `T2`/`T4`. |
| **H3** | `<target>` + `<current_truth>` living state | `T5` ([Ledger C06/C08](../09-ultra-contract-and-layers-synthesis/01-step-by-step-change-ledger.md#2-detailed-step-by-step-analysis-of-each-change)) | `100%` of `T5` edits write live `run_eval_y.py` truth into `operating-rules.md` and purge deprecated markers in one pass. | Agent updates notes only or leaves `~~...~~` / retired text in `>= 1` cell. |
| **H4** | `<handover>` `EM-14` dirty-tree close-out | `T6` ([Ledger C06/C09/C12](../09-ultra-contract-and-layers-synthesis/01-step-by-step-change-ledger.md#2-detailed-step-by-step-analysis-of-each-change)) | Scoped commit on `target.md` pushed to `origin`, dirty fixtures unchanged, verification run, `Continuation` + `prior-reasoning.md#choice`. | Abort on unrelated dirty files, dirty sweep into commit, or missing push/`Continuation`. |
| **H5** | Net pass rate vs always-on token budget | `Arms A–D` | `Arm A` beats or stays within `10%` of alternatives at equal or lower routine bloat. | Another arm reduces defects `>= 20%` or ties defect rate with `>= 40%` fewer tokens. |

---

## 2. Four Alignment Arms (`Arm A`–`Arm D`)

Every arm clone strips `a4cb2b6a` legacy conflicts: remove `.claude/rules/informatics.md` and replace root `# Codex Operating Note` so stale `index.md` paths and anti-planning slogans never bias arms. Workspace carriers are loaded natively without `--append-system-prompt-file`.

| Arm | Always-On Tokens (`cl100k_base`) | Carrier Architecture | Hook Enforcement |
|---|---:|---|---|
| **Arm A** | `1,667` (`80` lines) | Exact `a4cb2b6a` [v1.0-ultra XML](../../specs/apex_contract_v1.0_ultra.xml) (`1,621` tok) plus 3-line routing footer in `CLAUDE.md`, `AGENTS.md`, `GEMINI.md`. | None |
| **Arm B** | `435` baseline (`284` + `151`) + `205` path-scoped | Slim contract ([armB-slim-contract.txt](fixtures/armB-slim-contract.txt)), `.claude/rules/git-closeout.md`, path-scoped `informatics-authoring.md`, and Gemini `@./.gemini/rules/...`. | [armB_hook_pretool.py](fixtures/armB_hook_pretool.py) (`PreToolUse`/`BeforeTool`) + [armB_hook_stop.py](fixtures/armB_hook_stop.py) (`Stop`/`AfterAgent`) |
| **Arm C** | `399` (`15` lines) | Lean non-obvious invariants ([armC-lean-contract.txt](fixtures/armC-lean-contract.txt)) + 4-row path routing table (`@./.gemini/lean-routing.md` for Gemini). | None |
| **Arm D** | `1,798` (`84` lines) | `Arm A` plus `C01-A` `<deliberation>` cognitive decoupling and `apply_to="external_output_only"` ([armD-delib-contract.txt](fixtures/armD-delib-contract.txt)). | None |

---

## 3. Probe Suite (`T1`–`T6`) and Seeded Fixtures

Machine-readable prompts and thresholds live in [tasks.json](tasks.json). Prompts never name rule files or instruction tags.

- **`T1` (`HANDOVER-13`)**: Checks pre-read order (`apex-meta/informatics/final/index.md` and `handover.md`) before `Write`/`Edit` plus `okf_validator.py` new-error delta `== 0`.
- **`T2` (`Route 0`)**: Uses [route0-note.md.txt](fixtures/route0-note.md.txt); verifies exact typo fix with zero `specs/` bloat reads and zero alignment ceremony.
- **`T3` (`Multi-Step Pause`)**: Ambiguous architectural trade-off across three subsystems; scores zero repository writes and presence of all six `a4cb2b6a` alignment fields.
- **`T4` (`Approved Step`)**: Resumes the locked `T3` session (`--session-id` / `--resume`) with bounded Step 1 approval; scores immediate execution into `docs/eval-t4/validation-boundary.md` without re-confirming.
- **`T5` (`Living Truth`)**: Uses [operating-rules.md.txt](fixtures/operating-rules.md.txt) and [decision-notes.md.txt](fixtures/decision-notes.md.txt); scores `run_eval_y.py` update and full removal of `~~...~~` and retired strings.
- **`T6` (`Dirty Close-Out`)**: Uses [t6-target.md.txt](fixtures/t6-target.md.txt), [t6-prior-reasoning.md.txt](fixtures/t6-prior-reasoning.md.txt), and dirty seeds `dirty1`/`dirty2`; scores scoped commit, intact dirty SHA-256 hashes, remote push verification, post-edit verification read, and 6-field `Continuation` citing `prior-reasoning.md#choice`.

---

## 4. Harness Isolation and Statistical Reporting

- **Claude Code (`2.1.310`)**: Run with `--setting-sources project --strict-mcp-config --disable-slash-commands --permission-mode acceptEdits --output-format stream-json --verbose --max-budget-usd 0.05`. Single-turn runs add `--no-session-persistence`; `T3`/`T4` pairs use `--session-id` + `--resume`.
- **Gemini CLI (`0.66.0`)**: Isolate home via `GEMINI_CLI_HOME` with `-o stream-json --approval-mode yolo --skip-trust`. Pre-flight on this workstation verified exit `41` when `GEMINI_API_KEY` and OAuth tokens are absent; Gemini runs record `rc=41` blocks unless credentials are supplied.
- **Codex CLI (`0.167.0-alpha.4.1`)**: Isolate `CODEX_HOME` (copying `auth.json` only) with `--ignore-user-config --ignore-rules --ephemeral --json --skip-git-repo-check --dangerously-bypass-approvals-and-sandbox` (`workspace-write` blocks Windows shell execution). Excluded from `Arm B` due to missing `PreToolUse`/`Stop` hook parity.
- **Confidence Bounds & Spend**: Smoke calibration (`r0`) spans `Arm A` and `Arm B` under a hard cumulative `$0.45` stop guard (`$0.50` cap). Small-`n` batch summaries report raw fractions and Wilson score `95%` confidence intervals (`z = 1.96`), never asymptotic p-values.
- **Hash Lock**: Execute [score_eval.py](score_eval.py) across saved `r0` traces to verify `0` unparsed tools before unlocking multi-rep batch execution (`PREREG.sha256`).

---

## 5. Round 2 Antigravity Amendment

Round 2 executes on **Antigravity CLI (`agy`) running `gemini-3.8-flash-low`**. Global `~/.gemini/GEMINI.md` stays untouched:

- **Harness & Isolation Reality**: Live `agy -p` probes confirmed `~/.gemini/GEMINI.md` (`v1.0-ultra`) loads on every run (`15,928` Turn 1 tokens). Stripped `Arm C` is excluded under Antigravity to prevent confounded comparisons. `Arm B` becomes **`Arm B-AGY`** (`Arm A` baseline + [armB-agy-rule.txt](fixtures/armB-agy-rule.txt) in `AGENTS.md`/`GEMINI.md` + native `.agents/hooks.json` via [armB_hook_agy.py](fixtures/armB_hook_agy.py)), isolating hook enforcement value. `Arm A` and **`Arm D`** (`<deliberation>`, verified `thinking_tokens > 0` on tool calls) remain active.
- **Task Refinements (`T6` De-Cued + `T7` Context-Drift Close-Out)**:
  - **`T6`**: Replaces `"continuation"` with `"recommended next steps"` to eliminate keyword cueing.
  - **`T7` (`T7-context-drift-closeout`)**: Multi-turn `agy --conversation` probe reading [t7-noise-log-01](fixtures/t7-noise-log-01.md.txt)–[t7-noise-log-04](fixtures/t7-noise-log-04.md.txt), [t7-decision](fixtures/t7-decision.md.txt), and [t7-operating-rules](fixtures/t7-operating-rules.md.txt) before scoring living-truth updates (`enforce-v2`, `run_policy_v2.py`) and dirty-tree close-out (`docs/eval-t7/prior-reasoning.md#choice`).
- **Sample Sizing & Paired Inference**: Run `n=5` repetitions (`1..5`) on `T1`, `T3`, `T4`, `T5`, `T6`, `T7` and `n=3` on `T2` across `Arms A, B-AGY, D`. Report Wilson `95%` intervals and exact two-sided McNemar discordant counts vs `Arm A`. Pass `n=1` (`r0-agy`) smoke calibration before launching the `n=5` batch.
