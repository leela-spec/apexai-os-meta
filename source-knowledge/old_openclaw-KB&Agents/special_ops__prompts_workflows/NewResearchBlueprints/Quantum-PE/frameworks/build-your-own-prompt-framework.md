Title: Build Your Own Prompt Framework: 5-Step Design Process

URL Source: https://www.promptquorum.com/prompt-engineering/build-your-own-prompt-framework

Published Time: 2026-05-02

Markdown Content:
Frameworks

Last updated:May 2026·12 min read·By [Hans Kuepper](https://www.promptquorum.com/about) · Founder of PromptQuorum, multi-model AI dispatch tool · PromptQuorum

Read in:

When existing frameworks — CO-STAR, CRAFT, RISEN — don't fit your workflow, building a custom prompt framework gives your team a reusable, testable structure. This guide covers when to build vs adopt, the 5-step design process, and a worked example.

**A custom prompt framework is a structured template you design for a specific use case when standard frameworks (CO-STAR, CRAFT, RISEN) require consistent modification.** Build one when you repeat the same 3+ adaptations across every prompt in a given workflow.

⚡ Quick Facts

*   ·Build a custom framework when you add the same 3+ modifications to every prompt in a workflow
*   ·3–6 components: fewer is a technique, more creates friction and gets skipped
*   ·Test on 10 real prompts before documenting — frameworks built from theory fail in practice
*   ·REPAIR framework reduced onboarding from 2 weeks to 3 days for one support team
*   ·Consistency scores improved from 64% to 89% within the first month of using a custom framework
*   ·Cross-model test on GPT-5.5 and Claude 4.6 Sonnet before standardizing

Contents

1.   [Framework vs. Technique](https://www.promptquorum.com/prompt-engineering/build-your-own-prompt-framework#framework_vs_technique)
2.   [When to Build a Custom Framework](https://www.promptquorum.com/prompt-engineering/build-your-own-prompt-framework#when_to_build)
3.   [Building a Custom Framework: 5-Step Process](https://www.promptquorum.com/prompt-engineering/build-your-own-prompt-framework#five_step_process)
4.   [Example: REPAIR Framework for Support Teams](https://www.promptquorum.com/prompt-engineering/build-your-own-prompt-framework#support_example)
5.   [Common Mistakes When Building Custom Frameworks](https://www.promptquorum.com/prompt-engineering/build-your-own-prompt-framework#common_mistakes)
6.   [Frequently Asked Questions](https://www.promptquorum.com/prompt-engineering/build-your-own-prompt-framework#faq)
7.   [Related Reading](https://www.promptquorum.com/prompt-engineering/build-your-own-prompt-framework#related_reading)
8.   [Sources](https://www.promptquorum.com/prompt-engineering/build-your-own-prompt-framework#sources)

## Key Takeaways

*   Build a custom framework when you add the same 3+ components to every prompt in a workflow
*   Use 3–6 components: fewer is a technique, more creates friction and gets skipped
*   Test on 10 real prompts before documenting — frameworks built from theory fail in practice
*   Verify cross-model reliability on GPT-5.5 and Claude 4.6 Sonnet before standardizing
*   Store the framework spec in version control with a template and 3 annotated examples
*   Measure onboarding time and consistency scores to confirm the framework is working

## Framework vs. Technique: What Is the Difference?

📍 In One Sentence

A prompt framework is a structural template defining which components belong in every prompt; a technique is a pattern applied within one of those components.

💬 In Plain Terms

Think of a framework as the scaffold for every prompt — it sets the sections. A technique is what you do inside one section, like asking the model to reason step-by-step.

**A prompt framework is a structural template defining which components belong in every prompt; a technique is a pattern applied within one of those components.** Chain-of-thought prompting is a technique — you apply it inside the "task" component of a framework. CO-STAR is a framework — it defines 6 components that structure the entire prompt.

The distinction matters because frameworks and techniques solve different problems. A framework solves consistency: everyone on your team produces prompts with the same structure. A technique solves capability: it changes how the model approaches a specific step in the reasoning process.

Use an existing framework (CO-STAR, CRAFT, RISEN, RTF) when your task type matches what the framework was designed for. Build a custom one when you repeatedly add the same domain-specific components that existing frameworks don't include.

📌Key distinction

Frameworks solve consistency across the team. Techniques solve capability within a single prompt step. Both are necessary; neither replaces the other.

## When to Build a Custom Prompt Framework

**Build a custom framework when you apply the same 3+ modifications to a standard framework for every prompt in a given workflow.** If you always prepend a compliance anchor, append a citation requirement, and inject a terminology glossary — those are components, not ad-hoc additions.

Signs you need a custom framework:

*   You add the same fields to every prompt that no standard framework includes
*   Your team produces inconsistent prompts despite using CO-STAR or CRAFT
*   New team members take more than a week to write acceptable prompts
*   Your prompts average more than 600 words because you keep explaining the same context
*   You've created a "base prompt" that everyone copies and adapts manually

Signs you should stick with existing frameworks:

*   Your prompts cover diverse, unrelated use cases (no consistent pattern)
*   You write fewer than 10 prompts per week in this workflow
*   An existing framework already fits with minor tweaks
*   Your team has fewer than 3 people writing prompts

## Building a Custom Prompt Framework: 5-Step Process

**The 5-step process: define the goal → identify components → test on 10 prompts → refine → document.** Each step has a clear exit criterion. Don't skip to step 5 — documentation of an untested framework creates false confidence.

1.   1
Define the goal in one sentence

Why it matters: Write exactly what output this framework must reliably produce. Example: "Generate a first-response email to a support ticket that classifies severity, references our policy, and proposes a resolution path." This sentence governs every component decision.

2.   2
Identify 3–6 required components

Why it matters: List the input elements every prompt in this workflow needs. Start by writing 5 prompts from memory, then extract what they share. Common additions beyond standard frameworks: policy anchor, persona constraint, domain vocabulary, output schema, escalation condition.

3.   3
Apply to 10 real prompts

Why it matters: Use actual prompts from your workflow — not invented examples. Score each output: does it meet the goal? Which components were missing? Which were ignored? Run the same prompts on GPT-5.5 and Claude 4.6 Sonnet via PromptQuorum to confirm cross-model reliability.

4.   4
Refine the component list

Why it matters: Remove components that appeared in fewer than 7 of 10 prompts — they belong in specific prompts, not the framework. Add components you improvised in 5+ cases. Rerun the 10-prompt test with the revised framework before moving to step 5.

5.   5
Document and standardize

Why it matters: Write a one-page spec: framework name (acronym optional), definition of each component, a fill-in template with placeholders, and 3 annotated example prompts. Store in version control (Git or PromptHub). Distribute the spec before asking anyone to use the framework.

⚠️Do not skip step 3

Frameworks built without testing 10 real prompts almost always include components that sound important but get skipped under time pressure. Test first, document second.

## Example: Building a Framework for a Support Team

**A support team's custom framework — named REPAIR — consists of 5 components: Role, Escalation condition, Policy anchor, Action path, Intent confirmation.** Standard frameworks like CO-STAR and CRAFT don't include escalation logic or policy anchoring, which every support prompt requires.

The team started by noticing they manually added the same elements to every CO-STAR prompt: the agent's specific role tier, the applicable SLA policy, and a conditional escalation path if the issue exceeded tier-1 scope. After 3 weeks, those additions were formalized as framework components.

The resulting REPAIR template:

*   R (Role): "You are a tier-1 support agent for Product. Your authority covers scope."
*   E (Escalation): "If the issue involves condition, escalate to tier-2. Do not attempt resolution."
*   P (Policy anchor): "Apply policy ID for issue type. Quote the relevant clause in your response."
*   A (Action path): "Classify the issue, confirm understanding, propose resolution, request confirmation."
*   I (Intent confirmation): "End every response with: 'Does this address your issue, or would you like me to escalate?'"

Time to onboard new agents dropped from 2 weeks to 3 days after the REPAIR framework was documented and added to the team's prompt library. Prompt consistency scores (measured via Braintrust evaluation) improved from 64% to 89% within the first month.

Use a custom framework when you can name the pattern clearly and show it applies across your workflow. Avoid naming a framework just to have one — an unnamed, consistent 4-component structure you use daily is a framework even without an acronym.

💡Measure the impact

Track onboarding time and consistency scores before and after deploying a custom framework. If neither improves within 4 weeks, the framework needs refinement — not more documentation.

## Common Mistakes When Building Custom Frameworks

**The most common mistake is building a framework before testing 20+ real prompts manually.** Frameworks built from theory rather than observed patterns include components that sound important but get skipped in practice — which trains the team to ignore framework sections.

❌ Too many components (7+)

**Why it hurts:**Writers skip sections under time pressure, breaking consistency.

**Fix:**Limit to 6 components. Move domain-specific fields to prompt-type extensions, not the core framework.

❌ Copying a standard framework and renaming it

**Why it hurts:**A renamed CO-STAR isn't a custom framework — it's CO-STAR with extra branding overhead.

**Fix:**Only formalize a framework when you have at least 2 components that don't exist in any standard framework.

❌ No test set before documenting

**Why it hurts:**You document a framework that doesn't survive contact with real prompts.

**Fix:**Run 10 real prompts through the draft framework before writing the spec. Adjust based on what breaks.

❌ Not testing across models

**Why it hurts:**A framework that works on GPT-5.5 may produce different output on Claude 4.6 Sonnet if it relies on implicit GPT-specific behaviors.

**Fix:**Test on at least 2 models via PromptQuorum. Document any model-specific adjustments in the framework spec.

❌ No version control

**Why it hurts:**The framework drifts as team members edit it informally, creating inconsistent versions.

**Fix:**Store the framework spec in Git or PromptHub with a version number. Require PR review for any component change.

## Frequently Asked Questions

### What is a prompt framework?

A prompt framework is a structural template that defines which components to include in a prompt and in what order. Examples include CO-STAR (Context, Objective, Style, Tone, Audience, Response) and CRAFT (Context, Role, Action, Format, Target). Frameworks improve consistency and reduce the time spent writing prompts from scratch.

### When should I build a custom framework instead of using CO-STAR or CRAFT?

Build a custom framework when you modify an existing one in the same 3+ ways for every prompt in a workflow. If you always add a policy constraint, a persona anchor, and a domain vocabulary list to CO-STAR — those additions should become first-class components of your own framework, not manual additions.

### How many components should a custom prompt framework have?

Use 3–6 components. Fewer than 3 is a technique, not a framework. More than 6 creates friction — prompt writers skip sections, defeating the purpose. If you need more than 6, split into two specialized frameworks for different task types.

### How do I test if my custom framework is working?

Apply the framework to 10 representative prompts and score outputs against 3 criteria: task completion, format compliance, and quality consistency. A working framework should score 8/10 or better on all three. Use PromptQuorum to test the same framework prompt across GPT-5.5, Claude 4.6 Sonnet, and Gemini 2.5 Pro to confirm it works across models.

### Can a custom framework work across different AI models?

Yes, if designed correctly. Model-agnostic frameworks avoid model-specific syntax and rely on universal components (task definition, constraints, output format). Test your framework on at least GPT-5.5 and Claude 4.6 Sonnet before finalizing — if it needs significant rewording per model, simplify the component definitions.

### How do I name a custom prompt framework?

Naming with an acronym (like REPAIR) makes it memorable and helps onboarding. Choose letters that map to the 3-6 components in order. The acronym test: can a new team member remember all components from the name alone? If not, simplify the component list.

### How do I version a custom framework?

Store each framework version in a dated file (e.g., repair-v1-2026-05.md) in your prompt library directory. Tag breaking changes (component added/removed) as major versions. Tag refinements (definition updates) as minor versions. Document the reason for each change alongside the version file.

### Can I combine multiple existing frameworks?

You can combine components from CO-STAR, CRAFT, and RISEN — but treat the result as a new custom framework, not a hybrid. Name it, document it, and test it as if it were original. Combining without formalizing just creates an undocumented ad-hoc pattern.

## Sources

*   [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
*   [Anthropic Prompt Engineering Documentation](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)
*   [PromptQuorum Multi-Model Testing](https://www.promptquorum.com/features)

## Frequently Asked Questions

### What is the difference between a prompt technique and a prompt framework?

A technique is a single instruction or method (e.g., "think step by step"). A framework is a reusable structure with 3+ components that define how prompts should be built. Frameworks are repeatable; techniques are ad-hoc.

### When should I build a custom framework instead of using CO-STAR, CRAFT, or RISEN?

Build one when you repeatedly apply the same 3+ modifications to an existing framework for every prompt in a workflow. If you always add a policy constraint, domain terminology, and output schema to CO-STAR, those should be components of your own framework.

### Can a custom framework work across different AI models?

Yes, if designed correctly. Avoid model-specific syntax and build around universal components (task, constraints, output format). Test on GPT-5.5 and Claude before finalizing. If the framework needs rewording per model, simplify it.

### How many components should my custom framework have?

Use 3–6 components. Fewer than 3 is a technique, not a framework. More than 6 creates friction and writers skip sections. If you need more, split into two specialized frameworks for different task types.

### How do I test whether my custom framework actually works?

Apply it to 10 representative prompts from your workflow. Score outputs against three criteria: (1) task completion, (2) format compliance, (3) quality consistency. A working framework scores 8/10 or better on all three. Test across multiple models using PromptQuorum.

### How should I name a custom framework?

Use an acronym that maps to your components in order (like REPAIR). The acronym test: can a new team member recall all components from the name alone? If not, simplify your component list.

### Can I combine components from CO-STAR, CRAFT, and RISEN to build my own framework?

Yes, but treat it as a new framework, not a hybrid. Name it, document it, test it, and store it in version control. Combining without formalizing just creates an undocumented ad-hoc pattern.

### How do I version a custom framework?

Store each version in a dated file (e.g., repair-v1-2026-05.md) in your prompt library. Tag breaking changes (component added/removed) as major versions. Tag refinements (definition updates) as minor versions. Document the reason for each change.

### What should I document for my custom framework?

Write a one-page spec: (1) framework name and goal, (2) 3–6 component definitions with examples, (3) a fill-in template, (4) 3 annotated full example prompts using the framework. Keep it in version control alongside your prompt library.

### How do I get my team to use a custom framework I've created?

Start with a 30-minute walkthrough using real task examples. Test together on 2–3 prompts. Create a shareable one-page spec. Track compliance and impact metrics (task success rate, output consistency) for the first month. Iterate based on feedback.

Apply these techniques with a local LLM or your own API keys — PromptQuorum works with any backend.

[Try PromptQuorum free →](https://www.promptquorum.com/)

[← Back to Prompt Engineering](https://www.promptquorum.com/prompt-engineering)
