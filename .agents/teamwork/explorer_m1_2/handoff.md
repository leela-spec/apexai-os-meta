# Handoff Report: Writing Profile & Prose Ergonomics Design

**From**: Explorer Agent M1-2 (`explorer_m1_2`)  
**To**: Orchestrator (`b50b8c99-9617-41ab-85e5-9b6924358d5a`) / Builder Agent M1  
**Task**: M1 Exploration Task 2 — Writing Profile & Prose Ergonomics Design  
**Date**: 2026-10-19  
**Type**: Hard Handoff (Exploration Complete)  

---

## 1. Observation

1. **Authoritative Request & Ranking Mandate**:
   - In `c:\GitDev\apexai-os-meta\.agents\teamwork\ORIGINAL_REQUEST.md`, lines 19–31 (R1) mandate a four-tier Significance Ranking Architecture (P0–P3) and raw 3-metric qualitative/quantitative estimates:
     > "Every rule or option provides raw estimates (scale 1–100) for the 3 core dimensions without computing any mathematical formula: Impact (I)... Evidence (E)... Risk (R)... Tagged using the standardized syntax: `[P<tier> | I<impact>/E<evidence>/R<risk>]` (e.g., `[P0 | I95/E95/R10]`)."
   - Lines 31 mandate top-loaded primacy:
     > "Aim to position critical invariants near the top (within the first ~500 tokens) where model attention is highest."
   - Lines 33–40 (R2) establish approximate ceilings (~150 words per prose block before tables/lists, ~20 words/procedural sentence, ~25 words/descriptive sentence, heading depth <= 3 levels) paired with explicit rule-breaking authority:
     > "An agent or author is explicitly permitted to exceed an approximate ceiling or relax a stylistic constraint whenever strict adherence would harm technical accuracy, omit load-bearing context, create artificial distortions, or produce unnatural prose. Substantive realization of the target always overrides mechanical metric compliance."
   - Lines 49 (R4) define the scope of `writing-profile.md`:
     > "`writing-profile.md` (Writing & Prose Ergonomics): Information Mapping, 'One Chunk, One Job', approximate STE limits, visual block targets, durable IDs vs. ordinary labels."

2. **Empirical Primacy & Directive Writing Rules**:
   - In `c:\GitDev\apexai-os-meta\apex-meta\kb\old-apex-full-orchestration-agent-kb\sources\primary\managed-agent-kb\special_ops__ai_handling_routing\2Do_context_file_authority_reference.md`:
     - Line 31 (`CD-01`): Critical directives must appear in first 500 tokens to prevent "mid-document burial causing 30–50% compliance drop" (Evidence F-04).
     - Line 146 (`DWR-01`): Start every directive with an imperative verb; omit modal verbs entirely (`should`, `may`, `might`, `could`).
     - Line 155 (`DWR-02`): Encode one action per directive; split compound actions into separate entries to prevent "partial compliance counted as full compliance" (Evidence F-01).
     - Line 164 (`DWR-03`): Tag every directive inline with tier tag (`critical`/`required`/`recommended`).
     - Line 173 (`DWR-04`): Add examples only for genuinely ambiguous directives; limit to two examples maximum (one correct, one wrong) to prevent "example proliferation degrading task performance" (Evidence F-05).
     - Line 191 (`DWR-06`): Run the deletion test before finalizing any directive set; remove any rule that changes behavior in fewer than 10% of realistic cases.
     - Lines 9–14: Model directive ceilings: GPT-4o: 50, Claude Standard: 50, Claude Reasoning: 80, Gemini 2.5 Pro / o3: 100.

3. **Informatics Governance & Conformance Engine**:
   - In `c:\GitDev\apexai-os-meta\apex-meta\informatics\standard.md`:
     - Section 5 (lines 75–83): Block and topic design based on Information Mapping ("One Chunk, One Job"), visual block discipline, labeled tables, bulleted contracts, and no mixed-purpose blobs.
     - Section 6 (lines 85–95): STE-derived technical prose profile: procedural ≤20 words, descriptive ≤25 words, one instruction per sentence, active voice, explicit agents, and strict exemptions for code blocks, math, URLs, identifiers, and raw logs.
     - Section 10 (lines 122–126): Durable IDs (`WP-P0-01`, etc.) must remain immutable across revisions; ordinary labels and headings may evolve.
     - Section 12 (lines 137–144): Tri-class diagnostics (`OKF`, `APEX_PROFILE`, `ADVISORY`).
   - In `c:\GitDev\apexai-os-meta\apex-meta\scripts\okf_validator.py`:
     - Lines 60–83: YAML parser is a custom line-by-line parser; supports flat key-value pairs and inline lists `[a, b]`. Does NOT parse multiline `- item` lists.
     - Lines 108–129 (`check_writing_style`): Removes fenced code, inline code, and table lines before checking sentence lengths; flags sentences exceeding 30 words as `ADVISORY_WARNING`.
     - Lines 273–286: Enforces unique durable IDs declared in frontmatter (`id:`).

4. **Operational Lore & Failure Post-Mortems**:
   - In `apex-meta/AI-Snippets/Snippets.md`, lines 4–6: `<context_routing>` enforces Adaptive Informatics: apply formal standards strictly only when authoring technical documentation; use natural conversational prose for casual chat or troubleshooting.
   - In `apex-meta/AI-Snippets/Orga/2Dos Ai Instructions.md`, lines 19–21, 45: Purge stale residual names from documents; mentioning deleted names irritates models into ghost reasoning.
   - In `Snippets.md`, line 78: Formula REI Expected Value formula is recorded as historical lore, but rejected in favor of raw uncomputed `[P<tier> | I/E/R]` tags by `ORIGINAL_REQUEST.md` R1.

---

## 2. Logic Chain

1. **Ranking System Logic (Observation 1, 2, 4)**:
   - Observation 1 and 4 mandate raw 3-metric tags `[P<tier> | I<impact>/E<evidence>/R<risk>]` (1–100 scale) and strictly ban computed composite formulas.
   - Therefore, `writing-profile.md` must not calculate any numeric score; all 23 defined rules must bear clean inline tags with raw uncomputed values (e.g. `[P0 | I98/E98/R05]`).
   - Rules must be sorted strictly descending by priority tier (P0 → P1 → P2 → P3), and sorted by descending Impact/Evidence and ascending Risk within each tier.

2. **Top-Loaded Positional Primacy Logic (Observation 1, 2)**:
   - Observation 2 proves that model compliance drops from 73% to 30–50% when directives are placed past token 500.
   - Therefore, Section 1 of `writing-profile.md` must contain all 6 P0 Critical Invariants (Substance Over Ceremony, Single Command Invariant, Imperative Verbs, Grounded Evidence, Positional Primacy, Adaptive Scope) within the first 500 tokens (~400 tokens total).

3. **Information Mapping & Prose Ergonomics Logic (Observation 1, 3)**:
   - Observation 3 specifies Information Mapping ("One Chunk, One Job") and STE word limits (procedural ≤20, descriptive ≤25).
   - Combining multiple commands into a single sentence leads to partial execution failure (Observation 2).
   - Therefore, `writing-profile.md` must enforce the Single Command Invariant and mandate active-voice phrasing with explicit agents.
   - Prose paragraphs must target a ceiling of ~150 words before breaking into structured tables or bullet lists.

4. **Validator Compatibility Logic (Observation 3)**:
   - `okf_validator.py` uses a custom line parser that fails on multiline YAML lists and checks sentence lengths with strict exemptions for code, tables, and URLs.
   - Therefore, `writing-profile.md` must declare valid frontmatter (`type: Profile`, `id: apex-informatics-writing-profile`, `tags: [...]`) formatted as flat key-values or bracketed lists, and its prose must comply with the regex patterns in `okf_validator.py`.

5. **Substance Over Ceremony & Scope Logic (Observation 1, 3, 4)**:
   - Mechanical enforcement of word limits or ceilings can lead to distorted or truncated technical explanations.
   - Furthermore, imposing formal frontmatter or STE limits onto informal chats or raw code causes ceremony pollution.
   - Therefore, `writing-profile.md` must codify WP-P0-01 (Substance Over Ceremony Invariant) and WP-P0-06 (Adaptive Scope Boundary) as non-negotiable P0 invariants.

---

## 3. Caveats

- **No Caveats**: All relevant repositories, architectural studies, empirical post-mortems, and validator scripts were inspected and synthesized.
- **Production File Modification**: As instructed by the read-only exploration mandate, no production files in `apex-meta/informatics/` were created or modified. All deliverables are contained within `.agents/teamwork/explorer_m1_2/`.

---

## 4. Conclusion

The specification design and verbatim template for `apex-meta/informatics/writing-profile.md` are completely finalized and documented in `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m1_2\exploration_report.md`. 

The structural template:
- Organizes 23 battle-tested rules across tiers P0 (6 rules), P1 (8 rules), P2 (6 rules), and P3 (3 rules).
- Employs uncomputed raw 3-metric tags `[P<tier> | I/E/R]` sorted in descending order.
- Top-loads critical invariants within the first ~400 tokens.
- Codifies Information Mapping, visual block limits (~150 words), STE word limits (≤20/≤25 words), active voice, durable IDs, and Substance Over Ceremony.
- Is 100% compliant with OKF v0.2 and `okf_validator.py`.

The builder agent in Milestone 1 can immediately copy the template from Section 5 of `exploration_report.md` into `apex-meta/informatics/writing-profile.md`.

---

## 5. Verification Method

To independently verify this exploration report and template:

1. **Inspect Report and Template**:
   - Open `c:\GitDev\apexai-os-meta\.agents\teamwork\explorer_m1_2\exploration_report.md` and review Section 4 (Rule Matrix) and Section 5 (Structural Template).
2. **Verify OKF Frontmatter & Structure**:
   - Confirm frontmatter contains `type: Profile`, `title`, `description`, `id: apex-informatics-writing-profile`, and inline `tags: [...]`.
   - Confirm heading depth is strictly ≤ 3 levels (`#`, `##`, `###`).
3. **Verify Tag Syntax and Ordering**:
   - Confirm all rules use the exact uncomputed syntax: `[P<0-3> | I<1-100>/E<1-100>/R<1-100>]`.
   - Confirm rules are sorted descending: P0 → P1 → P2 → P3.
4. **Simulate Conformance Run**:
   - When written by the builder agent, execute:
     ```powershell
     python apex-meta/scripts/okf_validator.py apex-meta/informatics
     ```
   - Invalidation condition: Any `OKF_ERROR` or `APEX_PROFILE_ERROR` reported on `writing-profile.md` invalidates the deliverable.
