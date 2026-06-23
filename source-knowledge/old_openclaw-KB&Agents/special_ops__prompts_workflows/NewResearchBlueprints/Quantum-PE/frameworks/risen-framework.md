Title: RISEN Prompt Framework — Fields, Examples & When To Use It

URL Source: https://www.promptquorum.com/prompt-engineering/risen-framework

Published Time: 2026-03-16

Markdown Content:
[Home](https://www.promptquorum.com/)/[Frameworks](https://www.promptquorum.com/frameworks)/RISEN

High complexity

Role · Instructions · Steps · End Goal · Narrowing

Built for multi-step enterprise tasks. The Narrowing field keeps AI output on-track and within constraints.

Definition The **RISEN framework** (Role · Instructions · Steps · End Goal · Narrowing) is a prompt engineering structure that breaks your AI request into 5 discrete fields. It is best suited for enterprise workflows with sequential steps.

## The 5 Fields

1

### Role

The expert persona the AI should adopt for this task.

2

### Instructions

Clear directives about how the AI should approach and execute the task.

3

### Steps

The sequential steps the AI should follow, in order.

4

### End Goal

The final deliverable or outcome you want to achieve.

5

### Narrowing

Constraints, exclusions, and guardrails — what the AI should NOT do or include.

## Real Example

Scenario: Building a competitive analysis report

RISEN

Prompt

Role: Senior market analyst. Instructions: Analyze the multi-LLM tool market objectively. Steps: 1) List top 5 competitors, 2) Compare features, 3) Identify gaps. End Goal: A structured report with actionable insights. Narrowing: Do not include tools with fewer than 1000 users. Focus on tools launched after 2023.

## When to Use RISEN

Best for

*   ✓Enterprise workflows with sequential steps
*   ✓Complex processes requiring a specific order of operations
*   ✓Tasks where you need strict constraints on output
*   ✓Multi-stage research or analysis tasks

Not ideal for

*   ✗Simple one-answer questions (use APE or RTF)
*   ✗Tasks focused on tone and voice (use CO-STAR)
*   ✗Creative writing where constraints reduce quality

## Frequently Asked Questions

### What does RISEN stand for?

RISEN stands for Role, Instructions, Steps, End Goal, and Narrowing — a framework designed for sequential, multi-step enterprise tasks.

### What makes the Narrowing field useful?

The Narrowing field lets you define explicit constraints — what to exclude, avoid, or stay within. This prevents AI from going off-topic or including irrelevant content.

### When should I use RISEN instead of SPECS?

Use RISEN when your task has a clear sequence of steps to follow. Use SPECS when you need to define complex technical requirements without a fixed step order.

## Related Frameworks

## Use RISEN inside PromptQuorum

All 9 frameworks are built in. Write, optimize with your own LLM, dispatch to 25+ AI models, and run consensus analysis — free, no account required.

[Join the Waitlist](https://www.promptquorum.com/#waitlist)
