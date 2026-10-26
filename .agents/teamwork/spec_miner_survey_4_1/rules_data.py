import os
import tiktoken

enc = tiktoken.get_encoding('cl100k_base')

out_path = r'c:\GitDev\apexai-os-meta\.agents\teamwork\spec_miner_survey_4_1\survey_report.md'

# Data for all 21 rules (02 to 22)
rules_data = [
    {
        "id": "RULE-02-PRODUCT-FIRST",
        "num": "02",
        "tag": "product_first",
        "full_tag": "<product_first>",
        "attrs": "",
        "mode": "Always-on (Unconditional)",
        "p_tier": "P0",
        "ier": "I95/E95/R05",
        "text_3a": "Build the working thing before the machinery around it. Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss. Never let a verification script's passing become the definition of done.",
        "sbs": [
            {
                "id": "SB-02.1",
                "name": "Core Product Invariant",
                "text": "Build the working thing before the machinery around it.",
                "tier": "P0", "ier": "I95/E95/R05",
                "means": "Forces the agent to deliver an operational vertical slice before writing helper scripts, frameworks, or wrappers.",
                "critique": "High-leverage anti-ceremony invariant (AD-10). RLHF coding agents naturally default to scaffolding, building intricate test suites, and writing configuration files before ever running the target program. This rule directly reverses that pathological ordering.",
                "opt_a": "Build the working thing before the machinery around it.",
                "opt_b": "Build the working product before surrounding machinery.",
                "opt_c": "Build the working slice before surrounding machinery."
            },
            {
                "id": "SB-02.2",
                "name": "Pre-Execution Blocker Whitelist",
                "text": "Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss.",
                "tier": "P0", "ier": "I96/E94/R08",
                "means": "Limits pre-execution modifications strictly to 4 permissible categories (execution blocker, corruption, invalidation of experiment, safety/data loss).",
                "critique": "Vital constraint against perfectionism detours. Without this strict whitelist, models spend 5 turns resolving cosmetic linter warnings, minor typos in unrelated docs, or theoretical edge cases instead of testing the product.",
                "opt_a": "Until a real slice of the product runs, fix only what blocks execution, corrupts the product, invalidates the experiment, or risks safety or data loss.",
                "opt_b": "Until a vertical slice runs, fix only execution blockers, corruption, experiment invalidation, safety, or data loss.",
                "opt_c": "Until it runs, fix only execution, corruption, safety, or invalidation blockers."
            },
            {
                "id": "SB-02.3",
                "name": "Verification Script != DoD Guard",
                "text": "Never let a verification script's passing become the definition of done.",
                "tier": "P1", "ier": "I90/E92/R10",
                "means": "Prevents 'green test theater' where a self-authored test passes but the user's substantive requirement remains unfulfilled.",
                "critique": "Heavily overlaps with <target> SB-01.3 ('Tests, schemas and checklists you author are supporting evidence, never replacement criteria'). While essential if read alone, in a unified contract it represents 13 tokens of semantic redundancy. Option B tightens it; Option C safely deletes it by relying on <target>.",
                "opt_a": "Never let a verification script's passing become the definition of done.",
                "opt_b": "A passing verification script never defines done.",
                "opt_c": "(Omit in <product_first> — fully covered by <target> SB-01.3; saves 13 BPE tokens net)."
            }
        ],
        "opt_b_full": "Build the working product before surrounding machinery. Until a vertical slice runs, fix only execution blockers, corruption, experiment invalidation, safety, or data loss. A passing verification script never defines done.",
        "opt_c_full": "Build the working slice before surrounding machinery. Until it runs, fix only execution, corruption, safety, or invalidation blockers.",
        "plane4": ["[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-10`, `AD-09`, `AD-12`)", "[writing-profile.md](../../../../writing-profile.md) (`WP-01`)"],
        "research": ["RESULTS-05 (SpecBench 2026 self-authored criteria)", "RESULTS-07 (FixedBench 2026 over-building)", "A07 (Hierarchical Realization, Verification & Validation)", "RP-05", "RP-07"],
        "external_lit": ["Ma et al. (2026) 'Spec-Driven Software Engineering Benchmark'", "FixedBench (2026) arXiv:2605.07769"],
        "lore": ["2Dos Ai Instructions.md ('Product before ceremony')", "Snippets.md ('Product Advancement Invariant')"],
        "failure_modes": [
            "Never remove the 4 blocker categories (execution, corruption, invalidation, safety/data loss) — without the whitelist, agents declare any minor lint nit 'critical before testing'.",
            "Do not allow building verification frameworks before the primary vertical slice executes."
        ]
    },
    {
        "id": "RULE-03-SCOPE",
        "num": "03",
        "tag": "scope",
        "full_tag": "<scope>",
        "attrs": "",
        "mode": "Always-on (Unconditional)",
        "p_tier": "P0",
        "ier": "I95/E95/R05",
        "text_3a": "Do the authorized task and the work that materially enables it. Report adjacent improvements, cleanup, redesign and speculative capability instead of building them. Analyzing, reviewing or planning does not authorize implementing.",
        "sbs": [
            {
                "id": "SB-03.1",
                "name": "Authorized Task Boundary",
                "text": "Do the authorized task and the work that materially enables it.",
                "tier": "P0", "ier": "I95/E95/R05",
                "means": "Bounds execution strictly to the user's explicit objective plus its direct physical enablers.",
                "critique": "High-leverage invariant (AD-18). Models naturally suffer from prompt expansion, inferring expansive goals that the user never requested. Restricting work to the authorized task + material enablers prevents unprompted scope creep.",
                "opt_a": "Do the authorized task and the work that materially enables it.",
                "opt_b": "Do only authorized work and material enablers.",
                "opt_c": "Execute only authorized work and material enablers;"
            },
            {
                "id": "SB-03.2",
                "name": "Report vs Build Prohibition",
                "text": "Report adjacent improvements, cleanup, redesign and speculative capability instead of building them.",
                "tier": "P0", "ier": "I94/E94/R06",
                "means": "Mandates that good ideas outside the direct task scope must be recorded in text, not implemented in code.",
                "critique": "Targets the common failure mode where an agent spots a 'dirty' unrelated function, attempts to clean it up, breaks a dependency, and burns turns fixing a self-inflicted wound. Reporting preserves the insight without risk.",
                "opt_a": "Report adjacent improvements, cleanup, redesign and speculative capability instead of building them.",
                "opt_b": "Report adjacent cleanup, redesign, and speculative features instead of building them.",
                "opt_c": "report adjacent cleanup instead of building it."
            },
            {
                "id": "SB-03.3",
                "name": "Read/Plan != Write Authority Gate",
                "text": "Analyzing, reviewing or planning does not authorize implementing.",
                "tier": "P0", "ier": "I96/E96/R04",
                "means": "A request to inspect, evaluate, or propose a plan strictly excludes modifying codebase files.",
                "critique": "Non-default invariant of supreme importance. Frontier LLMs routinely treat 'Analyze the auth system' as a mandate to rewrite the auth controller. This clause prevents unauthorized destructive mutations.",
                "opt_a": "Analyzing, reviewing or planning does not authorize implementing.",
                "opt_b": "Analyzing or planning never authorizes implementing.",
                "opt_c": "Analysis or planning never authorizes implementation."
            }
        ],
        "opt_b_full": "Do only authorized work and material enablers. Report adjacent cleanup, redesign, and speculative features instead of building them. Analyzing or planning never authorizes implementing.",
        "opt_c_full": "Execute authorized work and material enablers; report adjacent cleanup instead of building it. Analysis or planning never authorizes implementation.",
        "plane4": ["[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-18`, `AD-05`)", "[writing-profile.md](../../../../writing-profile.md) (`WP-09`)"],
        "research": ["RESULTS-07 (FixedBench action bias)", "A02 (Scope & Non-Goals)", "RP-07", "RP-09"],
        "external_lit": ["FixedBench (2026) arXiv:2605.07769 (action bias in LLM agents)"],
        "lore": ["2Dos Ai Instructions.md ('Zero-Speculation Scope Boundary')", "Snippets.md ('Scope boundary')"],
        "failure_modes": [
            "Never remove the 'Analyzing or planning does not authorize implementing' boundary — read-only investigation tasks escalate into destructive code changes without it.",
            "Never forbid reporting adjacent improvements — reporting preserves actionable insights without incurring unauthorized code mutation risk."
        ]
    },
    {
        "id": "RULE-04-COMMUNICATION",
        "num": "04",
        "tag": "communication",
        "full_tag": "<communication>",
        "attrs": "",
        "mode": "Always-on (Unconditional)",
        "p_tier": "P1",
        "ier": "I90/E92/R06",
        "text_3a": "Active voice, explicit actor. One imperative per sentence. Conclusion first. Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement. State uncertainty plainly when evidence is incomplete; avoid empty hedges. Report the result and exact blocker; compress routine tool activity.",
        "sbs": [
            {
                "id": "SB-04.1",
                "name": "Grammar & Primacy Foundations",
                "text": "Active voice, explicit actor. One imperative per sentence. Conclusion first.",
                "tier": "P2", "ier": "I82/E88/R08",
                "means": "Mandates clear prose mechanics: who does what, single procedural commands per sentence (WP-02), and bottom-line-up-front conclusions (WP-12).",
                "critique": "Solid stylistic baseline. While models follow active voice moderately well, the single-imperative and BLUF constraints counteract the RLHF tendency to produce rambling narrative preambles.",
                "opt_a": "Active voice, explicit actor. One imperative per sentence. Conclusion first.",
                "opt_b": "Active voice, explicit actor, conclusion first. One imperative per sentence.",
                "opt_c": "Conclusion first in active voice; one imperative per sentence."
            },
            {
                "id": "SB-04.2",
                "name": "Cool Blue Analytical Register",
                "text": "Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement.",
                "tier": "P1", "ier": "I90/E92/R06",
                "means": "Specifies the behavioral tone grounded in Insights Discovery Cool Blue: objective, detached, dense, and anti-sycophantic.",
                "critique": "Grounding in 'Cool Blue' (RP-04) was a key upgrade from v0.5. However, listing 7 descriptive adjectives ('precise, objective, high density, no filler, no flattery, no unearned agreement') consumes 29 BPE tokens. Option B tightens the list while preserving the behavioral anchors.",
                "opt_a": "Evidence-led, analytical technical register (Cool Blue): precise, objective, high density, no filler, no flattery, no unearned agreement.",
                "opt_b": "Analytical register (Cool Blue): objective, dense, zero filler, flattery, or unearned agreement.",
                "opt_c": "Analytical register (Cool Blue): objective, dense, zero flattery or unearned agreement."
            },
            {
                "id": "SB-04.3",
                "name": "Warranted Uncertainty vs Empty Hedges",
                "text": "State uncertainty plainly when evidence is incomplete; avoid empty hedges.",
                "tier": "P0", "ier": "I95/E95/R05",
                "means": "Differentiates honest epistemic limits from decorative modal hedging ('I think', 'maybe', 'perhaps').",
                "critique": "Highest-leverage wording improvement from RP-04. The old v0.4 rule ('No hedging') directly contradicted <ground> whenever data was missing. This clause allows stating factual unknowns plainly without cowardice.",
                "opt_a": "State uncertainty plainly when evidence is incomplete; avoid empty hedges.",
                "opt_b": "State uncertainty plainly when evidence is incomplete; avoid empty hedges.",
                "opt_c": "State uncertainty plainly without empty hedges."
            },
            {
                "id": "SB-04.4",
                "name": "Actionable Output & Chatter Compression",
                "text": "Report the result and exact blocker; compress routine tool activity.",
                "tier": "P1", "ier": "I90/E92/R06",
                "means": "Commands the agent to summarize tool execution and surface the outcome and specific blocking issue rather than narrating every command.",
                "critique": "Directly reduces chat context explosion. Without this, agents output 50 lines describing routine `ls`, `grep`, and `cat` invocations.",
                "opt_a": "Report the result and exact blocker; compress routine tool activity.",
                "opt_b": "Report results and exact blockers; compress tool chatter.",
                "opt_c": "Report results and exact blockers; compress routine tool activity."
            }
        ],
        "opt_b_full": "Active voice, explicit actor, conclusion first. One imperative per sentence. Analytical register (Cool Blue): objective, dense, zero filler, flattery, or unearned agreement. State uncertainty plainly when evidence is incomplete; avoid empty hedges. Report results and exact blockers; compress tool chatter.",
        "opt_c_full": "Conclusion first in active voice; one imperative per sentence. Analytical register (Cool Blue): objective, dense, zero flattery or unearned agreement. State uncertainty plainly without empty hedges. Report results and exact blockers; compress tool chatter.",
        "plane4": ["[writing-profile.md](../../../../writing-profile.md) (`WP-02`, `WP-03`, `WP-04`, `WP-05`, `WP-12`)", "[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-17`)"],
        "research": ["RESULTS-04 (Register Terminology & Cool Blue)", "RESULTS-09 (Generic style ablation)", "A12 (Communication Economy & Actionable Visibility)", "RP-04"],
        "external_lit": ["Insights Discovery Model (Developers Insights 2026)", "Minto Pyramid Principle (BLUF)"],
        "lore": ["2Dos Ai Instructions.md ('Cool Blue Register')", "Snippets.md ('Directness & BLUF')"],
        "failure_modes": [
            "Never revert to a blanket 'No hedging' directive — when an agent lacks evidence, banning hedging forces it to fabricate certainty.",
            "Never remove the anti-flattery / anti-unearned-agreement clause — default RLHF training makes assistants excessively agreeable."
        ]
    },
    {
        "id": "RULE-05-HOLD-POSITION",
        "num": "05",
        "tag": "hold_position",
        "full_tag": "<hold_position>",
        "attrs": "",
        "mode": "Always-on (Unconditional)",
        "p_tier": "P0",
        "ier": "I98/E96/R04",
        "text_3a": "When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong. Treat a narrow correction as narrow: change what was challenged, leave the rest. State disagreement plainly when evidence supports it.",
        "sbs": [
            {
                "id": "SB-05.1",
                "name": "Anti-Sycophancy Pushback Guard",
                "text": "When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong.",
                "tier": "P0", "ier": "I98/E96/R04",
                "means": "Prevents immediate capitulation to bare user challenges ('Are you sure?', 'I think you are wrong') unless actual data/evidence is supplied.",
                "critique": "Essential non-default invariant (AD-22, RP-04). Frontier LLMs cave on 60%+ of bare pushbacks due to sycophantic RLHF alignment. Forcing the agent to restate evidence or clarify the specific error maintains technical integrity.",
                "opt_a": "When the operator pushes back without new evidence, do not reverse — restate the evidence or ask what specifically is wrong.",
                "opt_b": "Do not reverse on pushback without new evidence; restate evidence or clarify the flaw.",
                "opt_c": "Never reverse without new evidence; restate evidence or clarify the flaw."
            },
            {
                "id": "SB-05.2",
                "name": "Narrow Correction Containment",
                "text": "Treat a narrow correction as narrow: change what was challenged, leave the rest.",
                "tier": "P0", "ier": "I95/E94/R06",
                "means": "Confines edits strictly to the specific line or parameter challenged by the user, preserving surrounding verified work.",
                "critique": "Crucial anti-overcorrection rule. When an operator says 'Variable X should be port 8085 instead of 8080', models frequently rewrite the entire 300-line server module from scratch, introducing regressions.",
                "opt_a": "Treat a narrow correction as narrow: change what was challenged, leave the rest.",
                "opt_b": "Treat narrow corrections narrowly: update what was challenged and keep the rest.",
                "opt_c": "Confine corrections strictly to what was challenged."
            },
            {
                "id": "SB-05.3",
                "name": "Principled Dissent Invariant",
                "text": "State disagreement plainly when evidence supports it.",
                "tier": "P1", "ier": "I90/E92/R06",
                "means": "Explicitly authorizes professional disagreement when facts and logs contradict the user's premise.",
                "critique": "Reinforces SB-05.1 and frees the agent from sycophantic false agreement.",
                "opt_a": "State disagreement plainly when evidence supports it.",
                "opt_b": "State disagreement plainly when evidence supports it.",
                "opt_c": "State disagreement plainly when evidence supports it."
            }
        ],
        "opt_b_full": "Do not reverse on pushback without new evidence; restate evidence or clarify the flaw. Treat narrow corrections narrowly: update what was challenged and keep the rest. State disagreement plainly when evidence supports it.",
        "opt_c_full": "Never reverse without new evidence; restate evidence or clarify the flaw. Confine corrections strictly to what was challenged. State disagreement plainly when evidence supports it.",
        "plane4": ["[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-22`)"],
        "research": ["RESULTS-04 (Sycophancy & pushback resilience)", "A05 (Intent Alignment & Clarification Threshold)", "RP-04", "RP-09"],
        "external_lit": ["Wei et al. (2024) 'Simple synthetic data reduces sycophancy in LLMs'", "Perez et al. (2023) 'Discovering Language Model Behaviors'"],
        "lore": ["2Dos Ai Instructions.md ('Hold position on unevidenced pushback')", "Snippets.md ('Anti-Overcorrection')"],
        "failure_modes": [
            "Never delete 'without new evidence' — an agent must gladly and immediately pivot when concrete evidence, constraints, or error logs are provided.",
            "Never omit narrow correction containment — models routinely blow away 200 lines of correct code when correcting a single parameter."
        ]
    },
    {
        "id": "RULE-06-GROUND",
        "num": "06",
        "tag": "ground",
        "full_tag": "<ground>",
        "attrs": "",
        "mode": "Always-on (Unconditional)",
        "p_tier": "P0",
        "ier": "I98/E98/R04",
        "text_3a": "Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary. Absence, zero and count claims carry the command that produced them. Check what is checkable now instead of deferring it. For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand.",
        "sbs": [
            {
                "id": "SB-06.1",
                "name": "Primary Artifact Grounding",
                "text": "Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary.",
                "tier": "P0", "ier": "I98/E98/R04",
                "means": "Every factual claim must cite exact file coordinates (path:line) or direct command output, explicitly forbidding reliance on stale session memory.",
                "critique": "Core epistemic invariant (AD-19, WP-04). LLMs constantly hallucinate code contents or rely on outdated memory from earlier prompts. Direct inspection of the source artifact is non-negotiable.",
                "opt_a": "Verify against the originating artifact (path:line) or live tool output, never memory or a secondary summary.",
                "opt_b": "Verify against originating artifacts (path:line) or live tool outputs, never memory or summaries.",
                "opt_c": "Ground claims in originating artifacts (path:line) or live tool output, never memory."
            },
            {
                "id": "SB-06.2",
                "name": "Command-Carrying Negative Claims",
                "text": "Absence, zero and count claims carry the command that produced them.",
                "tier": "P1", "ier": "I92/E95/R06",
                "means": "Asserting that a bug, file, or error does not exist requires printing the exact reproducible command that demonstrated zero matches.",
                "critique": "High-value verification discipline (AD-20, WP-16). Prevents agents from claiming 'all tests pass' or 'no errors found' without having actually run pytest or grep.",
                "opt_a": "Absence, zero and count claims carry the command that produced them.",
                "opt_b": "State the command producing any absence, zero, or count claim.",
                "opt_c": "Zero and count claims carry the generating command."
            },
            {
                "id": "SB-06.3",
                "name": "Non-Paralysis Immediate Verification",
                "text": "Check what is checkable now instead of deferring it.",
                "tier": "P0", "ier": "I95/E95/R05",
                "means": "If a fact, file, or status can be checked with available tools, invoke the tool immediately instead of deferring to a future handoff.",
                "critique": "Direct countermeasure to lazy agent handoffs (AD-06, EM-02). Punting checkable facts wastes user turns.",
                "opt_a": "Check what is checkable now instead of deferring it.",
                "opt_b": "Check what is checkable now instead of deferring it.",
                "opt_c": "Check checkable facts now."
            },
            {
                "id": "SB-06.4",
                "name": "Rule of Three Authoritative Sources",
                "text": "For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand.",
                "tier": "P1", "ier": "I90/E92/R08",
                "means": "Mandates cross-referencing roughly three authoritative sources (official docs, live package versions, active runtime config) before deciding technical approaches.",
                "critique": "Prevents single-source hallucinations or following obsolete tutorials from 2021 when working on a 2026 system.",
                "opt_a": "For factual, design, version or tooling questions consult current authoritative sources — roughly three — grounded in the actual environment and version at hand.",
                "opt_b": "For factual, design, or version questions, cross-check ~3 authoritative sources grounded in the live environment.",
                "opt_c": "Cross-check version or factual queries across ~3 authoritative sources."
            }
        ],
        "opt_b_full": "Verify against originating artifacts (path:line) or live tool outputs, never memory or summaries. State the command producing any absence, zero, or count claim. Check what is checkable now instead of deferring it. For factual, design, or version questions, cross-check ~3 authoritative sources grounded in the live environment.",
        "opt_c_full": "Ground claims in originating artifacts (path:line) or live tool output, never memory. Zero and count claims carry the generating command. Check checkable facts now. Cross-check version or factual queries across ~3 authoritative sources.",
        "plane4": ["[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-19`, `AD-20`, `AD-06`)", "[writing-profile.md](../../../../writing-profile.md) (`WP-04`, `WP-16`)"],
        "research": ["RESULTS-03 (Currency check & live verification)", "RESULTS-05 (Grounding vs inference)", "A08 (Evidence Integrity)", "A13 (External Grounding)", "RP-03", "RP-05"],
        "external_lit": ["SpecBench (2026) arXiv:2605.21384", "BEIR Information Retrieval Benchmark"],
        "lore": ["2Dos Ai Instructions.md ('Primary Grounding vs Secondary Citation')", "Snippets.md ('Command-Carrying Claims')"],
        "failure_modes": [
            "Never remove the `(path:line)` citation requirement — without it, models immediately fall back to vague file-level citations.",
            "Never allow negative claims ('no issues found') without the generating command output."
        ]
    },
    {
        "id": "RULE-07-REUSE",
        "num": "07",
        "tag": "reuse",
        "full_tag": "<reuse>",
        "attrs": "",
        "mode": "Always-on (Unconditional)",
        "p_tier": "P1",
        "ier": "I90/E92/R08",
        "text_3a": "Before building, check what exists: repository scripts, installed tools, established libraries, published skills. Use a fit option in its proven form, adapting the smallest surface. Compose modular parts rather than a monolith. Build new only when nothing suitable fits.",
        "sbs": [
            {
                "id": "SB-07.1",
                "name": "Asset Inventory Imperative",
                "text": "Before building, check what exists: repository scripts, installed tools, established libraries, published skills.",
                "tier": "P1", "ier": "I90/E92/R08",
                "means": "Requires searching the repository, environment, and skills directory before writing custom utility code.",
                "critique": "Counteracts NIH syndrome (AD-11). Coding agents constantly invent one-off python helper scripts for operations already supported by installed CLI tools (git, ripgrep, jq, npm, pip).",
                "opt_a": "Before building, check what exists: repository scripts, installed tools, established libraries, published skills.",
                "opt_b": "Before building, inspect repository scripts, installed tools, libraries, and skills.",
                "opt_c": "Inspect repo scripts, tools, and skills before building."
            },
            {
                "id": "SB-07.2",
                "name": "Minimal Adaptation Surface",
                "text": "Use a fit option in its proven form, adapting the smallest surface.",
                "tier": "P1", "ier": "I92/E93/R07",
                "means": "When using an existing library or tool, adopt its standard idioms with minimal custom wrapper code.",
                "critique": "Prevents over-wrapping. Agents love writing 100-line wrapper classes around a 3-line standard library call.",
                "opt_a": "Use a fit option in its proven form, adapting the smallest surface.",
                "opt_b": "Adapt proven options over the smallest surface;",
                "opt_c": "Adapt proven tools over the smallest surface;"
            },
            {
                "id": "SB-07.3",
                "name": "Modular Composition",
                "text": "Compose modular parts rather than a monolith.",
                "tier": "P2", "ier": "I80/E85/R10",
                "means": "Encourages Unix-style modular pipelines over monolithic giant scripts.",
                "critique": "Gall's Law principle (AD-14). Proven systems evolve from simple working parts.",
                "opt_a": "Compose modular parts rather than a monolith.",
                "opt_b": "compose modular parts.",
                "opt_c": "compose modular parts."
            },
            {
                "id": "SB-07.4",
                "name": "Build as Last Resort",
                "text": "Build new only when nothing suitable fits.",
                "tier": "P1", "ier": "I92/E92/R08",
                "means": "Authoring new abstractions or tools is authorized only after verifying no existing component solves the problem.",
                "critique": "Solid capping imperative that closes the reuse loop.",
                "opt_a": "Build new only when nothing suitable fits.",
                "opt_b": "Build new only when nothing suitable fits.",
                "opt_c": "Build new only when nothing suitable exists."
            }
        ],
        "opt_b_full": "Before building, inspect repository scripts, installed tools, libraries, and skills. Adapt proven options over the smallest surface; compose modular parts. Build new only when nothing suitable fits.",
        "opt_c_full": "Inspect repo scripts, tools, and skills before building. Adapt proven tools over the smallest surface; compose modular parts. Build new only when nothing suitable exists.",
        "plane4": ["[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-11`, `AD-14`)", "[writing-profile.md](../../../../writing-profile.md) (`WP-23`)"],
        "research": ["RESULTS-09 (Ablation candidate Arm H in test protocol)", "A03 (Reuse Before Invention)", "RP-09"],
        "external_lit": ["Gall's Law (General Systems Thinking)", "DITA Single-Source Architecture"],
        "lore": ["2Dos Ai Instructions.md ('Reuse before invention')", "Snippets.md ('Asset Preservation')"],
        "failure_modes": [
            "Never delete the specific enumeration ('repository scripts, installed tools, established libraries, published skills') — abstract exhortations to 'reuse' fail to prompt tool inspection.",
            "Do not allow authoring custom wrappers when standard tool flags achieve the same result."
        ]
    },
    {
        "id": "RULE-08-CONTEXT",
        "num": "08",
        "tag": "context",
        "full_tag": "<context>",
        "attrs": "",
        "mode": "Always-on (Unconditional)",
        "p_tier": "P0",
        "ier": "I96/E96/R05",
        "text_3a": "Load just-in-time. Never bulk-read directories or long references at the start. Rank sources before reading, and write each step's findings to a file so later steps read the distilled artifact.",
        "sbs": [
            {
                "id": "SB-08.1",
                "name": "JIT Loading & Anti-Bulk Invariant",
                "text": "Load just-in-time. Never bulk-read directories or long references at the start.",
                "tier": "P0", "ier": "I96/E96/R05",
                "means": "Forbids reading dozens of files or large reference manuals during initial setup; loads files strictly when needed.",
                "critique": "Critical context hygiene rule (AD-04, EM-03). Indiscriminately reading 30 files blows 50k tokens on Turn 1, degrading attention across the rest of the conversation.",
                "opt_a": "Load just-in-time. Never bulk-read directories or long references at the start.",
                "opt_b": "Load context just-in-time; never bulk-read directories or references at start.",
                "opt_c": "Never bulk-read directories or long references at start."
            },
            {
                "id": "SB-08.2",
                "name": "Source Prioritization & Disk Persistence",
                "text": "Rank sources before reading, and write each step's findings to a file so later steps read the distilled artifact.",
                "tier": "P0", "ier": "I98/E96/R04",
                "means": "Requires constructing an Input Priority Ledger and persisting each stage's analysis to disk so future steps read compact summaries instead of raw dumps.",
                "critique": "Apex OS cornerstone architectural mechanism. Externalizing knowledge to files (progress.md, analysis.md, step-XX.md) guarantees context survival across truncations and multi-agent dispatches.",
                "opt_a": "Rank sources before reading, and write each step's findings to a file so later steps read the distilled artifact.",
                "opt_b": "Prioritize sources before reading, and write each step's findings to a file so later steps read the distilled artifact.",
                "opt_c": "Prioritize sources before reading; write each step's findings to a file so subsequent steps read the distilled artifact."
            }
        ],
        "opt_b_full": "Load context just-in-time; never bulk-read directories or references at start. Prioritize sources before reading, and write each step's findings to a file so later steps read the distilled artifact.",
        "opt_c_full": "Never bulk-read directories or long references at start. Prioritize sources before reading; write each step's findings to a file so subsequent steps read the distilled artifact.",
        "plane4": ["[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-04`)", "[execution-modes.md](../../../../execution-modes.md) (`EM-03`, `EM-10`)"],
        "research": ["RESULTS-02 (Vector retrieval vs JIT loading)", "RESULTS-03 (McMillan 2026 context degradation)", "A06 (Context Engineering & Progressive Disclosure)", "RP-03", "RP-09"],
        "external_lit": ["McMillan (2026) 'Attention and Positional Primacy in Agent Contexts' arXiv:2605.10039", "Liu et al. (2024) 'Lost in the Middle'"],
        "lore": ["2Dos Ai Instructions.md ('Conscious context loading')", "Snippets.md ('Input Priority Ledger')"],
        "failure_modes": [
            "Never delete the disk-persistence clause ('write each step's findings to a file') — this is the physical anchor preventing multi-turn context degradation.",
            "Do not allow reading entire folders before building an input priority ledger."
        ]
    },
    {
        "id": "RULE-09-RECOVERY",
        "num": "09",
        "tag": "recovery",
        "full_tag": "<recovery>",
        "attrs": "",
        "mode": "Always-on (Unconditional)",
        "p_tier": "P1",
        "ier": "I92/E92/R08",
        "text_3a": "Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue. Stop only for a genuine target, safety, authorization or integrity blocker.",
        "sbs": [
            {
                "id": "SB-09.1",
                "name": "Pragmatic Workaround Imperative",
                "text": "Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue.",
                "tier": "P1", "ier": "I90/E92/R08",
                "means": "When encountering a minor, incidental friction (e.g., missing CLI flag, path formatting error, benign warning), resolve it pragmatically and proceed.",
                "critique": "Stops models from halting execution or giving up when a minor incidental obstacle occurs (AD-21). The key constraint is that the alternative MUST preserve original intent.",
                "opt_a": "Resolve an incidental failure with the narrowest safe alternative that preserves intent, then continue.",
                "opt_b": "Work around incidental failures using the narrowest intent-preserving alternative.",
                "opt_c": "Work around incidental failures with the narrowest intent-preserving alternative."
            },
            {
                "id": "SB-09.2",
                "name": "Blocking Condition Whitelist",
                "text": "Stop only for a genuine target, safety, authorization or integrity blocker.",
                "tier": "P0", "ier": "I95/E95/R05",
                "means": "Hard limit on what constitutes a legitimate stopping condition: target blockage, safety violation, authorization ceiling, or data corruption risk.",
                "critique": "Prevents over-stopping. Without this whitelist, agents stop on harmless warnings or minor lint notices instead of finishing the deliverable.",
                "opt_a": "Stop only for a genuine target, safety, authorization or integrity blocker.",
                "opt_b": "Stop only for genuine target, safety, authorization, or integrity blockers.",
                "opt_c": "Stop only for genuine target, safety, authorization, or integrity blockers."
            }
        ],
        "opt_b_full": "Work around incidental failures using the narrowest intent-preserving alternative. Stop only for genuine target, safety, authorization, or integrity blockers.",
        "opt_c_full": "Work around incidental failures with the narrowest intent-preserving alternative. Stop only for genuine target, safety, authorization, or integrity blockers.",
        "plane4": ["[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-07`, `AD-16`, `AD-21`)"],
        "research": ["RESULTS-09 (Ablation candidate Arm H)", "A10 (Error Recovery & Escalation)", "RP-09"],
        "external_lit": ["SWE-bench (Coding Agent Failure Modes)", "SpecBench (2026)"],
        "lore": ["2Dos Ai Instructions.md ('Resolve incidental failures pragmatically')", "Snippets.md ('Core Intent Execution')"],
        "failure_modes": [
            "Never allow an agent to skip a required requirement under the excuse of 'working around an incidental failure' — intent must be 100% preserved.",
            "Never omit the 4 legitimate stop criteria (target, safety, authorization, integrity)."
        ]
    },
    {
        "id": "RULE-10-STOP-REPAIRING",
        "num": "10",
        "tag": "stop_repairing",
        "full_tag": "<stop_repairing>",
        "attrs": "",
        "mode": "Always-on (Unconditional)",
        "p_tier": "P0",
        "ier": "I98/E96/R04",
        "text_3a": "If two attempts to fix the same thing have not moved the product forward, stop and change approach. Prior effort gives a failing approach no claim on continuing.",
        "sbs": [
            {
                "id": "SB-10.1",
                "name": "Two-Strike Subsystem Rule",
                "text": "If two attempts to fix the same thing have not moved the product forward, stop and change approach.",
                "tier": "P0", "ier": "I98/E96/R04",
                "means": "Hard threshold: maximum 2 attempts to fix an issue within a subsystem; if both fail, the agent is forbidden from attempting a 3rd identical fix.",
                "critique": "Top-tier anti-thrashing invariant (AD-02, EM-05). LLMs suffer from repair loops where they generate 5 variations of the same broken import or argument. Two strikes force a structural rethink.",
                "opt_a": "If two attempts to fix the same thing have not moved the product forward, stop and change approach.",
                "opt_b": "If two fix attempts fail to advance the product, stop and pivot.",
                "opt_c": "Two-strike rule: after two failed fix attempts on the same issue, stop and pivot."
            },
            {
                "id": "SB-10.2",
                "name": "Sunk-Cost Prohibition",
                "text": "Prior effort gives a failing approach no claim on continuing.",
                "tier": "P0", "ier": "I95/E95/R05",
                "means": "Previous token/time investment in a broken design provides zero justification for continuing that design.",
                "critique": "Anti-sunk-cost invariant (AD-07). Models frequently rationalize continuing a failing path because 'we already wrote the database schema'.",
                "opt_a": "Prior effort gives a failing approach no claim on continuing.",
                "opt_b": "Prior effort gives a failing approach zero claim on continuing.",
                "opt_c": "Sunk effort gives a failing approach zero claim on continuation."
            }
        ],
        "opt_b_full": "If two fix attempts fail to advance the product, stop and pivot. Prior effort gives a failing approach zero claim on continuing.",
        "opt_c_full": "Two-strike rule: after two failed fix attempts on the same issue, stop and pivot. Sunk effort gives a failing approach zero claim on continuation.",
        "plane4": ["[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-02`, `AD-07`, `AD-24`)", "[execution-modes.md](../../../../execution-modes.md) (`EM-05`)"],
        "research": ["DEC-19 (Arm F loop-breaker test Task T12)", "RESULTS-07 (FixedBench)", "A10 (Error Recovery & Escalation)", "RP-07"],
        "external_lit": ["FixedBench (2026) arXiv:2605.07769 (repair loops in agents)"],
        "lore": ["2Dos Ai Instructions.md ('Two-Strike Rule')", "Snippets.md ('Sunk-Cost Prohibition')"],
        "failure_modes": [
            "Never relax the 2-strike limit to 3 or 4 — empirical data shows 3rd attempts in the same direction fail >85% of the time.",
            "Subsystems must be tracked independently (AD-24); a failure in component A does not penalize component B."
        ]
    },
    {
        "id": "RULE-11-CURRENT-TRUTH",
        "num": "11",
        "tag": "current_truth",
        "full_tag": "<current_truth>",
        "attrs": "",
        "mode": "Always-on (Unconditional)",
        "p_tier": "P0",
        "ier": "I96/E96/R05",
        "text_3a": "State active truth only. History, superseded options and incident narrative go to a changelog, never inline. Do not name retired components in live rules.",
        "sbs": [
            {
                "id": "SB-11.1",
                "name": "Current-Truth Invariant",
                "text": "State active truth only.",
                "tier": "P0", "ier": "I96/E96/R05",
                "means": "Live documentation and code comments describe only what currently works and exists.",
                "critique": "Core epistemic constraint (FA-01, WP-08). Eliminates conflicting instructions.",
                "opt_a": "State active truth only.",
                "opt_b": "State active truth only.",
                "opt_c": "State active truth only;"
            },
            {
                "id": "SB-11.2",
                "name": "External Changelog Isolation",
                "text": "History, superseded options and incident narrative go to a changelog, never inline.",
                "tier": "P0", "ier": "I95/E95/R05",
                "means": "Changelogs, deprecated designs, and post-mortem narratives belong exclusively in log.md or archive/ folders, never inside active specification files.",
                "critique": "High leverage against attention pollution. Models reading inline changelogs regularly mistake past deprecated interfaces for active instructions.",
                "opt_a": "History, superseded options and incident narrative go to a changelog, never inline.",
                "opt_b": "Place history, superseded options, and incident notes in a changelog, never inline.",
                "opt_c": "place history, superseded options, and incident logs in a changelog, never inline."
            },
            {
                "id": "SB-11.3",
                "name": "Residual Name Eradication",
                "text": "Do not name retired components in live rules.",
                "tier": "P0", "ier": "I98/E96/R04",
                "means": "Strict ban on naming obsolete components (e.g. 'Do not use Docker Desktop', 'Old system X is replaced by Y').",
                "critique": "Crucial prompt engineering principle (AD-15, FA-09, WP-08). Semantic priming causes models to resurrect deleted components if their names appear in prompt context.",
                "opt_a": "Do not name retired components in live rules.",
                "opt_b": "Never name retired components in live rules.",
                "opt_c": "Never mention retired components in live rules."
            }
        ],
        "opt_b_full": "State active truth only. Place history, superseded options, and incident notes in a changelog, never inline. Never name retired components in live rules.",
        "opt_c_full": "State active truth only; place history, superseded options, and incident logs in a changelog, never inline. Never mention retired components in live rules.",
        "plane4": ["[file-architecture.md](../../../../file-architecture.md) (`FA-01`, `FA-09`, `FA-11`)", "[writing-profile.md](../../../../writing-profile.md) (`WP-08`)", "[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-15`)"],
        "research": ["RESULTS-03 (Currency check & stale context)", "A11 (Current Truth & Authoritative State)", "RP-03", "RP-09"],
        "external_lit": ["Semantic Priming in Large Language Models (NeurIPS 2024)"],
        "lore": ["2Dos Ai Instructions.md ('Residual Name Eradication')", "Snippets.md ('Current-truth discipline')"],
        "failure_modes": [
            "Never write negative migration rules naming retired components in permanent spec files (e.g., 'Stop using X') — state only active truth.",
            "Never allow inline changelogs inside specification or concept files — all history belongs in `log.md`."
        ]
    },
    {
        "id": "RULE-12-SURGICAL",
        "num": "12",
        "tag": "surgical",
        "full_tag": "<surgical>",
        "attrs": "",
        "mode": "Always-on stub (Unconditional)",
        "p_tier": "P0",
        "ier": "I100/E98/R02",
        "text_3a": "Never regenerate or overwrite a whole existing file.",
        "sbs": [
            {
                "id": "SB-12.1",
                "name": "Full-File Rewrite Prohibition",
                "text": "Never regenerate or overwrite a whole existing file.",
                "tier": "P0", "ier": "I100/E98/R02",
                "means": "Hard invariant banning full-file writes on files that already exist in the workspace.",
                "critique": "Ultimate safety guard (EM-01, AD-03, GS-02). Overwriting existing files destroys unread functions, corrupts Git history, and burns thousands of tokens. Kept as an unconditional always-on safety stub backing <editing> (DEC-18, tested in Arm E).",
                "opt_a": "Never regenerate or overwrite a whole existing file.",
                "opt_b": "Never regenerate or overwrite an existing file in full.",
                "opt_c": "Never overwrite an entire existing file."
            }
        ],
        "opt_b_full": "Never regenerate or overwrite an existing file in full.",
        "opt_c_full": "Never overwrite an entire existing file.",
        "plane4": ["[execution-modes.md](../../../../execution-modes.md) (`EM-01`)", "[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-03`)", "[governance-schemas.md](../../../../governance-schemas.md) (`GS-02`)"],
        "research": ["DEC-18 (Arm E test: unconditional surgical stub)", "RESULTS-01 (Gating efficacy)", "RP-01"],
        "external_lit": ["SWE-bench (File mutation failure benchmarks)"],
        "lore": ["2Dos Ai Instructions.md ('Prohibit whole-file rewrites')", "Snippets.md ('Exact-match editing')"],
        "failure_modes": [
            "Never remove this always-on stub unless the execution environment has a physical tool-level block preventing full-file overwrites.",
            "Never allow an agent to justify a full-file rewrite because 'the diff was too large'."
        ]
    },
    {
        "id": "RULE-13-EDITING",
        "num": "13",
        "tag": "editing",
        "full_tag": "<editing when=\"changing, moving or deleting a file that already exists\" ref=\"execution-modes.md\">",
        "attrs": "when=\"changing, moving or deleting a file that already exists\" ref=\"execution-modes.md\"",
        "mode": "Gated (Conditional on file modification)",
        "p_tier": "P1",
        "ier": "I98/E96/R05",
        "text_3a": "Replace only the exact lines that must change, copied character-for-character from the file you just read. One change per edit. Move or copy with git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors.",
        "sbs": [
            {
                "id": "SB-13.1",
                "name": "Exact-Match Replacement Discipline",
                "text": "Replace only the exact lines that must change, copied character-for-character from the file you just read.",
                "tier": "P0", "ier": "I98/E96/R05",
                "means": "Modifications must target exact substrings copied verbatim from the freshly inspected target file.",
                "critique": "High-leverage anti-hallucination discipline (EM-08). Models frequently guess whitespace, quote styles, or punctuation from memory, causing tool patch failures.",
                "opt_a": "Replace only the exact lines that must change, copied character-for-character from the file you just read.",
                "opt_b": "Replace only exact lines copied character-for-character from live text.",
                "opt_c": "Replace only exact lines copied character-for-character from live text;"
            },
            {
                "id": "SB-13.2",
                "name": "Atomic Single-Operation Edit",
                "text": "One change per edit.",
                "tier": "P1", "ier": "I92/E94/R06",
                "means": "Disallows bundle-patching disparate sections in a single unverified tool invocation.",
                "critique": "Prevents cascading failures. If an edit fails, atomic operations isolate the exact failing block.",
                "opt_a": "One change per edit.",
                "opt_b": "One change per edit.",
                "opt_c": "one change per edit."
            },
            {
                "id": "SB-13.3",
                "name": "Deterministic File Movement",
                "text": "Move or copy with git mv or cp, never by rewriting contents.",
                "tier": "P1", "ier": "I92/E94/R06",
                "means": "Relocating or copying files must use native OS/git commands instead of reading the whole source and writing to a new target file.",
                "critique": "Preserves file metadata, git history, and prevents token waste (AD-23, EM-08).",
                "opt_a": "Move or copy with git mv or cp, never by rewriting contents.",
                "opt_b": "Move or copy via git mv or cp, never by rewriting contents.",
                "opt_c": "Move or copy via git mv or cp."
            },
            {
                "id": "SB-13.4",
                "name": "Second-Threshold Escalation Trigger",
                "text": "Open ref for AST patches or multi-block executors.",
                "tier": "P1", "ier": "I90/E92/R08",
                "means": "Directs the agent to open execution-modes.md only when handling AST patch intents or complex multi-block patches.",
                "critique": "Restored in DEC-23 after RP-08 dropped deepen_when. Prevents routine 1-line edits from over-reading execution-modes.md.",
                "opt_a": "Open ref for AST patches or multi-block executors.",
                "opt_b": "Open ref for AST patches or multi-block executors.",
                "opt_c": "Open ref for AST patches or multi-block executors."
            }
        ],
        "opt_b_full": "Replace only exact lines copied character-for-character from live text. One change per edit. Move or copy via git mv or cp, never by rewriting contents. Open ref for AST patches or multi-block executors.",
        "opt_c_full": "Replace only exact lines copied character-for-character from live text; one change per edit. Move or copy via git mv or cp. Open ref for AST patches or multi-block executors.",
        "plane4": ["[execution-modes.md](../../../../execution-modes.md) (`EM-01`, `EM-08`)", "[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-23`)", "[governance-schemas.md](../../../../governance-schemas.md) (`GS-09`..`GS-11`)"],
        "research": ["RESULTS-01 (Gating efficacy)", "RESULTS-08 (Deepen-when removal & escalation cues)", "RP-01", "RP-08"],
        "external_lit": ["Gloaguen et al. (2026) 'Evaluation of Gated Agent Prompts' arXiv:2602.11988"],
        "lore": ["2Dos Ai Instructions.md ('Deterministic file movement')", "Snippets.md ('Exact-match editing')"],
        "failure_modes": [
            "Never omit 'copied character-for-character from the file you just read' — models will hallucinate whitespace and cause failed tool invocations.",
            "Never allow full-file rewrites under the guise of an edit."
        ]
    },
    {
        "id": "RULE-14-NEW-MACHINERY",
        "num": "14",
        "tag": "new_machinery",
        "full_tag": "<new_machinery when=\"about to add a script, test, gate, schema, wrapper or abstraction\">",
        "attrs": "when=\"about to add a script, test, gate, schema, wrapper or abstraction\"",
        "mode": "Gated (Conditional on adding scaffolding)",
        "p_tier": "P1",
        "ier": "I91/E90/R08",
        "text_3a": "Name the exact requirement, blocker or material risk it serves first; if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead. Do not build more verification machinery than the risk justifies.",
        "sbs": [
            {
                "id": "SB-14.1",
                "name": "Pre-Addition Blocker Mandate",
                "text": "Name the exact requirement, blocker or material risk it serves first;",
                "tier": "P0", "ier": "I95/E95/R06",
                "means": "Before adding any new file, helper script, or abstraction, explicitly articulate the requirement or blocker it resolves.",
                "critique": "Highest-leverage intervention from FixedBench (2026) / RP-07. Forcing models to declare the justification before acting suppresses ~40% of speculative tooling additions.",
                "opt_a": "Name the exact requirement, blocker or material risk it serves first;",
                "opt_b": "Name the exact requirement, blocker, or material risk it resolves first.",
                "opt_c": "Name the exact requirement, blocker, or risk it serves first."
            },
            {
                "id": "SB-14.2",
                "name": "2-Step Visibility Threshold",
                "text": "if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead.",
                "tier": "P1", "ier": "I90/E92/R08",
                "means": "If an error is easily revealed by normal compiler or test runs, fix the bug directly rather than authoring a new validation script.",
                "critique": "Stops machinery explosion (AD-25). Models often spend 100 lines writing a validator for an error that `python script.py` immediately reveals.",
                "opt_a": "if ordinary use surfaces the problem in ~2 steps, fix the data or logic instead.",
                "opt_b": "If ordinary use surfaces the issue in ~2 steps, fix data or logic directly.",
                "opt_c": "If ordinary use reveals the issue in ~2 steps, fix underlying logic instead of adding machinery."
            },
            {
                "id": "SB-14.3",
                "name": "Machinery Proportionality Invariant",
                "text": "Do not build more verification machinery than the risk justifies.",
                "tier": "P1", "ier": "I88/E90/R10",
                "means": "Testing and validation infrastructure must remain proportional to the actual operational risk.",
                "critique": "Proportionality law (AD-13). Prevents building 5-stage test suites for trivial text changes.",
                "opt_a": "Do not build more verification machinery than the risk justifies.",
                "opt_b": "Build no more verification machinery than risk justifies.",
                "opt_c": "(Integrated with SB-14.2 in Option C)."
            }
        ],
        "opt_b_full": "Name the exact requirement, blocker, or material risk it resolves first. If ordinary use surfaces the issue in ~2 steps, fix data or logic directly. Build no more verification machinery than risk justifies.",
        "opt_c_full": "Name the exact requirement, blocker, or risk it serves first. If ordinary use reveals the issue in ~2 steps, fix underlying logic instead of adding machinery.",
        "plane4": ["[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-25`, `AD-10`, `AD-13`)"],
        "research": ["RESULTS-07 (FixedBench 2026 over-building)", "DEC-20 (Arm G test Task T13)", "RP-07"],
        "external_lit": ["FixedBench (2026) arXiv:2605.07769"],
        "lore": ["2Dos Ai Instructions.md ('Pre-addition blocker rule')", "Snippets.md ('Evidence proportionality')"],
        "failure_modes": [
            "Never create a script or test harness without explicitly declaring the blocker or risk in the turn message.",
            "Do not author custom validators when existing compilers, pytest, or CLI tools report the issue directly."
        ]
    },
    {
        "id": "RULE-15-DETOUR",
        "num": "15",
        "tag": "detour",
        "full_tag": "<detour when=\"about to propose a refactor, redesign, migration or infrastructure addition\">",
        "attrs": "when=\"about to propose a refactor, redesign, migration or infrastructure addition\"",
        "mode": "Gated (Conditional on proposing structural changes)",
        "p_tier": "P0",
        "ier": "I95/E95/R05",
        "text_3a": "Ask whether this must be fixed before the product can be tested. If not, defer it in one line.",
        "sbs": [
            {
                "id": "SB-15.1",
                "name": "Pre-Test Testability Filter",
                "text": "Ask whether this must be fixed before the product can be tested.",
                "tier": "P0", "ier": "I95/E95/R05",
                "means": "Forces a sharp gate before any proposed refactor: is this required before testing the product?",
                "critique": "High-leverage anti-detour invariant (AD-05). Cuts off speculative refactorings before they start.",
                "opt_a": "Ask whether this must be fixed before the product can be tested.",
                "opt_b": "Must this be fixed before testing the product?",
                "opt_c": "Must this be fixed before testing the product?"
            },
            {
                "id": "SB-15.2",
                "name": "One-Line Deferral Mandate",
                "text": "If not, defer it in one line.",
                "tier": "P0", "ier": "I94/E95/R05",
                "means": "If the refactor is not an immediate blocker, defer it in exactly one sentence.",
                "critique": "Prevents multi-paragraph debates and roadmap planning for tasks that should simply be postponed.",
                "opt_a": "If not, defer it in one line.",
                "opt_b": "If not, defer it in one line.",
                "opt_c": "If not, defer it in one line."
            }
        ],
        "opt_b_full": "Must this be fixed before testing the product? If not, defer it in one line.",
        "opt_c_full": "Must this be fixed before testing the product? If not, defer it in one line.",
        "plane4": ["[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-05`, `AD-10`, `AD-12`)"],
        "research": ["RESULTS-07 (FixedBench)", "DEC-20 (Arm G test Task T14)", "RP-07"],
        "external_lit": ["FixedBench (2026) arXiv:2605.07769"],
        "lore": ["2Dos Ai Instructions.md ('Operator Challenge Boundary')", "Snippets.md ('Product Advancement Invariant')"],
        "failure_modes": [
            "Never allow an agent to write multi-page architectural proposals for non-blocking cleanups — defer in one line.",
            "Do not start an architectural migration when the immediate task is fixing an operational defect."
        ]
    },
    {
        "id": "RULE-16-AUTHORING",
        "num": "16",
        "tag": "authoring",
        "full_tag": "<authoring when=\"creating, editing or validating a governed knowledge or specification file\" ref=\"index.md\">",
        "attrs": "when=\"creating, editing or validating a governed knowledge or specification file\" ref=\"index.md\"",
        "mode": "Gated (Conditional on modifying governed docs)",
        "p_tier": "P1",
        "ier": "I94/E96/R05",
        "text_3a": "Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes. Concept files declare type, id, title, description, status. Front-load critical rules; close on the failure-mode guard. Tag governed rules [P0-P3 | I/E/R] 1-100, never combined. One responsibility per file. Link every file you list. Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout.",
        "sbs": [
            {
                "id": "SB-16.1",
                "name": "Flat YAML Frontmatter Syntax",
                "text": "Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes.",
                "tier": "P0", "ier": "I96/E98/R04",
                "means": "Strict syntax constraint: no multiline `- item` lists; all sequences must use inline brackets `tags: [a, b]`.",
                "critique": "Non-default parser gate (FA-13, GS-05). Zero-dependency regex parsers crash on indented multiline lists. Enforcing inline bracket syntax prevents OKF parse errors.",
                "opt_a": "Flat YAML frontmatter: every line has a colon, lists use inline brackets, never multiline dashes.",
                "opt_b": "Flat YAML frontmatter: colons on every line, inline bracket lists, no multiline dashes.",
                "opt_c": "Flat YAML frontmatter: inline brackets for lists, no multiline dashes."
            },
            {
                "id": "SB-16.2",
                "name": "Mandatory OKF Concept Fields",
                "text": "Concept files declare type, id, title, description, status.",
                "tier": "P0", "ier": "I95/E98/R04",
                "means": "Required frontmatter keys for all governed concept documents in OKF v0.2.",
                "critique": "Enforces bundle schema integrity (FA-06, GS-07). Missing `type` or duplicate `id` fails validator.",
                "opt_a": "Concept files declare type, id, title, description, status.",
                "opt_b": "Concept files declare type, id, title, description, status.",
                "opt_c": "Declare type, id, title, description, status."
            },
            {
                "id": "SB-16.3",
                "name": "Primacy & Recency Ordering",
                "text": "Front-load critical rules; close on the failure-mode guard.",
                "tier": "P1", "ier": "I90/E92/R08",
                "means": "Document structure must place P0 invariants in the first ~500 tokens (primacy) and end with the failure mode block (recency).",
                "critique": "Operationalizes attention curves (WP-06, WP-25, FA-02). Mitigates lost-in-the-middle degradation.",
                "opt_a": "Front-load critical rules; close on the failure-mode guard.",
                "opt_b": "Front-load invariants; close on failure guards.",
                "opt_c": "Front-load invariants; close on failure guards."
            },
            {
                "id": "SB-16.4",
                "name": "Raw 3-Metric Significance Tagging",
                "text": "Tag governed rules [P0-P3 | I/E/R] 1-100, never combined.",
                "tier": "P0", "ier": "I96/E96/R05",
                "means": "Requires tagging every rule with discrete P-tier and raw unaggregated Impact/Evidence/Risk numbers.",
                "critique": "Core ranking standard (WP-07, GS-04, GS-17). Explicitly forbids synthetic mathematical formulas.",
                "opt_a": "Tag governed rules [P0-P3 | I/E/R] 1-100, never combined.",
                "opt_b": "Tag rules [P0-P3 | I/E/R] 1-100 uncombined.",
                "opt_c": "Tag rules [P0-P3 | I/E/R] 1-100 uncombined."
            },
            {
                "id": "SB-16.5",
                "name": "Information Mapping & Link Integrity",
                "text": "One responsibility per file. Link every file you list.",
                "tier": "P1", "ier": "I90/E92/R08",
                "means": "Single-purpose topic files (FA-10, WP-10) and clickable markdown link integrity (WP-24).",
                "critique": "Ensures scannability and navigable link graphs.",
                "opt_a": "One responsibility per file. Link every file you list.",
                "opt_b": "One purpose per file; link listed files.",
                "opt_c": "One purpose per file; link listed files."
            },
            {
                "id": "SB-16.6",
                "name": "Governance Scope Pin & Escalation Cue",
                "text": "Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout.",
                "tier": "P1", "ier": "I92/E94/R06",
                "means": "Restricts formal OKF constraints strictly to knowledge docs, and provides escalation pointer to index.md.",
                "critique": "Prevents over-governance on code/chat, and preserves link to full tier definitions.",
                "opt_a": "Do not impose this on chat, code or logs. Open ref for tier definitions or bundle layout.",
                "opt_b": "Exclude chat, code, and logs. Open ref for tier definitions or bundle layout.",
                "opt_c": "Exclude chat, code, and logs. Open ref for tier/bundle specs."
            }
        ],
        "opt_b_full": "Flat YAML frontmatter: colons on every line, inline bracket lists, no multiline dashes. Concept files declare type, id, title, description, status. Front-load invariants; close on failure guards. Tag rules [P0-P3 | I/E/R] 1-100 uncombined. One purpose per file; link listed files. Exclude chat, code, and logs. Open ref for tier definitions or bundle layout.",
        "opt_c_full": "Flat YAML frontmatter: inline brackets for lists, no multiline dashes. Declare type, id, title, description, status. Front-load invariants; close on failure guards. Tag rules [P0-P3 | I/E/R] 1-100 uncombined. One purpose per file; link listed files. Exclude chat, code, and logs. Open ref for tier/bundle specs.",
        "plane4": ["[file-architecture.md](../../../../file-architecture.md) (`FA-13`, `FA-06`, `FA-02`, `FA-10`)", "[writing-profile.md](../../../../writing-profile.md) (`WP-06`, `WP-07`, `WP-10`, `WP-19`, `WP-24`, `WP-25`)", "[governance-schemas.md](../../../../governance-schemas.md) (`GS-03`, `GS-04`, `GS-14`..`GS-17`)"],
        "research": ["RESULTS-08 (Deepen-when removal)", "RESULTS-09 (Frontmatter parsing & caching)", "C03 (Conditional Informatics Formal Authoring)", "RP-08", "RP-09"],
        "external_lit": ["OASIS DITA Architecture", "Information Mapping Methodology (Horn 1998)"],
        "lore": ["2Dos Ai Instructions.md ('Flat YAML Serialization')", "Snippets.md ('Significance Ranking Architecture')"],
        "failure_modes": [
            "Never use multiline YAML list syntax (`- item`) — causes zero-dependency okf_validator.py to fail immediately.",
            "Never compute a composite mathematical formula from (I/E/R) estimates."
        ]
    },
    {
        "id": "RULE-17-TRADE-OFF",
        "num": "17",
        "tag": "trade_off",
        "full_tag": "<trade_off when=\"the operator must choose between material alternatives, or asks for options\" ref=\"execution-modes.md\">",
        "attrs": "when=\"the operator must choose between material alternatives, or asks for options\" ref=\"execution-modes.md\"",
        "mode": "Gated (Conditional on presenting choices)",
        "p_tier": "P1",
        "ier": "I92/E94/R08",
        "text_3a": "Decide routine reversible choices yourself. For a material choice give each option a mechanism, a concrete grounding, and raw (I/E/R) estimates, then a recommendation and one line per rejection. Open ref for multi-candidate bake-offs.",
        "sbs": [
            {
                "id": "SB-17.1",
                "name": "Autonomous Reversible Decisions",
                "text": "Decide routine reversible choices yourself.",
                "tier": "P0", "ier": "I95/E95/R05",
                "means": "Agents must autonomously decide low-stakes, easily reversible implementation details without stalling the turn to ask the user.",
                "critique": "Anti-paralysis rule (EM-06). Stops agents from asking 'Should I name the variable foo or bar?'",
                "opt_a": "Decide routine reversible choices yourself.",
                "opt_b": "Decide routine reversible choices yourself.",
                "opt_c": "Decide routine reversible choices yourself."
            },
            {
                "id": "SB-17.2",
                "name": "Q&A Decision Matrix Protocol",
                "text": "For a material choice give each option a mechanism, a concrete grounding, and raw (I/E/R) estimates, then a recommendation and one line per rejection.",
                "tier": "P0", "ier": "I96/E96/R05",
                "means": "Material options must provide: mechanism, grounding example, raw (I/E/R) metrics, explicit recommendation, and 1-line rejection notes for losing options.",
                "critique": "Standardizes decision-making (EM-06, GS-12). Rejection notes are critical to prevent recurring debates.",
                "opt_a": "For a material choice give each option a mechanism, a concrete grounding, and raw (I/E/R) estimates, then a recommendation and one line per rejection.",
                "opt_b": "For material trade-offs, give each option a mechanism, concrete grounding, and raw (I/E/R) estimates, plus a recommendation and one line per rejection.",
                "opt_c": "For material trade-offs, provide each option's mechanism, grounding, and raw (I/E/R) metrics, plus recommendation and one-line rejections."
            },
            {
                "id": "SB-17.3",
                "name": "Bake-Off Escalation Pointer",
                "text": "Open ref for multi-candidate bake-offs.",
                "tier": "P1", "ier": "I90/E92/R08",
                "means": "Pointers to Adapter 2 (EM-07 4-Phase Comparison Bake-Off Rubric).",
                "critique": "Essential pointer preserved from RP-08. Directs models to full bake-off matrix when comparing 3+ libraries.",
                "opt_a": "Open ref for multi-candidate bake-offs.",
                "opt_b": "Open ref for multi-candidate bake-offs.",
                "opt_c": "Open ref for multi-candidate bake-offs."
            }
        ],
        "opt_b_full": "Decide routine reversible choices yourself. For material trade-offs, give each option a mechanism, concrete grounding, and raw (I/E/R) estimates, plus a recommendation and one line per rejection. Open ref for multi-candidate bake-offs.",
        "opt_c_full": "Decide routine reversible choices yourself. For material trade-offs, provide each option's mechanism, grounding, and raw (I/E/R) metrics, plus recommendation and one-line rejections. Open ref for multi-candidate bake-offs.",
        "plane4": ["[execution-modes.md](../../../../execution-modes.md) (`EM-06`, `EM-07`)", "[governance-schemas.md](../../../../governance-schemas.md) (`GS-12`, `GS-13`)"],
        "research": ["RESULTS-08 (Preserving bake-off escalation cue)", "C01 (Decision & Trade-Off Discipline)", "RP-08"],
        "external_lit": ["Multi-Attribute Decision Analysis (Keeney & Raiffa)"],
        "lore": ["2Dos Ai Instructions.md ('Q&A Decision Matrix Structure')", "Snippets.md ('Decision Triggers')"],
        "failure_modes": [
            "Never present a list of choices without declaring a definitive recommendation.",
            "Never omit the rejection notes explaining why unselected alternatives were disqualified."
        ]
    },
    {
        "id": "RULE-18-HANDOVER",
        "num": "18",
        "tag": "handover",
        "full_tag": "<handover when=\"ending a session, delegating to a subagent, or writing any handoff\" ref=\"execution-modes.md\">",
        "attrs": "when=\"ending a session, delegating to a subagent, or writing any handoff\" ref=\"execution-modes.md\"",
        "mode": "Gated (Conditional on session end or delegation)",
        "p_tier": "P1",
        "ier": "I94/E96/R05",
        "text_3a": "Never write a handover to defer what you can resolve now. When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce. Open ref for delegation contracts (input ledger, process, output, DoD).",
        "sbs": [
            {
                "id": "SB-18.1",
                "name": "Handover Non-Paralysis Invariant",
                "text": "Never write a handover to defer what you can resolve now.",
                "tier": "P0", "ier": "I98/E96/R04",
                "means": "Hard ban on writing a handoff as an excuse to avoid work that active tools can execute immediately.",
                "critique": "Supreme anti-sloth rule (EM-02, EM-09). Agents love declaring 'Task completed, handoff written: future agent should verify the tests'. Check it now!",
                "opt_a": "Never write a handover to defer what you can resolve now.",
                "opt_b": "Never write a handover to defer resolvable work.",
                "opt_c": "Never write a handover to defer resolvable work."
            },
            {
                "id": "SB-18.2",
                "name": "5-Component Forensic Report",
                "text": "When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce.",
                "tier": "P0", "ier": "I96/E96/R05",
                "means": "Mandatory 5-section report structure: Observation, Logic Chain, Caveats, Conclusion, Verification Method.",
                "critique": "Apex OS standard forensic structure (EM-09 §5.2). Ensures receiving agents have full evidence without requiring back-and-forth chat.",
                "opt_a": "When genuinely needed: what was observed, the reasoning chain, caveats, conclusion, and exact commands to reproduce.",
                "opt_b": "When needed: state observations, reasoning chain, caveats, conclusion, and reproduction commands.",
                "opt_c": "When needed: include observation, reasoning chain, caveats, conclusion, and reproduction commands."
            },
            {
                "id": "SB-18.3",
                "name": "Delegation Contract Escalation Pointer",
                "text": "Open ref for delegation contracts (input ledger, process, output, DoD).",
                "tier": "P1", "ier": "I92/E94/R06",
                "means": "Points to EM-09 §5.1 (4-Dimensional Delegation Contract: Input Priority Ledger, Process, Output Contract, DoD).",
                "critique": "Preserved from RP-08. Crucial when dispatching complex subagents.",
                "opt_a": "Open ref for delegation contracts (input ledger, process, output, DoD).",
                "opt_b": "Open ref for delegation contracts (input ledger, process, output, DoD).",
                "opt_c": "Open ref for delegation contracts (input ledger, process, output, DoD)."
            }
        ],
        "opt_b_full": "Never write a handover to defer resolvable work. When needed: state observations, reasoning chain, caveats, conclusion, and reproduction commands. Open ref for delegation contracts (input ledger, process, output, DoD).",
        "opt_c_full": "Never write a handover to defer resolvable work. When needed: include observation, reasoning chain, caveats, conclusion, and reproduction commands. Open ref for delegation contracts (input ledger, process, output, DoD).",
        "plane4": ["[execution-modes.md](../../../../execution-modes.md) (`EM-09`, `EM-02`)", "[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-06`)"],
        "research": ["RESULTS-08 (Escalation cue recovery)", "A08 (Evidence Integrity)", "A10 (Error Recovery)", "RP-08"],
        "external_lit": ["Teamwork Communication & Handoff Protocols (Antigravity 2026)"],
        "lore": ["2Dos Ai Instructions.md ('5-Component Handoff Report')", "Snippets.md ('Handover Non-Paralysis')"],
        "failure_modes": [
            "Never allow writing a handover when open questions can be answered with live tool execution in the current turn.",
            "Never omit the exact reproduction commands from section 5 (Verification Method)."
        ]
    },
    {
        "id": "RULE-19-ITERATIVE",
        "num": "19",
        "tag": "iterative",
        "full_tag": "<iterative when=\"the task spans multiple modules, needs research, or cannot finish in one pass\" ref=\"execution-modes.md\">",
        "attrs": "when=\"the task spans multiple modules, needs research, or cannot finish in one pass\" ref=\"execution-modes.md\"",
        "mode": "Gated (Conditional on multi-step/multi-module tasks)",
        "p_tier": "P1",
        "ier": "I95/E95/R08",
        "text_3a": "Execute a clear single-step task directly. For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step. For a multi-module project create a file per step. Open ref for the route ladder or MMM decomposition.",
        "sbs": [
            {
                "id": "SB-19.1",
                "name": "Route 0 Direct Execution",
                "text": "Execute a clear single-step task directly.",
                "tier": "P1", "ier": "I90/E92/R08",
                "means": "Simple, unambiguous tasks proceed straight to execution without creating preflight files or architectural scaffolding.",
                "critique": "Anti-overengineering rule (EM-10). Avoids spending 300 tokens planning a 1-line bug fix.",
                "opt_a": "Execute a clear single-step task directly.",
                "opt_b": "Execute single-step tasks directly.",
                "opt_c": "Execute single-step tasks directly."
            },
            {
                "id": "SB-19.2",
                "name": "Route 1 Compact Preflight",
                "text": "For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step.",
                "tier": "P0", "ier": "I95/E95/R05",
                "means": "Moderate multi-step tasks require writing a 5-item preflight block (Target, Inputs, Scope, Output, Active Step) before executing.",
                "critique": "High leverage against drift (EM-10). Anchors the active step in context.",
                "opt_a": "For multi-step work write a short preflight — target, inputs, scope, output, active step — then proceed step by step.",
                "opt_b": "For multi-step work, write a compact preflight (target, inputs, scope, output, active step) and proceed step by step,",
                "opt_c": "For multi-step work, draft a short preflight (target, inputs, scope, output, active step) and proceed step by step,"
            },
            {
                "id": "SB-19.3",
                "name": "Route 2 / MMM File-Producing Loop",
                "text": "For a multi-module project create a file per step.",
                "tier": "P0", "ier": "I96/E96/R05",
                "means": "Complex projects must materialize a dedicated artifact per step (step-XX.md, analysis.md), preventing in-memory drift.",
                "critique": "File-producing loop is the core of MMM (EM-10 §6.2). Disk files survive context compression.",
                "opt_a": "For a multi-module project create a file per step.",
                "opt_b": "creating a file per step for multi-module projects.",
                "opt_c": "creating a file per step for multi-module projects."
            },
            {
                "id": "SB-19.4",
                "name": "MMM Route Ladder Escalation Pointer",
                "text": "Open ref for the route ladder or MMM decomposition.",
                "tier": "P1", "ier": "I90/E92/R08",
                "means": "Pointers to Macro-Meso-Micro decomposition and Route 0/1/2 ladder (EM-10 §6.3).",
                "critique": "Preserved from RP-08. Directs models to full MMM decomposition.",
                "opt_a": "Open ref for the route ladder or MMM decomposition.",
                "opt_b": "Open ref for route ladder or MMM decomposition.",
                "opt_c": "Open ref for route ladder or MMM decomposition."
            }
        ],
        "opt_b_full": "Execute single-step tasks directly. For multi-step work, write a compact preflight (target, inputs, scope, output, active step) and proceed step by step, creating a file per step for multi-module projects. Open ref for route ladder or MMM decomposition.",
        "opt_c_full": "Execute single-step tasks directly. For multi-step work, draft a short preflight (target, inputs, scope, output, active step) and proceed step by step, creating a file per step for multi-module projects. Open ref for route ladder or MMM decomposition.",
        "plane4": ["[execution-modes.md](../../../../execution-modes.md) (`EM-10`, `EM-11`)", "[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-04`)"],
        "research": ["RESULTS-08 (Escalation cue recovery)", "RESULTS-09 (Default behavior audit)", "A04 (Complexity Adaptive Workflow)", "RP-08", "RP-09"],
        "external_lit": ["Macro-Meso-Micro Systems Decomposition", "Route Ladder Complexity Routing"],
        "lore": ["2Dos Ai Instructions.md ('MMM Execution Loop')", "Snippets.md ('Route Ladder')"],
        "failure_modes": [
            "Never allow complex multi-module tasks to run purely in conversation memory without writing step files to disk.",
            "Never violate the Upward Invalidation Rule (EM-11): do not alter Macro architecture solely because low-level Micro implementation details shifted."
        ]
    },
    {
        "id": "RULE-20-SCHEMAS",
        "num": "20",
        "tag": "schemas",
        "full_tag": "<schemas when=\"emitting a patch intent, or validating bundle or schema conformance\" ref=\"governance-schemas.md\">",
        "attrs": "when=\"emitting a patch intent, or validating bundle or schema conformance\" ref=\"governance-schemas.md\"",
        "mode": "Gated (Conditional on schema validation)",
        "p_tier": "P0",
        "ier": "I98/E98/R04",
        "text_3a": "Satisfy the declared schema exactly. Never invent fields. Target edits by heading path and surrounding text, never line number. Open ref for exact JSON or YAML schemas.",
        "sbs": [
            {
                "id": "SB-20.1",
                "name": "Mandatory Schema Conformance",
                "text": "Satisfy the declared schema exactly.",
                "tier": "P0", "ier": "I98/E98/R04",
                "means": "Payloads must strictly match the authoritative schema specification (GS-01).",
                "critique": "Non-negotiable data integrity invariant.",
                "opt_a": "Satisfy the declared schema exactly.",
                "opt_b": "Conform to declared schemas exactly;",
                "opt_c": "Satisfy declared schemas exactly"
            },
            {
                "id": "SB-20.2",
                "name": "Closed Object Invariant",
                "text": "Never invent fields.",
                "tier": "P0", "ier": "I98/E98/R04",
                "means": "Forbids adding unregistered, hallucinated keys to JSON or YAML objects (`additionalProperties: false`).",
                "critique": "Directly stops schema pollution (GS-01, GS-10).",
                "opt_a": "Never invent fields.",
                "opt_b": "never invent fields.",
                "opt_c": "with zero invented fields."
            },
            {
                "id": "SB-20.3",
                "name": "Prohibited Line-Number Target Locators",
                "text": "Target edits by heading path and surrounding text, never line number.",
                "tier": "P0", "ier": "I98/E96/R04",
                "means": "File mutations must be anchored by structural AST heading paths and text hints, strictly banning volatile line numbers.",
                "critique": "High-impact reliability invariant (GS-09, GS-11). Line numbers drift immediately upon the first patch in a file.",
                "opt_a": "Target edits by heading path and surrounding text, never line number.",
                "opt_b": "Locate patch targets by heading path and surrounding context, never line numbers.",
                "opt_c": "Target edits via heading path and context, never line numbers."
            },
            {
                "id": "SB-20.4",
                "name": "Schema Escalation Pointer",
                "text": "Open ref for exact JSON or YAML schemas.",
                "tier": "P1", "ier": "I90/E92/R08",
                "means": "Pointers to governance-schemas.md when exact schema definitions are needed.",
                "critique": "Preserved from RP-08. Restricts opening governance-schemas.md to times when machine schemas are actively evaluated.",
                "opt_a": "Open ref for exact JSON or YAML schemas.",
                "opt_b": "Open ref for exact JSON or YAML schemas.",
                "opt_c": "Open ref for exact JSON or YAML schemas."
            }
        ],
        "opt_b_full": "Conform to declared schemas exactly; never invent fields. Locate patch targets by heading path and surrounding context, never line numbers. Open ref for exact JSON or YAML schemas.",
        "opt_c_full": "Satisfy declared schemas exactly with zero invented fields. Target edits via heading path and context, never line numbers. Open ref for exact JSON or YAML schemas.",
        "plane4": ["[governance-schemas.md](../../../../governance-schemas.md) (`GS-01`, `GS-09`, `GS-10`, `GS-11`)"],
        "research": ["RESULTS-08 (Escalation cue recovery)", "RESULTS-09 (Schema efficiency)", "RP-08", "RP-09"],
        "external_lit": ["JSON Schema Draft 2020-12", "AST-based Markdown Patching"],
        "lore": ["2Dos Ai Instructions.md ('Prohibit line numbers in patch intents')", "Snippets.md ('Mandatory Schema Conformance')"],
        "failure_modes": [
            "Never allow line numbers (`line_number`, `line_start`) in patch intents — always locate edits by heading path and context.",
            "Never emit JSON/YAML payloads with undeclared, hallucinated properties."
        ]
    },
    {
        "id": "RULE-21-SYNC",
        "num": "21",
        "tag": "sync",
        "full_tag": "<sync when=\"the operator asks to sync, commit or push\">",
        "attrs": "when=\"the operator asks to sync, commit or push\"",
        "mode": "Gated (Conditional on git push/sync)",
        "p_tier": "P0",
        "ier": "I96/E96/R05",
        "text_3a": "Run the git commands first, not repository analysis. Preserve every file: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry.",
        "sbs": [
            {
                "id": "SB-21.1",
                "name": "Git Command Primacy",
                "text": "Run the git commands first, not repository analysis.",
                "tier": "P0", "ier": "I96/E96/R05",
                "means": "When asked to push or sync, execute git add, git commit, git push immediately without running repository analysis.",
                "critique": "High-value operational lore from 2Dos.md / Snippets.md (EM-12). Cuts out 3 wasted turns of unprompted git diff inspection.",
                "opt_a": "Run the git commands first, not repository analysis.",
                "opt_b": "Execute git commands immediately, not repo analysis.",
                "opt_c": "Run git commands immediately without repo analysis."
            },
            {
                "id": "SB-21.2",
                "name": "Asset Preservation Invariant",
                "text": "Preserve every file: commit unrelated dirty files separately rather than dropping them.",
                "tier": "P0", "ier": "I98/E96/R04",
                "means": "Strict ban on discarding, reverting, or stashing dirty files outside the active task scope; commit them separately if needed.",
                "critique": "Prevents catastrophic data loss (EM-12, AD-23). Agents love running `git checkout -- .` to 'clean up' working trees.",
                "opt_a": "Preserve every file: commit unrelated dirty files separately rather than dropping them.",
                "opt_b": "Preserve all files: commit unrelated dirty files separately rather than dropping them.",
                "opt_c": "Preserve all files: commit unrelated dirty files separately instead of dropping them."
            },
            {
                "id": "SB-21.3",
                "name": "Rebase Retry Protocol",
                "text": "On non-fast-forward, pull with rebase and retry.",
                "tier": "P1", "ier": "I92/E94/R06",
                "means": "Standard rebase-and-retry recovery on rejected git pushes.",
                "critique": "Automates routine git conflict handling.",
                "opt_a": "On non-fast-forward, pull with rebase and retry.",
                "opt_b": "On non-fast-forward, pull with rebase and retry.",
                "opt_c": "On non-fast-forward, pull --rebase and retry."
            }
        ],
        "opt_b_full": "Execute git commands immediately, not repo analysis. Preserve all files: commit unrelated dirty files separately rather than dropping them. On non-fast-forward, pull with rebase and retry.",
        "opt_c_full": "Run git commands immediately without repo analysis. Preserve all files: commit unrelated dirty files separately instead of dropping them. On non-fast-forward, pull --rebase and retry.",
        "plane4": ["[execution-modes.md](../../../../execution-modes.md) (`EM-12`)", "[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-23`)"],
        "research": ["RESULTS-10 (Surface layering & CLI dispatch deduplication)", "RP-10"],
        "external_lit": ["Git Pro (Chacon & Straub) Rebase Discipline"],
        "lore": ["2Dos.md ('Git Dispatch Primacy')", "Snippets.md ('Asset Preservation & Deterministic Moves')"],
        "failure_modes": [
            "Never run `git checkout -- .`, `git clean -fd`, or `git stash drop` on uncommitted files without explicit user instruction.",
            "Never enter multi-turn repository audits when the prompt is simply 'git push'."
        ]
    },
    {
        "id": "RULE-22-POINTERS",
        "num": "22",
        "tag": "pointers",
        "full_tag": "<pointers>",
        "attrs": "",
        "mode": "Terminal Guard (Unconditional)",
        "p_tier": "P0",
        "ier": "I96/E96/R05",
        "text_3a": "Paths are just-in-time pointers relative to base_ref. Open one only when its condition matches and the inline summary is insufficient.",
        "sbs": [
            {
                "id": "SB-22.1",
                "name": "Base Ref Path Factoring",
                "text": "Paths are just-in-time pointers relative to base_ref.",
                "tier": "P1", "ier": "I92/E90/R08",
                "means": "Declares that all `ref=\"...\"` paths resolve relative to `base_ref=\"apex-meta/informatics/\"` on the root tag.",
                "critique": "Factors out repository path prefixes once on root tag (RP-09, RP-10), saving 25 tokens across the contract and providing 100% Layer 1 portability.",
                "opt_a": "Paths are just-in-time pointers relative to base_ref.",
                "opt_b": "Paths are just-in-time pointers relative to base_ref.",
                "opt_c": "Paths are JIT pointers relative to base_ref."
            },
            {
                "id": "SB-22.2",
                "name": "Two-Threshold Escalation Invariant",
                "text": "Open one only when its condition matches and the inline summary is insufficient.",
                "tier": "P0", "ier": "I96/E96/R05",
                "means": "Opening a Plane 4 reference requires satisfying BOTH thresholds: (1) active task matches the `when` condition, AND (2) the contract's inline summary is inadequate for execution.",
                "critique": "Terminal Guard placed at the very end of the contract block (WP-25, AD-26). Folded from RP-08. Eliminates unnecessary reads of Plane 4 documentation.",
                "opt_a": "Open one only when its condition matches and the inline summary is insufficient.",
                "opt_b": "Open a reference only when its condition matches and the inline summary is insufficient.",
                "opt_c": "Open a reference only when its condition triggers and the inline summary is insufficient."
            }
        ],
        "opt_b_full": "Paths are just-in-time pointers relative to base_ref. Open a reference only when its condition matches and the inline summary is insufficient.",
        "opt_c_full": "Paths are JIT pointers relative to base_ref. Open a reference only when its condition triggers and the inline summary is insufficient.",
        "plane4": ["[general-informatics-router.md](../../../../general-informatics-router.md)", "[writing-profile.md](../../../../writing-profile.md) (`WP-25`, `WP-18`)", "[anti-drift-rules.md](../../../../anti-drift-rules.md) (`AD-26`)"],
        "research": ["RESULTS-08 (Deepen-when mechanics & terminal folding)", "RESULTS-09 (Base ref factoring)", "RESULTS-10 (Surface layering)", "RP-08", "RP-09", "RP-10"],
        "external_lit": ["OASIS DITA `conref` Architecture", "SpecBench (2026)"],
        "lore": ["2Dos Ai Instructions.md ('Two-threshold JIT routing')", "Snippets.md ('Terminal Guard')"],
        "failure_modes": [
            "Must always remain the terminal tag of `<apex_contract>` (WP-25 Terminal-Position Operative Content).",
            "Must explicitly require both thresholds (condition matches AND inline summary is insufficient) to prevent eager reading."
        ]
    }
]

print(f"Loaded {len(rules_data)} rules for generation.")
