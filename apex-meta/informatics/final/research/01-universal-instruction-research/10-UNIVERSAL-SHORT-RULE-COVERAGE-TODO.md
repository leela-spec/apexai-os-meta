---
type: ProgramTodo
title: Universal AI Instruction System — Short-Rule Coverage TODO
description: Final-synthesis checklist of high-value behavioral controls that must be covered, merged, or explicitly rejected before live propagation.
status: active_todo
created: 2026-09-07
---

# Universal AI Instruction System — Short-Rule Coverage TODO

## Purpose

Before the Universal AI Instruction System is propagated into live `AGENTS.md` / equivalent runtime instructions, verify that every high-value control below is either:

- covered by a completed module;
- deliberately merged into another module;
- represented by a conditional module / deeper method;
- or explicitly rejected with evidence.

Do not optimize for module count. Optimize for reliable agent behavior with the smallest sufficient always-loaded surface.

## Ranked coverage checklist

| Rank | Control | Current / likely owner | State | Final synthesis question |
|---:|---|---|---|---|
| 1 | Substantive outcome over proxy/checkmark | A01 `<target>` | COVERED | Does the agent realize the useful outcome rather than merely passing tests/files/checklists? |
| 2 | External reality grounding | proposed A13 `<grounding>` | TODO | Are material real-world claims/decisions verified externally instead of canonized from model reasoning alone? |
| 3 | Battle-proven reuse before invention | A03 `<reuse>` | COVERED / STRENGTHENING PENDING | Does the agent reuse proven systems near their established form and confine invention to verified gaps? |
| 4 | Scope / non-goals without under-delivery | A02 `<scope>` | COVERED | Does scope control stop adjacent work without forcing shallow realization? |
| 5 | Action authorization / side-effect boundary | proposed A14 `<authority>` | TODO | Is an in-scope action also authorized at execution time before durable/external/consequential effects? |
| 6 | Browser/subscription-model repository mutation boundary | proposed C04 `<mutation>` | TODO | Do online models propose bounded patches/change instructions instead of rewriting existing repository files through whole-file connector updates? |
| 7 | Read-before-change / current-state binding | C04 / A11 | TODO | Is every mutation proposal based on current authoritative file state? |
| 8 | Fail closed on stale / ambiguous mutation | C04 / A10 | TODO | Does a mismatch trigger re-read/regeneration rather than improvised editing? |
| 9 | Post-mutation diff / result verification | C04 / A01 / A07 | TODO | Is the actual resulting change inspected and validated before completion? |
| 10 | Intent clarification threshold | A05 `<intent>` | IN PROGRAM | Does the agent resolve discoverable ambiguity and escalate only material uncertainty? |
| 11 | Current truth / single authoritative state | A11 `<current_truth>` | QUEUED | Does the agent use current authority rather than stale history or duplicated state? |
| 12 | Context minimization / progressive disclosure / JIT | A06 `<context>` | QUEUED | Does the agent keep active context small and load deeper material only when relevant? |
| 13 | Complexity-adaptive execution | A04 `<workflow>` | COVERED | Does workflow rigor scale with complexity/uncertainty/consequence rather than habit? |
| 14 | Top-down realization / bottom-up verification-validation | A07 `<realization>` | QUEUED | Does decomposition preserve parent intent and does integration validate upward? |
| 15 | Evidence authority / provenance / freshness / uncertainty | A08 `<evidence>` | QUEUED | Are load-bearing claims source-grounded with uncertainty preserved? |
| 16 | Retry / replay / idempotency safety | A10 or conditional effect-safety module | TODO / DECIDE OWNER | Can retries/resumes avoid duplicate durable effects? |
| 17 | Narrow recovery without redesign | A10 `<recovery>` | QUEUED | Does incidental failure recovery preserve target/scope without spawning architecture? |
| 18 | Material decision / trade-study discipline | C01 `<decision>` | QUEUED | Are real alternatives compared with evidence and rejection reasons when operator choice matters? |
| 19 | Research execution / source hierarchy / triangulation | C02 `<research>` | QUEUED | Is deeper research performed rigorously without becoming universal ceremony? |
| 20 | Communication economy / exception reporting | A12 `<communication>` | QUEUED | Are material findings surfaced without routine internal narration and ceremony? |

## Pending architecture decisions

### A13 — External Grounding & Real-World Verification

Candidate role: require external verification when material decisions depend on real-world facts, capabilities, methods, integrations, standards, maturity, support, or reliability. Keep distinct from A08 evidence quality and C02 research method unless later synthesis proves a merge is cleaner.

### A14 — Action Authorization / Side-Effect Boundary

Candidate role: distinguish task scope from permission to perform durable, external, destructive, privileged, or consequential actions. Research whether this belongs as a universal invariant or should be partly conditional.

### C04 — Repository Mutation / Patch Handoff

Candidate role: online/browser subscription models should not directly rewrite existing repository files through whole-file connector mutation. Preferred reference format for the handoff: **Aider `editor-diff` / SEARCH-REPLACE blocks**. A separate authorized editor/executor applies and verifies the change.

### Retry / idempotency ownership

Do not create another module automatically. During A10 / final synthesis, decide whether replay/idempotency safety belongs under recovery, authority, mutation, or a separate conditional effect-safety module.

## Final synthesis gate

The program must not enter live propagation until:

1. every row above is `COVERED`, `MERGED`, or `REJECTED WITH EVIDENCE`;
2. neighboring-module overlaps are resolved;
3. root wording remains within the intended compact always-loaded budget;
4. conditional/deep behaviors are routed rather than duplicated in the root;
5. cross-agent evaluation tests the highest-risk interactions, especially A01+A03+A13, A02+A14, A11+C04, and A10+C04;
6. the final contract is checked for both under-control and over-control failure modes.

## Research note on patching

There is no single universal edit syntax across all coding agents. OpenAI exposes structured `apply_patch`; Claude uses exact-string editing; Aider supports multiple model-specific edit formats. For web-chat/subscription-model handoff specifically, Aider documents an architect/editor workflow and recommends `editor-diff` or `editor-whole`; `editor-diff` is the preferred patch-style reference to evaluate for this project.
