---
type: Plan
title: Apex Informatics Adoption — Patch Sequences A1 and A2
description: Reviewable patch sequence for implementing the W1 and W2 portions of the Apex Option A informatics adoption without starting later migration waves.
tags: [okf, informatics, patch-plan, a1, a2, apex-meta]
generated: { by: openai/gpt-5.6-sol, at: 2026-09-01T16:34:00Z }
status: approved_for_execution
---

# Purpose

Define the two bounded implementation patches authorized for the first Apex informatics adoption increment.

```text
A1 = W1 standard + always-on/scoped routing
A2 = W2 validator + tests + minimal authoring procedure
```

This document is a patch plan, not an applied-change record.

# Patch discipline

For both sequences:

1. read every live target file completely before modification;
2. preserve current orchestration/runtime semantics unless the patch explicitly changes routing ownership;
3. use the narrowest change that establishes the target architecture;
4. keep current truth in current files and history/research in their existing historical/research locations;
5. do not perform opportunistic cleanup;
6. do not migrate later knowledge zones;
7. verify after each bounded patch group rather than only at the end.

A1 and A2 should be independently reviewable. A2 must not be mixed into A1.

# A1 — Standard and routing patch

## Goal

Create the canonical Apex informatics profile and repair the repository's always-on/scoped instruction surfaces so they route to owners instead of duplicating knowledge.

## Preconditions

A1 starts only after W0 has produced:

- current repository pin;
- instruction-surface inventory;
- current OKF footprint;
- initial retrieval/routing evaluation;
- root `CLAUDE.md` load/dependency status, or an explicit unresolved exception.

## A1 file set

### Create

```text
apex-meta/informatics/index.md
apex-meta/informatics/standard.md
apex-meta/informatics/migration.md
apex-meta/informatics/log.md
.claude/rules/informatics.md
.github/instructions/informatics.instructions.md
```

### Patch

```text
AGENTS.md
.claude/CLAUDE.md
.github/copilot-instructions.md
```

### Conditional patch/delete

```text
CLAUDE.md
```

Only after actual load/dependency verification.

### Update discovery after core patch is verified

```text
apex-meta/SmallSkills/OKF_Format/adoption-project/index.md
apex-meta/SmallSkills/OKF_Format/adoption-project/log.md
```

These adoption-project updates record that the approved implementation plan exists and, once A1 is actually executed, link to the new canonical standard. They must not falsely state that execution occurred before it did.

## A1 patch groups

### A1.1 — Create canonical informatics package

Create `apex-meta/informatics/index.md` first.

Acceptance:

- root declares OKF v0.2 correctly;
- index contains descriptions sufficient for routing;
- no policy duplication in the index.

Then create `standard.md`.

The standard must lock these boundaries:

| Layer | Owner |
|---|---|
| knowledge serialization/conformance | OKF v0.2 |
| information construction | Information Mapping-derived block discipline |
| topic sanity | DITA topic principle |
| technical prose | STE-derived Apex profile |
| normative keywords | RFC 2119/8174 where used normatively |
| universal agent control | root agent instruction surfaces |
| localized agent control | scoped/path-specific instructions |
| repeatable procedure | Agent Skills |
| runtime context | smallest sufficient high-signal context, progressive/JIT retrieval |
| deterministic enforcement | local validator, added in A2 |

The standard must explicitly say:

```text
Apex profile conformance != OKF conformance
STE-derived != full ASD-STE100 compliance
AGENTS/CLAUDE adapters != durable knowledge owners
Skills != general knowledge bases
```

Create `migration.md` next.

Lock the migration strategy:

```text
new/current governed knowledge → conform going forward
live legacy knowledge → migrate only in explicit later waves
historical/raw/archive → leave untouched by default
.okf.md suffix → never treated as proof of OKF
```

Create `log.md` last.

Do not copy prior research narratives into the canonical package.

### A1.2 — Refactor root `AGENTS.md` into universal control

Read current `AGENTS.md` and identify content by role:

```text
universal invariant
repository router
procedure detail
knowledge detail
historical explanation
```

Keep universal invariants and routing.

For task-specific Apex-KB patch mechanics already owned by the `apex-kb` Skill, replace detailed duplication with a route to that owner where doing so preserves the current safety contract.

Do not weaken mutation safety by deleting the only enforceable statement of a rule. If W0 shows that a detail has no real owner yet, keep it until ownership is moved deliberately.

Verification after A1.2:

- simple Git/push intent still follows the same directness policy;
- Apex KB work still routes to `apex-kb`;
- existing mutation gates remain effective;
- unrelated current behavior is unchanged.

### A1.3 — Patch `.claude/CLAUDE.md` as Claude adapter/router

Preserve the current two-system model and Plan-Sync-Session boundaries.

Add only the minimum needed to:

- inherit/reference universal invariants without maintaining a second copy;
- route informatics/knowledge-authoring questions to `apex-meta/informatics/index.md`;
- keep current entrypoint-trigger rules intact;
- preserve the rule to load only active state/packets/references.

Do not turn `.claude/CLAUDE.md` into a summary of `standard.md`.

Verification after A1.3:

- Weekly Orchestrator route unchanged;
- Multi-Agent Orchestration route unchanged;
- `apex-plan`, `apex-sync`, `apex-session` boundary unchanged;
- informatics route resolves correctly;
- ordinary unrelated tasks do not require reading the informatics standard.

### A1.4 — Repair `.github/copilot-instructions.md`

Remove stale repository identity and stale wiki-only operating assumptions.

Target form:

```text
small Copilot-specific adapter
+ current Apex repository identity
+ current owner/entrypoint routes
+ pointer to shared/root rules where supported
+ path-specific instructions delegated to .github/instructions/
```

Do not reproduce the entire Apex architecture.

Verification:

- no claim that Apex is only an Obsidian wiki framework unless that is current truth;
- no obsolete `.skills/` routing where current owners differ;
- no duplicate informatics standard content.

### A1.5 — Add scoped informatics adapters

Create:

```text
.claude/rules/informatics.md
.github/instructions/informatics.instructions.md
```

Initial scope should cover only the canonical informatics package and explicitly governed OKF reference/adoption surfaces.

Each adapter should do five things at most:

1. route to the local informatics index;
2. require reading only the relevant standard section;
3. distinguish upstream OKF rules from Apex profile rules;
4. forbid presenting invented local fields as official OKF requirements;
5. require validation after current governed knowledge changes once A2 exists.

Before A2 lands, validation wording may point to the planned validator without pretending it exists.

### A1.6 — Resolve root `CLAUDE.md` duplication conditionally

Current root `CLAUDE.md` and `AGENTS.md` may be byte-identical, but duplication alone is not enough to delete it.

Required evidence:

- actual Claude project instruction load path;
- any external scripts/configs that reference root `CLAUDE.md`;
- behavior from a cold-start/session test.

Decision table:

| Evidence | Action |
|---|---|
| `.claude/CLAUDE.md` verified sufficient; no consumers require root | delete or reduce root file |
| root required as compatibility adapter | keep thin adapter only |
| evidence incomplete | keep file unchanged; log exception |

### A1.7 — Run A1 acceptance evaluation

Rerun W0 routing cases.

Minimum pass conditions:

```text
no authority-owner regression
no orchestration-entrypoint regression
Copilot stale identity removed
informatcs standard reachable in minimal hops
unrelated tasks do not gain new mandatory context
```

Record before/after values for the same test cases rather than introducing a different benchmark.

## A1 stop boundary

After A1 passes, stop.

Do not:

- migrate `apex-meta/orchestration/**`;
- migrate Weekly Orchestrator knowledge;
- normalize `.agent/.agents/.cursor/.kiro/.pi/.windsurf` mirrors;
- retrofit historical `.okf.md` files;
- add RAG/embeddings;
- add the validator in the same patch.

# A2 — Validator and authoring-mechanism patch

## Goal

Make the W1 standard deterministically checkable and give agents one minimal repeatable procedure for authoring governed knowledge.

## Preconditions

A2 starts only when:

- A1 is accepted;
- `apex-meta/informatics/standard.md` is the current profile;
- A1 routing tests are green;
- the actual repository scripting/runtime conventions are known from W0.

## A2 file set

Exact validator paths should follow repository conventions established during W0. Do not pre-commit to a new language/runtime in this planning file.

Expected classes of changes:

### Create or extend

```text
<existing-script-root>/...informatics/OKF validator...
<existing-test-root>/...validator tests...
```

### Potential Skill work

Prefer one of these, in order:

1. extend an existing current knowledge/KB authoring Skill if ownership is a clean fit;
2. otherwise create one small `informatics-authoring` Skill;
3. do not create multiple author/review/migrate Skills in A2 unless the procedures are demonstrably distinct.

### Patch

```text
apex-meta/informatics/standard.md        # only if implementation exposes a real ambiguity
apex-meta/informatics/migration.md       # only for validator targeting/exceptions actually needed
.claude/rules/informatics.md             # replace future-validator wording with real command/route
.github/instructions/informatics.instructions.md
apex-meta/informatics/log.md
```

Do not churn the standard merely to mirror implementation details.

## A2 patch groups

### A2.1 — Implement minimal OKF conformance checks

Implement only official/minimal conformance rules owned by OKF/local OKF reference:

```text
parseable YAML frontmatter for concept files
non-empty type
reserved index.md rules
reserved log.md rules
```

The implementation must tolerate:

```text
unknown local type values
missing optional fields
unknown extra metadata
```

unless an Apex profile rule separately governs them.

Result class must be `OKF`, not a generic mixed error.

### A2.2 — Implement Apex profile checks

Add only deterministic checks that have a named Apex owner and practical consumer.

Initial candidates:

```text
governed index links resolve
required local metadata for specifically governed artifact types
duplicate durable IDs within governed scope
known pseudo-OKF patterns
invalid canonical-owner duplication where a canonical owner map actually exists
relevant Skill structural checks
```

Do not invent a universal metadata schema for every Markdown file.

Result class must be `APEX_PROFILE`.

### A2.3 — Add advisory writing checks

Initial warnings only:

```text
long procedural sentence
long descriptive sentence
obvious multi-instruction procedure sentence
large mixed-purpose prose block
```

Exempt or suppress where appropriate:

```text
code
identifiers
URLs
formulas
quotations
raw evidence
archives
source corpora
```

Result class must be `ADVISORY`.

No writing warning may make an otherwise valid bundle fail A2 unless a later explicit decision promotes that rule.

### A2.4 — Add explicit target selection

The validator must require or clearly resolve a target bundle.

Initial supported targets:

```text
apex-meta/SmallSkills/OKF_Format/
apex-meta/informatics/
```

Critical regression test:

> Running the validator against one target must not cause unrelated Markdown elsewhere in the repository to be interpreted as concept files in the same OKF bundle.

### A2.5 — Add negative and false-positive tests

Required RED tests:

```text
malformed frontmatter
missing type
bad reserved index/log shape
broken governed index entry
duplicate durable ID
pseudo-OKF file with no real frontmatter
```

Required GREEN tests:

```text
unknown local type
optional metadata omitted
raw/archive material outside governed target
long code line
ordinary Markdown outside declared target
```

Every deterministic rule added in A2 should have at least one test proving it actually fires or stays silent correctly.

### A2.6 — Add minimal authoring procedure

The procedure should be approximately:

```text
identify authority
→ identify governed bundle
→ read index
→ read relevant standard section
→ patch/create concept
→ update index if required
→ run validator
→ report result
```

Keep durable rules in `apex-meta/informatics/standard.md`.

Do not duplicate:

- OKF field definitions;
- Information Mapping rules;
- STE rules;
- migration policy;
- validation semantics

inside `SKILL.md` beyond the minimum procedure pointers needed to execute correctly.

### A2.7 — Optional read-only third-party comparison

Only after local tests are green, a community OKF validator may be run read-only against the two governed bundles.

Use it to identify discrepancies, not to redefine the Apex standard.

Any disagreement is resolved by:

```text
official OKF spec/local grounded reference
→ Apex standard
→ local validator implementation
```

Do not add third-party tooling as a required dependency in A2 without a separate approval.

### A2.8 — Run A2 acceptance evaluation

Run:

- validator positive tests on both initial bundles;
- all negative tests;
- all false-positive tests;
- selected W0 authoring/retrieval cases;
- one cold-start knowledge-authoring case that proves the agent reaches the standard via routing rather than by loading the whole research bundle.

A2 passes only if:

```text
OKF errors and Apex errors are visibly separate
warnings do not masquerade as conformance failures
targeting is bounded
false positives are controlled
Skill/procedure points to standard rather than copying it
no later knowledge zone has been migrated
```

# A1/A2 relationship

```text
A1
creates the policy and routing contract

A2
makes that contract checkable and repeatable
```

A2 must not silently change A1 policy to fit an easier validator implementation.

If A2 reveals a standard ambiguity, patch the standard explicitly and record the reason in `apex-meta/informatics/log.md`.

# Review checklist

Before declaring A1 complete:

- [ ] canonical `apex-meta/informatics/` package exists
- [ ] root/shared rules have one owner
- [ ] Claude routes correctly
- [ ] Copilot stale identity is removed
- [ ] scoped informatics adapters exist
- [ ] root `CLAUDE.md` decision is evidence-based
- [ ] W0 routing benchmark rerun
- [ ] no W2/W3 work slipped in

Before declaring A2 complete:

- [ ] OKF validator layer exists
- [ ] Apex profile validator layer exists
- [ ] advisory writing layer is non-blocking
- [ ] target selection is bounded
- [ ] RED tests prove rules bite
- [ ] GREEN tests prove tolerances/exclusions
- [ ] one minimal authoring procedure exists or an existing owner was extended
- [ ] no third-party validator is authoritative
- [ ] no W3+ migration occurred

# Completion boundary

A1 and A2 completion authorizes only the infrastructure needed for later pilots.

The next migration wave must be separately launched after reviewing W0-W2 evidence.
