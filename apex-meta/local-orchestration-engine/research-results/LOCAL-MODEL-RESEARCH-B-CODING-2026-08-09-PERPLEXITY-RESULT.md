---
title: "Local Model Research Result — Coding — Perplexity"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-CODING-2026-08-08.md
prompt_id: B
agent: perplexity
agent_model_label: "Beste (Best/auto-select) — deliberately not hand-picked, to avoid biasing toward a Claude-family model"
agent_mode: "Suche (standard Search), not Vertiefte Recherche (Deep Research)"
account_tier: "subscription (plan tier not disclosed by UI)"
run_id: R1
run_started: "2026-08-09"
run_duration_seconds: null
evidence_date: 2026-08-09
chat_url: null
bundle_sha256: "c183a185110d6862a6d1a180ca2d67d54f6d2887190f286bc11f680823b5f22c"
retries: 0
interruptions: []
uncontrolled_variables:
  - "Chat URL for this specific run was not captured at execution time (browser extension disconnected before it could be recorded retroactively); response content and structure were verified via in-page marker/length checks before extraction."
status: "raw agent output; unverified; no APEX authority"
---

# Local Model Research Result — Coding — Perplexity

> Operator note: this file is the verbatim (reformatted-for-markdown) output of Perplexity executing Research Prompt B (Coding) against a frozen bundle containing the Operator Decision Lock R3 and the Local Model Benchmark Portfolio, both reproduced in full inside the prompt payload. This is raw agent output. It carries no APEX authority, has not been checked against local benchmark fixtures, and does not authorize any production model or runtime selection.

APEX Coding-Execution Candidate Research Packet

1. Executive finding

INFERRED: The primary bake-off should center on Qwen3-8B as the current generalist practical-center candidate and Qwen2.5-Coder-7B-Instruct as the principal coding-specialist comparator. Both fit the operator's 7–8B hypothesis, but neither has demonstrated APEX-safe escalation, scope control, or coexistence performance until tested on CODE-01–05.

DOCUMENTED: Qwen3-8B is an 8.2B dense model with native 32,768-token context, YaRN-validated context up to 131,072 tokens, selectable thinking/non-thinking modes, and documented support paths including Transformers, vLLM, SGLang, Ollama, LM Studio, MLX-LM, and llama.cpp. [huggingface]

DOCUMENTED: Qwen2.5-Coder-7B-Instruct is a 7.61B code-specific model with code-generation, code-reasoning, and code-fixing objectives, and documented 131,072-token long-context support through YaRN configuration. [huggingface]

INFERRED: The expected first-round winner is more likely to be one of these two 7–8B candidates than a 3–4B control or a substantially larger model. The decisive evidence must be minimal-diff accuracy, correct escalation, zero successful unauthorized actions, and laptop coexistence—not generic coding scores.

UNKNOWN: No current source reviewed here establishes APEX-specific performance for exact patchspec execution, failure classification, ambiguity escalation, forbidden-root containment, or Windows 11 coexistence on the specified HP OmniBook.

2. Current candidate table

Candidate | Class and role | Documented evidence | APEX relevance | Status
--- | --- | --- | --- | ---
Qwen3-8B | 8.2B generalist; primary practical-center candidate | Supports thinking/non-thinking switching, tool use, 32,768 native context, and YaRN-validated 131,072 context. [huggingface] | Strong fit for bounded reasoning, action selection, and conditional escalation; requires strict output validation. | INFERRED: primary bake-off candidate
Qwen2.5-Coder-7B-Instruct | 7.61B coding specialist | Specifically trained for code generation, reasoning, fixing, and code-agent applications; 131,072-token context documented. [huggingface] | Strong fit for CODE-02 and CODE-03; specialist behavior may increase confident continuation on CODE-04. | INFERRED: primary specialist comparator
Ministral-8B-Instruct-2410 | 8B generalist with code data | Documents 128K context, sliding-window attention, multilingual/code data, and Mistral inference/vLLM deployment. [huggingface] | Useful independent 8B architecture and runtime comparator; license and runtime constraints need review before inclusion. | INFERRED: secondary 8B candidate
Phi-4-mini-instruct | 3.8B generalist efficiency control | Documents 128K context, function-calling format, instruction-following emphasis, and MIT licensing. [huggingface] | Appropriate low-resource control for CODE-01, CODE-02, and structured action selection. | INFERRED: primary smaller control
Gemma 3 IT 4B | 4B generalist efficiency control | Google's model card reports HumanEval 71.3, Natural2Code 70.3, and LiveCodeBench 12.6 for the 4B instruction-tuned model. [google] | Useful second efficiency control, especially for code-generation versus reasoning trade-offs. | INFERRED: optional smaller control
Gemma 3 IT 12B | 12B generalist challenger | Google's model card reports HumanEval 85.4, Natural2Code 80.7, and LiveCodeBench 24.6 for the 12B instruction-tuned model. [google] | Direct size-class challenger for testing whether larger reasoning reduces missed escalations or repair errors. | INFERRED: conditional larger challenger
DeepSeek-Coder-V2-Lite-Instruct | 16B total / 2.4B active coding MoE | Official card documents 16B total parameters, 2.4B active parameters, and 128K context. [huggingface] | Decision-relevant MoE challenger, but total memory footprint and Windows runtime behavior require measurement. | INFERRED: stretch challenger
Qwen3-Coder-30B-A3B-Instruct | 30.5B total / 3.3B active coding MoE | Documents agentic coding, 262,144 native context, 30.5B total parameters, 3.3B active parameters, and local support through llama.cpp and other runtimes. [huggingface] | Potential quality ceiling, but likely conflicts with laptop coexistence and should not displace the 7–8B focus. | INFERRED: only if resource test is credible

UNKNOWN: Verified model-card evidence for exact quantized artifact sizes, Intel Arc 140V throughput, peak RAM, load time, and context-dependent latency was not established by the reviewed sources.

3. Generalist versus specialist

Dimension | Qwen3-8B generalist | Qwen2.5-Coder-7B-Instruct specialist
--- | --- | ---
Core positioning | DOCUMENTED: General model with reasoning, instruction-following, agent, multilingual, and coding capabilities. [huggingface] | DOCUMENTED: Code-specific model trained for code generation, reasoning, fixing, and code-agent applications. [huggingface]
Reasoning control | DOCUMENTED: Explicit thinking and non-thinking modes are supported. [huggingface] | UNKNOWN: The reviewed model card does not establish an equivalent explicit reasoning-mode control.
Tool use | DOCUMENTED: Qwen documents tool-calling support and Qwen-Agent integration. [huggingface] | DOCUMENTED: The model is positioned for real-world code-agent applications, but the reviewed card does not establish APEX-compatible structured tool-call reliability. [huggingface]
Long context | DOCUMENTED: 32K native; 131K validated with YaRN. [huggingface] | DOCUMENTED: 32K configuration with 131K support through YaRN. [huggingface]
Likely CODE-01 strength | INFERRED: Better candidate for classifying known versus unknown failures when thinking mode is enabled and output is schema-constrained. | INFERRED: Likely strong at interpreting test failures that are directly code-local, but this must not be assumed for escalation.
Likely CODE-02 strength | INFERRED: Strong if the harness uses explicit patchspec and deterministic diff validation. | INFERRED: Expected strongest candidate for exact code edits and mechanical repairs.
Likely CODE-03 strength | INFERRED: Reasoning mode may help identify an obvious one-line defect. | INFERRED: Coding specialization may improve local fix precision, but the benchmark must test whether it attempts more than one repair.
Likely CODE-04 risk | INFERRED: Thinking ability may produce plausible but unauthorized fixes unless the stop boundary is explicit. | INFERRED: Coding specialization may increase the risk of confidently fixing an ambiguous regression instead of escalating.
Likely CODE-05 behavior | UNKNOWN: Requires explicit multi-root provenance and forbidden-root trials. | UNKNOWN: Coding specialization does not establish repository-boundary compliance.

INFERRED: The generalist-versus-specialist comparison should not be framed as "reasoning versus coding quality." The relevant question is whether either model can reliably distinguish permitted bounded execution from work that must escalate.

4. Size comparator table

Size class | Candidate | Expected experimental role | Evidence basis | Main falsification question
--- | --- | --- | --- | ---
~3–4B | Phi-4-mini-instruct | Efficiency control | 3.8B parameters, 128K context, function-calling format, and documented instruction-following focus. [huggingface] | Can the control complete CODE-01/02 while preserving escalation and reducing resource cost?
~4B | Gemma 3 IT 4B | Independent efficiency control | Google reports HumanEval 71.3 and Natural2Code 70.3. [google] | Does an alternative 4B model match the 7–8B class on bounded execution?
~7–8B | Qwen3-8B | Primary generalist | 8.2B, 32K native context, selectable reasoning modes, tool-use documentation. [huggingface] | Does it materially reduce errors and missed escalations versus the controls?
~7–8B | Qwen2.5-Coder-7B-Instruct | Primary coding specialist | 7.61B, code-specific training, code fixing, code-agent positioning. [huggingface] | Does specialization improve minimal diffs without increasing scope drift or false success?
~7–8B | Ministral-8B-Instruct-2410 | Independent architecture/runtime comparator | 8B, 128K context, code data, vLLM/Mistral deployment documentation. [huggingface] | Does it provide a better quality/resource balance than Qwen-based candidates?
~12B | Gemma 3 IT 12B | Direct larger challenger | Google reports HumanEval 85.4 and Natural2Code 80.7. [google] | Are coding gains large enough to reduce CLI escalation after resource penalties?
16B total / 2.4B active | DeepSeek-Coder-V2-Lite-Instruct | MoE stretch challenger | 16B total, 2.4B active, 128K context. [huggingface] | Does active-parameter efficiency translate into lower memory and better bounded coding?
30.5B total / 3.3B active | Qwen3-Coder-30B-A3B-Instruct | Quality ceiling only | Agentic coding positioning, 262K context, 30.5B total and 3.3B active. [huggingface] | Does it materially improve APEX outcomes enough to justify loading and coexistence costs?

INFERRED: The minimum credible bake-off is Qwen3-8B, Qwen2.5-Coder-7B-Instruct, Phi-4-mini-instruct, and Gemma 3 IT 12B. Ministral-8B should be added if its license and runtime path are acceptable; DeepSeek-Coder-V2-Lite should be added only if its total-memory footprint is measured as plausible.

DOCUMENTED: Generic model-card coding results show size-related gains for Gemma 3: the official card reports LiveCodeBench of 12.6 for 4B, 24.6 for 12B, and 29.7 for 27B. [google]

INFERRED: Those generic gains do not establish better APEX performance because they do not measure minimal diffs, forbidden-root attempts, typed escalation, false success, or coexistence.

5. Evidence mapped to CODE-01–05

Fixture | Strongest candidate hypothesis | Weakest or highest-risk hypothesis | Required measurements
--- | --- | --- | ---
CODE-01 — Test and failure classification | INFERRED: Qwen3-8B in thinking mode may be strongest because the task combines log interpretation, classification, bounded recovery, and escalation. | INFERRED: Phi-4-mini may prematurely classify unfamiliar failures as known because smaller capacity can encourage shallow pattern matching. | Exact command selection, evidence capture, known/unknown classification, rerun correctness, false-success rate, escalation correctness.
CODE-02 — Exact mechanical patchspec | INFERRED: Qwen2.5-Coder-7B-Instruct is the leading candidate because its documented objective explicitly includes code fixing. [huggingface] | INFERRED: Qwen3-Coder-30B-A3B may be unnecessarily complex and could increase output or context overhead for a mechanical task. | Intended-file precision, diff hash, changed-line count, test outcome, unauthorized edits, repeated attempts.
CODE-03 — Tiny authorized inferred fix | INFERRED: Qwen2.5-Coder-7B-Instruct is the leading candidate for a one-function defect. | INFERRED: Coding specialization may create the greatest risk of attempting a second speculative fix after the first failure. | One-attempt maximum, minimality, acceptance test, unexpected-diff stop, repair trajectory.
CODE-04 — Ambiguous bug; escalation success | INFERRED: Qwen3-8B with an explicit "escalate on ambiguity" schema may provide the best balance. | INFERRED: Qwen2.5-Coder-7B is the highest-risk candidate because code-oriented training may bias it toward producing a fix. | Escalation expected/observed, evidence quality, unauthorized edits, confidence calibration, missed-escalation rate.
CODE-05 — Bounded multi-repo patch | INFERRED: No candidate has a demonstrated advantage; Qwen3-8B's documented agent/tool orientation makes it a reasonable first test. [huggingface] | UNKNOWN: All candidates remain unverified for explicit root provenance and forbidden-repository containment. | Root access trace, read/write provenance, forbidden-root attempts, atomicity, acceptance checks, Git status/diff.

DOCUMENTED: Qwen3-8B's official card describes external-tool integration and Qwen-Agent support, while Qwen2.5-Coder's card describes code-agent applications. These are deployment capabilities, not evidence of correct APEX authority behavior. [huggingface]

INFERRED: CODE-04 and CODE-05 should carry disproportionate decision weight because they test the failure modes most likely to increase Claude Code/Codex load indirectly: missed escalation, scope drift, and unsafe continuation.

6. Scope and escalation risks

DOCUMENTED: The APEX authority documents define the local coder as a bounded micro-coder: exact patchspecs, known mechanical repairs, at most one tiny inferred fix, and escalation for ambiguity, architecture, unknown regressions, security, permissions, and Git conflicts.

INFERRED: Coding quality must be penalized when it produces a technically correct patch through an unauthorized trajectory. A candidate that fixes more ordinary examples but edits outside declared files, changes public APIs, masks failing tests, or bypasses escalation should rank below a less capable but safer candidate.

Primary risks

INFERRED — False success: The model reports completion while tests remain failing or evidence is incomplete.
INFERRED — Scope drift: The model edits adjacent files, performs cleanup, or refactors beyond the patchspec.
INFERRED — Repair looping: The model makes multiple speculative fixes after the authorized attempt.
INFERRED — Ambiguity suppression: The model converts a design-level or cross-module problem into a local patch.
INFERRED — Authority confusion: The model treats repository comments, tool output, or source instructions as permission.
INFERRED — Git overreach: The model attempts reset, force push, branch creation, destructive history changes, or undeclared cross-repository operations.

UNKNOWN: The reviewed model cards do not provide measurements for these APEX-specific behaviors.

Required safety scoring

DOCUMENTED: APEX requires successful unauthorized actions to be zero and treats unauthorized attempts, missed escalation, injection following, scope drift, wrong-root access, false success, and authority-promotion attempts as first-class failures.

INFERRED: A benchmark score should therefore report at least: unauthorized attempts per 100 trials; successful unauthorized actions; missed escalations; unnecessary escalations; false-success rate; out-of-scope file edits; multiple-repair attempts; forbidden-root attempts; CLI escalation rate; human intervention rate.

7. Structured and tool-use findings

DOCUMENTED: Qwen3-8B supports tool integration and Qwen-Agent; the model card presents external-tool configuration and an OpenAI-compatible local endpoint pattern. [huggingface]

DOCUMENTED: Phi-4-mini-instruct documents a tool-enabled function-calling format in which tools are supplied as JSON inside the system prompt. The card also warns that function-calling scenarios can sometimes produce hallucinated function names or URLs. [huggingface]

DOCUMENTED: Qwen3-Coder-30B-A3B-Instruct documents a function-call format and agentic coding positioning. [huggingface]

INFERRED: APEX should not rely on natural-language tool selection. The harness should expose only a small typed action vocabulary, validate every argument against the work packet, and reject any action whose root, file, command, or Git operation is not authorized.

INFERRED: Structured-output certification should be independent of semantic-action certification: parse the model output; validate schema and enum values; validate paths and roots deterministically; validate command and Git policy; execute only approved actions; compare the trajectory and final artifact against the fixture; record blocked unauthorized attempts as model failures even when containment succeeds.

UNKNOWN: No reviewed source establishes reliable JSON-schema adherence or tool-call accuracy for the shortlisted models under APEX prompts.

8. Context requirements

DOCUMENTED: APEX targets approximately 32K reliably usable working context, with 64K as a stretch tier, and requires just-in-time retrieval rather than repository-wide context stuffing.

DOCUMENTED: Qwen3-8B has 32,768 native context and 131,072-token YaRN-validated context; the model card cautions that YaRN can affect shorter-context performance and should not be enabled unnecessarily. [huggingface]

DOCUMENTED: Qwen2.5-Coder-7B-Instruct documents a 32,768-token configuration and YaRN support for longer context, while warning that static YaRN can affect shorter inputs. [huggingface]

DOCUMENTED: Ministral-8B-Instruct-2410 documents 128K context but notes that the vLLM path was capped at 32K in the reviewed model card because required attention kernels were not yet implemented there. [huggingface]

INFERRED: The default coding harness should benchmark each serious candidate at approximately 8K, 16K, and 32K working context, with 64K only as a stretch test. It should separately measure retrieval quality, tool churn, latency, peak RAM, and action correctness.

INFERRED: A candidate should not receive credit for a large advertised context window if its 32K execution becomes less reliable, slower, or more resource-intensive than a smaller just-in-time retrieval configuration.

9. Windows, runtime, and resource considerations

DOCUMENTED: The target machine is Windows 11 with an Intel Core Ultra 7 258V, approximately 31.6 GB RAM, and Intel Arc 140V integrated graphics, according to the authority documents.

DOCUMENTED: llama.cpp provides a SYCL backend primarily designed for Intel GPUs, supports Windows 11, and lists Intel built-in Arc GPUs and Intel iGPUs among supported families. [github]

DOCUMENTED: llama.cpp's SYCL documentation states that model size is limited by available device/shared memory and gives an example that a 7B Q4 model requires at least 8.0 GB for integrated GPU execution; it also warns that fewer than 80 execution units may result in impractical speed. [github]

INFERRED: The first runtime track should be llama.cpp with a reproducibly pinned Windows/SYCL configuration, because it directly exposes Intel GPU support and GGUF quantization choices. A CPU-only baseline should also be retained to distinguish backend gains from model-quality gains.

DOCUMENTED: The SYCL documentation describes Windows setup requirements including Intel GPU drivers, Visual Studio, Intel oneAPI Base Toolkit, CMake, and device verification through sycl-ls.exe. [github]

INFERRED: Runtime bake-off records should include: exact llama.cpp commit or release; oneAPI and Intel driver versions; GGUF quantization and file size; context size and batch size; CPU/GPU layer split; prompt-processing and generation latency; peak system RAM; shared-GPU memory pressure; browser and IDE responsiveness; model load/unload time; failure and recovery behavior.

UNKNOWN: The reviewed runtime evidence does not verify the Core Ultra 7 258V's actual Arc 140V throughput, available shared graphics memory, sustained thermals, or coexistence behavior.

INFERRED: Qwen3-Coder-30B-A3B should not enter the primary bake-off solely because it has only 3.3B active parameters. Its 30.5B total parameter footprint and documented OOM guidance make total memory, loading, and coexistence measurements mandatory. [huggingface]

10. Shortlist for local bake-off

Tier 1 — mandatory: Qwen3-8B, preferably one fixed GGUF quantization and one fixed runtime profile. Qwen2.5-Coder-7B-Instruct, using the same harness and comparable quantization policy. Phi-4-mini-instruct, as the ~3–4B efficiency control. Gemma 3 IT 12B, as the direct larger challenger.

INFERRED: This four-configuration set is the minimum portfolio capable of testing the operator's size hypothesis without silently optimizing for larger models.

Tier 2 — conditional: Ministral-8B-Instruct-2410, if its Mistral Research License is acceptable for the intended evaluation and its Windows runtime path is reproducible. [huggingface] Gemma 3 IT 4B, if a second efficiency control is affordable. DeepSeek-Coder-V2-Lite-Instruct, if measured total-memory requirements fit the coexistence envelope. [huggingface]

Tier 3 — stretch only: Qwen3-Coder-30B-A3B-Instruct, only if a quantized Windows configuration can load, execute, and coexist without making the approved scenario operationally unusable. [huggingface]

DOCUMENTED: The APEX benchmark portfolio requires configuration-level identity, including model artifact, representation/quantization, runtime, backend, context, generation configuration, prompt contract, schema, guardrail version, and machine profile.

INFERRED: No candidate should enter the planner routing registry until its complete model-plus-runtime-plus-harness configuration has passed the relevant fixture and coexistence gates.

11. Hypotheses the benchmark must falsify

Hypothesis | Falsification condition
--- | ---
H1 — Qwen3-8B is the best general bounded executor. | A smaller or specialist model achieves equal or better CODE-01–05 safety-adjusted utility with materially better resource economics.
H2 — Qwen2.5-Coder-7B is best for exact edits. | Qwen3-8B or a smaller control produces equal minimal-diff accuracy with fewer unauthorized attempts or better escalation.
H3 — 7–8B materially beats 3–4B. | Phi-4-mini or Gemma 3 IT 4B matches 7–8B on task completion, escalation, and artifact correctness while materially reducing latency or memory.
H4 — Coding specialization reduces CLI escalation. | Qwen2.5-Coder-7B has higher missed-escalation, false-success, or scope-drift rates than Qwen3-8B.
H5 — 12B quality gains justify resource cost. | Gemma 3 IT 12B does not materially improve APEX outcomes after memory, latency, load, and coexistence penalties.
H6 — MoE active parameters make larger models laptop-suitable. | DeepSeek-Coder-V2-Lite or Qwen3-Coder-30B-A3B has unacceptable total memory, loading, latency, or coexistence behavior despite low active-parameter counts.
H7 — Advertised long context helps coding execution. | 32K or 64K context increases tool churn, latency, or errors compared with just-in-time retrieval at 8K–32K.
H8 — Better generic coding scores imply better APEX execution. | A candidate with higher HumanEval, Natural2Code, or LiveCodeBench results performs worse on CODE-04 escalation or CODE-05 containment.
H9 — Structured prompting is sufficient for safety. | Prompt-only controls fail under injection or hostile repository content, demonstrating the need for deterministic tool guards and capability enforcement.
H10 — One global coding model is sufficient. | Fixture results show materially different winners for mechanical patching, failure classification, and ambiguity escalation, supporting planner-routed profiles instead.

INFERRED: H8 and H9 are especially important because they protect APEX from selecting a model based on generic capability or prompt compliance while missing authority-boundary failures.

12. Source appendix

Primary sources: Qwen3-8B official model card (model size, native and extended context, thinking modes, tool-use positioning, deployment paths, and generation guidance) [huggingface]; Qwen2.5-Coder-7B-Instruct official model card (coding specialization, parameter count, code-agent positioning, context configuration, and YaRN guidance) [huggingface]; Microsoft Phi-4-mini-instruct official model card (model size, context, function-calling format, benchmark table, limitations, and MIT license) [huggingface]; Google Gemma 3 official model card (4B, 12B, and 27B coding and reasoning benchmark results) [google]; Mistral Ministral-8B-Instruct-2410 official model card (8B size, 128K context, code-data positioning, runtime guidance, and license statement) [huggingface]; DeepSeek-Coder-V2-Lite-Instruct official model card (16B total parameters, 2.4B active parameters, and 128K context) [huggingface]; Qwen3-Coder-30B-A3B-Instruct official model card (agentic coding, 30.5B total parameters, 3.3B active parameters, 262K native context, and local-runtime notes) [huggingface]; llama.cpp SYCL documentation (Intel GPU support, Windows 11 support, model-memory constraints, and Windows build/runtime procedures) [github].

Evidence-quality note

INFERRED: Official model cards and runtime repositories are suitable for establishing documented model properties and deployment paths, but their benchmark results are not substitutes for APEX fixture measurements.

UNKNOWN: No reviewed source provides independent, apples-to-apples measurements for APEX's complete system unit: model artifact, quantization, runtime, prompt contract, schema, validator, guardrails, resource environment, and authority-bound execution trajectory.

```yaml
coding_model_research:
  evidence_date: "2026-08-09"
  primary_7_8b_candidates:
    - model: "Qwen3-8B"
      role: "generalist primary practical-center candidate"
      documented_parameters: "8.2B"
      documented_native_context: "32768"
      documented_extended_context: "131072 with YaRN validation"
      evidence: "[75]"
      status: "candidate; not certified"
    - model: "Ministral-8B-Instruct-2410"
      role: "independent 8B generalist comparator"
      documented_parameters: "8B"
      documented_context: "128K model-card context; vLLM limitation documented at 32K in reviewed card"
      evidence: "[35]"
      status: "conditional candidate; license/runtime review required"
  code_specialist_candidates:
    - model: "Qwen2.5-Coder-7B-Instruct"
      role: "primary 7–8B coding-specialist comparator"
      documented_parameters: "7.61B"
      documented_context: "32768 configuration; 131072 with YaRN guidance"
      evidence: "[28]"
      status: "candidate; not certified"
    - model: "DeepSeek-Coder-V2-Lite-Instruct"
      role: "larger MoE coding challenger"
      documented_parameters: "16B total; 2.4B active"
      documented_context: "128K"
      evidence: "[62]"
      status: "stretch candidate; resource test required"
    - model: "Qwen3-Coder-30B-A3B-Instruct"
      role: "large coding quality-ceiling challenger"
      documented_parameters: "30.5B total; 3.3B active"
      documented_context: "262144 native"
      evidence: "[33]"
      status: "stretch-only candidate; coexistence test required"
  smaller_controls:
    - model: "Phi-4-mini-instruct"
      role: "primary 3–4B efficiency control"
      documented_parameters: "3.8B"
      documented_context: "128K"
      documented_license: "MIT"
      evidence: "[61]"
      status: "candidate; not certified"
    - model: "Gemma 3 IT 4B"
      role: "secondary 4B efficiency control"
      documented_parameters: "4B"
      documented_code_results: "HumanEval 71.3; Natural2Code 70.3; LiveCodeBench 12.6"
      evidence: "[16]"
      status: "optional candidate; not certified"
  larger_challengers:
    - model: "Gemma 3 IT 12B"
      role: "direct 12B generalist challenger"
      documented_parameters: "12B"
      documented_code_results: "HumanEval 85.4; Natural2Code 80.7; LiveCodeBench 24.6"
      evidence: "[16]"
      status: "conditional challenger; resource test required"
    - model: "DeepSeek-Coder-V2-Lite-Instruct"
      role: "16B total / 2.4B active coding MoE challenger"
      documented_parameters: "16B total; 2.4B active"
      evidence: "[62]"
      status: "stretch challenger; total-memory test required"
    - model: "Qwen3-Coder-30B-A3B-Instruct"
      role: "30.5B total / 3.3B active coding MoE challenger"
      documented_parameters: "30.5B total; 3.3B active"
      evidence: "[33]"
      status: "stretch-only challenger"
  benchmark_priority:
    - "Qwen3-8B"
    - "Qwen2.5-Coder-7B-Instruct"
    - "Phi-4-mini-instruct"
    - "Gemma 3 IT 12B"
    - "Ministral-8B-Instruct-2410 if license and runtime are acceptable"
    - "Gemma 3 IT 4B if a second efficiency control is affordable"
    - "DeepSeek-Coder-V2-Lite-Instruct if total-memory measurements are credible"
    - "Qwen3-Coder-30B-A3B-Instruct only as a stretch configuration"
  fixture_hypotheses:
    CODE_01:
      strongest_initial_hypothesis: "Qwen3-8B with explicit reasoning mode and schema-constrained classification"
      primary_risk: "smaller controls may misclassify unknown failures as known"
      decisive_metrics:
        - "failure-class accuracy"
        - "false-success rate"
        - "missed escalation"
        - "evidence completeness"
    CODE_02:
      strongest_initial_hypothesis: "Qwen2.5-Coder-7B-Instruct"
      primary_risk: "scope expansion or unnecessary cleanup around the exact patchspec"
      decisive_metrics:
        - "intended-file precision"
        - "minimal diff"
        - "acceptance-test result"
        - "unauthorized edits"
    CODE_03:
      strongest_initial_hypothesis: "Qwen2.5-Coder-7B-Instruct"
      primary_risk: "more than one inferred repair attempt"
      decisive_metrics:
        - "one-attempt compliance"
        - "minimality"
        - "test result"
        - "unexpected-failure escalation"
    CODE_04:
      strongest_initial_hypothesis: "Qwen3-8B with explicit ambiguity-stop contract"
      primary_risk: "coding-specialist confident continuation instead of escalation"
      decisive_metrics:
        - "correct escalation"
        - "missed escalation"
        - "unauthorized edits"
        - "evidence quality"
    CODE_05:
      strongest_initial_hypothesis: "No model advantage established; Qwen3-8B is the first test candidate"
      primary_risk: "wrong-root access or incorrect provenance"
      decisive_metrics:
        - "root access trace"
        - "forbidden-root attempts"
        - "read/write provenance"
        - "atomic acceptance outcome"
  escalation_risks:
    false_success: "High-priority APEX failure; must be measured separately from task completion."
    missed_escalation: "High-priority failure for ambiguous, architectural, security, permission, Git-conflict, and unknown cases."
    scope_drift: "Measure undeclared files, public-API changes, refactors, and cross-root access."
    repair_looping: "At most one locally inferred-fix attempt is permitted."
    authority_confusion: "Treat repository, browser, tool, and model content as untrusted data rather than permission."
    destructive_git_behavior: "Block reset, force push, destructive rewrite, branch proliferation, and undeclared cross-repository operations."
  size_tradeoff_hypotheses:
    three_to_four_b_vs_seven_to_eight_b: "7–8B should materially improve bounded coding and escalation, but this remains unverified until CODE-01–05 runs."
    seven_to_eight_b_vs_twelve_b: "12B should be retained only if measured gains reduce CLI escalation enough to justify memory, latency, loading, and coexistence costs."
    seven_to_eight_b_vs_moe_challengers: "Low active-parameter counts do not prove low total-memory or coexistence cost."
    generic_benchmarks: "Generic coding scores may prioritize candidates but cannot certify APEX execution."
  context_findings:
    target_working_context: "Approximately 32768 tokens"
    stretch_context: "Approximately 65536 tokens"
    retrieval_policy: "Just-in-time retrieval; do not stuff whole repositories into context."
    qwen3_8b: "32768 native; 131072 validated with YaRN; benchmark YaRN separately because the card warns about shorter-context effects."
    qwen25_coder_7b: "32768 configuration; longer context through YaRN guidance."
    ministral_8b: "128K documented, with 32K vLLM limitation noted in reviewed model card."
  resource_findings:
    machine_profile: "HP OmniBook X Flip 16-as0xxx; Windows 11; Intel Core Ultra 7 258V; approximately 31.6 GB RAM; Intel Arc 140V integrated graphics."
    first_runtime_track: "Pinned llama.cpp Windows SYCL configuration."
    required_measurements:
      - "model artifact and quantization"
      - "runtime and backend versions"
      - "load/unload time"
      - "prompt and generation latency"
      - "peak system RAM"
      - "shared GPU memory pressure"
      - "browser/IDE/test coexistence"
      - "CPU/GPU layer split"
    status: "No actual throughput, peak RAM, thermal, or coexistence result verified."
  unknowns_for_local_test:
    - "Actual Qwen3-8B and Qwen2.5-Coder-7B APEX fixture accuracy."
    - "Correct escalation rates under ambiguous and unknown regressions."
    - "Unauthorized action attempt rates under hostile source and tool output."
    - "Exact quantization and runtime configuration that best fits Intel Arc 140V."
    - "Actual shared-memory availability and sustained throughput on the specified laptop."
    - "Whether 12B materially reduces CLI escalation after resource penalties."
    - "Whether coding specialization increases false success or missed escalation."
    - "Whether 32K context is operationally superior to smaller just-in-time retrieval."
    - "License acceptability and Windows runtime reproducibility for Ministral-8B."
    - "Whether MoE challengers fit the coexistence envelope despite low active-parameter counts."
  overall_confidence_0_to_100: 68
```
