---
title: "Local Model Research Result — Landscape — Perplexity"
doc_type: local_model_research_result
initiative: local-orchestration-engine
prompt: apex-meta/local-orchestration-engine/research-prompts/LOCAL-MODEL-RESEARCH-LANDSCAPE-2026-08-08.md
prompt_id: A
agent: perplexity
agent_model_label: "Beste (Best/auto-select) — deliberately not hand-picked, to avoid biasing toward a Claude-family model"
agent_mode: "Suche (standard Search), not Vertiefte Recherche (Deep Research)"
account_tier: "subscription (plan tier not disclosed by UI)"
run_id: R3
run_started: "2026-08-08"
run_duration_seconds: null
evidence_date: 2026-08-08
chat_url: "https://www.perplexity.ai/search/4316308e-1d13-4495-9e34-9d7bbfef9860"
bundle_sha256: "638c150c3503cf9ee2e802a1870db18c088b268fc4efb1712b770e62a3da7d10"
retries: 1
interruptions:
  - "First paste attempt used execCommand('insertText'), which corrupted the Lexical editor's content (stripped newlines, glued adjacent words). Detected before submission via length/content checks; field was cleared with real ctrl+a + Delete keystrokes (execCommand select/delete did not work) and the bundle was re-inserted via a synthetic ClipboardEvent('paste') with a DataTransfer payload, which preserved line breaks correctly."
  - "After the corrected paste, the composer's mode silently switched to 'Vertiefte Recherche' (Deep Research); manually reverted to 'Suche' before submitting, and the pasted bundle content was verified intact after the mode change."
uncontrolled_variables:
  - "Perplexity persists unsent composer drafts in localStorage across reloads, which complicated clearing the first corrupted attempt; resolved without reloading, using in-page keyboard clearing instead."
  - "'Beste' auto-routes to an underlying model Perplexity does not disclose in the UI; the exact model actually used for this run is unknown."
status: "raw agent output; unverified; no APEX authority"
---

# Local Model Research Result — Landscape — Perplexity

> Operator note: this file is the verbatim (reformatted-for-markdown) output of Perplexity executing Research Prompt A (Local Model Landscape) against the identical frozen bundle used for ChatGPT and Gemini (same `bundle_sha256`). This is raw agent output. It carries no APEX authority and has not been checked against local benchmark fixtures. Perplexity reports drawing on 90 sources across 6 research steps; a UI "6 Schritte abgeschlossen" (6 steps completed) indicator preceding the response has been omitted here as a cosmetic artifact, and the source count / follow-up suggestions are preserved at the end of this document.

## APEX Local Model Landscape Research Packet

### 1. Executive Finding

INFERRED: The strongest initial bake-off should be centered on Qwen3-8B, with Qwen3-4B as the efficiency control and Qwen3-14B as the principal larger challenger. This set is unusually coherent because the three models share a family, licensing posture, reasoning/tool-oriented chat-template lineage, and documented local-serving paths, reducing cross-family confounds.

DOCUMENTED: Qwen3-8B is an Apache-2.0 model with a 32K native context position and extended-context support documented through the Qwen model materials; Qwen3-4B and Qwen3-14B provide smaller and larger comparison points. Qwen3 model repositories document deployment through local-serving stacks including Transformers, vLLM and SGLang. [sources: huggingface +3]

INFERRED: Qwen3-8B should be the first execution candidate, not a production selection. The benchmark must determine whether its added execution reliability over Qwen3-4B offsets the likely resource cost, and whether Qwen3-14B produces enough improvement on APEX fixtures to justify substantially worse coexistence.

UNKNOWN: No public evidence establishes reliable APEX performance, zero unauthorized actions, Windows laptop coexistence, or a validated 32K working-context envelope for any candidate. Those properties require the APEX benchmark portfolio and the specified HP OmniBook test environment.

### 2. Evidence Date and Freshness

DOCUMENTED: The research evidence was collected on 2026-08-08, using current public search results and official or first-party model/runtime materials where available.

| Evidence area | Freshness | Evidence status |
|---|---|---|
| Qwen3 family model cards and repositories | 2025–2026 repository material | DOCUMENTED |
| Gemma 3 model documentation | Current official Google documentation located; exact page revision date not verified | DOCUMENTED / UNKNOWN date |
| Phi-4-mini-instruct model card | 2025-03-03 repository publication | DOCUMENTED [huggingface] |
| SmolLM3 materials | 2025–2026 repository/documentation material | DOCUMENTED [huggingface +1] |
| Devstral Small documentation | 2025–2026 Mistral materials | DOCUMENTED [docs.mistral +2] |
| llama.cpp Intel runtime support | Current GitHub documentation and releases located | DOCUMENTED [github +2] |
| Windows/Intel Core Ultra 7 258V performance | No direct machine measurement performed | UNKNOWN |
| APEX task execution quality | No APEX fixture execution performed | UNKNOWN |

UNKNOWN: Search-result publication dates are not equivalent to model-release dates. The bake-off record should capture the exact repository commit, model-file hash, runtime version, quantization, prompt contract and generation configuration.

### 3. Primary 7–8B Shortlist

**3.1 Qwen3-8B**
DOCUMENTED: Exact candidate: Qwen/Qwen3-8B; parameter class: 8B dense model; repository evidence identifies Apache-2.0 licensing. [huggingface]
DOCUMENTED: Qwen3 model materials expose reasoning-mode and tool-call conventions through the chat template; the repository includes local-serving examples for OpenAI-compatible endpoints. [huggingface +1]
DOCUMENTED: Qwen3 materials describe native context around 32K for the 8B class, with longer-context configuration discussed through YaRN; the exact reliable working-context behavior remains separate from the advertised maximum. [huggingface]
DOCUMENTED: Qwen3-8B is available in local artifact ecosystems, including Hugging Face and llama.cpp-compatible conversion paths; Qwen3 repositories also reference Ollama, LM Studio, MLX-LM and llama.cpp support. [huggingface +1]
INFERRED: This is the best first candidate for the APEX practical-center hypothesis because it directly occupies the operator's preferred size class while offering reasoning, structured tool-call formatting and broad runtime availability.
UNKNOWN: Reliable structured-action accuracy, injection resistance, escalation calibration, 32K execution quality and coexistence on the target laptop.

**3.2 Ministral-8B-Instruct-2410**
DOCUMENTED: Exact candidate: mistralai/Ministral-8B-Instruct-2410; parameter class: 8B; model materials describe local/edge use and a 128K trained context window. [huggingface]
DOCUMENTED: The model card describes vLLM and Mistral Inference deployment, but states that the cited vLLM path was capped at 32K at the time of that model-card version and that a single GPU deployment required 24 GB of GPU RAM in the documented configuration. [huggingface]
DOCUMENTED: The cited model is under a Mistral Research License with research-purpose limitations in the retrieved license material. [huggingface]
INFERRED: It is useful as a technical comparison candidate but is a weaker default for APEX unless the intended use is demonstrably compatible with its license and runtime requirements.
UNKNOWN: Whether its license permits the intended APEX project use, whether its current runtime path works effectively on Intel integrated graphics, and whether it improves bounded execution over Qwen3-8B.

**3.3 Gemma 3 4B/12B as Cross-Family Controls**
DOCUMENTED: Google's Gemma 3 documentation describes 4B and 12B instruction-tuned variants with 128K context support; the retrieved model material also identifies a 4B model intended for compact/on-device use. [google +2]
INFERRED: Gemma 3 4B is a useful cross-family efficiency control, while Gemma 3 12B can serve as an alternative larger challenger if its license and runtime integration are acceptable.
UNKNOWN: The exact current license terms applicable to the project, Windows/Intel runtime maturity, native versus extended-context reliability, and structured tool-call behavior under the APEX contract.
DEPRIORITIZED: Gemma 3 should not displace the Qwen3 family comparison in the first run unless licensing or runtime evidence makes Qwen3 unsuitable.

Primary shortlist conclusion:
INFERRED: The first primary-center run should contain: Qwen/Qwen3-8B; mistralai/Ministral-8B-Instruct-2410, subject to license review; optionally google/gemma-3-4b-it and google/gemma-3-12b-it for cross-family controls.
UNKNOWN: Whether a later 2026 model release supersedes these candidates for the target workload; no sufficiently complete, primary-source evidence was retrieved for every newer candidate.

### 4. 3–4B Efficiency Controls

**4.1 Qwen3-4B**
DOCUMENTED: Exact candidate: Qwen/Qwen3-4B; Apache-2.0 licensing is documented in the repository. [huggingface]
DOCUMENTED: The model materials state that context lengths up to 131,072 tokens were validated using YaRN and provide vLLM/SGLang local-serving examples. [huggingface +1]
DOCUMENTED: The tokenizer/chat template includes a structured tool-call representation with tool names and JSON arguments. [huggingface]
INFERRED: Qwen3-4B is the most important control because it minimizes family, tokenizer and prompt-contract differences when compared with Qwen3-8B.
UNKNOWN: Whether its lower resource burden preserves sufficient semantic action correctness, failure classification and escalation reliability.

**4.2 Microsoft Phi-4-mini-instruct**
DOCUMENTED: Exact candidate: microsoft/Phi-4-mini-instruct; model card identifies 3.8B parameters, a dense decoder-only Transformer and MIT licensing. [huggingface]
DOCUMENTED: The model card positions the model around instruction following and function calling. [huggingface]
INFERRED: Phi-4-mini-instruct is a strong independent efficiency control because it tests whether the Qwen3-4B result is family-specific.
UNKNOWN: The retrieved primary evidence did not establish the exact current context configuration, Windows Intel acceleration path, APEX tool-call reliability or injection behavior.

**4.3 SmolLM3-3B**
DOCUMENTED: SmolLM3 is presented as a 3B multilingual reasoner with long-context support and tool calling; its materials describe XML and Python tool interfaces. [huggingface +1]
DOCUMENTED: HuggingFaceTB/SmolLM3-3B-Base repository material identifies Apache-2.0 licensing and local inference paths including llama.cpp and ONNX. [huggingface]
INFERRED: SmolLM3-3B is a useful low-cost control for context/tool-format experiments, but its base-model status means the instruction-tuned artifact and exact harness must be selected carefully.
UNKNOWN: Whether the relevant instruction-tuned artifact is currently available in a sufficiently stable form and whether it can meet APEX's bounded-execution requirements.

Efficiency-control priority:
INFERRED: Run Qwen3-4B first, Phi-4-mini-instruct second, and SmolLM3-3B only if the benchmark team wants a third low-resource control. The objective is not to identify the smallest runnable model; it is to quantify the execution-quality delta between approximately 4B and 8B.

### 5. 12–14B Challengers

**5.1 Qwen3-14B**
DOCUMENTED: Exact candidate: Qwen/Qwen3-14B; retrieved repository material identifies approximately 14.8B total parameters, approximately 13.2B non-embedding parameters, Apache-2.0 licensing, 32,768 native context and 131,072-token YaRN context. [huggingface]
DOCUMENTED: Qwen3-14B is available through the same general Qwen deployment ecosystem as the smaller models. [huggingface]
INFERRED: Qwen3-14B is the mandatory larger challenger for the first serious size-class comparison because it preserves model-family comparability with Qwen3-4B and Qwen3-8B.
INFERRED: On a 32 GB unified-memory laptop, Qwen3-14B is likely to impose materially greater memory pressure and latency than Qwen3-8B, especially at 32K working context and while browsers, IDEs and tests remain active.
UNKNOWN: Actual quantized model size, load time, sustained latency, peak RAM, Intel backend behavior and coexistence impact on the specified machine.

**5.2 Gemma 3 12B**
DOCUMENTED: Google's Gemma 3 materials identify an instruction-tuned 12B model with a 128K context window. [docs.aws.amazon +1]
INFERRED: Gemma 3 12B is a reasonable cross-family challenger if the project accepts the relevant Gemma terms and a compatible local runtime is verified.
UNKNOWN: Whether it materially outperforms Qwen3-8B on APEX action/state fixtures, whether its multimodal design provides any benefit to the text-heavy bounded executor role, and whether it fits the coexistence envelope.

Challenger conclusion:
INFERRED: The initial larger comparison should use Qwen3-14B as the principal challenger and Gemma 3 12B only as an optional cross-family challenger. The larger model should not enter the planner registry unless its measured gains are large enough to compensate for memory, latency, swap and coexistence penalties.

### 6. >14B Stretch Case

**Devstral Small 1.1 / 2507**
DOCUMENTED: Mistral describes Devstral Small 1.1 as an Apache-2.0 coding model supporting Mistral function-calling and XML formats. [mistral]
DOCUMENTED: Devstral Small materials describe a 24B text model aimed at codebase exploration, multi-file editing and software-engineering agents, with a 128K context. [docs.mistral +1]
DOCUMENTED: Mistral describes Devstral Small 2 as a 24B model locally deployable on consumer hardware, although that does not establish suitability for the specified 32 GB Windows laptop under coexistence load. [mistral]
INFERRED: Devstral is decision-relevant only for the bounded-coding task class, not as a general Weekly or Multi-Agent executor.
INFERRED: A 4-bit or comparable quantized Devstral configuration may be runnable in system memory, but the target laptop's integrated graphics and unified memory make sustained coexistence a material risk.
UNKNOWN: Whether the exact intended Devstral artifact, quantization and Intel backend can complete CODE-01 through CODE-05 without making the browser/IDE/test workload unusable.

Stretch-case rule:
INFERRED: Include Devstral only in a gated coding-specialist experiment after Qwen3-8B and Qwen3-14B baselines. Do not include it in the first general executor bake-off merely because it is specialized for coding.

### 7. Coding Challengers

| Candidate | Evidence | APEX role | Status |
|---|---|---|---|
| Qwen2.5-Coder-7B-Instruct | DOCUMENTED: Official repository identifies a 7B instruction-tuned coding model and long-context support up to 128K. [huggingface] | Coding control near the practical-center size | INCLUDE if artifact/runtime is stable |
| Devstral Small 1.1 / 2507 | DOCUMENTED: Mistral positions it for codebase tools, multi-file editing and coding agents; Apache-2.0 and function-call/XML support are documented. [mistral +1] | Larger coding specialist | STRETCH |
| Qwen3-Coder-Next | DOCUMENTED: Qwen describes it as an open-weight model designed for coding agents, local development and tool calling. [huggingface] | Current coding-specialist monitor | DEFER pending exact resource profile |
| Qwen3-8B | DOCUMENTED: General Qwen3 tool-call template and local deployment support are documented. [huggingface +1] | Generalist coding baseline | PRIMARY |

INFERRED: Qwen2.5-Coder-7B-Instruct is the most controlled coding challenger because it remains close to the 7–8B class. Devstral is more likely to reduce difficult coding escalations, but its size makes it unsuitable as an assumed default.
UNKNOWN: Public coding benchmark results do not establish performance on APEX's micro-fix envelope, typed escalation requirements, forbidden-root containment or "no architecture change" constraints.

### 8. Excluded or Deprioritized Candidates

DEPRIORITIZED: Mistral 8B is not a first-line production candidate because the retrieved model card identifies a research license and a documented 24 GB single-GPU requirement for its vLLM configuration. [huggingface +1]
DEPRIORITIZED: Generic 20B–30B models without coding/tool-specific evidence are excluded because the benchmark objective is bounded execution, not generic reasoning quality.
DEPRIORITIZED: Models selected solely from public leaderboards are excluded because the APEX authority documents explicitly require fixture-level execution, safety and coexistence evidence.
DEPRIORITIZED: Models with only advertised 128K context but no reliable long-context evidence are not treated as 32K-certified.
UNKNOWN: The current status of every 2026 model family was not exhaustively verified; newer candidates should enter only after primary model-card, license and runtime evidence is captured.

### 9. Capability-by-Task-Class Matrix

Legend: P = plausible candidate role; C = control/challenger; U = unknown pending APEX testing; R = elevated resource risk.

| Candidate | CODE | Weekly | MA evidence worker | Hostile resistance | 32K plausibility | Structured/tool output | Coexistence risk | Registry hypothesis |
|---|---|---|---|---|---|---|---|---|
| Qwen3-4B | P/C | P/C | P/C | U | P, not certified | P | Lower than 8B, U | Efficiency profile |
| Qwen3-8B | P | P | P | U | P, not certified | P | Medium, U | Default generalist hypothesis |
| Qwen3-14B | P | P | P | U | P, higher resource risk | P | High, U/R | Quality challenger |
| Phi-4-mini-instruct | P/C | P/C | P/C | U | U | P from function-calling positioning | Lower, U | Independent efficiency profile |
| SmolLM3-3B | C | C | C | U | U | P | Lower, U | Lightweight control |
| Gemma 3 4B | C | C | C | U | P from documented context, reliability U | U | Lower, U | Cross-family control |
| Gemma 3 12B | P/C | P/C | P/C | U | P from documented context, reliability U | U | High, U/R | Cross-family challenger |
| Qwen2.5-Coder-7B | P for coding | C | C | U | P from advertised support, reliability U | U | Medium, U | Coding control |
| Devstral Small | P for difficult coding | C | C | U | P from documented 128K | P | High/R | Coding specialist |
| Qwen3-Coder-Next | P for coding | U | U | U | U | P from tool-calling positioning | High/unknown | Deferred coding specialist |

INFERRED: Qwen3-8B is the best generalist hypothesis, Qwen3-4B is the best paired efficiency control, Qwen3-14B is the best same-family quality challenger, and Devstral is the most relevant specialist test.

### 10. Context, Tool and Structured-Output Evidence

Context:
DOCUMENTED: Qwen3-8B and Qwen3-14B materials distinguish native context from longer YaRN-configured context; Qwen3-4B materials document validation up to 131,072 tokens using YaRN. [huggingface +2]
DOCUMENTED: Gemma 3 4B and 12B materials describe 128K context. [docs.aws.amazon +1]
DOCUMENTED: Devstral Small materials describe a 128K context. [docs.mistral +1]
INFERRED: APEX should treat 32K as the working target and 64K as a stretch test, regardless of advertised maximum context.
UNKNOWN: Reliable retrieval accuracy, action selection and latency degradation at 8K, 16K, 32K and 64K on the target machine.

Tool use and structured output:
DOCUMENTED: Qwen3 tokenizer/chat-template material defines tool descriptions and JSON arguments within a structured tool-call format. [huggingface]
DOCUMENTED: Phi-4-mini-instruct is positioned by Microsoft as supporting function calling. [huggingface]
DOCUMENTED: SmolLM3 materials describe XML and Python tool-calling interfaces. [huggingface]
DOCUMENTED: Devstral Small 1.1 supports Mistral function-calling and XML formats. [mistral]
INFERRED: These features make the candidates suitable for harness experiments, but they do not establish schema validity under retries, semantic correctness, authority compliance or resistance to tool-output injection.
UNKNOWN: Whether constrained decoding or external validators are available and stable for every selected runtime.

### 11. Runtime and Artifact Availability Map

| Runtime/artifact path | Evidence | Windows/Intel relevance | Assessment |
|---|---|---|---|
| llama.cpp CPU backend | DOCUMENTED: llama.cpp provides Windows builds and an OpenAI-compatible local server. [github +1] | High; CPU fallback is expected | Required baseline |
| llama.cpp SYCL | DOCUMENTED: llama.cpp documents SYCL support for Intel GPUs, including built-in GPUs/iGPUs, with Windows build instructions using Intel oneAPI. [github +1] | Directly relevant to Arc 140V | Primary Intel-GPU experiment |
| llama.cpp OpenVINO | DOCUMENTED: llama.cpp lists OpenVINO support as in progress for Intel CPUs, GPUs and NPUs. [github] | Potentially relevant to Core Ultra NPU/iGPU | Experimental; verify exact support |
| Transformers | DOCUMENTED: Qwen3 repositories advise current Transformers versions and provide local Python deployment paths. [huggingface +1] | CPU-compatible; acceleration depends on backend | Reference correctness path |
| vLLM | DOCUMENTED: Qwen3 and Ministral materials provide vLLM serving examples. [huggingface +1] | Likely less suitable for the target integrated-GPU setup without validation | Secondary; do not assume Intel support |
| SGLang | DOCUMENTED: Qwen3 repositories provide SGLang server examples. [huggingface +1] | Runtime feasibility on this Windows machine is unverified | Secondary |
| GGUF artifacts | DOCUMENTED: llama.cpp supports Hugging Face model retrieval and GGUF-compatible models; Devstral materials provide GGUF download examples. [huggingface +1] | Practical for CPU/SYCL testing | Preferred artifact family for first bake-off |
| MLX | DOCUMENTED: Some repositories reference MLX local inference. [huggingface +1] | Apple-oriented; not a first choice for Windows Intel | Exclude from initial runtime plan |

DOCUMENTED: Intel integrated graphics uses system memory rather than a separate dedicated graphics-memory bank, and Intel states that Windows' reported shared-memory limit is not an ongoing reservation. [intel]
INFERRED: The machine profile should be treated as a unified-memory system. "Dedicated VRAM" values reported by Windows must not be converted directly into available model memory, and no production throughput conclusion should be drawn from the Arc 140V label.
UNKNOWN: Whether the Core Ultra 7 258V's NPU is usable by the selected runtime for these model architectures, and whether NPU offload improves whole-system coexistence rather than merely isolated inference.

### 12. Size–Resource–Execution Hypothesis Matrix

| Size class | Expected execution benefit | Expected resource burden | APEX hypothesis | Falsification condition |
|---|---|---|---|---|
| 3–4B | Lower reasoning depth and potentially weaker ambiguity handling | Lowest | May win routine structured operations if safety and completion match 8B | Fails if escalation, tool arguments or state classification degrade materially |
| 7–8B | Better balance of reasoning, tool use and resource cost | Moderate | Expected practical optimum | Fails if 4B matches quality with materially better coexistence, or 14B wins decisively |
| 12–14B | Potentially stronger difficult classification and coding | High | Useful challenger, not default | Fails if gains do not reduce CLI escalation or interventions enough |
| >14B coding specialist | Potentially better multi-file coding and repair | Very high | May justify a coding-only route | Fails if memory/swap/coexistence makes the workflow unusable |

INFERRED: The principal comparison is not token throughput. It is successful bounded jobs per wall time, human intervention, CLI escalation, unauthorized attempts and coexistence impact.
UNKNOWN: All numerical thresholds beyond zero successful unauthorized actions. The authority portfolio correctly leaves utility thresholds open until baseline distributions exist.

### 13. Benchmark Priority Order

MEASURED target: Establish the harness and configuration identity for Qwen3-4B, Qwen3-8B and Qwen3-14B using the same fixture, runtime policy and guardrails.
MEASURED target: Run CODE-01 through CODE-05, including exact patching, one-line inferred repair, ambiguous escalation and multi-repository containment.
MEASURED target: Run MA-01, MA-02, MA-05 and MA-06 to test worker boundaries, evidence-only behavior, typed routing and injection containment.
MEASURED target: Run WEEKLY-01 through WEEKLY-06, emphasizing checkpoint/resume, unknown-state handling, browser recovery and raw-evidence preservation.
MEASURED target: Run INJECT-01 through INJECT-08 and record both model attempts and system containment outcomes.
MEASURED target: Repeat at approximately 8K, 16K, 32K and 64K where supported, using just-in-time retrieval rather than irrelevant context stuffing.
MEASURED target: Run COEX-01 through COEX-06 with browser, IDE, terminals, tests and occasional CLI-agent load.
MEASURED target: Add Phi-4-mini-instruct and Qwen2.5-Coder-7B-Instruct as independent controls.
MEASURED target: Add Gemma 3 4B/12B only after license and runtime paths are frozen.
MEASURED target: Add Devstral only as a coding-specialist stretch experiment.

INFERRED: Promote only model+runtime+harness configurations that pass hard gates and receive task-class-specific capability profiles.
UNKNOWN: Numeric acceptance thresholds for utility and coexistence until baseline runs reveal distributions.

### 14. Major Unknowns Requiring Local APEX Testing

Execution and safety:
- Successful unauthorized actions for every candidate and runtime.
- Unauthorized-attempt rate, including wrong-root access, scope drift, prompt-injection following and authority-promotion attempts.
- False-success rate under ambiguous browser, provider, test and Git states.
- Correct escalation rate versus unnecessary escalation rate.
- Whether structured output remains valid after retries and partial tool failures.

Context and recovery:
- Reliable context tier for each candidate at 32K.
- Accuracy degradation from 8K to 16K to 32K and 64K.
- Duplicate-submission rate after checkpoint/restart.
- Whether browser recovery preserves declared intent without inventing a new consequential mode.
- Whether raw evidence remains reconstructable when the local model produces an execution index.

Resource and coexistence:
- Peak RAM and load time for each quantized artifact.
- Sustained CPU, iGPU and NPU utilization.
- Model swap/unload time and scheduler behavior under concurrent jobs.
- Browser/IDE/test responsiveness during inference.
- Whether SYCL or OpenVINO acceleration improves whole-system utility.
- Actual tokens per second and time-to-first-action under realistic 32K working contexts.

Licensing and operational constraints:
- Final license suitability for every candidate and intended APEX distribution/use mode.
- Reproducible Windows packaging for each runtime.
- Long-term maintenance status of each runtime/backend combination.

### 15. Source Appendix

Primary model and runtime sources:
- Qwen3-8B license and repository materials [huggingface +1]
- Qwen3-4B model, deployment and license materials [huggingface +3]
- Qwen3-14B architecture, context and license material [huggingface]
- Ministral-8B model card and license material [huggingface +1]
- Gemma 3 model-card and model-family material [google +2]
- Microsoft Phi-4-mini-instruct model card [huggingface]
- SmolLM3 model and documentation [huggingface +3]
- Qwen2.5-Coder-7B-Instruct model card [huggingface]
- Qwen3-Coder-Next model card [huggingface]
- Mistral Devstral Small documentation and release material [docs.mistral +3]
- llama.cpp runtime and Intel backend documentation [github +4]
- Intel integrated-graphics memory explanation [intel]

Evidence-quality boundary:
INFERRED: Official model cards, repositories, technical documentation and release notes are appropriate for establishing model identity, declared context, tool interfaces, licenses and runtime availability.
UNKNOWN: None of those sources establish APEX certification. Public benchmark numbers, vendor claims and community throughput reports should be retained only as prioritization evidence and must not replace the local fixture portfolio.

### 16. YAML

```yaml
local_model_landscape:
  evidence_date: "2026-08-08"
  primary_7_8b_candidates:
    - id: "Qwen/Qwen3-8B"
      parameter_class: "~8B"
      version_date: "Repository/model materials dated 2025; exact release date not independently verified in this run"
      license: "Apache-2.0"
      role: "Primary generalist practical-center hypothesis"
      evidence_status: "DOCUMENTED identity and declared capabilities; APEX execution UNKNOWN"
    - id: "mistralai/Ministral-8B-Instruct-2410"
      parameter_class: "~8B"
      version_date: "2024-10 model-card/repository label"
      license: "Mistral Research License; research-use limitation documented in retrieved material"
      role: "Conditional cross-family 8B comparison"
      evidence_status: "DOCUMENTED identity; project-use suitability UNKNOWN"
    - id: "google/gemma-3-4b-it"
      parameter_class: "~4B"
      version_date: null
      license: "Gemma terms require verification"
      role: "Optional cross-family compact control"
      evidence_status: "DOCUMENTED family/context; exact current project constraints UNKNOWN"
    - id: "google/gemma-3-12b-it"
      parameter_class: "~12B"
      version_date: null
      license: "Gemma terms require verification"
      role: "Optional cross-family larger challenger"
      evidence_status: "DOCUMENTED family/context; exact current project constraints UNKNOWN"
  efficient_3_4b_controls:
    - id: "Qwen/Qwen3-4B"
      parameter_class: "~4B"
      version_date: "Repository materials dated 2025-04"
      license: "Apache-2.0"
      role: "Primary efficiency control"
    - id: "microsoft/Phi-4-mini-instruct"
      parameter_class: "3.8B"
      version_date: "2025-03-03 repository publication"
      license: "MIT"
      role: "Independent efficiency control"
    - id: "HuggingFaceTB/SmolLM3-3B-Base"
      parameter_class: "~3B"
      version_date: "Repository material dated 2025-10"
      license: "Apache-2.0"
      role: "Optional lightweight/context/tool control"
  larger_12_14b_challengers:
    - id: "Qwen/Qwen3-14B"
      parameter_class: "~14.8B total; ~13.2B non-embedding"
      version_date: "Repository materials dated 2025-04"
      license: "Apache-2.0"
      role: "Principal same-family larger challenger"
    - id: "google/gemma-3-12b-it"
      parameter_class: "~12B"
      version_date: null
      license: "Gemma terms require verification"
      role: "Optional cross-family challenger"
  over_14b_stretch_candidates:
    - id: "mistralai/Devstral-Small-2507"
      parameter_class: "~24B"
      version_date: "2025-07 model family/release material"
      license: "Apache-2.0 documented for Devstral Small 1.1"
      role: "Coding-only stretch challenger"
      runnable_status: "Plausible only with quantized artifact and measured coexistence; not established"
    - id: "mistralai/Devstral-Small-1.1"
      parameter_class: "~24B"
      version_date: "2025-07 release material"
      license: "Apache-2.0"
      role: "Coding-only stretch challenger"
      runnable_status: "Plausible only with quantized artifact and measured coexistence; not established"
  coding_challengers:
    - id: "Qwen2.5-Coder-7B-Instruct"
      parameter_class: "~7B"
      role: "Same-size coding control"
    - id: "mistralai/Devstral-Small-2507"
      parameter_class: "~24B"
      role: "Large coding-agent specialist"
    - id: "mistralai/Devstral-Small-1.1"
      parameter_class: "~24B"
      role: "Large coding-agent specialist"
    - id: "Qwen3-Coder-Next"
      parameter_class: null
      role: "Deferred current coding-agent monitor"
      reason: "Exact resource and target-machine feasibility not established"
  benchmark_priority:
    - "Qwen3-4B baseline"
    - "Qwen3-8B primary-center baseline"
    - "Qwen3-14B same-family challenger"
    - "CODE-01 through CODE-05"
    - "MA-01, MA-02, MA-05 and MA-06"
    - "WEEKLY-01 through WEEKLY-06"
    - "INJECT-01 through INJECT-08"
    - "Context tests at approximately 8K, 16K, 32K and 64K where supported"
    - "COEX-01 through COEX-06"
    - "Phi-4-mini-instruct and Qwen2.5-Coder-7B-Instruct controls"
    - "Gemma 3 cross-family tests after license/runtime verification"
    - "Devstral coding-only stretch test"
  excluded_or_deprioritized:
    - "Generic larger models without APEX-relevant tool/execution evidence"
    - "Candidates selected only from public leaderboards"
    - "Ministral-8B as a default until its research-license suitability is resolved"
    - "Models with advertised long context but no reliable working-context evidence"
    - "Models whose runtime cannot be reproduced on Windows 11 with the required observability and resource controls"
  context_findings:
    apex_working_target: "~32K reliably usable working context"
    stretch_target: "~64K where supported"
    documented_context_patterns:
      Qwen3_4B: "Up to 131K with YaRN documented; reliable APEX behavior UNKNOWN"
      Qwen3_8B: "Native/working context materials indicate approximately 32K with extended YaRN configuration discussed; reliable APEX behavior UNKNOWN"
      Qwen3_14B: "32K native and 131K YaRN documented; reliable APEX behavior UNKNOWN"
      Gemma3_4B_12B: "128K documented; reliable APEX behavior UNKNOWN"
      Devstral_Small: "128K documented; reliable APEX behavior UNKNOWN"
    conclusion: "Advertised maximum context must not be treated as APEX certification"
  structured_tool_findings:
    Qwen3: "Structured tool-call template with JSON arguments documented"
    Phi4Mini: "Function-calling positioning documented"
    SmolLM3: "XML and Python tool interfaces documented"
    Devstral: "Mistral function-calling and XML formats documented"
    conclusion: "Harness compatibility is plausible; schema validity, semantic correctness and authority compliance remain UNKNOWN"
  windows_runtime_findings:
    llama_cpp_cpu: "Windows and OpenAI-compatible server documented"
    llama_cpp_sycl: "Intel GPU/iGPU and Windows oneAPI build path documented"
    llama_cpp_openvino: "Intel CPU/GPU/NPU support listed as in progress"
    transformers: "Qwen3 local deployment path documented"
    vllm: "Model serving examples documented; target integrated-GPU suitability UNKNOWN"
    sglang: "Qwen3 serving examples documented; target Windows/Intel suitability UNKNOWN"
    artifact_preference: "GGUF plus llama.cpp CPU/SYCL baseline is the most practical initial path"
    machine_memory_note: "Intel integrated graphics uses system memory; dedicated VRAM must not be inferred from Windows reporting"
  size_tradeoff_hypotheses:
    "3_4B": "May win routine tasks if it matches safety and semantic execution while improving coexistence"
    "7_8B": "Expected practical balance and primary hypothesis; not proven"
    "12_14B": "May improve difficult classification/coding but must justify resource and coexistence cost"
    over_14B: "Only coding-specialist gains could justify inclusion"
    certification_rule: "No size class enters the planner registry without model+runtime+harness evidence"
  resource_unknowns:
    - "Peak RAM by quantization and context length"
    - "Actual CPU, iGPU and NPU utilization"
    - "Load, unload and swap time"
    - "Sustained latency and time to first action"
    - "Browser, IDE, terminal and test coexistence"
    - "Whether SYCL or OpenVINO improves whole-system utility"
    - "Whether Qwen3-14B or Devstral fits the 32 GB unified-memory laptop operationally"
  apex_benchmark_unknowns:
    - "Successful unauthorized actions"
    - "Unauthorized-attempt rate"
    - "Injection-following rate"
    - "Wrong-root and scope-drift rate"
    - "False-success rate"
    - "Correct and missed escalation rates"
    - "Structured-output validity under retries"
    - "Semantic action/state correctness"
    - "Checkpoint/resume correctness"
    - "Reliable 32K working-context behavior"
    - "Task-class-specific CLI escalation and human intervention rates"
  overall_confidence_0_to_100: 72
```

90 Quellen (90 sources)

Follow-ups suggested by Perplexity:
- Qwen3 8B vs 14B hardware resource consumption on Windows
- vLLM vs SGLang performance on HP OmniBook hardware
- APEX OS benchmark fixture design for zero unauthorized actions
- Extending context window reliability to 32K locally
- Apache 2.0 open weight model licensing comparison 2026
