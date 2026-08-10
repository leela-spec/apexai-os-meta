---
title: "OpenClaw Local Executor — Verification Report 2026-08-10"
doc_type: verification_report
initiative: local-executor
created: 2026-08-10
status: in-progress-bounded-immediate-dispatch-verified
canonical_plan: FEE/OpenClaw Local Executor — Installation and Implementation Plan.md
canonical_decision: FEE/OpenClaw Local Executor — Operator Decision Lock.md
---

# OpenClaw Local Executor — Verification Report 2026-08-10

## Current status

The operator authorized continuation with the already-passing standalone llama.cpp endpoint as the production generation topology. The in-process comparison gate is closed as a documented capability mismatch, not left blocking: the official compatible plugin is embeddings-only, while the standalone provider passes both normal and structured-tool OpenClaw trajectories.

The bounded execution-request validator, safety wrappers, protected runtime installer, and immediate dispatcher are now implemented test-first. The current 49-test helper suite covers the valid contract, fail-closed schema and authority checks, hashed and read-locked script/executable identity, reviewed-identity exact-argv commands, bounded Git status/diff/add/commit, protected immutable installations, request freezing, idempotency conflicts, evidence tampering, symlink and hard-link attacks, post-copy reparse rejection, exact OpenClaw configuration restoration, and recovery serialization. The three tests that invoke the live Gateway are opt-in; they have also passed separately against the protected runtime.

Immediate model dispatch is intentionally limited to the exact OpenClaw tools `browser`, `read`, `write`, and `session_status`. Model-visible process, script, command, and Git grants remain fail-closed until their exact approval integration exists. The dispatcher freezes the validated request and prompt, uses request-derived sessions, serializes active configuration changes with a machine-wide mutex and recovery journal, restores the original configuration bytes, and creates independently hashable evidence through retained no-delete, no-write handles.

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
| Repository checkpoint before this report update | `325b71d4810ba6676b03c9bdaf7cc2dea35c9831` |
| OpenClaw | `2026.7.1-2 (0790d9f)` |
| Node | `v24.18.0` |
| Active config SHA-256 | `68791DB12C3ED537951DB1613757432720399FE0771413EAF03A4104D3104668` |
| Qwen GGUF SHA-256 | `D98CDCBD03E17CE47681435B5150E34C1417F50B5C0019DD560E4882C5745785` |
| llama-server launcher SHA-256 | `63E7ED32203FC90DF3DF42FCC42762B988446E0D66B786ADB9AD059FA3CE2819` |
| Gateway | loopback `127.0.0.1:18789`, token SecretRef from user environment |
| Standalone model endpoint | loopback `127.0.0.1:8090` |
| Evidence timestamp | `2026-08-10T21:33:18.8593565+02:00` |

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
| Protected OpenClaw runtime | PASS | Exact OpenClaw `2026.7.1-2` and its Node runtime are installed as immutable identity `38f1eec9e8e5c087567ef21a16304a6a544921551580f5b017305305a9aa9fa1` at `C:\ProgramData\ApexExecutor\runtime\openclaw-2026.7.1-2-38f1eec9e8e5c087`. The manifest covers all 32,079 files and attests ACL policy `admin-system-full-operator-rx/v1`; the operator has only RX/Synchronize. |
| Immediate dispatcher | PASS | Preparation, idempotent replay, conflict rejection, prompt/message freezing, evidence tamper rejection, child-symlink and hard-link rejection, bounded failure capture, live local-Qwen execution, exact config restoration, interrupted-config recovery, and concurrent recovery serialization passed. Model dispatch rejects exec/script/command/Git grants pending their approval bridge. |
| Guard deployment | PASS | Protected identity `cb8060f57d2525065b9a8fd29bd7967f145ef03216334c66ffd0341cc323c9d0` is installed at `C:\ProgramData\ApexExecutor\guards\guards-v1-cb8060f57d252506` with exact protected ACLs, matching manifest hashes, and exact equality to checkpoint `cffd1367`. The deployed dispatcher binds to its co-located manifest and validator. |
| Post-change regression | PASS | 49 OpenClaw helper tests passed with 3 live integrations explicitly skipped in the default run; 32 FEE tests and 177 LMBench tests passed; every OpenClaw PowerShell file parsed cleanly. All 11 dispatcher tests then passed through the protected `cb8060f5...` identity with live integration enabled, including real Qwen execution, exact configuration restoration, interrupted-config recovery, and concurrent recovery serialization. Independent final review found no remaining Critical or Important issues and approved deployment. |
| Chrome extension pairing and selected-tab containment | PASS | The official extension bundled with the protected runtime paired over loopback relay port `18799` in an isolated Chrome data directory. Its manifest has no host permissions and no `<all_urls>` grant. Before sharing, OpenClaw saw zero tabs. After the operator explicitly shared `https://example.com/`, OpenClaw saw exactly one tab and captured its accessibility snapshot. After **Stop sharing this tab**, visibility returned to zero while the relay remained healthy and attach-only. |

## Diagnostic findings

1. The default OpenClaw workspace exceeded the 8K context gate. The dedicated minimal executor workspace reduced the prompt enough to run at 8K while preserving OpenClaw's fixed 4,096-token reserve.
2. With lazy tool mode enabled and the broad executor surface declared, Qwen mapped `session_status` to `exec {"command":"session_status"}`. Cautious exec policy did not execute it; the request remained blocked for approval and timed out. This is retained as a negative fixture.
3. With only the typed `session_status` tool exposed, the complete structured tool trajectory passed. Per-request tool shaping is therefore required; a broad always-visible operational surface is not acceptable for this 8B executor.
4. The Gateway currently runs in foreground-test mode and is healthy. The Windows Scheduled Task is deliberately not installed because the plan permits persistence only after the provider and capability gates pass.
5. Current OpenClaw package documentation and installed code do not support the research plan's generative `local://llama-cpp` assumption. This is an architecture-input error, not a Qwen, llama.cpp, browser, skill, or configuration failure.
6. Protected guard identity `7db272b3...` rejected dispatch before request execution because two immutable guard versions contained the same pinned validator bytes. No model turn or configuration mutation occurred. Discovery now binds deployed dispatchers to the sibling validator named by their own manifest; repository-source diagnostics accept multiple byte-identical pinned validators and choose deterministically. Independent security review approved the correction.

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

Provider authentication and one-tab-at-a-time provider containment are the next checkpoint. Browser hostile-page tests, Cron gates, persistent Gateway installation, context promotion, the subscription vertical slice, cross-stage restart/idempotency testing, real recurring workflows, and deferred FEE reconciliation remain. The installed embedding plugin will not be configured as a chat provider; no in-process generative substitute or cloud fallback will be introduced.
