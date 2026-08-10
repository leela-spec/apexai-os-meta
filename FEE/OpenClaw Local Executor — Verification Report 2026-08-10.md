---
title: "OpenClaw Local Executor — Verification Report 2026-08-10"
doc_type: verification_report
initiative: local-executor
created: 2026-08-10
status: in-progress-standalone-provider-selected
canonical_plan: FEE/OpenClaw Local Executor — Installation and Implementation Plan.md
canonical_decision: FEE/OpenClaw Local Executor — Operator Decision Lock.md
---

# OpenClaw Local Executor — Verification Report 2026-08-10

## Current status

The operator authorized continuation with the already-passing standalone llama.cpp endpoint as the production generation topology. The in-process comparison gate is closed as a documented capability mismatch, not left blocking: the official compatible plugin is embeddings-only, while the standalone provider passes both normal and structured-tool OpenClaw trajectories.

The bounded execution-request validator and safety wrappers are now implemented test-first. Their 34-test suite covers the valid contract, fail-closed schema and authority checks, hashed and read-locked script/executable identity, reviewed-identity exact-argv commands, bounded Git status/diff/add/commit, a bound origin identity and exact main refspec, disabled commit/pre-push hooks, sanitized Git configuration and environment, rename-source containment, versioned guard deployment, and branch/path/message/fetch-URL/push-URL denials in disposable repositories.

The original in-process finding remains relevant. The plan requested a generative provider able to run the Qwen GGUF and return chat tool calls. The operator authorized the compatible published plugin `@openclaw/llama-cpp-provider@2026.7.1` after npm confirmed that `2026.7.1-2` does not exist.

The installed plugin is not a generative provider. Its manifest describes `Local GGUF embeddings through node-llama-cpp`, registers only `embeddingProviders: ["local"]`, exposes no model provider IDs, and its implementation calls `registerEmbeddingProvider` only. It cannot supply the researched `local://llama-cpp` Qwen chat path.

Published plugin state at the stop:

- latest stable: `2026.7.1`
- extended stable: `2026.6.34`
- beta: `2026.7.2-beta.7`
- latest stable peer requirement: `openclaw >=2026.7.1`
- installed plugin: `@openclaw/llama-cpp-provider@2026.7.1`, pinned and loaded
- installed plugin capability: local GGUF embeddings only

The host remains `OpenClaw 2026.7.1-2 (0790d9f)`. The version-policy deviation was explicitly approved; no unreviewed package or cloud provider was introduced.

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
| G3 provider selection | PASS WITH DOCUMENTED DEVIATION | Authorized plugin `2026.7.1` implements embeddings only. Operator selected the passing standalone llama.cpp endpoint as production generation topology; cloud fallback remains prohibited. |
| Bounded request validator | PASS | Versioned closed-world request schema validates immutable prompt hashes, roots/modes, tools, exact scripts and commands, Git authority, success criteria, stop conditions, result path, and evidence directory. |
| Script and command safety wrappers | PASS | Exact declared executable/script/argv fixtures executed by ID; identities are hashed, reparse paths rejected, and files read-locked through execution. Scripts require read-only roots; command grants require a reviewed executable hash. The pinned packaged Python runtime is hashed and read-locked while validating. |
| Git safety wrapper | PASS | Disposable-repository status/diff/add/commit and bound-origin main push passed. Hooks, fsmonitor, external diff/text conversion, signing, unsafe protocols, URL rewrites, executable local config, and Git execution environment overrides are blocked or sanitized. Work-tree root, sole fetch/push URL, branch, commit message, staged rename source/destination paths, Git binary, and credential helper identities are independently rechecked. |
| Guard deployment | PASS | Versioned identity `ba69b1ac5103fe40572a86ff4df0c106372ea2cecbb274dcc13b13c5dae30759` is installed at `C:\ProgramData\ApexExecutor\guards\guards-v1-ba69b1ac5103fe40`. Root, version, and manifest are Administrators-owned; the executor user has only RX/Synchronize. All manifest hashes match, and non-elevated file-creation probes in both root and version were denied. Interrupted ACL installation was recovered idempotently without overwriting guard bytes. |

## Diagnostic findings

1. The default OpenClaw workspace exceeded the 8K context gate. The dedicated minimal executor workspace reduced the prompt enough to run at 8K while preserving OpenClaw's fixed 4,096-token reserve.
2. With lazy tool mode enabled and the broad executor surface declared, Qwen mapped `session_status` to `exec {"command":"session_status"}`. Cautious exec policy did not execute it; the request remained blocked for approval and timed out. This is retained as a negative fixture.
3. With only the typed `session_status` tool exposed, the complete structured tool trajectory passed. Per-request tool shaping is therefore required; a broad always-visible operational surface is not acceptable for this 8B executor.
4. The Gateway currently runs in foreground-test mode and is healthy. The Windows Scheduled Task is deliberately not installed because the plan permits persistence only after the provider and capability gates pass.
5. Current OpenClaw package documentation and installed code do not support the research plan's generative `local://llama-cpp` assumption. This is an architecture-input error, not a Qwen, llama.cpp, browser, skill, or configuration failure.

## Current runtime state

- standalone `llama-server`: running, PID observed as `27564`
- foreground OpenClaw Gateway: running, Node PID observed as `45952`
- Gateway RPC/read probe: pass
- persistent Gateway service: not installed
- active model path: standalone llama.cpp provider
- llama.cpp plugin: installed for embeddings only; not selected for generation
- cloud fallback: none
- active Qwen inference lanes: one

## Remaining work

Full per-request capability dispatch, Chrome profile/extension pairing, provider containment, Cron gates, persistent Gateway installation, context promotion, subscription vertical slice, restart/idempotency testing, real recurring workflows, and deferred FEE reconciliation remain. The installed embedding plugin will not be configured as a chat provider; no in-process generative substitute or cloud fallback will be introduced.
