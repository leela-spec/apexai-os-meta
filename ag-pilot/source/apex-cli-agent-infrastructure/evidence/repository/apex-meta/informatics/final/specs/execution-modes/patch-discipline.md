---
type: Adapter
id: ADPT-EXEC-PATCH-v0.2
title: Adapter 3 — Exact-Match Patch Discipline (EM-08)
description: Block-replacement protocol and structured AST patch_intent.v1 for modifying existing files without full rewrites.
tags: [execution-modes, patching, ast, em-08]
status: current
---

## 4. Adapter 3: Exact-Match Patch Discipline

- **EM-08 [P1 | I98/E96/R05] Conditional Patch Trigger**:
  - **IF** modifying any existing repository file → **THEN** apply surgical exact-match replacement blocks (`Mode A`) or AST patch intents (`Mode B`).
  - **IF** exact live target lines have not been inspected in the current session → **THEN** read the target file range first; never guess `<old>` lines from memory.
  - **IF** moving or copying files → **THEN** use deterministic filesystem/git commands (`git mv`, `cp`), never whole-file content rewrites.

### 4.1 Mode A: Block Replacement Protocol (`<file>/<old>/<new>`)
When generating file edits for deterministic executors:

1. **One Change Per Block**: Isolate edits into single distinct operations.
2. **Copy Verbatim**: Copy `<old>` text directly from the live inspected file character-for-character.
3. **No Line Numbers**: Identify edit locations purely by exact text matching.
4. **Disambiguating Context**: Include 1–2 surrounding lines so `<old>` matches a single unique location.
5. **Exact Whitespace**: Preserve all indentation, tabs, and line breaks byte-for-byte.
6. **Explicit Uncertainty**: State uncertainty honestly if exact text is unconfirmed rather than guessing.
7. **Unconfirmed Edits**: Never declare an edit complete until tool output confirms application and test evidence passes.
8. **Iterative Application & Git Sync**: Apply patches iteratively, resolve minor incidental friction pragmatically, and synchronize via `git add`, `git commit`, and `git push` (`git pull --rebase` on non-fast-forward).

```xml
<file>path/to/target/file.md</file>
<old>
exact live lines to replace
including surrounding context
</old>
<new>
replacement lines to insert
including surrounding context
</new>
```

### 4.2 Mode B: Structured AST Patch Intent (`patch_intent.v1`)
When interfacing with automated AST patch tools, output JSON conforming to `patch_intent.v1`. The operative contract is in [governance-schemas.md](governance-schemas.md) §2.2; the authoritative schema is [patch-intent-schema.json](../../../../.claude/skills/deterministic-markdown-patcher2/references/patch-intent-schema.json). This block is the worked example, not a second copy of the schema (`WP-23`):

```json
{
  "schema_version": "patch_intent.v1",
  "intents": [
    {
      "intent_id": "update-auth-port",
      "operation": "replace-once",
      "target": {
        "target_file_guess": "config/services.yaml"
      },
      "hints": {
        "nearby_phrases": ["auth_service:", "port: 8080"]
      },
      "replacement": {
        "content": "  port: 8085\n",
        "content_role": "span_replacement"
      },
      "safety": {
        "require_unique_match": true,
        "fail_on_ambiguity": true,
        "allow_full_file_rewrite": false,
        "max_files_touched": 1
      }
    }
  ]
}
```

---
