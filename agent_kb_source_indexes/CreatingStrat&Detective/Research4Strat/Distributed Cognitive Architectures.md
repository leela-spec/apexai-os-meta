The evolution of agentic workflows has moved past "chatting with a bot" into the realm of **Distributed Cognitive Architectures**. By treating agents as components of a Viable System Model (VSM), we move from simple automation to autonomous strategy and refinement.

Here is the research breakdown for high-functioning agentic workflows.

---

## 1. Generic Workflow Patterns

Modern agentic design relies on a tiered approach to reasoning, moving from raw data to strategic execution.

- **The PECR Loop (Plan → Execute → Critique → Refine):** This is the fundamental unit of agentic self-correction. Instead of a single-shot prompt, the agent generates a draft, a "Critic" agent identifies hallucinations or logic gaps, and the "Executor" iterates.

- **HMAS Decomposition:** To manage complexity, tasks are broken down into:

    - **Macro (System):** The overarching objective (e.g., "Build a market entry strategy").

    - **Meso (Interaction):** How agents collaborate (e.g., the handoff between a researcher and a writer).

    - **Micro (Individual):** The specific prompt engineering and tool-use logic of a single agent.

- **Medallion Knowledge Layering:**

    - **Bronze:** Raw context, web scrapes, and unverified data.

    - **Silver:** Synthesized summaries, cross-referenced facts, and "cleaned" reasoning.

    - **Gold:** Final strategic recommendations, verified and ready for System 5 (Policy) approval.


---

## 2. Role Boundaries (VSM & SOPs)

To prevent agents from stepping on each other's toes, we use **MetaGPT-style SOPs** and **Viable System Model (VSM)** levels.

|**VSM Level**|**Agent Role**|**Responsibility**|**Boundary**|
|---|---|---|---|
|**System 5 (Policy)**|The Identity Agent|Defines the "Why" and final "Go/No-Go."|Cannot execute code; only judges alignment.|
|**System 4 (Strategy)**|The Intelligence Agent|Scans the environment; "What" should we do next?|Limited to planning and simulation.|
|**System 3 (Ops Control)**|The Manager Agent|Optimizes resources and "How" tasks are assigned.|Manages the "Specialists."|
|**System 1 & 2 (Ops)**|The Bounded Specialists|Tactical execution (Coding, Research, Writing).|Strictly restricted to a specific toolset.|

---

## 3. Strategy vs. Ops vs. Detective Split

The "Detective" is the missing link in most basic workflows. This split ensures that the person doing the work isn't the one grading it.

- **Strategy (The Architect):** Uses **System 4** logic to look at future states. It maps out dependencies and sets the KPIs for a "successful" run.

- **Ops (The Builder):** Follows the **MetaGPT SOPs**. It is optimized for speed, token efficiency, and tool-call accuracy.

- **Detective (The Critic):** Acts as the auditor. It uses **Red-Teaming** prompts to find flaws in the Ops agent's output. It doesn't fix the problem; it merely points it out.


---

## 4. Promotion Criteria: Function vs. Agent

Not every task needs a "thinking" agent. Over-engineering leads to high latency and "agentic drift."

- **When to use a Function (Deterministic):**

    - Formatting JSON.

    - Calculating mathematical formulas.

    - Running a specific API call with known parameters.

    - _Rule:_ If the "Review" can be done via Regex or Schema validation, it’s a function.

- **When to promote to an Agent (Probabilistic):**

    - **Ambiguity:** The critique requires understanding tone, nuance, or "spirit of the law."

    - **Open-Ended Refinement:** The "Refine" step requires creative synthesis that a script cannot provide.

    - **Bounded Specialist Invocation:** When the system must decide _which_ tool to use based on intermediate results.


---

## 5. Template for Strategy-Agent Handoff

When a Strategy Agent (System 4) hands a task to an Ops Agent (System 1), it should use a structured **Mission Briefing** to minimize drift.

> **### Mission Briefing: [Task Name]**
>
> **1. Objective:** Clear statement of the desired "Gold" state.
>
> **2. Constraints:** (Budget, Token limit, "Do Not" list).
>
> **3. Contextual Layer:** Link to "Silver" data (the synthesized research).
>
> **4. Success Heuristics:** What will the **Detective Agent** be looking for?
>
> **5. Termination Trigger:** Under what condition should the agent stop and ask for human intervention?

---

## 6. Anti-Sprawl Rules

To keep your agentic ecosystem from becoming an expensive, self-perpetuating mess, follow these constraints:

1. **The Rule of Three:** No workflow should exceed three recursive "Refine" loops without a "System 5" (Human or Policy Agent) interrupt.

2. **Stateless Execution:** Agents should not "remember" past runs unless explicitly passed a summary in the "Medallion" Silver layer. This prevents "hallucination debt."

3. **Strict Tool Shadowing:** An agent can only invoke tools explicitly granted in its "Bounded Specialist" profile. If it needs a new tool, it must request a "Promotion" from the Manager Agent.

4. **Token Budgeting:** Every "Macro" task has a hard cost ceiling. If the PECR cycle consumes 80% of the budget without reaching "Gold" status, the process halts.