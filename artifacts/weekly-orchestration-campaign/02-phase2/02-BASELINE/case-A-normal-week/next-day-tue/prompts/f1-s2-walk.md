# Full index validation walk (F1-S2)

**Recommended surface:** session-local agent worker  
**Use when:** after a clean F1-S1 pre-flight; executes the 100%-coverage validation walk over the Lika main SSoT index.  
**Expected return artifact:** findings list with one line per problem plus coverage statement.  
**Routing reference:** default-session-local (unverified pending operator confirmation)

## Prompt

You are executing an SSoT index validation walk.

Inputs:
- `Lika/SSoT/index.yaml` - the index under validation
- filesystem listing of the `Lika/` subtree

Validation rules:
1. Every index entry path must exist on disk.
2. Every file in scope must appear exactly once as canonical, redirect, or archive.
3. redirect entries must have a non-empty redirect_target that itself exists.
4. status values are limited to: canonical | redirect | archive.

Return format:

```
WALK_REPORT
coverage: <n_of_m entries walked>
findings:
- entry: <canonical_id>
  class: MISSING_PATH | DUPLICATE_LISTING | BAD_STATUS | BROKEN_REDIRECT | ORPHAN_FILE
  note: <one line>
(no-findings line if clean)
```

Stop conditions (return early with STOP_REPORT):
- more than 20 findings: stop after 20 and state the total estimate.
- unreadable inputs: name exactly which input failed.

Constraints:
- classify, do not fix anything.
- do not propose archive deletions; archives are operator-reserved.
