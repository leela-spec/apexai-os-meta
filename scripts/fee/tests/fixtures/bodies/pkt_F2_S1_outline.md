You are drafting a migration outline for a documentation corpus.

Task: produce a staged migration outline moving 1,500 markdown files into a
manifest-driven structure, preserving all existing cross-references.

Context: the corpus currently has no manifest. Cross-references are relative paths.

Output contract: a numbered list of stages. Each stage states its precondition, the
transformation applied, and how the stage is verified before the next one starts.

Constraints: no stage may leave the corpus in a state where cross-references are
broken. Every stage must be independently revertible.

Validation criteria: a reader can execute stage N without reading stage N+1.

Stop when the outline reaches the point where the corpus is fully migrated and
verified. Do not begin implementing any stage.
