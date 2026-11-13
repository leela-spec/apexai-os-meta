---
type: Reference
id: APEX-INFRA-NATIVE-EXAMPLES
title: Inert Native Example Guide
description: Scope, provenance and interpretation limits for the proposed package artifacts.
status: draft
tags: [examples, compatibility, evidence]
---

# Inert native examples

Status: **proposed, not installed, no native host execution**.

- `hook_envelope_probe.py` only encodes a fixed delivery canary from fixture JSON. It is not an applicability router, validator, permission policy, or semantic evaluator.
- The `*.example.json` files show incompatible native containers and event names. They are not placed at active discovery paths. Antigravity explicitly disables its sample; Claude/Gemini disable hooks in settings. The Codex sample is paired with `codex-config.example.toml`, which disables hooks.
- Replace interpreter/path placeholders only in a disposable test copy after authorization. Enabling a handler is a separate integration action, not part of this research run.
- The agent Markdown and TOML files show native metadata for the same review role. The Codex file expresses read-only behavior as an instruction; its parent sandbox must supply actual isolation. No definition is installed in a native agent folder.
- No portable `SKILL.md` is installed by these examples. The root design package owns skill/reference composition and canonical rule IDs.
- `offline-results.json` and `codex-offline-results.json` establish only package behavior, shape checks, and a narrow proposed semantic allowlist. Native invocation, actual context delivery, tool denial, recovery and adherence remain unexecuted.

## Reproduce the offline checks

From this directory, run `python offline_check.py` and `python codex_offline_check.py`. They write their corresponding result JSON files. Python 3.11+ and the `jsonschema` package are required for the second command; tested dependency versions appear in its result. Neither command starts an agent host or installs configuration. The first uses only the Python standard library.

`codex-hook-fixtures.json` contains valid injection/denial examples and deliberately invalid examples. Do not deploy fixtures. The released wire schema accepts some outputs that the opened runtime documentation rejects; both shape and semantic gates must pass. `codex_hook_probe.py` emits a denial only for the fixed invented `APEX_PROBE_DENY` marker. It does not implement a production policy.

For a future native probe, resolve absolute interpreter/script paths in a disposable copy, choose the intended surface and version, review the exact hook definitions, and follow the relevant case in `../../compatibility/probe-plan.json`. This step requires deployment authorization and was not performed here.

Evidence: [Codex hooks](https://learn.chatgpt.com/docs/hooks), [pinned schemas](../../compatibility/native-schemas/codex/README.md), [Claude hooks](https://code.claude.com/docs/en/hooks), [Antigravity hooks](https://antigravity.google/docs/hooks), [Gemini hook reference](https://geminicli.com/docs/hooks/reference/), [Claude agents](https://code.claude.com/docs/en/sub-agents), [Antigravity agents](https://antigravity.google/docs/subagents/).
