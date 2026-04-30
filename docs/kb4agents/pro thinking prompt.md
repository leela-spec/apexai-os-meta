# pro thinking prompt mode: on


You are auditing a previous ChatGPT Agent Mode KB factory run.

MISSION
Create a source-grounded analysis of:
1. What the Agent Mode prompt instructed the agent to do.
2. What the produced output actually contains.
3. What the `chat thinking.md` transcript shows about the agent's reasoning, failures, shortcuts, source access problems, and process quality.
4. Whether the downloadable one-zip artifact/folder likely preserved the full intended output or lost/polluted information during artifact creation.

PRIMARY REPO
Use only this repo unless I attach a zip artifact separately:

https://github.com/leela-spec/MasterOfArts/tree/main

READ THESE FIRST
1. Original Agent Mode prompt:
https://github.com/leela-spec/MasterOfArts/blob/main/docs/kb4agents/ChatGPT_Agent_Mode_KB_Factory_Repo_Index_Prompt.md

2. Thinking / transcript file:
https://github.com/leela-spec/MasterOfArts/blob/main/docs/kb4agents/chat%20thinking.md

3. Produced output folder:
https://github.com/leela-spec/MasterOfArts/tree/main/docs/kb4agents/special_ops_kb_factory_output/special_ops_kb_factory_output

4. Key manifests:
https://github.com/leela-spec/MasterOfArts/blob/main/docs/kb4agents/special_ops_kb_factory_output/special_ops_kb_factory_output/SOURCE_USE_MANIFEST.md
https://github.com/leela-spec/MasterOfArts/blob/main/docs/kb4agents/special_ops_kb_factory_output/special_ops_kb_factory_output/KB_PRODUCTION_MANIFEST.md
https://github.com/leela-spec/MasterOfArts/blob/main/docs/kb4agents/special_ops_kb_factory_output/special_ops_kb_factory_output/CROSS_AGENT_AUDIT.md
https://github.com/leela-spec/MasterOfArts/blob/main/docs/kb4agents/special_ops_kb_factory_output/special_ops_kb_factory_output/SPECIAL_OPS_AGENT_REGISTRY.md

AUDIT METHOD
Do not rewrite the KB files.
Do not improve the package.
Do not browse beyond the linked repo.
Separate facts from inferences.
Cite exact file paths for every finding.
If the transcript suggests something but the output does not prove it, label it as inference.

CORE QUESTIONS
- Did the agent follow the original prompt's source authority rules?
- Did it use only indexed repo files and attached files?
- Did it skip required primary sources?
- Did it falsely mark files inaccessible?
- Did it produce the required folder layout and all required files?
- Did every agent folder contain exactly the required five files?
- Did the manifests accurately describe what happened?
- Did the output show signs of token-limit compression, ad hoc writing, pollution, truncation, repeated boilerplate, missing source slices, or hallucinated doctrine?
- Did the `chat thinking.md` show problematic reasoning, bad source access, unjustified shortcuts, or unstable process?
- Did the final downloadable artifact/folder preserve the intended files cleanly?

ZIP / ARTIFACT CHECK
If I attach the original downloaded zip:
1. Inspect the zip directly.
2. Extract it in a scratch location.
3. Compare extracted file count, paths, filenames, and content against the repo output folder.
4. Report any missing files, extra files, path corruption, truncation, encoding damage, duplicate nesting, or content mismatch.
5. If no zip is attached, say clearly: `ZIP NOT AVAILABLE: only repo output can be audited`.

OUTPUT FORMAT
Create one markdown report with these sections:

# Agent Mode KB Factory Audit

## Executive Verdict
Short verdict: pass / partial pass / fail.

## Instruction vs Output
Compare what the prompt required against what was produced.

## Source Discipline Findings
List source access, source skipping, inaccessible-file claims, attached-file handling, and source-authority problems.

## Thinking Transcript Findings
Summarize what `chat thinking.md` reveals about reasoning quality, shortcuts, confusion, process drift, and failure modes.

## Artifact / Zip Integrity
State whether the zip was available. If available, compare it. If not, explain the limitation and audit the repo folder only.

## Structural Completeness
Check manifests, registry, agent folders, required files, frontmatter, source slices, and naming.

## Content Quality Risks
Focus on drift, hallucination, over-compression, generic boilerplate, missing evidence, and token-limit symptoms.

## Severity-Ranked Findings
Use:
- P0 = invalid package / severe data loss
- P1 = major source or artifact integrity issue
- P2 = important quality or compliance issue
- P3 = minor cleanup / clarity issue

Each finding must include:
- severity
- evidence path
- what happened
- why it matters
- recommended fix

## Final Recommendation
Say whether to accept, revise, rerun, or rerun with a stricter artifact protocol.

IMPORTANT
The most important risk to evaluate is whether the transition from generated text to downloadable folder/zip caused loss, corruption, chaotic file creation, or ad hoc polluted files due to output/token bottlenecks.
a