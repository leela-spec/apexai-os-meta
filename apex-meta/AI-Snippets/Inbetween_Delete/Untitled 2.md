# AGENTS.md — Leela Cloud 2026

The repo's operating rules for agents. Settle conflicts with the authority ladder in §2; the
approval boundaries in §7 are the things you may never decide alone.

## 1. Execution

<leela_contract v="2.0">

<method>The operator selects the working method. Do not adopt a framework, methodology or
skill-driven process unless the operator asks for it in the current task; a recommendation is never
permission to invoke. Framework output is working material until an accepted conclusion is
integrated into the artifact that owns it.</method>

<ground>The authored materialization ledger IS the originating artifact for build state — read it,
never re-derive what it already records (SSOT-D-054). A generated view of it is not grounding.
Before restoring, re-adding or "recovering" anything that is absent, search why it was removed
(`qmd search "<the thing itself>" -c leela-ssot`) and quote what you find. Search the subject, not
your explanation of it. Treat absence as a decision until the record shows otherwise.</ground>

<documents>Default to not writing one. A finding belongs in the artifact it corrects — a rule, a
spec, a decision record, or the work package. Analysis that produces no durable change produces no
file. A `description:` must state the question the file answers, not its contents
(SSOT-D-056).</documents>

<authoring when="writing or editing a rule in this file">State a conditional rule as an imperative
with named, checkable trigger conditions — see the `--full` triggers in §5 for the pattern — not as
rationale the reader must infer a trigger from. Keep prose only for concepts with no trigger to
check; keep a discrete disjoint mapping a table. A prose pointer ("if X, read Y") is a hint, not
routing: no controlled test shows it stops an agent reading non-matching files, so never present one
as a measured saving (RP-01).</authoring>

<new_machinery when="about to add a script, gate, check, schema or test">Name the failure it serves
and confirm ordinary use does not already surface it. Past that bar, build it: here a cheap
deterministic check is measured to beat a rule that depends on remembering to apply it
(SSOT-D-058).</new_machinery>

<product_first>Provenance bookkeeping is a footnote: a green-except-provenance result is reportable
as-is.</product_first>

<instruction_contract name="lean_execution">
  <context_routing> <!-- GATING: evaluate task shape before applying -->
  WHEN executing multi-step code work (edit -> commit -> verify) in this repo:
  - Apply <efficiency_rules> strictly.
  OTHERWISE (one trivial edit, a question, read-only exploration):
  - Skip; use normal judgment.
  </context_routing>
  <efficiency_rules>
  <rule id="verification_scope">Never run `flutter analyze`/`flutter test` directly; reach them
  through the gate runner in §5, and never per edit or micro-commit. Reuse successful validation
  evidence while its inputs are unchanged.</rule>
  <rule id="commit_granularity">Commit per coherent verified unit, never per file or micro-edit.
  Batch related edits into one commit. Expect a handful of commits per task, not a dozen.</rule>
  </efficiency_rules>
</instruction_contract>

</leela_contract>

## 2. Authority — settle product conflicts here

1. **accepted operator decisions + authored per-feature materialization ledgers**
2. **current code**
3. **SSOT narrative/spec/canon material**

Tier 1 is shared: if a decision and the ledger conflict, surface it rather than inventing a winner.
Generated views are derived caches. Tests and gates are verification evidence, never a higher
semantic tier. `docs/ssot/**` is design context — a statement does not become authoritative merely
by living there.

`master` is current truth; never revive instructions from a stale branch. Delivery authority comes
from the current work package — historical Wave-C branches and orchestration packets are not
standing execution instructions. Execute new operator decisions and flag conflicting older
artifacts rather than blocking; "execute" never extends to the §7 approval boundaries.

**materialization** is the durable rule-to-artifact map, and its primary purpose is build state:
`target_status` answers *"realized, or still only a spec?"* — which no test can answer, because a
test only runs code that exists. Freshness is advisory; a row claiming `exists` for an absent target
blocks (SSOT-D-053). Contract: [`materialization.md`](docs/ssot/architecture/materialization.md).

## 3. Routes — load the row you are on, not the whole ladder

Nothing below your row is mandatory context. Each route ends at the artifact that *owns* the answer.

The map answers *does it exist yet* and is the inventory; the tests answer *does the code that
exists work*; the work tracker answers *what am I supposed to do* and is the commitment
(SSOT-D-054). Three different systems — never use one to answer another's question, and never
hand-restate one in the other.

| Your task | Route |
|---|---|
| **Semantic / product claim** — what is XP, who owns the week, is this locked? | the authority ladder in §2. `--rule` is a routing aid, not a truth upgrade |
| **What is built vs. still spec** | the feature's `materialization.csv`; `target_status` answers it (`exists` · `to_change` · `to_write` · `blocked` · `unverified`). Query with `generate_ssot_views.py --rule <ID>` or `--target <path>` |
| **Current execution** — what should I work on? | OpenProject, via the `openproject` skill. Project `leela-cloud-2026`; subprojects `leela-path`, `leela-skill-tree`, `leela-sequencing`, `leela-rhythm` |
| **Provenance / history** — why was this decided? | the decision record in `docs/ssot/decisions/` (cite `SSOT-D-###`, never a filename) → targeted grep of `docs/data-architecture/STATE.md`. Stop there; `docs/audits/` is superseded |
| **What happened in a past session** | `docs/data-architecture/STATE.md` — an append-only history log, never a work queue |
| **Landing operator decisions** | the `decision-integration-batch` skill |
| **Unknown vocabulary** | [`glossary.md`](docs/ssot/glossary.md) → grep `docs/ssot/` → the owner it names |
| **Project history and prior research** | `qmd search "<term>" -c leela-audits` — also `leela-ssot`, `leela-orchestration`, `leela-data-architecture`, `apex-informatics-final` — then `qmd get "#docid:from:count"` |
| **Operational detail for a tree you are editing** | `.claude/rules/` — path-triggered, Claude Code only. Handed to you on a matching file access; nothing else reaches it, so open it by name when you need it before touching the tree |

`docs/orchestration/**` is historical provenance, never a work queue; open one only when a
provenance question names it. `STATUS.md` is a generated roll-up and untracked (SSOT-D-052):
regenerate it to read it, never commit it.

## 4. Environment

The OpenProject skill is not vendored here. Its canonical source is
`C:\GitDev\agent-skills\skills\openproject\`, linked per-skill into your agent's user-global skills
directory. The token loads from `~/.config/openproject/op.env` and is never in-repo.

## 5. Gates

One entry point. Guarantees and blind spots:
[`gates-and-checkers.md`](docs/ssot/architecture/gates-and-checkers.md). Whether they earn their
cost is measured, not argued (SSOT-D-058) — run `scripts/sabotage_audit.py` before deleting any;
it last scored 28/28 on 2026-10-28.

A gate passes on exit 0 and fails on anything else — a nonzero exit, a missing tool, or a new
warning identity from a gate that ran. There is no expected-red state. A numeric limit never vetoes
correct work: raise it deliberately and record why, never shave a load-bearing rule or a domain fact
to fit.

```text
python scripts/gates.py                        # fast tier
python scripts/gates.py --since origin/master  # only gates the diff can affect; prints what it parked
python scripts/gates.py --full                 # canary; run only per the 3 triggers below
```

`--since` parks any gate whose declared dependency family the diff does not touch, and names every
parked family so a bounded run cannot be mistaken for full coverage. **A clean `--since` is
sufficient evidence on its own — do not follow it with `--full` "to be safe."** Run `--full` only
when: (1) the diff touches `scripts/gates.py` or another selector/control-plane file, (2) a parked
gate's exposure looks wrong for this change, or (3) the operator asks for a release-grade canary.
If `--full` ever catches something `--since` parked, widen that gate's `exposure` immediately.

Never run a validator directly — the runner collapses repeated findings into stable warning
identities.

## 6. Domain facts

**Flutter.** Required toolchain is Flutter 3.44.8 / Dart 3.12.2. Android debug is
`flutter build apk --debug`, release is `flutter build apk --release`, bundle is
`flutter build appbundle --release --target-platform android-arm64`. There is no active
`build_runner` step on `master` — do not introduce or run code generation unless the approved task
requires it.

**Data plane (SSOT-D-059).** Fixture-first and database-neutral; feature repositories may keep
temporary mutable state for the current app session. Screens and controllers must not receive
database row types or SQL/table names from new code. Build local-first with full data — logins and
cloud persistence come later. Supabase auth, a `SharedPreferences` outbox and live view reads
already exist: do not extend them and do not delete them, and preserve the live-then-fixture
fallback in `readView`, which is what lets the app run with no account. Do not add a new storage
engine, auth flow, sync layer, outbox or multi-device behaviour. Do not require live credentials or
hosted data for UI/UX work, and never import the old hosted dataset — it is untrusted. The committed
anon key is a known, accepted deferral (SSOT-D-059 §5): do not re-raise it as a finding, and do not
ship against it.

**Sequencing.** Wave A types, serializers, IDs and structure hashes are storage-neutral: a storage
decision never changes the domain layer. Preserve the Wave A structure-hash projection exactly
unless the Canon changes it explicitly. Reuse Wave A typed IDs and domain serializers; do not
recreate parallel domain objects. Canonical fixture manifest entries are `{path, sha256}` and must
be verified before decoding.
Preserve occurrence order, duplicate bindings, relation endpoints, Parallel Layer bindings, accepted
projections and policy references. `primaryChunkIds` and `derivedUniqueChunkIds` are display/legacy
helpers, never execution authority. New writes use canonical terminology; legacy aliases are
normalized only on read.

**Media.** Git LFS covers `png`, `jpg`, `jpeg`, `gif`, `webp` and `pdf` unless the runtime allowlist
applies — platform icons, `assets/icons/**` and `assets/mock/**`. Enforcement is `.gitattributes`
plus `scripts/ci_verify_lfs_media.sh` in CI, and the LFS hooks `git lfs install` placed in
`.git/hooks` do run. The duplicate copies under `.githooks/` are not wired, and
`.githooks/pre-commit` is deliberately left that way: it would run `flutter analyze` and
`flutter test` on every commit touching Dart, which `verification_scope` forbids.

**Authoring under `docs/`.** A decision record goes in `docs/ssot/decisions/` — allocate the next
`SSOT-D-###`, cite the ID and never the filename, then rebuild the registry with
`build_decision_registry.py`, which `check_decision_closure.py` joins against every donor mention so
a question closed in the ledger cannot stay open in a handover. Rebuild after touching any decision
record or `OPEN_QUESTIONS.md`. `registry-mentions.csv` is a local convenience file, untracked and
never a gate input. A generated artifact lives in the `_generated/` zone of its source domain and is
never hand-edited — no gate polices those trees (SSOT-D-058), so this rule is their only protection.

## 7. Approval boundaries — never decide these alone

- **Never commit credentials, signing secrets, service keys, or private hosted data.**
- **Never infer permission to commit, push, branch, or open a PR** from an unrelated instruction.
  These verbs are pre-approved in the tool permission config; that removes the prompt, never the
  need for authority. A config allow-list is not a task instruction.
- **Never delete a tracked file — archive it.** `git mv` it under an `_archive/` directory with a
  README naming why it was retired, where its content now lives, and anything deliberately not
  carried over. Deleting destroys the record that answers "was this removed on purpose?"
- Preserve unrelated dirty files and failure artifacts; never stash, discard, move or rewrite them
  without approval.
- Before changing more than ten tracked files, report the expected blast radius by code, generated
  files, tests, fixtures and documentation.
- Do not bundle database selection, wave execution, fixture regeneration, or docs/tool retirement
  into unrelated work.
- The warning baseline may shrink freely; growing it requires explicit operator authorization.
- Do not create a Git worktree by hand — an ordinary branch in the primary checkout is the isolation
  mechanism. A harness-created worktree is permitted, but land it on `master` promptly: each one
  fragments per-directory session history.
- Before switching branches, inspect the working tree first.
- The SQLite archive branches are reference-only and must never be merged wholesale.
