=== FILE PATCH PROCESS — MANDATORY PROTOCOL ===

TRIGGER: Any request to modify an existing file in the repository.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1 — PREPARE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1.1  READ the target file from the repository via the GitHub connector.
     Store the exact file content AND the current SHA in working context.
     Do NOT rely on memory of what the file contains.

1.2  Identify every change needed. For each change, produce one
     SEARCH/REPLACE block using the following exact format:

     [TARGET: path/to/filename.ext]
     <<<<<<< SEARCH
     [verbatim copy of the lines to be replaced,
      including 3-5 surrounding context lines above and below
      to guarantee uniqueness in the file]
     =======
     [new replacement lines]
     >>>>>>> REPLACE

     RULES FOR SEARCH BLOCKS:
     - Copy lines EXACTLY from the file just read — no paraphrasing
     - Include enough context that the block appears EXACTLY ONCE in the file
     - Never use line numbers
     - Never write a full file rewrite
     - Never write a unified diff
     - Multiple blocks allowed per file; list them sequentially

1.3  Write all SEARCH/REPLACE blocks to a patch file in the repo:
     Filename: [originalfilename].patch.md
     This creates an auditable, reversible record of intent.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2 — VALIDATE (before writing anything)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

2.1  Re-fetch the target file via the GitHub connector (fresh GET).
     Confirm the SHA matches the one stored in Phase 1.
     If SHA changed: discard all blocks, restart from Phase 1.

2.2  For EVERY SEARCH block: verify the exact text appears verbatim
     and EXACTLY ONCE in the freshly fetched file content.

2.3  If any SEARCH block does NOT match:
     - Do NOT apply any blocks
     - Regenerate only the failing block(s) using the fresh file content
     - Repeat from step 2.1

2.4  Only proceed to Phase 3 when ALL blocks are confirmed to match.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3 — APPLY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

3.1  Hold the full validated file content in working memory.
     Apply each SEARCH/REPLACE block SEQUENTIALLY, one at a time,
     replacing the FIRST and ONLY occurrence of each SEARCH text.

3.2  After applying ALL blocks, review the complete resulting file
     mentally: confirm no unintended lines were removed or added.

3.3  Write the full patched file content back to the repository
     via the GitHub connector (PUT), including the current SHA
     to prevent overwrite conflicts.

3.4  If GitHub returns a SHA conflict error:
     - Discard the in-memory result
     - Re-fetch the file (it was modified externally)
     - Restart from Phase 2

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 4 — VERIFY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

4.1  Re-read the committed file from the repository (fresh GET).

4.2  Confirm every intended change is present and no unintended
     changes exist anywhere in the file.

4.3  If verification fails:
     - STOP. Do not attempt automatic correction.
     - Report the discrepancy to the user with exact details.
     - Wait for explicit user instruction before proceeding.

4.4  If verification passes: report success with a one-line summary
     of what was changed and the new commit SHA.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ABSOLUTE PROHIBITIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✗ Never produce unified diffs (@@ hunk headers, +/- lines)
✗ Never write a full file rewrite unless explicitly asked
✗ Never apply patches from memory — always read live file first
✗ Never skip Phase 2 validation under any circumstances
✗ Never auto-retry a failed Phase 4 — always surface to user
✗ Never apply multiple files' patches in one write operation

=== END OF FILE PATCH PROCESS ===