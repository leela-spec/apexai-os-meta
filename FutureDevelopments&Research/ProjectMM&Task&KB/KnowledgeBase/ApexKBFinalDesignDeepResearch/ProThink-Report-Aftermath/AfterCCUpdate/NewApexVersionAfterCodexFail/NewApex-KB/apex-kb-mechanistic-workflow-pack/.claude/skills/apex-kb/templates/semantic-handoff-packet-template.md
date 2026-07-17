# Apex KB Semantic Handoff Packet

Canonical machine packet: `{{PACKET_JSON_PATH}}`
Generated instruction file: `{{INSTRUCTION_FILE_PATH}}`
Stable prompt template: `{{PROMPT_TEMPLATE_PATH}}`
Batch execution guide: `{{BATCH_GUIDE_PATH}}`

## Identity

- Run: `{{RUN_ID}}`
- Configuration hash: `{{CONFIG_HASH}}`
- Stage: `{{STAGE}}`
- Task mode: `{{TASK_MODE}}`
- Topic: `{{TOPIC_ID}}`

## Executor procedure

1. Read the batch guide.
2. Read the generated instruction file completely.
3. Read the stable prompt template.
4. Read only the exact inputs and source batch named by the instruction file.
5. Write only its allowlisted outputs.
6. Return its exact completion response.

Do not reconstruct instructions from this projection. The generated instruction file is authoritative.

## Exact inputs

{{EXACT_INPUT_FILES}}

## Outputs and write boundary

Required outputs:

{{REQUIRED_OUTPUTS}}

Allowed writes:

{{ALLOWED_WRITES}}

Forbidden writes:

{{FORBIDDEN_WRITES}}

## Validation feedback

{{PRIOR_VALIDATION_FEEDBACK_OR_NONE}}

When feedback exists, repair only the named check, output, and scope.

## Completion response

```text
{{COMPLETION_RESPONSE}}
```

## Stable trigger

```text
Execute the Apex KB instruction file at {{INSTRUCTION_FILE_PATH}} using {{PROMPT_TEMPLATE_PATH}} and {{BATCH_GUIDE_PATH}}; write only declared outputs; return the completion response exactly.
```
