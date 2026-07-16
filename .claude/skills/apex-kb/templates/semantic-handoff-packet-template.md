# Apex KB Semantic Handoff Packet

Canonical machine packet: `{{PACKET_JSON_PATH}}`

## Identity

- Run: `{{RUN_ID}}`
- Stage: `{{STAGE}}`
- Topic: `{{TOPIC_ID}}`

## Exact inputs

{{EXACT_INPUT_FILES}}

## Canonical template or schema owners

{{CANONICAL_OWNERS}}

## Outputs

- Exact required output: `{{EXACT_OUTPUT_PATH}}`
{{ADDITIONAL_OUTPUT_PATHS}}

## Write boundary

Allowed writes:

{{ALLOWED_WRITES}}

Forbidden writes:

{{FORBIDDEN_WRITES}}

## Stop conditions

{{STOP_CONDITIONS}}

## Success conditions

{{SUCCESS_CONDITIONS}}

## Required readback

{{REQUIRED_READBACK}}

## Completion response

Return exactly:

```text
{{COMPLETION_RESPONSE}}
```

## Stable trigger

```text
{{SHORT_TRIGGER}}
```
