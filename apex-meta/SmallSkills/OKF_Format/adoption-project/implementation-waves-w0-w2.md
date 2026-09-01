---
type: Plan
title: Apex Informatics Adoption — Implementation Waves W0-W2
description: Compatibility-first implementation plan for the first three waves of the Apex Option A informatics adoption: baseline, standard/routing lock, and deterministic validation/authoring support.
tags: [okf, informatics, implementation-plan, apex-meta, w0, w1, w2]
generated: { by: openai/gpt-5.6-sol, at: 2026-09-01T16:34:00Z }
status: approved_for_execution
---

# Purpose

Implement the first three waves of the approved **Option A** architecture in `leela-spec/apexai-os-meta` without starting the later repository-wide migration.

Target architecture:

```text
small always-on control
→ scoped instructions
→ task-triggered Skills
→ indexed OKF knowledge
→ evidence/raw/history only when needed
```

This plan is compatibility-first. It preserves working orchestration boundaries, the existing Agent Skills system, and the existing `SmallSkills/OKF_Format/` reference bundle.

# Scope lock

Included:

- W0 — freeze and measure the current state.
- W1 — ratify the Apex Informatics Standard and repair always-on routing surfaces.
- W2 — add deterministic validation and the minimal authoring mechanism.
- Patch sequences A1 and A2 are specified separately in [Patch Sequences A1-A2](patch-sequences-a1-a2.md).

Excluded:

- migration of `apex-meta/orchestration/` or other live knowledge zones;
- Weekly Orchestrator migration;
- bulk retrofit of historical `.okf.md` files;
- multi-client skill mirror consolidation;
- RAG, embeddings, vector databases, or semantic retrieval infrastructure;
- Leela or any other repository;
- broad restructuring of application code, runtime data, scripts, fixtures, or Supabase-related architecture.

# Governing decisions

1. **Continue the existing adoption project.** Do not create a second OKF or informatics program.
2. **OKF v0.2 owns knowledge-bundle conformance.** Apex-specific requirements are a separate profile layer.
3. **Root agent surfaces are maps, not knowledge bases.** Universal invariants and routing stay always-on; detail lives in scoped instructions, Skills, and knowledge files.
4. **Refs replace copies.** One owner for durable rules and contracts; adapters point to owners.
5. **No mass rewrite.** Existing files are migrated only when a wave explicitly names them.
6. **No history cleanup in these waves.** Raw, archival, generated, and historical material remains untouched unless needed to classify current state.
7. **Validation must distinguish official OKF failures from Apex-profile failures.** A local rule must never be reported as an upstream OKF requirement.
8. **Warnings before hard gates for writing-style rules.** STE-derived sentence limits start as advisory checks.
9. **No deletion based on apparent duplication alone.** Consumers and citations must be checked before removing any file.
10. **No cross-repository rollout until Apex has passed its own acceptance benchmark.**

# W0 — Freeze and measure

## Objective

Create a trustworthy baseline before changing instruction loading, knowledge structure, or validation behavior.

W0 is read-only except for W0 evidence artifacts inside this adoption project.

## Required inventory

Create a compact inventory of the live surfaces relevant to informatics adoption.

### A. Always-on and scoped instruction surfaces

Classify at minimum:

```text
AGENTS.md
CLAUDE.md
.claude/CLAUDE.md
.github/copilot-instructions.md
.claude/rules/**
.github/instructions/**
.agent/**
.agents/**
.cursor/**
.kiro/**
.pi/**
.windsurf/**
```

For each material surface record:

| Field | Meaning |
|---|---|
| path | Current repository path |
| consumer | Claude, Codex, Copilot, Cursor, Kiro, Pi, Windsurf, shared agent runtime, etc. |
| load_scope | always / path-scoped / task-triggered / unknown |
| authority_role | universal invariant / adapter / procedure / knowledge / evidence |
| canonicality | canonical / mirror / adapted mirror / unknown |
| duplicate_hash_group | Same bytes as another file when applicable |
| action | preserve / candidate-refactor / investigate / exclude |

### B. Knowledge zones

Classify the high-value current areas, not every repository file.

Initial zones:

```text
apex-meta/SmallSkills/OKF_Format/**
apex-meta/orchestration/**
apex-meta/kb/Weekly-Orchestrator/**
apex-meta/kb/claude-code-orchestration-design/**
apex-meta/handoff/**
.claude/skills/**
```

Use four axes:

```yaml
authority: normative | operational | evidence | historical
loading: universal | path | task | evidence-only
artifact: knowledge | instruction | procedure | state | source
lifecycle: current | generated | superseded | archive | unknown
```

### C. OKF inventory

Record:

- explicitly declared OKF v0.2 bundles;
- `index.md` roots declaring `okf_version`;
- concept files with conformant frontmatter;
- `.okf.md` files that are not actually conformant;
- files whose status cannot be established without deeper inspection.

Do not rename or retrofit anything in W0.

### D. Skill inventory

For active/high-use Skills, record:

- canonical `SKILL.md` location;
- whether the entrypoint is concise or carries heavy knowledge;
- supporting `references/`, `scripts/`, and `assets/`;
- mirrored copies across clients;
- whether copied versions are byte-identical or adapted.

W0 does not normalize mirrors.

## Baseline evaluation suite

Create an initial set of **20-30 real Apex retrieval/operation questions**. The suite must include at least the following classes:

| Class | Representative question |
|---|---|
| orchestration routing | What entrypoint runs the Weekly Orchestrator? |
| orchestration routing | What entrypoint starts Multi-Agent Orchestration? |
| mutation ownership | What owns durable project/task mutation? |
| KB procedure | How is an Apex KB created or resumed? |
| informatics authority | Where is the adopted knowledge-authoring standard? |
| OKF | What makes an Apex knowledge bundle OKF-conformant? |
| evidence lookup | Where is the source-backed rationale for progressive disclosure? |
| history routing | Where should historical orchestration rationale be read? |
| negative routing | A task unrelated to informatics must not load the informatics standard unnecessarily. |

Measure where available:

```yaml
correctness:
  - correct_answer
  - correct_authority_owner
  - no_false_authority

economy:
  - files_opened
  - irrelevant_files_opened
  - retrieval_hops
  - context_bytes_or_tokens_before_answer

quality:
  - contradiction_introduced
  - unsupported_inference
  - duplicated_rule_used
```

Do not invent a fixed token/file budget in W0. Record empirical baseline values first.

## W0 outputs

Keep W0 evidence compact. Preferred outputs inside `adoption-project/`:

```text
w0-baseline-inventory.md
w0-retrieval-eval.md
```

Do not create separate ledgers for every inventory category unless one file becomes unusable.

## W0 acceptance gate

W0 passes when:

- the current repository revision is recorded;
- relevant instruction surfaces are classified;
- the current OKF footprint and known pseudo-OKF drift are captured;
- active/high-use Skills are mapped sufficiently to detect duplication and loading scope;
- the 20-30-task baseline evaluation exists and has been run at least once;
- no production instruction, knowledge, orchestration, or runtime file has been modified.

W0 failure conditions:

- baseline depends on old chat memory instead of current repository evidence;
- ambiguous files are silently classified as canonical;
- the inventory expands into an exhaustive repository documentation project;
- implementation changes are mixed into baseline collection.

# W1 — Lock the standard and repair always-on context

## Objective

Establish one canonical Apex informatics standard and make always-on agent surfaces route to it without duplicating its content.

W1 is implemented by **Patch Sequence A1**.

## Canonical standard package

Create:

```text
apex-meta/informatics/
├── index.md
├── standard.md
├── migration.md
└── log.md
```

### `index.md`

Purpose: smallest possible routing surface for the informatics standard.

Requirements:

- OKF root frontmatter uses only `okf_version: "0.2"` as required by the local reference bundle;
- links to `standard.md`, `migration.md`, and `log.md` with one-line descriptions;
- points to `apex-meta/SmallSkills/OKF_Format/` as the detailed OKF reference/research source;
- does not restate the standard.

### `standard.md`

Purpose: one durable Apex conformance profile for knowledge and instruction architecture.

Required sections:

1. Purpose / scope / non-scope.
2. Standards precedence and ownership.
3. Five-plane information architecture.
4. Knowledge bundle structure and OKF conformance.
5. Block/topic design.
6. Technical-language profile.
7. Progressive disclosure and context delivery.
8. Agent instruction scoping.
9. Procedure/Skill boundaries.
10. Identity: durable IDs vs ordinary labels.
11. Provenance/current-truth/history handling.
12. Validation classes: OKF vs Apex profile.
13. Exceptions.
14. References to the existing local research/reference material.

The profile composes, rather than copies, the established layers already verified by the adoption research:

```text
OKF v0.2
Information Mapping
ASD-STE100-derived technical-language profile
DITA topic principle
RFC 2119/8174 normative semantics
Agent Skills progressive disclosure
scoped agent instructions
context engineering / smallest-sufficient-context principle
```

### `migration.md`

Purpose: define how existing Apex content enters the standard.

Required decisions:

- forward default: new/current knowledge follows the standard;
- existing live material is patched when explicitly onboarded by a migration wave;
- historical/raw/archive material is not mass-retrofitted;
- `.okf.md` suffix never proves OKF conformance;
- do not mass-rename historical `.okf.md` files;
- one subtree becomes a declared strict OKF bundle only by explicit adoption;
- migration must preserve semantic authority and current runtime behavior;
- later repository waves require before/after retrieval evaluation.

### `log.md`

Purpose: current adoption history for this canonical package.

Keep concise. Do not move research narratives here.

## Always-on routing repairs

W1 inspects and minimally patches:

```text
AGENTS.md
.claude/CLAUDE.md
.github/copilot-instructions.md
CLAUDE.md  # only after runtime load verification
```

### `AGENTS.md`

Target role:

```text
universal cross-agent invariants
+ repository-level routing
+ critical safety/mutation boundaries
```

Remove duplicated task-specific procedure detail only when its real owner is already established and reachable.

Apex-KB-specific mutation detail should be routed to the `apex-kb` Skill rather than re-owned globally.

### `.claude/CLAUDE.md`

Preserve its current strengths:

- compact activation router;
- two-orchestration-system separation;
- Plan-Sync-Session backbone routing;
- explicit operator-intent requirement;
- read-only-what-is-needed rule.

Patch only what is necessary to:

- reference the universal root invariants rather than duplicate them;
- route knowledge-authoring questions to `apex-meta/informatics/index.md`;
- preserve all existing runtime entrypoints.

### `.github/copilot-instructions.md`

Replace stale repository identity/context with a compact Copilot adapter.

It must not describe Apex as an Obsidian-only wiki framework if that is no longer current truth.

Keep only genuine Copilot-specific guidance plus routing to current Apex owners.

### Root `CLAUDE.md`

Current duplicate content must not be deleted merely because it looks redundant.

Before deletion or replacement:

1. verify which Claude project instruction file is actually loaded in the current runtime;
2. confirm `.claude/CLAUDE.md` is sufficient in the selected execution environments;
3. confirm no tooling explicitly depends on root `CLAUDE.md`;
4. only then remove or reduce it.

If verification is incomplete, retain it and record the duplication as a W1 exception.

## Scoped adapters

Create narrow routing adapters only for the new informatics zone:

```text
.claude/rules/informatics.md
.github/instructions/informatics.instructions.md
```

Responsibilities:

- point to the canonical informatics index;
- instruct agents to read only the section needed for the active task;
- distinguish OKF conformance from Apex-profile rules;
- prevent invented local metadata from being presented as upstream OKF requirements;
- require validation when creating or materially changing current knowledge in the governed scope.

Do not copy `standard.md` into these adapters.

## W1 verification

Required checks:

- existing Weekly Orchestrator activation still resolves to its current entrypoint;
- existing Multi-Agent Orchestration activation still resolves to its current entrypoint;
- Plan-Sync-Session ownership remains unchanged;
- Apex-KB requests still route to the `apex-kb` Skill;
- informatics questions resolve to the new canonical index/standard;
- unrelated tasks do not unnecessarily load the informatics standard;
- Copilot no longer receives materially false repository identity/instructions;
- Claude instruction loading is empirically verified before any root `CLAUDE.md` deletion;
- no code/data/runtime architecture is redesigned.

## W1 acceptance gate

W1 passes when:

- `apex-meta/informatics/` exists and is internally coherent;
- the standard clearly separates upstream OKF conformance from the Apex profile;
- always-on surfaces are smaller or no larger without losing required invariants;
- all current orchestration entrypoints still route correctly;
- no working procedure has been duplicated into the new standard;
- W0 evaluation cases relevant to routing are rerun and show no authority regression.

W1 must stop before migrating `apex-meta/orchestration/` or other knowledge zones.

# W2 — Deterministic validation and minimal authoring mechanism

## Objective

Turn the W1 standard into a checkable repository contract without creating a large control plane or automatic rewriting system.

W2 is implemented by **Patch Sequence A2**.

## Validator architecture

Create one small local validator owned by Apex.

The implementation language/location should follow existing repository conventions discovered in W0; do not introduce a new runtime solely for this validator.

The validator must expose two clearly separate result classes.

### A. `OKF` conformance

Only report an **OKF error** for rules owned by the official OKF/local reference contract, including the minimal conformance set already captured in `SmallSkills/OKF_Format/conformance-rules.md`:

- parseable YAML frontmatter on concept files;
- non-empty `type`;
- reserved `index.md` / `log.md` rules.

Do not reject unknown local `type` values merely because they are not centrally registered.

### B. `APEX_PROFILE` conformance

Apex-specific errors/warnings may cover:

- required local metadata for specifically governed artifact classes;
- broken local index entries;
- invalid internal references where deterministically checkable;
- duplicate durable IDs inside one governed scope;
- known pseudo-OKF patterns such as `.okf.md` files that lack real OKF frontmatter;
- canonical owner duplication when an explicit owner map exists;
- Skill frontmatter/shape checks where the Skill format already defines a deterministic contract.

Do not globally enforce a new metadata schema across every Markdown file.

### C. Advisory writing checks

Start as warnings only:

- procedure sentence >20 words;
- descriptive sentence >25 words;
- obvious multi-instruction procedural sentences;
- prose blocks that should likely be lists/tables;
- large mixed-purpose files that warrant human review.

Writing checks must support exemptions for:

- code;
- formulas;
- URLs;
- identifiers;
- quotations;
- raw evidence;
- archive/source material.

Do not claim full ASD-STE100 compliance.

## Validator targeting

The validator must accept an explicit target/bundle path.

Initial governed targets:

```text
apex-meta/SmallSkills/OKF_Format/
apex-meta/informatics/
```

Do not recursively declare the entire repository an OKF bundle.

## Negative tests

At minimum prove the gate catches:

```text
missing type
malformed YAML frontmatter
invalid reserved index/log shape
broken governed index entry
duplicate durable ID in the same governed scope
pseudo-OKF file with no conformant frontmatter
```

Also prove it **does not** falsely reject:

```text
unknown-but-valid local type
optional OKF metadata omitted
raw/archive file outside governed scope
code block containing long lines
unrelated Markdown outside a declared target
```

## Output contract

Validator output should be compact and machine/human readable.

Recommended shape:

```yaml
summary:
  okf_errors: 0
  apex_profile_errors: 0
  warnings: 0
findings:
  - class: OKF | APEX_PROFILE | ADVISORY
    path: ...
    rule: ...
    message: ...
```

Exact serialization may follow existing repository conventions. Do not add multiple mirrored formats without a demonstrated consumer.

## Authoring mechanism

Do not create a broad new agent framework.

After the W1 standard is stable, add the smallest reusable procedure needed to author/refactor governed knowledge.

Preferred form: an Agent Skill or existing authoring-skill extension whose core procedure is:

```text
identify authority
→ identify governed bundle
→ read local index
→ read only relevant standard section
→ create/patch concept
→ update local index when needed
→ run validator
→ report result
```

Rules:

- the Skill owns procedure, not the standard;
- the standard remains in `apex-meta/informatics/`;
- `SKILL.md` stays concise;
- detailed examples/references load only when needed;
- no automatic repository-wide rewrite;
- no silent mutation of historical/source evidence.

If an existing Skill can cleanly own this procedure, extend it instead of adding a near-duplicate Skill.

## Optional third-party cross-check

Community OKF tools may be tested read-only after the local validator passes, but they are never the Apex authority.

Authority order:

```text
official OKF specification
→ Apex informatics standard/profile
→ local deterministic validator
→ optional third-party cross-check
```

Do not install a third-party tool as a prerequisite for W2 unless separately approved.

## W2 verification

Run:

1. positive validation against `SmallSkills/OKF_Format/`;
2. positive validation against `apex-meta/informatics/`;
3. all negative tests;
4. all false-positive tests;
5. the relevant W0 retrieval tasks using the new authoring/routing path.

Record known legacy failures as explicit warnings/exclusions rather than rewriting historical material to make the gate green.

## W2 acceptance gate

W2 passes when:

- official OKF failures and Apex-profile failures are visibly separate;
- all required negative tests fail correctly;
- all required false-positive tests stay green;
- validator targeting cannot accidentally reinterpret the whole repository as one OKF bundle;
- the authoring procedure routes to the canonical standard instead of copying it;
- no third-party tool is required for ordinary validation;
- no production knowledge zone beyond the W1/W2 governed targets has been migrated.

# Sequence and dependencies

```text
W0 baseline
    ↓ required
W1 standard + routing
    ↓ required
W2 validator + authoring mechanism
```

Hard dependencies:

- W1 must not begin without a usable W0 baseline.
- W2 must validate the standard actually produced by W1, not an earlier draft.
- A2 must not introduce blocking writing-style rules before empirical W0/W1 evidence justifies them.

# Rollback principle

Each wave must remain independently reviewable and reversible.

If a wave changes routing behavior incorrectly, revert that wave rather than compensating with more instructions.

Do not preserve a broken migration merely to avoid reverting documentation work.

# Completion boundary

Completion of this plan means only:

```text
W0 complete
W1 complete
W2 complete
A1 complete
A2 complete
```

It does **not** authorize W3 or later migrations. A separate decision is required before onboarding `apex-meta/orchestration/`, Weekly Orchestrator knowledge, large KBs, or other repositories.
