# Phase 0 Semantic Depth and Git Synchronization — Exact-Match Patch Instructions

These instructions are **not applied changes**. A deterministic executor must apply each block literally and report success or failure per block.

## Decision summary

- Deterministic corpus intelligence always runs at its full configured capability. It is not reduced by quick/standard/deep.
- The operator field is renamed from `detail` to `semantic_depth`.
- `quick`, `standard`, and `deep` are preserved for later semantic packet generation and semantic execution.
- The existing Phase 1 coverage floor remains a fixed compatibility value until the semantic module owns a real depth contract. It is no longer presented as the meaning of semantic depth.
- Start may fetch `origin/main` and attempt a fast-forward-only synchronization.
- Fetch or fast-forward failure is reported but does not block creating a new non-overlapping KB destination.
- Dirty and untracked files are informational. Apex KB does not stash, reset, clean, overwrite, or mix linked worktrees.

<file>C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\references\start-input.schema.json</file>
<old>
        "detail",
        "output",
</old>
<new>
        "semantic_depth",
        "output",
</new>

<file>C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\references\start-input.schema.json</file>
<old>
        "detail": {
          "enum": ["quick", "standard", "deep"]
        },
</old>
<new>
        "semantic_depth": {
          "enum": ["quick", "standard", "deep"]
        },
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb_start.py</file>
<old>
DETAIL_COVERAGE = {"quick": 0.4, "standard": 0.6, "deep": 0.8}
EXAMPLE_MARKERS = (
</old>
<new>
COMPAT_PHASE1_MIN_COVERAGE = 0.6
EXAMPLE_MARKERS = (
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb_start.py</file>
<old>
        "phase1_min_coverage": DETAIL_COVERAGE[options["detail"]],
        "detail_profile": options["detail"],
        "non_text_policy": options["non_text"],
</old>
<new>
        "phase1_min_coverage": COMPAT_PHASE1_MIN_COVERAGE,
        "semantic_depth": options["semantic_depth"],
        "non_text_policy": options["non_text"],
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb_start.py</file>
<old>
def resolve_primary_worktree(start: Path, repository: str, control: Any) -> Dict[str, Any]:
    probe = git(start, "rev-parse", "--show-toplevel")
    if probe.returncode:
        raise StartError("repository_not_found", probe.stderr.strip() or "No Git repository found", [str(start)])
    invoked = Path(probe.stdout.strip()).resolve()
    listing = git(invoked, "worktree", "list", "--porcelain")
    if listing.returncode:
        raise StartError("worktree_list_failed", listing.stderr.strip() or "git worktree list failed")
    worktrees = parse_worktrees(listing.stdout)
    if not worktrees:
        raise StartError("worktree_topology_empty", "Git returned no worktree records")
    primary = Path(worktrees[0]["path"]).resolve()
    branch = worktrees[0].get("branch")
    if branch != "main":
        raise StartError(
            "primary_worktree_not_main",
            f"Primary worktree is on {branch or 'detached HEAD'}, not main. Apex KB will not switch branches automatically.",
            [str(primary)],
        )
    origin = git(primary, "remote", "get-url", "origin")
    detected = remote_slug(origin.stdout) if origin.returncode == 0 else None
    if detected and detected.lower() != repository.lower():
        raise StartError(
            "repository_identity_mismatch",
            f"Configuration names {repository}, but primary worktree origin is {detected}",
            [str(primary)],
        )
    state = control.classify_git_state(primary)
    if not state.get("safe_for_kb_write"):
        raise StartError("primary_worktree_unsafe", str(state.get("reason")), state.get("changed_paths", []))
    return {
        "schema": "apex.kb.worktree-safety.v1",
        "policy": "primary_main_only",
        "invoked_root": str(invoked),
        "primary_root": str(primary),
        "fallback_applied": invoked != primary,
        "primary_branch": branch,
        "primary_head": worktrees[0].get("head") or state.get("head"),
        "worktree_count": len(worktrees),
        "ignored_worktrees": worktrees[1:],
        "git_state": state,
        "rules": [
            "never_create_worktree",
            "never_switch_branch",
            "never_mix_worktree_content",
            "write_only_in_primary_main_worktree",
        ],
    }
</old>
<new>
def resolve_primary_worktree(start: Path, repository: str, control: Any) -> Dict[str, Any]:
    probe = git(start, "rev-parse", "--show-toplevel")
    if probe.returncode:
        raise StartError("repository_not_found", probe.stderr.strip() or "No Git repository found", [str(start)])
    invoked = Path(probe.stdout.strip()).resolve()
    listing = git(invoked, "worktree", "list", "--porcelain")
    if listing.returncode:
        raise StartError("worktree_list_failed", listing.stderr.strip() or "git worktree list failed")
    worktrees = parse_worktrees(listing.stdout)
    if not worktrees:
        raise StartError("worktree_topology_empty", "Git returned no worktree records")
    primary = Path(worktrees[0]["path"]).resolve()
    branch = worktrees[0].get("branch")
    if branch != "main":
        raise StartError(
            "primary_worktree_not_main",
            f"Primary worktree is on {branch or 'detached HEAD'}, not main. Apex KB will not switch branches automatically.",
            [str(primary)],
        )
    origin = git(primary, "remote", "get-url", "origin")
    detected = remote_slug(origin.stdout) if origin.returncode == 0 else None
    if detected and detected.lower() != repository.lower():
        raise StartError(
            "repository_identity_mismatch",
            f"Configuration names {repository}, but primary worktree origin is {detected}",
            [str(primary)],
        )

    synchronization = {
        "fetch_attempted": True,
        "fetch_status": "not_run",
        "fast_forward_attempted": False,
        "fast_forward_status": "not_needed",
        "warning": None,
    }
    fetched = git(primary, "fetch", "--prune", "origin", "main")
    if fetched.returncode:
        synchronization["fetch_status"] = "failed_continue_local"
        synchronization["warning"] = fetched.stderr.strip() or "git fetch failed; continuing with the current local main"
    else:
        synchronization["fetch_status"] = "ok"
        relation = git(primary, "rev-list", "--left-right", "--count", "HEAD...origin/main")
        if relation.returncode == 0:
            parts = relation.stdout.strip().split()
            ahead = int(parts[0]) if len(parts) == 2 else 0
            behind = int(parts[1]) if len(parts) == 2 else 0
            synchronization["ahead"] = ahead
            synchronization["behind"] = behind
            if behind > 0 and ahead == 0:
                synchronization["fast_forward_attempted"] = True
                advanced = git(primary, "merge", "--ff-only", "origin/main")
                if advanced.returncode:
                    synchronization["fast_forward_status"] = "failed_continue_local"
                    synchronization["warning"] = advanced.stderr.strip() or "Fast-forward failed; continuing with current local files"
                else:
                    synchronization["fast_forward_status"] = "ok"
            elif ahead > 0 and behind > 0:
                synchronization["fast_forward_status"] = "diverged_continue_local"
                synchronization["warning"] = "Local main and origin/main diverged; Apex KB did not merge or rewrite local work"
            elif ahead > 0:
                synchronization["fast_forward_status"] = "local_ahead_continue_local"

    state = control.classify_git_state(primary)
    refreshed_head = git(primary, "rev-parse", "HEAD")
    primary_head = refreshed_head.stdout.strip() if refreshed_head.returncode == 0 else worktrees[0].get("head") or state.get("head")
    return {
        "schema": "apex.kb.worktree-safety.v1",
        "policy": "primary_main_prefer_synchronized",
        "invoked_root": str(invoked),
        "primary_root": str(primary),
        "fallback_applied": invoked != primary,
        "primary_branch": branch,
        "primary_head": primary_head,
        "worktree_count": len(worktrees),
        "ignored_worktrees": worktrees[1:],
        "git_state": state,
        "synchronization": synchronization,
        "rules": [
            "never_create_worktree",
            "never_switch_branch",
            "never_mix_worktree_content",
            "prefer_fetch_and_fast_forward_only",
            "dirty_and_untracked_files_are_informational",
            "never_stash_reset_clean_merge_or_rebase_operator_work",
            "write_only_to_the_configured_non_overlapping_kb_destination",
        ],
    }
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\tests\test_apex_kb_start.py</file>
<old>
    def test_detail_profiles_have_explicit_coverage_floors(self):
        self.assertEqual(start.DETAIL_COVERAGE, {"quick": 0.4, "standard": 0.6, "deep": 0.8})
</old>
<new>
    def test_semantic_depth_does_not_reduce_deterministic_phase_capability(self):
        self.assertEqual(start.COMPAT_PHASE1_MIN_COVERAGE, 0.6)
        self.assertNotIn("DETAIL_COVERAGE", vars(start))
</new>

<file>C:\GitDev\apexai-os-meta\FutureDevelopments&Research\ProjectMM&Task&KB\KnowledgeBase\ApexKBFinalDesignDeepResearch\ProThink-Report-Aftermath\AfterCCUpdate\NewApexVersionAfterCodexFail\NewApex-KB\apex-kb-mechanistic-workflow-pack\templates\start-qa-option-a-v3-example-guidance.md</file>
<old>
  detail: quick / standard / deep
  output: analysis_only / compiled_kb / query_ready
</old>
<new>
  semantic_depth: quick / standard / deep
  output: analysis_only / compiled_kb / query_ready
</new>

## Required executor verification

After applying the blocks, the executor must:

1. prove every `<old>` block matched exactly once;
2. run `python -m unittest apex-meta/scripts/tests/test_apex_kb_start.py`;
3. run the existing Apex KB control tests;
4. validate one Start configuration for each semantic depth;
5. prove the three configurations produce identical deterministic source scope and Phase 0 inputs;
6. prove semantic depth remains preserved in `manifests/start-input.json`;
7. create a temporary repository with a dirty primary `main` plus one linked worktree;
8. prove Start ignores the linked worktree and does not stash, reset, clean, merge, rebase, or create a worktree;
9. prove failed fetch or failed fast-forward is a warning rather than a Start blocker;
10. report the exact commit and all changed files. 
