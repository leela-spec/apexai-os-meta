---
name: markdown-table-lint
description: Check and enforce explicit markdown table column alignments
scope: generic
---
# Markdown Table Lint Procedure
1. Scan for pipe-delimited lines.
2. Verify delimiter row contains explicit colons (`:--`, `:-:`, `--:`).
3. Warn on unaligned separator rows.
