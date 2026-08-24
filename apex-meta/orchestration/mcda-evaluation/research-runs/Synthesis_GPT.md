# Synthesis: the decision has narrowed substantially

The independent runs are useful, but their raw rankings should **not** be averaged. They were based on different snapshots, different interpretations of “complete system,” and in several cases materially different evidence quality.

The central conclusion after reconciling the repo research with current primary sources is:

> **Do not build another custom Master of Arts orchestration architecture.**
> 
> The most promising pattern is now a **thin, durable CLI control plane + repo-local, pinned Agent Skills + Git as canonical knowledge/artifact substrate**.
> 
> The current best hypothesis is **Hermes Kanban as the control plane**, with commercially usable upstream skill packages installed into the repo. **Spec Kit + GitHub** is the strongest deterministic control. **OpenClaw core** is the strongest knowledge-heavy challenger. A newly discovered **Babysitter** ecosystem deserves one bounded wildcard check because it already ships deterministic cross-agent orchestration _and_ a surprisingly broad business-agent/process library.

I would **not select production yet**. I would stop broad architecture research and move to a tightly controlled bake-off designed to eliminate uncertainty that can actually change the ranking.

---

# 1. First: use MCDA, but not the way we previously used it

Our earlier analyses often used weighted scorecards. That is useful for orientation, but formal MCDA is more disciplined.

Current HM Treasury guidance explicitly warns against simple “importance × score” MCA because it can create false precision. Proper MCDA uses **swing weighting**: criteria get weight based both on how important they are **and how much the candidates actually differ on them**. It then requires sensitivity analysis and switching values. ([GOV.UK](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026 "https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026"))

NASA's decision-analysis guidance adds the other important part: prototypes, human-in-the-loop testing and user evaluation are legitimate decision tools, and **uncertainty should only be reduced when reducing it could plausibly change the ranking**. ([NASA](https://www.nasa.gov/reference/6-8-decision-analysis/ "https://www.nasa.gov/reference/6-8-decision-analysis/"))

So the efficient decision process is:

**Hard gates → shortlist → evidence-adjusted MCDA → sensitivity/switching analysis → only decision-changing pilots → final decision.**

Not:

**research → more research → bigger architecture → custom implementation → discover it does not work.**

That distinction is particularly important here.

---

# 2. What the independent researchers actually found

|Research run|Original winner|What remains valid|What needs correction|
|---|---|---|---|
|**AntiG_DR**|Gas City 92.3; Politik 73.4; Hermes 69.8|Correctly emphasized existing packaged multi-agent workflows|Gas City is explicitly a coding-factory system; Politik fails maturity/adoption; Hermes analysis is stale|
|**Gemini**|Spec Kit + GitHub 89.05|Strong evidence for deterministic resumable workflows, gates and GitHub portability|Underestimates the newer Hermes/OpenClaw control planes and treats specialist ecosystem too narrowly|
|**CC / Perplexity**|GitHub + BMAD + Agent Skills 65.6|Very important insight: compose proven specialist skills around a durable repo|Researcher explicitly could not read the authoritative repo files, reducing confidence in its fit assessment|
|**ChatGPT run**|OpenClaw 89.5; Hermes+BMAD 87.7|Correctly identified current OpenClaw memory/Workboard and Hermes Kanban evolution|Over-credited ClawHub as a safe specialist marketplace; security evidence requires a stricter skill-sourcing policy|

The Gemini result remains useful as the **deterministic-control argument**. The CC result remains useful as the **portable-skill-layer argument**. The AntiG result identified a real autonomy architecture, but its Gas City and Politik conclusions do not survive the stronger hard gates.

---

# 3. The important corrections

## Gas City: real system, wrong default target

Gas City is powerful. But its own current materials describe it as an orchestration SDK for **multi-agent coding workflows**, and its packs encode things like BMAD PRD → architecture → stories → implementation → adversarial code review.

That is precisely the sort of system that looks transferable by analogy but risks forcing us to invent the MoA translation layer ourselves.

Given the principle **reuse before invention**, it should therefore be:

**later autonomy challenger**, not production favorite.

Its entry condition should be: _our selected core demonstrably cannot run unattended parallel work reliably enough_.

---

## Politik: remove from the shortlist

The AntiG recommendation was interesting architecturally, but current adoption evidence is nowhere near the “battle-proven ecosystem” threshold.

It should be removed rather than piloted.

---

## Hermes: substantially stronger than several researchers realized

Current Hermes is no longer adequately described as “one agent plus delegation.”

Its current skill system explicitly supports the open Agent Skills format, project skills, shared `.agents/skills/`, arbitrary external skill directories, Git-backed skill taps, progressive disclosure and security scanning. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/?utm_source=chatgpt.com "Skills System | Hermes Agent"))

Its current Kanban system adds durable task state, dependencies, named execution profiles, review/request-changes loops, retries, human unblock/comment, scheduled starts, audit history and multi-agent assignment. The current docs even use **parallel researchers → analyst → writer** as an intended workload.

That is extremely close to the operating primitive MoA needs.

Hermes also supports ChatGPT/Codex subscription OAuth directly; OpenRouter is **not required**. Local/self-hosted endpoints remain available. The current Anthropic subscription route is much less attractive because Hermes documents Claude Pro as unsupported and Claude Max usage as consuming purchased extra credits rather than the base allowance. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/integrations/providers?utm_source=chatgpt.com "AI Providers | Hermes Agent"))

This pushes Hermes sharply upward.

---

## OpenClaw: core is stronger; marketplace should be treated separately

OpenClaw's current **core** is impressive.

Workboard provides durable SQLite cards, dependencies, claims, retries/attempts, proof/artifact references, review/blocked states, decomposition, dispatch and Codex/Claude execution. But OpenClaw itself explicitly says Workboard is intentionally small and **not a replacement for GitHub Issues, Linear or Jira**. ([OpenClaw](https://docs.openclaw.ai/plugins/workboard "https://docs.openclaw.ai/plugins/workboard"))

Its native memory system is stronger than Hermes' default knowledge story: SQLite-backed BM25 + vector hybrid retrieval, deterministic recency/importance ranking and MMR. ([OpenClaw](https://docs.openclaw.ai/concepts/memory-builtin "https://docs.openclaw.ai/concepts/memory-builtin"))

It can also run ChatGPT/Codex subscription OAuth without separate OpenAI API billing. ([OpenClaw](https://docs.openclaw.ai/providers/openai "https://docs.openclaw.ai/providers/openai"))

But **ClawHub must not be conflated with OpenClaw core**. OpenClaw itself warns that third-party skills are untrusted code and supports local/Git installs plus install-policy enforcement. ([OpenClaw](https://docs.openclaw.ai/skills "https://docs.openclaw.ai/skills")) More importantly, Palo Alto Unit 42 found malicious skills that survived ClawHub's VirusTotal/ClawScan screening during 2026. ([Unit 42](https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/ "https://unit42.paloaltonetworks.com/openclaw-ai-supply-chain-risk/"))

Therefore:

> **OpenClaw remains a serious candidate, but no ClawHub skill should be trusted merely because it is in ClawHub.**

For MoA, use only pinned Git/local skills whose source we have inspected.

---

# 4. The biggest thing all four research runs underweighted: portable skill libraries

This is potentially more important than discovering another orchestration engine.

## BMAD is more useful than “software methodology” implies

BMAD now produces project-local `SKILL.md` packages for agents, workflows, tasks and tools. ([BMAD Method](https://docs.bmad-method.org/reference/commands/ "https://docs.bmad-method.org/reference/commands/"))

Its current core includes:

- `bmad-deep-recon`: decision-grade research on **any subject**, including literature, market, domain, user voice and competitor analysis;
    
- `bmad-review`: multi-lens review of documents and artifacts, not only code;
    
- `bmad-brainstorming`;
    
- `bmad-forge-idea`;
    
- `bmad-party-mode`. ([BMAD Method](https://docs.bmad-method.org/reference/core-tools/ "https://docs.bmad-method.org/reference/core-tools/"))
    

Deep Recon persists source-grounded research to disk and supports refresh/deepen instead of restarting the research. ([BMAD Method](https://docs.bmad-method.org/zh-cn/explanation/deep-recon/ "https://docs.bmad-method.org/zh-cn/explanation/deep-recon/"))

The Creative Intelligence Suite adds Innovation Strategist, Design Thinking Coach and Brainstorming Coach agents. ([BMAD Method](https://docs.bmad-method.org/reference/modules/ "https://docs.bmad-method.org/reference/modules/"))

And BMAD itself is MIT licensed.

**Verdict:** strong production-usable workflow/skill donor.

---

## MarketingSkills is an unusually good match for MoA

Corey Haines' MarketingSkills is much more than copywriting.

It contains prebuilt skills for content strategy, copywriting/editing, customer research, social, video, offers, pricing, launches, marketing loops, community, SEO, analytics, CRO, email, sales enablement and more. It explicitly supports Claude Code, Codex and any Agent Skills-compatible runtime.

It can install straight into `.agents/skills/` and is MIT licensed.

This maps extraordinarily well to W4 content/public communication and parts of W5 product/offer.

**Verdict:** very high-priority production skill pack.

---

## Product-Manager-Skills: technically excellent, licensing problem

This was a very useful discovery.

It currently advertises **77 skills + six workflow commands**, with workshop facilitation, autonomous investigation, market intelligence, discovery, business health, pricing, stakeholder analysis, agent orchestration and multiple structured workshop skills.

It explicitly packages for Codex and other Agent Skills clients.

But the same current README says **CC BY-NC-SA 4.0**.

For a commercial MoA organization, I would therefore classify it:

**excellent research/reference source; do not incorporate into production until commercial-use permission is clarified.**

This is exactly why licensing belongs in the hard gates.

---

## Anthropic's official skill repo: high trust, narrower direct reuse

Anthropic's official Agent Skills repository is extremely mature and provides useful enterprise/communication examples. But Anthropic explicitly says some skills are Apache-2.0 while its document-generation skills are merely source-available rather than open source.

So use it selectively according to each skill's license rather than treating the entire repo as reusable production code.

---

# 5. A genuinely new out-of-the-box candidate: Babysitter

This one deserves separate attention because **none of the four original researchers surfaced it**.

`a5c-ai/Babysitter` is MIT licensed and explicitly designed to enforce deterministic multi-agent processes with gates and an immutable journal. Its current runtime supports twelve agent harnesses, including Codex, Claude Code, Gemini, Hermes and OpenClaw, although several integrations are currently beta/experimental.

More interestingly, it already contains a large **business** domain tree:

- business analysis;
    
- business strategy;
    
- customer experience;
    
- decision intelligence;
    
- digital marketing;
    
- entrepreneurship;
    
- finance/accounting;
    
- HR;
    
- knowledge management;
    
- legal;
    
- marketing;
    
- operations;
    
- procurement and more.
    

Its business-analysis module contains actual agents including:

**management consultant, process expert, risk analyst, stakeholder expert, training designer, workshop facilitator, financial analyst and QA analyst.**

It also ships a real `workshop-facilitation` `SKILL.md`, not merely a theoretical extensibility claim.

And its business-analysis specialization contains existing processes such as consulting engagement planning, business-case development, change-readiness assessment and hypothesis-driven analysis.

### Why I am _not_ immediately making it #1

It was only created in January 2026 and currently has roughly 1.7k GitHub stars. Its library is broad, but breadth is not proof that its hundreds of business assets have been battle-tested in real organizations.

There is also substantially more runtime machinery than Hermes.

So:

> **Babysitter is the mandatory wildcard, not the provisional winner.**

If its _existing_ processes fit our user stories without modifying their code, it could jump sharply upward.

---

# 6. Revised complete-system ranking

These are **pre-pilot synthesis scores**, not “scientific truth.” I have deliberately penalized custom glue, unverified marketplaces, external API dependence, licensing problems and software-only adaptation more heavily than some earlier researchers did.

|Rank|Architecture|Synthesis|Confidence|Recommendation|
|--:|---|--:|:-:|---|
|**1**|**Hermes Kanban + repo-local pinned Agent Skills**|**~90/100**|B+|**Primary pilot**|
|**2**|**Spec Kit + GitHub + same pinned skill layer**|**~88–89**|A-/B+|**Deterministic control pilot**|
|**3**|**Hermes native/bundled only**|**~87–88**|B+|**Simplicity control**|
|**4**|**OpenClaw core + Workboard + builtin memory + pinned Git/local skills, no ClawHub**|**~86–89**|B|**Knowledge-heavy challenger**|
|**5**|**Babysitter + existing business specialization library**|**~84 provisional**|C+|**Mandatory wildcard inspection/pilot**|
|**6**|GitHub Issues/Projects + portable skills, human-routed|~83|A|Simplest manual fallback|
|**7**|n8n + GitHub + local model/RAG|~78|A-/B|Downstream automation component|
|**8**|Dify + GitHub|~77|B|Knowledge-app/HITL component|
|**9**|Beads + repo skills|~76|B|Agent-task-graph specialist|
|**10**|Ruflo + GitHub|~74|B|Too much operational surface|
|**11**|Gas City + packs|~71|B|Coding/autonomy factory only unless pilot proves transfer|
|—|Politik|**hard fail**|—|Insufficient maturity/adoption|
|—|CrewAI / LangGraph / AutoGen / Agno|component|—|Good construction frameworks; require us to author too much|
|—|BMAD / Superpowers / OpenSpec / Task Master standalone|donor|—|Valuable modules, not complete MoA OS|

### Sensitivity

The top result is relatively stable:

- **Reuse/CLI-first:** Hermes + pinned skills leads.
    
- **Autonomy-first:** Hermes remains strongest; Babysitter becomes more interesting.
    
- **Knowledge-first:** OpenClaw moves upward because of native hybrid memory.
    
- **Simplicity/security-first:** Hermes and Spec Kit improve; OpenClaw drops.
    
- **Maximum deterministic workflow-first:** Spec Kit becomes highly competitive with Hermes.
    

So I would not spend another research cycle debating #1 versus #2.

We can measure it.

---

# 7. Ranking by Master of Arts use case

|Use case|#1|#2|#3|Reason|
|---|---|---|---|---|
|**Weekly CEO operating cycle**|**Hermes Kanban**|Spec Kit + GitHub|OpenClaw Workboard|Hermes already has durable tasks, profiles, dependencies, review/change and scheduling|
|**Research → evidence → knowledge**|**Hermes + BMAD Deep Recon**|OpenClaw + pinned research skill|Spec Kit + BMAD|BMAD already supplies research/verification workflow; OpenClaw has superior native retrieval|
|**Workshop creation**|**Hermes + existing workshop/creative skills**|Babysitter existing business library|Spec Kit + same skills|Babysitter's shipped workshop facilitator/training designer is particularly interesting here|
|**Coaching/method formalization**|**Hermes + BMAD/CIS + MoA canon**|Spec Kit|Babysitter|No mature upstream system fully captures MoA's unique embodied/coaching method; canonical MoA knowledge remains necessary|
|**Content / website / social**|**Hermes + MarketingSkills**|Spec Kit + MarketingSkills|OpenClaw + MarketingSkills|MarketingSkills already covers most of the pipeline without us inventing agents|
|**Offer/pricing/market testing**|**Hermes + MarketingSkills/BMAD**|Spec Kit|Babysitter|Existing offer/pricing/research methods already exist|
|**Admin / SaaS integration**|**Selected core + n8n**|OpenClaw automation|Hermes scripts/cron|n8n is excellent here, but should be a tool beneath the OS, not the OS|
|**Private/sensitive MoA work**|**Hermes + local/Codex + pinned skills**|Spec Kit + trusted CLI|OpenClaw core without ClawHub|Fewest uncontrolled external components|
|**Knowledge-heavy source retrieval**|**OpenClaw builtin memory**|Hermes + repo retrieval/qmd-style skill|Dify RAG|This is OpenClaw's strongest differentiator|
|**Leela software precursor**|**Spec Kit + BMAD**|Hermes + BMAD|Gas City later|Software/spec pipelines are where Spec Kit/BMAD/Gas City are natively strongest|
|**Very high autonomy / long parallel factory**|**Hermes first**|Babysitter|Gas City|Gas City enters only if simpler systems actually hit an autonomy ceiling|

---

# 8. The architecture I would test first

Not build. **Test.**

```text
MasterOfArts Git repository
│
├── canonical knowledge / sources / final artifacts
│
├── .agents/skills/
│   ├── selected BMAD skills
│   ├── MarketingSkills
│   ├── selected commercially-usable upstream skills
│   └── eventually only truly-MoA-specific skills
│
└── Hermes
    ├── Kanban = active workflow/task state
    ├── profiles = worker/reviewer roles
    ├── Agent Skills = methods
    ├── Codex/ChatGPT OAuth = primary subscription executor
    ├── local model = sensitive/cheap tasks where viable
    └── human review = CEO gates
```

Hermes explicitly supports pointing at shared `.agents/skills/` directories, so the skills can remain **repo-visible and runtime-portable** rather than becoming Hermes-private configuration. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/?utm_source=chatgpt.com "Skills System | Hermes Agent"))

That is a crucial architectural property.

### What I would _not_ add initially

No OpenRouter.

No custom RAG server.

No vector database unless retrieval testing proves it necessary.

No custom MoA orchestration DSL.

No Beads.

No n8n until a concrete SaaS automation needs it.

No custom “40-agent company.”

No duplicated Hermes Kanban → GitHub Issues synchronization.

No ClawHub packages.

And no custom MoA specialist simply because we can imagine one.

---

# 9. The actual decision experiment

This is the part that I think should replace further broad research.

## Gate 0 — licensing / installability / unchanged reuse

Before running a workflow, eliminate anything that requires us to fork or rewrite upstream assets.

Each shortlisted skill/process gets:

|Test|Required outcome|
|---|---|
|Commercial license|Allowed, or explicit permission obtained|
|Install into repo|Yes|
|No private marketplace state required|Yes|
|Usable by ≥2 executor families unchanged|Preferably yes|
|No mandatory OpenRouter/API aggregator|Yes|
|Source pinned to version/commit|Yes|
|No bespoke adapter|**Zero**|
|Security inspection|Pass|

BMAD and MarketingSkills currently look good here. Product-Manager-Skills does **not** currently pass the licensing gate.

Babysitter needs a deeper asset-level check before promotion.

---

## Pilot 1 — Research → knowledge

Run the **same real MoA research question** through:

**A. Hermes + pinned skills**  
**B. Spec Kit + GitHub + the exact same skills**  
**C. OpenClaw + the exact same pinned Git/local skills**

Use the same executor where technically possible—ideally Codex subscription—to prevent “better model” from contaminating the framework comparison.

Deliberately kill/interupt each run once.

Measure:

|Metric|Operational definition|
|---|---|
|**Upstream reuse**|% of semantic process performed by unchanged upstream skills/workflows|
|**Custom glue**|number of new runtime/adaptor/workflow files written solely to make stack function|
|**Human intervention**|manual actions excluding planned CEO gates|
|**Context transfer**|copy/paste or manual context handoffs|
|**Recovery**|can it restart without chat reconstruction?|
|**Review independence**|reviewer receives bounded artifact/evidence rather than maker's hidden chat|
|**Evidence quality**|unsupported claims caught / citations retained|
|**Knowledge promotion**|accepted result becomes retrievable without copying it manually|
|**State duplication**|same state represented in multiple systems|
|**Data egress**|every external provider receiving private task content|
|**Incremental cost**|cost outside already-paid subscriptions/local compute|
|**Operator comprehensibility**|can you understand status without reading agent chatter?|

This produces far more useful information than another 100-page research report.

---

## Pilot 2 — Weekly CEO cycle

Only the **top two from Pilot 1** continue.

Give them real portfolio state and test:

```text
read portfolio
→ find blocked/stale/dependent work
→ continue routine work autonomously
→ surface only consequential decisions
→ accept operator decisions
→ resume work
→ produce next CEO brief
```

This is where Hermes either proves the Kanban advantage or loses to GitHub/Spec Kit's superior human visibility.

---

## Pilot 3 — Workshop → content

Again, top two only.

```text
existing MoA research
→ workshop draft
→ independent review
→ CEO choice
→ final workshop
→ website/article content
→ social/video derivatives
→ portfolio updated
→ accepted learning retained
```

This simultaneously tests W3, W4 and W5 and is intentionally **non-software**.

If a framework handles research beautifully but falls apart here, it is not the MoA OS.

---

# 10. Where the Babysitter wildcard enters

Before Pilot 1 I would perform **one bounded source inspection**:

> Does Babysitter already contain an existing, unmodified process sufficiently close to one of US-A / US-B / US-D?

If **yes**, run that existing process in parallel as **Candidate D**.

If it requires us to start writing a bespoke JavaScript orchestration process, drop it immediately.

This is the right “out-of-the-box” test:

> We are not asking _can Babysitter build our system?_  
> We are asking _has Babysitter already built enough of our system that we can simply use it?_

Its existing `workshop-facilitation` skill, workshop-facilitator and training-designer agents make that question worth answering.

---

# 11. Explicit switching conditions

This is more useful than arguing over 90.5 versus 88.5 points.

|Current favorite|It loses if…|
|---|---|
|**Hermes + skills**|third-party project skills do not execute cleanly; CEO visibility is poor; Kanban needs lots of manual intervention|
|**Spec Kit**|each MoA workflow requires us to hand-author/maintain substantial YAML; GitHub + workflow run state becomes confusing|
|**OpenClaw**|security/gateway burden outweighs retrieval benefit; Workboard forces a second project SSOT|
|**Babysitter**|existing business library is generic/generated rather than operationally robust; MoA requires custom JS processes|
|**Gas City**|essentially already loses unless an autonomy requirement appears that the others demonstrably cannot satisfy|
|**n8n/Dify**|only become core contenders if the business evolves toward application/integration automation rather than agentic knowledge work|

One additional decision rule I would adopt for MoA:

> **If the more sophisticated architecture does not produce a clearly material operational advantage over the simpler one, choose the simpler one.**

Not “technically better.” It should meaningfully reduce operator work, custom configuration, recovery failures, or context waste.

---

# 12. My current recommendation

### **Pilot favorite: Hermes Kanban + pinned repo-local Agent Skills**

The fit with the desired operating model is currently unusually strong:

**durable orchestration + Agent Skills standard + shared `.agents/skills/` + subscription/local models + human review + scheduling + low need for custom infrastructure.**

Use:

- **BMAD** for research, review, structured ideation and selected workflows; MIT. ([BMAD Method](https://docs.bmad-method.org/reference/commands/ "https://docs.bmad-method.org/reference/commands/"))
    
- **MarketingSkills** for content, social, offers, pricing, launch, marketing and related outputs; MIT.
    
- **Babysitter business skills** only after checking whether individual MIT `SKILL.md` assets are portable enough; its workshop assets are particularly promising.
    
- **Product-Manager-Skills** as a research benchmark/reference until the noncommercial license issue is resolved.
    

Use **Codex/ChatGPT subscription OAuth first** for the main cloud executor and local models where privacy or cost makes that preferable. Hermes documents that path directly. ([Hermes Agent](https://hermes-agent.nousresearch.com/docs/integrations/providers?utm_source=chatgpt.com "AI Providers | Hermes Agent"))

### **Deterministic control: Spec Kit + GitHub + the same skills**

This needs to be in the bake-off because its workflow semantics are extremely strong: commands, arbitrary agent prompts, shell, human gates, conditions, loops, fan-out/fan-in and exact persisted resume. ([GitHub](https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md "https://github.com/github/spec-kit/blob/main/docs/reference/workflows.md"))

If Hermes feels too “agent decides what to do next,” Spec Kit may be the safer operating spine.

### **Knowledge challenger: OpenClaw core**

Its memory engine is the strongest integrated knowledge/retrieval story currently found. But use **only Git/local pinned skills** initially and explicitly configure local embeddings for sensitive material rather than relying on default external embeddings. ([OpenClaw](https://docs.openclaw.ai/skills "https://docs.openclaw.ai/skills"))

### **Wildcard: Babysitter**

Do one short evidence/compatibility pass because it may represent the thing the original research question wanted all along: **existing non-software specialists + existing deterministic workflows + cross-CLI execution**. Do not invest in custom Babysitter processes before this is proven.

---

The main change in direction is therefore fairly substantial:

> **I would stop searching for one monolithic “AI company framework.”**
> 
> **The emerging stable unit is the Agent Skill.**
> 
> Pick the smallest control plane that can durably route, resume and review those skills. Keep the skills and organizational knowledge in the repo. Replace runtimes when better ones appear without rewriting the company.

That architecture has a much better chance of surviving the exact failure mode that has repeatedly cost this project time: sophisticated AI-designed infrastructure whose logic looked convincing on paper but had not already proven itself in operation.