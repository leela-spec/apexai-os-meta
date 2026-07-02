Title: Model Catalog | Hermes Agent

URL Source: https://hermes-agent.nousresearch.com/docs/reference/model-catalog

Markdown Content:
Hermes fetches curated model lists for **OpenRouter** and **Nous Portal** from a JSON manifest hosted alongside the docs site. This lets maintainers update picker lists without shipping a new `hermes-agent` release.

When the manifest is unreachable (offline, network blocked, hosting failure), Hermes silently falls back to the in-repo snapshot that ships with the CLI. The manifest never breaks the picker — worst case you see whatever list was bundled with your installed version.

`https://hermes-agent.nousresearch.com/docs/api/model-catalog.json`

Published on every merge to `main` via the existing `deploy-site.yml` GitHub Pages pipeline. The source of truth lives in the repo at `website/static/api/model-catalog.json`.

`{  "version": 1,  "updated_at": "2026-04-25T22:00:00Z",  "metadata": {},  "providers": {    "openrouter": {      "metadata": {},      "models": [        {"id": "moonshotai/kimi-k2.6", "description": "recommended", "metadata": {}},        {"id": "openai/gpt-5.4",       "description": ""}      ]    },    "nous": {      "metadata": {},      "models": [        {"id": "anthropic/claude-opus-4.7"},        {"id": "moonshotai/kimi-k2.6"}      ]    }  }}`

Cache location: `~/.hermes/cache/model_catalog.json`.

Set `enabled: false` to disable remote fetch entirely and always use the in-repo snapshot.

Third parties can self-host their own curation list using the same schema. Point a provider at a custom URL:

The overriding manifest only needs to populate the provider block(s) it cares about. Other providers continue to resolve against the master URL.

Then PR the resulting change to `website/static/api/model-catalog.json` to `main`. The docs site auto-deploys on merge and the new manifest is live within a few minutes.

You can also hand-edit the JSON directly for fine-grained metadata changes that don't belong in the in-repo snapshot — the generator script is a convenience, not the single source of truth.
