Let me look at the repo structure and relevant context first.Good news: OpenMausBot already has most of the primitives you need — the skill database would mostly be packaging and exposing them, not building from scratch.

## What already exists

- **Open format**: bots consume the `agentskills.io` spec — a folder with `SKILL.md` containing YAML frontmatter (`name`, `description`) plus an instruction body. `parseSkillMd()` enforces lowercase-hyphen names (≤64 chars), description ≤1024 chars, file ≤256KB [1](#0-0) 
- **Built-in skills directory**: the repo ships examples under `skills/` (e.g. `skills/phone-harness/`) with a `SKILL.md` plus a `manifest.json` carrying `id`, `version`, `triggerTerms`, and `requiredCapabilities` [2](#0-1) 
- **Library + fetch layers**: `server/skill-library.ts` and `server/skill-fetch.ts` already handle remote skill catalogs/imports, and `server/skill-learn.ts` lets bots author skills via `/learn` into a staged review queue.
- **MCP bridge**: `scripts/mcp-server.ts` exposes the whole bot team to external orchestrators (list bots, send messages, create tasks) — this is the "vice versa" direction [3](#0-2) 

## Tips for the database design

1. **Keep SKILL.md as the canonical artifact.** OpenMausBot deliberately imports *only* `SKILL.md` — supporting scripts are stripped and named in warnings, because registry audits found exfiltration payloads in public skills. If your DB stores multi-file skills, expect OMB to ignore everything but SKILL.md; keep auxiliary files optional [4](#0-3) 

2. **Add a manifest layer, not a new format.** Follow the `manifest.json` pattern already in `skills/phone-harness`: version, `triggerTerms` for discovery/routing, and `requiredCapabilities` (e.g. `phoneMcp`) so agents can filter skills they can actually execute [5](#0-4) 

3. **Store provenance + integrity fields.** OMB records `source` URL and `sha256` per skill, and *blocks enablement* if stored bytes change after review. Your DB should expose content hashes so OMB imports stay tamper-evident [6](#0-5) 

4. **Design for "disabled by default."** Imported skills land `enabled: false` and nothing reaches a prompt until a human approves. Don't build auto-install/sync flows — expose a catalog the user browses and explicitly enables [7](#0-6) 

5. **Pre-empt the static scanner.** `scanSkillText()` flags base64 blobs, `curl|sh` pipes, and invisible Unicode. Validate submissions server-side with the same rules so your DB doesn't distribute skills that always show warnings [8](#0-7) 

6. **Reuse the discovery symlinks.** Enabled skills get symlinked into `.claude/skills`, `.agents/skills`, `.grok/skills` in the bot workspace — so Claude Code, Codex-style agents, and Grok discover them natively. Your DB format works with other agents *for free* if you stay spec-compliant [9](#0-8) 

7. **For the reverse direction (external agents → OMB)**, don't push skills into bots directly. Either expose your DB as an MCP server that bots mount, or let external agents use the existing `scripts/mcp-server.ts` tools to message a bot and trigger `/learn`, which stages the skill for human review [10](#0-9) 

8. **Mind the index budget.** Only ~30 skills / 4KB of name+description lines ride the system prompt; bodies are read on demand from files. Rank and curate rather than bulk-importing [11](#0-10) 

A pragmatic shape: a Git repo (or HTTP API) of `skill-name/{SKILL.md, manifest.json}` folders, each with sha256 + version, validated against `parseSkillMd`/`scanSkillText` rules on ingestion, consumable both by OMB's existing import path and by any agent that reads `.agents/skills`-style directories.

### Citations

**File:** server/skills.ts (L12-14)
```typescript
//   - imports land DISABLED. The UI shows the full SKILL.md and the scan
//     warnings; a person enables it after reading. Nothing an import
//     contains reaches any prompt before that.
```

**File:** server/skills.ts (L24-27)
```typescript
// Agent-authored skills (/learn + skill_manage) use the same store, but
// land in staged.json first. A person confirms the in-app card before
// applyStagedSkillWrite promotes and enables the exact bytes the person
// reviewed.
```

**File:** server/skills.ts (L56-76)
```typescript
/** Spec rule: lowercase alphanumerics with single hyphens, 1-64 chars,
 * folder name must equal it. The regex IS the traversal gate — no dots, no
 * slashes, no way to name a skill "..". */
const SKILL_NAME = /^[a-z0-9]+(?:-[a-z0-9]+)*$/;
export const SKILL_NAME_MAX = 64;
export const DESCRIPTION_MAX = 1024;
/** One SKILL.md may be at most this large; the spec recommends <5k tokens. */
export const SKILL_FILE_MAX_BYTES = 256 * 1024;
/** Index budget: name+description lines only, ~100 tokens per skill. */
export const INDEX_MAX_SKILLS = 30;
export const INDEX_MAX_BYTES = 4_000;
/** Agent-authored writes sit here until a person confirms the in-app card. */
export const MAX_STAGED_SKILLS = 20;
export const STAGED_GIST_MAX = 240;
/** Learned skills are duplicated onto their durable review card. Keep that
 * exact review payload bounded while leaving fetched skill imports unchanged. */
export const STAGED_SKILL_FILE_MAX_BYTES = 32 * 1024;

export function isSkillName(name: string): boolean {
  return name.length >= 1 && name.length <= SKILL_NAME_MAX && SKILL_NAME.test(name);
}
```

**File:** server/skills.ts (L119-133)
```typescript
export function scanSkillText(raw: string): string[] {
  const warnings: string[] = [];
  if (/[A-Za-z0-9+/]{120,}={0,2}/.test(raw)) {
    warnings.push("contains a long base64-looking blob — a common wrapper for hidden instructions or payloads");
  }
  if (/\b(curl|wget)\b[^\n]{0,200}\|\s*(ba|z|da)?sh\b/.test(raw)) {
    warnings.push("pipes a download straight into a shell (curl|sh) — never enable without understanding why");
  }
  // zero-width and bidi-control characters hide text from the reviewer while
  // the model still reads it — the invisible-instruction trick
  if (/[\u200B-\u200F\u202A-\u202E\u2060-\u2064\uFEFF]/.test(raw)) {
    warnings.push("contains invisible Unicode characters (zero-width or bidi controls) — text you cannot see");
  }
  return warnings;
}
```

**File:** server/skills.ts (L135-151)
```typescript
interface SkillManifestEntry {
  description: string;
  enabled: boolean;
  source: string;
  sha256: string;
  importedAt: string;
  license?: string;
  compatibility?: string;
  warnings: string[];
  skippedFiles: string[];
  /** Makes approval replay safe if the process stops after promotion but
   * before the confirmation card is durably settled. Never exposed to agents. */
  appliedStageId?: string;
  /** Immutable workspace revision selected by the protected manifest. Older
   * skills omit this and continue to use skills/<name>. */
  storageRevision?: string;
}
```

**File:** server/skills.ts (L446-449)
```typescript
/** The native discovery dirs of the CLIs bots run. A skill enabled here is
 * linked into each, inside the workspace, so engines with first-class skill
 * support load it themselves with their own progressive disclosure. */
const NATIVE_SKILL_DIRS = [".claude/skills", ".agents/skills", ".grok/skills"];
```

**File:** server/skills.ts (L861-887)
```typescript
function preparedSkillFiles(
  files: Array<{ path: string; content: string }>,
): PreparedSkillFiles | { error: string } {
  const skillMd = files.find((file) => file.path === "SKILL.md" || file.path.endsWith("/SKILL.md"));
  if (!skillMd) return { error: "no SKILL.md found at that location" };
  if (Buffer.byteLength(skillMd.content, "utf8") > SKILL_FILE_MAX_BYTES) {
    return { error: `SKILL.md is larger than ${SKILL_FILE_MAX_BYTES / 1024}KB` };
  }
  const parsed = parseSkillMd(skillMd.content);
  if ("error" in parsed) return parsed;
  const prefix = skillMd.path.slice(0, skillMd.path.length - "SKILL.md".length);
  const skippedFiles = [
    ...new Set(
      files
        .filter((file) => file !== skillMd)
        .map((file) => {
          const relative = file.path.startsWith(prefix) ? file.path.slice(prefix.length) : file.path;
          return relative || file.path;
        }),
    ),
  ];
  const warnings = [
    ...scanSkillText(skillMd.content),
    ...skippedFiles.map((path) => `skipped supporting file "${path}" — v1 imports only SKILL.md`),
  ];
  return { files: [{ path: "SKILL.md", content: skillMd.content }], parsed, warnings, skippedFiles };
}
```

**File:** skills/phone-harness/manifest.json (L1-17)
```json
{
  "id": "phone-harness",
  "name": "Phone Harness",
  "version": "0.1.0",
  "description": "Control a physical Android phone connected over authorized USB debugging.",
  "defaultEnabled": true,
  "triggerTerms": [
    "android",
    "usb phone",
    "usb debugging",
    "adb",
    "my phone",
    "mobile app",
    "on the phone"
  ],
  "requiredCapabilities": ["phoneMcp"]
}
```

**File:** scripts/mcp-server.ts (L150-200)
```typescript
      properties: {},
      additionalProperties: false,
    },
    annotations: READ_ONLY,
  },
  {
    name: "list_bots",
    description: "List bots, their current status, active task, and available tasks without loading transcripts.",
    inputSchema: {
      type: "object",
      properties: {},
      additionalProperties: false,
    },
    annotations: READ_ONLY,
  },
  {
    name: "get_bot_messages",
    description: "Retrieve a bounded page of recent messages from one bot task. Images are never returned inline.",
    inputSchema: {
      type: "object",
      properties: {
        bot_id: { type: "string", description: "The ID of the bot." },
        task_id: { type: "string", description: "Optional task/thread ID. Defaults to the bot's active task." },
        limit: { type: "integer", minimum: 1, maximum: 200, description: "Messages to retrieve (default: 30, max: 200)." },
      },
      required: ["bot_id"],
      additionalProperties: false,
    },
    annotations: READ_ONLY,
  },
  {
    name: "send_bot_message",
    description: "Send an instruction to one bot task without changing the selected task. This may cause the bot to use external tools.",
    inputSchema: {
      type: "object",
      properties: {
        bot_id: { type: "string", description: "The ID of the bot to message." },
        task_id: { type: "string", description: "Optional owned task/thread ID. Defaults to the bot's selected task." },
        text: { type: "string", description: "The message content/instruction to send." },
      },
      required: ["bot_id", "text"],
      additionalProperties: false,
    },
    annotations: AGENT_ACTION,
  },
  {
    name: "create_bot",
    description: "Create a new bot and optionally configure its profile, section, and exact model selection.",
    inputSchema: {
      type: "object",
      properties: {
```
