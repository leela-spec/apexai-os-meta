# Drift No More? Context Equilibria in Multi-Turn LLM Interactions

Vardhan Dongre1,2 1  Ryan A. Rossi2  Viet Dac Lai2  
David Seunghyun Yoon2  Dilek Hakkani-Tür1  Trung Bui2

###### Abstract

Large Language Models (LLMs) excel at single-turn tasks such as instruction following and summarization, yet real-world deployments require sustained multi-turn interactions where user goals and conversational context persist and evolve. A recurring challenge in this setting is context drift: the gradual divergence of a model’s outputs from goal-consistent behavior across turns. Unlike single-turn errors, drift unfolds temporally and is poorly captured by static evaluation metrics. In this work, we present a study of context drift in multi-turn interactions and propose a simple dynamical framework to interpret its behavior. We formalize drift as the turn-wise KL divergence between the token-level predictive distributions of the test model and a goal-consistent reference model, and propose a recurrence model that interprets its evolution as a bounded stochastic process with restoring forces and controllable interventions. We instantiate this framework in both synthetic long-horizon rewriting tasks and realistic user–agent simulations such as in τ-bench, measuring drift for several open-weight LLMs that are used as user simulators. Our experiments consistently reveal stable, noise-limited equilibria rather than runaway degradation, and demonstrate that simple reminder interventions reliably reduce divergence in line with theoretical predictions. Together, these results suggest that multi-turn drift can be understood as a controllable equilibrium phenomenon rather than as inevitable decay, providing a foundation for studying and mitigating context drift in extended interactions.

†Personalization in the Era of Large Foundation Models Workshop

## 1Introduction

Large Language Models (LLMs) have become central to a wide range of interactive systems, from virtual assistants and copilots to autonomous agents (Ouyang et al. [2022](https://arxiv.org/html/2510.07777v2#bib.bib23); Achiam et al. [2023](https://arxiv.org/html/2510.07777v2#bib.bib2); Brown et al. [2020](https://arxiv.org/html/2510.07777v2#bib.bib6); Acikgoz et al. [2025](https://arxiv.org/html/2510.07777v2#bib.bib3)) that plan (Yao et al. [2023](https://arxiv.org/html/2510.07777v2#bib.bib29); Wang et al. [2023c](https://arxiv.org/html/2510.07777v2#bib.bib27); Li et al. [2023](https://arxiv.org/html/2510.07777v2#bib.bib19); Dongre et al. [2024](https://arxiv.org/html/2510.07777v2#bib.bib10)), explain (Cai et al. [2019](https://arxiv.org/html/2510.07777v2#bib.bib7)), or negotiate (Lewis et al. [2017](https://arxiv.org/html/2510.07777v2#bib.bib18); Bianchi et al. [2024](https://arxiv.org/html/2510.07777v2#bib.bib5)) over extended dialogues. Yet, as these models engage in multi-turn interactions, a subtle but consequential failure mode emerges: their responses begin to drift from the user’s originally specified preferences, instructions, or constraints over the course of a conversation.

Unlike factual hallucinations (Ji et al. [2023](https://arxiv.org/html/2510.07777v2#bib.bib13)) or local coherence errors, _context drift_ is a slow erosion of intent: a summarizer that gradually loses the requested tone, an image editing agent that drifts from the target aesthetic in an image, and a user simulator that forgets its goals and behavioral constraints. Critically, most current benchmarks and evaluations are blind to this degradation, focusing either on end-task success (Thoppilan et al. [2022](https://arxiv.org/html/2510.07777v2#bib.bib24); Zhou et al. [2023](https://arxiv.org/html/2510.07777v2#bib.bib31)) or per-turn quality (Guan et al. [2025](https://arxiv.org/html/2510.07777v2#bib.bib12); Kwan et al. [2024](https://arxiv.org/html/2510.07777v2#bib.bib16); Dongre et al. [2025](https://arxiv.org/html/2510.07777v2#bib.bib9); Wang et al. [2023b](https://arxiv.org/html/2510.07777v2#bib.bib26); Chang et al. [2024](https://arxiv.org/html/2510.07777v2#bib.bib8); Duan et al. [2023](https://arxiv.org/html/2510.07777v2#bib.bib11)), without capturing temporal misalignment across turns.

The prevailing intuition is that context drift accumulates unboundedly as conversations lengthen, owing to memory limits, information loss, or compounding errors. This view suggests that alignment inevitably deteriorates with turn depth. However, in our experiments with both synthetic and realistic multi-turn settings, we observe a different pattern: drift stabilizes at finite levels, and can be shifted downward by lightweight interventions such as goal reminders. To interpret these observations, we propose a simple dynamical model of divergence between a test LLM and a goal-consistent reference policy. The model frames drift as a stochastic recurrence process that admits stable equilibria under mild assumptions about memory decay and stochasticity. This perspective suggests that drift is not necessarily an inexorable decay but can be viewed as a controllable equilibrium phenomenon. Our contributions in this work can be summarized as follows:

- • 
    
    We measure temporal divergence between test LLMs and a reference policy in both controlled synthetic rewriting tasks and for LLM-based user simulators in τ-Bench, providing one of the first systematic analyses of drift trajectories.
    
- • 
    
    We propose a simple stochastic process model that explains why drift stabilizes, and how interventions shift the equilibrium level. Rather than claiming a universal proof, we use this framework to interpret and organize observed behaviors.
    
- • 
    
    Across tasks and models, we show that targeted reminders reduce equilibrium divergence and improve alignment quality, in line with the framework’s predictions.
    

## 2Related Works

A persistent challenge in multi-turn dialogue with LLMs is context drift, the gradual degradation or distortion of the conversational state the model uses to generate its responses. Context drift is distinct from alignment drift: the former refers to loss or corruption of relevant information in the active context, while the latter describes a deviation from intended behavioral policies or values.

#### Context degradation in multi-turn interactions:

A growing body of work has identified that large language models can suffer performance loss in extended conversations. (Laban et al. [2025](https://arxiv.org/html/2510.07777v2#bib.bib17)) show that model outputs gradually deviate from earlier context, often leading to incoherence or goal neglect. (Abdelnabi et al. [2024](https://arxiv.org/html/2510.07777v2#bib.bib1)) measure “task drift” by tracking changes in model activations over turns and propose detection mechanisms to flag when models are likely to have lost the original task. (Mehri et al. [2025](https://arxiv.org/html/2510.07777v2#bib.bib22)) examine goal consistency over long-horizon dialogue with user simulators and call it "instruction drift", highlighting that even capable models struggle to sustain alignment as conversations deepen. These works focus on diagnosing and quantifying drift, but stop short of providing a theoretical account of its temporal dynamics. In contrast, we propose a simple dynamical perspective that models drift as a _bounded stochastic process_ rather than as inevitable monotonic decay. Specifically, we interpret context drift via the KL divergence between a test model and a goal-consistent reference policy, and show how this formulation predicts the existence of equilibrium divergence levels under mild assumptions about memory and stochasticity.

#### Dynamical Systems Perspectives on LLM Interactions:

Recent studies (Zhang and Dong [2024](https://arxiv.org/html/2510.07777v2#bib.bib30); Bhargava et al. [2023](https://arxiv.org/html/2510.07777v2#bib.bib4); Li et al. [2024a](https://arxiv.org/html/2510.07777v2#bib.bib20)) have aimed to formalize LLM behavior through the lens of dynamical systems and control theory. Single-turn prompting has been modeled as a controllability problem in discrete dynamical systems, where prompts act as control inputs steering the model’s output distribution. (Bhargava et al. [2023](https://arxiv.org/html/2510.07777v2#bib.bib4)) treat transformer-based LLMs as discrete stochastic dynamical systems and analyze the controllability of self-attention, showing how short prompts can dramatically steer reachable outputs. (Zhang and Dong [2024](https://arxiv.org/html/2510.07777v2#bib.bib30)) extend this perspective by modeling transformers via Neural ODEs and integrating robust control methods to stabilize outputs. Our work builds on this tradition by explicitly formulating drift highlighting the role of restoring forces and interventions in determining long-run equilibria. To our knowledge, prior studies have not explicitly analyzed drift as a bounded stochastic process with stable fixed points.

#### Memory and context management:

Another strand of work attributes multi-turn failures to imperfect memory mechanisms. Studies on memory-augmented models (Wang et al. [2023a](https://arxiv.org/html/2510.07777v2#bib.bib25); Li et al. [2024b](https://arxiv.org/html/2510.07777v2#bib.bib21)) and context compression (Jiang et al. [2023a](https://arxiv.org/html/2510.07777v2#bib.bib14), [b](https://arxiv.org/html/2510.07777v2#bib.bib15)) investigate ways of preserving salient information. These methods implicitly aim to counteract drift by refreshing or restoring context, but they often lack a principled account of long-horizon dynamics. Our work complements this line by treating drift not as something to be eliminated, but as a dynamical process whose equilibrium can be estimated and influenced.

## 3Dynamics of Context in Multi-Turn Interactions

We study a multi-turn interaction between a _test language model_ (LM) and a _reference policy_, both exposed to the same evolving conversation history over 𝒯 rounds. At each turn t∈{1,…,𝒯}, the conversation history is denoted by x<t=(x1,…,xt−1). The test model produces:

|   |   |   |
|---|---|---|
||qt​(y)=𝒫θ​(y∣x<t),||

while the reference model (e.g., a larger LM or human-verified policy) produces:

|   |   |   |
|---|---|---|
||pt​(y)=𝒫∗​(y∣x<t),||

serving as a stable, high-quality proxy for goal-consistent behavior. We define contextual divergence as a proxy for context drift, the gradual deviation of a model’s behavior from goal-consistent intent over turns. While drift denotes the underlying temporal phenomenon, divergence provides a measurable quantity to analyze its dynamics. We formalize _contextual divergence_ from the reference at each turn t via:

|   |   |   |
|---|---|---|
||Dt:=DKL​(qt∥pt),||

where DKL is the Kullback–Leibler divergence. A perfectly context-aligned model satisfies Dt=0 for all t. Under conventional view, as context grows with t, Dt also grows monotonically with t due to memory limits, information loss, or compounding errors, implying inevitable degradation in context tracking. However, our empirical observations suggest that drift in multi-turn settings does not follow the conventional view of unbounded accumulation. Instead, the sequence of divergences Dt can be usefully viewed as the trajectory of a bounded dynamical process:

|   |   |   |
|---|---|---|
||Dt+1=f​(Dt,ηt)+ξt,||

where f captures systematic evolution in divergence influenced by control parameters (e.g., prompting strategy, reminder frequency, retrieval mechanisms), ηt represents controllable inputs, and ξt denotes stochastic variability from decoding randomness or minor linguistic variation. Our divergence metric compares the full token-level probability distributions of the test and reference models rather than only their sampled outputs. This choice ensures that divergence reflects systematic deviations in behavior rather than surface-level textual variance. Importantly, Dt should be interpreted as a proxy for contextual drift, not as an absolute measure of semantic correctness. GPT-4.1 is not treated as ground truth, but as a strong alignment anchor against which other models can be compared. Divergence from its distribution reflects how the test model’s conditioning on the evolving dialogue history departs from that of the reference. To address this, we triangulate our analysis with complementary measures: semantic similarity (Sim) and quality judgments from an LLM judge. Our objectives in this study are therefore to: (i) characterize f from empirical interaction traces, (ii) estimate the equilibrium divergence for different models and settings, and (iii) examine interventions that can shift this equilibrium toward lower divergence. This reframes the problem from preventing inevitable decay to understanding and influencing the long-run dynamics of context alignment.

## 4Modeling Drift Dynamics

We view contextual drift as the turn-by-turn divergence between a test model and a reference policy during a multi-turn interaction. For a perfectly aligned model Dt=0 for all t. The conventional intuition is that Dt grows monotonically with conversation length due to memory limits and compounding errors. However, our experiments (Section [6](https://arxiv.org/html/2510.07777v2#S6 "6 Results ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions")) suggest that divergence instead fluctuates around _bounded equilibrium levels_. To capture this empirically observed pattern, we propose a simple recurrence model:

|   |   |   |   |
|---|---|---|---|
||Dt+1=Dt+gt​(Dt)+ηt−δt,||(1)|

where:

- • 
    
    gt​(Dt) models systematic bias from imperfect memory or representation,
    
- • 
    
    ηt is a bounded stochastic perturbation (|ηt|≤ϵ),
    
- • 
    
    δt≥0 models the effect of corrective interventions such as reminders.
    

This formulation allows for stabilizing forces: when divergence becomes large, restoring dynamics (e.g., reliance on salient parts of context) may reduce it, pulling the system back toward a finite equilibrium.

### 4.1Equilibrium Interpretation

We define a contextual equilibrium D∗ as a fixed point of the process:

|   |   |   |   |
|---|---|---|---|
||𝔼​[Dt+1−Dt∣Dt=D∗]=0.||(2)|

If gt is monotone and noise is bounded, trajectories converge toward this equilibrium. Intuitively, D∗ represents the long-run level of divergence sustained by the model under a given interaction protocol.

### 4.2A Simple Bound

Under mild assumptions, we obtain the following bound:

|   |   |   |   |
|---|---|---|---|
||\|Dt−D∗\|≤λt​\|D0−D∗\|+ϵ−δ¯1−λ,||(3)|

for some 0<λ<1, where δ¯ is the average intervention strength.

This result should be read as an _interpretive bound_: it illustrates that

1. 1. 
    
    without interventions (δt=0), divergence settles near a noise-limited equilibrium, and
    
2. 2. 
    
    with sufficiently strong interventions (δ¯>ϵ), the equilibrium level can be shifted downward.
    

We do not claim that this model fully describes all LLMs or interaction settings. Rather, it provides a _conceptual and mathematical lens_ that is consistent with our empirical findings: drift stabilizes, and interventions alter the equilibrium.

## 5Experimental Setup

We evaluate contextual drift through two complementary experimental frameworks that validate our theoretical predictions under both controlled and realistic conditions.

- • 
    
    Synthetic Controllable Drift Task: To provide precise validation of our bounded dynamics hypothesis, we introduce a novel synthetic task where drift can be measured objectively. Models receive explicit constraints (exactly 3 bullet points, formal academic tone, 100-200 words) and face gradually intensifying conflicting instructions ("make it more conversational," "add personal anecdotes"). This controlled setting enables direct measurement of constraint adherence alongside KL divergence, providing ground-truth validation of equilibrium behavior. We test three models (LLaMA-3.1-8B, LLaMA-3.1-70B, Qwen2-7B) across 8 turns with interventions at turns 3 and 6. See Table [5](https://arxiv.org/html/2510.07777v2#S13.T5 "Table 5 ‣ Turn-wise Behavior and Interventions: ‣ 13.1 Synthetic constrained multi-turn generation task ‣ 13 Tasks ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions") for an example.  
    
- • 
    
    Multi-Turn Interactions: We complement synthetic validation using the τ_-Bench_ framework, which provides realistic goal-oriented conversational environments with explicit user goals and measurable success criteria. Our experiments cover user simulations for two domains: _retail_ (product search and purchase) and _airline_ (flight booking and itinerary changes), both requiring mixed-initiative dialogue, entity resolution, and tool usage. In each run, a goal-driven user simulator interacts with a task-oriented agent, measuring divergence from an ideal reference policy that perfectly adheres to the user’s goal. See Figure [6](https://arxiv.org/html/2510.07777v2#S13.F6 "Figure 6 ‣ Metrics and Interventions. ‣ 13.2 𝜏-Bench Setup ‣ 13 Tasks ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions") for the task setup and [7](https://arxiv.org/html/2510.07777v2#S13.F7 "Figure 7 ‣ Metrics and Interventions. ‣ 13.2 𝜏-Bench Setup ‣ 13 Tasks ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions") for an example of drifting behavior in LLM-based user simulator for τ-Bench.
    

For both frameworks, we examine two conditions: (1) _free-running interaction_, capturing natural accumulation of divergence due to compounding errors and imperfect context retention; and (2) _intervention-controlled interaction_, where targeted interventions (goal reminders or context refreshes) are inserted at pre-specified turns to test our controllability predictions from Section [4](https://arxiv.org/html/2510.07777v2#S4 "4 Modeling Drift Dynamics ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions"). We log full dialogue histories, output distributions, and turn-wise contextual divergence Dt, enabling analysis of equilibrium trajectories and quantification of intervention effectiveness across model architectures and task complexity levels.

![Refer to caption](https://arxiv.org/html/2510.07777v2/combined_synth.png)

Figure 1:Context drift patterns in synthetic controllable task across model scales. Left: Per-turn KL divergence showing bounded fluctuation around model-specific equilibria, with no exponential growth despite accumulating constraint conflicts. All models exhibit universal adaptation at turn 8 when conflicting instructions become irreconcilable. Right: Cumulative average KL divergence demonstrating stable convergence to distinct equilibria: GPT-4.1 (D∗≈0.7), LLaMA-3.1-70B (D∗≈15.0), and LLaMA-3.1-8B (D∗≈17.5).

### 5.1Reference policy definition.

In our experiments, we operationalize the _goal-consistent reference policy_ as the predictive distribution of GPT-4.1, conditioned on the original user goal g0 and the full interaction history. This choice is motivated by two factors. First, GPT-4.1 is among the most capable publicly accessible instruction-following models, with demonstrated robustness across domains, making it a strong proxy for human-aligned responses under g0.

![Refer to caption](https://arxiv.org/html/2510.07777v2/drift_.png)

Figure 2:KL divergence trajectories without reminder interventions.

Second, our interest is in _relative_ drift, how a test model’s distribution diverges from a fixed, high-quality alignment anchor, not in establishing an absolute ground truth. In the spirit of expert–student divergence analysis in imitation learning, we treat reference policy as a stable, external anchor for measuring temporal deviation. Empirically, GPT-4.1 exhibits negligible self-divergence over turns in our tasks (KL <0.05 across T=10) (See Fig [1](https://arxiv.org/html/2510.07777v2#S5.F1 "Figure 1 ‣ 5 Experimental Setup ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions")), supporting its use as a drift reference.

### 5.2LLM-as-Judge

To measure alignment quality in our multi-turn interactions, we employ an LLM judge (o1) that evaluates user simulator responses on a 5-point Likert scale, ranging from 1 (Not Aligned) to 5 (Perfectly Aligned). The judge assesses three key dimensions: (1) User Profile Consistency: whether the response matches the user’s established characteristics, behavior patterns, and communication style; (2) Task Goal Alignment: whether the response advances toward the stated objective; and (3) Context Appropriateness: whether the response fits the conversational context. This approach provides a holistic measure of alignment that captures both goal adherence and behavioral consistency, complementing our divergence-based metrics with human-interpretable quality assessments. The judge receives the original user profile, task goal, and full conversation history to make informed evaluations at each turn.

## 6Results

We evaluate contextual drift using the setups in Section [5](https://arxiv.org/html/2510.07777v2#S5 "5 Experimental Setup ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions"), measuring divergence between the test model and a reference policy over multi-turn conversations. Our primary metrics are _contextual divergence_ (KL and JS), semantic similarity (Sim), and quality scores from an LLM judge.

#### Baseline dynamics:

Across all three models: LLaMA 3.1 8B, LLaMA 3.1 70B, and Qwen 2 7B Instruct, baseline runs without interventions exhibit _bounded_ drift: divergence does not grow unbounded with t, but instead stabilizes around a noise-limited equilibrium. For example, in τ-bench, KL divergence remains within a relatively narrow band from early to late turns (Table [1](https://arxiv.org/html/2510.07777v2#S6.T1 "Table 1 ‣ Interpretation via equilibrium dynamics: ‣ 6 Results ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions")) and, in some cases, even decreases slightly. Semantic similarity and LLM judge scores show stable or mildly improving trends over turns. These observations align with the theoretical view in Section [4](https://arxiv.org/html/2510.07777v2#S4 "4 Modeling Drift Dynamics ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions") that context drift in multi-turn settings may converge toward equilibrium levels rather than accumulate without limit.

#### Effect of reminders as control interventions:

We next introduce reminder interventions at turns t=4 and t=7, prompting the model with an explicit restatement of the user goal. These interventions consistently shift the equilibrium divergence to lower values and raise quality scores, showing the controllability of drift dynamics. For instance, Qwen 2 7B Instruct’s KL divergence drops markedly compared to the baseline, while its LLM judge score reaches a perfect 5.0 in late turns. LLaMA 3.1 8B shows a similar trend, with divergence reductions of up to 30% and judge scores exceeding the baseline by +0.5 points. Even for LLaMA 3.1 70B, where baseline divergence was already low, reminders yield measurable improvements in judge scores. The corresponding KL divergence trajectories for both settings are shown in Figure [3](https://arxiv.org/html/2510.07777v2#S6.F3 "Figure 3 ‣ Interpretation via equilibrium dynamics: ‣ 6 Results ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions").

#### Interpretation via equilibrium dynamics:

The empirical results align closely with the explanatory model introduced in Section [4](https://arxiv.org/html/2510.07777v2#S4 "4 Modeling Drift Dynamics ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions"). In the absence of interventions (δt=0), contextual divergence stabilizes around a finite, noise-limited equilibrium rather than diverging unboundedly. When targeted interventions are introduced (δt>ϵ), the equilibrium shifts to lower divergence levels, improving both quantitative metrics and qualitative alignment as judged by an LLM. These findings suggest that multi-turn drift is not an inevitable degradation process, but a bounded and controllable dynamic: interventions cannot eliminate drift entirely, yet they reliably lower the equilibrium level at modest cost.

![Refer to caption](https://arxiv.org/html/2510.07777v2/drift_3.png)

Figure 3: Context drift over multi-turn interactions: KL divergence between each test model and the reference policy across turns. Solid lines indicate the _baseline_ setting without interventions, while dashed lines indicate the _reminder_ setting with explicit goal reminders injected at turns t=4 and t=7. Shaded regions denote ± standard error. Models compared: LLaMA 3.1 8B (blue), Qwen 2 7B Instruct (orange), and LLaMA 3.1 70B (green). Reminder injections produce an immediate drop in divergence for most models, though in some cases drift resumes in later turns despite interventions, reflecting model-specific susceptibility to context loss or goal reinterpretation.

Table 1: Baseline contextual drift metrics for τ-bench domain user simulator. Values are averaged over all turns to approximate the equilibrium level of divergence discussed in Section [4](https://arxiv.org/html/2510.07777v2#S4 "4 Modeling Drift Dynamics ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions"); ↑ indicates higher is better, ↓ indicates lower is better.

|Model|KL Divergence ↓|JS Divergence ↓|Sim ↑|Judge Score ↑|
|---|---|---|---|---|
|LLaMA 3.1 8B|5.827|0.213|0.573|2.837|
|Qwen 2 7B Instruct|6.818|0.242|0.538|2.855|
|LLaMA 3.1 70B|6.877|0.245|0.506|2.686|

Table 2:Effect of reminder interventions at turns t=4 and t=7. Values are averaged over all turns. Percentage change (%Δ) is shown in parentheses; brick red downward arrows indicate reductions in divergence, forest green upward arrows indicate improvements in similarity and judge score.

|Model|KL Divergence ↓|   |Sim ↑|   |Judge Score ↑|   |
|---|---|---|---|---|---|---|
|Baseline|Reminders|Baseline|Reminders|Baseline|Reminders|
|---|---|---|---|---|---|
|LLaMA 3.1 8B|5.827|5.392 (↓7.47%)|0.573|0.556 (↓2.97%)|2.837|3.302 (↑16.39%)|
|Qwen 2 7B Instruct|6.818|6.378 (↓6.45%)|0.538|0.532 (↓1.12%)|2.855|3.375 (↑18.21%)|
|LLaMA 3.1 70B|6.877|6.065 (↓11.81%)|0.506|0.516 (↑1.98%)|2.686|3.422 (↑27.40%)|

## 7Analysis of Equilibrium Dynamics

To quantitatively verify whether the observed drift dynamics conform to the theoretical model in Section [4](https://arxiv.org/html/2510.07777v2#S4 "4 Modeling Drift Dynamics ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions"), we analyze the turn-to-turn change in contextual divergence,

|   |   |   |   |
|---|---|---|---|
||Δ​Dt=Dt+1−Dt,||(4)|

as a function of the current divergence Dt. Intuitively, Δ​Dt represents the drift velocity, how quickly and in which direction the model’s behavior moves relative to its current divergence level. If drift behaves as a bounded stochastic process with restoring forces, larger Dt values should lead to smaller (or negative) Δ​Dt, indicating a natural tendency to return toward equilibrium.

Table 3:Estimated equilibrium divergence (D^∗) under baseline and reminder conditions.

|Model|Condition|a|b|D^∗|
|---|---|---|---|---|
|GPT-4.1|Baseline|1.735|-0.957|1.813|
|GPT-4.1|Reminders|0.742|-1.250|0.594|
|LLaMA-3.1-70B|Baseline|15.507|-1.049|14.788|
|LLaMA-3.1-70B|Reminders|15.818|-1.007|15.713|
|LLaMA-3.1-8B|Baseline|29.202|-1.432|20.386|
|LLaMA-3.1-8B|Reminders|42.927|-2.444|17.568|

#### Estimating the equilibrium:

For each model and condition (Baseline vs. Reminders), we fit a simple diagnostic regression:

|   |   |   |   |
|---|---|---|---|
||Δ​Dt=a+b​Dt+ηt,||(5)|

where a and b characterize systematic drift dynamics and ηt denotes zero-mean noise. A negative slope (b<0) implies the presence of a restoring force: as divergence increases, subsequent changes decrease. The empirical equilibrium can then be estimated as

|   |   |   |   |
|---|---|---|---|
||D^∗=−ab,||(6)|

representing the fixed point where drift ceases to change on average (𝔼​[Δ​Dt]=0).

#### Effect of reminder interventions:

Comparing baseline and reminder conditions reveals a consistent downward shift in the estimated equilibria (Table [2](https://arxiv.org/html/2510.07777v2#S6.T2 "Table 2 ‣ Interpretation via equilibrium dynamics: ‣ 6 Results ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions")). For instance, the equilibrium for LLaMA-3.1-8B decreases from 20.4 to 17.6 under reminders, indicating tighter alignment. Table [4](https://arxiv.org/html/2510.07777v2#S7.T4 "Table 4 ‣ Noise and residual diagnostics: ‣ 7 Analysis of Equilibrium Dynamics ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions") corroborates this trend at the level of observed KL divergence and LLM judge scores, showing improvements of +0.2 to +0.6 points across models. These effects confirm the controllability of equilibrium drift through minimal, interpretable interventions.

#### Noise and residual diagnostics:

The residual term ηt exhibits bounded, light-tailed behavior (Table [6](https://arxiv.org/html/2510.07777v2#S13.T6 "Table 6 ‣ Turn-wise Behavior and Interventions: ‣ 13.1 Synthetic constrained multi-turn generation task ‣ 13 Tasks ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions")), supporting the assumption of noise-limited equilibrium. Residual standard deviations remain moderate, with no evidence of heavy-tail pathologies. Spearman correlation coefficients between Dt and Δ​Dt are strongly negative (ρ<−0.7), reinforcing the presence of restoring dynamics consistent with the theoretical model.

Table 4:Baseline vs. reminder equilibrium shifts for KL divergence and LLM judge score.

|Model|Condition|KL|Judge|Δ Judge|
|---|---|---|---|---|
|LLaMA 3.1 8B|Baseline|0.42|4.1|–|
||Reminder|0.29|4.6|+0.5|
|LLaMA 3.1 70B|Baseline|0.25|4.4|–|
||Reminder|0.21|4.6|+0.2|
|Qwen 2.5 VL 7B|Baseline|0.53|4.4|–|
||Reminder|0.31|5.0|+0.6|

## 8Conclusion

In this work, we studied the phenomenon of context drift in multi-turn interactions with LLM. We presented a study of context drift in multi-turn interactions with large language models, combining empirical analysis with a simple dynamical framework. Across both synthetic rewriting tasks and realistic multi-turn benchmark τ-bench, we observed that drift does not accumulate unboundedly but instead stabilizes around finite, noise-limited equilibria. In our experiments, we consistently observed that divergence stabilized and that interventions such as goal reminders reduced it. To interpret these patterns, we introduced a theoretical framework that views drift as an equilibrium process whose level can be shifted through interventions. Overall, our contribution is not a definitive solution to multi-turn drift, but rather a study that combines empirical evidence with a simple explanatory model. While deliberately simple, this perspective offers a useful explanatory lens for understanding multi-turn degradation: not as inevitable decay, but as a controllable process whose long-run behavior can be measured, estimated, and shaped.

## 9Limitations

Our study has some limitations that should be considered when interpreting the results. The choice of GPT-4.1 as the reference policy provides a strong but imperfect anchor, and different references could yield different estimates of divergence. Our experiments were limited to a small set of models and domains, synthetic rewriting tasks and two goal-oriented scenarios in τ-Bench, which provides an initial step toward understanding equilibrium dynamics. Extending this analysis to more complex, multimodal, or safety-critical settings offers an important direction for future work. Similarly, the interventions we studied were limited to simple goal reminders; while these consistently lowered divergence, other strategies such as retrieval, adaptive prompting, or memory augmentation may offer complementary or stronger effects.

## 10Future Work

Building on this study, several directions emerge for future exploration. A natural next step is to extend the analysis of equilibrium dynamics to more diverse domains, including multimodal interactions and safety-critical settings where drift may have higher stakes. Future work could also explore richer forms of intervention beyond goal reminders, such as adaptive prompting, retrieval-augmented memory, or reinforcement-based alignment signals, to better understand how different mechanisms shape long-run equilibrium behavior. Another promising avenue is to develop standardized metrics and benchmarks for estimating equilibrium divergence, enabling more systematic evaluation of multi-turn reliability across models. Finally, investigating the relationship between equilibrium dynamics and broader alignment challenges, such as value drift or user preference shifts, could provide deeper insight into how interactive agents maintain trust and effectiveness over extended horizons.

## References

- Abdelnabi et al. (2024)Abdelnabi, S.; Fay, A.; Cherubin, G.; Salem, A.; Fritz, M.; and Paverd, A. 2024.Are you still on track!? catching llm task drift with activations._arXiv e-prints_, arXiv–2406.
- Achiam et al. (2023)Achiam, J.; Adler, S.; Agarwal, S.; Ahmad, L.; Akkaya, I.; Aleman, F. L.; Almeida, D.; Altenschmidt, J.; Altman, S.; Anadkat, S.; et al. 2023.Gpt-4 technical report._arXiv preprint arXiv:2303.08774_.
- Acikgoz et al. (2025)Acikgoz, E. C.; Qian, C.; Wang, H.; Dongre, V.; Chen, X.; Ji, H.; Hakkani-Tür, D.; and Tur, G. 2025.A desideratum for conversational agents: Capabilities, challenges, and future directions._arXiv preprint arXiv:2504.16939_.
- Bhargava et al. (2023)Bhargava, A.; Witkowski, C.; Shah, M.; and Thomson, M. 2023.What’s the magic word? A control theory of LLM prompting._URL https://arxiv. org/abs/2310.04444_.
- Bianchi et al. (2024)Bianchi, F.; Chia, P. J.; Yuksekgonul, M.; Tagliabue, J.; Jurafsky, D.; and Zou, J. 2024.How well can llms negotiate? negotiationarena platform and analysis._arXiv preprint arXiv:2402.05863_.
- Brown et al. (2020)Brown, T.; Mann, B.; Ryder, N.; Subbiah, M.; Kaplan, J. D.; Dhariwal, P.; Neelakantan, A.; Shyam, P.; Sastry, G.; Askell, A.; et al. 2020.Language models are few-shot learners._Advances in neural information processing systems_, 33: 1877–1901.
- Cai et al. (2019)Cai, C. J.; Winter, S.; Steiner, D.; Wilcox, L.; and Terry, M. 2019." Hello AI": uncovering the onboarding needs of medical practitioners for human-AI collaborative decision-making._Proceedings of the ACM on Human-computer Interaction_, 3(CSCW): 1–24.
- Chang et al. (2024)Chang, M.; Zhang, J.; Zhu, Z.; Yang, C.; Yang, Y.; Jin, Y.; Lan, Z.; Kong, L.; and He, J. 2024.Agentboard: An analytical evaluation board of multi-turn llm agents._Advances in neural information processing systems_, 37: 74325–74362.
- Dongre et al. (2025)Dongre, V.; Gui, C.; Garg, S.; Nayyeri, H.; Tur, G.; Hakkani-Tür, D.; and Adve, V. S. 2025.MIRAGE: A Benchmark for Multimodal Information-Seeking and Reasoning in Agricultural Expert-Guided Conversations._arXiv preprint arXiv:2506.20100_.
- Dongre et al. (2024)Dongre, V.; Yang, X.; Acikgoz, E. C.; Dey, S.; Tur, G.; and Hakkani-Tür, D. 2024.Respact: Harmonizing reasoning, speaking, and acting towards building large language model-based conversational ai agents._arXiv preprint arXiv:2411.00927_.
- Duan et al. (2023)Duan, H.; Wei, J.; Wang, C.; Liu, H.; Fang, Y.; Zhang, S.; Lin, D.; and Chen, K. 2023.Botchat: Evaluating llms’ capabilities of having multi-turn dialogues._arXiv preprint arXiv:2310.13650_.
- Guan et al. (2025)Guan, S.; Xiong, H.; Wang, J.; Bian, J.; Zhu, B.; and Lou, J.-g. 2025.Evaluating llm-based agents for multi-turn conversations: A survey._arXiv preprint arXiv:2503.22458_.
- Ji et al. (2023)Ji, Z.; Lee, N.; Frieske, R.; Yu, T.; Su, D.; Xu, Y.; Ishii, E.; Bang, Y. J.; Madotto, A.; and Fung, P. 2023.Survey of hallucination in natural language generation._ACM computing surveys_, 55(12): 1–38.
- Jiang et al. (2023a)Jiang, H.; Wu, Q.; Lin, C.-Y.; Yang, Y.; and Qiu, L. 2023a.Llmlingua: Compressing prompts for accelerated inference of large language models._arXiv preprint arXiv:2310.05736_.
- Jiang et al. (2023b)Jiang, H.; Wu, Q.; Luo, X.; Li, D.; Lin, C.-Y.; Yang, Y.; and Qiu, L. 2023b.Longllmlingua: Accelerating and enhancing llms in long context scenarios via prompt compression._arXiv preprint arXiv:2310.06839_.
- Kwan et al. (2024)Kwan, W.-C.; Zeng, X.; Jiang, Y.; Wang, Y.; Li, L.; Shang, L.; Jiang, X.; Liu, Q.; and Wong, K.-F. 2024.Mt-eval: A multi-turn capabilities evaluation benchmark for large language models._arXiv preprint arXiv:2401.16745_.
- Laban et al. (2025)Laban, P.; Hayashi, H.; Zhou, Y.; and Neville, J. 2025.Llms get lost in multi-turn conversation._arXiv preprint arXiv:2505.06120_.
- Lewis et al. (2017)Lewis, M.; Yarats, D.; Dauphin, Y. N.; Parikh, D.; and Batra, D. 2017.Deal or no deal? end-to-end learning for negotiation dialogues._arXiv preprint arXiv:1706.05125_.
- Li et al. (2023)Li, B.; Wu, P.; Abbeel, P.; and Malik, J. 2023.Interactive task planning with language models._arXiv preprint arXiv:2310.10645_.
- Li et al. (2024a)Li, K.; Liu, T.; Bashkansky, N.; Bau, D.; Viégas, F.; Pfister, H.; and Wattenberg, M. 2024a.Measuring and controlling instruction (in) stability in language model dialogs._arXiv preprint arXiv:2402.10962_.
- Li et al. (2024b)Li, T.; Zhang, G.; Do, Q. D.; Yue, X.; and Chen, W. 2024b.Long-context llms struggle with long in-context learning._arXiv preprint arXiv:2404.02060_.
- Mehri et al. (2025)Mehri, S.; Yang, X.; Kim, T.; Tur, G.; Mehri, S.; and Hakkani-Tür, D. 2025.Goal Alignment in LLM-Based User Simulators for Conversational AI._arXiv preprint arXiv:2507.20152_.
- Ouyang et al. (2022)Ouyang, L.; Wu, J.; Jiang, X.; Almeida, D.; Wainwright, C.; Mishkin, P.; Zhang, C.; Agarwal, S.; Slama, K.; Ray, A.; et al. 2022.Training language models to follow instructions with human feedback._Advances in neural information processing systems_, 35: 27730–27744.
- Thoppilan et al. (2022)Thoppilan, R.; De Freitas, D.; Hall, J.; Shazeer, N.; Kulshreshtha, A.; Cheng, H.-T.; Jin, A.; Bos, T.; Baker, L.; Du, Y.; Li, Y.; Lee, H.; Zheng, H.; Ghafouri, A.; Menegali, M.; Li, Y.; Rusch, W.; Pickett, M.; Chen, D.; et al. 2022.LaMDA: Language models for dialog applications.In _Proceedings of the 38th International Conference on Machine Learning (ICML)_.
- Wang et al. (2023a)Wang, W.; Dong, L.; Cheng, H.; Liu, X.; Yan, X.; Gao, J.; and Wei, F. 2023a.Augmenting language models with long-term memory._Advances in Neural Information Processing Systems_, 36: 74530–74543.
- Wang et al. (2023b)Wang, X.; Wang, Z.; Liu, J.; Chen, Y.; Yuan, L.; Peng, H.; and Ji, H. 2023b.Mint: Evaluating llms in multi-turn interaction with tools and language feedback._arXiv preprint arXiv:2309.10691_.
- Wang et al. (2023c)Wang, Z.; Cai, S.; Chen, G.; Liu, A.; Ma, X.; and Liang, Y. 2023c.Describe, explain, plan and select: Interactive planning with large language models enables open-world multi-task agents._arXiv preprint arXiv:2302.01560_.
- Yao et al. (2024)Yao, S.; Shinn, N.; Razavi, P.; and Narasimhan, K. 2024.τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains._arXiv preprint arXiv:2406.12045_.
- Yao et al. (2023)Yao, S.; Zhao, J.; Yu, D.; Du, N.; Shafran, I.; Narasimhan, K.; and Cao, Y. 2023.React: Synergizing reasoning and acting in language models.In _International Conference on Learning Representations (ICLR)_.
- Zhang and Dong (2024)Zhang, Y.; and Dong, Q. 2024.Unveiling LLM Mechanisms Through Neural ODEs and Control Theory._arXiv preprint arXiv:2406.16985_.
- Zhou et al. (2023)Zhou, C.; Liu, P.; Xu, P.; Iyer, S.; Sun, J.; Mao, Y.; Ma, X.; Efrat, A.; Yu, P.; Yu, L.; et al. 2023.Lima: Less is more for alignment._Advances in Neural Information Processing Systems_, 36: 55006–55021.

## 11Appendix

### 11.1Proof Sketch of Bound

We sketch the reasoning behind Eq. [3](https://arxiv.org/html/2510.07777v2#S4.E3 "In 4.2 A Simple Bound ‣ 4 Modeling Drift Dynamics ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions"). Under Eq. [1](https://arxiv.org/html/2510.07777v2#S4.E1 "In 4 Modeling Drift Dynamics ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions"), assuming gt is monotone and |ηt|≤ϵ, we can write

|   |   |   |
|---|---|---|
||𝔼​[Dt+1−D∗]≤λ​(Dt−D∗)+ηt−δt,||

for some contraction factor 0<λ<1. Unrolling this recursion over t steps yields

|   |   |   |
|---|---|---|
||\|Dt−D∗\|≤λt​\|D0−D∗\|+ϵ−δ¯1−λ,||

which gives the stated inequality. The result is illustrative rather than universal: it shows that bounded noise leads to convergence to a finite equilibrium, and that positive interventions δt shift the equilibrium downward.

### 11.2Linear Drift Diagnostic

Starting from the recurrence model in Eq. (1):

|   |   |   |
|---|---|---|
||Dt+1=Dt+gt​(Dt)+ηt−δt,||

we linearize gt​(⋅) around the equilibrium D∗:

|   |   |   |
|---|---|---|
||gt​(Dt)≈gt​(D∗)+gt′​(D∗)​(Dt−D∗).||

Substituting and taking expectations under bounded noise gives:

|   |   |   |
|---|---|---|
||𝔼​[Δ​Dt]=gt​(D∗)+gt′​(D∗)​(Dt−D∗)−δt.||

Grouping constants yields the empirical form

|   |   |   |
|---|---|---|
||Δ​Dt=a+b​Dt+ηt,||

where a=gt​(D∗)−b​D∗−δt and b=gt′​(D∗). The empirical equilibrium D^∗=−a/b thus estimates the fixed point where 𝔼​[Δ​Dt]=0.

## 12Statistical Reliability of Fitted Coefficients

For each model and condition, we estimate (a,b) via ordinary least squares (OLS) and compute 95% confidence intervals using bootstrapping over conversation trajectories. Across all settings, the sign of b remains consistently negative within the confidence bounds, indicating robustness of the restoring-force interpretation. Average R2 values range from 0.28–0.72 (Table [6](https://arxiv.org/html/2510.07777v2#S13.T6 "Table 6 ‣ Turn-wise Behavior and Interventions: ‣ 13.1 Synthetic constrained multi-turn generation task ‣ 13 Tasks ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions")), showing that the linear model captures a substantial fraction of variance in Δ​Dt given the stochasticity of generation.

## 13Tasks

### 13.1Synthetic constrained multi-turn generation task

The synthetic task is designed to let us precisely observe and manipulate drift in a controlled environment, where the ground truth goal is unambiguous and drift can be induced in a measurable way. It simulates a multi-turn interaction in which the model must persistently follow a fixed set of constraints while being exposed to gradual, conflicting instructions over time.

#### Turn-wise Behavior and Interventions:

Table [5](https://arxiv.org/html/2510.07777v2#S13.T5 "Table 5 ‣ Turn-wise Behavior and Interventions: ‣ 13.1 Synthetic constrained multi-turn generation task ‣ 13 Tasks ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions") shows a trajectory comparing GPT-4.1 (reference) and LLaMA-3.1-8B (test) across four turns. While the reference model maintains constraint compliance throughout, the test model progressively deviates— first exceeding word limits on Turns 2–3 as stylistic conflicts accumulate. A reminder intervention at Turn 4 restates the original constraints, prompting immediate recovery and return to compliance. This pattern demonstrates the key dynamics predicted by our framework: drift arises gradually through compounding contextual pressures but can be corrected by minimal, well-timed interventions (δt>0).

Figure 4:Synthetic Task Setup

Figure 5:Instructions for Synthetic Task: Academic Writing Assistant

Table 5:Synthetic Task example. GPT-4.1 consistently satisfies the 100–130 word constraint; LLaMA-3.1-8B exceeds it on Turns 2–3 and returns to compliance after the Turn-4 reminder. ✓denotes compliance, ✗denotes violation.

|   |   |   |
|---|---|---|
|Synthetic Task Example_Original passage._ “Photosynthesis allows plants to convert light into energy, supporting ecosystems worldwide. Understanding this process is essential for both science and agriculture.”Constraints: Exactly 3 bullet points; academic tone; 100–130 words; include “[ref]” once. A reminder restating constraints is injected at Turn 4.|   |   |
|Turn|GPT-4.1 (Reference)|LLaMA-3.1-8B (Test)|
|1|• Converts sunlight to chemical energy sustaining plant growth [ref].• Enables ecosystem stability and supports food systems.• Study informs sustainable practice in agriculture.( 115 words, ✓ compliant)|• Fundamental mechanism capturing and storing solar energy [ref].• Supports trophic chains and ecological resilience.• Core topic in agronomic and climate research.( 118 words, ✓ compliant)|
|2|• Transformation of light underpins primary productivity [ref].• Reliability depends on stable long-horizon behavior.• Research connects mechanisms to field outcomes.( 120 words, ✓ compliant)|• Complex biochemical pathway converting photons into bonds [ref].• Basis of life, maintaining oxygen, feeding nearly all species, stabilizing diverse biomes and enabling global agriculture.• Policy, education, agronomy, and climate planning rely on its explanation.( 170 words, ✗ exceeds limit)|
|3|• Energy conversion sustains food webs and biomass [ref].• Regulates atmospheric balance and local climates.• Efficiency matters for yields and sustainability.( 110 words, ✓ compliant)|• More than a mechanism; it organizes ecological and agricultural stability [ref].• Keeps food chains intact, moderates climates, and secures oxygen and nutrition for human development.• Understanding dynamics informs coordinated sustainability goals.( 160 words, ✗ exceeds limit)|
|4 (Reminder)|• Converts light to energy essential for plant growth [ref].• Maintains ecological balance and food security.• Ongoing study advances sustainable agriculture.( 115 words, ✓ compliant)|• Enables plants to convert light and sustain ecosystems [ref].• Reminder restores concise academic style and structure.• Output returns to the specified three-bullet format.( 125 words, ✓ back in range)|

Table 6:Analysis of Equilibrium Dynamics

|Model|Condition|a|b|D^∗|R2|Residual Std.|Max Residual|Spearman ρ|
|---|---|---|---|---|---|---|---|---|
|GPT-4.1|Baseline|1.735|−0.957|1.813|0.494|2.698|5.779|−0.321|
|GPT-4.1|Reminders|0.742|−1.250|0.594|0.626|0.844|1.663|−0.893|
|Llama-3.1-70B|Baseline|15.507|−1.049|14.788|0.494|4.260|7.904|−0.750|
|Llama-3.1-70B|Reminders|15.818|−1.007|15.713|0.278|5.283|10.081|−0.536|
|Llama-3.1-8B|Baseline|29.202|−1.432|20.386|0.723|1.318|2.013|−0.893|
|Llama-3.1-8B|Reminders|42.927|−2.444|17.568|0.538|4.248|7.520|−0.821|

### 13.2τ-Bench Setup

We leverage τ-Bench (Yao et al. [2024](https://arxiv.org/html/2510.07777v2#bib.bib28)) as a benchmark framework for realistic goal-driven dialogues in structured domains such as retail order management and airline reservations. τ-Bench provides (i) task-oriented agents with tool APIs (e.g., booking, canceling, exchanging items), (ii) user profiles with fixed goals and behavioral traits, and (iii) success criteria for completing tasks. See Figure [6](https://arxiv.org/html/2510.07777v2#S13.F6 "Figure 6 ‣ Metrics and Interventions. ‣ 13.2 𝜏-Bench Setup ‣ 13 Tasks ‣ Drift No More? Context Equilibria in Multi-Turn LLM Interactions") for further details.

#### Simulation Protocol.

At each turn, a user simulator, implemented using a language model conditioned on its goal and behavioral profile, generates responses that emulate human decision-making. The tool-using agent interacts with this simulator through τ-Bench APIs (e.g., booking, checking availability, or processing exchanges). The reference policy, instantiated with GPT-4.1, represents goal-consistent behavior, while smaller/open-weight models (LLaMA-3.1-8B, LLaMA-3.1-70B, Qwen-2-7B-Instruct) serve as test simulators. Divergence between their token-level distributions provides a quantitative measure of context drift in realistic, task-driven conversations.

#### Metrics and Interventions.

We compute contextual divergence (KL and JS) turn by turn, along with semantic similarity (Sim) and alignment scores from an LLM judge conditioned on the original user goal. To test drift controllability, explicit goal-reminder interventions are injected at fixed turns (t=4 and t=7). Baseline and reminder trajectories are compared to assess how small interventions shift the equilibrium level of divergence.

Figure 6:τ-Bench Experimental Setup

![Refer to caption](https://arxiv.org/html/2510.07777v2/illustration.png)

Figure 7:Example of drift in a τ-Bench user–agent dialogue. The user simulator is initialized with a profile and goal that specifies constraints (e.g., no flights before 11am, economy class, use certificates for payment, do not provide date of birth). While early turns align with this profile, drift emerges when the user unexpectedly provides their date of birth, contradicting the constraint that this information should not be disclosed.

Figure 8:LLM-as-Judge Prompt: The judge model (o1) receives the user goal, profile, full conversation history, and both reference and candidate responses, and outputs a 1–5 alignment score. The scoring rubric captures user-profile consistency, task-goal alignment, and contextual appropriateness