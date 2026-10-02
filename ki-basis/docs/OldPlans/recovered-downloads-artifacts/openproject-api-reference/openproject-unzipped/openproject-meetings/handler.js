const { confirmOrNull } = require("../_lib/opSkillWriteConfirm.js");

module.exports.runtime = {
  handler: async function (args) {
    args = args || {};
    const runtime = this.runtimeArgs || {};
    const base = (runtime.openproject_base_url || "http://web:8080").replace(/\/+$/, "");
    const token = runtime.openproject_token || "";
    const basic = `Basic ${Buffer.from(`apikey:${token}`).toString("base64")}`;
    const headers = { Authorization: basic, Accept: "application/json" };
    const operation = String(args.operation || "").trim();
    if (!operation) return "Bitte operation angeben.";

    const requireArgs = (names) => {
      for (const n of names) {
        if (args[n] === undefined || args[n] === null || args[n] === "") {
          return `Pflichtfeld fehlt für operation=${operation}: ${n}`;
        }
      }
      return null;
    };

    let method, path, body, missing;
    switch (operation) {
      case "create_agenda_item":
      {
        if (args.durationInMinutes !== undefined && args.durationInMinutes !== null && String(args.durationInMinutes).trim() !== "") {
          const _n = Number(args.durationInMinutes);
          if (!Number.isFinite(_n) || !Number.isInteger(_n)) {
            return `durationInMinutes muss eine ganze Zahl sein (got: ${args.durationInMinutes})`;
          }
        }
      }
      {
        if (args.lockVersion !== undefined && args.lockVersion !== null && String(args.lockVersion).trim() !== "") {
          const _n = Number(args.lockVersion);
          if (!Number.isFinite(_n) || !Number.isInteger(_n)) {
            return `lockVersion muss eine ganze Zahl sein (got: ${args.lockVersion})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/meeting_agenda_items`;
      {
        const knownArgs = new Set(["operation", "confirmed", "title", "notes", "durationInMinutes", "itemType", "lockVersion", "id", "kind", "location", "startTime", "duration", "state", "sharing", "template", "notify", "meeting_id", "agenda_item_id", "project_id", "project", "participant_ids"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.title !== undefined && args.title !== null && String(args.title).trim() !== "") {
        body["title"] = args.title;
      }
      if (args.notes !== undefined && args.notes !== null && String(args.notes).trim() !== "") {
        let _v_notes = args.notes;
        if (typeof _v_notes === "string") {
          const _s = String(_v_notes).trim();
          if (_s.startsWith("{") || _s.startsWith("[")) {
            try { _v_notes = JSON.parse(_s); }
            catch (e) { _v_notes = { raw: _s }; }
          } else {
            _v_notes = { raw: _s };
          }
        }
        if (typeof _v_notes !== "object" || _v_notes === null || Array.isArray(_v_notes)) {
          return `notes muss ein Objekt sein (z.B. Formattable mit raw: string)`;
        }
        if (typeof _v_notes.format !== "string") {
          return `notes.format fehlt oder ist kein string`;
        }
        if (_v_notes.raw !== undefined && _v_notes.raw !== null && typeof _v_notes.raw !== "string") {
          return `notes.raw muss ein string sein`;
        }
        if (_v_notes.html !== undefined && _v_notes.html !== null && typeof _v_notes.html !== "string") {
          return `notes.html muss ein string sein`;
        }
        body["notes"] = _v_notes;
      }
      if (args.durationInMinutes !== undefined && args.durationInMinutes !== null && String(args.durationInMinutes).trim() !== "") {
        {
          const _n = Number(args.durationInMinutes);
          body["durationInMinutes"] = Number.isNaN(_n) ? args.durationInMinutes : _n;
        }
      }
      if (args.itemType !== undefined && args.itemType !== null && String(args.itemType).trim() !== "") {
        {
          const _allowed = ["simple", "work_package"];
          if (!_allowed.includes(String(args.itemType))) {
            return `itemType muss einer von: ${_allowed.join(", ")} sein (got: ${args.itemType})`;
          }
        }
        body["itemType"] = args.itemType;
      }
      if (args.lockVersion !== undefined && args.lockVersion !== null && String(args.lockVersion).trim() !== "") {
        {
          const _n = Number(args.lockVersion);
          body["lockVersion"] = Number.isNaN(_n) ? args.lockVersion : _n;
        }
      }
      break;

      case "delete_agenda_item":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "DELETE"; path = `/api/v3/meeting_agenda_items/${encodeURIComponent(args.id)}`;
      break;

      case "get_agenda_item":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/meeting_agenda_items/${encodeURIComponent(args.id)}`;
      break;

      case "update_agenda_item":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      {
        if (args.durationInMinutes !== undefined && args.durationInMinutes !== null && String(args.durationInMinutes).trim() !== "") {
          const _n = Number(args.durationInMinutes);
          if (!Number.isFinite(_n) || !Number.isInteger(_n)) {
            return `durationInMinutes muss eine ganze Zahl sein (got: ${args.durationInMinutes})`;
          }
        }
      }
      {
        if (args.lockVersion !== undefined && args.lockVersion !== null && String(args.lockVersion).trim() !== "") {
          const _n = Number(args.lockVersion);
          if (!Number.isFinite(_n) || !Number.isInteger(_n)) {
            return `lockVersion muss eine ganze Zahl sein (got: ${args.lockVersion})`;
          }
        }
      }
      method = "PATCH"; path = `/api/v3/meeting_agenda_items/${encodeURIComponent(args.id)}`;
      {
        const knownArgs = new Set(["operation", "confirmed", "title", "notes", "durationInMinutes", "itemType", "lockVersion", "id", "kind", "location", "startTime", "duration", "state", "sharing", "template", "notify", "meeting_id", "agenda_item_id", "project_id", "project", "participant_ids"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.title !== undefined && args.title !== null && String(args.title).trim() !== "") {
        body["title"] = args.title;
      }
      if (args.notes !== undefined && args.notes !== null && String(args.notes).trim() !== "") {
        let _v_notes = args.notes;
        if (typeof _v_notes === "string") {
          const _s = String(_v_notes).trim();
          if (_s.startsWith("{") || _s.startsWith("[")) {
            try { _v_notes = JSON.parse(_s); }
            catch (e) { _v_notes = { raw: _s }; }
          } else {
            _v_notes = { raw: _s };
          }
        }
        if (typeof _v_notes !== "object" || _v_notes === null || Array.isArray(_v_notes)) {
          return `notes muss ein Objekt sein (z.B. Formattable mit raw: string)`;
        }
        if (typeof _v_notes.format !== "string") {
          return `notes.format fehlt oder ist kein string`;
        }
        if (_v_notes.raw !== undefined && _v_notes.raw !== null && typeof _v_notes.raw !== "string") {
          return `notes.raw muss ein string sein`;
        }
        if (_v_notes.html !== undefined && _v_notes.html !== null && typeof _v_notes.html !== "string") {
          return `notes.html muss ein string sein`;
        }
        body["notes"] = _v_notes;
      }
      if (args.durationInMinutes !== undefined && args.durationInMinutes !== null && String(args.durationInMinutes).trim() !== "") {
        {
          const _n = Number(args.durationInMinutes);
          body["durationInMinutes"] = Number.isNaN(_n) ? args.durationInMinutes : _n;
        }
      }
      if (args.itemType !== undefined && args.itemType !== null && String(args.itemType).trim() !== "") {
        {
          const _allowed = ["simple", "work_package"];
          if (!_allowed.includes(String(args.itemType))) {
            return `itemType muss einer von: ${_allowed.join(", ")} sein (got: ${args.itemType})`;
          }
        }
        body["itemType"] = args.itemType;
      }
      if (args.lockVersion !== undefined && args.lockVersion !== null && String(args.lockVersion).trim() !== "") {
        {
          const _n = Number(args.lockVersion);
          body["lockVersion"] = Number.isNaN(_n) ? args.lockVersion : _n;
        }
      }
      break;

      case "create_outcome":
      method = "POST"; path = `/api/v3/meeting_outcomes`;
      {
        const knownArgs = new Set(["operation", "confirmed", "title", "notes", "durationInMinutes", "itemType", "lockVersion", "id", "kind", "location", "startTime", "duration", "state", "sharing", "template", "notify", "meeting_id", "agenda_item_id", "project_id", "project", "participant_ids"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.kind !== undefined && args.kind !== null && String(args.kind).trim() !== "") {
        {
          const _allowed = ["information", "work_package"];
          if (!_allowed.includes(String(args.kind))) {
            return `kind muss einer von: ${_allowed.join(", ")} sein (got: ${args.kind})`;
          }
        }
        body["kind"] = args.kind;
      }
      if (args.notes !== undefined && args.notes !== null && String(args.notes).trim() !== "") {
        let _v_notes = args.notes;
        if (typeof _v_notes === "string") {
          const _s = String(_v_notes).trim();
          if (_s.startsWith("{") || _s.startsWith("[")) {
            try { _v_notes = JSON.parse(_s); }
            catch (e) { _v_notes = { raw: _s }; }
          } else {
            _v_notes = { raw: _s };
          }
        }
        if (typeof _v_notes !== "object" || _v_notes === null || Array.isArray(_v_notes)) {
          return `notes muss ein Objekt sein (z.B. Formattable mit raw: string)`;
        }
        if (typeof _v_notes.format !== "string") {
          return `notes.format fehlt oder ist kein string`;
        }
        if (_v_notes.raw !== undefined && _v_notes.raw !== null && typeof _v_notes.raw !== "string") {
          return `notes.raw muss ein string sein`;
        }
        if (_v_notes.html !== undefined && _v_notes.html !== null && typeof _v_notes.html !== "string") {
          return `notes.html muss ein string sein`;
        }
        body["notes"] = _v_notes;
      }
      break;

      case "delete_outcome":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "DELETE"; path = `/api/v3/meeting_outcomes/${encodeURIComponent(args.id)}`;
      break;

      case "get_outcome":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/meeting_outcomes/${encodeURIComponent(args.id)}`;
      break;

      case "update_outcome":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "PATCH"; path = `/api/v3/meeting_outcomes/${encodeURIComponent(args.id)}`;
      {
        const knownArgs = new Set(["operation", "confirmed", "title", "notes", "durationInMinutes", "itemType", "lockVersion", "id", "kind", "location", "startTime", "duration", "state", "sharing", "template", "notify", "meeting_id", "agenda_item_id", "project_id", "project", "participant_ids"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.kind !== undefined && args.kind !== null && String(args.kind).trim() !== "") {
        {
          const _allowed = ["information", "work_package"];
          if (!_allowed.includes(String(args.kind))) {
            return `kind muss einer von: ${_allowed.join(", ")} sein (got: ${args.kind})`;
          }
        }
        body["kind"] = args.kind;
      }
      if (args.notes !== undefined && args.notes !== null && String(args.notes).trim() !== "") {
        let _v_notes = args.notes;
        if (typeof _v_notes === "string") {
          const _s = String(_v_notes).trim();
          if (_s.startsWith("{") || _s.startsWith("[")) {
            try { _v_notes = JSON.parse(_s); }
            catch (e) { _v_notes = { raw: _s }; }
          } else {
            _v_notes = { raw: _s };
          }
        }
        if (typeof _v_notes !== "object" || _v_notes === null || Array.isArray(_v_notes)) {
          return `notes muss ein Objekt sein (z.B. Formattable mit raw: string)`;
        }
        if (typeof _v_notes.format !== "string") {
          return `notes.format fehlt oder ist kein string`;
        }
        if (_v_notes.raw !== undefined && _v_notes.raw !== null && typeof _v_notes.raw !== "string") {
          return `notes.raw muss ein string sein`;
        }
        if (_v_notes.html !== undefined && _v_notes.html !== null && typeof _v_notes.html !== "string") {
          return `notes.html muss ein string sein`;
        }
        body["notes"] = _v_notes;
      }
      break;

      case "create_section":
      method = "POST"; path = `/api/v3/meeting_sections`;
      {
        const knownArgs = new Set(["operation", "confirmed", "title", "notes", "durationInMinutes", "itemType", "lockVersion", "id", "kind", "location", "startTime", "duration", "state", "sharing", "template", "notify", "meeting_id", "agenda_item_id", "project_id", "project", "participant_ids"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.title !== undefined && args.title !== null && String(args.title).trim() !== "") {
        body["title"] = args.title;
      }
      break;

      case "delete_section":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "DELETE"; path = `/api/v3/meeting_sections/${encodeURIComponent(args.id)}`;
      break;

      case "get_section":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/meeting_sections/${encodeURIComponent(args.id)}`;
      break;

      case "update_section":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "PATCH"; path = `/api/v3/meeting_sections/${encodeURIComponent(args.id)}`;
      {
        const knownArgs = new Set(["operation", "confirmed", "title", "notes", "durationInMinutes", "itemType", "lockVersion", "id", "kind", "location", "startTime", "duration", "state", "sharing", "template", "notify", "meeting_id", "agenda_item_id", "project_id", "project", "participant_ids"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.title !== undefined && args.title !== null && String(args.title).trim() !== "") {
        body["title"] = args.title;
      }
      break;

      case "list":
      method = "GET"; path = `/api/v3/meetings`;
      {
        const _qs = new URLSearchParams();
        if (args.offset !== undefined && args.offset !== null && String(args.offset).trim() !== "") _qs.set("offset", String(args.offset));
        if (args.pageSize !== undefined && args.pageSize !== null && String(args.pageSize).trim() !== "") _qs.set("pageSize", String(args.pageSize));
        if (args.filters !== undefined && args.filters !== null && String(args.filters).trim() !== "") _qs.set("filters", String(args.filters));
        if (args.sortBy !== undefined && args.sortBy !== null && String(args.sortBy).trim() !== "") _qs.set("sortBy", String(args.sortBy));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "create":
      {
        if (args.lockVersion !== undefined && args.lockVersion !== null && String(args.lockVersion).trim() !== "") {
          const _n = Number(args.lockVersion);
          if (!Number.isFinite(_n) || !Number.isInteger(_n)) {
            return `lockVersion muss eine ganze Zahl sein (got: ${args.lockVersion})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/meetings`;
      {
        const knownArgs = new Set(["operation", "confirmed", "title", "notes", "durationInMinutes", "itemType", "lockVersion", "id", "kind", "location", "startTime", "duration", "state", "sharing", "template", "notify", "meeting_id", "agenda_item_id", "project_id", "project", "participant_ids"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.title !== undefined && args.title !== null && String(args.title).trim() !== "") {
        body["title"] = args.title;
      }
      if (args.location !== undefined && args.location !== null && String(args.location).trim() !== "") {
        body["location"] = args.location;
      }
      if (args.startTime !== undefined && args.startTime !== null && String(args.startTime).trim() !== "") {
        body["startTime"] = args.startTime;
      }
      if (args.duration !== undefined && args.duration !== null && String(args.duration).trim() !== "") {
        body["duration"] = args.duration;
      }
      if (args.state !== undefined && args.state !== null && String(args.state).trim() !== "") {
        {
          const _allowed = ["open", "draft", "in_progress", "cancelled", "closed"];
          if (!_allowed.includes(String(args.state))) {
            return `state muss einer von: ${_allowed.join(", ")} sein (got: ${args.state})`;
          }
        }
        body["state"] = args.state;
      }
      if (args.sharing !== undefined && args.sharing !== null && String(args.sharing).trim() !== "") {
        {
          const _allowed = ["none", "descendants", "system"];
          if (!_allowed.includes(String(args.sharing))) {
            return `sharing muss einer von: ${_allowed.join(", ")} sein (got: ${args.sharing})`;
          }
        }
        body["sharing"] = args.sharing;
      }
      if (args.template !== undefined && args.template !== null && String(args.template).trim() !== "") {
        {
          const _raw = args.template;
          if (typeof _raw === "boolean") {
            body["template"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `template muss boolean sein (got: ${args.template})`;
            }
            body["template"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.notify !== undefined && args.notify !== null && String(args.notify).trim() !== "") {
        {
          const _raw = args.notify;
          if (typeof _raw === "boolean") {
            body["notify"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `notify muss boolean sein (got: ${args.notify})`;
            }
            body["notify"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.lockVersion !== undefined && args.lockVersion !== null && String(args.lockVersion).trim() !== "") {
        {
          const _n = Number(args.lockVersion);
          body["lockVersion"] = Number.isNaN(_n) ? args.lockVersion : _n;
        }
      }
      {
        const pid = String(args.project_id || args.project || "").trim();
        if (pid) {
          const href = pid.startsWith("/api/") ? pid : `/api/v3/projects/${encodeURIComponent(pid)}`;
          body._links = Object.assign({}, body._links || {}, { project: { href } });
        }
      }
      if (args.participant_ids !== undefined && args.participant_ids !== null && String(args.participant_ids).trim() !== "") {
        const ids = String(args.participant_ids).split(/[\s,]+/).map((s) => s.trim()).filter(Boolean);
        if (ids.length) {
          body._links = Object.assign({}, body._links || {}, {
            participants: ids.map((id) => ({ href: `/api/v3/users/${encodeURIComponent(id)}` })),
          });
        }
      }
      break;

      case "create_form":
      method = "POST"; path = `/api/v3/meetings/form`;
      body = undefined;
      break;

      case "get_schema":
      method = "GET"; path = `/api/v3/meetings/schema`;
      break;

      case "delete":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "DELETE"; path = `/api/v3/meetings/${encodeURIComponent(args.id)}`;
      break;

      case "get":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/meetings/${encodeURIComponent(args.id)}`;
      break;

      case "update":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      {
        if (args.lockVersion !== undefined && args.lockVersion !== null && String(args.lockVersion).trim() !== "") {
          const _n = Number(args.lockVersion);
          if (!Number.isFinite(_n) || !Number.isInteger(_n)) {
            return `lockVersion muss eine ganze Zahl sein (got: ${args.lockVersion})`;
          }
        }
      }
      method = "PATCH"; path = `/api/v3/meetings/${encodeURIComponent(args.id)}`;
      {
        const knownArgs = new Set(["operation", "confirmed", "title", "notes", "durationInMinutes", "itemType", "lockVersion", "id", "kind", "location", "startTime", "duration", "state", "sharing", "template", "notify", "meeting_id", "agenda_item_id", "project_id", "project", "participant_ids"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.title !== undefined && args.title !== null && String(args.title).trim() !== "") {
        body["title"] = args.title;
      }
      if (args.location !== undefined && args.location !== null && String(args.location).trim() !== "") {
        body["location"] = args.location;
      }
      if (args.startTime !== undefined && args.startTime !== null && String(args.startTime).trim() !== "") {
        body["startTime"] = args.startTime;
      }
      if (args.duration !== undefined && args.duration !== null && String(args.duration).trim() !== "") {
        body["duration"] = args.duration;
      }
      if (args.state !== undefined && args.state !== null && String(args.state).trim() !== "") {
        {
          const _allowed = ["open", "draft", "in_progress", "cancelled", "closed"];
          if (!_allowed.includes(String(args.state))) {
            return `state muss einer von: ${_allowed.join(", ")} sein (got: ${args.state})`;
          }
        }
        body["state"] = args.state;
      }
      if (args.sharing !== undefined && args.sharing !== null && String(args.sharing).trim() !== "") {
        {
          const _allowed = ["none", "descendants", "system"];
          if (!_allowed.includes(String(args.sharing))) {
            return `sharing muss einer von: ${_allowed.join(", ")} sein (got: ${args.sharing})`;
          }
        }
        body["sharing"] = args.sharing;
      }
      if (args.template !== undefined && args.template !== null && String(args.template).trim() !== "") {
        {
          const _raw = args.template;
          if (typeof _raw === "boolean") {
            body["template"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `template muss boolean sein (got: ${args.template})`;
            }
            body["template"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.notify !== undefined && args.notify !== null && String(args.notify).trim() !== "") {
        {
          const _raw = args.notify;
          if (typeof _raw === "boolean") {
            body["notify"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `notify muss boolean sein (got: ${args.notify})`;
            }
            body["notify"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.lockVersion !== undefined && args.lockVersion !== null && String(args.lockVersion).trim() !== "") {
        {
          const _n = Number(args.lockVersion);
          body["lockVersion"] = Number.isNaN(_n) ? args.lockVersion : _n;
        }
      }
      break;

      case "list_agenda_items":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/meetings/${encodeURIComponent(args.id)}/agenda_items`;
      break;

      case "update_form":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/meetings/${encodeURIComponent(args.id)}/form`;
      body = undefined;
      break;

      case "list_sections":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/meetings/${encodeURIComponent(args.id)}/sections`;
      break;

      case "list_outcomes":
      missing = requireArgs(["meeting_id", "agenda_item_id"]); if (missing) return missing;
      {
        if (args.meeting_id !== undefined && args.meeting_id !== null && String(args.meeting_id).trim() !== "") {
          const _n = Number(args.meeting_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `meeting_id muss eine ganze Zahl und > 0 sein (got: ${args.meeting_id})`;
          }
        }
      }
      {
        if (args.agenda_item_id !== undefined && args.agenda_item_id !== null && String(args.agenda_item_id).trim() !== "") {
          const _n = Number(args.agenda_item_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `agenda_item_id muss eine ganze Zahl und > 0 sein (got: ${args.agenda_item_id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/meetings/${encodeURIComponent(args.meeting_id)}/agenda_items/${encodeURIComponent(args.agenda_item_id)}/outcomes`;
      break;

      case "get_outcome_by_agenda_item":
      missing = requireArgs(["meeting_id", "agenda_item_id", "id"]); if (missing) return missing;
      {
        if (args.meeting_id !== undefined && args.meeting_id !== null && String(args.meeting_id).trim() !== "") {
          const _n = Number(args.meeting_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `meeting_id muss eine ganze Zahl und > 0 sein (got: ${args.meeting_id})`;
          }
        }
      }
      {
        if (args.agenda_item_id !== undefined && args.agenda_item_id !== null && String(args.agenda_item_id).trim() !== "") {
          const _n = Number(args.agenda_item_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `agenda_item_id muss eine ganze Zahl und > 0 sein (got: ${args.agenda_item_id})`;
          }
        }
      }
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/meetings/${encodeURIComponent(args.meeting_id)}/agenda_items/${encodeURIComponent(args.agenda_item_id)}/outcomes/${encodeURIComponent(args.id)}`;
      break;

      case "get_agenda_item_by":
      missing = requireArgs(["meeting_id", "id"]); if (missing) return missing;
      {
        if (args.meeting_id !== undefined && args.meeting_id !== null && String(args.meeting_id).trim() !== "") {
          const _n = Number(args.meeting_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `meeting_id muss eine ganze Zahl und > 0 sein (got: ${args.meeting_id})`;
          }
        }
      }
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/meetings/${encodeURIComponent(args.meeting_id)}/agenda_items/${encodeURIComponent(args.id)}`;
      break;

      case "get_section_by":
      missing = requireArgs(["meeting_id", "id"]); if (missing) return missing;
      {
        if (args.meeting_id !== undefined && args.meeting_id !== null && String(args.meeting_id).trim() !== "") {
          const _n = Number(args.meeting_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `meeting_id muss eine ganze Zahl und > 0 sein (got: ${args.meeting_id})`;
          }
        }
      }
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/meetings/${encodeURIComponent(args.meeting_id)}/sections/${encodeURIComponent(args.id)}`;
      break;
      default:
        return `Unbekannte operation: ${operation}`;
    }

    const confirmBlock = confirmOrNull({
      hubId: "openproject-meetings",
      operation,
      method,
      args,
    });
    if (confirmBlock) return confirmBlock;

    try {
      const res = await fetch(`${base}${path}`, {
        method,
        headers: body ? { ...headers, "Content-Type": "application/json" } : headers,
        body: body ? JSON.stringify(body) : undefined,
      });
      if (!res.ok) return `OpenProject-Fehler ${res.status}: ${await res.text()}`;
      const _raw = await res.text();
      if (!_raw || !String(_raw).trim()) {
        if (String(method).toUpperCase() === "DELETE") return "Gelöscht.";
        return `(leer, HTTP ${res.status})`;
      }
      let item;
      try { item = JSON.parse(_raw); }
      catch (e) { return `Fehler beim Aufruf von OpenProject: ${e.message}`; }
      // AnythingLLM surfaces skill returns as-is — Markdown table with header.
      // formatHalResponse — Markdown table with header (AnythingLLM shows skill returns as-is).
      // Signature: formatHalResponse(item: object) -> string
      // Handles Collection / *Collection, DRF {count, results}, and single resources.
      // HAL link titles (status/assignee/type/project/parent) + lockVersion for PM update flows.
      const cell = (v) => {
        if (v === null || v === undefined) return "-";
        if (typeof v === "object") {
          if (typeof v.raw === "string") return String(v.raw).replace(/\|/g, "/").replace(/\r?\n/g, " ").slice(0, 80) || "-";
          if (v.title) return String(v.title).replace(/\|/g, "/").replace(/\r?\n/g, " ");
          if (v.href) {
            const m = String(v.href).match(/\/(\d+)(?:\/)?$/);
            return m ? m[1] : String(v.href).replace(/\|/g, "/").slice(-40);
          }
          return "-";
        }
        return String(v).replace(/\|/g, "/").replace(/\r?\n/g, " ");
      };
      const linkTitle = (e, rel) => {
        const l = e && e._links && e._links[rel];
        if (!l) return undefined;
        const node = Array.isArray(l) ? l[0] : l;
        if (!node) return undefined;
        if (node.title) return node.title;
        if (node.href) {
          const m = String(node.href).match(/\/(\d+)(?:\/)?$/);
          return m ? `#${m[1]}` : undefined;
        }
        return undefined;
      };
      const fieldVal = (e, k) => {
        if (!e) return undefined;
        if (e[k] !== undefined && e[k] !== null && typeof e[k] !== "object") return e[k];
        if (k === "status") return linkTitle(e, "status");
        if (k === "assignee") return linkTitle(e, "assignee");
        if (k === "type" || k === "typeName") return linkTitle(e, "type");
        if (k === "project") return linkTitle(e, "project");
        if (k === "parent") return linkTitle(e, "parent");
        if (k === "priority") return linkTitle(e, "priority");
        if (k === "author") return linkTitle(e, "author");
        if (k === "lockVersion" && e.lockVersion !== undefined && e.lockVersion !== null) return e.lockVersion;
        return undefined;
      };
      const hasField = (e, k) => fieldVal(e, k) !== undefined;
      const LABELS = {
        de: {
          id: "ID", name: "Name", subject: "Betreff", title: "Titel", identifier: "Kennung",
          login: "Login", email: "E-Mail", status: "Status", active: "aktiv",
          createdAt: "erstellt", updatedAt: "aktualisiert", firstName: "Vorname", lastName: "Nachname",
          firstname: "Vorname", lastname: "Nachname",
          lockVersion: "lockVersion", assignee: "Assignee", type: "Typ", typeName: "Typ",
          project: "Projekt", parent: "Parent", priority: "Priorität", author: "Autor",
          percentageDone: "%", dueDate: "fällig", startDate: "Start",
        },
        en: {
          id: "ID", name: "Name", subject: "Subject", title: "Title", identifier: "Identifier",
          login: "Login", email: "E-Mail", status: "Status", active: "active",
          createdAt: "created", updatedAt: "updated", firstName: "First name", lastName: "Last name",
          firstname: "First name", lastname: "Last name",
          lockVersion: "lockVersion", assignee: "Assignee", type: "Type", typeName: "Type",
          project: "Project", parent: "Parent", priority: "Priority", author: "Author",
          percentageDone: "%", dueDate: "due", startDate: "Start",
        },
      };
      const UI = {
        de: {
          empty: (total) => `Keine Einträge (total=${total ?? 0}).`,
          entries: (n, total) => `Einträge (${n}/${total})`,
        },
        en: {
          empty: (total) => `No entries (total=${total ?? 0}).`,
          entries: (n, total) => `Entries (${n}/${total})`,
        },
      };
      const resolveLocale = () => {
        const raw =
          (args && (args.locale || args.lang)) ||
          (typeof runtime !== "undefined" && runtime && (runtime.locale || runtime.language)) ||
          (typeof this !== "undefined" && this && this.runtimeArgs && (this.runtimeArgs.locale || this.runtimeArgs.language)) ||
          "de";
        const s = String(raw || "de").toLowerCase();
        return s.startsWith("en") ? "en" : "de";
      };
      const locale = resolveLocale();
      const labels = LABELS[locale] || LABELS.de;
      const ui = UI[locale] || UI.de;
      const preferred = [
        "id", "name", "subject", "title", "identifier", "status", "type", "assignee",
        "project", "parent", "priority", "lockVersion", "percentageDone", "startDate", "dueDate",
        "login", "email", "active", "createdAt", "updatedAt", "firstName", "lastName", "firstname", "lastname",
      ];
      const collectionTable = (els, total) => {
        if (!els.length) return ui.empty(total ?? 0);
        let cols = preferred.filter((k) => els.some((e) => hasField(e, k)));
        if (!cols.length) {
          const keys = Object.keys(els[0] || {}).filter((k) => !k.startsWith("_") && typeof els[0][k] !== "object");
          cols = keys.slice(0, 8);
        }
        if (!cols.includes("id") && els[0] && els[0].id !== undefined) cols = ["id", ...cols.filter((c) => c !== "id")];
        cols = cols.slice(0, 10);
        const header = "| " + cols.map((c) => labels[c] || c).join(" | ") + " |";
        const sep = "| " + cols.map(() => "---").join(" | ") + " |";
        const rows = els.map((e) => "| " + cols.map((c) => cell(fieldVal(e, c))).join(" | ") + " |");
        return [ui.entries(els.length, total ?? els.length), "", header, sep, ...rows].join("\n");
      };
      if (item && item._type && (item._type === "Collection" || String(item._type).endsWith("Collection"))) {
        const els = (item._embedded && item._embedded.elements) ? item._embedded.elements : [];
        return collectionTable(els, item.total);
      }
      if (item && Array.isArray(item.results)) {
        return collectionTable(item.results, item.count);
      }
      if (item && typeof item === "object" && item._type && item._type !== "Error") {
        const cols = preferred.filter((k) => hasField(item, k)).slice(0, 10);
        if (cols.length) {
          return [
            "| " + cols.map((c) => labels[c] || c).join(" | ") + " |",
            "| " + cols.map(() => "---").join(" | ") + " |",
            "| " + cols.map((c) => cell(fieldVal(item, c))).join(" | ") + " |",
          ].join("\n");
        }
      }
      return JSON.stringify(item, null, 2).slice(0, 4000);

    } catch (e) {
      return `Fehler beim Aufruf von OpenProject: ${e.message}`;
    }
  },
};
