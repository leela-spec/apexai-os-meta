# Phase 0 Setup Minimal Live Slice — Exact-Match Patch Instructions

These edits are **not applied**. A deterministic executor must apply every block as a literal exact-match replacement and report success or failure separately.

## Scope

- Rename the operator option `detail` to `semantic_depth`.
- Keep deterministic corpus intelligence at full capability for every semantic-depth choice.
- Preserve a fixed compatibility coverage value until the semantic module owns a real depth contract.
- Prefer read-only worktree discovery plus `fetch origin main` and fast-forward-only synchronization.
- Preserve dirty and untracked files and never create, combine, clean, reset, stash, rebase, or non-fast-forward merge worktrees.
- Expose the Start adapter through `python apex-meta/scripts/apex_kb.py start`.
- Update the selected Q&A and unit tests.

## Patch blocks

<file>C:\GitDev\apexai-os-meta\.claude\skills\apex-kb\references\start-input.schema.json</file>
<old>
  "$id": "apex.kb.start-input.v1",
</old>
<new>
  "$id": "apex.kb.start-input.v2",
</new>

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
START_SCHEMA = "apex.kb.start-input.v1"
OUTPUT_MAP = {
</old>
<new>
START_SCHEMA = "apex.kb.start-input.v2"
OUTPUT_MAP = {
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

    synchronization: Dict[str, Any] = {
        "fetch_attempted": True,
        "fetch_status": "not_run",
        "fast_forward_attempted": False,
        "fast_forward_status": "not_needed",
        "warning": None,
    }
    fetched = git(primary, "fetch", "--prune", "origin", "main")
    if fetched.returncode:
        synchronization["fetch_status"] = "failed_continue_local"
        synchronization["warning"] = fetched.stderr.strip() or "git fetch failed; continuing with current local main"
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
    if not state.get("safe_for_kb_write"):
        raise StartError("primary_worktree_unsafe", str(state.get("reason")), state.get("changed_paths", []))
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

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb.py</file>
<old>
_CONTROL_MODULE: Any = None


def _control_module() -> Any:
</old>
<new>
_CONTROL_MODULE: Any = None
_START_MODULE: Any = None


def _control_module() -> Any:
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb.py</file>
<old>
    _CONTROL_MODULE = module
    return module


def cmd_postflight(args: argparse.Namespace) -> Dict[str, Any]:
</old>
<new>
    _CONTROL_MODULE = module
    return module


def _start_module() -> Any:
    global _START_MODULE
    if _START_MODULE is not None:
        return _START_MODULE
    path = Path(__file__).resolve().with_name("apex_kb_start.py")
    spec = importlib.util.spec_from_file_location("apex_kb_start", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load Apex KB Start frontend: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    _START_MODULE = module
    return module


def cmd_start(args: argparse.Namespace) -> Dict[str, Any]:
    return _start_module().run(args)


def cmd_postflight(args: argparse.Namespace) -> Dict[str, Any]:
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb.py</file>
<old>
    control_cmd = sub.add_parser("control", help="Canonical run-state, stage orchestration, semantic packets, recovery, and Git classification")
    _control_module().configure_parser(control_cmd)

    sc = sub.add_parser("scaffold")
</old>
<new>
    control_cmd = sub.add_parser("control", help="Canonical run-state, stage orchestration, semantic packets, recovery, and Git classification")
    _control_module().configure_parser(control_cmd)

    start_cmd = sub.add_parser("start", help="Validate and preview or initialize one Apex KB Setup configuration")
    start_cmd.add_argument("--config", required=True, help="Path to the operator Start YAML configuration")
    start_cmd.add_argument("--repo-root", help="Repository checkout or linked-worktree path used for read-only topology discovery")
    start_cmd.set_defaults(func=cmd_start)

    sc = sub.add_parser("scaffold")
</new>

<file>C:\GitDev\apexai-os-meta\apex-meta\scripts\apex_kb.py</file>
<old>
    args = parser.parse_args(argv)
    if not args.kb_root:
        parser.error("--kb-root is required")
    try:
        control = _control_module()
        if args.command == "control":
            result = control.dispatch(args, globals())
        else:
            guarded = control.guard_direct_command(args)
            result = guarded if guarded is not None else args.func(args)
        maybe_write_output_json(args, result, resolve_kb_root(args.kb_root))
</old>
<new>
    args = parser.parse_args(argv)
    if args.command != "start" and not args.kb_root:
        parser.error("--kb-root is required")
    try:
        control = _control_module()
        if args.command == "start":
            result = args.func(args)
        elif args.command == "control":
            result = control.dispatch(args, globals())
        else:
            guarded = control.guard_direct_command(args)
            result = guarded if guarded is not None else args.func(args)
        output_root = resolve_kb_root(args.kb_root) if args.kb_root else Path.cwd()
        maybe_write_output_json(args, result, output_root)
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

<file>C:\GitDev\apexai-os-meta\FutureDevelopments&Research\ProjectMM&Task&KB\KnowledgeBase\ApexKBFinalDesignDeepResearch\ProThink-Report-Aftermath\AfterCCUpdate\NewApexVersionAfterCodexFail\NewApex-KB\apex-kb-mechanistic-workflow-pack\templates\start-qa-option-a-v3-example-guidance.md</file>
<old>
| **Run detail** | `quick` | The corpus is small and already understood | Inventory, formats, headings, and basic phrase matches |
|  | `standard` **default** | Normal project or documentation KB | Structured topic matching, duplicates, dates when available, work packs, and statistics |
|  | `deep` | The corpus is large, highly versioned, or relationship-heavy | Standard processing plus broader extraction and configured relationship analysis |
</old>
<new>
| **Semantic depth** | `quick` | The semantic questions are narrow or a concise answer is sufficient | Uses the strongest evidence first, answers locked questions concisely, and avoids optional expansion |
|  | `standard` **default** | Normal project or documentation KB | Reviews the complete bounded work pack with normal authority, contradiction, version, dossier, and source-atlas treatment |
|  | `deep` | The topic is highly versioned, contradictory, or strategically important | Performs maximum bounded cross-source reconciliation, evolution analysis, uncertainty treatment, and richer Macro/Meso/Micro synthesis |
</new>

## Required executor verification

1. Prove every `<old>` block matches exactly once before editing.
2. Apply one block at a time and report each result.
3. Run `python -m unittest apex-meta/scripts/tests/test_apex_kb_start.py`.
4. Run the existing Apex KB control-plane test suite.
5. Run `python apex-meta/scripts/apex_kb.py start --help`.
6. Validate one no-write Start configuration for each semantic depth.
7. Prove all three depths produce identical deterministic source scope and retain `semantic_depth` in the Start result.
8. Create a temporary Git repository with a dirty primary `main` and one linked worktree.
9. Prove Start ignores linked-worktree content and does not create, stash, reset, clean, rebase, or non-fast-forward merge anything.
10. Prove failed fetch or failed fast-forward is visible as a warning rather than a Start blocker.
11. Prove unresolved merge conflicts or an active Git operation still block writes.
12. Return the exact changed files, tests, command output, and resulting commit. Do not claim completion until all checks pass.
