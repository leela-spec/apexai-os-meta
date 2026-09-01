---
name: informatics-authoring
description: Minimal deterministic procedure for authoring, editing, or validating knowledge files in governed APEX OS bundles.
user-facing: true
---

# Informatics Authoring Skill

Deterministic operational procedure for creating or editing knowledge concepts within governed APEX OS bundles.

## Procedure

1. **Identify Governed Bundle**:
   - Determine target bundle directory (e.g. `apex-meta/informatics/`, `apex-meta/SmallSkills/OKF_Format/`).
   - Read the bundle root `index.md`.

2. **Retrieve Relevant Standard**:
   - Consult [Apex Informatics Standard](../../../apex-meta/informatics/standard.md) for required frontmatter, block formatting, and technical prose rules.
   - Load only the specific section needed for the current concept.

3. **Author or Patch Concept**:
   - For new concepts: create markdown file with valid YAML frontmatter (`type`, `title`, `description`).
   - For existing concepts: author exact-match `<file>`, `<old>`, `<new>` patch block and apply using `apex-meta/scripts/apply_exact_patch.py`.

4. **Update Bundle Index**:
   - When adding a new concept, add a relative markdown link with a concise description to the bundle root `index.md`.

5. **Run Deterministic Validation**:
   - Execute the validator against the target bundle:
     ```bash
     python apex-meta/scripts/okf_validator.py --target <bundle_directory>
     ```
   - Ensure `OKF Errors: 0` and `Apex Profile Errors: 0`.

6. **Report Completion**:
   - Output machine-readable validation summary and final report.
