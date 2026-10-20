# Scoped Informatics Rule — Claude Code

When creating, editing, or validating knowledge files under `apex-meta/informatics/` or `apex-meta/SmallSkills/OKF_Format/`:

1. **Routing**: Refer to the canonical standard index at `apex-meta/informatics/index.md`, and follow its `<informatics>` dispatch gates to the one module the active task needs.
2. **Smallest Sufficient Context**: Read only the specific module section relevant to the active task — `writing-profile.md`, `file-architecture.md`, `execution-modes.md`, `anti-drift-rules.md`, or `governance-schemas.md`. Consult `standard.md` or `migration.md` only for scope boundaries, precedence, and migration policy.
3. **Specification Separation**: Distinguish official upstream OKF v0.2 rules (owned by `SmallSkills/OKF_Format/`) from local Apex profile rules. Local profile rules are owned by the modular suite (`WP-XX`, `FA-XX`, `EM-XX`, `AD-XX`, `GS-XX`); `standard.md` §2 defines the precedence ladder and defers to those modules on every subject they cover.
4. **No Invented Requirements**: Never present local metadata conventions as upstream OKF specification requirements.
5. **Deterministic Validation**: Run `apex-meta/scripts/okf_validator.py --target <bundle_path>` on modified bundles before declaring completion.
