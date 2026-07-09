# Skill Package Rules

The following rules summarise best practices for creating a Claude‑
compatible skill package, distilled from the available guidance and
failure analyses.  Adhering to these rules helps ensure that the
skill is easy to understand, maintain and integrate.

## SKILL.md Structure

1. **Front‑matter only name and description** – The YAML front‑matter at
   the top of `SKILL.md` must contain only two keys: `name` and
   `description`.  Do not include other keys such as `version` or
   `author` here.
2. **Description begins with “Use this skill when”** – The
   description must begin with the phrase “Use this skill when” and
   clearly state when and why the skill should be used.  Avoid
   generalities and marketing fluff.
3. **Section order is fixed** – After the front‑matter, use the
   following order of sections:
   - Overview
   - Inputs
   - Outputs
   - Procedure (6–8 coarse steps)
   - Failure Modes
   - Non‑Goals
   - Supporting Files
   - Completion Gate
   Additional sections may be added only if absolutely necessary and
   must not disrupt the core order.
4. **Procedure length** – The procedure should contain between six
   and eight high‑level steps.  Each step should describe one
   observable outcome or action.  Avoid overly granular instructions.
5. **Failure modes summary** – List only the most common failure
   modes (no more than eight).  Provide concise recovery hints and
   refer to a separate reference document for details.
6. **Non‑goals** – State what the skill intentionally does not do.
   Use imperative sentences beginning with “Do not…”.
7. **Supporting files section** – List each supporting file along
   with a short description and when it should be read.  Use the
   keyword `read_when` to specify the context in which the file is
   relevant.
8. **Completion gate** – Provide a simple checklist of conditions
   that must be satisfied before concluding that the task is complete.

## Supporting Files

1. **References** – Store detailed explanations and contracts in the
   `references/` directory.  These files should be concise and avoid
   duplicating content found in SKILL.md.  Use plain Markdown or
   OKF‑flavoured Markdown as appropriate.
2. **Templates** – Place any templates in the `templates/` directory.
   Templates should provide skeleton structures with placeholders and
   should be kept short.  Do not include long prose here.
3. **Examples** – Keep examples minimal and illustrative.  They should
   demonstrate how to use the skill but must not replicate large
   portions of real projects.  Use generic or dummy content.
4. **Scripts** – Scripts should live in the `scripts/` directory and
   rely only on the Python standard library.  They must not perform
   network access and must enforce the hard rules outlined in the
   patching contract.

## Other Guidelines

* **Schema definition once** – Define any JSON schema (such as the
  fixture specification) in a single file.  Do not duplicate schema
  definitions across multiple files.
* **Typed constraints** – When defining schemas or structured
  templates, express constraints as types (e.g., string, integer,
  boolean) rather than human‑readable descriptions.
* **Non‑goals emphasised** – Use clear non‑goals to prevent misuse
  of the skill.  Include them even if they seem obvious.
* **Avoid redundancy** – Do not repeat large sections of other files
  within SKILL.md.  Instead, reference supporting documents via
  `read_when`.
* **No manifest duplication** – The package manifest should summarise
  the contents of the package.  Do not reproduce the manifest as a
  contract within other documents.