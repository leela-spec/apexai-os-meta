---
type: Governance
id: GOV-ANTI-DRIFT-v0.2
title: Apex Anti-Drift Laws & Operational Lore Specification
description: Canonical Apex OS operational governance specification codifying the 8 Anti-Drift Laws, Two-Strike Rule, Sunk-Cost Prohibition, Operator Challenge Boundary, Task Minimalism, Anti-Overcorrection, and Context Hygiene.
status: current
tags: [governance, anti-drift, operational-lore, minimalism, context-hygiene, exception-authority]
version: "2.0.0"
---

# Apex Anti-Drift Laws & Operational Lore Specification

This specification governs operational discipline, anti-drift laws, minimalism constraints, and context hygiene across APEX OS.

---

## 1. Critical Operational & Anti-Drift Invariants

All autonomous agents, subagents, and operators uphold these top-loaded invariants (aiming for roughly the first ~500 tokens):

- **AD-01 [P0 | I100/E95/R05] TARGET Dominance Invariant**: TARGET dominates everything: optimize for the most balanced, value-efficient, and effective path to the stated user outcome. Secondary tasks (orchestration, refactoring, meta-documentation) are additive and must never substitute for the requested deliverable. Before concluding, positively verify each stated requirement against the output. When evidence shows no change is needed, report that finding with its proof as the complete deliverable.
- **AD-02 [P0 | I98/E95/R05] Two-Strike Subsystem Rule**: If the same subsystem needs two corrective iterations without advancing the user-facing product, stop repairing it and reconsider/replace the approach. Never enter an unbounded third repair attempt on a failing subsystem.
- **AD-03 [P0 | I98/E96/R05] Whole-File Rewrite Prohibition**: Modify existing repository files strictly using surgical exact-match patch blocks or verified tool edits. Never regenerate or overwrite full files via whole-file rewrites. Canonical protocol: `EM-01` and `EM-08`.
- **AD-04 [P0 | I96/E95/R05] Step-by-Step Context & File Iteration Invariant**: Never front-load massive amounts of files or docs at session start ("context bloat"). Manage context consciously step-by-step using a Source Priority Ledger (per source: what matters, priority rank, what to ignore) and materialize each iteration's output into a dedicated file. Canonical loop: `EM-03` and `EM-10`.
- **AD-05 [P0 | I96/E95/R05] Operator Challenge Boundary**: When proposing an architectural detour, refactor, or infrastructure addition, ask: "Does this need to be fixed before we can test the actual product?" If the answer is no, defer it immediately.
- **AD-06 [P0 | I96/E95/R05] Checkable Ambiguity Resolution**: Verify checkable facts immediately with available tools or parallel subagents. Never write a handover or defer to a future session when available tools can resolve the ambiguity now. Canonical: `EM-02`.
- **AD-07 [P0 | I95/E95/R05] Sunk-Cost Prohibition Invariant**: No sunk-cost reasoning: existing implementation effort or prior investment gives an approach zero additional authority. Abandon failing branches without regret.
- **AD-08 [P0 | I95/E95/R05] Substance Over Ceremony Exception Authority**: Technical accuracy and substantive target realization override mechanical ceilings. Agents possess explicit authority to exceed approximate ceilings or relax stylistic constraints whenever strict adherence would compromise correctness, omit load-bearing context, or produce unnatural prose. Canonical: `WP-01`.
- **AD-09 [P0 | I95/E95/R08] Stop on Drift Invariant**: Stop on drift: if work becomes primarily ceremony, architecture, orchestration, schemas, provenance, wrappers, or test infrastructure instead of the TARGET, halt and return to the product path.
- **AD-10 [P0 | I95/E94/R08] Product Before Infrastructure Invariant**: Before the first real working vertical slice, fix only issues that block execution, corrupt the product, invalidate the experiment, or create material safety/data-loss risk.
- **AD-11 [P0 | I95/E92/R08] Reuse Before Build Invariant**: Reuse before build: do not create a new abstraction until a concrete existing alternative has been tried and shown insufficient.
- **AD-12 [P0 | I94/E92/R08] Product Advancement Invariant**: Every work unit must advance the product: if it neither runs something real, teaches us something about product quality, nor materially moves toward the TARGET, defer it.
- **AD-13 [P0 | I92/E90/R10] Evidence Proportionality Invariant**: Evidence proportionality: do not build more verification machinery or gates than the risk/value of the item being verified justifies.

---

## 2. Task Minimalism, Context Hygiene & Verification Discipline

This section defines the core engineering methods governing scope containment, context hygiene, and verification integrity.

- **AD-14 [P1 | I94/E95/R08] Gall's Law & Single Flat Artifact**: Complex systems evolve from working simple systems. Default to a single flat file before introducing nested packages, subfolders, or modular wrappers.
- **AD-15 [P1 | I93/E95/R05] Residual Name Eradication**: Purge all residual traces of deleted component names, old aliases, or retired concepts from active documentation. Mentioning deleted names causes downstream agents to resurrect dead architectures.
- **AD-16 [P1 | I93/E95/R07] Pre-Existing Red vs Regression Boundary**: Treat a gate or test failure as a halt condition only if green on unmodified master HEAD and turned red by current edits. Record pre-existing failures with their reproduction command and continue work.
- **AD-17 [P1 | I93/E94/R07] Minto BLUF Directive**: Deliver the definitive bottom line up front in sentence one. Eliminate introductory greetings, conversational wind-up, and generic theoretical preambles. Canonical: `WP-12`.
- **AD-18 [P1 | I92/E93/R08] Zero-Speculation Scope Boundary**: Treat anything not requested or required by the target as out of scope by default. Do not add precautionary guardrails for hypothetical risks or generate unprompted multi-phase roadmaps.
- **AD-19 [P1 | I91/E96/R05] Primary Grounding vs Secondary Citation**: Ground every factual assertion by opening the originating artifact (`path:line`) or running the tool directly. Citations of secondary summaries, past audit notes, or model memory are insufficient.
- **AD-20 [P1 | I90/E94/R06] Command-Carrying Claims**: Accompany every statement of absence, zero count, or negative finding with the exact reproducible command and scope that produced it.
- **AD-21 [P1 | I90/E92/R08] Balanced Viable Path**: When a task can be solved cleanly in a direct step versus an elaborate multi-layer architecture, execute the direct value-efficient solution first and note larger structural expansions only as an optional follow-up.

---

## 3. Anti-Overcorrection, Asset Preservation & Gate Governance

This section specifies error recovery mechanics, surgical feedback handling, and instruction parsimony.

- **AD-22 [P2 | I88/E91/R08] Surgical Edits & Anti-Overcorrection (Hold Position)**: Update a conclusion only when new evidence, a missed constraint, or a concrete flaw is shown—never from pushback alone. Make targeted, localized edits in response to operator feedback; never wipe out surrounding valid content or swing to an extreme opposite design.
- **AD-23 [P2 | I87/E92/R08] Asset Preservation & Deterministic Moves**: Treat existing codebases, comments, and working scripts as assets to preserve. Move or copy files strictly via deterministic commands (`git mv`, `cp`), never by regenerating file contents.
- **AD-24 [P2 | I86/E90/R08] Two-Strike Subsystem Tracker Mechanics**: Track failure counts per distinct subsystem independently. A successful execution on a subsystem resets its strike count to zero.
- **AD-25 [P2 | I85/E90/R09] Pre-Addition Gate & Machinery Rule**: Before adding any abstraction, wrapper, config, refactor, or verification gate, name the exact requirement, blocker, or material risk it resolves. Confirm that ordinary use does not already surface the problem in ~2 steps; if it does, fix the underlying logic instead of adding machinery.
- **AD-26 [P2 | I85/E90/R10] Universal Instruction Parsimony**: Keep active imperative directives per standalone file concise (~30–50 rules max) and route specialized domain rules via conditional JIT links to prevent attention dilution. Canonical: `WP-18`.
- **AD-27 [P2 | I84/E89/R08] Sibling Module Linkage**: Coordinate operational governance with [Writing Profile](writing-profile.md), [File Architecture](file-architecture.md), [Execution Modes](execution-modes.md), and [Governance Schemas](governance-schemas.md). Use repository-relative links so references resolve in every clone and runner.
- **AD-28 [P3 | I68/E82/R10] Objective Run Outcome Classification**: Inspect `git log` and deliverable state at session close to classify outcomes into `product-shipped`, `governance-only`, or `halted-preproduct`.

---

## 4. Failure Modes & Not-To-Dos (Anti-Patterns)

Guard actively against these recurring autonomous agent failure modes:

- **No Upfront Context Bloat**: Never bulk-read entire directories or long reference manuals at session start; always filter through a step-by-step Input Priority Ledger (`AD-04`).
- **No Self-Verifying Scripts**: Never write superficial verification scripts (e.g., regex checks that only test whether your own keywords exist) and treat a green script exit code as proof of product quality.
- **No Overcorrection on Feedback**: When the operator corrects a specific sentence or parameter, do not delete valid adjacent rules or impose rigid hard-coded limits that cause drift (`AD-22`).
- **No Synthetic Score Calculation**: Never invent or compute mathematical formulas combining `Impact`, `Evidence`, and `Risk` into a single score; keep `[P<tier> | I/E/R]` as raw unaggregated estimates.
- **No Handover Escapism**: Never write a `HANDOVER.md` to defer a checkable question to a "next actor" when tools or subagents are available in the current session (`AD-06`).
- **No Stale Residual Names**: Never leave mentions of deleted systems or superseded concepts inside active rules; either eradicate them completely or isolate necessary migration warnings in a dedicated migration/not-to-do section (`AD-15`).
