# Mistakes - Do Not Repeat

This file tracks specific mistakes your agent has made. The goal: mistakes become rules; rules prevent repeats.

## Format
- **Date**: when it happened
- **What went wrong**: specific description
- **Why**: root cause
- **Fix**: what was done
- **Rule**: the standing rule to prevent recurrence

---

## Known Pattern (Seeded for v0)

Python command-name failure in this environment may be a shell-resolution issue rather than a missing interpreter.

### Response Pattern

- test `python` first
- test the verified absolute interpreter path second
- avoid reinstall-first behavior when the absolute path works
- record the successful interpreter path in the run artifact

<!-- Your agent will add entries here as it learns from mistakes -->
