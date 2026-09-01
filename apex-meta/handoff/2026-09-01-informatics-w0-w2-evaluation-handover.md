# Handover Document: Evaluation of Apex Informatics Adoption (Waves W0–W2 & Patch Sequences A1–A2)

This document is prepared for an independent reviewer or another agent session to evaluate the implementation of **Wave 0 (Freeze & Measure)**, **Wave 1 / Patch Sequence A1 (Standard & Routing Lock)**, and **Wave 2 / Patch Sequence A2 (Deterministic Validation & Authoring Mechanism)** in `leela-spec/apexai-os-meta`.

---

## 1. Repository State & Verification Coordinates

- **Branch**: `main`
- **Head Commit**: `499a3947`
- **Pre-execution Commit**: `c21915f0`
- **Working Tree Status**: Clean (0 uncommitted files)
- **Governed Paths**:
  - Instruction surfaces: `AGENTS.md`, `CLAUDE.md`, `.claude/CLAUDE.md`, `.github/copilot-instructions.md`, `.claude/rules/**`, `.github/instructions/**`
  - Canonical standard: `apex-meta/informatics/` (`index.md`, `standard.md`, `migration.md`, `log.md`)
  - Grounded reference: `apex-meta/SmallSkills/OKF_Format/`
  - Tooling & tests: `apex-meta/scripts/apply_exact_patch.py`, `apex-meta/scripts/okf_validator.py`, `apex-meta/scripts/tests/`
  - Authoring skill: `.claude/skills/informatics-authoring/`
  - Patches: `apex-meta/patches/a1/`, `apex-meta/patches/a2/`
  - Adoption evidence: `apex-meta/SmallSkills/OKF_Format/adoption-project/` (`w0-baseline-inventory.md`, `w0-retrieval-eval.md`, `log.md`, `index.md`)

---

## 2. Fast Independent Verification Commands

An evaluating agent can run the following deterministic test suite to verify all claims:

```powershell
# 1. Run unit tests for exact patch runner (4/4 tests)
python -m unittest discover -s apex-meta/scripts/tests -p "test_apply_exact_patch.py"

# 2. Run unit & fixture tests for OKF validator (9/9 tests: RED fault-injection & GREEN tolerances)
python -m unittest discover -s apex-meta/scripts/tests -p "test_okf_validator.py"

# 3. Validate governed OKF reference bundle (0 errors, 8 advisory warnings)
python apex-meta/scripts/okf_validator.py --target apex-meta/SmallSkills/OKF_Format

# 4. Validate canonical informatics package (0 errors, 0 warnings)
python apex-meta/scripts/okf_validator.py --target apex-meta/informatics

# 5. Check git log and diff against base commit
git diff c21915f0...HEAD --stat
```

---

## 3. Top 20 High-Impact Changes (From $\rightarrow$ To)

Below are 20 concrete examples detailing the exact file locations, before-and-after content diffs, and the architectural rationale for the highest-impact changes made during this increment:

---

### Example 1: `AGENTS.md` — Universal Informatics & Knowledge Routing
- **File**: `AGENTS.md:L31-L36`
- **From (Old)**:
  ```markdown
  - No-changelog: Do not retain old errors, rejected options, prior versions, incident narratives, or "what changed" explanations in current-truth content.

  ## Apex KB Dispatch
  - Trigger: Requests to create, start, set up, build, intake, compile, query, retrieve, audit, or maintain an Apex KB use the repository-local `.claude/skills/apex-kb/SKILL.md`.
  ```
- **To (New)**:
  ```markdown
  - No-changelog: Do not retain old errors, rejected options, prior versions, incident narratives, or "what changed" explanations in current-truth content.

  ## Informatics & Knowledge Routing
  - Trigger: Requests to create, edit, audit, or validate repository knowledge files or documentation follow the canonical standard at `apex-meta/informatics/index.md`.
  - Authority: The canonical profile in `apex-meta/informatics/standard.md` overrides ad-hoc formatting conventions or generic agent habits.

  ## Apex KB Dispatch
  - Trigger: Requests to create, start, set up, build, intake, compile, query, retrieve, audit, or maintain an Apex KB use the repository-local `.claude/skills/apex-kb/SKILL.md`.
  ```
- **Impact & Rationale**: Establishes universal, cross-agent authority routing for all repository knowledge authoring and documentation tasks, keeping root instructions minimal while pointing directly to the canonical standard.

---

### Example 2: `CLAUDE.md` — Root Instruction Mirror Synchronization
- **File**: `CLAUDE.md:L31-L36`
- **From (Old)**:
  ```markdown
  ## Apex KB Dispatch
  - Trigger: Requests to create, start, set up, build, intake, compile, query, retrieve, audit, or maintain an Apex KB use the repository-local `.claude/skills/apex-kb/SKILL.md`.
  ```
- **To (New)**:
  ```markdown
  ## Informatics & Knowledge Routing
  - Trigger: Requests to create, edit, audit, or validate repository knowledge files or documentation follow the canonical standard at `apex-meta/informatics/index.md`.
  - Authority: The canonical profile in `apex-meta/informatics/standard.md` overrides ad-hoc formatting conventions or generic agent habits.

  ## Apex KB Dispatch
  - Trigger: Requests to create, start, set up, build, intake, compile, query, retrieve, audit, or maintain an Apex KB use the repository-local `.claude/skills/apex-kb/SKILL.md`.
  ```
- **Impact & Rationale**: Synchronizes the root `CLAUDE.md` mirror byte-for-byte with `AGENTS.md` to prevent split-brain instruction loading across different client runtimes without breaking backwards compatibility.

---

### Example 3: `.claude/CLAUDE.md` — Direct Route to Canonical Informatics
- **File**: `.claude/CLAUDE.md:L35-L37`
- **From (Old)**:
  ```markdown
  ## Navigation

  - Repository map: `apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md`.
  - Weekly design and evidence: `apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md`.
  ```
- **To (New)**:
  ```markdown
  ## Navigation

  - Repository map: `apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md`.
  - Informatics standard & knowledge authoring: `apex-meta/informatics/index.md`.
  - Weekly design and evidence: `apex-meta/kb/Weekly-Orchestrator/00-START-HERE.md`.
  ```
- **Impact & Rationale**: Enables Claude Code project sessions to discover and navigate to the canonical informatics standard in 1 hop upon operator intent.

---

### Example 4: `.claude/CLAUDE.md` — Universal Invariant Pointer in Navigation
- **File**: `.claude/CLAUDE.md:L38-L41`
- **From (Old)**:
  ```markdown
  - Multi-Agent architecture and terminology: `apex-meta/orchestration/ARCHITECTURE.md` and `apex-meta/orchestration/GLOSSARY.md`.
  - Skill-specific triggers, failure behavior, gates, and output contracts remain owned by each selected `SKILL.md`.
  ```
- **To (New)**:
  ```markdown
  - Multi-Agent architecture and terminology: `apex-meta/orchestration/ARCHITECTURE.md` and `apex-meta/orchestration/GLOSSARY.md`.
  - Universal invariants & patch safety: `AGENTS.md`.
  - Skill-specific triggers, failure behavior, gates, and output contracts remain owned by each selected `SKILL.md`.
  ```
- **Impact & Rationale**: Explicitly anchors Claude Code navigation to shared repository invariants in `AGENTS.md` rather than maintaining duplicate safety rule definitions.

---

### Example 5: `.github/copilot-instructions.md` — Removal of Obsolete Framework Identity
- **File**: `.github/copilot-instructions.md:L1-L3`
- **From (Old)**:
  ```markdown
  # Obsidian Wiki — Copilot Context

  This project is a **skill-based framework** for building and maintaining an Obsidian knowledge base using AI coding agents. There are no scripts or dependencies — everything is markdown instructions that the agent executes directly.
  ```
- **To (New)**:
  ```markdown
  # APEX OS — Copilot Context

  APEX OS is a multi-agent orchestration operating system and capability backbone. Detailed instructions, architecture contracts, and skills are scoped to specific entrypoints.
  ```
- **Impact & Rationale**: Eliminates stale prompt identity that falsely informed Copilot that the repository was purely an Obsidian wiki toolkit.

---

### Example 6: `.github/copilot-instructions.md` — Elimination of 38-Line Stale Skills Table
- **File**: `.github/copilot-instructions.md:L5-L13`
- **From (Old)**:
  ```markdown
  ## Skills Reference

  | Skill | Folder | Purpose |
  |---|---|---|
  | Setup | `.skills/wiki-setup/` | Initialize vault structure |
  | Ingest | `.skills/wiki-ingest/` | Distill documents into wiki pages... |
  ... [30 more lines of obsolete wiki skill paths] ...
  ```
- **To (New)**:
  ```markdown
  ## Core Navigation & Entrypoints

  - Universal Invariants & Git Dispatch: `AGENTS.md`
  - Orchestration Systems Index: `apex-meta/ORCHESTRATION-SYSTEMS-INDEX.md`
  - Informatics & Knowledge Standard: `apex-meta/informatics/index.md`
  - Weekly Orchestrator: `.claude/skills/weekly-orchestrator/SKILL.md`
  - Multi-Agent Orchestration: `apex-meta/orchestration/00-START-HERE.md`
  - Shared Backbone: `.claude/skills/apex-plan/`, `.claude/skills/apex-sync/`, `.claude/skills/apex-session/`
  ```
- **Impact & Rationale**: Replaces nonexistent `.skills/` paths with live APEX OS orchestration and backbone entrypoints.

---

### Example 7: `.github/copilot-instructions.md` — Scoped Instructions & Progressive Disclosure
- **File**: `.github/copilot-instructions.md:L15-L20`
- **From (Old)**:
  ```markdown
  ## Coding Conventions

  - When creating wiki pages, always use YAML frontmatter.
  - Use `[[wikilinks]]` syntax for cross-references — NOT markdown links.
  - Never modify the `.obsidian/` directory.
  ```
- **To (New)**:
  ```markdown
  ## Working Principles

  - **Smallest Sufficient Context**: Load only the specific entrypoint or scoped reference required for the active task.
  - **Path-Specific Rules**: Path-scoped instructions are located under `.github/instructions/` and `.claude/rules/`.
  - **Knowledge Authoring**: Follow the canonical profile in `apex-meta/informatics/standard.md`.
  ```
- **Impact & Rationale**: Establishes progressive disclosure principles for Copilot, directing path-specific rule enforcement to `.github/instructions/`.

---

### Example 8: `adoption-project/index.md` — Link to Ratified Informatics Standard
- **File**: `apex-meta/SmallSkills/OKF_Format/adoption-project/index.md:L5-L7`
- **From (Old)**:
  ```markdown
  * [Implementation Waves W0-W2](implementation-waves-w0-w2.md) - Approved compatibility-first implementation plan for baseline measurement...
  * [Patch Sequences A1-A2](patch-sequences-a1-a2.md) - Reviewable patch sequence for W1/A1 and W2/A2...
  ```
- **To (New)**:
  ```markdown
  * [Canonical Informatics Standard](../../informatics/index.md) - The ratified Apex informatics standard package and conformance profile.
  * [Implementation Waves W0-W2](implementation-waves-w0-w2.md) - Approved compatibility-first implementation plan for baseline measurement...
  * [Patch Sequences A1-A2](patch-sequences-a1-a2.md) - Reviewable patch sequence for W1/A1 and W2/A2...
  ```
- **Impact & Rationale**: Connects the research and adoption package directly to the newly ratified canonical standard.

---

### Example 9: `adoption-project/log.md` — Formal Recording of W0 Baseline
- **File**: `apex-meta/SmallSkills/OKF_Format/adoption-project/log.md:L7`
- **From (Old)**:
  ```markdown
  **Implementation planning** — Added the approved compatibility-first implementation plan for W0-W2 and the bounded A1/A2 patch sequence... They are plans only: no W0-W2 production migration... is recorded as executed.
  ```
- **To (New)**:
  ```markdown
  **Wave 0 Baseline Recorded** — Generated read-only baseline inventory (`w0-baseline-inventory.md`) and 24-task baseline retrieval benchmark (`w0-retrieval-eval.md`).
  ```
- **Impact & Rationale**: Formally transitions the adoption project log from planning state to execution state, anchoring empirical baseline artifacts.

---

### Example 10: `adoption-project/log.md` — Formal Recording of W1 / A1 Execution
- **File**: `apex-meta/SmallSkills/OKF_Format/adoption-project/log.md:L5-L6`
- **From (Old)**: Absent.
- **To (New)**:
  ```markdown
  **Wave 1 / A1 Execution** — Executed Wave 1 / Patch Sequence A1: ratified the canonical informatics package (`apex-meta/informatics/`), surgically updated `AGENTS.md`, `.claude/CLAUDE.md`, and `.github/copilot-instructions.md` via exact-match patch runner, created scoped adapters in `.claude/rules/` and `.github/instructions/`, and verified routing.
  ```
- **Impact & Rationale**: Records the exact patch runner application and ratification of Wave 1.

---

### Example 11: `adoption-project/log.md` — Formal Recording of W2 / A2 Execution
- **File**: `apex-meta/SmallSkills/OKF_Format/adoption-project/log.md:L3-L4`
- **From (Old)**: Absent.
- **To (New)**:
  ```markdown
  **Wave 2 / A2 Execution** — Implemented deterministic OKF v0.2 / Apex Profile validator (`apex-meta/scripts/okf_validator.py`) with tri-class diagnostics (`OKF`, `APEX_PROFILE`, `ADVISORY`), created automated RED/GREEN test suite (`apex-meta/scripts/tests/test_okf_validator.py`), established minimal authoring procedure skill (`.claude/skills/informatics-authoring/`), and validated governed bundles.
  ```
- **Impact & Rationale**: Records completion of deterministic validator tooling, unit test suites, and authoring skill.

---

### Example 12: `apex-meta/informatics/index.md` — Creation of Canonical OKF Root
- **File**: `apex-meta/informatics/index.md:L1-L19` *(NEW FILE)*
- **From (Old)**: Non-existent.
- **To (New)**:
  ```markdown
  ---
  okf_version: "0.2"
  title: Apex Informatics Standard
  description: Canonical entrypoint and routing index for the Apex OS knowledge and instruction architecture standard.
  ---

  # Apex Informatics Standard
  ...
  - [Apex Informatics Standard](standard.md)
  - [Migration & Onboarding Policy](migration.md)
  - [Change Log](log.md)
  ```
- **Impact & Rationale**: Creates a clean, conformant OKF v0.2 bundle root that acts as the single entrypoint for knowledge standards in the repo.

---

### Example 13: `apex-meta/informatics/standard.md` — Five-Plane Architecture Specification
- **File**: `apex-meta/informatics/standard.md:L38-L50` *(NEW FILE)*
- **From (Old)**: Non-existent / implicit.
- **To (New)**:
  ```markdown
  ## 3. Five-Plane Information Architecture

  | Plane | Purpose | Primary Artifacts | Loading Rule |
  |---|---|---|---|
  | **Control** | Universal invariants, security boundaries, repo routing | `AGENTS.md`, `.claude/CLAUDE.md` | Always-on / Session start |
  | **Scoped Instructions** | Path-specific or domain-specific constraints | `.claude/rules/*.md`, `.github/instructions/*.md` | Path or domain trigger only |
  | **Procedures (Skills)** | Reusable, repeatable operational workflows | `.claude/skills/*/SKILL.md` | Task-intent trigger only |
  | **Knowledge Bundles** | Curated, distilled, verified conceptual truth | OKF bundles (`index.md` + concept files) | JIT reference via index |
  | **Evidence & History** | Raw logs, transcripts, research benchmarks, audit trails | `_raw/`, `logs/`, `adoption-project/` | Deep audit/research only |
  ```
- **Impact & Rationale**: Formalizes the operational hierarchy ensuring agents load only the smallest sufficient context needed for a task.

---

### Example 14: `apex-meta/informatics/standard.md` — STE-Derived Prose Rules & Exemptions
- **File**: `apex-meta/informatics/standard.md:L72-L86` *(NEW FILE)*
- **From (Old)**: Non-existent.
- **To (New)**:
  ```markdown
  ## 6. Technical-Language Profile (STE-Derived)

  Technical text MUST adhere to the following prose rules:
  1. **Procedural Sentences**: SHOULD NOT exceed 20 words per sentence.
  2. **Descriptive Sentences**: SHOULD NOT exceed 25 words per sentence.
  3. **One Instruction per Sentence**: Multiple imperative commands MUST NOT be combined with commas or "and".
  4. **Active Voice & Explicit Agents**: State clearly who or what performs each action.
  5. **Normative Semantics**: RFC 2119 / 8174 keywords (`MUST`, `MUST NOT`, `SHOULD`, `MAY`) MUST be used only when defining strict requirements.
  6. **Exemptions**: Code blocks, mathematical formulas, URLs, identifiers, literal quotations, and raw historical evidence are exempt from sentence-length checks.
  ```
- **Impact & Rationale**: Provides clear, deterministic guidelines for human and AI authors while guaranteeing that code blocks, math, and URLs are never penalized.

---

### Example 15: `apex-meta/informatics/standard.md` — Tri-Class Validation Separation
- **File**: `apex-meta/informatics/standard.md:L130-L140` *(NEW FILE)*
- **From (Old)**: Non-existent.
- **To (New)**:
  ```markdown
  ## 12. Validation Classes

  Deterministic tooling enforces three distinct diagnostic classes:
  1. **`OKF`**: Upstream specification violations (missing frontmatter, missing `type`, invalid root `okf_version`).
  2. **`APEX_PROFILE`**: Apex-specific profile violations (broken governed index links, duplicate durable IDs in scope, unfrontmattered `.okf.md` files in governed targets).
  3. **`ADVISORY`**: Non-blocking stylistic suggestions (sentence length, prose chunk size).
  ```
- **Impact & Rationale**: Ensures clean separation between upstream spec compliance and internal repository hygiene checks.

---

### Example 16: `apex-meta/informatics/migration.md` — The `.okf.md` Suffix Policy
- **File**: `apex-meta/informatics/migration.md:L15-L25` *(NEW FILE)*
- **From (Old)**: Non-existent.
- **To (New)**:
  ```markdown
  ## 1. Governing Migration Principles

  1. **Forward Default**: All newly created and actively modified knowledge files in governed targets MUST follow the [Apex Informatics Standard](standard.md).
  2. **Explicit Wave Onboarding**: Existing repository knowledge zones... are onboarded into the standard only through explicit, approved implementation waves.
  3. **No Mass Retrofit or Renaming**: Legacy `.okf.md` files that predate standard conformance are NOT mass-renamed or retrofitted in place.
  4. **The `.okf.md` Suffix Rule**: A `.okf.md` file suffix does NOT prove OKF conformance. Conformance is determined exclusively by valid YAML frontmatter and bundle structure.
  ```
- **Impact & Rationale**: Prevents scope drift and avoids mass destructive renaming of 62 historical `.okf.md` files.

---

### Example 17: `.claude/rules/informatics.md` — Scoped Claude Rule
- **File**: `.claude/rules/informatics.md:L1-L10` *(NEW FILE)*
- **From (Old)**: Non-existent.
- **To (New)**:
  ```markdown
  # Scoped Informatics Rule — Claude Code

  When creating, editing, or validating knowledge files under `apex-meta/informatics/` or `apex-meta/SmallSkills/OKF_Format/`:
  1. **Routing**: Refer to the canonical standard index at `apex-meta/informatics/index.md`.
  2. **Smallest Sufficient Context**: Read only the specific section of `standard.md` or `migration.md` relevant to the active task.
  3. **Specification Separation**: Distinguish official upstream OKF v0.2 rules from local Apex profile rules.
  4. **No Invented Requirements**: Never present local metadata conventions as upstream OKF specification requirements.
  5. **Deterministic Validation**: Run `apex-meta/scripts/okf_validator.py --target <bundle_path>` on modified bundles before declaring completion.
  ```
- **Impact & Rationale**: Loads standard authoring constraints dynamically into Claude Code only when working on governed knowledge files.

---

### Example 18: `.github/instructions/informatics.instructions.md` — Scoped Copilot Instructions
- **File**: `.github/instructions/informatics.instructions.md:L1-L13` *(NEW FILE)*
- **From (Old)**: Non-existent.
- **To (New)**:
  ```markdown
  ---
  applyTo: "apex-meta/informatics/**,apex-meta/SmallSkills/OKF_Format/**"
  ---

  # Scoped Informatics Instructions — GitHub Copilot

  When authoring or modifying files in governed knowledge bundles:
  1. **Canonical Standard**: Route to `apex-meta/informatics/index.md`.
  2. **Prose Profile**: Follow the STE-derived sentence and chunking limits in `apex-meta/informatics/standard.md`.
  3. **OKF vs Profile**: Respect OKF v0.2 frontmatter requirements while maintaining local Apex profile checks.
  4. **No Mass Retrofit**: Do not rename or edit legacy `.okf.md` files outside governed scope.
  5. **Validation**: Validate changes with the deterministic validator script before completing.
  ```
- **Impact & Rationale**: Automates path-targeted rule injection for Copilot without bloating global workspace context.

---

### Example 19: `apex-meta/scripts/apply_exact_patch.py` — Exact-Match Patch Applier
- **File**: `apex-meta/scripts/apply_exact_patch.py:L42-L65` *(NEW FILE)*
- **From (Old)**: Non-existent.
- **To (New)**:
  ```python
  def apply_patch_blocks(patch_path: str, repo_root: str = ".", dry_run: bool = False):
      patches = parse_patch_file(patch_path)
      ...
      count = target_norm.count(old_norm)
      if count == 0:
          raise ValueError(f"FAILED exact match for {file_rel}: <old> block not found in live file.")
      elif count > 1:
          raise ValueError(f"AMBIGUOUS exact match for {file_rel}: <old> block found {count} times (must be exactly 1).")
      ...
      backup_path = f"{full_path}.bak.{int(time.time())}"
      with open(backup_path, "w", encoding="utf-8") as f:
          f.write(target_content)
      with open(full_path, "w", encoding="utf-8") as f:
          f.write(patched_content)
  ```
- **Impact & Rationale**: Guarantees deterministic, safe modifications with single-match assertions and automatic backup snapshots, replacing whole-file overwrite hazards.

---

### Example 20: `apex-meta/scripts/okf_validator.py` — Tri-Class Validator Tooling
- **File**: `apex-meta/scripts/okf_validator.py:L130-L160` *(NEW FILE)*
- **From (Old)**: Non-existent.
- **To (New)**:
  ```python
  def validate_bundle(target_dir: str) -> ValidationReport:
      ...
      # 1. OKF Root index.md verification
      if not root_index.is_file():
          findings.append(Finding(severity="OKF_ERROR", rule="OKF-ROOT-INDEX-EXISTS", ...))
      elif fm.get("okf_version") != "0.2":
          findings.append(Finding(severity="OKF_ERROR", rule="OKF-VERSION-DECLARATION", ...))
      
      # 2. Apex Profile link integrity check
      for link in extract_links(content):
          if not (target_path / link).resolve().exists():
              findings.append(Finding(severity="APEX_PROFILE_ERROR", rule="APEX-LINK-INTEGRITY", ...))
      
      # 3. Advisory prose check
      advisories = check_writing_style(rel_path, body)
      findings.extend(advisories)
      ...
  ```
- **Impact & Rationale**: Implements automated repository checking with targeted bundle scoping, broken link detection, duplicate ID detection, and non-blocking advisory writing checks.

---

## 4. Scope Boundary Verification

The evaluating agent should verify that the following out-of-scope boundaries were strictly respected:
- `apex-meta/orchestration/**`: Untouched (0 modifications).
- `apex-meta/kb/Weekly-Orchestrator/**`: Untouched (0 modifications).
- `apex-meta/handoff/**`: Untouched (0 modifications outside this handover document).
- Pre-existing `.okf.md` files: Untouched (0 mass renames or modifications).
- External repositories (`leela`): Untouched.
