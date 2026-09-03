## 1. Immediate security correction: the Paperless token leaked again

This is the most important finding.

C1 correctly rotated the original leaked token. But the **replacement token was then written verbatim into the new handover dossier**.

Worse, the dossier says:

> `NO PUSH ENFORCED`

but GitHub shows the dossier itself was committed as:

`b9d7a77c — docs(ki-basis): record AI handover and architectural reviewer dossier`

and the correction commits are present remotely.

So two things are now false:

```
"new token remains secret"     -> false
"no push was performed"        -> false
```

### Required action

Rotate the Paperless API token **again**.