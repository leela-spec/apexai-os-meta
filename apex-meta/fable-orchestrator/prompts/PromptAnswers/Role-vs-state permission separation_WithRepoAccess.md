
## 1. Decision table

| Permission model | Authority carried by | Failure class it prevents | Failure class it **cannot** prevent | Real system/paper exhibiting this | Adoption cost in a file-based Claude Code system |
|---|---|---|---|---|---|
| **Role/tool partitioning** | Agent identity plus runtime tool allow/deny rules | A planning or review agent directly using mutation tools it was not granted. Claude Code permission rules are enforced by the runtime rather than by prompt obedience, and `PreToolUse` hooks can deterministically deny calls. citeturn545495search1turn545495search5turn545495search6 | **Object-authority errors:** an authorized reader or writer treating an unreviewed, rejected, or stale artifact as authoritative. Tool permission says *who may act*, not *which lifecycle version of an artifact may justify that action*. **Inference from the permission model.** | **Framework docs:** Claude Code subagents, permissions and hooks. Subagents provide isolated contexts and specialized instructions; runtime configuration controls their tools. citeturn545495search0turn545495search11 | **Already paid / low.** This is effectively System B. |
| **Role/task assignment without durable lifecycle state** | Named agent role, assigned task and attached tools | Responsibility confusion and accidental use of tools that were not attached to the assigned task. CrewAI tasks explicitly identify the responsible agent and required tools. citeturn527714search20 | Premature promotion, stale dependency use and self-attestation. A “reviewer” role does not mechanically prove that the exact current candidate was reviewed. **Inference.** | **Framework docs:** CrewAI Crews, agents and tasks. | **Low.** Similar to the current skill contracts, but adds no missing protection. |
| **Handoff/topology-based authority** | Currently active agent, its tools, handoff graph and tool guardrails | Keeps specialist capabilities bounded and determines whether control remains with an orchestrator or transfers to a specialist. OpenAI distinguishes handoffs, where the specialist takes over, from agents-as-tools, where the orchestrator retains control. citeturn960956search11turn960956search13 | Handoff completion does not establish that an artifact is reviewed, current or canonical. Agent-level input/output guardrails also do not automatically run around every intermediate tool call; OpenAI documents that tool guardrails are required for that coverage. citeturn896178search0turn896178search20 | **Framework docs:** OpenAI Swarm used Agents plus handoffs; the production Agents SDK retains tools, handoffs and guardrails. citeturn960956search0turn960956search4turn896178search4 | **Low–medium.** Maps cleanly to ephemeral Claude subagents, but still requires a separate object-authority rule. |
| **State/graph-controlled workflow** | Shared graph state, node logic and conditional edges | Out-of-order execution, missing approval pauses and unsafe continuation after a rejected action—provided those conditions are encoded. LangGraph persists state and supports interrupts for approval, review, edit and rejection before continuing. citeturn330688search0turn330688search1turn330688search2 | A node may write an incorrect state or self-assert that verification passed. Graph state provides a control substrate, not an inherent trust model. **Inference from the framework mechanics.** | **Framework docs:** LangGraph `StateGraph`, checkpointers and interrupts. | **High if imported wholesale.** Requires graph runtime, checkpoint semantics and migration of Markdown work items into graph execution. |
| **Agent roles plus constrained transition graph** | Specialized agents/tools plus allowed speaker or execution transitions | Invalid agent ordering, uncontrolled speaker selection and some retry-loop errors. AutoGen GraphFlow supports structured sequential, parallel, conditional and looping execution; AG2 supports explicit valid speaker transitions and state-oriented routing. citeturn527714search0turn527714search6turn527714search10turn527714search16 | A correctly ordered agent can still consume an unverified or stale artifact unless artifact authority is itself represented in the graph state. **Inference.** | **Framework docs:** AutoGen GraphFlow and AG2 FSM/StateFlow. | **Medium–high.** Adds transition definitions and runtime machinery beyond Claude Code skills and files. |
| **Roles inside a stateful Flow** | Flow state and execution path outside; roles and tools inside each Crew step | Uncontrolled task order and loss of application state. CrewAI recommends a Flow for production structure, state and logic, with autonomous Crews embedded in bounded Flow steps. citeturn527714search17turn527714search23turn527714search26 | The Flow does not automatically know that `candidate.md` is unverified; developers must encode that object attribute and route condition. **Inference.** | **Framework docs:** CrewAI Flow + Crew hybrid. | **Medium–high.** Conceptually useful, but adopting the runtime would duplicate the existing file-backed orchestrator. |
| **ABAC-style object authority** | Subject role, requested operation, **object attributes** and optionally environment attributes | The exact gap in role-only control: the same session writer may be authorized to write one artifact but forbidden from promoting another because its lifecycle attribute is `candidate` or `invalidated`. NIST defines ABAC as evaluating subject, object, operation and environment attributes together. citeturn740520search1turn740520search5 | It does not prove semantic correctness. A bad or sycophantic verifier can still assign the wrong attribute. | **Security standard:** NIST SP 800-162. **Mapping to APEX is an inference.** | **Low–medium.** One YAML object and one deterministic check on the existing write path. |
| **Workflow-synchronized authorization / continuous usage control** | Current task or lifecycle state, with privileges granted, revoked or re-evaluated as state changes | Stale authority that survives before or after the task that justified it. Workflow authorization literature explicitly grants privileges at task start and revokes them at completion; UCON adds ongoing checks and mutable attributes. citeturn740520search2turn740520search6turn740520search3turn740520search7 | Reviewer error, correlated model bias and semantically weak evidence. It controls when authority exists, not whether the underlying judgment is correct. | **Security papers:** workflow authorization model and UCON. | **Medium for one object attribute; high for full continuous authorization.** |
| **Full BUILD/VERIFY/LOCK lifecycle** | Role identity plus an enforced state machine on every work item | Self-promotion, silent substantive rewrites during review, and writes against locked material—**if every read, write and promotion path actually enforces the state**. The historical APEX design intended this candidate/canon separation and prohibited self-promotion, but it remained prose rather than running enforcement. fileciteturn3file0 fileciteturn3file2 | Correlated reviewers, sycophantic agreement and false PASS judgments. Research shows LLM evaluators can favor their own generations, while multi-agent discussions can reinforce rather than critically challenge earlier answers. citeturn472891search0turn472891search1turn472891search5 | **Historical APEX design**, analogous to workflow authorization/FSM approaches. | **High.** Requires transition ownership, handling rules for every command, migration of all existing items and recovery semantics. It is disproportionate to the demonstrated gap. |

## 2. Strongest break-scenario against the current answer

### Scenario: an unverified KB candidate becomes the authority for a confirmed durable decision

1. **Research produces a candidate.**  
   A research subagent writes `candidate-routing-rule.md`. It has valid YAML, expected headings and plausible citations, but its synthesis is semantically thin: it overstates one source and omits a contradictory source. This is the project’s existing “structurally complete but semantically ungrounded” failure class; the APEX lifecycle test explicitly warns that headings, frontmatter, lint or file creation do not establish usability. fileciteturn3file1

2. **The candidate has no lifecycle attribute.**  
   It is simply a readable repository file. Nothing identifies it mechanically as `candidate`, `verified` or `invalidated`.

3. **The planning skill consumes it.**  
   `apex-plan` reads the file and proposes a project-level routing change. It does not mutate state, so its role contract is respected.

4. **The compute skill propagates it.**  
   `apex-sync` computes dependencies and consequences from the proposed plan. It does not author the plan or write confirmed mutations, so its contract is also respected.

5. **Role separation does not force a review of the exact artifact version.**  
   A nominal reviewer might never run, or might review an earlier version. Even when another LLM reviews it, separate role labels alone do not guarantee adversarial independence: self-preference and inter-agent sycophancy are documented failure modes. citeturn472891search0turn472891search1

6. **The session skill presents the final mutation.**  
   The operator sees a concise and plausible proposal to update `decisions.md`. The operator confirms the change. The request contains:

   ```yaml
   operator_validation: confirmed
   no_implicit_apply: true
   ```

7. **All existing gates pass.**  
   The session script generates a dry-run, the diff touches only the intended file, and the confirmed write succeeds.

8. **The candidate has now indirectly become canon.**  
   Every role boundary was obeyed. The single write path was used. Operator confirmation was present. The deterministic diff was correct. The failure was not unauthorized mutation; it was **authorized mutation based on an artifact that lacked current authority**.

9. **A later correction exposes the defect.**  
   The original candidate is found to be ungrounded or superseded, but the accepted decision has already propagated through plans and dependencies. Recent agent-memory research documents the related failure: models can retrieve updated evidence yet continue acting on an implicitly invalidated earlier state. citeturn472891search2turn472891search6

### Why the current gate cannot prevent it

`operator_validation` answers:

> Did the operator authorize this proposed mutation?

It does not answer:

> Were all artifacts used to justify the mutation independently reviewed, still byte-identical to what was reviewed, and not invalidated by newer evidence?

That second question is an **object-state authorization question**. Static role partitioning cannot answer it because the relevant property belongs to the artifact, not the session agent.

A mechanized BUILD/VERIFY/LOCK system would block the promotion while the candidate remained in BUILD. But the full machine is unnecessary: one enforced authority attribute supplies the specific missing fact.

## 3. Recommendation

### **Verdict (b): add a minimal state field to every work item—not a full machine.**

The decision-change bar is cleared.

The break-scenario is concrete, compatible with all current role prohibitions, compatible with operator confirmation, and compatible with dry-run-first mutation. It is blocked by an artifact-level state because the write depends on an object whose authority is `candidate`, not `verified`.

The correct model is a small ABAC hybrid:

```text
subject role
+ requested operation
+ artifact authority state
+ current verification basis
= permission decision
```

Do **not** restore the general BUILD/VERIFY/LOCK machine. Current orchestration frameworks use graph or flow state where ordering and lifecycle genuinely matter, but none establishes that every artifact needs a universal three-stage workflow. Anthropic’s engineering guidance also favors the simplest composable pattern that solves the demonstrated problem rather than importing a complex framework by default. citeturn545495search3turn896178search3

The new field should remain distinct from `operator_validation`:

- **`authority.state`**: may this artifact be treated as authoritative input?
- **`operator_validation`**: may this particular mutation be applied?

Both must pass for canon-changing writes.

This field prevents **missing review, review of the wrong version, stale verification and use of explicitly invalidated material**. It does not prevent a verifier from making a bad judgment. No state machine does; evaluator self-preference and agent sycophancy remain review-quality risks. citeturn472891search0turn472891search1

## 4. Exact YAML fields and one enforcement surface

```yaml
authority:
  state: candidate | verified | invalidated
  basis_digest: null | "sha256:<64-hex-digest>"
  verification_ref: null | "<repository-relative-review-artifact-path>"
```

### Transition rules

```yaml
authority_transition_rules:
  on_create:
    state: candidate
    basis_digest: null
    verification_ref: null

  on_content_or_declared_evidence_change:
    state: candidate
    basis_digest: null
    verification_ref: null

  candidate_to_verified:
    allowed_only_when:
      - "verification_ref resolves to an independent review artifact"
      - "review verdict is pass"
      - "reviewer identity or run identity differs from the creator identity or run"
      - "review basis_digest equals the current deterministic digest"
    result:
      state: verified

  candidate_or_verified_to_invalidated:
    allowed_when:
      - "review verdict is fail or needs_revision"
      - "a governing source contradiction is recorded"
      - "the stored basis_digest no longer matches the current item and declared evidence closure"

  invalidated_to_candidate:
    allowed_only_after:
      - "substantive revision or evidence update"
    result:
      state: candidate
      basis_digest: null
      verification_ref: null

  canon_changing_write:
    allowed_only_when:
      - "operator_validation is confirmed"
      - "every authoritative input in the mutation dependency closure has authority.state verified"
      - "every stored basis_digest matches the current content and declared evidence closure"
```

`basis_digest` should be computed deterministically from the canonicalized work-item content plus the content hashes of its declared evidence and dependency references. This binds the review to the exact artifact and evidence version rather than merely recording that “someone reviewed something.”

### ONE enforcement surface

**A schema-and-transition check inside the existing `apex-session` write script.**

Before producing or applying any canon-changing mutation, that single checker must:

1. validate the `authority` object;
2. validate the requested state transition;
3. recompute and compare `basis_digest`;
4. resolve `verification_ref` and require a passing independent verdict;
5. traverse the declared authoritative-input closure;
6. reject the mutation if any dependency is not currently `verified`.

Do not add a separate lifecycle engine or git hook. Keeping enforcement in the existing exclusive write path preserves System B’s strongest property—one mechanized mutation surface—while adding the one object-state fact that role partitioning cannot represent.