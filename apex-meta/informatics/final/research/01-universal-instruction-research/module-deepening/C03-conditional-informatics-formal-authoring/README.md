---
type: ModuleDeepeningResult
title: C03 Conditional Informatics / Formal Authoring
description: Evidence-backed deepening result for the final conditional module, reducing Informatics to a precise router into the existing Apex Informatics standard instead of duplicating formal-authoring rules in the always-loaded contract.
status: RESEARCH_COMPLETE_PATCH_PENDING
updated: 2026-09-23
---

# C03 — Conditional Informatics / Formal Authoring

## 1. Final decision

- **Module:** C03
- **XML tag:** `<informatics>`
- **Semantic purpose:** Route only genuinely Informatics-governed repository knowledge work into the canonical Apex Informatics standard.
- **Selected deeper owner:** **Existing focused reference**, not a new Skill.
- **Canonical owner:** `apex-meta/informatics/index.md` -> `standard.md`, `migration.md`, validators, and underlying OKF references.
- **Key correction:** the current root block duplicates serialization, Information Mapping, prose, and progressive-disclosure rules that already live in the canonical standard. It also triggers too broadly on "architectural documentation."
- **Result:** shrink C03 to a routing + conformance rule and keep all detailed authoring method JIT in the existing Informatics bundle.

### Final root XML

~~~xml
<informatics when="creating, editing, auditing, or validating an artifact governed by the Apex Informatics Standard"
             principles="conformance,information-typing,progressive-disclosure,current-truth"
             ref="apex-meta/informatics/index.md"
             deepen_when="the artifact's canonical profile, metadata, topic structure, migration, or validation requirements are needed">
  Apply the canonical Informatics profile only to governed artifacts. Preserve the artifact's information type, authority, and current-truth boundary; load and validate only the profile details required for the task. Do not impose Informatics serialization or style on ordinary documentation, code, chat, or unmanaged history.
</informatics>
~~~

### Compact Markdown control

~~~markdown
**Informatics — conformance / information typing / progressive disclosure / current truth:** When creating, editing, auditing, or validating an artifact governed by the Apex Informatics Standard, use the canonical profile at `apex-meta/informatics/index.md`. Preserve information type, authority, and current-truth boundaries; load only the profile details needed. Do not impose Informatics serialization or style on ordinary documentation, code, chat, or unmanaged history.
~~~

## 2. What problem C03 actually needs to solve

C03 is not a general "write structured documents well" rule.

The actual failure modes are:

~~~text
formal governed artifact
-> agent does not realize a repository standard applies
-> invents local structure / metadata / style
-> creates drift from canonical knowledge architecture
~~~

and the opposite failure:

~~~text
ordinary documentation or chat
-> agent sees "documentation"
-> applies YAML/frontmatter, rigid block rules, STE sentence limits, or OKF-like structure
-> over-formalizes the output and degrades usefulness
~~~

C03 therefore needs to answer one narrow question:

> Does this artifact fall under the Apex Informatics governance boundary, and if so, where is the canonical profile?

It should not duplicate the profile itself.

## 3. Why this is the right method

### 3.1 Current OpenAI / Codex evidence

OpenAI's September 2026 guidance for GPT-6 Astra explicitly warns that accumulated Skills, `AGENTS.md`, and task prompt scaffolding can bloat context. It recommends revisiting persistent instructions because more capable models need less handholding.

OpenAI's current Skill guidance defines Skills as modular reusable instructions for specific workflows and conventions. This supports moving detailed procedure and conventions out of the always-loaded root when they apply only to a recognizable task class.

OpenAI's current Codex model guidance also confirms that `AGENTS.md` files are automatically merged into context and that instruction scope/order matters. Persistent root content therefore carries a real context cost.

Portable implication:

~~~text
always-on root
-> only routing + high-value invariant

specialized authoring standard
-> load only when the governed artifact requires it
~~~

### 3.2 Independent mature-agent convergence

**Claude Code.** Current Claude Code documentation says persistent instructions should stay specific and concise. If guidance is a multi-step procedure or matters only to one part of the codebase, move it to a Skill or a path-scoped rule. Claude also recommends topic-specific rule files and path scoping to reduce noise and save context.

**GitHub Copilot.** Current GitHub Copilot documentation separates:
- repository-wide instructions;
- path-specific instructions;
- `AGENTS.md`;
- task-specific Skills.

GitHub explicitly says path-specific instructions prevent repository-wide instructions from being overloaded with guidance that only applies to certain files/directories.

This is direct support for C03 as a conditional router rather than a root-embedded style manual.

### 3.3 Established external discipline

**DITA topic architecture** supports:
- single-subject topics;
- information typing such as concept, task, and reference;
- modular authoring and reuse;
- more specific information types where appropriate.

This supports the local Informatics ideas of typed knowledge and single-purpose topics.

**RFC 2119 / RFC 8174** support precise normative terminology such as `MUST`, `SHOULD`, and `MAY` when a specification needs explicit requirement levels.

However, neither DITA nor RFC normative language implies that every document should use formal topic types or normative keywords. Their value is conditional on the artifact actually being a structured technical/specification surface.

### 3.4 Local repository authority

The current Apex Informatics standard already owns the details:

- five-plane information architecture;
- OKF bundle requirements;
- topic/block design;
- STE-derived prose;
- progressive disclosure;
- instruction scoping;
- procedure-vs-knowledge boundaries;
- durable IDs;
- current-truth/history separation;
- validation classes;
- migration/onboarding policy.

Therefore repeating selected parts inside the C03 root block creates two authorities and future drift.

The root module should say **when** to route and **what invariant to preserve**. The existing bundle should say **how** to conform.

## 4. Semantic contract

### MUST

- Determine whether the artifact is actually governed by the Apex Informatics Standard before applying Informatics-specific structure.
- Use `apex-meta/informatics/index.md` as the canonical routing entrypoint.
- Preserve the artifact's intended information type and authority boundary.
- Preserve current truth separately from historical/evidence material when the standard requires that distinction.
- Load only the specific standard/profile/migration/validation details needed for the current operation.
- Use the repository validator when the governed profile requires deterministic validation.
- Preserve existing runtime/semantic contracts during migration or normalization.
- Treat the canonical standard as authority over duplicated local summaries.

### MUST NOT

- Apply Informatics merely because the output is Markdown or "technical documentation."
- Force YAML frontmatter, OKF structure, tables, block decomposition, sentence-length limits, or normative keywords onto ordinary documentation unless the governing profile requires them.
- Duplicate detailed Informatics rules inside `AGENTS.md`, the C03 root block, or another always-loaded file.
- Treat a `.okf.md` suffix as proof of conformance.
- Mass-retrofit legacy repository content unless an approved migration wave authorizes it.
- mix superseded history into live current-truth artifacts.
- create a new Informatics Skill that merely restates the existing standard.
- let C03 override task target, scope, evidence, or current-truth authority owned by other modules.

### Activation condition

C03 activates when the task is creating, editing, auditing, validating, or migrating an artifact that the **Apex Informatics Standard actually governs**.

Examples:

- canonical Informatics bundle content;
- declared OKF knowledge bundles;
- governed knowledge/instruction surfaces;
- approved migration-wave targets;
- other artifacts explicitly placed under Informatics governance.

### Non-activation examples

C03 should remain dormant for:

- normal chat answers;
- ordinary README/documentation not declared Informatics-governed;
- application code;
- database migrations;
- runtime scripts outside governed knowledge bundles;
- raw transcripts;
- unmanaged historical/evidence folders;
- external repositories not explicitly onboarded.

### Deepen condition

Open the Informatics bundle only when the task needs profile details such as:

- metadata/frontmatter;
- bundle structure;
- topic typing;
- migration policy;
- validator requirements;
- history/current-truth handling;
- durable identifiers;
- specific prose constraints.

Do not load the full standard preemptively when only a simple route/authority check is needed.

## 5. Neighboring-module boundaries

**A02 <scope>** determines whether modifying or migrating a knowledge zone is authorized. C03 cannot expand governance scope by itself.

**A06 <context>** owns general progressive disclosure. C03 applies that principle specifically by routing to the Informatics bundle only when needed.

**A08 <evidence>** governs claim support. Informatics metadata or structure is not evidence that substantive claims are correct.

**A11 <current_truth>** owns the universal current-authority behavior. C03 applies repository-specific current-truth/history conventions inside governed knowledge artifacts.

**A12 <communication>** owns general communication quality. C03 must not export its formal technical-prose profile into ordinary user-facing answers.

**A13 / C02** govern external grounding and deeper research. C03 structures governed artifacts after the evidence has been established; it does not replace research.

**C01** still owns material operator decisions. Formalizing a decision in an Informatics artifact does not transfer decision authority to C03.

## 6. Deeper-owner decision

### Selected: existing focused reference

The repository already has the correct deeper owner:

~~~text
apex-meta/informatics/index.md
  -> standard.md
  -> migration.md
  -> validator / referenced standards
~~~

No new `SKILL.md` is justified.

Why:

1. The detailed content is primarily a **canonical standard and conformance profile**, not a reusable procedural workflow.
2. The existing index already implements progressive disclosure.
3. The standard already distinguishes scope, non-scope, procedure, knowledge, validation, and migration.
4. A new Skill would duplicate authority and create another drift surface.
5. Deterministic validation already belongs in repository tooling rather than prose duplication.

### Why not a new scoped rule as the primary owner

Runtime-specific path scoping is useful and should be considered during later synthesis/propagation, especially because Claude and GitHub support it well. But the cross-agent C03 semantic contract must remain portable. The canonical standard is the stable owner; runtime-specific scoped rules should only be adapters that point to it.

## 7. Scenario simulations

| Scenario | Current-pilot risk | Candidate behavior | Observable pass criterion | Deep reference? |
|---|---|---|---|---|
| **Simple negative:** user asks for an ordinary Markdown project note | "formal repository knowledge" may be interpreted broadly | write the note normally unless the path/artifact is actually governed | no Informatics frontmatter/style ceremony | No |
| **Governed knowledge file:** create a concept inside a declared OKF bundle | current block contains some rules but not full profile | route to `informatics/index.md`, load relevant profile/OKF details, create typed artifact, validate | canonical metadata/topic rules followed | Yes |
| **Architecture README outside governed zone** | current trigger mentions architectural documentation | do not automatically impose Informatics; inspect explicit governance first | no false activation merely from document subject | Usually no |
| **Approved migration wave** | current block lacks preservation/migration boundary | load migration policy; preserve runtime semantics; validate target | no mass retrofit or authority regression | Yes |
| **Legacy `.okf.md` file** | filename may be treated as sufficient | check actual frontmatter/bundle conformance | suffix alone is not accepted as proof | Yes |
| **Raw transcript/evidence folder** | structured-authoring instinct may normalize raw evidence | preserve unmanaged/raw evidence unless explicitly onboarded | no destructive formalization of evidence/history | No |
| **Procedural formal doc** | current nested rule enforces one-command-per-sentence regardless of profile | load profile and apply only rules actually required by that governed artifact | prose rules come from authority, not root duplication | Yes |
| **Known failure: duplicate standard** | agent copies the full standard into a new rule/Skill | keep one canonical standard and route to it | no second rulebook created | No |
| **XML vs Markdown control** | XML may look more authoritative than it is | both forms route identically to canonical standard | representation does not create a second authority | N/A |

## 8. Realistic orchestration / agent user stories

### US-C03-01 — knowledge bundle authoring

An agent is asked to create a new canonical knowledge topic.

Expected:
- detect Informatics governance;
- read the index and only required standard sections;
- choose the correct information type;
- author the artifact;
- run required validation;
- report conformance.

### US-C03-02 — ordinary documentation

An agent is asked to improve a normal README.

Expected:
- do not activate C03 unless the README is explicitly governed;
- use normal documentation conventions;
- avoid injecting frontmatter or rigid Informatics structure without authority.

### US-C03-03 — migration

An approved wave targets a legacy knowledge zone.

Expected:
- read migration policy;
- benchmark/preserve semantics;
- normalize only authorized targets;
- validate deterministically;
- do not mass-retrofit unrelated history.

### US-C03-04 — cross-runtime adapter

A runtime supports path-specific instructions.

Expected:
- runtime adapter may scope activation to governed paths;
- adapter points to the canonical Informatics standard;
- adapter does not become an independently authored copy of the standard.

### US-C03-05 — conflict between local summary and canonical standard

Expected:
- canonical `apex-meta/informatics/index.md` / standard wins;
- stale summary is flagged;
- no synthesis of contradictory instructions.

## 9. Wording alternatives considered

### Candidate A — current pilot

~~~xml
<informatics when="creating, editing, auditing, or validating formal repository knowledge, architectural documentation, or Informatics-governed artifacts"
             principles="structured-authoring,progressive-disclosure,current-truth"
             ref="apex-meta/informatics/index.md"
             deepen_when="the canonical profile, metadata, migration, or validation details are needed">
  Apply the canonical Informatics profile only when this trigger matches; otherwise respond in the form best suited to the task.
  <serialization>Use the canonical metadata and index conventions without duplicating deeper body content.</serialization>
  <information_mapping>Prefer scan-friendly single-purpose blocks, tables, and bullets when they improve comprehension; do not force them where cohesive prose is better.</information_mapping>
  <procedural_prose>Use active voice and one command per sentence for procedural instructions; apply sentence-length targets only when the canonical style profile requires them.</procedural_prose>
  <progressive_disclosure>Provide the smallest sufficient context first and load deeper specification details just in time.</progressive_disclosure>
</informatics>
~~~

**Strengths:** has a trigger, canonical ref, JIT deepening, and useful anti-overformalization language.

**Why it loses:** broad "architectural documentation" trigger; duplicates canonical detail; spends root tokens on four subrules; creates future two-authority drift.

### Candidate B — path-only trigger

~~~xml
<informatics when="working under apex-meta/informatics or declared OKF bundle paths">
  Follow apex-meta/informatics/index.md.
</informatics>
~~~

**Rejected:** too narrow. Approved migration waves and other explicitly governed artifacts may exist outside those paths.

### Candidate C — generic structured writing

~~~xml
<informatics when="writing structured technical documentation">
  Use typed topics, concise blocks, metadata, and progressive disclosure.
</informatics>
~~~

**Rejected:** over-generalizes a local repository standard into a universal writing rule.

### Candidate D — selected router

The selected candidate keys activation to **actual governance**, preserves a few load-bearing invariants, and routes all mechanics to the existing canonical bundle.

## 10. Source record

Checked 2026-09-23.

### OpenAI / Codex primary

1. OpenAI Developers — Rethinking skills and prompts for GPT-6 Astra
   https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra
2. OpenAI API — Skills
   https://developers.openai.com/api/docs/guides/tools-skills
3. OpenAI API — Model guidance / Using agents.md
   https://developers.openai.com/api/docs/guides/latest-model
4. OpenAI API — Agents
   https://developers.openai.com/api/docs/guides/agents

### Independent mature-agent systems

5. Claude Code — How Claude remembers your project
   https://code.claude.com/docs/en/memory
6. Claude Code — Extend Claude with skills
   https://code.claude.com/docs/en/skills
7. GitHub Docs — Adding repository custom instructions
   https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/add-custom-instructions/add-repository-instructions
8. GitHub Docs — About Copilot code review / instructions vs AGENTS.md vs Skills
   https://docs.github.com/en/copilot/concepts/agents/code-review
9. GitHub Docs — About customizing responses
   https://docs.github.com/en/copilot/concepts/prompting/response-customization

### External disciplines

10. OASIS DITA — topic as the basic unit of information
    https://docs.oasis-open.org/dita/v1.2/os/spec/archSpec/topicdefined.html
11. OASIS DITA — technical content information types
    https://docs.oasis-open.org/dita/v1.2/os/spec/archSpec/dita_technicalContent_InformationTypes.html
12. RFC Editor — RFC 2119
    https://www.rfc-editor.org/info/rfc2119/
13. RFC Editor — RFC 8174
    https://www.rfc-editor.org/info/rfc8174/

### Local canonical authority

14. `apex-meta/informatics/index.md`
15. `apex-meta/informatics/standard.md`
16. `apex-meta/informatics/migration.md`

## 11. Evidence confidence and open uncertainty

- **High confidence:** detailed Informatics rules should not be duplicated in the always-loaded C03 block.
- **High confidence:** persistent root instructions should remain concise; specialized rules should be path/task scoped or JIT-loaded.
- **High confidence:** "architectural documentation" is too broad as an automatic Informatics trigger.
- **High confidence:** the existing Informatics index/standard is already the correct deeper conceptual owner.
- **High confidence:** no new generic Informatics Skill is justified.
- **Moderate-high confidence:** `conformance,information-typing,progressive-disclosure,current-truth` are sufficient semantic anchors for the compact root rule.
- **Open evaluation question:** later cross-module synthesis should test whether C03 needs to remain in the universal root at all, or whether runtime path-scoped rules can replace it without missed activation.
- **Open repository question:** some current runtime-specific Informatics rules may still be loaded too broadly. That is a later propagation/synthesis concern, not part of this C03 patch.

## 12. Final invariant

~~~text
C03 does not teach the Informatics standard.

C03 only does this:

is the artifact governed?
  -> no: do not impose Informatics
  -> yes: route to canonical Informatics index
          load only needed profile detail
          preserve type / authority / current truth
          validate as required
~~~
