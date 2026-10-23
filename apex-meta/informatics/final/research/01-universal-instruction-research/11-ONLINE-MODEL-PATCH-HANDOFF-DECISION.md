---
type: ArchitectureDecisionCandidate
title: Online Subscription Model Repository Patch Handoff
description: Candidate mutation boundary for browser/subscription models connected to repositories through whole-file GitHub connectors.
status: candidate_pending_module_integration
created: 2026-09-07
---

# Online Subscription Model Repository Patch Handoff

## Decision candidate

For online/browser subscription models whose connected repository tool rewrites complete existing files rather than applying localized edits:

> Existing repository files are **patch-proposal only**. The online model must not directly rewrite an existing file through the connector. A separate authorized editor/executor applies and verifies the requested change.

Explicit creation of a genuinely new file may remain separately authorized because it does not overwrite existing file content.

## Preferred patch-style reference

**Aider `editor-diff` / SEARCH-REPLACE blocks**.

Do not treat this as a universal industry syntax. It is the current preferred reference for this browser-model -> editor/executor architecture because Aider explicitly supports web-chat models as architecture/reasoning clients with a separate file editor.

## Candidate module

- **ID:** C04
- **Tag:** `<mutation>`
- **Role:** Repository Mutation / Patch Handoff
- **Activation:** when an online/browser subscription model proposes changes to existing repository files.

Candidate compact rule:

```xml
<mutation when="an online or browser subscription model proposes changes to existing repository files"
          principles="patch-handoff,read-before-change,fail-closed">
  Do not rewrite existing repository files directly through whole-file connector updates. Emit bounded patch/change instructions for a separate authorized editor/executor to apply against current state and verify the resulting diff; on mismatch, re-read and regenerate rather than improvise.
</mutation>
```

This wording is provisional and must be researched/tested during C04 deepening before live propagation.

## Verified architecture observations

- The ChatGPT GitHub connector available to this project exposes existing-file updates as complete replacement content rather than native localized `git apply`/patch execution.
- OpenAI's coding API exposes a structured `apply_patch` tool, but that is a different execution environment from this ChatGPT GitHub connector.
- Claude Code uses exact-string editing rather than one universal patch syntax.
- Aider deliberately supports multiple edit formats because models differ in edit-format reliability.
- Aider documents a browser/web-chat workflow in which the web model acts as the higher-level architect and a separate editor model applies changes; `editor-diff` / `editor-whole` are the recommended editor formats for that workflow.

## Guardrail

Do not infer from the existence of `git apply`, OpenAI `apply_patch`, Claude Edit, or another local coding-agent feature that the same operation exists through a browser subscription model's connected GitHub interface. Tool capability must be verified for the actual execution surface before designing the workflow around it.
