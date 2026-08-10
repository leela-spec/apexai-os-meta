---
title: "OpenClaw Local Executor — Verification Report 2026-08-10"
doc_type: verification_report
initiative: local-executor
created: 2026-08-10
status: blocked-at-g3-plugin-version
canonical_plan: FEE/OpenClaw Local Executor — Installation and Implementation Plan.md
canonical_decision: FEE/OpenClaw Local Executor — Operator Decision Lock.md
---

# OpenClaw Local Executor — Verification Report 2026-08-10

## Terminal status

Execution stopped at the in-process llama.cpp provider installation gate. The plan requires exact plugin version `@openclaw/llama-cpp-provider@2026.7.1-2` and prohibits substituting an unreviewed release. npm returned `E404 No match found for version 2026.7.1-2`.

Published plugin state at the stop:

- latest stable: `2026.7.1`
- extended stable: `2026.6.34`
- beta: `2026.7.2-beta.7`
- latest stable peer requirement: `openclaw >=2026.7.1`
- installed in-process llama.cpp plugin: none

The host is installed as `OpenClaw 2026.7.1-2 (0790d9f)`. Installing plugin `2026.7.1` would therefore be a version-policy deviation requiring operator approval.

## Evidence identity

| Item | Value |
|---|---|
| Repository checkpoint | `35ef223bcbf3c523edecdda32749720aa66d0bba` |
| OpenClaw | `2026.7.1-2 (0790d9f)` |
| Node | `v24.18.0` |
| Active config SHA-256 | `75D2C58A33136E698F24F3FB329FEDC6668E29DFB835DE74A3C30DFBEFDF52AF` |
| Qwen GGUF SHA-256 | `D98CDCBD03E17CE47681435B5150E34C1417F50B5C0019DD560E4882C5745785` |
| llama-server launcher SHA-256 | `63E7ED32203FC90DF3DF42FCC42762B988446E0D66B786ADB9AD059FA3CE2819` |
| Gateway | loopback `127.0.0.1:18789`, token SecretRef from user environment |
| Standalone model endpoint | loopback `127.0.0.1:8090` |
| Evidence timestamp | `2026-08-10T18:44:17.8391418+02:00` |

No token value or account credential is stored in this repository.

## Gate results

| Gate | Status | Evidence |
|---|---|---|
| G0 repository/model preservation | PASS | `main` matched `origin/main` before work; unrelated files excluded; model hash matched the installation record. |
| Existing test baseline | PASS | 32 FEE tests and 177 LMBench tests passed before installation. |
| G0A direct structured tool call | PASS | Qwen returned `finish_reason=tool_calls` with one `echo` call and arguments `{"text":"APEX_TOOL_OK"}`. |
| Pinned host install | PASS WITH DOCUMENTED DEVIATION | Official MSI handoff returned Windows Installer 1602 twice. Official Node `v24.18.0` portable ZIP was verified against Node's published SHA-256 `0AE68406B42D7725661DA979B1403EC9926DA205C6770827F33AAC9D8F26E821`, then OpenClaw was installed user-locally at exact version `2026.7.1-2`. |
| Baseline setup/config | PASS | `openclaw setup --baseline`; active configuration validates with no warnings; Gateway binds loopback with token auth; secrets use an environment SecretRef. |
| Standalone normal turn | PASS | Dedicated `apex-executor` returned exactly `APEX_QWEN_OK` through `apex-local/qwen3-8b-q4km`. |
| G2 standalone tool trajectory | PASS | One typed `session_status` call, zero tool failures, result returned to Qwen, final response `apex-local/qwen3-8b-q4km`. |
| Skill containment | PASS | Only `apex-flow-executor` is visible to `apex-executor`; 15 otherwise eligible bundled skills are excluded by the agent allowlist. |
| G3 in-process provider | BLOCKED | Required exact plugin version is unpublished; no substitute installed. |

## Diagnostic findings

1. The default OpenClaw workspace exceeded the 8K context gate. The dedicated minimal executor workspace reduced the prompt enough to run at 8K while preserving OpenClaw's fixed 4,096-token reserve.
2. With lazy tool mode enabled and the broad executor surface declared, Qwen mapped `session_status` to `exec {"command":"session_status"}`. Cautious exec policy did not execute it; the request remained blocked for approval and timed out. This is retained as a negative fixture.
3. With only the typed `session_status` tool exposed, the complete structured tool trajectory passed. Per-request tool shaping is therefore required; a broad always-visible operational surface is not acceptable for this 8B executor.
4. The Gateway currently runs in foreground-test mode and is healthy. The Windows Scheduled Task is deliberately not installed because the plan permits persistence only after the provider and capability gates pass.

## Current runtime state

- standalone `llama-server`: running, PID observed as `27564`
- foreground OpenClaw Gateway: running, Node PID observed as `45952`
- Gateway RPC/read probe: pass
- persistent Gateway service: not installed
- active model path: standalone llama.cpp provider
- cloud fallback: none
- active Qwen inference lanes: one

## Unexecuted work

The following remains blocked behind G3: in-process equivalence testing, production execution-request validator and wrappers, full per-request capability dispatch, Chrome profile/extension pairing, provider containment, script and disposable-Git gates, Cron gates, persistent Gateway installation, context promotion, subscription vertical slice, restart/idempotency testing, real recurring workflows, and deferred FEE reconciliation.

## Required operator decision

Either:

1. authorize reviewed plugin `@openclaw/llama-cpp-provider@2026.7.1`, whose declared peer range accepts the installed OpenClaw host; or
2. keep the exact-version rule and wait for a `2026.7.1-2` plugin publication.

No plugin substitution was made in this run.
