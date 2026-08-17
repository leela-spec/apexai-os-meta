# Module 04 — Sprint Prompt Assets

## Purpose

Replace placeholder/repetitive prompt packs with actual prepared execution prompts.

## Locked intent

- prompts are real execution assets, not metadata-only promises;
- full prompt bodies are directly openable/copyable/callable;
- Flow Execution Cards link directly to prompts;
- prompt-generation capability/PromptEngineer should materialize the prompt before a flow is marked ready;
- prompt files should not repeat full flow context already owned by the Flow Card.

## Expected output

Default artifact pattern:

`prompts/<flow>-S1-<slug>.md`
`prompts/<flow>-S2-<slug>.md`
`prompts/<flow>-S3-<slug>.md` when a prompt is actually needed.

Each contains minimal usage context plus the full execution prompt.

## Known current defect

W34 prompt packs use degraded generic/unspecified-provider placeholders and persist a large wrapper even when the actual prompt body is absent.

## Module work

Fresh module chat determines prompt lifecycle, routing/callability and fallback behavior, then integrates real materialization into production.

## Completion

Production integration -> Master verifies flow-readiness dependency and interfaces -> fresh W34 prompt generation test -> operator confirms prompts are directly usable.
