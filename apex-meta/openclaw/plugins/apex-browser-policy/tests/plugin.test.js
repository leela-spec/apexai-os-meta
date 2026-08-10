import assert from "node:assert/strict";
import { mkdir, mkdtemp, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";

import { policyFileName } from "../policy.js";
import { registerApexBrowserPolicy } from "../plugin.js";

const sessionKey = "agent:apex-executor:apex-0123456789abcdef";

function policy() {
  return {
    schema_version: "apex.browser-policy/v1",
    execution_id: "exec-20260810-001",
    agent_id: "apex-executor",
    session_key: sessionKey,
    browser_profile: "chrome",
    hostname: "www.perplexity.ai",
    tab_id: "t2",
    expires_at: "2099-08-10T20:05:00.000Z",
  };
}

function fakeApi(policyDir, tabs) {
  const hooks = new Map();
  const requests = [];
  return {
    api: {
      pluginConfig: { policyDir },
      runtime: {
        gateway: {
          request: async (method, params) => {
            requests.push({ method, params });
            return { tabs };
          },
        },
      },
      on: (name, handler) => hooks.set(name, handler),
    },
    hooks,
    requests,
  };
}

test("registered hook loads the session policy and checks live tabs", async () => {
  const dir = await mkdtemp(join(tmpdir(), "apex-browser-policy-"));
  try {
    await mkdir(dir, { recursive: true });
    await writeFile(join(dir, policyFileName(sessionKey)), JSON.stringify(policy()), "utf8");
    const fixture = fakeApi(dir, [{
      targetId: "raw-target",
      tabId: "t2",
      suggestedTargetId: "t2",
      type: "page",
      url: "https://www.perplexity.ai/",
    }]);
    registerApexBrowserPolicy(fixture.api);
    const hook = fixture.hooks.get("before_tool_call");
    assert.equal(typeof hook, "function");

    const result = await hook(
      { toolName: "browser", params: { action: "tabs", profile: "chrome" } },
      { agentId: "apex-executor", sessionKey, toolName: "browser" },
    );
    assert.equal(result, undefined);
    assert.deepEqual(fixture.requests, [{
      method: "browser.request",
      params: { method: "GET", path: "/tabs", query: { profile: "chrome" }, timeoutMs: 5000 },
    }]);
  } finally {
    await rm(dir, { recursive: true, force: true });
  }
});

test("registered hook fails closed when the policy is absent", async () => {
  const dir = await mkdtemp(join(tmpdir(), "apex-browser-policy-"));
  try {
    const fixture = fakeApi(dir, []);
    registerApexBrowserPolicy(fixture.api);
    const result = await fixture.hooks.get("before_tool_call")(
      { toolName: "browser", params: { action: "tabs", profile: "chrome" } },
      { agentId: "apex-executor", sessionKey, toolName: "browser" },
    );
    assert.equal(result.block, true);
    assert.match(result.blockReason, /missing policy/);
    assert.equal(fixture.requests.length, 0);
  } finally {
    await rm(dir, { recursive: true, force: true });
  }
});

test("hook ignores non-browser calls and agents outside apex-executor", async () => {
  const fixture = fakeApi("C:\\missing", []);
  registerApexBrowserPolicy(fixture.api);
  const hook = fixture.hooks.get("before_tool_call");
  assert.equal(
    await hook({ toolName: "read", params: {} }, { agentId: "apex-executor", sessionKey, toolName: "read" }),
    undefined,
  );
  assert.equal(
    await hook({ toolName: "browser", params: {} }, { agentId: "other", sessionKey, toolName: "browser" }),
    undefined,
  );
});

test("hook blocks when live tab inspection fails", async () => {
  const dir = await mkdtemp(join(tmpdir(), "apex-browser-policy-"));
  try {
    await writeFile(join(dir, policyFileName(sessionKey)), JSON.stringify(policy()), "utf8");
    const fixture = fakeApi(dir, []);
    fixture.api.runtime.gateway.request = async () => {
      throw new Error("relay unavailable");
    };
    registerApexBrowserPolicy(fixture.api);
    const result = await fixture.hooks.get("before_tool_call")(
      { toolName: "browser", params: { action: "tabs", profile: "chrome" } },
      { agentId: "apex-executor", sessionKey, toolName: "browser" },
    );
    assert.equal(result.block, true);
    assert.match(result.blockReason, /live tab inspection failed/);
  } finally {
    await rm(dir, { recursive: true, force: true });
  }
});
