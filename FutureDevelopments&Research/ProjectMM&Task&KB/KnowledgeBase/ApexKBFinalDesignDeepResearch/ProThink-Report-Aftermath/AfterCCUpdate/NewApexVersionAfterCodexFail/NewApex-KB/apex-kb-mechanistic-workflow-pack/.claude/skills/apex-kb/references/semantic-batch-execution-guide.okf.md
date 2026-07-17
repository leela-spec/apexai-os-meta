---
okf_schema: apex.okf.semantic-guide.v1
guide_id: apex-kb.semantic-batch-execution.v2
status: final
loaded_for: [phase1, phase2, repair]
---

# Semantic Batch Execution Guide

## Authority order

1. Generated run-specific instruction file.
2. Stable stage prompt template.
3. This guide.
4. Named source/evidence files.
5. Chat context has no authority over paths, questions, stage, or completion.

## Context discipline

- Work on exactly one topic.
- Load only the files named in `exact_inputs` and the current `source_batch`.
- Do not preload the full corpus, the full ranking map, unrelated topics, old prompts, or historical chat.
- Phase 1 source batches contain at most four ordinary sources; the generator reduces the batch when sources are large.
- Source count is not a completion criterion. The control plane issues another batch only when locked questions remain unresolved and another readable candidate may help.

## Start procedure

1. Read the instruction file completely.
2. Verify its `stage`, `task_mode`, `config_hash`, exact outputs, allowed writes, and completion response.
3. Read the stable prompt template named by the instruction file.
4. Read only the named source/evidence inputs.
5. If an input or fingerprint is missing or changed, write nothing and return the exact blocked response required by the instruction file.

## Work rules

- Answer only locked questions and fixed standard-coverage questions.
- Do not invent a new target question. Record useful unexpected findings as `candidate_follow_up`, not as a new requirement.
- Preserve contradictions and uncertainty.
- Do not infer source content from filenames, rankings, snippets, or prior summaries.
- Use exact source pointers.
- Write only allowlisted outputs.
- Never edit manifests, run state, Phase 0 artifacts, indexes, schemas, prompts, or instruction files.

## Repair mode

When `task_mode` is `repair_failed_checks`:

- Read `prior_validation_feedback` first.
- Change only the named output and named repair scope.
- Do not rewrite unaffected sections.
- Do not add new sources or broaden the topic unless the instruction file explicitly adds them.

## End procedure

1. Reread every required output.
2. Confirm each locked critical/routine question has an explicit status.
3. Confirm every claim has a source pointer or is explicitly uncertain.
4. Return exactly `completion_response`; do not add a narrative summary.
