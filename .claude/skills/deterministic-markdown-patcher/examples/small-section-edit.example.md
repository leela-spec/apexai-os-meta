# Example: Small Span Replacement

This example demonstrates how to replace a single word in a Markdown file
using the `replace‑once` mode.  Suppose the file `docs/intro.md`
contains the sentence:

```markdown
Welcome to our old product.
```

We want to replace `old` with `new`.  The patch intent would look like
this:

```yaml
target_file: docs/intro.md
mode: replace_once
old_text: "old"
new_text: "new"
description: Update the product description to the new name.
```

Run the patch executor:

```sh
python scripts/patch_executor.py replace_once --file docs/intro.md \
    --old "old" --new "new"
```

After running, validate and diff the result:

```sh
python scripts/patch_executor.py validate_scope --file docs/intro.md \
    --old "old" --new "new"
python scripts/patch_executor.py diff --file docs/intro.md
```

The diff should show a single replacement from `old` to `new`.