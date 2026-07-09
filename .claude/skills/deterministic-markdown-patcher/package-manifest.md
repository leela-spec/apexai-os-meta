# Package Manifest

This manifest lists all files included in the `deterministic‑markdown‑patcher` skill
package along with a brief description of their purpose.  Use it as a
quick reference to locate documents, templates, examples and scripts.

## Root

| Path | Purpose |
| --- | --- |
| **SKILL.md** | Main skill definition file with procedure, failure modes and references. |
| **package‑manifest.md** | This manifest. |

## Agents

| Path | Purpose |
| --- | --- |
| **agents/openai.yaml** | OpenAI Assistant configuration, including model and instructions. |

## References

| Path | Purpose |
| --- | --- |
| **references/source‑ledger.okf.md** | Catalog of all source documents and their classification. |
| **references/patching‑process‑contract.md** | Formal contract for deterministic patching, including principles, modes and hard rules. |
| **references/action‑decision‑matrix.md** | Guidance on selecting the correct patch action mode. |
| **references/skill‑package‑rules.md** | Summary of best‑practice rules for building Claude skill packages. |
| **references/hook‑policy.md** | Policies for hooking into patch execution and error handling. |
| **references/failure‑modes‑and‑recovery.md** | Catalog of common failure modes and recovery steps. |

## Templates

| Path | Purpose |
| --- | --- |
| **templates/patch‑intent.okf.md** | Template for drafting patch intents. |
| **templates/fixture‑spec.json** | JSON schema describing fixture files for automated patch packs. |
| **templates/final‑report.okf.md** | Template for final patch reports summarising execution results. |

## Examples

| Path | Purpose |
| --- | --- |
| **examples/small‑section‑edit.example.md** | Demonstrates replacing a small span of text using `replace_once`. |
| **examples/frontmatter‑edit.example.md** | Demonstrates updating YAML front‑matter using `front_matter_set`. |
| **examples/patch‑pack‑run.example.md** | Shows how to create and run a patch pack via the fixture runner. |

## Scripts

| Path | Purpose |
| --- | --- |
| **scripts/patch_executor.py** | Core deterministic patch executor implementing multiple modes. |
| **scripts/fixture_runner.py** | Utility for running patch packs defined in JSON fixtures. |
| **scripts/package_check.py** | Tool to validate that the package adheres to structural rules. |
