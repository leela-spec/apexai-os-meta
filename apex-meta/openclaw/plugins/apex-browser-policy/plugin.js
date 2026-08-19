import { lstat, readFile } from "node:fs/promises";
import { isAbsolute, join } from "node:path";

import { authorizeBrowserCall, policyFileName, validatePolicy } from "./policy.js";

const MAX_POLICY_BYTES = 8192;

async function loadPolicy(policyDir, sessionKey) {
  if (!isAbsolute(policyDir)) return null;
  const path = join(policyDir, policyFileName(sessionKey));
  try {
    const metadata = await lstat(path);
    if (!metadata.isFile() || metadata.isSymbolicLink() || metadata.size > MAX_POLICY_BYTES) return null;
    return JSON.parse(await readFile(path, "utf8"));
  } catch {
    return null;
  }
}

function block(reason) {
  return { block: true, blockReason: reason };
}

export function registerApexBrowserPolicy(api) {
  const policyDir = api.pluginConfig?.policyDir;
  api.on(
    "before_tool_call",
    async (event, ctx) => {
      if (event.toolName !== "browser" || ctx.agentId !== "apex-executor") return;
      if (typeof ctx.sessionKey !== "string" || ctx.sessionKey.length === 0) {
        return block("APEX_BROWSER_POLICY: missing session identity");
      }
      const policy = await loadPolicy(policyDir, ctx.sessionKey);
      if (!policy) return block("APEX_BROWSER_POLICY: missing policy");
      if (!validatePolicy(policy)) return block("APEX_BROWSER_POLICY: invalid policy");

      // Live per-call tab re-inspection was removed: it required the Gateway's
      // "browser.request" method, which is reserved for operator.admin scope.
      // api.runtime.gateway.request() only ever grants operator.write scope to
      // plugins, so that call could never succeed. The dispatcher already
      // queries live tabs with real admin scope (via the CLI) once, before
      // writing this policy file, and pins tab_id/hostname/profile into it.
      const decision = authorizeBrowserCall({
        agentId: ctx.agentId,
        sessionKey: ctx.sessionKey,
        params: event.params,
        policy,
      });
      if (!decision.ok) return block(decision.reason);
    },
    { priority: 100, timeoutMs: 10000 },
  );
}
