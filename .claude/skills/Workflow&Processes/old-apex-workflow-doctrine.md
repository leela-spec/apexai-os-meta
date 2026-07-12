# Old-Apex Workflow Doctrine

Purpose: supplemental workflow/process-structure doctrine for Workflow&Processes when validating workflow records, sprint structure, and prompt/workflow alignment.
Consumer: Workflow&Processes (workflow_record, sprint_structure_review, prompt_workflow_alignment_review).
Source basis: `apex-meta/kb/old-apex-full-orchestration-agent-kb/sources/primary/managed-agent-kb/special_ops__prompts_workflows/` (ESSENCE.md, BEST_PRACTICES.md, MISTAKES.md, TEMPLATES.md — item IDs cited per entry). Entries validated against the current Workflow&Processes skill contract and kept only where not already covered.

## Best practices

- Rule: Design workflows as bounded, stage-gated, artifact-centered sequences: each stage produces one substantial deliverable or one closed file set, with an explicit gate between stages. Reject broad-autonomy or giant multi-phase structures where gates are named but not sequenced. (PW-BP-003)
- Rule: Every workflow stage gets a source-authority check as a pre-step gate and a verification step as a post-step gate. A stage without a verification exit condition is structurally incomplete. (PW-BP-004)
- Rule: Treat HALT, CLARIFY, failed validation, and split-required conditions as hard routing controls in the workflow structure — they block downstream stages until corrected. Never model them as prose warnings the executor may read past. (PW-BP-011, PW-MK-011)
- Rule: Validate completion against the operator's intended deliverable and requested decision layer, not against artifact existence. Check intended output, exact target, content completeness, and stop condition; if existing content does not answer the requested layer, the gap is the finding. (PW-MK-007, PW-MK-008)
- Rule: Handoffs between chats, agents, or execution lanes must carry: settled decisions, source-authority stack, non-redo list, exact next job, required inputs, risks/holds, and success condition. A handoff missing any of these predicts state loss and redundant rework. (PW-BP-006)
- Rule: Out-of-mode improvements discovered mid-run route to an explicit capture point in the workflow; they are never applied silently inside a closed stage. Application requires a new authorized bounded stage. (PW-BP-005, PW-MK-006)

## Known failure modes

- Avoid: Reporting no-op because a named artifact already exists. Compare operator intent against the artifact contract and current state first; if the intended execution scope is broader than the named artifact, the workflow owes the missing bounded output or a blocking question. (PW-MK-007)
- Avoid: Treating templates or promptflow scaffolds as governance. Templates are construction aids only — they confer no routing, promotion, config, or QA authority; route authority questions to the owning surface. (PW-MK-005)
- Avoid: Workflow stages whose scope contains "and"/"then", whose target is inferred rather than named, or whose inputs are directory-level rather than explicit — these expand into unauthorized targets and scope bleed. One atomic task per stage with exact target and exact input refs. (PW-MK-010)

## Templates worth reusing

- Template: Clean Handoff — sections: what is being continued; settled decisions; authority stack (ranked sources); do-not-redo list; exact next job; required inputs; risks and holds; success condition. (PW-TPL-005)
- Template: Intent/Artifact Contract Check — before declaring completion from file equality or existing-artifact status, record: user intent in plain language; named artifact; intended execution scope; exact output expected; write/mutation permissions; allowed and forbidden source inputs; open questions; stop_if_mismatch: true. If intent and artifact contract disagree, surface the mismatch instead of executing or no-op'ing. (PW-TPL-006)
- Template: Improvement Opportunities Not Applied — capture table with columns: opportunity | why noticed | why not applied now (current phase + allowed target) | suggested future target. Capture without applying; application requires a new bounded contract. (PW-TPL-008)
- Template: Control-signal closure packet — HALT carries task id, machine-readable reason, safe-state flag, and recovery route; CLARIFY carries exactly one blocking question with the ambiguous field and options; closure carries scope-respected status, additions-beyond-scope, and validation results (state check, target check, claim status). Closure is accepted only with state-validation evidence. (PW-TPL-010)
