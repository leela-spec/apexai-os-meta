# Old-Apex Prompting Doctrine

Purpose: supplemental prompt-craft doctrine for PromptEngineer when designing prompt packets.
Consumer: PromptEngineer (prompt_packet / final_copy_paste_prompt design).
Source basis: `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__prompts_workflows/` (ESSENCE.md, BEST_PRACTICES.md, MISTAKES.md, TEMPLATES.md — item IDs cited per entry). Provider-agnostic items only; all entries validated against the current PromptEngineer skill contract and kept only where not already covered.

## Best practices

- Rule: Freeze the exact deliverable, scope, non-goals, source authority, and stop condition inside the prompt body before any execution instructions. Unstated non-goals and success criteria are the primary cause of scope drift in file- or research-producing prompts. (PW-BP-002)
- Rule: Declare source-authority tiers inside the prompt when multiple sources exist. Raw or current primary files outrank summaries, prior-chat claims, and derived artifacts; if primary sources conflict, the prompt must instruct the executor to stop and surface the conflict rather than pick silently. (PW-MK-002, PW-BP-004)
- Rule: Prompts that produce files, patches, or artifacts must require verification evidence — read-back, diff, file-state check, checklist, or test — before the executor may claim completion. Fluent, well-structured output is not evidence of completion. (PW-MK-004)
- Rule: Scope each prompt to one atomic task: one deliverable or one closed file set, one exact target, explicit input references. Split compound work ("do X and then Y") into separate prompts rather than chaining inside one payload. (PW-BP-010, PW-MK-010)
- Rule: Continuation and follow-up prompts must carry an explicit state block (settled decisions, current target, source refs). Never write prompts that say "continue where we left off" and rely on chat-history reconstruction. (PW-BP-009, PW-MK-009)
- Rule: When the prompt runs in a closed or bounded mode, include a constraint instructing the executor to capture out-of-scope improvement ideas in a dedicated capture section instead of applying them. (PW-BP-005)
- Rule: Treat concrete prompt examples in a prompt pack as behavioral regression tests: each example must demonstrate correct target lock, source discipline, mode choice, validation step, and stop behavior — not serve as decoration. (PW-BP-008)

## Known failure modes

- Avoid: Broad rewrite instructions on long documents ("clean up", "make coherent") without an explicit preservation invariant — they cause silent compression, omissions, and unrelated wording changes. State exactly what must remain untouched. (PW-MK-001)
- Avoid: Blending research, architecture, editing, QA, packaging, and finalization into one opaque prompt pass. If quality gates are mentioned but not sequenced, the executor will substitute a summary for the artifact. (PW-MK-003)

## Templates worth reusing

- Template: Research prompt preflight frame — before the task body, state: (1) frozen target frame: primary objective, non-goals, deferred items, required output sections; (2) source-authority table: each source path, its role (primary/evidence-only/excluded), and behavior if missing; (3) detour budget table: zero budget for locked assumptions, excluded topics, and generic background — convert residual uncertainty into a named validation test instead of open research; (4) output discipline: one artifact only, hard rules before prose, separate certain / likely / open / excluded, stop after output. (PW-TPL-002)
