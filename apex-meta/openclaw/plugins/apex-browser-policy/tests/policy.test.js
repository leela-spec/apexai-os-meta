import assert from "node:assert/strict";
import test from "node:test";

import { authorizeBrowserCall, policyFileName } from "../policy.js";

const sessionKey = "agent:apex-executor:apex-0123456789abcdef";
const now = Date.parse("2026-08-10T20:00:00.000Z");

function policy(overrides = {}) {
  return {
    schema_version: "apex.browser-policy/v1",
    execution_id: "exec-20260810-001",
    agent_id: "apex-executor",
    session_key: sessionKey,
    browser_profile: "chrome",
    hostname: "www.perplexity.ai",
    tab_id: "t2",
    expires_at: "2026-08-10T20:05:00.000Z",
    ...overrides,
  };
}

function authorize(params, overrides = {}) {
  return authorizeBrowserCall({
    agentId: "apex-executor",
    sessionKey,
    params,
    policy: policy(overrides.policy),
    now,
  });
}

test("policy file name is a fixed lowercase SHA-256 name", () => {
  assert.equal(
    policyFileName(sessionKey),
    "413467709284c4561b953e103d5167f89ec053c7948e270cc3afd876fd87bc19.json",
  );
});

test("allows observation and bounded actions on the frozen tab", () => {
  assert.deepEqual(authorize({ action: "tabs", profile: "chrome" }), { ok: true });
  assert.deepEqual(
    authorize({ action: "snapshot", profile: "chrome", targetId: "t2" }),
    { ok: true },
  );
  assert.deepEqual(
    authorize({
      action: "act",
      profile: "chrome",
      request: { kind: "click", targetId: "t2", ref: "e291" },
    }),
    { ok: true },
  );
  assert.deepEqual(
    authorize({
      action: "navigate",
      profile: "chrome",
      targetId: "t2",
      targetUrl: "https://www.perplexity.ai/",
    }),
    { ok: true },
  );
});

test("fails closed for missing malformed or expired policy", () => {
  assert.match(
    authorizeBrowserCall({
      agentId: "apex-executor",
      sessionKey,
      params: { action: "tabs", profile: "chrome" },
      policy: null,
      now,
    }).reason,
    /missing policy/,
  );
  assert.match(
    authorize({ action: "tabs", profile: "chrome" }, {
      policy: { schema_version: "apex.browser-policy/v2" },
    }).reason,
    /invalid policy/,
  );
  assert.match(
    authorize({ action: "tabs", profile: "chrome" }, {
      policy: { expires_at: "2026-08-10T19:59:59.000Z" },
    }).reason,
    /expired policy/,
  );
});

test("rejects wrong agent session profile and tab", () => {
  const wrongAgent = authorizeBrowserCall({
    agentId: "other-agent",
    sessionKey,
    params: { action: "tabs", profile: "chrome" },
    policy: policy(),
    now,
  });
  assert.match(wrongAgent.reason, /agent mismatch/);

  const wrongSession = authorizeBrowserCall({
    agentId: "apex-executor",
    sessionKey: "agent:apex-executor:wrong",
    params: { action: "tabs", profile: "chrome" },
    policy: policy(),
    now,
  });
  assert.match(wrongSession.reason, /session mismatch/);

  assert.match(authorize({ action: "tabs", profile: "user" }).reason, /profile mismatch/);
  assert.match(
    authorize({ action: "snapshot", profile: "chrome", targetId: "t9" }).reason,
    /tab mismatch/,
  );
});

test("rejects cross-host navigation and unneeded browser authority", () => {
  assert.match(
    authorize({
      action: "navigate",
      profile: "chrome",
      targetId: "t2",
      targetUrl: "https://chatgpt.com/",
    }).reason,
    /navigation hostname mismatch/,
  );
  assert.match(
    authorize({ action: "open", profile: "chrome", targetUrl: "https://www.perplexity.ai/" }).reason,
    /action is not permitted/,
  );
  assert.match(
    authorize({
      action: "act",
      profile: "chrome",
      request: { kind: "evaluate", targetId: "t2", fn: "() => location.href" },
    }).reason,
    /act kind is not permitted/,
  );
});

test("requires an explicit frozen target for consequential actions", () => {
  assert.match(
    authorize({ action: "snapshot", profile: "chrome" }).reason,
    /targetId is required/,
  );
  assert.match(
    authorize({ action: "act", profile: "chrome", request: { kind: "click", ref: "e291" } }).reason,
    /targetId is required/,
  );
});
