# Prompt: F1-S2 full index validation walk

inputs:
  - `Lika/SSoT/index.yaml`
  - filesystem listing of `Lika/` subtree
return: WALK_REPORT block (coverage + classified findings)
done: coverage 100%, zero unclassified findings
stop: >20 findings or unreadable input
surface: session-local worker
routing: default-local [exceptions only — see note]

## Prompt

Validate the SSoT index:
1. Every entry path exists on disk.
2. Every in-scope file appears exactly once as canonical/redirect/archive.
3. redirect targets exist and are non-empty.

Return:

```
WALK_REPORT
coverage: <n_of_m>
findings:
- entry: <id> | MISSING_PATH|DUPLICATE_LISTING|BAD_STATUS|BROKEN_REDIRECT|ORPHAN_FILE | <one line>
```

Classify only; fix nothing; archive deletions are operator-reserved.

---
routing-note: this file carries the ONE authoritative route statement for this sprint; cards and the index reference it rather than restating it.
