---
type: Plan
title: PATCH-01 — Informatics Scope and Standards Separation
description: Exact-match patch pack to path-scope Claude informatics rules and separate upstream OKF v0.2 conformance from the Apex governed-bundle profile.
tags: [patch, informatics, okf, claude, conformance]
generated: { by: openai/gpt-5.6-sol, at: 2026-09-02T07:02:00Z }
status: proposed_not_applied
---

# Intent

Fix four connected defects without changing the broader architecture:

1. `.claude/rules/informatics.md` is accidentally always-on.
2. `standard.md` presents Apex profile rules as upstream OKF MUSTs.
3. the root informatics `index.md` carries extra frontmatter that the local OKF reference itself advises against.
4. the authoring Skill uses a non-current Claude frontmatter key and does not distinguish upstream from local metadata requirements.

**Do not apply this file as a whole-file rewrite. Apply each exact-match block independently.**

# Block 1 — path-scope the Claude rule

<file>.claude/rules/informatics.md</file>
<old># Scoped Informatics Rule — Claude Code

When creating, editing, or validating knowledge files under `apex-meta/informatics/` or `apex-meta/SmallSkills/OKF_Format/`:

1. **Routing**: Refer to the canonical standard index at `apex-meta/informatics/index.md`.
2. **Smallest Sufficient Context**: Read only the specific section of `standard.md` or `migration.md` relevant to the active task.
3. **Specification Separation**: Distinguish official upstream OKF v0.2 rules (owned by `SmallSkills/OKF_Format/`) from local Apex profile rules (owned by `apex-meta/informatics/standard.md`).
4. **No Invented Requirements**: Never present local metadata conventions as upstream OKF specification requirements.
5. **Deterministic Validation**: Run `apex-meta/scripts/okf_validator.py --target <bundle_path>` on modified bundles before declaring completion.</old>
<new>---
paths:
  - "apex-meta/informatics/**"
  - "apex-meta/SmallSkills/OKF_Format/**"
---

# Scoped Informatics Rule — Claude Code

When creating, editing, or validating knowledge files under `apex-meta/informatics/` or `apex-meta/SmallSkills/OKF_Format/`:

1. **Routing**: Refer to the canonical standard index at `apex-meta/informatics/index.md`.
2. **Smallest Sufficient Context**: Read only the specific section of `standard.md` or `migration.md` relevant to the active task.
3. **Specification Separation**: Distinguish official upstream OKF v0.2 rules (owned by `SmallSkills/OKF_Format/`) from local Apex profile rules (owned by `apex-meta/informatics/standard.md`).
4. **No Invented Requirements**: Never present local metadata conventions as upstream OKF specification requirements.
5. **Deterministic Validation**: Run `apex-meta/scripts/okf_validator.py --target <bundle_path>` on modified governed bundles before declaring completion.</new>

# Block 2 — make the root OKF version declaration minimal

<file>apex-meta/informatics/index.md</file>
<old>---
okf_version: "0.2"
title: Apex Informatics Standard
description: Canonical entrypoint and routing index for the Apex OS knowledge and instruction architecture standard.
---</old>
<new>---
okf_version: "0.2"
---</new>

# Block 3 — narrow upstream OKF ownership wording

<file>apex-meta/informatics/standard.md</file>
<old>1. **Upstream OKF v0.2 Specification**: Governs raw serialization format, parseable YAML frontmatter, and bundle root conventions.</old>
<new>1. **Upstream OKF v0.2 Specification**: Governs concept frontmatter, reserved `index.md` / `log.md` structure when those files are present, and permissive bundle conformance.</new>

# Block 4 — replace Section 4 with explicit upstream/profile separation

<file>apex-meta/informatics/standard.md</file>
<old>## 4. Knowledge Bundle Structure and OKF Conformance

A declared OKF knowledge bundle MUST conform to OKF v0.2:
1. **Root `index.md`**:
   - MUST begin with parseable YAML frontmatter containing `okf_version: "0.2"`.
   - MUST provide concise routing links to all bundle member concepts.
   - MUST NOT duplicate substantive body text from concept files.
2. **Concept Files**:
   - MUST begin with parseable YAML frontmatter containing `type`, `title`, and `description`.
   - MUST use recognized or locally documented `type` values (e.g. `Reference`, `Standard`, `Policy`, `Research`, `Plan`).
3. **Changelog `log.md`**:
   - MUST maintain chronological record of bundle changes without embedding discarded drafts.</old>
<new>## 4. Knowledge Bundle Structure and Conformance

### 4.1 Upstream OKF v0.2 conformance

A bundle is OKF v0.2-conformant when:

1. every non-reserved `.md` concept file has parseable YAML frontmatter;
2. every concept frontmatter block contains a non-empty `type`;
3. reserved `index.md` and `log.md` files follow the upstream structure when present.

Upstream OKF conformance MUST NOT fail merely because a bundle has no `index.md`, omits optional concept fields, uses an unknown local `type`, contains unknown additional keys, or has a broken cross-link. A root `index.md` MAY declare `okf_version: "0.2"`; the version declaration is not an upstream requirement for bundle conformance.

### 4.2 Apex governed-bundle profile

For a bundle explicitly governed by this Apex profile:

1. **Root routing index**:
   - MUST contain a root `index.md` so agents have a bounded progressive-disclosure entrypoint.
   - MUST declare `okf_version: "0.2"` in root-index frontmatter.
   - SHOULD keep that frontmatter to the version declaration only.
   - MUST provide concise routing links to current member concepts without duplicating their substantive bodies.
2. **Current concept files**:
   - MUST satisfy upstream OKF (`type`).
   - MUST also provide `title` and `description` as Apex profile metadata for routing and previews.
   - MAY use producer-defined local type values. Unknown types are not upstream OKF failures.
3. **History**:
   - A maintained canonical bundle MUST use `log.md` for concise dated change history.
   - `log.md` MUST follow upstream reserved-file structure and MUST NOT become a store for discarded drafts or research narrative.

Local failures in this subsection are `APEX_PROFILE`, not `OKF`, diagnostics.</new>

# Block 5 — correct validation ownership

<file>apex-meta/informatics/standard.md</file>
<old>## 12. Validation Classes

Deterministic tooling enforces three distinct diagnostic classes:

1. **`OKF`**: Upstream specification violations (missing frontmatter, missing `type`, invalid root `okf_version`).
2. **`APEX_PROFILE`**: Apex-specific profile violations (broken governed index links, duplicate durable IDs in scope, unfrontmattered `.okf.md` files in governed targets).
3. **`ADVISORY`**: Non-blocking stylistic suggestions (sentence length, prose chunk size).</old>
<new>## 12. Validation Classes

Deterministic tooling enforces three distinct diagnostic classes:

1. **`OKF`**: Upstream specification violations: an invalid concept frontmatter block, a missing or empty concept `type`, or an invalid reserved `index.md` / `log.md` structure when such a reserved file is present.
2. **`APEX_PROFILE`**: Apex-specific governed-bundle violations: missing required root routing index/version declaration, missing Apex-required `title` / `description`, broken governed index links, duplicate durable IDs in scope, or unfrontmattered `.okf.md` drift in governed targets.
3. **`ADVISORY`**: Non-blocking stylistic suggestions such as sentence length and prose chunk size.

The validator MUST NOT upgrade an Apex profile preference into an upstream OKF error.</new>

# Block 6 — replace the undifferentiated reference list

<file>apex-meta/informatics/standard.md</file>
<old>## 14. Grounded References

- [OKF v0.2 Conformance Rules](../SmallSkills/OKF_Format/conformance-rules.md)
- [Informatics Design Formats Practice Guide](../kb/claude-code-orchestration-design/wiki/summaries/informatics-design-formats-practice-guide.md)
- [Token-Efficient Information Design](../kb/claude-code-orchestration-design/wiki/summaries/token-efficient-information-design.md)
- [Informatics Design Doctrine (Weekly Role)](../../.claude/skills/weekly-orchestrator/references/roles/informatics-design-doctrine.md)</old>
<new>## 14. References and Source Roles

### Normative upstream standards

| Source | Role in this profile |
|---|---|
| [Open Knowledge Format v0.2 Specification](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) | Normative owner of OKF serialization and conformance. |
| [RFC 2119](https://www.rfc-editor.org/rfc/rfc2119) and [RFC 8174](https://www.rfc-editor.org/rfc/rfc8174) | Normative meaning of capitalized requirement keywords where this standard uses them normatively. |

### Method and runtime references

| Source | Role in this profile |
|---|---|
| Information Mapping — Maps/Blocks guidance | Authoring-method reference for labeled blocks and one-main-idea construction; not an OKF requirement. |
| OASIS DITA topic architecture | Reference for self-contained topic boundaries and concept/task/reference separation; Apex does not adopt DITA XML. |
| ASD-STE100 Issue 9 | Reference for the STE-derived prose subset in §6; Apex does not claim full ASD-STE100 compliance. |
| Agent Skills specification | Reference for progressively disclosed task procedures and Skill packaging. |
| Claude Code project rules and Skills documentation | Runtime authority for Claude `paths:`, Skill invocation, and `context: fork` behavior. |
| GitHub Copilot custom-instruction documentation | Runtime authority for `.github/copilot-instructions.md` and `applyTo`-scoped instruction files. |

### Local grounded references

- [OKF v0.2 Conformance Rules](../SmallSkills/OKF_Format/conformance-rules.md) — local grounded synopsis of upstream OKF; upstream specification wins on conflict.
- [Token-Efficient Information Design](../kb/claude-code-orchestration-design/wiki/summaries/token-efficient-information-design.md) — supporting synthesis for catalog-first, refs-not-copies, and load-on-demand design.
- [Informatics Design Formats Practice Guide](../kb/claude-code-orchestration-design/wiki/summaries/informatics-design-formats-practice-guide.md) — supporting synthesis whose own uncertainty note limits universalization of Skill-package rules.

Weekly role doctrine is downstream of this standard. `weekly-orchestrator/references/roles/informatics-design-doctrine.md` MUST conform to this standard rather than serve as a base authority for it.</new>

# Block 7 — use current Claude Skill frontmatter vocabulary

<file>.claude/skills/informatics-authoring/SKILL.md</file>
<old>---
name: informatics-authoring
description: Minimal deterministic procedure for authoring, editing, or validating knowledge files in governed APEX OS bundles.
user-facing: true
---</old>
<new>---
name: informatics-authoring
description: Minimal deterministic procedure for authoring, editing, or validating knowledge files in governed APEX OS bundles.
user-invocable: true
---</new>

# Block 8 — distinguish upstream-required vs Apex-required metadata in the procedure

<file>.claude/skills/informatics-authoring/SKILL.md</file>
<old>3. **Author or Patch Concept**:
   - For new concepts: create markdown file with valid YAML frontmatter (`type`, `title`, `description`).
   - For existing concepts: author exact-match `<file>`, `<old>`, `<new>` patch block and apply using `apex-meta/scripts/apply_exact_patch.py`.</old>
<new>3. **Author or Patch Concept**:
   - For new governed concepts: create valid YAML frontmatter with non-empty `type` (upstream OKF requirement) plus `title` and `description` (Apex governed-bundle profile requirements).
   - Producer-defined local `type` values are allowed; do not present them as centrally registered OKF types.
   - For existing concepts: author exact-match `<file>`, `<old>`, `<new>` patch block and apply using `apex-meta/scripts/apply_exact_patch.py`.</new>

# Block 9 — label the local authoring checklist correctly

<file>apex-meta/SmallSkills/OKF_Format/conformance-rules.md</file>
<old># Practical checklist when authoring a new bundle

- [ ] Every concept file has `type` at minimum
- [ ] Root `index.md` has `okf_version: "0.2"` and nothing else in frontmatter
- [ ] Every `sources[].id` is cited by a `[^id]` somewhere in that file's body
- [ ] `stale_after` is set only where content is genuinely time-sensitive
- [ ] A `log.md` exists if the bundle expects to change over time</old>
<new># Recommended authoring checklist — not the OKF conformance bar

The following items are local/recommended authoring practices. A bundle can still be upstream OKF-conformant without the optional items below.

- [ ] Every concept file has `type` at minimum — upstream requirement
- [ ] When a root `index.md` is used, prefer `okf_version: "0.2"` and no other frontmatter keys
- [ ] Every `sources[].id` is cited by a `[^id]` somewhere in that file's body
- [ ] `stale_after` is set only where content is genuinely time-sensitive
- [ ] Add `log.md` when the bundle benefits from scoped chronological history</new>

# Verification after application

```text
1. Open an unrelated source file in Claude and inspect /memory: informatics.md must not be loaded solely because the session started.
2. Open apex-meta/informatics/standard.md: informatics.md should become applicable.
3. Run the validator only after PATCH-02 is also applied; its diagnostic classes must match revised §12.
4. Confirm upstream OKF-only test: concept with only `type` is conformant.
5. Confirm Apex governed-profile test: the same concept can separately fail APEX_PROFILE for missing title/description.
```
