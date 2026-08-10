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

      let liveTabs;
      try {
        const result = await api.runtime.gateway.request("browser.request", {
          method: "GET",
          path: "/tabs",
          query: { profile: policy.browser_profile },
          timeoutMs: 5000,
        });
        liveTabs = result?.tabs;
      } catch {
        return block("APEX_BROWSER_POLICY: live tab inspection failed");
      }

      const decision = authorizeBrowserCall({
        agentId: ctx.agentId,
        sessionKey: ctx.sessionKey,
        params: event.params,
        policy,
        tabs: liveTabs,
      });
      if (!decision.ok) return block(decision.reason);
    },
    { priority: 100, timeoutMs: 10000 },
  );
}
