"use strict";

const { describe, it } = require("node:test");
const assert = require("node:assert/strict");
const {
  truthyConfirmed,
  isSkillWriteConfirmEnabled,
  isMutatingMethod,
  confirmOrNull,
} = require("./opSkillWriteConfirm.js");

describe("opSkillWriteConfirm", () => {
  it("truthyConfirmed accepts ja/yes/true/1", () => {
    for (const v of ["1", "true", "yes", "ja", "JA", " True "]) {
      assert.equal(truthyConfirmed({ confirmed: v }), true);
    }
    assert.equal(truthyConfirmed({ confirmed: "false" }), false);
    assert.equal(truthyConfirmed({}), false);
  });

  it("isSkillWriteConfirmEnabled defaults on; OP_SKILL overrides LEXICON", () => {
    assert.equal(isSkillWriteConfirmEnabled({}), true);
    assert.equal(isSkillWriteConfirmEnabled({ LEXICON_OP_WRITE_CONFIRM: "1" }), true);
    assert.equal(isSkillWriteConfirmEnabled({ LEXICON_OP_WRITE_CONFIRM: "0" }), false);
    assert.equal(
      isSkillWriteConfirmEnabled({
        LEXICON_OP_WRITE_CONFIRM: "0",
        OP_SKILL_WRITE_CONFIRM: "1",
      }),
      true
    );
    assert.equal(
      isSkillWriteConfirmEnabled({
        LEXICON_OP_WRITE_CONFIRM: "1",
        OP_SKILL_WRITE_CONFIRM: "0",
      }),
      false
    );
  });

  it("isMutatingMethod covers PATCH PUT DELETE only (POST create free)", () => {
    for (const m of ["PATCH", "put", "DELETE"]) {
      assert.equal(isMutatingMethod(m), true);
    }
    assert.equal(isMutatingMethod("POST"), false);
    assert.equal(isMutatingMethod("GET"), false);
    assert.equal(isMutatingMethod("HEAD"), false);
  });

  it("confirmOrNull blocks mutating without confirmed", () => {
    const msg = confirmOrNull({
      hubId: "openproject-work-packages",
      operation: "delete",
      method: "DELETE",
      args: { id: "42" },
      env: { OP_SKILL_WRITE_CONFIRM: "1" },
    });
    assert.equal(typeof msg, "string");
    assert.match(msg, /Bestätigung erforderlich/);
    assert.match(msg, /confirmed=true/);
    assert.match(msg, /id=42/);
    assert.match(msg, /openproject-work-packages/);
  });

  it("confirmOrNull allows GET, POST create, and confirmed writes", () => {
    assert.equal(
      confirmOrNull({
        hubId: "openproject-work-packages",
        operation: "get",
        method: "GET",
        args: { id: "1" },
        env: { OP_SKILL_WRITE_CONFIRM: "1" },
      }),
      null
    );
    assert.equal(
      confirmOrNull({
        hubId: "openproject-work-packages",
        operation: "create",
        method: "POST",
        args: { subject: "Neu" },
        env: { OP_SKILL_WRITE_CONFIRM: "1" },
      }),
      null
    );
    assert.equal(
      confirmOrNull({
        hubId: "openproject-work-packages",
        operation: "delete",
        method: "DELETE",
        args: { id: "1", confirmed: "true" },
        env: { OP_SKILL_WRITE_CONFIRM: "1" },
      }),
      null
    );
  });

  it("confirmOrNull is off when gate disabled", () => {
    assert.equal(
      confirmOrNull({
        hubId: "openproject-projects",
        operation: "create",
        method: "POST",
        args: { name: "x" },
        env: { OP_SKILL_WRITE_CONFIRM: "0" },
      }),
      null
    );
  });
});
