# TEMPLATES

## Purpose

Accepted validated reusable Prompts Workflows templates.

## Template schema

```yaml
template_entry:
  id:
  status: accepted | deprecated
  use_when:
  template_body:
  evidence_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due:
```

## Accepted templates

- id: `PW-TPL-001`
  status: accepted
  use_when: A bounded Markdown existing-file change is approved, but a chat-authored unified diff would be fragile or unsafe.
  template_body: |
    # Codex Live Edit - One File

    ## Role

    You are Codex acting as deterministic live-repo editor.
    Edit exactly one target file. Do not widen scope, touch config, touch source/staging folders, or commit before validation and diff review.

    ## Target file

    `<TARGET_FILE>`

    ## Authority

    Use the approved patch intent for this target only. Do not re-decide architecture.

    ## Safety start

    Run:

    ```bash
    git status --short
    git branch --show-current
    git diff --check
    git ls-files --eol <TARGET_FILE>
    ```

    Record whether the file uses LF or CRLF. Preserve the existing line-ending style unless repo tooling clearly normalizes it.
    Abort if tracked files are dirty unless explicitly approved.

    ## Edit rules

    - edit only `<TARGET_FILE>`
    - preserve unrelated text
    - keep the patch minimal
    - do not modify `managed/config/openclaw.json`
    - do not modify `NewFinals/`, `BaselinePatches/`, `AdvancedUpdateProcess/`, or `AllAIBestPractice/`
    - do not treat learning queues as runtime truth

    ## Validation

    Run:

    ```bash
    git diff --check
    git diff --name-only
    git diff -- <TARGET_FILE>
    git diff --name-only | grep -E 'OpenClaw/07_finalopenclawsystem/(NewFinals|BaselinePatches|AdvancedUpdateProcess|AllAIBestPractice)/' && exit 1 || true
    git diff --name-only | grep 'OpenClaw/07_finalopenclawsystem/managed/config/openclaw.json' && exit 1 || true
    ```

    Verify only `<TARGET_FILE>` changed. Do not commit until the real Git diff has been reviewed.
  evidence_refs:
    - operator feedback, 2026-04-27, "Replacement Pack D Prompt Shape"
    - `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27
- id: `PW-TPL-002`
  status: accepted
  use_when: A fenced unified diff fails `git apply --check` as corrupt, but the intended bounded edit is visible and the live target has not drifted.
  template_body: |
    # Malformed Diff Recovery - One File

    ## Preconditions

    - `git apply --check <patch>` failed.
    - The failure is patch-form corruption, not target mismatch.
    - The live target has been read.
    - The intended bounded edit is visible in the artifact.

    ## Recovery steps

    1. Record the failed command output.
    2. Verify the live target has no unexpected drift.
    3. Live-edit only the intended bounded content into the target file.
    4. Run `git diff --check`.
    5. Show `git diff -- <target>` from the actual checkout.
    6. Continue only with downstream validation that depends on the recovered file.

    ## Stop conditions

    - target drift is unclear
    - intended content is incomplete
    - edit would widen scope
    - config or source/staging paths would change
  evidence_refs:
    - `OpenClaw/07_finalopenclawsystem/NewFinals/NextLevel2/NeweFinal/PACK_D_CROSS_REFERENCE_MANIFEST_UNIFIED_DIFF.md`
    - `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27
- id: `PW-TPL-003`
  status: accepted
  use_when: A deep-research prompt needs an implementation-ready report from locked local/repo sources and must avoid generic research detours.
  template_body: |
    # Deep Research Preflight Contract

    ## Locked Assumptions

    Treat these as accepted for this run. Do not re-research them. If one appears false, record a validation test or open question instead of spending research budget.

    - `<LOCKED_ASSUMPTION_1>`
    - `<LOCKED_ASSUMPTION_2>`

    ## Source Access Priority

    Use sources in this order:

    1. exact local paths or exact repo paths listed below
    2. current managed canon/protocol surfaces
    3. official external docs only for external tool mechanics
    4. prior model outputs only as weak synthesis

    Required source surfaces:

    | Source | Access method | If missing |
    |---|---|---|
    | `<SOURCE_PATH>` | direct file read or exact-path fetch first | report once, state consequence, continue only within safe scope |

    Do not begin with broad connector discovery unless exact-path access fails.

    ## Citation And Evidence Rule

    Use file-path references for internal/local source evidence unless the final report explicitly requires formal citations. Cite official external docs only when relying on external tool mechanics. Do not spend task budget researching citation mechanics.

    ## Detour Budget

    | Topic | Budget | Required behavior |
    |---|---:|---|
    | locked tool capability assumptions | 0 | convert uncertainty into validation test |
    | excluded topics | 0 | mention only if needed as explicitly excluded |
    | missing or renamed internal file | 1 check | report once, then use nearest authoritative available surface |
    | generic architecture theory | 0 | use only if prompt explicitly asks |

    ## Failure Routing

    - If required source access fails, mark the affected section partial and continue with the safe subset.
    - If evidence conflicts, prefer the locked source basis and record a validation test.
    - If output scope is too large, complete the named Phase 1 subset rather than broadening research.
    - If connector behavior is unclear, do not research generic connector behavior; define an implementation validation test.

    ## Output Discipline

    Produce the requested operational artifacts only. Do not add background sections, generic tool explanations, or reopened decisions.
  evidence_refs:
    - `OpenClaw/02_research-kb/best-practices/operational-framework/UpdateProcessSSOTS/DRGPT55THinkingProcess.md`
    - `OpenClaw/04_final-system-setup/AfterOpenClawFIrstSetup/New_orchestration/DeepResearchPrompt_v2.md`
    - `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-28

## Empty-state marker or initial entries

Add entries here only after validation and promotion from `LEARNING_QUEUE.md`.
