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
      case "list_user_non_working_times":
      missing = requireArgs(["id"]); if (missing) return missing;
      method = "GET"; path = `/api/v3/users/${encodeURIComponent(args.id)}/non_working_times`;
      {
        const _qs = new URLSearchParams();
        if (args.year !== undefined && args.year !== null && String(args.year).trim() !== "") _qs.set("year", String(args.year));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "create_user_non_working_time":
      missing = requireArgs(["id", "_type", "startDate", "endDate"]); if (missing) return missing;
      method = "POST"; path = `/api/v3/users/${encodeURIComponent(args.id)}/non_working_times`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "year", "_type", "startDate", "endDate", "non_working_time_id", "validFrom", "mondayHours", "tuesdayHours", "wednesdayHours", "thursdayHours", "fridayHours", "saturdayHours", "sundayHours", "availabilityFactor", "working_hours_id"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args._type !== undefined && args._type !== null && String(args._type).trim() !== "") {
        {
          const _allowed = ["UserNonWorkingTime"];
          if (!_allowed.includes(String(args._type))) {
            return `_type muss einer von: ${_allowed.join(", ")} sein (got: ${args._type})`;
          }
        }
        body["_type"] = args._type;
      }
      if (args.startDate !== undefined && args.startDate !== null && String(args.startDate).trim() !== "") {
        body["startDate"] = args.startDate;
      }
      if (args.endDate !== undefined && args.endDate !== null && String(args.endDate).trim() !== "") {
        body["endDate"] = args.endDate;
      }
      break;

      case "delete_user_non_working_time":
      missing = requireArgs(["id", "non_working_time_id"]); if (missing) return missing;
      {
        if (args.non_working_time_id !== undefined && args.non_working_time_id !== null && String(args.non_working_time_id).trim() !== "") {
          const _n = Number(args.non_working_time_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `non_working_time_id muss eine ganze Zahl und > 0 sein (got: ${args.non_working_time_id})`;
          }
        }
      }
      method = "DELETE"; path = `/api/v3/users/${encodeURIComponent(args.id)}/non_working_times/${encodeURIComponent(args.non_working_time_id)}`;
      break;

      case "get_user_non_working_time":
      missing = requireArgs(["id", "non_working_time_id"]); if (missing) return missing;
      {
        if (args.non_working_time_id !== undefined && args.non_working_time_id !== null && String(args.non_working_time_id).trim() !== "") {
          const _n = Number(args.non_working_time_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `non_working_time_id muss eine ganze Zahl und > 0 sein (got: ${args.non_working_time_id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/users/${encodeURIComponent(args.id)}/non_working_times/${encodeURIComponent(args.non_working_time_id)}`;
      break;

      case "update_user_non_working_time":
      missing = requireArgs(["id", "non_working_time_id", "_type", "startDate", "endDate"]); if (missing) return missing;
      {
        if (args.non_working_time_id !== undefined && args.non_working_time_id !== null && String(args.non_working_time_id).trim() !== "") {
          const _n = Number(args.non_working_time_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `non_working_time_id muss eine ganze Zahl und > 0 sein (got: ${args.non_working_time_id})`;
          }
        }
      }
      method = "PATCH"; path = `/api/v3/users/${encodeURIComponent(args.id)}/non_working_times/${encodeURIComponent(args.non_working_time_id)}`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "year", "_type", "startDate", "endDate", "non_working_time_id", "validFrom", "mondayHours", "tuesdayHours", "wednesdayHours", "thursdayHours", "fridayHours", "saturdayHours", "sundayHours", "availabilityFactor", "working_hours_id"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args._type !== undefined && args._type !== null && String(args._type).trim() !== "") {
        {
          const _allowed = ["UserNonWorkingTime"];
          if (!_allowed.includes(String(args._type))) {
            return `_type muss einer von: ${_allowed.join(", ")} sein (got: ${args._type})`;
          }
        }
        body["_type"] = args._type;
      }
      if (args.startDate !== undefined && args.startDate !== null && String(args.startDate).trim() !== "") {
        body["startDate"] = args.startDate;
      }
      if (args.endDate !== undefined && args.endDate !== null && String(args.endDate).trim() !== "") {
        body["endDate"] = args.endDate;
      }
      break;

      case "list_user_working_hours":
      missing = requireArgs(["id"]); if (missing) return missing;
      method = "GET"; path = `/api/v3/users/${encodeURIComponent(args.id)}/working_hours`;
      break;

      case "create_user_working_hours":
      missing = requireArgs(["id", "_type", "validFrom", "mondayHours", "tuesdayHours", "wednesdayHours", "thursdayHours", "fridayHours", "saturdayHours", "sundayHours", "availabilityFactor"]); if (missing) return missing;
      {
        if (args.mondayHours !== undefined && args.mondayHours !== null && String(args.mondayHours).trim() !== "") {
          const _n = Number(args.mondayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `mondayHours muss eine Zahl und >= 0 sein (got: ${args.mondayHours})`;
          }
        }
      }
      {
        if (args.tuesdayHours !== undefined && args.tuesdayHours !== null && String(args.tuesdayHours).trim() !== "") {
          const _n = Number(args.tuesdayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `tuesdayHours muss eine Zahl und >= 0 sein (got: ${args.tuesdayHours})`;
          }
        }
      }
      {
        if (args.wednesdayHours !== undefined && args.wednesdayHours !== null && String(args.wednesdayHours).trim() !== "") {
          const _n = Number(args.wednesdayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `wednesdayHours muss eine Zahl und >= 0 sein (got: ${args.wednesdayHours})`;
          }
        }
      }
      {
        if (args.thursdayHours !== undefined && args.thursdayHours !== null && String(args.thursdayHours).trim() !== "") {
          const _n = Number(args.thursdayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `thursdayHours muss eine Zahl und >= 0 sein (got: ${args.thursdayHours})`;
          }
        }
      }
      {
        if (args.fridayHours !== undefined && args.fridayHours !== null && String(args.fridayHours).trim() !== "") {
          const _n = Number(args.fridayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `fridayHours muss eine Zahl und >= 0 sein (got: ${args.fridayHours})`;
          }
        }
      }
      {
        if (args.saturdayHours !== undefined && args.saturdayHours !== null && String(args.saturdayHours).trim() !== "") {
          const _n = Number(args.saturdayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `saturdayHours muss eine Zahl und >= 0 sein (got: ${args.saturdayHours})`;
          }
        }
      }
      {
        if (args.sundayHours !== undefined && args.sundayHours !== null && String(args.sundayHours).trim() !== "") {
          const _n = Number(args.sundayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `sundayHours muss eine Zahl und >= 0 sein (got: ${args.sundayHours})`;
          }
        }
      }
      {
        if (args.availabilityFactor !== undefined && args.availabilityFactor !== null && String(args.availabilityFactor).trim() !== "") {
          const _n = Number(args.availabilityFactor);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 0) {
            return `availabilityFactor muss eine ganze Zahl und >= 0 sein (got: ${args.availabilityFactor})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/users/${encodeURIComponent(args.id)}/working_hours`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "year", "_type", "startDate", "endDate", "non_working_time_id", "validFrom", "mondayHours", "tuesdayHours", "wednesdayHours", "thursdayHours", "fridayHours", "saturdayHours", "sundayHours", "availabilityFactor", "working_hours_id"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args._type !== undefined && args._type !== null && String(args._type).trim() !== "") {
        {
          const _allowed = ["UserWorkingHours"];
          if (!_allowed.includes(String(args._type))) {
            return `_type muss einer von: ${_allowed.join(", ")} sein (got: ${args._type})`;
          }
        }
        body["_type"] = args._type;
      }
      if (args.validFrom !== undefined && args.validFrom !== null && String(args.validFrom).trim() !== "") {
        body["validFrom"] = args.validFrom;
      }
      if (args.mondayHours !== undefined && args.mondayHours !== null && String(args.mondayHours).trim() !== "") {
        {
          const _n = Number(args.mondayHours);
          body["mondayHours"] = Number.isNaN(_n) ? args.mondayHours : _n;
        }
      }
      if (args.tuesdayHours !== undefined && args.tuesdayHours !== null && String(args.tuesdayHours).trim() !== "") {
        {
          const _n = Number(args.tuesdayHours);
          body["tuesdayHours"] = Number.isNaN(_n) ? args.tuesdayHours : _n;
        }
      }
      if (args.wednesdayHours !== undefined && args.wednesdayHours !== null && String(args.wednesdayHours).trim() !== "") {
        {
          const _n = Number(args.wednesdayHours);
          body["wednesdayHours"] = Number.isNaN(_n) ? args.wednesdayHours : _n;
        }
      }
      if (args.thursdayHours !== undefined && args.thursdayHours !== null && String(args.thursdayHours).trim() !== "") {
        {
          const _n = Number(args.thursdayHours);
          body["thursdayHours"] = Number.isNaN(_n) ? args.thursdayHours : _n;
        }
      }
      if (args.fridayHours !== undefined && args.fridayHours !== null && String(args.fridayHours).trim() !== "") {
        {
          const _n = Number(args.fridayHours);
          body["fridayHours"] = Number.isNaN(_n) ? args.fridayHours : _n;
        }
      }
      if (args.saturdayHours !== undefined && args.saturdayHours !== null && String(args.saturdayHours).trim() !== "") {
        {
          const _n = Number(args.saturdayHours);
          body["saturdayHours"] = Number.isNaN(_n) ? args.saturdayHours : _n;
        }
      }
      if (args.sundayHours !== undefined && args.sundayHours !== null && String(args.sundayHours).trim() !== "") {
        {
          const _n = Number(args.sundayHours);
          body["sundayHours"] = Number.isNaN(_n) ? args.sundayHours : _n;
        }
      }
      if (args.availabilityFactor !== undefined && args.availabilityFactor !== null && String(args.availabilityFactor).trim() !== "") {
        {
          const _n = Number(args.availabilityFactor);
          body["availabilityFactor"] = Number.isNaN(_n) ? args.availabilityFactor : _n;
        }
      }
      break;

      case "delete_user_working_hours_record":
      missing = requireArgs(["id", "working_hours_id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      {
        if (args.working_hours_id !== undefined && args.working_hours_id !== null && String(args.working_hours_id).trim() !== "") {
          const _n = Number(args.working_hours_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `working_hours_id muss eine ganze Zahl und > 0 sein (got: ${args.working_hours_id})`;
          }
        }
      }
      method = "DELETE"; path = `/api/v3/users/${encodeURIComponent(args.id)}/working_hours/${encodeURIComponent(args.working_hours_id)}`;
      break;

      case "get_user_working_hours_record":
      missing = requireArgs(["id", "working_hours_id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      {
        if (args.working_hours_id !== undefined && args.working_hours_id !== null && String(args.working_hours_id).trim() !== "") {
          const _n = Number(args.working_hours_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `working_hours_id muss eine ganze Zahl und > 0 sein (got: ${args.working_hours_id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/users/${encodeURIComponent(args.id)}/working_hours/${encodeURIComponent(args.working_hours_id)}`;
      break;

      case "update_user_working_hours_record":
      missing = requireArgs(["id", "working_hours_id", "_type", "validFrom", "mondayHours", "tuesdayHours", "wednesdayHours", "thursdayHours", "fridayHours", "saturdayHours", "sundayHours", "availabilityFactor"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      {
        if (args.working_hours_id !== undefined && args.working_hours_id !== null && String(args.working_hours_id).trim() !== "") {
          const _n = Number(args.working_hours_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `working_hours_id muss eine ganze Zahl und > 0 sein (got: ${args.working_hours_id})`;
          }
        }
      }
      {
        if (args.mondayHours !== undefined && args.mondayHours !== null && String(args.mondayHours).trim() !== "") {
          const _n = Number(args.mondayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `mondayHours muss eine Zahl und >= 0 sein (got: ${args.mondayHours})`;
          }
        }
      }
      {
        if (args.tuesdayHours !== undefined && args.tuesdayHours !== null && String(args.tuesdayHours).trim() !== "") {
          const _n = Number(args.tuesdayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `tuesdayHours muss eine Zahl und >= 0 sein (got: ${args.tuesdayHours})`;
          }
        }
      }
      {
        if (args.wednesdayHours !== undefined && args.wednesdayHours !== null && String(args.wednesdayHours).trim() !== "") {
          const _n = Number(args.wednesdayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `wednesdayHours muss eine Zahl und >= 0 sein (got: ${args.wednesdayHours})`;
          }
        }
      }
      {
        if (args.thursdayHours !== undefined && args.thursdayHours !== null && String(args.thursdayHours).trim() !== "") {
          const _n = Number(args.thursdayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `thursdayHours muss eine Zahl und >= 0 sein (got: ${args.thursdayHours})`;
          }
        }
      }
      {
        if (args.fridayHours !== undefined && args.fridayHours !== null && String(args.fridayHours).trim() !== "") {
          const _n = Number(args.fridayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `fridayHours muss eine Zahl und >= 0 sein (got: ${args.fridayHours})`;
          }
        }
      }
      {
        if (args.saturdayHours !== undefined && args.saturdayHours !== null && String(args.saturdayHours).trim() !== "") {
          const _n = Number(args.saturdayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `saturdayHours muss eine Zahl und >= 0 sein (got: ${args.saturdayHours})`;
          }
        }
      }
      {
        if (args.sundayHours !== undefined && args.sundayHours !== null && String(args.sundayHours).trim() !== "") {
          const _n = Number(args.sundayHours);
          if (!Number.isFinite(_n) || _n < 0) {
            return `sundayHours muss eine Zahl und >= 0 sein (got: ${args.sundayHours})`;
          }
        }
      }
      {
        if (args.availabilityFactor !== undefined && args.availabilityFactor !== null && String(args.availabilityFactor).trim() !== "") {
          const _n = Number(args.availabilityFactor);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 0) {
            return `availabilityFactor muss eine ganze Zahl und >= 0 sein (got: ${args.availabilityFactor})`;
          }
        }
      }
      method = "PATCH"; path = `/api/v3/users/${encodeURIComponent(args.id)}/working_hours/${encodeURIComponent(args.working_hours_id)}`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "year", "_type", "startDate", "endDate", "non_working_time_id", "validFrom", "mondayHours", "tuesdayHours", "wednesdayHours", "thursdayHours", "fridayHours", "saturdayHours", "sundayHours", "availabilityFactor", "working_hours_id"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args._type !== undefined && args._type !== null && String(args._type).trim() !== "") {
        {
          const _allowed = ["UserWorkingHours"];
          if (!_allowed.includes(String(args._type))) {
            return `_type muss einer von: ${_allowed.join(", ")} sein (got: ${args._type})`;
          }
        }
        body["_type"] = args._type;
      }
      if (args.validFrom !== undefined && args.validFrom !== null && String(args.validFrom).trim() !== "") {
        body["validFrom"] = args.validFrom;
      }
      if (args.mondayHours !== undefined && args.mondayHours !== null && String(args.mondayHours).trim() !== "") {
        {
          const _n = Number(args.mondayHours);
          body["mondayHours"] = Number.isNaN(_n) ? args.mondayHours : _n;
        }
      }
      if (args.tuesdayHours !== undefined && args.tuesdayHours !== null && String(args.tuesdayHours).trim() !== "") {
        {
          const _n = Number(args.tuesdayHours);
          body["tuesdayHours"] = Number.isNaN(_n) ? args.tuesdayHours : _n;
        }
      }
      if (args.wednesdayHours !== undefined && args.wednesdayHours !== null && String(args.wednesdayHours).trim() !== "") {
        {
          const _n = Number(args.wednesdayHours);
          body["wednesdayHours"] = Number.isNaN(_n) ? args.wednesdayHours : _n;
        }
      }
      if (args.thursdayHours !== undefined && args.thursdayHours !== null && String(args.thursdayHours).trim() !== "") {
        {
          const _n = Number(args.thursdayHours);
          body["thursdayHours"] = Number.isNaN(_n) ? args.thursdayHours : _n;
        }
      }
      if (args.fridayHours !== undefined && args.fridayHours !== null && String(args.fridayHours).trim() !== "") {
        {
          const _n = Number(args.fridayHours);
          body["fridayHours"] = Number.isNaN(_n) ? args.fridayHours : _n;
        }
      }
      if (args.saturdayHours !== undefined && args.saturdayHours !== null && String(args.saturdayHours).trim() !== "") {
        {
          const _n = Number(args.saturdayHours);
          body["saturdayHours"] = Number.isNaN(_n) ? args.saturdayHours : _n;
        }
      }
      if (args.sundayHours !== undefined && args.sundayHours !== null && String(args.sundayHours).trim() !== "") {
        {
          const _n = Number(args.sundayHours);
          body["sundayHours"] = Number.isNaN(_n) ? args.sundayHours : _n;
        }
      }
      if (args.availabilityFactor !== undefined && args.availabilityFactor !== null && String(args.availabilityFactor).trim() !== "") {
        {
          const _n = Number(args.availabilityFactor);
          body["availabilityFactor"] = Number.isNaN(_n) ? args.availabilityFactor : _n;
        }
      }
      break;
      default:
        return `Unbekannte operation: ${operation}`;
    }

    const confirmBlock = confirmOrNull({
      hubId: "openproject-user-working-times",
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
      if (item && item._type && (item._type === "Collection" || String(item._type).endsWith("Collection"))) {
        const els = (item._embedded && item._embedded.elements) ? item._embedded.elements : [];
        if (!els.length) return `Keine Benutzer (total=${item.total ?? 0}).`;
        const cell = (v) => String(v ?? "-").replace(/\|/g, "/").replace(/\r?\n/g, " ");
        const rows = els.map((u) => {
          const admin = u.admin ? "ja" : "nein";
          return `| ${u.id ?? "?"} | ${cell(u.name)} | ${cell(u.login)} | ${cell(u.email)} | ${cell(u.status)} | ${admin} |`;
        });
        return [
          `Benutzer (${els.length}/${item.total ?? els.length})`,
          "",
          "| ID | Name | Login | E-Mail | Status | Admin |",
          "| --- | --- | --- | --- | --- | --- |",
          ...rows,
        ].join("\n");
      }
      if (item && (item._type === "User" || item.login !== undefined)) {
        const cell = (v) => String(v ?? "-").replace(/\|/g, "/").replace(/\r?\n/g, " ");
        const admin = item.admin ? "ja" : "nein";
        return [
          "| ID | Name | Login | E-Mail | Status | Admin |",
          "| --- | --- | --- | --- | --- | --- |",
          `| ${item.id} | ${cell(item.name)} | ${cell(item.login)} | ${cell(item.email)} | ${cell(item.status)} | ${admin} |`,
        ].join("\n");
      }
      return JSON.stringify(item, null, 2).slice(0, 4000);
    } catch (e) {
      return `Fehler beim Aufruf von OpenProject: ${e.message}`;
    }
  },
};
