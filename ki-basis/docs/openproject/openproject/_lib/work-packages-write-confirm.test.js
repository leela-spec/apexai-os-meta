"use strict";

const { describe, it, before, after } = require("node:test");
const assert = require("node:assert/strict");
const path = require("node:path");

describe("openproject-work-packages write confirm gate", () => {
  let handler;
  let calls;
  let prevFetch;

  before(() => {
    prevFetch = globalThis.fetch;
    calls = [];
    globalThis.fetch = async (url, opts) => {
      calls.push({ url: String(url), method: opts && opts.method });
      return {
        ok: true,
        status: 200,
        async text() {
          return JSON.stringify({ id: 1, _type: "WorkPackage", subject: "x" });
        },
      };
    };
    // fresh require
    const hp = path.join(__dirname, "../openproject-work-packages/handler.js");
    delete require.cache[require.resolve(hp)];
    delete require.cache[require.resolve("./opSkillWriteConfirm.js")];
    handler = require(hp).runtime.handler.bind({
      runtimeArgs: {
        openproject_base_url: "http://op.test",
        openproject_token: "tok",
      },
    });
  });

  after(() => {
    globalThis.fetch = prevFetch;
  });

  it("blocks delete without confirmed (no fetch)", async () => {
    calls.length = 0;
    const out = await handler({ operation: "delete", id: 99 });
    assert.match(String(out), /Bestätigung erforderlich/);
    assert.equal(calls.length, 0);
  });

  it("allows delete with confirmed=true (fetch once)", async () => {
    calls.length = 0;
    const out = await handler({ operation: "delete", id: 99, confirmed: "true" });
    assert.equal(calls.length, 1);
    assert.equal(calls[0].method, "DELETE");
    assert.match(String(out), /Betreff|Gelöscht|1/);
  });

  it("allows create (POST) without confirmed", async () => {
    calls.length = 0;
    const out = await handler({
      operation: "create",
      id: "8",
      subject: "Neu ohne Confirm",
    });
    assert.equal(calls.length, 1);
    assert.equal(calls[0].method, "POST");
    assert.doesNotMatch(String(out), /Bestätigung erforderlich/);
  });

  it("allows get without confirmed", async () => {
    calls.length = 0;
    await handler({ operation: "get", id: 7 });
    assert.equal(calls.length, 1);
    assert.equal(calls[0].method, "GET");
  });

  it("knownArgs allows confirmed on update (does not reject unknown arg)", async () => {
    const out = await handler({
      operation: "update",
      id: 99,
      subject: "x",
      lockVersion: 1,
      confirmed: "true",
    });
    // either success string or confirm/network — must NOT be unknown-arg rejection
    assert.ok(typeof out === "string");
    assert.doesNotMatch(String(out), /Unknown argument.*confirmed|unbekannte.*confirmed/i);
  });
});
