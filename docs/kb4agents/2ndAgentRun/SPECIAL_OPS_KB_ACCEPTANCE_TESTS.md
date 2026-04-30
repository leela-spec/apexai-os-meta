# SPECIAL_OPS_KB_ACCEPTANCE_TESTS

## Purpose

These mechanical acceptance tests verify that each batch of the Special Ops KB package complies with structural, metadata, and source‑integrity requirements. All tests must pass before the package may be recommended for human review.

|Test|Requirement|Pass condition|
|---|---|---|
|**Structure**|Expected package files exist|All required control files and any agent files in scope are present; no missing files|
|**Metadata**|Frontmatter matches schema|YAML frontmatter in every KB file conforms to the specified fields and values|
|**Source access**|Required sources were read or blocked|No final state of “not accessed due to time”; missing primary sources are flagged and affected agents are blocked|
|**Source slice**|Metadata matches actual source use|`source_slice` in each file correctly lists primary, supporting, and evidence sources|
|**Evidence boundary**|Evidence‑only stays evidence‑only|Failure anecdotes and evidence are not promoted into best practices|
|**Essence**|Essence compresses prior files|`ESSENCE.md` files include only content from the preceding four files and do not introduce new doctrine|
|**Citation durability**|Repo‑stable references|Source references in files use durable repo paths or section names; no opaque runtime tokens remain|
|**Diff integrity**|Patches apply to live preimage|Unified diffs apply cleanly against the current repo state (`git apply --check` passes)|
|**Audit honesty**|Verdict matches evidence|`CROSS_AGENT_AUDIT.md` does not claim approval when unresolved gaps or failing tests remain|