Here is the complete failure/drift post-mortem handover.[[ppl-ai-file-upload.s3.amazonaws](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/104634686/de9c861d-5139-49b1-ae2d-8f360daaef89/Anotehr-failed-DRPromptdesign.md?AWSAccessKeyId=ASIA2F3EMEYE4ZYJJDQQ&Signature=ygUEywafh1V8LbsCzvYtnhq7%2FmM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJIMEYCIQCtJZNOvIXW4KOOQ7KtxLj44ykBN1gDpGrCtcmV4wfGAwIhAOGOYg%2FNagVkcakO7AHOu7XmbQnmXOoscXcqd68NmhyZKvMECGgQARoMNjk5NzUzMzA5NzA1IgznkjtqcM0r%2B9J0b3sq0ASn0QomC0GymVCPobTYJ6jGdRxVKVzSkZB3Ea0YOfGhDRkUXba7DPTpvYQnNeTBlv0dm7%2FmBgWM9qYORm9qwzmMJnnTRqJhtaKV8GuFju8DPrRFJlItmAekZWgy2zZ2gHloIyFHXVsjGqF9SufEc30d%2Fz3j1sWqMJn6d3M1udGEklUfVjP0sbjemsHukUTpcZ%2FBSDo10z%2B42IpQ197JLAkgOB78LfXBPpYvBcVLu68WG%2Fq8TJa2i9hgmopnzWgg%2Fr5YrGOLe0S2aNLXoth%2BIDYSiEL8%2F8uE2sr7mbfEXnCA5oj2gb5MTRJp2rLQZKk1%2BL9%2FmcqEwSOlXTTI%2BbHBovFeW4kKyADf0kUDGNIak710V71f6vf1QWk%2F3oHIw9qwrT5oFbDreCIcXfeJughRlNiFL1db8HD1AtVHY3OcwjcR8nPvqNCGpwRl7uYluKejHSxdemiyW%2FHgsSTgclpoUp5izAW1GUJv5Dp4nw%2Fy%2FqwqSbAPqycrL1%2Bal%2BxjmfwTKPoQQWMY26a6%2FgE0yKw5VU0elQ2nJSm4Cy%2Bq4hJuIrMiON5hUTIwlORojMNBzqifLCAXkAKZIZDUnXaY7Mil8JCvsQdrYEI1ktdl6tQMi9xN6Kkrqo%2F4nUlq8PgyD%2FH9twqUI9DhDiCR1Kkie7JR0M2QC36N%2FeuOYLsYNjha2F5ipY1ujBjgdUjpZUwWmOsItekfM7nfsXVvXltni0RsrADmLGq5phbwi04o%2B9AiLR9DhKJm2Iravu4Xtq6t7PhwQgJwiffGhi1Py2GWE0DjfuSuMOKd%2BtEGOpcB2oI1Ey4IHyS5mtgb02fgEvI%2BsHvw8%2F6753%2FCWezX4PSGVgHlZ8q62ds8e%2FyGun4sWX4fIGNCbm6pB9G1SBxzWE5Nb5rAczr%2FfLjcJm2qishiPL6vo3u8tHsjDK8pWbKceTcidZECIyVX24HDNAbH92Z2O4YdibjZ6Mww3hLVlXlSMQOKrYFwaOK6GE3cOh8p2gci1h3FMA%3D%3D&Expires=1782488245)]

---

# HANDOVER: Failure & Drift Post-Mortem

## For the Next Chat — Do Not Repeat These Mistakes

**Project:** Apex KB Phase 0 — Deep Research Prompt Engineering  
**Status:** 3 failed attempts + 1 improved attempt (still untested)  
**Purpose of this document:** Give the next chat a precise, categorized record of every failure mode — both in **target drift** (what the AI produced vs. what was asked) and **prompt engineering errors** (structural choices that caused the AI to fail). This is not a project overview. This is a forensic failure log.

---

## Part 1 — Target Drift Failures (What the AI Kept Getting Wrong)

These are failures in what was _produced_, regardless of what was asked.

## TD-01 — Output B skeleton collapse (CRITICAL, occurred in all 3 attempts)

**What happened:** Output B was the core deliverable — a complete integration map with file creation at macro, meso, and micro levels. In every attempt, the AI produced B as a skeleton table with placeholder text. Examples of placeholder text that survived into final output:

- `[exact heading from repo read]` — never replaced
    
- `[from research]` — never replaced
    
- `extract exact list from Implementation Decision Section 4.1` — literal instruction text left in the output
    

**Why it happened:** The prompt said what the output _should contain_ but did not enforce that it _must be filled from source reads_. The AI treated B as a template to hand off rather than a deliverable to complete.

**Fix applied in last version:** Every B section now has a hard rule: "No `[from research]` placeholders. Fill every field from actual source reads. If unreadable, mark REPO_UNVERIFIED — do not leave it blank."

**Watch for:** Any output B table that still contains bracket placeholders is a failure. Reject it immediately.

---

## TD-02 — Meso level content replaced by description of content (CRITICAL)

**What happened:** The prompt asked for the _actual internal structure_ of new files (headings, field names, contract language). The AI instead wrote descriptions like "this section should contain the acceptance criteria" rather than the acceptance criteria themselves.

**Why it happened:** The prompt used language like "describe the meso structure" rather than "write the meso structure." The AI interpreted "describe" as acceptable.

**Fix applied in last version:** Meso sections now contain literal file content — the actual section headings, the actual YAML fields, the actual contract text — not a description of what those should be.

**Watch for:** Any section where the AI says "this file should contain X" instead of writing X is a meso-level failure.

---

## TD-03 — Micro guidance evaporated entirely (HIGH)

**What happened:** Output C was supposed to contain code-ready YAML with all fields populated plus guidance on argument signatures, error handling patterns, and key function shapes. In every attempt the YAML had empty fields or was identical to the prompt template.

**Why it happened:** The prompt said "fill from research" but the AI had no forcing function to actually do so. It copied the YAML structure from the prompt and left the values as instructions.

**Fix applied in last version:** Every YAML field in Output C now has a non-negotiable population rule. The output C self-check item explicitly says: "Output C C1 YAML spec has no empty fields — fill from research or mark NO_DATA."

**Watch for:** YAML blocks where values are still instruction text (e.g., `parser_strategy: [from F02]`) are failures.

---

## TD-04 — Contamination audit was cosmetic (HIGH)

**What happened:** Every prompt included a contamination audit table. In all three attempts, the table was either empty or contained generic examples that were not extracted from the actual source files. The purpose — catching real drift decisions that had survived into B and C — was never fulfilled.

**Why it happened:** The audit was placed as a step _before_ the outputs, where the AI had not yet done enough reading to populate it. It became a box-ticking exercise.

**Fix applied in last version:** Contamination rules are now a **Contamination Notice** (a standing constraint list embedded in §0), not an audit to produce. This removes the dependency on the AI actually populating the audit — the rules are enforced throughout, not reviewed once.

---

## TD-05 — Web validation was 5 queries instead of 10 (MEDIUM)

**What happened:** All three prompts asked for web validation of tool availability. All three produced a 5-row table covering only the tools listed in the prompt's example. No additional validation was performed.

**Why it happened:** The prompt listed 5 examples and said "use web search for these specific questions." The AI treated the list as exhaustive.

**Fix applied in last version:** 10 specific queries are now listed explicitly with a "run all 10" instruction. The table has a "CONFIRMED/INCONCLUSIVE/CONTRADICTS_DECISION" column to force real validation, not just result recording.

---

## TD-06 — Phase 0 and retrieval layers collapsed (HIGH)

**What happened:** Multiple attempts mixed Phase 0 (deterministic navigation artifacts, V1) with the SQLite FTS5/BM25 retrieval layer (V1.5+). The AI would include retrieval design in Phase 0 scope, or treat FTS5 as an immediate V1 requirement.

**Why it happened:** Several source files (especially CCv2, the Patch Pack) focused heavily on retrieval, and the prompt did not clearly weight Phase 0 as the _only_ current scope. The AI's natural tendency to be "complete" caused it to pull in V1.5 content.

**Fix applied in last version:** §0.2 has explicit scope locks. The retrieval layer section in Output A is labeled "V1.5 scope — note, not immediate" and separated from Phase 0 content. A specific contamination flag (C04) covers this.

---

## TD-07 — Navigation report allowed as skeleton (CRITICAL)

**What happened:** In no attempt did the AI define `phase0-navigation-report.md` as anything other than a skeleton placeholder. This is the most dangerous failure because the navigation report is the primary grounding artifact for Claude before ingest.

**Why it happened:** The prompt said "required sections" but did not say what "required" means — it was interpreted as a checklist, not a content requirement.

**Fix applied in last version:** Contamination flag C13 states explicitly: "phase0-navigation-report.md must contain populated ranked file guidance — never a skeleton." The acceptance criterion in A6 states: "populated ranked file guidance — never a skeleton." The YAML contract in C1 states: "NEVER produce a skeleton; NEVER leave a section blank without explicit 'no data' note."

---

## Part 2 — Prompt Engineering Failures (What Was Wrong With the Prompts Themselves)

These are structural and design errors in how the prompts were written that predictably caused failures.

## PE-01 — "Read all files equally" source list (HIGH)

**What happened:** All three prompts listed 12–15 source files with equal-weight formatting. No priority routing was given.

**Why it happened:** The prompt was written for completeness rather than efficiency. The assumption was that the AI would prioritize intelligently.

**Consequence:** The AI spent disproportionate compute on low-priority/stale files (CCv1, KB-Researchv2, older retrieval specs) and treated them as equally authoritative as F01, the binding Phase 0 decision file.

**Fix:** The new prompt has a strict 4-phase reading plan (Phase A: 6 files, always; Phase B: conditional; Phase C: context only; Phase D: do not read). Files to avoid are explicitly named. This matches the machine-readable index IDX001.

---

## PE-02 — Contamination guard placed as a preamble, not a constraint system (HIGH)

**What happened:** All three prompts opened with an "Anti-Contamination Guard — Read This First" section. This was treated by the AI as an orientation section, not as an enforcement system.

**Why it happened:** The guard was written as rules to internalize before reading, but had no connection to the outputs. The AI read it, acknowledged it, then forgot it during output generation.

**Consequence:** Contaminated decisions (hardcoded KB paths, invented guardrails, version drift) survived into B and C because the guard had no teeth.

**Fix:** The contamination system is now embedded as a standing instruction list (§2) with explicit IDs (C01–C14), severity levels, and an in-output self-check. The AI is instructed to test every decision against the list _before writing it_, not just at the start. Emit `CONTAMINATION_GUARD::[ID]` before correcting.

---

## PE-03 — Output B was structured as a template, not a deliverable (CRITICAL)

**What happened:** All three prompts included Output B as a table with example rows and placeholder text showing the AI what the format should look like. The AI copied the format and filled it with descriptions of what the values should be.

**Why it happened:** The distinction between "this is the format you should follow" and "this is the content you must produce" was not explicit. The AI treated the template as the output.

**Consequence:** B was never actually completed. It was always a structural shell.

**Fix:** The new prompt separates macro, meso, and micro into distinct subsections (B1/B2 for macro, B3/B4 for meso, C for micro guidance). Each section has an explicit "write the actual content — not a description of what to write" rule. Meso sections contain literal example content (actual YAML, actual markdown blocks) that show what populated looks like.

---

## PE-04 — Compute budget was unspecified, causing A to consume B's budget (HIGH)

**What happened:** Output A (research summary) is inherently easier to produce and the AI naturally expanded it. By the time the AI reached B, context budget was constrained and B was compressed.

**Why it happened:** No compute weight guidance was given. The AI defaulted to proportional effort based on token length of instructions (A had more instructions, got more effort).

**Consequence:** B was consistently the weakest output despite being the most important.

**Fix:** Explicit compute weights are now declared at the top: A=30%, B=40%, C=30%. A hard rule states: "If context budget is running low, skip A sections before cutting anything from B." A BUDGET_EXCEEDED flag is defined for when B cannot be completed.

---

## PE-05 — "Forbidden" rules were listed but had no enforcement mechanism (MEDIUM)

**What happened:** Every prompt had a "Forbidden" section listing things like "writing complete scripts" or "architecture re-invention." These were ignored repeatedly.

**Why it happened:** Forbidden rules with no consequence or detection mechanism are treated as soft suggestions.

**Consequence:** The AI re-invented architecture decisions that had already been locked, produced skeleton scripts labeled as complete, and proposed expanding scope.

**Fix:** Forbidden behaviors now have specific detection triggers. Drift triggers emit `DRIFT_DEFENSE::[TAG]` and require an explicit correction, not just avoidance. The self-check at the end (§8) covers the key forbidden behaviors as binary pass/fail checkboxes.

---

## PE-06 — Source authority chain was implicit (HIGH)

**What happened:** All three prompts said "newer file wins when sources conflict" but did not define which file was newest or most authoritative for each decision domain.

**Why it happened:** The chain was left for the AI to infer from file names and dates. The AI inferred incorrectly, sometimes treating CCv2 as more authoritative than F01 for Phase 0 scope decisions.

**Consequence:** Wrong files drove wrong decisions. Specifically, retrieval implementation files (which are rich, detailed, and well-structured) won over the Phase 0 decision file (which is binding but less detailed) because the AI weighted detail over authority.

**Fix:** The binding authority chain is now explicit and ordered: Operator instruction > F01 > F02 > F03 > F06 chain for retrieval. Topic-to-file routing is lifted directly from IDX001 and embedded in the prompt.

---

## PE-07 — GitHub repo reads had no consequence for failure (MEDIUM)

**What happened:** All three prompts said "if file is unreadable, label REPO_UNVERIFIED and continue." The AI consistently filled repo-dependent fields with invented content rather than REPO_UNVERIFIED markers.

**Why it happened:** The consequence of labeling REPO_UNVERIFIED was not defined. The AI found it easier to invent a plausible value than to leave a field empty.

**Consequence:** Patch targets (exact section headings in SKILL.md etc.) were invented, making the patch instructions incorrect.

**Fix:** Every table with repo-dependent fields now has two-state enforcement: either "filled from live repo read" or "REPO_UNVERIFIED" — no other option. The degradation rules are now a hard lookup table with specific responses per failure condition.

---

## PE-08 — The pro-thinking handoff wrapper was embedded in the research prompt (MEDIUM)

**What happened:** Attempt 3 (file:57) embedded a "Pro Thinking prompt wrapper" inside Output C of the Deep Research prompt. This told the AI that its job was to write a _handoff brief_, not to complete Output B/C as real outputs.

**Why it happened:** The operator's workflow uses a two-step process (Deep Research → Pro Thinking). This was correctly understood but incorrectly implemented — the handoff wrapper became the output, replacing the actual code-ready spec.

**Consequence:** Output C became meta-output (instructions for the next AI) instead of the content itself. This is the reason for the explicit operator instruction: "Do not write a Pro Thinking wrapper."

**Fix:** The new prompt explicitly forbids this: "Do not produce a Pro Thinking wrapper or handoff format around the outputs." Output C is the code-ready spec, not a brief for something else.

---

## Part 3 — What the Next Chat Must Carry Forward

The following rules are non-negotiable. If any of them are violated, stop and restart.

|Rule ID|Rule|Failure it prevents|
|---|---|---|

|Rule ID|Rule|Failure it prevents|
|---|---|---|
|R01|Output B must have no bracket placeholders|TD-01|
|R02|Meso sections must contain literal content, not descriptions|TD-02|
|R03|YAML in Output C must have all fields populated|TD-03|
|R04|Contamination rules are standing constraints, not a one-time audit|TD-04|
|R05|Run all 10 web validation queries|TD-05|
|R06|Phase 0 and V1.5 retrieval must never appear in the same scope section|TD-06|
|R07|phase0-navigation-report.md is never a skeleton|TD-07|
|R08|Read only the Phase A spine (6 files); route others by topic|PE-01|
|R09|Compute weights: A=30%, B=40%, C=30%. B wins if budget is tight|PE-04|
|R10|Forbidden behaviors emit DRIFT_DEFENSE tags, not silent avoidance|PE-05|
|R11|Authority chain is explicit: F01 > F02 > F03 > F06 chain for their domains|PE-06|
|R12|Repo unreadable → REPO_UNVERIFIED everywhere it was depended on|PE-07|
|R13|No Pro Thinking wrapper inside the Deep Research output|PE-08|

---

## Part 4 — What "Success" Looks Like

The correct output of the deep research prompt has these properties. Check all of them before accepting any output.

- **Output B, B2 (meso — files to create):** Contains literal YAML/markdown structure of each new file — actual headings, actual fields, actual contract language. No descriptions. No "this section contains X."
    
- **Output B, B4 (meso — patch content):** Contains the actual patch text in the format of the target file, ready to insert. Not "append a block that looks like this."
    
- **Output B, B3 (macro — files to patch):** Has exact section headings from live repo reads. If repo was unreadable: REPO_UNVERIFIED — not an invented heading.
    
- **Output C, C1 (YAML spec):** Every field is populated. NO_DATA is acceptable for truly unknown values. `[from research]` is not acceptable anywhere.
    
- **Output C, C3 (validation shape):** 10 binary validation markers. No partial success category.
    
- **No architecture rediscovery:** All outputs treat locked decisions as locked. No "we could also consider..." language.
    
- **phase0-navigation-report.md:** Described as having populated ranked file guidance in every place it appears. Never described as a skeleton, template, or to-be-filled structure.