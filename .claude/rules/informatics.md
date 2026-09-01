# Scoped Informatics Rule — Claude Code

When creating, editing, or validating knowledge files under `apex-meta/informatics/` or `apex-meta/SmallSkills/OKF_Format/`:

1. **Routing**: Refer to the canonical standard index at `apex-meta/informatics/index.md`.
2. **Smallest Sufficient Context**: Read only the specific section of `standard.md` or `migration.md` relevant to the active task.
3. **Specification Separation**: Distinguish official upstream OKF v0.2 rules (owned by `SmallSkills/OKF_Format/`) from local Apex profile rules (owned by `apex-meta/informatics/standard.md`).
4. **No Invented Requirements**: Never present local metadata conventions as upstream OKF specification requirements.
5. **Deterministic Validation**: Run `apex-meta/scripts/okf_validator.py --target <bundle_path>` on modified bundles before declaring completion.
