---
type: Handover
id: HANDOVER-13-CROSS-CLI-HOOKS
title: Handover 13 — Cross-CLI Hook Architecture & Multi-Repo Organization
description: Research handover synthesizing Round 2 empirical validation findings and tasking downstream investigation of Antigravity, Claude Code, and Codex hook architectures across repositories.
status: current
tags: [informatics, handover, hooks, cross-cli, antigravity, claude-code, codex, em-14]
---

# Handover 13: Cross-CLI Hook Architecture & Multi-Repository Organization

## At a Glance

- **Part of**: [Master Index](../../index.md) and [Ultra Upgrade Validation Bundle](../../research/10-ultra-upgrade-validation/index.md).
- **Preceding Milestone**: [HANDOVER-12](HANDOVER-12-TEST-UPGRADED-CONTRACT-AND-ALIGNMENT-ARMS.md) and [Round 2 Results](../../research/10-ultra-upgrade-validation/01-results-and-verdict.md).
- **Core Directive**: Keep the ratified XML contract (`apex_contract_v1.0_ultra.xml`) unchanged as the universal constitution. Investigate how native hooks across Antigravity, Claude Code, and Codex enforce boundaries without burning tokens.

---

## 1. Accomplished Work: 5-Component Forensic Summary

### 1.1 Observation
- Completed `14` `r0-agy` calibration runs and `99` pre-registered batch runs (`n=5` / `n=3`) on `gemini-3.8-flash-low` under `C:/tmp/apex-eval/`.
- `Arm A` (`v1.0-ultra` XML in markdown only) achieved `18 / 33` (`54.5%`, Wilson `95%` `[0.38, 0.70]`).
- `Arm B-AGY` (XML contract + doorway hooks) achieved **`31 / 33` (`93.9%`**, Wilson `95%` `[0.80, 0.98]`, exact McNemar **`p = 0.002350`**).
- `Arm D` (`<deliberation>`) scored `17 / 33` (`51.5%`) and produced `0` `thinking_tokens` on `gemini-3.8-flash-low`.
- Zero eval files or git branches were modified in live repositories (`C:/GitDev/apexai-os-meta`, `mindful-bar`, `Leela-Cloud-2026`).

### 1.2 Logic Chain
- Contract rules alone cannot physically prevent an agent from invoking a write tool before reading required specs.
- On `T1`, all five `Arm A` runs skipped reading `handover.md` because the user prompt said *"right away"*.
- In `Arm B-AGY`, `PreToolUse` caught premature write attempts before disk mutation, forcing the agent to read `handover.md` first.
- For `T6` and `T7`, git isolation and pushing succeeded across all arms (`30 / 30`).
- Omitting the word *"continuation"* in user prompts caused `Arm A` to drop the 6-field format in `20 / 20` runs.
- Concise action reminders prevented this drop (`10 / 10`), proving that un-cued close-outs require distinct visibility.

### 1.3 Caveats
- Global `~/.gemini/GEMINI.md` loads unconditionally in Antigravity (`15,928` Turn 1 tokens), preventing isolated runs of stripped `Arm C`.
- Antigravity hooks caused minor over-skepticism during open-ended planning in `T3` (`3 / 5` pass rate).
- Native hook support differs across coding CLIs: Antigravity and Claude Code support pre-tool hooks; Codex CLI currently relies on git-level hooks and execution sandboxes.

### 1.4 Conclusion
- Do not rewrite the 23-rule XML constitution into loose markdown bullets.
- Do not maintain duplicate text rules at the bottom of instruction files.
- Move hard invariant enforcement (spec pre-reads, dirty git staging) into native runtime hooks.
- Refine `<handover>` wording to clarify that any final task summary constitutes a continuation step.

### 1.5 Verification Method
- Benchmark traces and scoring logs reside in `C:/tmp/apex-eval/scores-batch-agy.csv`.
- Rerun evaluation scoring:
  ```bash
  python apex-meta/informatics/final/research/10-ultra-upgrade-validation/score_eval.py --harness agy
  ```
- Run bundle validation:
  ```bash
  python apex-meta/informatics/final/tools/okf_validator.py --target apex-meta/informatics/final
  ```

---

## 2. Dimensional Handover Contract for Downstream AI

### 2.1 Input & Priority Ledger
1. **Primary Authority**:
   - [01-results-and-verdict.md](../../research/10-ultra-upgrade-validation/01-results-and-verdict.md): Settled empirical findings from the 99-run benchmark.
   - [armB_hook_agy.py](../../research/10-ultra-upgrade-validation/fixtures/armB_hook_agy.py): Working Antigravity lifecycle hook reference implementation.
   - [apex_contract_v1.0_ultra.xml](../../specs/apex_contract_v1.0_ultra.xml): Canonical Layer 1 contract.
2. **Workstation Environment & CLI Specs**:
   - Antigravity hook reference: `~/.gemini/antigravity/builtin/skills/agy-customizations/docs/hooks.md`.
   - Claude Code settings reference: `.claude/settings.json` hook schemas (`PreToolUse`, `Stop`, `UserPromptSubmit`).
   - Codex CLI execution model: Windows native execution under `c:\GitDev\`, sandbox flags, and git hook lifecycle.
3. **Repository Targets**:
   - `c:\GitDev\apexai-os-meta`: Meta-operating repository, governance tools, and shared contracts.
   - `c:\GitDev\mindful-bar`: Commercial product codebase with vendored Apex carrier.
   - `c:\GitDev\Leela-Cloud-2026`: Cloud application with Python gates runner and master branch workflow.

### 2.2 Process & Investigation Tasks
The downstream AI must execute three concrete analysis tasks:

- **Task 1: Cross-CLI Hook Compatibility Audit**
  - Map the hook lifecycle across Antigravity, Claude Code, and Codex CLI.
  - Determine what events each tool natively supports (`PreToolUse`, `PostToolUse`, `PreInvocation`, `Stop`).
  - Document fallback strategies for tools lacking native tool-level interception (such as git-level hooks or MCP middleware).

- **Task 2: Repository Hook Organization Architecture**
  - Design a unified directory layout for hook scripts across repositories (such as `.agents/hooks/` versus `.claude/hooks/`).
  - Determine whether hook logic can share a single portable Python script across Antigravity and Claude Code.
  - Specify how `apex_carrier_sync.py` or vendor drift tools should manage and update hook configurations.

- **Task 3: Operational Guardrails Specification**
  - Define the minimal set of checks delegated to hooks (such as blocking `git add -A` and enforcing spec reads before modifying `final/`).
  - Ensure hook scripts execute in under `50ms` and require zero network access.
  - Ensure hook failures provide actionable, single-sentence guidance without infinite retry loops.

### 2.3 Expected Deliverables & Output
Produce a comprehensive architectural specification at:
`apex-meta/informatics/final/specs/cross-cli-hook-architecture.md`

The document must contain:
1. Matrix comparing Antigravity, Claude Code, and Codex hook triggers.
2. Portable hook file layout for multi-repository deployments.
3. Reference command configuration for `.agents/hooks.json` and `.claude/settings.json`.
4. Fallback strategy for Codex CLI using git hooks (`.git/hooks/pre-commit`).
5. Concrete rollout roadmap for `apexai-os-meta`, `mindful-bar`, and `Leela-Cloud-2026`.

### 2.4 Definition of Done (DoD)
- The specification conforms to OKF v0.2 frontmatter and passes `okf_validator.py` with zero errors.
- Every hook configuration uses documented CLI parameters verified against local installations.
- Hook scripts run cross-platform on Windows 11 host without requiring Docker or elevated privileges.
- All real repositories remain clean with zero unauthorized file mutations.

---

## 3. Major Step Close-Out & Continuation (`EM-14`)

- **Goal**: Persist completed Round 2 validation work to `origin/main` and initialize the cross-CLI hook architecture specification.
- **Input**: Local commit history (`9517bedd..HEAD`), [01-results-and-verdict.md](../../research/10-ultra-upgrade-validation/01-results-and-verdict.md), and [HANDOVER-13](HANDOVER-13-CROSS-CLI-HOOK-ARCHITECTURE-AND-REPOSITORY-ORGANIZATION.md).
- **Process**: Execute scoped git stage, commit, and push; verify remote tracking alignment; update master index.
- **Skills**: `none`
- **Output**: Pushed `main` branch containing Round 2 deliverables and indexed Handover 13.
- **Redraft**:
  - `Given` 9 local commits ahead of `origin/main`,
  - `When` git push completes on `main`,
  - `Then` the remote repository reflects all empirical validation findings and Handover 13 is ready for downstream execution.
