Yes. I would run this as a **fix-first, simplify-second** program, with the first wave focused on the broken audit chain, derived-artifact hygiene, and validation coverage before touching larger lifecycle design changes.

text

`apex_kb_remediation_program:   objective:    primary: "fix the high-impact integrity and maintenance gaps first"    secondary: "reduce operator complexity without losing source-grounding and deterministic controls"  sequencing_principle:    - "repair truth and auditability before process simplification"    - "remove repo noise before adding new outputs"    - "validate retrieval harder before changing retrieval architecture"    - "merge lifecycle steps only after deterministic behavior is stable"  execution_style:    - "one bounded step per chat"    - "each step ends with evidence, diff summary, and go/no-go"    - "prefer search/replace patch outputs over large rewrites"    - "avoid semantic page rewrites unless the step explicitly targets them"  iterations:    - step: 1      name: "Restore source custody baseline"      priority: "critical"      why_first: "source-manifest.json is empty, so the formal source custody chain is broken"      targets:        - "apex-meta/kb/claude-code-orchestration-design/manifests/source-manifest.json"        - "phase0 artifacts that should feed the manifest"        - "apex_kb.py manifest/status validation logic if missing"      outputs:        - "populated source-manifest.json"        - "manifest completeness rules"        - "short audit report: manifest repaired / remaining gaps"      done_when:        - "sources array is no longer empty"        - "every compiled page family can be traced to source custody artifacts"        - "status or lint surfaces manifest completeness clearly"     - step: 2      name: "Separate canonical from derived artifacts"      priority: "critical"      why_first: "derived search artifacts are rebuildable and should not create repo bloat or branch friction"      targets:        - ".gitignore or repo ignore policy"        - "derived/search/*.sqlite"        - "derived/search/*.json"        - "derived/search/*.ndjson"        - "derived/search/index-meta.json policy"        - "docs/contracts that currently imply committing derived artifacts"      outputs:        - "ignore policy for derived retrieval artifacts"        - "cleanup/removal plan for committed derived files"        - "canonical-vs-derived file policy note"      done_when:        - "rebuildable artifacts are excluded from canonical version control"        - "team guidance clearly states what is disposable vs canonical"     - step: 3      name: "Stabilize deterministic validation"      priority: "high"      why_first: "S8 showed stale lint noise caused by wiki/index.md mtime behavior"      targets:        - "apex-meta/scripts/apex_kb.py"        - "lint/index freshness rules"        - "references/script-command-contract.md if needed"      outputs:        - "content-hash-based freshness rule"        - "clearer flag-order and command-surface behavior"        - "updated validation contract"      done_when:        - "false-positive stale warnings drop"        - "global flag usage is explicit and consistent"        - "lint results map to real defects, not process noise"     - step: 4      name: "Create real S10 maintenance loop"      priority: "high"      why_first: "maintenance is the missing control plane, and needs_review pages already exist"      targets:        - "lifecycle-state-machine.md"        - "ingest-query-lint-audit-rules.md"        - "acceptance-tests.md"        - "audit/ conventions"      outputs:        - "S10 maintenance contract"        - "needs_review triage rules"        - "review cadence and closure criteria"        - "audit item schema"      done_when:        - "S10 is no longer implied only"        - "needs_review accumulation has explicit handling"        - "open audit items become a managed queue"     - step: 5      name: "Harden retrieval evaluation before changing retrieval tech"      priority: "high"      why_first: "current retrieval evidence is strong for easy known-item queries but weak for paraphrase, broad, and adversarial queries"      targets:        - "apex_kb_retrieval.py query test workflow"        - "outputs/queries/ sample set"        - "acceptance-tests.md"        - "retrieval-contract.md"      outputs:        - "expanded query suite: known-item, paraphrase, broad, adversarial, ambiguous"        - "manual scoring rubric: excellent/good/acceptable/noisy/wrong/missing_critical_page"        - "retrieval evaluation report template"      done_when:        - "retrieval quality is tested beyond title-match queries"        - "BM25 sufficiency or failure is evidenced, not assumed"     - step: 6      name: "Resolve or quarantine weak semantic pages"      priority: "medium-high"      why_now: "after maintenance exists, low-confidence and needs_review pages can be processed systematically"      targets:        - "wiki pages marked needs_review"        - "page confidence and claim labels"        - "query outputs that surface weak pages"      outputs:        - "resolved / downgraded / quarantined page list"        - "rule for excluding or demoting weak pages in retrieval outputs"      done_when:        - "needs_review pages are either fixed, isolated, or clearly signposted"        - "retrieval trust improves"     - step: 7      name: "Simplify the lifecycle"      priority: "medium-high"      why_now: "only simplify once integrity, validation, and maintenance controls are stable"      targets:        - "lifecycle-state-machine.md"        - "SKILL.md"        - "runbook examples"        - "operator-facing docs"      outputs:        - "reduced lifecycle, likely 7-step instead of 10-step"        - "merged deterministic validation/maintenance stage"        - "simplified operator checklist"      done_when:        - "operator no longer needs to manage unnecessary phase distinctions"        - "same protections remain with fewer named steps"     - step: 8      name: "Trim low-value output clutter"      priority: "medium"      why_now: "cleanup should follow policy, not precede it"      targets:        - "log/ retention rules"        - "outputs/queries/ retention rules"        - "audit-only vs canonical vs disposable labels"      outputs:        - "retention policy"        - "archive/delete recommendations"        - "reduced ongoing file clutter"      done_when:        - "future repo growth is controlled"        - "operators know what must persist and what can be regenerated"`

## Work order

The first four steps should come before any bigger redesign because the highest-impact defects are structural, not conceptual: the manifest is empty, derived artifacts are being treated too much like repo citizens, lint has a freshness-noise issue, and S10 maintenance is not yet established.

That means the initial program is: **truth chain -> artifact hygiene -> deterministic stability -> maintenance loop -> harder retrieval eval -> semantic cleanup -> lifecycle simplification -> clutter reduction**.

## Step details

|Step|Main goal|Expected file/process changes|Risk|Output from execution chat|
|---|---|---|---|---|
|1|Repair source custody|Populate `source-manifest.json`, validate linkage to Phase0 and compiled KB|Medium|Patch set, manifest gap report, pass/fail note|
|2|Stop derived artifact drift|Add ignore policy, classify derived/search as rebuildable, remove commit pressure|Low|Patch set, canonical-vs-derived policy note|
|3|Reduce lint noise|Shift freshness toward content/hash logic and clarify CLI behavior|Medium|Patch set, deterministic validation note|
|4|Install S10|Define maintenance queue, `needs_review` handling, audit item flow|Medium|Patch set, maintenance contract, sample audit entry|
|5|Prove retrieval quality properly|Expand test queries and scoring rubric before any vector/hybrid decision|Low|Query-suite spec, scoring sheet, evaluation report shell|
|6|Process weak pages|Fix or quarantine `needs_review` content and clarify retrieval exposure|Medium|page-action list, patch set, retrieval policy update|
|7|Simplify lifecycle|Merge unnecessary stages and reduce operator ceremony|Medium|revised lifecycle doc, operator checklist|
|8|Control output sprawl|Retention rules for `log/`, `outputs/queries/`, audit-only files|Low|retention policy, delete/archive candidates|

## Execution protocol

I recommend we use **one executor chat per step**, with each chat limited to a single bounded objective, explicit file targets, and a mandatory end state of: changed files, unchanged files, evidence, and unresolved questions.

For your workflow, that keeps token load and drift lower, matches your preference for critical steps that build on one another, and gives us a clean feedback loop before the next patch wave.

The outputs from each executor chat should be:

- machine-readable step result block,
    
- minimal patch set in search/replace style,
    
- validation evidence,
    
- rollback note,
    
- recommendation: proceed / revise / stop.
    

## Questions

I need these answers before I draft the executor prompt series:

1. Should the remediation target **only** `s6-phase2-wiki-compile` first, or do you want each step to also include a `main` comparison/merge-readiness check?
    
2. Do you want derived retrieval artifacts to be fully **removed from version control**, or only marked as non-canonical while temporarily kept in-branch for demonstration?
    
3. For Step 1, should the executor be allowed to reconstruct `source-manifest.json` from existing repo evidence only, or can it also revise the manifest schema if the current template is insufficient?
    
4. Do you want me to optimize the next prompts for **GPT browser extended thinking** specifically, with strict token-efficient patch instructions and Q&A checkpoints?