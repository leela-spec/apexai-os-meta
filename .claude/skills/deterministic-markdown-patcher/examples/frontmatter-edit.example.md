# Example: Front‑Matter Update

This example updates the YAML front‑matter of a Markdown document.  Suppose
`posts/2024-01-01-welcome.md` begins with:

```yaml
---
title: Welcome
date: 2024-01-01
tags: ["announcement"]
---

Welcome to our blog!
```

We want to add a new tag and update the title.  The patch intent is:

```yaml
target_file: posts/2024-01-01-welcome.md
mode: front_matter_set
front_matter:
  title: "Welcome to the Blog"
  tags: ["announcement", "blog"]
description: Add a blog tag and clarify the title.
```

Execute the patch:

```sh
python scripts/patch_executor.py front_matter_set \
    --file posts/2024-01-01-welcome.md \
    --front-matter '{"title": "Welcome to the Blog", "tags": ["announcement", "blog"]}'
```

Validate and diff as usual.  The diff will show only changes within
the front‑matter block.