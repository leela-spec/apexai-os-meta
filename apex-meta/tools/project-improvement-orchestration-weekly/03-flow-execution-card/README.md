# Module 03 — Flow Execution Card

## Purpose

Make each flow's file the operator's actual execution workspace.

## Locked intent

- one individual Flow Execution Card per represented full flow;
- a full flow has exactly three sprints;
- operator opens and works from this file;
- direct prompt links are part of execution readiness;
- machine metadata must not dominate the card.

## Expected output

The card should contain enough context to execute without reproducing upstream documents:

- flow identity and readiness;
- why today / outcome target;
- exact next action;
- goals and expected outputs;
- available/missing inputs and real dependencies;
- S1, S2, S3 with tasks, prompt access, expected outputs, done conditions and stop/review conditions;
- concise end-of-flow evidence/handoff requirement.

## Known current defect

The current W34 flow packet declares the operator as primary consumer but is dominated by orchestration/schema metadata and repeated upstream context.

## Module work

Fresh module chat lands the detailed human workspace and updates the active flow-generation contracts/templates accordingly.

## Completion

Production implementation -> Master integration PASS -> fresh W34 F1 test at minimum -> operator verifies the card is actually executable.
