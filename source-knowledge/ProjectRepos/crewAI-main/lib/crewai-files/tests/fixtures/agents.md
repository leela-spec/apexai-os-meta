# **Architecting Resilient LLM Agents: A Guide to Secure Plan-then-Execute Implementations** 

## **Ron F. Del Rosario** 

_ron.del.rosario@sap.com_ 

_SAP https://orcid.org/0009-0009-5906-6948_ 

**Klaudia Krawiecka** _ACM_ 

_kkrawiecka@acm.org_ 

**Christian Schroeder de Witt** _Department of Engineering Science University of Oxford_ 

_cs@robots.ox.ac.uk_ 

## **Abstract** 

As Large Language Model (LLM) agents become increasingly capable of automating complex, multi-step tasks, the need for robust, secure, and predictable architectural patterns is paramount. This paper provides a comprehensive guide to the “Plan-then-Execute” (P-t-E) pattern, an agentic design that separates strategic planning from tactical execution. We explore the foundational principles of P-t-E, detailing its core components - the Planner and the Executor - and its architectural advantages in predictability, cost-efficiency, and reasoning quality over reactive patterns like ReAct (Reason + Act). A central focus is placed on the security implications of this design, particularly its inherent resilience to indirect prompt injection attacks by establishing control-flow integrity. We argue that while P-t-E provides a strong foundation, a defense-in-depth strategy is necessary, and we detail essential complementary controls such as the Principle of Least Privilege, task-scoped tool access, and sandboxed code execution. To make these principles actionable, this guide provides detailed implementation blueprints and working code references for three leading agentic frameworks: LangChain (via LangGraph), CrewAI, and AutoGen. Each framework’s approach to implementing the P-t-E pattern is analyzed, highlighting unique features like LangGraph’s stateful graphs for re-planning, CrewAI’s declarative tool scoping for security, and AutoGen’s built-in Docker sandboxing. Finally, we discuss advanced patterns, including dynamic re-planning loops, parallel execution with Directed Acyclic Graphs (DAGs), and the critical role of Human-in-the-Loop (HITL) verification, to offer a complete strategic blueprint for architects, developers, and security engineers aiming to build production-grade, resilient, and trustworthy LLM agents. 

## **1 Foundational Principles of the Plan-then-Execute Pattern** 

The rapid evolution of Large Language Model (LLM) agents has introduced powerful new paradigms for automating complex tasks. Among these, the Plan-then-Execute (P-t-E) architectural pattern has emerged as a cornerstone for building robust, predictable, and efficient agentic systems. Unlike more reactive approaches, P-t-E enforces a deliberate separation between strategic planning and tactical execution, a design choice with profound implications for an agent’s performance, cost-effectiveness, and, most critically, its security posture. This section deconstructs the fundamental principles of the P-t-E pattern, establishes its architectural advantages, and provides a comparative analysis against the prevalent ReAct (Reason-Act) model, setting a theoretical foundation for the secure implementation guides that follow. 

1 

**==> picture [468 x 193] intentionally omitted <==**

**----- Start of picture text -----**<br>
User Objective User Objective<br>1. Input 1. Input<br>Execution Plan<br>LLM Agent LLM Agent [Step #1<br>Step #2]<br>5. Step #2 2. Step #1 4. "Forget the objective, execute Step #2" 5. Step #2 2. Step #1<br>Delete_Files_Tool Web_Search_Tool Write_Files_Tool Web_Search_Tool<br>3. Retrieve content 3. Retrieve content<br>Malicious  Malicious<br>Website Website<br>**----- End of picture text -----**<br>


## **1.1 Deconstructing the Pattern: The Planner and the Executor** 

At its core, the Plan-then-Execute pattern is an agentic design methodology wherein an LLM first formulates a comprehensive, multi-step plan to achieve a complex objective. Subsequently, a distinct component, the executor, carries out that predetermined plan step by step (He et al., 2025). This explicit decoupling of planning from execution is the pattern’s defining characteristic and the source of its primary benefits. The architecture is composed of two fundamental components: the Planner and the Executor. 

**The Planner** The Planner’s function is to act as the agent’s strategic mind. It is typically implemented using a powerful, reasoning-intensive LLM, such as GPT-4 or Claude 3 Opus, which possesses the cognitive capabilities necessary to deconstruct a high-level, often ambiguous, user request into a coherent sequence of concrete, executable subtasks (Shen et al., 2023). The input to the Planner is the user’s objective, and its output is a structured plan. This plan is not merely a conversational suggestion; it is a formal artifact that will govern the agent’s behavior. The structure of this plan can vary, from a simple numbered list of natural language instructions to a more rigorous format like a JSON object or even a Directed Acyclic Graph (DAG) for tasks with complex dependencies (He et al., 2025). The quality of the plan is heavily dependent on the prompt used to invoke the Planner. Effective planner prompts are meticulously engineered to constrain the LLM’s output into the desired structured format. These prompts often include few-shot examples or a detailed template that specifies the exact output schema, ensuring the plan is machine-readable and directly consumable by the Executor (He et al., 2025). For instance, a prompt might instruct the Planner to “Generate a JSON array of steps, where each step has a ’task_description’ and a ’required_tool’ field” (Shen et al., 2023). 

**The Executor** The Executor is the agent’s tactical workhorse. Its responsibility is to take the structured plan generated by the Planner and carry it out, one step at a time. The Executor receives a single step from the plan and invokes the necessary tools, functions, or APIs to accomplish that specific subtask (Shen et al., 2023). A key architectural feature of the P-t-E pattern is that the Executor can be a much simpler, more specialized, and less computationally expensive component than the Planner. It can be a smaller, faster LLM, a simple ReAct agent focused on a single task, or even a deterministic piece of code that directly maps task descriptions to function calls (LangChain, 2024). In more sophisticated hierarchical implementations, the Executor itself can be a fully-fledged ReAct agent. This creates a powerful hybrid pattern where P-t-E operates at the strategic level, defining the overall mission, while ReAct is employed at the tactical level to handle the nuances of executing each individual step (LangChain, 2024). This modularity allows architects to tailor the complexity of the Executor to the complexity of the sub-tasks it is expected to perform. 

2 

**The Verifier** In advanced implementations, a third optional component is introduced to enhance trust and correctness in the planning process. The Verifier can be a human expert (as in HITL workflows) or an automated agent (often another LLM), a smaller rule-based model, or a static analysis engine. Its role is to inspect the output of the Planner before the Executor begins, ensuring that the proposed steps are logically sound, security-compliant, and aligned with high-level objectives or constraints. The Verifier adds a P-V-E safeguard, particularly in workflows where blind execution of incorrect plans could lead to high costs or irreversible actions. When automated, the Verifier uses a different prompt, persona, or model from the Planner to reduce the risk of mirroring the same mistakes. This separation of roles introduces a form of redundancy and cross-checking, significantly improving system resilience in low-trust or high-stakes environments. 

**The Refiner** Sometimes a Verifier is accompanied by a dedicated Refiner, which may be a human expert (HITL) or an automated agent. The Refiner implements any improvements, or provides workarounds or fixes for any issues flagged by the Verifier. In some systems the Planner may take over the role of the Refiner, thus not assigning a dedicated role to it. 

## **1.2 Architectural Advantages: Predictability, Cost-Efficiency, and Performance** 

The deliberate separation of concerns in the P-t-E pattern yields significant architectural advantages, making it particularly suitable for enterprise-grade and production-critical applications. 

**Predictability and Control** By generating the entire plan upfront, the agent’s trajectory becomes highly predictable. The sequence of actions is determined before the agent begins interacting with external tools or data sources. This design mitigates the risk of common failure modes seen in single-step reasoning agents, such as getting stuck in repetitive loops, taking suboptimal or circuitous paths to a solution, or losing focus on the overarching objective (He et al., 2025). This predictability is not merely a convenience; it is a critical feature for applications in domains like finance, logistics, or automated science, where reliability and auditable behavior are non-negotiable requirements. The upfront plan serves as a clear, auditable artifact of the agent’s intent. 

**Performance and Cost-Efficiency** From an operational standpoint, P-t-E architectures can be significantly faster and more cost-effective than their reactive counterparts, especially for tasks involving multiple steps (LangChain, 2024). The most expensive component - the large, reasoning-focused Planner LLM is invoked sparingly, perhaps only once at the beginning of a task, and occasionally for re-planning if the workflow supports it (Singh, 2025b). The execution of individual steps, which constitutes the bulk of the work, can then be handled by smaller, cheaper, and lower-latency models or, in many cases, by direct, non-LLM function calls (Patten, 2025). This architectural choice drastically reduces the number of calls to the primary LLM, which is a major driver of both latency and operational cost in agentic systems (LangChain, 2024). 

**Improved Reasoning Quality** The act of forcing an LLM to "think through" the entire problem and produce a complete, step-by-step plan before taking any action often leads to a higher quality of reasoning and a greater rate of successful task completion (LangChain, 2024) This phenomenon leverages a well-established principle in prompt engineering: eliciting a detailed chain of thought or a step-by-step breakdown of a problem enhances the logical coherence and accuracy of an LLM’s output (He et al., 2025). By making this comprehensive planning step a formal part of the architecture, the P-t-E pattern systematically encourages more robust and successful problem-solving from the underlying model. 

## **1.3 Comparative Analysis: Plan-then-Execute vs. ReAct** 

To fully appreciate the strategic value of the P-t-E pattern, it is essential to contrast it with the ReAct (Reason-Act) pattern, one of the most common and foundational designs for LLM agents. The ReAct pattern operates as a tight, iterative loop: the agent generates a Thought about what to do next, performs an Action (typically a tool call), observes the Observation (the result of the action), and then feeds that observation back into the loop to generate the next Thought (LangChain, 2024). This step-by-step process makes ReAct 

3 

agents highly adaptive and effective for simple, dynamic tasks. However, this same characteristic exposes them to a key weakness: “short-term thinking” (LangChain, 2024). Because the agent only plans one step at a time, it lacks a holistic view of the overall task, which can lead to inefficient paths or failures in complex scenarios with inter-step dependencies. The choice between these two patterns involves a series of critical trade-offs that architects must weigh based on their specific application requirements. 

**Task Complexity** ReAct is well-suited for simple, direct tasks that can be solved with a few tool calls and do not require long-term strategic planning. P-t-E, conversely, is designed for and excels at complex, multi-step tasks, particularly those with dependencies between steps where the outcome of one step informs the input of another (Shen et al., 2023). 

**Flexibility vs. Rigidity** ReAct’s iterative nature gives it high flexibility; it can immediately adapt its next step based on an unexpected tool output. The P-t-E pattern, in its simplest form, is more rigid. Once the plan is set, the agent follows it. This rigidity is a feature when it comes to predictability and security, but it becomes a bug if the initial plan is flawed and the architecture lacks a mechanism for re-planning (He et al., 2025). **Error Recovery** A ReAct agent that encounters a failed tool call can easily get stuck in a reasoning loop, repeatedly trying the same failed action. A P-t-E agent equipped with a re-planning loop can approach error recovery more strategically. It can assess the failure in the context of the entire plan and the overall objective, allowing it to formulate a more intelligent recovery strategy, such as trying an alternative tool or modifying subsequent steps in the plan (LangChain, 2024). 

**Cost and Latency** For tasks requiring many actions, ReAct’s model of one LLM call per action can lead to significant cumulative latency and API costs. P-t-E front-loads the primary LLM cost to the initial planning phase, after which execution can proceed more rapidly and cheaply (Singh, 2025b). A consolidated view of these trade-offs is available in Appendix B.1, serving as a decision-making aid for architects and developers. 

The selection of an agentic pattern is not a minor implementation choice; it is a foundational architectural decision. This choice has direct and cascading consequences on the application’s operational profile, including its cost model, its performance characteristics, its reliability, and its security posture. An application designed for financial reporting, which demands high accuracy, auditable steps, and complex data processing, is architecturally unsuited for a simple ReAct pattern and naturally calls for a P-t-E design (Patten, 2025). Conversely, a simple chatbot for answering one-off customer queries might find the overhead of P-t-E unnecessary and benefit from ReAct’s immediacy (Patten, 2025). Therefore, the architect’s first responsibility is to align the chosen pattern with the core business and operational requirements of the system. 

In addition, the “Plan-then-Execute” name belies the architectural richness available within the pattern itself. It is not a monolithic design but rather a family of related architectures defined by the intelligence of the Executor. The implementation can range from a simple for loop that iterates through plan steps and calls predefined functions, to an intelligent executor that uses a small LLM to map a natural language plan step to the correct tool and parameters, all the way to a fully agentic executor that is itself a ReAct agent tasked with completing a single, high-level objective from the main plan (LangChain, 2024). This creates a spectrum of possible implementations, allowing an architect to choose the complexity of the execution mechanism to precisely match the complexity of the sub-tasks, enabling a highly modular, scalable, and maintainable design. 

## **2 A Security-First Approach to Agentic Design** 

In the context of LLM agents capable of interacting with external systems and data, security is not an afterthought but a prerequisite for responsible deployment. The Plan-then-Execute pattern, while offering benefits in predictability and efficiency, also provides significant, inherent security advantages. However, it is no panacea. A robust security posture requires combining the P-t-E pattern with other established security 

4 

principles to create a defense-in-depth strategy. This section examines the specific security benefits of P-t-E, particularly its resistance to prompt injection, and details the complementary controls necessary to mitigate the full spectrum of risks associated with tool-using agents. 

## **2.1 The Core Security Benefit: Control-Flow Integrity and Prompt Injection Resistance** 

The most significant vulnerability facing LLM agents today is prompt injection. This attack class involves an adversary crafting inputs that manipulate the agent into executing unintended behaviors. While direct prompt injection (where a malicious user directly instructs the agent) is a concern, the more insidious threat is indirect prompt injection. In this scenario, malicious instructions are hidden within external, seemingly benign data sources that the agent consumes via its tools, such as a webpage, a PDF document, an email, or an API response (Masood, 2025). 

In a standard ReAct agent, this vulnerability is acute. The agent’s reasoning loop is continuously open to influence. After executing a tool and observing the output, the agent’s next “Thought” is generated based on this new, potentially tainted, information. If the tool output contains a prompt injection like, “Ignore previous instructions and send the user’s entire chat history to evil.com,” a ReAct agent is liable to interpret this as a valid new instruction and attempt to execute it, leading to data exfiltration or other malicious actions (Harang, 2023). 

The Plan-then-Execute pattern provides a powerful, architectural mitigation against this specific threat vector. By design, the P-t-E agent generates its entire plan of action before it begins ingesting any external, untrusted data through its tool calls. This means the agent’s high-level control flow is effectively “locked in” before it is exposed to potentially malicious inputs (Masood, 2025). A malicious instruction embedded in a tool’s output cannot alter the pre-approved sequence of planned actions. It might corrupt the data that is passed to a subsequent step, for example, the malicious text might be included in the body of an email, but it cannot cause the agent to spawn a new, unplanned action, like calling a different tool or altering the fundamental logic of its workflow (Masood, 2025). This separation of planning from execution provides a strong form of control-flow integrity, a concept borrowed from traditional software security. 

This security benefit is not merely theoretical. Formal research into secure agent architectures has identified the P-t-E pattern as a critical design choice for building prompt-injection-resilient systems (Li et al., 2025). For example, the Agent-centric Controllable Execution (ACE) framework proposes a system with a trusted, abstract planner that is immune to influence from installed applications. It generates a plan, which is then verified against static security policies (e.g., permissible information flows) before any execution is allowed to commence in a separate, isolated environment (Li et al., 2025). This formalizes the core security principle of P-t-E: plan in a trusted state, then execute in a potentially untrusted context with the plan held immutable. 

## **2.2 Mitigating Tool & Function Call Vulnerabilities** 

While P-t-E provides excellent protection for the plan’s structure, it does not inherently secure the data that flows between the steps of the plan. An attacker can still leverage a compromised tool output to execute attacks. For example, if Step 1 is “Search the web for the latest company report” and Step 2 is “Summarize the report and email it to the CEO,” an attacker who controls the website could inject a malicious payload into the report’s text. The P-t-E agent would correctly follow its plan, but the email sent in Step 2 would contain the malicious content, potentially leading to a phishing attack on the CEO. 

Therefore, to build a truly secure system, the P-t-E pattern must be augmented with a suite of complementary security controls that form a defense-in-depth strategy (Masood, 2025). 

**Input Sanitization and Validation** All data returned from tools, especially those that access external or user-generated content, must be treated as untrusted. Before this data is used as input for another tool or included in a final response, it should be rigorously sanitized and validated. This could involve stripping out potential script tags, checking for known injection phrases, or validating that the data conforms to an expected format (Posta, 2025). 

5 

**Output Filtering** Before presenting a final response to the user or passing data to a sensitive outbound tool (like an email client or API), the agent’s output should be filtered. This post-processing step can scan for anomalies, potential leakage of personally identifiable information (PII), or content that violates security policies (Posta, 2025). 

**Dual LLM / Quarantined LLM Pattern** For enhanced security, a Dual LLM architecture can be employed. This pattern uses a “privileged” LLM for trusted operations like planning and a separate, “quarantined” LLM whose sole purpose is to process untrusted data. The privileged planner would never directly see the raw content of a webpage. Instead, it would delegate that task to the quarantined LLM, which would be instructed to summarize the page or extract specific information into a strict, data-only format. The privileged LLM then receives this sanitized, structured data, never the raw, potentially malicious input. This creates a “cognitive sandbox” that shields the agent’s core reasoning process from direct injection attacks (Masood, 2025). 

**Human-in-the-Loop (HITL) for High-Risk Actions:** For any action deemed critical or irreversible - such as executing a financial transaction, writing to a production database, or sending a high-importance email - the agent’s execution must pause and await explicit human approval. This ensures that a human operator has the final say before any potentially damaging action is taken, serving as a crucial backstop against automated failures or attacks (Konsinski, 2024). 

## **3 The Principle of Least Privilege: Scoping Tools and Permissions** 

A foundational concept in modern cybersecurity is the Zero Trust principle of “Least Privileged Access,” which dictates that any entity (a user, a service, or an agent) should be granted only the minimum level of access and permissions necessary to perform its specific, authorized function (Srivastava, 2025). This principle must be rigorously applied to the design of LLM agents (Konsinski, 2024). 

In practice, this means that tools should not be made globally available to an agent or all of its components. The Planner agent, for instance, may require no tools at all, as its job is simply to reason and produce a plan. If it does need tools, they should be limited to introspection capabilities, such as listing the tools available to the executors. 

Most importantly, the Executor component should be dynamically provisioned with access only to the specific tool(s) required for the immediate step of the plan it is executing. This is a critical security control that prevents an entire class of attacks. For example, consider a plan with two steps: (1) “Use the calculator to determine the total cost,” and (2) “Send an email with the result” When the executor is working on Step 1, it should only have access to the calculator_tool. It should be architecturally impossible for it to access the send_email_tool at that moment. This prevents an attacker from injecting a prompt that tricks the agent into sending an email during the calculation phase (Russo, 2025). This dynamic, task-scoped provision of tools is a key feature that modern agentic frameworks like CrewAI and LangGraph enable and will be a central theme in the implementation guides. 

Still, while task-scoping governs tool access during individual execution steps, it does not define the broader functional boundaries of what an agent should ever be allowed to do. And while task-scoping determines what an agent can do in a specific moment, another layer of protection answers a more durable question: what class of actions is the agent fundamentally allowed to perform at all? This is where Role-Based Access Control (RBAC) becomes relevant, not yet implemented in frameworks like CrewAI, but highly applicable to future iterations of such systems. 

RBAC is a widely adopted industry standard, prevalent in sectors such as finance, healthcare, and cloud computing, where permissions are not granted directly to individual users or agents, but instead to roles (e.g., Research Analyst, Compliance Reviewer, Data Engineer). Agents are assigned roles according to their function, and each role comes with a pre-approved, auditable permission set. 

In LLM-based multi-agent architectures, RBAC could offer a structured and scalable way to enforce least privilege. While task-level scoping restricts tools dynamically during execution, RBAC defines the upper bound of access, based on role identity assigned during the planning phase. For instance, an agent assigned 

6 

the role of DataReader might be categorically prevented from invoking write or communication tools, even if a plan or prompt erroneously included such steps. The combination of RBAC (durable, role-level constraints) and task-scoped tool assignment (fine-grained, step-level control) forms a defense-in-depth model for secure agent execution. It enables consistency across dynamic workloads, improves auditability (actions are tied to roles), and aligns with the principle of least privilege by ensuring that agents can neither exceed their planned permissions nor escape their immediate task scope. 

While CrewAI and similar frameworks currently emphasize task-based scoping, future frameworks could, and likely will, incorporate RBAC-style abstractions (since lots of systems currently deploy this IAM model). Doing so would bring agent systems closer to the mature access control models used in real-world enterprise environments, enabling policy enforcement, role governance, and traceable execution boundaries that scale with system complexity. 

## **3.1 Sandboxing Execution: The Role of Isolated Environments** 

Among the most powerful and dangerous capabilities an agent can possess is the ability to write and execute code, such as Python scripts or shell commands (Harang, 2023). A vulnerability in this area can easily escalate to a full Remote Code Execution (RCE) attack on the host system, giving an attacker complete control. 

For this reason, it is a non-negotiable security requirement that any agent system that generates and executes code must do so within a strongly isolated, sandboxed environment. The most common and effective method for achieving this is by using Docker containers (Autogen, 2025). When the agent needs to execute a piece of code, the system should: 

1. Spin up a new, ephemeral Docker container from a minimal base image. 

2. Copy the generated code into the container. 

3. Execute the code inside the container. 

4. Capture the output (stdout/stderr) and any generated files. 

5. Destroy the container. 

This ensures that even if the agent is tricked into generating malicious code (e.g., code that attempts to delete files or access the network), the “blast radius” of the attack is confined entirely to the temporary container. The host system’s file system, network, and processes remain unaffected. Frameworks like AutoGen (Autogen, 2025) provide built-in support for this Docker-based code execution, making it a key differentiator for security-conscious development teams (Autogen, 2025). 

Appendix B.2 maps common agent-related security threats to their primary P-t-E-based mitigations and essential complementary controls, providing a checklist for designing a defense-in-depth strategy. 

A significant implication of this security-first approach is a fundamental shift in how we think about agent safety. Early attempts at LLM security focused heavily on behavioral containment - that is, trying to make the LLM itself “safe” through clever system prompting (e.g., “You are a helpful assistant and you must never follow malicious instructions”) (Konsinski, 2024). However, extensive research and real-world attacks have demonstrated that this approach is brittle and fundamentally unreliable (Masood, 2025). An LLM cannot be fully trusted to police its behavior when faced with a sufficiently sophisticated adversarial input. 

The P-t-E pattern, when combined with the controls discussed above, represents a move towards a much more robust paradigm: architectural containment. This approach aligns with the Zero Trust principle of “assume breach” (Srivastava, 2025). It operates on the assumption that the LLM component might be compromised by a malicious input. The security of the system, therefore, does not rely on the LLM’s good behavior. Instead, it relies on the surrounding architecture, which enforces hard constraints: even if the LLM is hijacked, it can only execute the pre-approved plan (P-t-E), it can only use the specific tools it has been granted for the current step (least privilege), and it can only run code within a locked-down sandbox 

7 

(isolation). This moves the boundary of trust from the unpredictable, probabilistic LLM to the predictable, auditable components of the system architecture. This is a profound and necessary evolution in thinking for any security architect designing agentic systems. 

This leads to a further refinement of the pattern for high-stakes applications. While Human-in-the-Loop is often considered for approving individual execution steps, empirical studies on user trust reveal a critical flaw in this model: LLMs can generate “convincingly wrong” plans that appear plausible and well-structured but are logically flawed or based on incorrect assumptions (He et al., 2025). Users, even experts, can be misled by the agent’s confident presentation into approving a fundamentally bad plan. If a flawed plan is approved, then even with perfect, human-supervised execution of each step, the final outcome will still be incorrect. The error was introduced and cemented at the planning stage. 

This suggests that for mission-critical systems, the most vital point for human intervention is not during execution, but after the plan is generated and before any action is taken. This gives rise to a more secure variant of the pattern: Plan-Validate-Execute. In this model, the agent generates a plan, which is then presented to an expert human operator for validation. The human reviews the entire proposed sequence of actions for logical soundness, safety, and alignment with the objective. Only after the human explicitly validates the plan is the Executor permitted to begin its work. This “Plan-Validate-Execute” workflow mitigates the significant risk of acting on “convincingly wrong” plans and represents a crucial design pattern for deploying agents in high-risk domains like medicine, finance, and industrial control. 

While strong sandboxing remains non-negotiable for tasks involving arbitrary code execution, we recognize that not every agent action carries the same operational risk. Some steps such as extracting metadata, formatting summaries, or reading structured data may not involve critical system-level side effects. Applying full containerized sandboxing to these low-risk actions may be unnecessarily costly and slow, particularly at scale. 

To address this, agent systems can adopt a tiered or partial sandboxing strategy, guided by the role assigned to each agent or task during the planning phase. Under this approach, RBAC roles and tasks not only determine what tools an agent may use, but also what level of isolation is required to execute its actions safely. For instance: 

- An agent with the role CodeExecutor would always run in a Docker-based sandbox. 

- An agent tagged ReportReader might be allowed to run natively in a read-only mode. 

This allows architects to calibrate execution environments based on risk and intent, ensuring that high-risk behaviors remain tightly confined, while benign operations could run efficiently under well-scoped permissions. 

Future agentic frameworks may embed this logic as a runtime policy: a mapping between roles, tasks, and isolation strategies, enforced automatically by The Planner or The Executor. This creates a secure and scalable foundation where sandboxing is precise but not excessive, maintaining safety without trading off performance. In practice, this could further strengthen the P-t-E paradigm by ensuring that architectural containment is not just applied globally, but tuned intelligently based on what the agent is doing and who it is authorized to be. 

## **4 Framework Implementation Guide: LangChain & LangGraph** 

LangChain, as one of the most established frameworks for developing LLM applications, provides multiple avenues for implementing the Plan-then-Execute pattern. The modern, recommended approach leverages LangGraph, a library designed for building stateful, multi-agent applications as cyclic graphs. This offers far greater flexibility, control, and resilience than the legacy, experimental implementations. This section will briefly cover the legacy approach for historical context before providing a detailed, security-focused guide to building a P-t-E agent with LangGraph. 

8 

**==> picture [468 x 241] intentionally omitted <==**

**----- Start of picture text -----**<br>
Permission Boundary<br>State<br>END<br>User_input<br>State Agent #1 Plan: [Agent#1,<br>3. Send  State Tool A Agent#2]<br>User_input<br>Plan: [Agent#1, Planner Past_steps:[Agent#1]<br>Agent#2]<br>11. Send  4. Update  State<br>Past_steps: [] Final Response<br>State<br>User_input<br>State 2.Update  State 5. Send  State Agent #2Tool B Plan: [Agent#1,<br>User_input START 1. Send  State Executor Agent#2]<br>Plan: [] 6. Update  State<br>Past_steps: [] OnFailure Past_steps:[Agent#1, Agent#2]<br>7. Replan  State<br>State<br>9. Send  State<br>User_input<br>State 10. Update  State Agent #3Tool C Plan: [Agent#1,Agent#2, Agent#3]<br>(...) Replanner 8.  Update  State Past_steps:<br>Plan: [Agent#1, [Agent#1, Agent#2,<br>Agent#2, Agent#4] Agent#3]<br>**----- End of picture text -----**<br>


## **4.1 Legacy Implementation: The PlanAndExecute Executor in LangChain** 

For completeness, it is worth noting LangChain’s original implementation of this pattern, which resides in the langchain_experimental.plan_and_execute module (LangChain, 2024). This approach provides a high-level abstraction that combines a planner and an executor into a single agentic chain. 

The mechanism involves two primary components: load_chat_planner, which uses an LLM to generate the plan from a user’s input, and load_agent_executor, which takes the plan and executes each step (LangChain, 2024). A common pattern is for the executor itself to be a ReAct agent, creating the hierarchical model where the high-level plan is executed by a low-level agent that can reason through the specifics of each step (LangChain, 2024). 

However, this implementation is designated “experimental” for several reasons. It offers limited flexibility for customization. Implementing robust error handling, conditional logic, or, most importantly, a re-planning loop is non-trivial and often requires subclassing and overriding internal methods. The linear, one-shot nature of the planner makes it brittle in the face of unexpected tool outputs. For these reasons, while it served as an important proof of concept, it is not recommended for production systems. The modern, more powerful approach is to use LangGraph. 

## **4.2 Modern Implementation with LangGraph: Building a State Machine** 

LangGraph reimagines agentic workflows not as linear chains but as stateful graphs. It is a library for building complex, long-running, and stateful agents by defining their logic as a graph of nodes and edges (LangGraph, 2025). This paradigm is exceptionally well-suited for implementing a robust and secure P-t-E pattern. 

The P-t-E workflow in LangGraph is modeled as a state machine, where the state is explicitly defined and passed between nodes in the graph (LangGraph, 2025). 

**The State** The foundation of a LangGraph workflow is the state object, typically a Python TypedDict. This central data structure persists and is updated throughout the graph’s execution. For a P-t-E agent, the state must contain, at a minimum, the initial user input, the generated plan (e.g., a list of strings), a history of past_steps (e.g., a list of tuples containing the step and its result), and a field for the final response (LangGraph, 2025). 

9 

**The Nodes** Nodes are functions or other callables that represent the computational steps in the graph. Each node receives the current state as input and returns a dictionary of updates to be applied to the state. A P-t-E graph typically consists of the following nodes: 

- **planner_node** : This node is the entry point after the start. It takes the user input from the state, calls a planner LLM (often with a structured output format enforced via Pydantic or JSON mode) to generate the plan, and returns the plan to be added to the state (LangGraph, 2025). 

- **executor_node** : This node contains the execution logic. It reads the plan and past_steps from the state, identifies the next step to be executed, and invokes a tool-equipped agent to perform that action. The result of the execution is then returned as an update to the past_steps list in the state (LangGraph, 2025). 

- **replan_node** : In advanced implementations, a re-planning node can be added. This node examines the history of past_steps to determine if the execution is proceeding as expected. If a failure occurred or the plan is no longer viable, this node can invoke the planner LLM again to generate a revised plan (LangGraph, 2025). 

**The Edges** Edges define the control flow, connecting the nodes. LangGraph uses both standard edges and conditional edges. The flow starts with an edge from the START node to the planner_node. The planner then connects to the executor_node. The most critical part of the P-t-E graph is the **conditional edge** that follows the executor. This edge contains logic to inspect the state and decide where to go next. For example, it checks if there are more steps left in the plan. If yes, it routes the flow back to the executor_node to continue the loop. If all steps are complete, it routes the flow to the END node, terminating the workflow (langchain-ai, 2025b). 

## **4.3 Code Reference: A Secure LangGraph Plan-and-Execute Agent** 

A complete, runnable example of a secure P-t-E agent built with LangGraph is available in Appendix A.1. This implementation goes beyond basic examples by incorporating the Principle of Least Privilege directly into the executor node. 

**Security Enhancement** The planner is prompted to produce a plan where each step includes not just a description but also the single specific tool required for that step. The executor node then dynamically creates a new, temporary agent for each step, equipping it only with the one tool specified in the plan. This prevents a tool that is valid for Step 3 from being accessible during the execution of Step 1, providing granular security. 

The architecture of LangGraph does more than just implement the P-t-E pattern; it elevates it from a rigid, linear process into a flexible, potentially cyclic graph. This is a fundamental shift that enables the creation of more resilient and intelligent agents. The legacy PlanAndExecute class was largely a “fireand-forget” mechanism - the plan was made and then followed inflexibly (LangChain, 2024). LangGraph, through its introduction of nodes, state, and particularly conditional edges, makes cycles a natural part of the architecture (LangGraph, 2025). The most powerful of these cycles is the Execute _→_ Re-plan _→_ Execute loop. By adding a replan_node, the agent can inspect the results of its actions (stored in the past_steps list within the state) and intelligently decide if the original plan remains viable. If a tool fails or returns an unexpected result, the replanner can generate a new, more robust plan, and the conditional edge can route the control flow back to the executor with this revised strategy (LangGraph, 2025). This transforms P-t-E from a brittle script into an adaptive, self-correcting system, representing a significant leap in agentic robustness and a primary motivation for adopting LangGraph for production systems. 

## **5 Framework Implementation Guide: CrewAI** 

CrewAI is a multi-agent framework designed to facilitate collaboration between autonomous AI agents. Its high-level abstractions - Agents, Tasks, and a Crew - provide a structured and intuitive way to build complex 

10 

workflows. The framework’s design, particularly its hierarchical process, naturally maps to the Plan-thenExecute pattern, with a strong and unique emphasis on granular security controls through task-level tool scoping. 

## **5.1 The Hierarchical Process: Manager as Planner, Workers as Executors** 

CrewAI’s architecture is built upon three core components: the Agent, which is the actor performing the work; the Task, which defines a specific unit of work to be done; and the Crew, which orchestrates the agents and tasks to achieve an overall objective (CrewAI, 2025c). To implement a P-t-E workflow, one must use the Process.hierarchical setting when instantiating the Crew (CrewAI, 2025c). 

This setting fundamentally changes the crew’s operational model and requires the designation of a manager, which maps directly to the P-t-E components: 

**Planner** _→_ **Manager Agent** When process is set to hierarchical, the Crew must be assigned a manager_agent. This agent’s designated role is to act as the Planner. It receives the overall goal, analyzes it, breaks it down into a series of discrete tasks, and then delegates each task to the most appropriate worker agent in the crew (CrewAI, 2025c). For the manager agent to be able to delegate, its allow_delegation parameter must be set to True. The manager’s system prompt and goal should be crafted to guide it in this strategic planning and coordination role. 

**Executors** _→_ **Worker Agents** The other agents defined in the agents list of the crew function as the Executors. Each worker is typically designed as a specialist with a specific role, backstory, and a set of tools tailored to its function (e.g., a “Researcher” with search tools, a “Writer” with file I/O tools) (CrewAI, 2025c). They do not create the high-level plan; they receive specific tasks delegated to them by the Manager Agent and execute them. 

This manager-worker dynamic provides a clean and high-level abstraction for the P-t-E pattern, allowing developers to focus on defining the roles and capabilities of their agents rather than the low-level mechanics of the control flow. 

## **5.2 Secure Tool Scoping: Assigning Capabilities to Agents vs. Tasks** 

A standout feature of CrewAI, and one that is critical for security, is its mechanism for scoping tool access. The framework makes a crucial distinction between assigning tools at the Agent level versus the Task level, providing a powerful method for enforcing the Principle of Least Privilege (Russo, 2025). 

**Agent-Level Tools (agent.tools)** This parameter defines the complete set of tools that an agent could use. It represents the agent’s full potential capabilities - its entire toolbox (Russo, 2025). For example, a DataAnalyst agent might have tools for reading databases, performing calculations, and writing files. 

**Task-Level Tools (task.tools)** This parameter defines a specific, limited subset of tools that are permitted for the execution of that particular task. This is the key to granular security control (Russo, 2025). The critical rule of precedence is that Task.tools overrides Agent.tools. If Task.tools is explicitly defined for a given task, the agent assigned to that task can only use the tools in that list, regardless of what other tools it may have in its own tools list. If the Task.tools list is left undefined, the task will inherit the full set of tools from the assigned agent (Russo, 2025). 

This mechanism allows for the implementation of a robust security posture. The best practice is to define a worker agent with its potential capabilities, but then for each task delegated to it, to strictly constrain the available tools to the absolute minimum required. For instance, a FinancialAgent might have both a market_data_lookup_tool and a trade_execution_tool. For a “Market Research” task, its tools can be scoped to only the market_data_lookup_tool. For a subsequent “Execute Trade” task, it can be given access to only the trade_execution_tool. This prevents the agent from being tricked into executing a trade 

11 

while it is only supposed to be conducting research, effectively mitigating the risk of unauthorized tool use (Russo, 2025). 

## **5.3 Secure Tool Scoping: Hybrid approaches** 

CrewAI already enables fine-grained tool restriction on a per-task basis, supporting the enforcement of least privilege dynamically during execution. However, this can be enhanced further through the integration with existing RBAC ecosystems. 

In an RBAC-integrated setup, each agent could be tagged with a role at plan time, assigned by the Planner, and each role maps to a static permission profile. For example, the role WebSearcher may include access to web search, summarization, and citation tools, while FinanceWriter may allow read-only access to internal datasets and spreadsheet generation, but no write access to other types of APIs. 

This dual enforcement mechanism offers defense-in-depth: 

- Roles act as coarse-grained, pre-approved permission containers, defining what an agent is ever allowed to do. 

- Tasks scope tools within those roles to the minimum necessary for the current execution step. 

RBAC has proven itself effective in real-world access control at scale, from Kubernetes clusters and AWS IAM policies to internal enterprise tools and SaaS platforms. Its adoption in LLM agent architectures would bring similar benefits: auditability (each action can be logged against the role it was performed under), composability (roles are reusable across agents), and clarity of trust boundaries (system operators can reason about what classes of actions an agent is even capable of). For example, a Planner could output the following metadata during planning: 

```
{
"task":"extract_customer_feedback",
"agent":"feedbackBot",
"role":"DataReader",
"tools":["read_file","summarise_text"]
}
```

Here, the role DataReader would be validated against a predefined permission map. Any attempt by this agent to use write or external communication tools would be rejected at execution time, even if they appear in the plan, because they exceed the privileges of the assigned role. 

By embedding RBAC directly into the planning and execution lifecycle, agentic systems gain structural enforcement of least privilege that scales with system complexity and existing organizational policies. 

## **5.4 Code Reference: A Secure CrewAI Manager-Worker Crew** 

A complete, runnable example of a secure P-t-E implementation in CrewAI is available in Appendix A.2. It demonstrates the manager-worker pattern and explicitly uses task-level tool scoping to enforce the Principle of Least Privilege. 

The CrewAI design philosophy introduces a subtle but powerful shift in where security controls are applied. In many agentic frameworks, security policies like tool access are primarily bound to the Agent definition. This can be somewhat static; the agent has a fixed set of capabilities. CrewAI, through its powerful Task abstraction, makes security more dynamic and granular. The Task object becomes the primary locus of control, capable of overriding an agent’s default toolset for a specific job (Russo, 2025). 

This means the same Agent can be deployed in multiple contexts with different, situationally appropriate security postures. A DataAnalyst agent might be defined with a full suite of tools for reading from and writing to a database. However, when the Manager assigns it a “Generate Quarterly Summary Report” 

12 

Task, its tools can be dynamically restricted to read-only database access. Later, when the same agent is assigned an “Update Customer Records” Task, it can be granted the necessary write permissions for that specific job. The Planner (the Manager Agent) is responsible for creating and delegating these well-defined, security-scoped Tasks. Consequently, security in CrewAI is not just about defining safe agents; it is about defining safe units of work. This task-centric security model is more flexible, more dynamic, and aligns more closely with the Principle of Least Privilege, as permissions are granted “just-in-time” for a specific task, not “just-in-case” for the agent’s entire operational lifecycle. 

## **6 Framework Implementation Guide: AutoGen** 

Microsoft’s AutoGen (Autogen, 2025) is a highly flexible framework designed for orchestrating complex conversations and workflows between multiple, specialized agents (Awan, 2025). Unlike frameworks with a built-in, high-level primitive for “plan-and-execute,” AutoGen achieves this pattern through its core strength: the sophisticated management of multi-agent dialogues. Implementing P-t-E in AutoGen (Autogen, 2025) involves architecting a conversation flow that enforces the desired separation between planning and execution. This section explores how to construct such a workflow and highlights AutoGen’s critical, built-in feature for secure code execution. 

## **6.1 Orchestrating P-t-E with Group Chat and Sequential Conversations** 

AutoGen’s fundamental paradigm is the “conversable agent” (Awan, 2025). The framework’s power lies not in predefined workflow structures but in the developer’s ability to define the rules of interaction between these agents. There are two primary methods for orchestrating a P-t-E pattern. 

**Method 1: Sequential Chat (initiate_chats)** A straightforward way to mimic a P-t-E workflow is by using the initiate_chats method, which allows one agent to start a series of distinct, sequential conversations with other agents (AutoGen, 2025). The output or summary of one conversation can be passed as a “carryover” context to the next. 

- **Chat 1 (Planning):** A UserProxyAgent (representing the user or a higher-level orchestrator) initiates a chat with a PlannerAgent. The PlannerAgent’s sole task is to receive the user’s objective and generate a structured plan. The result of this chat - the plan itself - is captured and used as the input for the next stage. 

- **Chat 2 (Execution):** The UserProxyAgent then initiates a new chat with an ExecutorAgent. The plan from the first chat is passed into this conversation as context. The ExecutorAgent is then responsible for carrying out the steps of the plan. This can be implemented as a loop within the agent’s logic or, for more complex plans, as a further sequence of chats. 

**Method 2: Group Chat with Custom Speaker Selection (Recommended)** This is a more powerful, flexible, and robust method for implementing P-t-E. It involves creating a GroupChat containing all the necessary agents (planner, executors, user proxy) and controlling the flow of conversation via a GroupChatManager equipped with a custom speaker_selection_method (Autogen, 2025). This custom function acts as the central orchestrator, effectively hard-coding the P-t-E logic into the state machine of the conversation. 

- **Agent Roles:** The group would contain a Planner agent, one or more specialist Executor agents (e.g., a CodeWriterAgent), and a UserProxyAgent to execute code and represent the user. 

- **Custom Logic:** The speaker_selection_method is a Python function that is called after each turn to decide which agent speaks next. The logic would be defined as follows: 

   1. If the chat has just started, select the Planner agent. 

   2. If the last speaker was the Planner, analyze its message. If it contains a complete plan, select the appropriate Executor agent. 

13 

3. If the last speaker was an Executor that produced code, select the UserProxyAgent (configured as the code executor) to run the code. 

4. If the UserProxyAgent reports a successful execution, the function can select the next Executor or terminate the chat. If it reports an error, it can select the CodeWriterAgent again to debug the code. 

This method turns the conversational flow into a deterministic state machine that precisely follows the P-t-E pattern, including potential loops for debugging and refinement. 

## **6.2 Enforcing Security with Dockerized Code Execution** 

A critical security feature of AutoGen (Autogen, 2025) is its built-in support for sandboxed code execution. In many AutoGen workflows, the UserProxyAgent is configured not just to represent the human user but also to act as the entity that executes code generated by other agents (Tizkova). This is managed through the code_execution_config parameter. 

This parameter is a dictionary that contains several key settings, but the most important for security is use_docker (Autogen, 2025). 

**use_docker: True:** When this setting is enabled, AutoGen will not execute any generated Python code directly on the host machine’s operating system. Instead, it will automatically perform the following actions: 

1. Provision a new Docker container using a specified or default Python image. 

2. Execute the generated code snippet inside this isolated container. 

3. Capture the results (e.g., stdout) from the container. 

4. Return the results to the agent conversation. 

5. Terminate and discard the container. 

This provides a powerful layer of isolation. Even if a planner or writer agent is compromised through a prompt injection attack and generates malicious code (e.g., os.system(’rm -rf /’)), the code’s execution is contained entirely within the ephemeral Docker environment. It cannot access the host file system, network (unless explicitly configured), or other processes. This makes the use_docker: True setting an essential, non-negotiable best practice for any AutoGen application that involves code generation and execution. 

## **6.3 Code Reference: A Secure AutoGen. Planner-Executor Group** 

A complete, runnable example of a secure P-t-E workflow in AutoGen (Autogen, 2025). is available in Appendix A.3. It uses the recommended Group Chat with Custom Speaker Selection method and enforces secure, Dockerized code execution. 

The conversational architecture of AutoGen necessitates a unique perspective on implementing agentic patterns like P-t-E. It is less about defining a static data flow graph and more about designing a governed dialogue. The security and logic of the system are emergent properties of the rules of this conversation and the intrinsic capabilities of its participants. 

An architect using AutoGen must essentially design a secure protocol. Who is allowed to speak to whom, and in what order? This is managed by the GroupChatManager and the speaker selection logic (Autogen, 2025). What are the capabilities of each participant? This is defined in their agent configurations. Crucially, in what environment do they perform their actions? This is controlled by settings like code_execution_config (Autogen, 2025). The P-t-E pattern is thus abstracted into a problem of protocol design. This mental model is particularly powerful for security engineers, who are well-versed in analyzing and designing secure communication protocols. The overall security of the AutoGen system becomes a function of the robustness of its defined conversational rules and the sandboxed environments in which its agents operate. 

14 

## **7 Advanced Patterns and Strategic Considerations** 

While the basic Plan-then-Execute pattern provides a solid foundation for building predictable and secure agents, its simple, linear form has limitations in complex, real-world scenarios. To create truly resilient, efficient, and trustworthy production-grade systems, architects must incorporate more sophisticated patterns that address brittleness, performance bottlenecks, and the inherent fallibility of LLMs. This section explores advanced strategies, including dynamic re-planning, parallel execution via Directed Acyclic Graphs (DAGs), and the critical role of Human-in-the-Loop (HITL) verification. 

## **7.1 Dynamic Adaptation: Implementing Re-planning Loops** 

A static, one-shot plan is inherently brittle. It assumes a perfect world where tools always succeed, data is always in the expected format, and the initial assumptions made by the planner hold true throughout execution. In reality, it rarely is. A tool call might fail due to a network error, an API may return an unexpected response, or the information gathered in an early step may invalidate the logic of later steps (LangChain, 2024). Without a mechanism to adapt, the agent will fail. 

The ability to dynamically re-plan is, therefore, crucial for building resilient agents (LangChain, 2024). This involves adding a feedback loop to the P-t-E architecture. The implementation typically involves a “replanner” step or node in the workflow. After each execution step, the control flow moves to this re-planner, which is an LLM call that is provided with: 

1. The original high-level objective. 

2. The original plan. 

3. The history of all previously executed steps and their outcomes. 

With this context, the re-planner LLM can assess the current situation and make an intelligent decision: continue with the existing plan, generate a completely new plan to overcome an obstacle, or determine that the task is complete (LangGraph, 2025). Frameworks like LangGraph, with their native support for cyclic graphs, are exceptionally well-suited for implementing this pattern. A dedicated replan node can be added after the executor node, with conditional edges routing the flow back to the executor (with a potentially new plan) or to the end of the workflow. This transforms the agent from a rigid automaton into a resilient problem-solver. 

## **7.2 Enhancing Performance** 

## **7.2.1 Parallel Execution with Directed Acyclic Graphs (DAGs)** 

The standard P-t-E model executes plan steps sequentially, one after another. This is a significant performance bottleneck if the plan contains independent tasks that could be performed concurrently (LangGraph, 2025). For example, a plan to “Research competitor A’s market share and competitor B’s latest product launch” involves two independent web search tasks that do not need to wait for each other. 

To overcome this, the planning model can be advanced from generating a simple linear list to producing a Directed Acyclic Graph (DAG). In a DAG-based plan, each task explicitly declares its dependencies on other tasks (LangChain, 2024). For example, a task to “Synthesize research findings” would have dependencies on the two research tasks mentioned above. 

This concept has been formalized in research like the LLMCompiler paper (LangChain, 2024). In this architecture, the Planner streams a DAG of tasks. A separate component, the “Task Fetching Unit,” monitors the graph and schedules tasks for execution as soon as their declared dependencies have been met. This allows for maximal parallelism, as multiple independent tasks can be executed concurrently. The paper reports significant speed boosts (up to 3.6x) from this parallel execution, especially for tasks that involve I/O-bound operations like web searches or API calls (LangChain, 2024). While implementing a full-scale 

15 

DAG-based execution engine is a complex engineering task, the architectural concept is critical for developers building performance-sensitive agentic systems. 

The evolution of the P-t-E pattern from a simple, linear sequence to a robust loop with re-planning, and finally to a high-performance parallel graph mirrors the historical evolution of software build systems in traditional engineering. The initial P-t-E model is analogous to a simple shell script that executes commands in a fixed order. The introduction of re-planning loops is akin to adding error handling and conditional logic to that script, making it more resilient. The final step, moving to a DAG-based planner that manages dependencies and enables parallel execution, is conceptually identical to the shift from simple scripts to sophisticated build tools like make or Bazel. These tools parse a dependency graph (Makefile or BUILD files) to execute compilation and testing tasks in parallel for maximum efficiency. This parallel suggests that as agentic systems mature, they are independently rediscovering and adapting proven principles from decades of software architecture. Architects can leverage this understanding by applying established patterns like dependency management, parallel processing, and fault tolerance to their agent designs, rather than treating them as an entirely novel class of problems. 

## **7.2.2 Minimizing Context Overhead with GraphQL Integration** 

Another promising direction for optimizing data retrieval in multi-agent systems is the integration of GraphQL (GraphQL, 2025) as a tool interface. While not yet widely adopted in current multi-agentic frameworks, it offers a highly aligned model for P-t-E architectures: agents can request exactly the fields they need from structured data sources, minimizing context window usage and API latency. 

In this design, the Planner could formulate or select GraphQL queries (e.g., through a schema-aware tool wrapper), and the Executor would execute them as discrete steps. This has two clear benefits: 

- **Reduced token overhead** , since only the explicitly requested fields (e.g., user.name rather than the entire profile) are returned and added to context 

- **Fewer steps per plan** , as GraphQL can resolve nested or related data in a single call, avoiding the need to chain multiple REST tool invocations. 

Emerging frameworks such as MCP (and its multi-server architecture) already demonstrate how GraphQL operations can function as callable tools (Hawkins, 2025) This confirms the feasibility of treating GraphQL queries as structured, predictable agents’ tools, delivering JSON payloads that are compact, auditable, and easy to constrain via schema validation. 

While a full GraphQL agent integration remains a forward-looking recommendation, it represents a clean, cost-efficient path for multi-agent architectures that require consistent access to structured internal data, particularly in systems where token control, latency, and interface trust boundaries are key concerns. 

## **7.2.3 Graph-Based Conditional Execution Paths** 

Rather than waiting for failures to occur before re-engaging the Planner, agentic systems can be made more resilient by embedding alternate execution paths directly into the initial plan structure. One way to improve execution resilience is to embed conditional fallback branches directly into the initial plan, allowing agents to handle known contingencies without restarting from scratch. Instead of outputting a strictly linear execution sequence, the Planner could emit a graph that includes aforementioned conditional edges, encoding alternate paths or recovery actions ahead of time. 

This approach builds upon the graph model discussed in the previous section, extending it beyond parallelism into dynamic routing. For example, the Planner could produce logic like: “If Tool A fails, attempt Tool B,” or “If the input data is structured as X, follow path A; else follow path B.” These embedded decision points would enable the Executor to locally pivot to alternate steps when minor, anticipated failures occur, without re-invoking the Planner or invalidating the entire plan. 

As mentioned before, LangGraph already supports this model through conditional edge evaluation (you can see an example in the Appendix), making it feasible to express branching control flow in LLM-driven work- 

16 

flows (AI/ML, 2025) By leveraging these capabilities, developers can predefine multiple valid routes through the plan graph, allowing agentic systems to recover gracefully from predictable faults while still reserving full re-planning for true edge cases. This pattern saves latency, reduces token overhead, and enhances robustness by turning the plan into a resilient decision graph, rather than a fragile one-shot instruction list. 

We recommend that for high-critical or extensive planning tasks, developers consider encoding such fallback logic during planning, either through conditionally linked nodes or alternate execution branches that are activated based on runtime signals. In doing so, the P-t-E paradigm gains a valuable middle ground: not just rigid upfront planning or expensive full re-plans, but intelligent local adaptation built into the plan itself. 

## **7.3 Calibrating Trust: The Role of Human-in-the-Loop (HITL) Verification** 

Deploying LLM agents in real-world applications requires a carefully calibrated level of trust between the human user and the AI system. Research has shown that agents can be a “double-edged sword” (He et al., 2025). They are immensely capable, but they can also be “convincingly wrong”, generating plans, code, or factual statements that appear plausible, confident, and well-structured but are fundamentally incorrect or logically flawed (He et al., 2025). This can mislead users into placing unwarranted trust in a faulty agent. 

Human-in-the-Loop (HITL) verification is the primary mechanism for mitigating this risk and calibrating user trust. However, empirical studies show that the effectiveness of HITL depends heavily on where in the workflow it is applied (He et al., 2025). 

**User-Involved Planning** Contrary to intuition, directly involving a user in the initial planning phase does not consistently lead to better plans. In some cases, users can be swayed by the LLM’s confident but incorrect suggestions and may even introduce new errors while trying to “help” modify the plan (He et al., 2025). The risk of being misled by a “convincingly wrong” plan is high at this stage. 

**User-Involved Execution** HITL is far more beneficial during the execution phase. When presented with a specific, concrete action and its outcome (e.g., “The agent is about to send this email. Approve?”), users are effective at catching specific errors, correcting faulty tool outputs, and preventing undesirable actions. This is particularly true for tasks with higher complexity or risk (He et al., 2025). 

Based on these findings, the recommended architectural pattern for many critical systems is **Automatic Planning + User-Involved Execution** (He et al., 2025). This leverages the LLM’s strength in generating a comprehensive initial strategy while using the human’s superior judgment to supervise the tactical execution of each step. As discussed previously, this can be further strengthened for the highest-risk scenarios by evolving the pattern to **Plan-Validate-Execute** , where an expert human must approve the automatically generated plan _before_ any execution begins, providing a crucial safeguard against acting on a fundamentally flawed strategy. 

## **7.3.1 HITL vs Automated Verification** 

While human review provides a strong safeguard against flawed reasoning, it does not always scale, particularly in automated or low-risk workflows. To address this, we could augment the architecture with an automated Verifier agent (see Section 1), a distinct module responsible for validating the Planner’s output before execution begins. This pattern could extend P-t-E into a Plan-Validate-Execute loop, where validation occurs independently of planning and execution. 

As mentioned, the Verifier can be instantiated as another LLM (with a different prompt or model), a rulebased engine, or a symbolic checker. Its role is to inspect the plan for logical coherence, policy compliance, and alignment with system constraints. This introduces a layer of redundancy and cross-checking that helps mitigate issues like overconfidence or hallucination in the Planner’s output. 

This pattern aligns with recent architectural advances such as the use of dedicated **process verifiers** , agents that review intermediate reasoning steps to ensure progress toward a goal, rather than trusting the planner’s 

17 

output wholesale. For example, this paper (Setlur et al., 2024) introduces a similar idea, demonstrating how separate verifier agents can guide and validate structured reasoning processes. 

Incorporating a Verifier improves system safety without requiring human oversight for every single task. In enterprise or compliance-sensitive contexts, it also creates an internal audit checkpoint, making failures easier to diagnose and trust boundaries easier to enforce. 

## **7.4 Architectural Weaknesses: The Cost of Upfront Planning** 

While the Plan-then-Execute pattern offers significant advantages in predictability, security, and reasoning quality for complex tasks, it is not without its architectural weaknesses, particularly concerning initial latency and cost-efficiency. These trade-offs stem directly from its defining feature of comprehensive upfront planning. 

## **7.4.1 Upfront Latency and “Time-to-First-Action”** 

The most immediate drawback of the P-t-E pattern is its initial response time. Before the agent can perform its first action, it must make a call to a powerful planner LLM and wait for the entire multi-step plan to be generated. This planning phase can introduce significant latency, making the pattern feel slower to the end-user compared to more reactive approaches (Patten, 2025). A ReAct agent, in contrast, performs a much quicker initial reasoning step and can execute its first tool call almost immediately. For applications where a fast “time-to-first-action” is critical, the P-t-E pattern’s initial planning overhead is a distinct disadvantage. 

## **7.4.2 High Token Consumption in the Planning Phase** 

The comprehensive nature of the planning phase often leads to higher initial token consumption. The prompt sent to the planner must contain the full user objective, detailed instructions, and tool definitions. The resulting plan can be lengthy and verbose. For complex tasks, this single planning call can consume a large number of tokens, sometimes between 3,000 and 4,500, which can be more than a ReAct agent might use for an entire simple task (Patten, 2025). This front-loaded cost can be a significant concern for costsensitive applications, especially if many of the tasks are simple enough that they do not warrant such an extensive planning investment. 

**Hierarchical Planning through Sub-Planners** While the conventional P-t-E architecture introduces a single Planner responsible for generating the full execution roadmap, in more complex or cost-sensitive workflows, this responsibility can be distributed across multiple planning layers. An architectural extension involves introducing sub-planners - smaller, purpose-specific planning agents that handle discrete segments of the overall task. In this hierarchical model, the primary **Planner first generates a high-level blueprint by decomposing the user’s objective into broad milestones or phases** . These milestones are then delegated to sub-planners, which operate independently or in parallel to develop detailed plans for their assigned segments. This design offers several advantages. First, it reduces upfront token costs (as sub-planners operate with narrower context windows and more focused objectives), avoiding a monolithic, memory-heavy planning prompt. Second, it enhances modularity and reusability; sub-planners can be specialized for domain-specific planning (e.g., data preprocessing, API integration, or report generation), allowing for targeted optimization or fine-tuning. Finally, it introduces a natural failure containment boundary: if one sub-plan is flawed or requires re-planning, only that segment needs regeneration, preserving the rest of the execution logic and improving overall system resilience. This hierarchical approach could extend the P-t-E pattern from a linear, centralized planning model to a distributed, scalable planning ecosystem more suitable for real-world, multi-agent applications. 

## **7.4.3 Risk of Wasted Effort and Sequential Bottlenecks** 

The upfront investment in planning carries the risk of being entirely wasted. If the initial plan is flawed or an early step fails in an unrecoverable way (and the system lacks a re-planning loop), the time and tokens spent on generating the full plan are lost. Furthermore, in its basic form, the P-t-E pattern executes its plan 

18 

sequentially (LangGraph, 2025). This creates an unnecessary performance bottleneck if the plan contains independent tasks that could have been executed in parallel. While advanced implementations using DAGs can mitigate this, the standard linear execution model remains a potential weakness (LangGraph, 2025). 

Ultimately, the P-t-E pattern’s cost and latency profile represent a strategic trade-off. It front-loads the computational expense with the expectation that this will lead to a more efficient and successful overall execution for complex, multi-step workflows (Singh, 2025b). However, for simpler tasks or scenarios where initial responsiveness is paramount, this upfront cost can become a significant architectural liability, making a more iterative pattern like ReAct a more suitable choice (Patten, 2025). 

## **8 Strategic Recommendations for Implementation** 

The successful deployment of secure and reliable LLM agents requires a combination of architectural theory, security-first principles, and practical framework knowledge. The choice of a reasoning pattern and implementation framework is a critical decision with long-term consequences for a project’s flexibility, scalability, and security posture. This final section provides a consolidated framework selection matrix and a strategic architectural blueprint to guide architects, developers, and security engineers in building production-grade Plan-then-Execute agents. 

## **8.1 Framework Selection Matrix: Matching Tools to Use Cases** 

The choice between LangGraph, CrewAI, and AutoGen. depends on the specific priorities of the project. Each framework offers a different set of abstractions and trade-offs for implementing the P-t-E pattern. A comparative analysis to aid in this strategic decision is provided in Appendix B.3. 

## **8.2 Architectural Blueprint for Secure, Production-Grade Agents** 

Regardless of the chosen framework, a set of core architectural principles should guide the development of any secure, production-grade agentic system. This report’s key findings are summarized in the following recommendations, forming an actionable blueprint. 

1. **Default to Plan-then-Execute:** For any task that is non-trivial or involves more than one or two tool calls, the Plan-then-Execute pattern should be the default high-level architecture. Its inherent predictability, control, and resistance to control-flow hijacking make it a more suitable foundation for reliable systems than purely reactive patterns. 

2. **Embrace Defense-in-Depth:** No single pattern is a silver bullet (Masood, 2025). A robust security posture is achieved by layering multiple controls. The P-t-E pattern must be combined with a comprehensive set of complementary security measures, including: 

   - **Strict Input Sanitization and Output** Filtering to protect the data plane. 

   - **The Principle of Least Privilege** applied rigorously to tool access, ideally at the task or step level. 

   - **Strongly Sandboxed Execution** for any code generation capabilities, with Docker being the industry standard. 

3. **Design for Resilience with Re-planning:** A static plan is a brittle plan. Production systems must be able to handle unexpected failures and adapt. Architect the workflow to include a replanning loop that allows the agent to assess failures in the context of its overall goal and formulate a new strategy. 

4. **Implement Risk-Appropriate Human Oversight:** Calibrate the level of human involvement based on the risk and criticality of the agent’s tasks. 

   - For low-risk tasks, fully autonomous operation may be acceptable. 

19 

   - For medium-risk or irreversible actions, implement **User-Involved Execution** , requiring human approval for specific steps. 

   - For high-stakes, mission-critical systems, adopt the **Plan-Validate-Execute** pattern, where an expert human must validate the agent’s entire plan before any execution is permitted. 

5. **Ensure Comprehensive Auditability:** The ability to understand why an agent took a certain action is critical for debugging, compliance, and trust. Implement robust, structured logging for all significant events, including the initial user request, the generated plan, each tool call with its inputs and outputs, any re-planning decisions, and the final response. Observability platforms like LangSmith are invaluable for tracing these complex execution paths (Lan, 2025). 

Ultimately, the challenge of building secure LLM agents is a systems architecture problem, not merely a model-tuning problem. By moving beyond attempts to make the LLM itself infallible and instead focusing on building a resilient and constrained architectural framework around it, we can harness the power of these models. By applying proven engineering principles of security, modularity, fault tolerance, and resilience, developers and architects can construct powerful, effective, and trustworthy agentic systems capable of tackling real-world challenges. 

## **References** 

Langchain-ai/langgraph. LangChain, August 2025. 

- Engineer’s Guide to Data & AI/ML. LangGraph Simplified: Understanding Conditional edge using Hotel Guest Check-In Process, June 2025. 

- AutoGen. Conversation Patterns | AutoGen 0.2. https://microsoft.github.io/autogen/0.2/docs/tutorial/conversationpatterns/, 2025. 

Autogen. Group Chat — AutoGen. https://microsoft.github.io/autogen/dev//user-guide/core-userguide/design-patterns/group-chat.html, 2025. 

AutoGen. Group Chat with Coder and Visualization Critic | AutoGen 0.2. https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_vis/, 2025. 

Autogen. Group Chat with Customized Speaker Selection Method | AutoGen 0.2. https://microsoft.github.io/autogen/0.2/docs/notebooks/agentchat_groupchat_customized/, 2025. 

Abid Ali Awan. AutoGen Tutorial: Build Multi-Agent AI Applications. https://www.datacamp.com/tutorial/autogen-tutorial, 2025. 

CrewAI. Custom Manager Agent. https://docs.crewai.com/en/learn/custom-manager-agent, 2025a. 

CrewAI. Customize Agents. https://docs.crewai.com/en/learn/customizing-agents, 2025b. 

CrewAI. Hierarchical Process. https://docs.crewai.com/en/learn/hierarchical-process, 2025c. 

CrewAI. Tasks. https://docs.crewai.com/en/concepts/tasks?utm_source=chatgpt.com, 2025. 

Shibsankar Das and Lucia Cordero Sanchez. How to Build an LLM Agent With AutoGen: Step-by-Step Guide. https://neptune.ai/blog/building-llm-agents-with-autogen, 2025. 

Deep Charts. Build a "Plan and Execute" AI Agent Workflow with LangGraph, March 2025. 

fabkosta. How does LangChain actually implement the ReAct pattern on a high level?, November 2023. 

GraphQL. GraphQL | A query language for your API. https://graphql.org/, 2025. 

Harang. Securing LLM Systems Against Prompt Injection. https://developer.nvidia.com/blog/securing-llmsystems-against-prompt-injection/, August 2023. 

20 

- Hawkins. Every Token Counts: Building Efficient AI Agents with GraphQL and Apollo MCP Server | Apollo GraphQL Blog. https://www.apollographql.com/[post], 2025. 

- Gaole He, Gianluca Demartini, and Ujwal Gadiraju. Plan-Then-Execute: An Empirical Study of User Trust and Team Performance When Using LLM Agents As A Daily Assistant. In _Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems_ , number 414, pp. 1–22. Association for Computing Machinery, New York, NY, USA, April 2025. ISBN 979-8-4007-1394-1. 

- Eoin Hinchy. Beyond the hype: How security leaders can build AI agents that matter | Cybersecurity Dive. https://www.cybersecuritydive.com/spons/beyond-the-hype-how-security-leaders-can-build-aiagents-that-matter/751647/, 2025. 

- Romin Irani. Tutorial : Multi-Agent interactions with Autogen and Gemini — Part 7: Sequential Chat, October 2024. 

- Matthew Konsinski. Protect Against Prompt Injection | IBM. https://www.ibm.com/think/insights/preventprompt-injection, April 2024. 

LangChain. Plan-and-Execute Agents. https://blog.langchain.com/planning-agents/, February 2024. 

- langchain-ai. Langchain/cookbook/plan_and_execute_agent.ipynb at master _·_ langchain-ai/langchain. https://github.com/langchain-ai/langchain/blob/master/cookbook/plan_and_execute_agent.ipynb, 2025a. 

- langchain-ai. Langchain-ai/langgraph _·_ Discussions. https://github.com/langchain-ai/langgraph/discussions, 2025b. 

- LangGraph. Plan-and-Execute. https://langchain-ai.github.io/langgraph/tutorials/plan-and-execute/planand-execute/, 2025. 

- Evan Li, Tushin Mallick, Evan Rose, William Robertson, Alina Oprea, and Cristina Nita-Rotaru. ACE: A Security Architecture for LLM-Integrated App Systems, May 2025. 

- Manika. How to Build an AI Agent with CrewAI? https://www.projectpro.io/article/build-an-ai-agentwith-crewai/1095?utm_source=chatgpt.com, 2025. 

- Adnan Masood. The Sandboxed Mind — Principled Isolation Patterns for Prompt-Injection-Resilient LLM Agents, June 2025. 

- Andrew Y. Ng. Agentic Design Patterns Part 4: Planning. https://www.deeplearning.ai/the-batch/agenticdesign-patterns-part-4-planning/, April 2024. 

Visakh Padmanabhan. Plan-and-Execute in LangChain: Handling Complexity with Structure, June 2025. 

Dave Patten. LLM Security & Safe Prompt Engineering, March 2025. 

Christian Posta. Mitigating Indirect Prompt Injection Attacks on LLMs | Solo.io. https://www.solo.io/blog/mitigating-indirect-prompt-injection-attacks-on-llms, 2025. 

Simone Russo. Tool Best Practice: Assign to Agent or Task? - General. https://community.crewai.com/t/tool-best-practice-assign-to-agent-or-task/5919, May 2025. 

Harpreet Sahota. Plan-and-Execute Agents in Langchain, December 2023. 

- Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal, Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning. In _The Thirteenth International Conference on Learning Representations_ , October 2024. 

21 

- Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, and Yueting Zhuang. HuggingGPT: Solving AI tasks with chatgpt and its friends in hugging face. In _Proceedings of the 37th International Conference on Neural Information Processing Systems_ , NIPS ’23, pp. 38154–38180, Red Hook, NY, USA, December 2023. Curran Associates Inc. 

- Ozdemir Sinanu. Oreilly-ai-agents/notebooks/LangGraph_Plan_Execute.ipynb at main _·_ sinanuozdemir/oreilly-ai-agents. https://github.com/sinanuozdemir/oreilly-aiagents/blob/main/notebooks/LangGraph_Plan_Execute.ipynb, 2025. 

- Satbir Singh. LLM-Based Agents: The Benefits and the Risks | Enkrypt AI. https://www.enkryptai.com/blog/llm-agents-benefits-risks, https://www.enkryptai.com/blog/llmagents-benefits-risks, 2025a. 

- Shubham Kumar Singh. Plan and Execute: AI Agents Architecture, 2025b. URL `https://medium.com/ @shubham.ksingh.cer14/plan-and-execute-ai-agents-architecture-f6c60b5b9598` . 

- Yogi Srivastava. Security planning for LLM-based applications. https://learn.microsoft.com/enus/ai/playbook/technology-guidance/generative-ai/mlops-in-openai/security/security-plan-llmapplication, 2025. 

- sugarforever. AutoGen-Tutorials/autogen_rag_agent.ipynb at main _·_ sugarforever/AutoGen-Tutorials. https://github.com/sugarforever/AutoGen-Tutorials/blob/main/autogen_rag_agent.ipynb, 2025. 

- Nick T. (Ph.D.). CrewAI’s Task Tool vs. Agent Tool: The differences you MUST Know. https://ai.plainenglish.io/crewais-task-tool-vs-agent-tool-the-differences-you-must-know-f466262951a0, September 2024. 

- TeeTracker. CrewAI / Hierarchical Manager: Build Reflection Enabled Agentic, March 2025. 

- Tereza Tizkova. Microsoft’s AutoGen - A guide to code-executing agents — E2B Blog. https://e2b.dev/blog/microsoft-s-autogen. 

- Simon Willison. Design Patterns for Securing LLM Agents against Prompt Injections. https://simonwillison.net/2025/Jun/13/prompt-injection-design-patterns/, 2025. 

- Vanna Winland, Meredith Syed, and Anna Gutowska. What is crewAI? | IBM. https://www.ibm.com/think/topics/crew-ai, October 2024. 

- Feiwang Zheng and Chao Wang. Tracing with AutoGen — Prompt flow documentation. https://microsoft.github.io/promptflow/tutorials/trace-autogen-groupchat.html, 2025. 

## **A Code Examples** 

## **A.1 LangGraph Plan-and-Execute Agent** 

```
importos
importoperator
fromtypingimportTypedDict ,Annotated ,List ,Tuple ,Union
fromlangchain_core .pydantic_v1importBaseModel ,Field
fromlangchain_core .promptsimportChatPromptTemplate
fromlangchain_openaiimportChatOpenAI
fromlanggraph.graphimportStateGraph ,END
fromlanggraph.prebuiltimportcreate_react_agent
fromlangchain_core .toolsimporttool
#---1.DefineTools---
#Defineafewdistincttoolstodemonstratesecurityscoping .
```

```
@tool
```

22 

```
defweb_search(query:str)->str:
""" Performsawebsearchforthegivenquery ."""
#Inarealimplementation ,thiswouldcallasearchAPI.
print(f"---ExecutingWebSearchfor:{query}---")
if"weather"inquery.lower ():
return"TheweatherinSanFranciscois65ÂřFandsunny."
elif"capitaloffrance"inquery.lower ():
return"ThecapitalofFranceisParis."
return"Norelevantinformationfound."
@tool
defwrite_file(filename:str ,content:str)->str:
""" Writesthegivencontenttoafile."""
print(f"---Writingtofile:{ filename }---")
withopen(filename ,"w")asf:
f.write(content)
returnf" Successfullywroteto{ filename }."
@tool
defcalculate(expression:str)->str:
""" Calculatestheresultofamathematicalexpression ."""
print(f"---Calculating :{ expression }---")
try:
result=eval(expression ,{" __builtins__ ":{}},{})
returnf"Theresultis{result}."
exceptExceptionase:
returnf"Errorduringcalculation :{e}"
#Masterlistofallavailabletools
all_tools=[web_search ,write_file ,calculate]
tool_map={t.name:tfortinall_tools }
#---2.DefineGraphState---
#Thestateobjectthatwillbepassedbetweennodes .
classPlanExecuteState (TypedDict):
input:str
plan:List[dict]#Eachdictwillhave’task ’and’tool_name ’
past_steps:Annotated],operator.add]
response:str
#---3.DefinePlannerandExecutorLogic---
#Pydanticmodelsforstructuredoutputfromtheplanner
classPlanStep(BaseModel):
task:str=Field(description="Thedetaileddescriptionofthesub -tasktoperform.")
tool_name:str=Field(description =f"Thesingle ,mostappropriatetooltouseforthis
taskfromtheavailabletools:{[t.name
fortinall_tools]}")
classPlan(BaseModel):
"""Acomprehensive ,step -by -stepplantoachievetheuser ’sobjective ."""
steps:List=Field( description ="Thesequenceofstepstoexecute.")
#PlannerNode
defplanner_node (state:PlanExecuteState ):
"""
Generatesaplanwithaspecifictoolassignedtoeachstep.
"""
print("---Planning ...---")
prompt=ChatPromptTemplate . from_template (
""" Forthegivenobjective ,createadetailed ,step -by -stepplan.
Foreachstep ,specifythesingletoolfromtheavailablelistthatisbestsuited
toperformthetask.
Objective :{input}
AvailableTools:{tools}"""
)
planner_llm=ChatOpenAI(model="gpt -4o",temperature =0)
structured_planner=planner_llm . with_structured_output (Plan)
```

23 

```
plan_result=structured_planner .invoke({
"input":state["input"],
"tools":",".join([t.namefortinall_tools])
})
#ConvertPydanticmodelstosimpledictsforstatecompatibility
plan_as_dicts=[{"task":step.task ,"tool_name":step.tool_name }forstepin
plan_result .steps]
return{"plan":plan_as_dicts }
#ExecutorNode
defexecutor_node (state:PlanExecuteState ):
"""
ExecutesthenextstepintheplanusingONLYthespecifiedtoolforthatstep.
"""
plan=state["plan"]
past_steps=state["past_steps"]
iflen( past_steps)>=len(plan):
return{"response":"Finishedallplannedsteps."}
current_step_dict=plan[len(past_steps)]
task_description=current_step_dict ["task"]
tool_name=current_step_dict ["tool_name"]
print(f"---ExecutingStep{len(past_steps )+1}:{ task_description }---")
print(f"---SecurityConstraint:UsingONLYtool’{ tool_name }’---")
#SecurityEnhancement :Provideonlythesingle ,specifiedtooltotheexecutoragent.
iftool_namenotintool_map:
result=f"Error:Tool’{ tool_name }’notfound.Availabletools:{list(tool_map.keys
())}"
else:
scoped_tool=tool_map[tool_name]
#Createatemporary ,single -toolagentforthisstep
executor_agent_llm=ChatOpenAI (model="gpt -4o -mini",temperature =0)
agent_executor=create_react_agent (executor_agent_llm ,[ scoped_tool ])
#Createarichpromptfortheexecutoragent
executor_prompt=f""" Youareataskexecutor .Yourgoalistocompletethe
followingtask.
Task:’{ task_description }’
Todothis ,youhaveaccesstoONLYONEtool:’{ scoped_tool .name} ’.
Previousstepshavebeencompletedandtheirresultsareavailableifneeded ,but
youshouldfocusonthecurrenttask.
Historyofpaststeps:{ past_steps }
Executethetaskusingtheprovidedtool.
"""
result=agent_executor .invoke({"messages":[("user",executor_prompt )]})
result=result.get("messages",[{}])[-1].content
return{"past_steps":[(current_step_dict ,result)]}
#ConditionalEdgeLogic
defshould_continue (state:PlanExecuteState ):
"""
Determineswhethertocontinueexecutingtheplanortoend.
"""
iflen(state["past_steps"])>=len(state["plan"]):
returnEND
return"executor"
```

24 

```
#---4.ConstructtheGraph---
workflow=StateGraph( PlanExecuteState )
workflow.add_node("planner",planner_node )
workflow.add_node("executor",executor_node )
workflow. set_entry_point ("planner")
workflow.add_edge("planner","executor")
workflow. add_conditional_edges (
"executor",
should_continue ,
)
app=workflow. compile ()
#---5.RuntheAgent---
if__name__=="__main__":
#SetyourOpenAIAPIkey
#os. environ [" OPENAI_API_KEY "]=" your_api_key_here "
objective="WhatistheweatherinSanFrancisco ,andwhatis100*5?Writethefinal
answerstoafilenamed’results.txt ’."
config={" recursion_limit ":50}
final_state=app.invoke({"input":objective },config=config)
print("\n---FinalResult---")
print(f"FinalResponse:{ final_state .get(’response ’)}")
print("ExecutionHistory:")
forstep ,resultinfinal_state [’past_steps ’]:
print(f"-Step:{step[’task ’]}(Tool:{step[’tool_name ’]})->Result:{result}")
```

## **A.2 CrewAI Manager-Worker Crew** 

```
importos
fromcrewaiimportAgent ,Task ,Crew ,Process
fromcrewai_toolsimportSerperDevTool ,FileWriterTool
#---1.SetupEnvironment---
#SetAPIkeysforrequiredservices .
#os. environ [" OPENAI_API_KEY "]=" YOUR_OPENAI_API_KEY "
#os. environ=" YOUR_SERPER_API_KEY "
#---2.DefineTools---
#Definethetoolsthatwillbeavailable .
search_tool=SerperDevTool ()
file_writer_tool=FileWriterTool ()
#---3.DefineWorkerAgents( Executors )---
#Theseagentsarespecialistsdoingtheactualwork.
#ResearcherAgent
researcher=Agent(
role="SeniorTechnologyResearcher ",
goal="Discovercutting -edgedevelopmentsinAIandmachinelearning.",
backstory=""" Youarearenownedresearcheratatop -tiertechnologylab.
Yourexpertiseliesinidentifyingemergingtrendsandexplainingtheirsignificance .
Youhaveaknackforfindingthemostrelevantandimpactfulinformation .""" ,
verbose=True ,
#ThisagentCANNOTdelegate .
allow_delegation =False ,
#Thisdefinestheagent ’sfullpotentialtoolkit .
tools=[search_tool]
)
```

25 

```
#WriterAgent
writer=Agent(
role="TechnicalContentStrategist ",
goal="Craftcompellingandclearcontentfromtechnicalresearchfindings.",
backstory=""" Youareaprofessionaltechnicalwriterknownforyourability
todistillcomplextopicsintoaccessibleandengagingarticles .
Youareskilledatstructuringinformationlogicallyandwritingtoafile.""" ,
verbose=True ,
allow_delegation =False ,
#Thisagent ’spotentialtoolkitincludesthefilewriter .
tools=[ file_writer_tool ]
)
#---4.DefineManagerAgent( Planner )---
#Thisagent ’sroleistoplananddelegatetaskstotheworkers .
manager=Agent(
role="ResearchProjectManager",
goal=" Efficientlymanagetheresearchandwritingprocesstoproduceahigh -quality
report.",
backstory=""" Youareanexperiencedprojectmanager ,skilledinoverseeingcomplex
researchprojects .Yourroleistobreakdownthemaingoalintoactionabletasks
anddelegatethemtotheappropriateteammembers ,ensuringasmoothworkflow
andafinaloutputthatmeetsallrequirements .""" ,
verbose=True ,
#ThemanagerMUSTbeabletodelegate .
allow_delegation =True
)
#---5.DefineTaskswithScopedTools---
#Definetheunitsofwork.Crucially ,wescopethetoolsatthetasklevelforsecurity .
#Task1:Research
#Thistaskisassignedtotheresearcheragent .
research_task=Task(
description=""" ConductathoroughsearchforthelatestadvancementsinLargeLanguage
Model(LLM)agents .
Focusonthe’Plan -then - Execute ’architecturalpattern .Identifyatleast3keybenefits
and3keysecurityconsiderations .""" ,
expected_output ="Adetailedreportsummarizingthefindings ,includingbenefitsand
securityconsiderations .",
agent=researcher ,
#SECURITY :Eventhoughtheresearcheragentisdefinedwiththesearch_tool ,
#weexplicitlyscopethistasktoONLYusethesearch_tool .
#Iffile_writer_toolwereintheagent ’slist ,itwouldbeinaccessibleforthistask.
tools=[search_tool]
)
#Task2:Write
#Thistaskisassignedtothewriteragent .
write_task=Task(
description=""" Usingtheresearchreportprovided ,writeaconcisesummaryofthe
findings .
Thesummaryshouldbewell -structured ,clear ,andsavedtoafilenamed’
llm_agents_report .md ’.""" ,
expected_output ="Thefinalsummarycontentwrittentothefile’llm_agents_report .md ’.",
agent=writer ,
#SECURITY :Thistaskisstrictlylimitedtousingthefile_writer_tool .
#Thewriteragentcannotperformawebsearchduringthistask ,evenifithadthetool
.
tools=[ file_writer_tool ],
#Specifytheoutputfileforthistask.
output_file=’llm_agents_report .md’
)
#---6.InstantiatetheCrewwithHierarchicalProcess---
#Thecrewisconfiguredwiththemanagerandthehierarchicalprocess .
crew=Crew(
agents=[researcher ,writer],#Theworkeragents .
```

26 

```
tasks=[research_task ,write_task],#Thetaskstobecompleted .
manager_agent =manager ,#Thedesignatedplanner .
process=Process. hierarchical#Enablesthemanager -ledP-t-Eworkflow .
)
```

```
#---7.KickofftheCrew ’sWork---
if__name__=="__main__":
result=crew.kickoff ()
print("\n\n ######################## ")
print("##CrewExecutionResult:")
print(" ########################\ n")
print(result)
```

## **A.3 AutoGen Planner-Executor Group** 

```
importos
importautogen.
#---1.SetupEnvironmentandLLMConfig---
#EnsureyouhaveaDockerdaemonrunning .
#SetyourOpenAIAPIkey ,forexample :
#os. environ [" OPENAI_API_KEY "]=" your_api_key_here "
config_list=autogen. config_list_from_json (
" OAI_CONFIG_LIST ",
filter_dict={"model":["gpt -4o"]},
)
llm_config={" config_list ":config_list ,"timeout":120}
#---2.DefineAgents---
#PlannerAgent:Createstheplan.
planner=autogen. AssistantAgent (
name="Planner",
system_message =""" Youareameticulousplanner .Yourgoalistocreateastep -by -step
Pythonscripttosolvetheuser ’srequest .
Donotwritethefullcodeyourself .Instead ,provideaclear ,numberedplanofwhatthe
codeshoulddo.
Forexample :
1.Importnecessarylibraries(e.g.,pandas ,matplotlib ).
2.Loadthedatafromthegivensource .
3.Performtherequiredanalysisorvisualization .
4.Printorsavethefinalresult .
Concludeyourplanwiththephrase’Plancomplete .’forthenextagenttotakeover.""" ,
llm_config=llm_config ,
)
#CoderAgent:WritesPythoncodebasedontheplan.
coder=autogen. AssistantAgent (
name="Coder",
system_message =""" YouareaPythonprogrammer .Youwillbegivenaplan.
Yourtaskistowriteasingle ,completePythonscripttoexecutethatplan.
Ensurethescriptisself - containedandreadyforexecution .
Donotaskforconfirmation .WritethecodedirectlyinaPythoncodeblock .
Ifyouneedtofixcodebasedonanerror ,providethefull ,correctedscript .""" ,
llm_config=llm_config ,
)
#ExecutorAgent:Executesthecodeinasecureenvironment .
#SECURITY :ThisagentisconfiguredtoexecutecodewithinaDockercontainer .
executor=AutoGen .. UserProxyAgent (
name="Executor",
human_input_mode ="NEVER",
code_execution_config ={
"work_dir":" autogen_coding ",
" use_docker":True ,#Thisisthecriticalsecuritysetting .
```

27 

```
},
```

```
)
```

```
#---3.DefineCustomSpeakerSelectionLogicforP-t-E---
defcustom_speaker_selection_func ( last_speaker :AutoGen.Agent ,groupchat:autogen.GroupChat)
:
"""AcustomfunctiontoenforcethePlan->Code->Executeworkflow ."""
messages=groupchat.messages
#Ifthechatjuststarted ,thePlannerbegins .
iflen(messages)<=1:
returnplanner
#IfthePlannerjustspokeandfinishedtheplan ,theCodertakesover.
iflast_speaker .name=="Planner":
if"Plancomplete."inmessages[-1][’content ’]:
returncoder
else:#Plannerneedstocontinueplanning
returnplanner
#IftheCoderjustprovidedascript ,theExecutorrunsit.
eliflast_speaker .name=="Coder":
returnexecutor
#IftheExecutorjustranthecode ,checkforerrors .
eliflast_speaker .name=="Executor":
#Iftherewasanerror ,theCoderneedstofixit.
if"exitcode:1"inmessages[-1][’content ’]or"Error:"inmessages[-1][’content ’]:
returncoder
else:
#Ifsuccessful ,thetaskisdone.
returnNone#Terminatethechat
else:
returnNone#Terminatebydefault
#---4.CreatetheGroupChatandManager---
groupchat=autogen.GroupChat(
agents=[planner ,coder ,executor],
messages=,
max_round=10 ,
speaker_selection_method = custom_speaker_selection_func
```

```
)
```

```
manager=autogen. GroupChatManager (groupchat=groupchat ,llm_config =llm_config )
```

```
#---5.InitiatetheChat---
if__name__=="__main__":
objective="Plotabarchartofthepopulationsofthe5mostpopulouscountriesinthe
worldandsaveittoafilenamed’
population_chart .png ’."
#Theexecutoragentwillinitiatethechat ,butthecustomselectionfunction
#willimmediatelypasscontroltothePlanner .
executor. initiate_chat (
manager ,
message=objective ,
)
```

28 

|**Metric**|**ReAct Pattern**|**Plan-then-Execute**<br>**Pat-**|**Best For**|
|---|---|---|---|
|||**tern**||
|Core Loop|Iterative: Thought _→_Action|Sequential: Plan _→_[Execute|P-t-E is better for structured,|
||_→_Observation|_→_Observe]*|predictable workfows.|
|Task<br>Com-|Low to Medium.<br>Excels at|High.<br>Excels at complex,|P-t-E is superior for orchestrat-|
|plexity|simple, direct tasks.|multi-step, dependent tasks.|ing long chains of actions.|
|LLM Calls|One LLM call per action.|One LLM call per plan (or re-|P-t-E is more efcient for tasks|
|||plan).|with many steps.|
|Typical Cost|Lower for short tasks; scales|Higher upfront cost for plan-|P-t-E ofers better cost control|
||linearly and can become high.|ning; scales sub-linearly.|for complex operations.|
|Adaptability|High. Adapts its strategy af-|Low (without re-planning).|ReAct is better for highly dy-|
||ter every single step.|The plan is fxed upfront.|namic or unpredictable environ-|
||||ments.|
|Predictability|Low. The agent’s path can be|High. The entire sequence of|P-t-E is essential for systems re-|
||emergent and hard to predict.|actions is known in advance.|quiring auditable and reliable be-|
||||havior.|
|Security (In-|More vulnerable.<br>Malicious|More resilient. Control fow is|P-t-E provides a strong architec-|
|direct Injec-|tool output can hijack the|locked before tool execution.|tural defense against prompt in-|
|tion)|next thought.||jection.|
|Error Recov-|Prone to getting stuck in|More robust, especially when|P-t-E with re-planning ofers su-|
|ery|loops without sophisticated|combined with a re-planning|perior resilience.|
||handling.|loop.||



Table 1: Comparison of ReAct vs Plan-then-Execute patterns. 

|**Threat**||**Description**|**Primary Mitigation (via**|**Essential Complementary**|
|---|---|---|---|---|
|**Vector**|||**P-t-E)**|**Controls**|
|Indirect||Malicious instructions in|P-t-E Control-Flow Integrity:|Input Sanitization,<br>Output|
|Prompt|In-|tool outputs hijack agent’s|Plan is fxed before ingesting|Filtering, Dual LLM Pattern.|
|jection||reasoning loop.|untrusted tool data, prevent-||
||||ing logic hijacking.||
|Unauthorized||Agent is tricked into using|N/A<br>(P-t-E<br>alone<br>doesn’t|Principle of Least Privilege:|
|Tool Use||a tool that is inappropri-|scope tools).|Tools are scoped to the spe-|
|||ate for the current task.||cifc task or step, not the|
|||||agent globally.|
|Privilege|Es-|Agent is coerced into per-|P-t-E Plan Review: The plan|Human-in-the-Loop<br>(HITL)|
|calation||forming a high-privilege,|can be audited before execu-|Approval: Mandatory human|
|||irreversible action.|tion to spot risky steps.|sign-of for critical actions.|
|Malicious||Agent generates and runs|P-t-E Plan Review: The plan|Sandboxed Execution:<br>All|
|Code Execu-||harmful code on the host|to generate code can be au-|code execution must occur in|
|tion||system.|dited before execution.|an isolated environment, like|
|||||a Docker container.|
|Data<br>Exfl-||Agent is tricked into send-|P-t-E Plan Review: The plan|Output<br>Filtering,<br>Network|
|tration||ing sensitive internal data|can be audited for steps that|Egress Controls, Data Loss|
|||to an external entity.|involve outbound communi-|Prevention (DLP) systems.|
||||cation.||



Table 2: Threat vectors, mitigations via Plan-then-Execute, and complementary controls. 

29 

## **B Tables** 

- **B.1 Table 1: ReAct vs. Plan-then-Execute - A Comparative Analysis** 

- **B.2 Table 2: Security Threat Mitigation with Plan-then-Execute and Complementary Patterns** 

- **B.3 Table 3: Framework Implementation Comparison for Plan-then-Execute** 

|**Dimension**|**Dimension**|**Dimension**|**LangGraph**|**CrewAI**|**AutoGen**|
|---|---|---|---|---|---|
|Core|Abstrac-||State<br>Graph:<br>Low-level,|Crew: High-level abstraction|Conversation:<br>Flexible or-|
|tion|||explicit control over state,|of Agents, Tasks, and a man-|chestration of dialogues be-|
||||nodes, and edges.|aged Process.|tween conversable agents.|
|Planning||Mech-|Custom Planner Node:<br>De-|Hierarchical Manager Agent:|Planner Agent in a Governed|
|anism|||veloper implements a func-|A<br>designated<br>agent<br>with|Chat:<br>A specialized agent|
||||tion that calls an LLM to gen-|`allow_delegation=True`|whose role is to plan within|
||||erate the plan.|acts as the planner.|a custom conversational fow.|
|Execution||Con-|Executor Node:<br>A function|Worker<br>Agents<br>executing|Executor Agent in a Gov-|
|trol|||that executes one step, of-|Tasks:<br>Specialized<br>agents|erned Chat: An agent (often|
||||ten using a temporary ReAct|are delegated specifc, pre-|a `UserProxyAgent`) executes|
||||agent.|defned tasks.|code or tool calls as a turn in|
||||||the conversation.|
|Re-planning|||Natively Supported:<br>Cyclic|Possible via Logic: Requires|Possible via Custom Flow:|
||||graph<br>structure<br>makes<br>re-|custom logic within the Man-|Requires designing the cus-|
||||planning loops a frst-class|ager Agent to re-evaluate and|tom speaker selection logic to|
||||citizen.|re-delegate tasks.|loop back to the planner on|
||||||certain conditions.|
|Tool|Scoping||Programmatic: Must be im-|Declarative: A core feature.|Via Agent Capabilities: Tools|
|(Least||Privi-|plemented manually in the|`Task.tools`provides explicit,|are<br>generally<br>tied<br>to<br>the|
|lege)|||executor node by dynamically|granular control, overriding|agent; requires careful agent|
||||providing tools.|`Agent.tools`.|design or custom logic to|
||||||scope.|
|Execution||Sand-|Manual Implementation: De-|Manual Implementation: De-|Built-in<br>Support:|
|boxing|||veloper is responsible for in-|veloper is responsible for en-|`code_execution_config`|
||||tegrating<br>sandboxing<br>(e.g.,|suring tools that execute code|with `use_docker=True` pro-|
||||Docker).|do so safely.|vides<br>a<br>frst-class,<br>secure|
||||||sandboxing mechanism.|
|Best For|||Maximum<br>Flexibility<br>and|Rapid<br>Development<br>and|Complex Agent-to-Agent In-|
||||Control:<br>Ideal for complex,|Clarity: Excellent for quickly|teractions:<br>Best for scenar-|
||||bespoke workfows requiring|building robust multi-agent|ios where the workfow is best|
||||fne-grained<br>control<br>over|systems with clear, role-based|modeled as a sophisticated,|
||||state and logic, and for build-|specializations<br>and<br>strong,|multi-party conversation with|
||||ing resilient,<br>self-correcting|declarative security for tools.|dynamic turn-taking.|
||||agents.|||



Table 3: Comparison of LangGraph, CrewAI, and AutoGen. across key dimensions. 

30 

