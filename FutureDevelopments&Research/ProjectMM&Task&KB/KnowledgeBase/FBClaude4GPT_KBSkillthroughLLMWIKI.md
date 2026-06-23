Good. I have what I need. The apex-plan package shows `.dr.md`, `.pro.md`, `.v1.md` versioning pattern — this is the live convention. Now delivering the full verdict and build instructions.

---

## Verdict on GPT's Analysis: 82% Correct — Three Additions Required

## ✅ What's Correct and Keep As-Is

- Options A/B/C rejection reasoning — sound
    
- Option E recommendation — correct
    
- Two-phase ingest model (analysis gate before generation) — correct and must be preserved
    
- `does_not_own` list — complete
    
- NARM sequencing (theory first, personal material second, no fusion yet) — correct
    
- `do_not` list in 8.7 — correct and conservative enough
    

---

## ❌ Addition 1: The SKILL.md for apex-kb Must Be Claude-Executable, Not Just Architectural

The GPT output is a design document. It describes what apex-kb _should_ own. It does not produce a Claude-executable SKILL.md. The difference is critical:

**Design document (what GPT produced):**

text

`owns:   - ingest_phase_1_analysis  - operator_review_gate_for_ingest`

**Claude-executable SKILL.md (what you actually need):**

text

`# In SKILL.md Procedure section: # Step 3: Read raw/<subfolder>/<filename>. Extract candidate concepts, #         contradictions, and operator questions. Write output to #         ingest-analysis/<filename>.analysis.md. Do not generate wiki pages yet. # Step 4: Output the analysis file path and halt. Require operator to send #         "approve ingest" before proceeding to Step 5.`

Claude executes **procedures with explicit file paths and halt conditions** — not ownership lists. The GPT analysis correctly identifies what apex-kb should do but stops before specifying _how Claude executes it step by step_.

---

## ❌ Addition 2: The Repo Layout Is Missing `CLAUDE.md` vs `SKILL.md` Distinction

The GPT proposed `apex-meta/kb/<kb-slug>/CLAUDE.md` inside each KB instance folder. This is wrong for two reasons confirmed by live repo :

- `CLAUDE.md` is Claude Code's root context file (repo-level instructions)
    
- `SKILL.md` is the skill package entrypoint under `.claude/skills/`
    
- KB instance folders under `apex-meta/kb/` are **data folders, not skill packages** — they need no SKILL.md or CLAUDE.md
    

The correct distinction:

|Location|File|Purpose|
|---|---|---|
|`.claude/skills/apex-kb/`|`SKILL.md`|Claude-executable skill — triggers, procedure, gates|
|`apex-meta/kb/<slug>/`|_(no SKILL.md)_|Data folder — raw sources, wiki output, manifests|
|`apex-meta/kb/<slug>/`|`README.md` (optional)|Human-readable KB description only|

The skill lives in `.claude/skills/apex-kb/`. The data lives in `apex-meta/kb/`. These are separate. The skill reads and writes to the data folder — it is not inside it.

---

## ❌ Addition 3: The `apex-meta/kb/` Root Needs a Confirmed `apex-meta/` Inventory First

The live repo shows `apex-plan` has `.dr.md` / `.pro.md` / `.v1.md` versioning files — this is an active draft/versioning convention not mentioned in the GPT analysis. Before creating `apex-meta/kb/`, you need the apex-meta directory listing to avoid creating a path that conflicts with existing structure.

---

## Complete Build Instructions for Claude Code

## Step 1 — Confirm apex-meta layout (one read, no writes)

text

`Task: Read directory structure only. No writes. cd C:/GitDev/apexai-os-meta Get-ChildItem apex-meta -Recurse -Depth 2 | Select-Object FullName, PSIsContainer Output: full tree as text. Nothing else.`

Paste result here → I confirm `apex-meta/kb/` is safe to create.

---

## Step 2 — Scaffold the KB data folder (after Step 1 confirmed)

text

`Task: Create apex-kb data folder scaffold only. No skill package files yet. mkdir apex-meta/kb/narm-support-knowledgebase/raw/papers mkdir apex-meta/kb/narm-support-knowledgebase/raw/notes mkdir apex-meta/kb/narm-support-knowledgebase/raw/refs mkdir apex-meta/kb/narm-support-knowledgebase/wiki/concepts mkdir apex-meta/kb/narm-support-knowledgebase/wiki/entities mkdir apex-meta/kb/narm-support-knowledgebase/wiki/summaries mkdir apex-meta/kb/narm-support-knowledgebase/manifests mkdir apex-meta/kb/narm-support-knowledgebase/ingest-analysis mkdir apex-meta/kb/narm-support-knowledgebase/audit/resolved mkdir apex-meta/kb/narm-support-knowledgebase/outputs/queries mkdir apex-meta/kb/narm-support-knowledgebase/log # Create placeholder to make git track empty dirs: New-Item apex-meta/kb/narm-support-knowledgebase/manifests/source-manifest.json -Value '{"kb_slug":"narm-support-knowledgebase","sources":[]}' Verify: list the created tree. Report any mkdir failures verbatim.`

---

## Step 3 — The Canonical apex-kb SKILL.md (ready to write)

This is the Claude-executable version — not a design doc. Paste this directly to Claude Code as the file content for `.claude/skills/apex-kb/SKILL.md`:

text

`` --- name: apex-kb description: Use this skill when the operator asks to ingest a source document into a project knowledge base, query compiled KB content, run a KB lint check, or process an audit item using "ingest kb", "compile kb", "query kb", "lint kb", or "audit kb". --- # Apex KB ## Skill Contract ```yaml skill_contract:   role: project_knowledgebase_compiler  kb_root: apex-meta/kb/  kb_slug_required: true  modes:    - ingest    - query    - lint    - audit  phase_gate: operator_approval_required_between_ingest_phase_1_and_phase_2  raw_sources_policy: never_modify_raw_sources  wiki_policy: llm_generated_synthesis_only_after_operator_approval  scope: one_kb_slug_per_invocation ``` ## Supporting Files ```yaml supporting_files:   - path: references/contract.md    read_when: always  - path: references/rules.md    read_when: before_any_write_or_generation  - path: templates/ingest-analysis-template.md    read_when: ingest_mode_phase_1  - path: templates/wiki-page-template.md    read_when: ingest_mode_phase_2  - path: examples/ingest-example.md    read_when: examples_needed  - path: package-manifest.md    read_when: package_audit ``` ## Procedure 1. Detect mode (ingest / query / lint / audit) and kb_slug from the operator trigger. If either is missing, ask for it before proceeding. 2. Read `references/contract.md` and `references/rules.md`. Confirm the kb_root path `apex-meta/kb/<kb-slug>/` exists before any read or write. 3. For **ingest mode**: read the source file from `raw/<subfolder>/`. Extract candidate concepts, contradictions, open questions, and source metadata. Write the analysis to `ingest-analysis/<filename>.analysis.md` and add a source entry to `manifests/source-manifest.json`. Output the analysis file path and HALT. Do not generate wiki pages until the operator sends "approve ingest". 4. For **ingest phase 2** (after operator approval): generate wiki pages to `wiki/summaries/`, `wiki/concepts/`, and `wiki/entities/` as approved. Rebuild `wiki/index.md`. Write a log entry to `log/YYYY-MM-DD.md`. Do not touch personal material, fusion models, or self-exploration flows. 5. For **query mode**: read `wiki/index.md` first. Read only the wiki pages relevant to the query. Return a compact answer with source pointers. Write the query output to `outputs/queries/<slug>-<YYYY-MM-DD>.md`. 6. For **lint mode**: check that every wiki page has a source pointer, `wiki/index.md` lists all pages, and `manifests/source-manifest.json` has an entry for every file in `raw/`. Report gaps without modifying files. 7. For **audit mode**: read the oldest unresolved item in `audit/`. Propose resolution to the operator. Write to `audit/resolved/` only after operator confirms. 8. Run the completion gate. Surface every unresolved operator_review_needed flag before closing. ## Failure Modes ```yaml failure_modes:   - trigger: kb_slug_not_found    correction: Stop and ask operator to confirm the kb_slug or run scaffold first.  - trigger: raw_source_missing    correction: Report the expected path and ask operator to place the file before ingesting.  - trigger: phase_2_without_approval    correction: Halt and output the phase 1 analysis path. Do not generate wiki pages.  - trigger: wiki_page_without_source_pointer    correction: Flag in lint output. Do not delete the page. Ask operator to review.  - trigger: personal_material_referenced_without_source    correction: Remove the inference and add an operator_review_needed flag.  - trigger: fusion_model_generation_attempted    correction: Halt. Fusion requires explicit operator instruction and both theory and personal indexes exist.  - trigger: write_to_obsidian_folder_requested    correction: Halt. Obsidian writes require explicit operator approval per session.  - trigger: ambiguous_source_path    correction: Stop and ask operator to confirm the exact file path before reading. ``` ## Output Requirements ```yaml output_requirements:   ingest_phase_1:    - analysis_file_path    - source_manifest_entry_added    - candidate_concept_count    - contradiction_count    - operator_review_questions    - halt_confirmation  ingest_phase_2:    - wiki_pages_written    - wiki_index_rebuilt    - log_entry_written    - pages_skipped_with_reason  query:    - answer_with_source_pointers    - query_output_file_path  lint:    - pages_without_source_pointer    - index_gaps    - manifest_gaps  audit:    - item_reviewed    - resolution_proposed    - awaiting_operator_confirmation ``` ## Completion Gate ```yaml completion_gate:   mode_detected: false  kb_slug_confirmed: false  kb_root_path_exists: false  contract_and_rules_loaded: false  raw_sources_not_modified: false  phase_gate_respected: false  no_personal_inference_without_source: false  no_fusion_model_generated: false  no_obsidian_write_without_approval: false  operator_review_flags_surfaced: false  output_file_written: false ``` ``

---

## Step 4 — Write `references/contract.md` and `references/rules.md` only after SKILL.md is operator-approved

Do not write these until you confirm the SKILL.md above is correct. Paste it back here after Claude Code writes it and I will produce the two reference files.

---

## What the GPT Analysis Gets Right But Understates

The **two-phase ingest gate** is the single most important correctness mechanism in the entire design. It must be explicit in the procedure — not just in the architecture notes. The SKILL.md above encodes it as a hard `HALT` in Step 3 with an explicit unlock phrase `"approve ingest"`. This is what makes it actually executable rather than theoretical.