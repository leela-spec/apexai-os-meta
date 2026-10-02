const { confirmOrNull } = require("../_lib/opSkillWriteConfirm.js");

module.exports.runtime = {
  handler: async function (args) {
    args = args || {};
    const runtime = this.runtimeArgs || {};
    const base = (
      runtime.openproject_base_url ||
      process.env.OPENPROJECT_BASE_URL ||
      "http://web:8080"
    ).replace(/\/+$/, "");
    // Prefer skill setup_args; fall back to container env (provisioned OPENPROJECT_API_KEY)
    // so a value-less plugin.json hot-patch cannot leave the hub unauthenticated.
    const token = String(
      runtime.openproject_token || process.env.OPENPROJECT_API_KEY || ""
    ).trim();
    if (!token) {
      return "openproject_token fehlt (Skill-Setup oder OPENPROJECT_API_KEY).";
    }
    const basic = `Basic ${Buffer.from(`apikey:${token}`).toString("base64")}`;
    const headers = { Authorization: basic, Accept: "application/json" };
    const operation = String(args.operation || "").trim();
    if (!operation) return "Bitte operation angeben.";

    
    const applyParentLink = (body, args) => {
      const raw = args.parent_id !== undefined && args.parent_id !== null && String(args.parent_id).trim() !== ""
        ? args.parent_id
        : args.parent;
      if (raw === undefined || raw === null || String(raw).trim() === "") return null;
      const _n = Number(raw);
      if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
        return `parent_id muss eine ganze Zahl und > 0 sein (got: ${raw})`;
      }
      body._links = body._links || {};
      body._links.parent = { href: `/api/v3/work_packages/${_n}` };
      return null;
    };

    /** Parse filters JSON → array (fail-open empty). */
    const parseFiltersArg = (raw) => {
      if (raw == null || String(raw).trim() === "") return [];
      if (Array.isArray(raw)) return raw;
      try {
        const v = JSON.parse(String(raw));
        return Array.isArray(v) ? v : [];
      } catch {
        return [];
      }
    };

    /**
     * Resolve category id or name within a project (NL Tag/Label → OP Category).
     * @returns {{ id: string, name?: string }|null|{ error: string }}
     */
    const resolveCategoryInProject = async (projectId, raw) => {
      const token = String(raw == null ? "" : raw).trim();
      if (!token) return null;
      if (/^\d+$/.test(token)) return { id: token };
      const res = await fetch(
        `${base}/api/v3/projects/${encodeURIComponent(projectId)}/categories`,
        { method: "GET", headers }
      );
      if (!res.ok) {
        return {
          error: `OpenProject-Fehler ${res.status} beim Laden der Kategorien: ${await res.text()}`,
        };
      }
      let data;
      try {
        data = JSON.parse(await res.text());
      } catch (e) {
        return { error: `Kategorien-JSON ungültig: ${e.message}` };
      }
      const els =
        data && data._embedded && Array.isArray(data._embedded.elements)
          ? data._embedded.elements
          : [];
      const q = token.toLowerCase();
      const hits = els.filter((c) => {
        const n = String((c && (c.name || c.title)) || "")
          .trim()
          .toLowerCase();
        return n === q || n.includes(q) || q.includes(n);
      });
      if (hits.length === 0) {
        return {
          error: `Ask[missing_resource]: Kategorie/Tag „${token}“ fehlt in Projekt #${projectId}. Bitte in OpenProject anlegen (Projekteinstellungen → Arbeitspakete → Kategorien), dann „ja“.`,
          reason: "missing_resource",
        };
      }
      if (hits.length > 1) {
        const names = hits
          .slice(0, 5)
          .map((c) => `${c.id}:${c.name || c.title}`)
          .join(", ");
        return {
          error: `Ask[ambiguous_slot]: Mehrdeutige Kategorie/Tag „${token}“ (${names}). Bitte präzisieren.`,
          reason: "ambiguous_slot",
        };
      }
      return { id: String(hits[0].id), name: hits[0].name || hits[0].title };
    };

    const applyCategoryLink = async (body, args, projectIdHint) => {
      const raw =
        args.category_id !== undefined &&
        args.category_id !== null &&
        String(args.category_id).trim() !== ""
          ? args.category_id
          : args.category !== undefined &&
              args.category !== null &&
              String(args.category).trim() !== ""
            ? args.category
            : null;
      if (raw == null) return null;
      const asNum = Number(raw);
      if (Number.isFinite(asNum) && Number.isInteger(asNum) && asNum >= 1) {
        body._links = body._links || {};
        body._links.category = { href: `/api/v3/categories/${asNum}` };
        return null;
      }
      const projectId = String(
        projectIdHint ||
          args.projectId ||
          (operation === "create_project" || operation === "create_workspace"
            ? args.id
            : "") ||
          ""
      ).trim();
      if (!projectId) {
        return "Ask: Projekt-ID fehlt, um Tag/Label (Kategorie) per Name aufzulösen.";
      }
      const resolved = await resolveCategoryInProject(projectId, raw);
      if (!resolved) return null;
      if (resolved.error) return resolved.error;
      body._links = body._links || {};
      body._links.category = {
        href: `/api/v3/categories/${resolved.id}`,
      };
      return null;
    };

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
      case "project_available_assignees":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/projects/${encodeURIComponent(args.id)}/available_assignees`;
      break;

      case "get_project_collection":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/projects/${encodeURIComponent(args.id)}/work_packages`;
      {
        const _qs = new URLSearchParams();
        if (args.offset !== undefined && args.offset !== null && String(args.offset).trim() !== "") _qs.set("offset", String(args.offset));
        if (args.pageSize !== undefined && args.pageSize !== null && String(args.pageSize).trim() !== "") _qs.set("pageSize", String(args.pageSize));
        if (args.filters !== undefined && args.filters !== null && String(args.filters).trim() !== "") _qs.set("filters", String(args.filters));
        if (args.sortBy !== undefined && args.sortBy !== null && String(args.sortBy).trim() !== "") _qs.set("sortBy", String(args.sortBy));
        if (args.groupBy !== undefined && args.groupBy !== null && String(args.groupBy).trim() !== "") _qs.set("groupBy", String(args.groupBy));
        if (args.showSums !== undefined && args.showSums !== null && String(args.showSums).trim() !== "") _qs.set("showSums", String(args.showSums));
        if (args.select !== undefined && args.select !== null && String(args.select).trim() !== "") _qs.set("select", String(args.select));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "create_project":
      missing = requireArgs(["id", "subject"]); if (missing) return missing;
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
      {
        if (args.position !== undefined && args.position !== null && String(args.position).trim() !== "") {
          const _n = Number(args.position);
          if (!Number.isFinite(_n) || !Number.isInteger(_n)) {
            return `position muss eine ganze Zahl sein (got: ${args.position})`;
          }
        }
      }
      {
        if (args.storyPoints !== undefined && args.storyPoints !== null && String(args.storyPoints).trim() !== "") {
          const _n = Number(args.storyPoints);
          if (!Number.isFinite(_n) || !Number.isInteger(_n)) {
            return `storyPoints muss eine ganze Zahl sein (got: ${args.storyPoints})`;
          }
        }
      }
      {
        if (args.percentageDone !== undefined && args.percentageDone !== null && String(args.percentageDone).trim() !== "") {
          const _n = Number(args.percentageDone);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 0) {
            return `percentageDone muss eine ganze Zahl und >= 0 sein (got: ${args.percentageDone})`;
          }
        }
      }
      {
        if (args.derivedPercentageDone !== undefined && args.derivedPercentageDone !== null && String(args.derivedPercentageDone).trim() !== "") {
          const _n = Number(args.derivedPercentageDone);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 0) {
            return `derivedPercentageDone muss eine ganze Zahl und >= 0 sein (got: ${args.derivedPercentageDone})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/projects/${encodeURIComponent(args.id)}/work_packages`;
      {
        const _qs = new URLSearchParams();
        if (args.notify !== undefined && args.notify !== null && String(args.notify).trim() !== "") _qs.set("notify", String(args.notify));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "offset", "pageSize", "filters", "sortBy", "groupBy", "showSums", "select", "notify", "displayId", "lockVersion", "subject", "_type", "description", "scheduleManually", "readonly", "hasProjectAttributes", "startDate", "dueDate", "date", "derivedStartDate", "derivedDueDate", "duration", "estimatedTime", "derivedEstimatedTime", "ignoreNonWorkingDays", "position", "spentTime", "storyPoints", "percentageDone", "derivedPercentageDone", "createdAt", "updatedAt", "_meta", "timestamps", "identifier", "comment", "internal", "query", "type", "_embedded", "user", "user_id", "work_package_id", "remindAt", "note", "parent_id", "parent", "category_id", "category"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.displayId !== undefined && args.displayId !== null && String(args.displayId).trim() !== "") {
        body["displayId"] = args.displayId;
      }
      if (args.lockVersion !== undefined && args.lockVersion !== null && String(args.lockVersion).trim() !== "") {
        {
          const _n = Number(args.lockVersion);
          body["lockVersion"] = Number.isNaN(_n) ? args.lockVersion : _n;
        }
      }
      if (args.subject !== undefined && args.subject !== null && String(args.subject).trim() !== "") {
        body["subject"] = args.subject;
      }
      if (args._type !== undefined && args._type !== null && String(args._type).trim() !== "") {
        {
          const _allowed = ["WorkPackage"];
          if (!_allowed.includes(String(args._type))) {
            return `_type muss einer von: ${_allowed.join(", ")} sein (got: ${args._type})`;
          }
        }
        body["_type"] = args._type;
      }
      if (args.description !== undefined && args.description !== null && String(args.description).trim() !== "") {
        body["description"] = args.description;
      }
      if (args.scheduleManually !== undefined && args.scheduleManually !== null && String(args.scheduleManually).trim() !== "") {
        {
          const _raw = args.scheduleManually;
          if (typeof _raw === "boolean") {
            body["scheduleManually"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `scheduleManually muss boolean sein (got: ${args.scheduleManually})`;
            }
            body["scheduleManually"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.readonly !== undefined && args.readonly !== null && String(args.readonly).trim() !== "") {
        {
          const _raw = args.readonly;
          if (typeof _raw === "boolean") {
            body["readonly"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `readonly muss boolean sein (got: ${args.readonly})`;
            }
            body["readonly"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.hasProjectAttributes !== undefined && args.hasProjectAttributes !== null && String(args.hasProjectAttributes).trim() !== "") {
        {
          const _raw = args.hasProjectAttributes;
          if (typeof _raw === "boolean") {
            body["hasProjectAttributes"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `hasProjectAttributes muss boolean sein (got: ${args.hasProjectAttributes})`;
            }
            body["hasProjectAttributes"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.startDate !== undefined && args.startDate !== null && String(args.startDate).trim() !== "") {
        body["startDate"] = args.startDate;
      }
      if (args.dueDate !== undefined && args.dueDate !== null && String(args.dueDate).trim() !== "") {
        body["dueDate"] = args.dueDate;
      }
      if (args.date !== undefined && args.date !== null && String(args.date).trim() !== "") {
        body["date"] = args.date;
      }
      if (args.derivedStartDate !== undefined && args.derivedStartDate !== null && String(args.derivedStartDate).trim() !== "") {
        body["derivedStartDate"] = args.derivedStartDate;
      }
      if (args.derivedDueDate !== undefined && args.derivedDueDate !== null && String(args.derivedDueDate).trim() !== "") {
        body["derivedDueDate"] = args.derivedDueDate;
      }
      if (args.duration !== undefined && args.duration !== null && String(args.duration).trim() !== "") {
        body["duration"] = args.duration;
      }
      if (args.estimatedTime !== undefined && args.estimatedTime !== null && String(args.estimatedTime).trim() !== "") {
        body["estimatedTime"] = args.estimatedTime;
      }
      if (args.derivedEstimatedTime !== undefined && args.derivedEstimatedTime !== null && String(args.derivedEstimatedTime).trim() !== "") {
        body["derivedEstimatedTime"] = args.derivedEstimatedTime;
      }
      if (args.ignoreNonWorkingDays !== undefined && args.ignoreNonWorkingDays !== null && String(args.ignoreNonWorkingDays).trim() !== "") {
        {
          const _raw = args.ignoreNonWorkingDays;
          if (typeof _raw === "boolean") {
            body["ignoreNonWorkingDays"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `ignoreNonWorkingDays muss boolean sein (got: ${args.ignoreNonWorkingDays})`;
            }
            body["ignoreNonWorkingDays"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.position !== undefined && args.position !== null && String(args.position).trim() !== "") {
        {
          const _n = Number(args.position);
          body["position"] = Number.isNaN(_n) ? args.position : _n;
        }
      }
      if (args.spentTime !== undefined && args.spentTime !== null && String(args.spentTime).trim() !== "") {
        body["spentTime"] = args.spentTime;
      }
      if (args.storyPoints !== undefined && args.storyPoints !== null && String(args.storyPoints).trim() !== "") {
        {
          const _n = Number(args.storyPoints);
          body["storyPoints"] = Number.isNaN(_n) ? args.storyPoints : _n;
        }
      }
      if (args.percentageDone !== undefined && args.percentageDone !== null && String(args.percentageDone).trim() !== "") {
        {
          const _n = Number(args.percentageDone);
          body["percentageDone"] = Number.isNaN(_n) ? args.percentageDone : _n;
        }
      }
      if (args.derivedPercentageDone !== undefined && args.derivedPercentageDone !== null && String(args.derivedPercentageDone).trim() !== "") {
        {
          const _n = Number(args.derivedPercentageDone);
          body["derivedPercentageDone"] = Number.isNaN(_n) ? args.derivedPercentageDone : _n;
        }
      }
      if (args.createdAt !== undefined && args.createdAt !== null && String(args.createdAt).trim() !== "") {
        body["createdAt"] = args.createdAt;
      }
      if (args.updatedAt !== undefined && args.updatedAt !== null && String(args.updatedAt).trim() !== "") {
        body["updatedAt"] = args.updatedAt;
      }
      {
        const _pe = applyParentLink(body, args); if (_pe) return _pe;
      }
      break;

      case "form_create_in_project":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/projects/${encodeURIComponent(args.id)}/work_packages/form`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "offset", "pageSize", "filters", "sortBy", "groupBy", "showSums", "select", "notify", "displayId", "lockVersion", "subject", "_type", "description", "scheduleManually", "readonly", "hasProjectAttributes", "startDate", "dueDate", "date", "derivedStartDate", "derivedDueDate", "duration", "estimatedTime", "derivedEstimatedTime", "ignoreNonWorkingDays", "position", "spentTime", "storyPoints", "percentageDone", "derivedPercentageDone", "createdAt", "updatedAt", "_meta", "timestamps", "identifier", "comment", "internal", "query", "type", "_embedded", "user", "user_id", "work_package_id", "remindAt", "note", "parent_id", "parent", "category_id", "category"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.subject !== undefined && args.subject !== null && String(args.subject).trim() !== "") {
        body["subject"] = args.subject;
      }
      if (args.description !== undefined && args.description !== null && String(args.description).trim() !== "") {
        body["description"] = args.description;
      }
      if (args.scheduleManually !== undefined && args.scheduleManually !== null && String(args.scheduleManually).trim() !== "") {
        {
          const _raw = args.scheduleManually;
          if (typeof _raw === "boolean") {
            body["scheduleManually"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `scheduleManually muss boolean sein (got: ${args.scheduleManually})`;
            }
            body["scheduleManually"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.startDate !== undefined && args.startDate !== null && String(args.startDate).trim() !== "") {
        body["startDate"] = args.startDate;
      }
      if (args.dueDate !== undefined && args.dueDate !== null && String(args.dueDate).trim() !== "") {
        body["dueDate"] = args.dueDate;
      }
      if (args.estimatedTime !== undefined && args.estimatedTime !== null && String(args.estimatedTime).trim() !== "") {
        body["estimatedTime"] = args.estimatedTime;
      }
      if (args.duration !== undefined && args.duration !== null && String(args.duration).trim() !== "") {
        body["duration"] = args.duration;
      }
      if (args.ignoreNonWorkingDays !== undefined && args.ignoreNonWorkingDays !== null && String(args.ignoreNonWorkingDays).trim() !== "") {
        {
          const _raw = args.ignoreNonWorkingDays;
          if (typeof _raw === "boolean") {
            body["ignoreNonWorkingDays"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `ignoreNonWorkingDays muss boolean sein (got: ${args.ignoreNonWorkingDays})`;
            }
            body["ignoreNonWorkingDays"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args._meta !== undefined && args._meta !== null && String(args._meta).trim() !== "") {
        let _v__meta = args._meta;
        if (typeof _v__meta === "string") {
          const _s = String(_v__meta).trim();
          if (_s.startsWith("{") || _s.startsWith("[")) {
            try { _v__meta = JSON.parse(_s); }
            catch (e) { _v__meta = { raw: _s }; }
          } else {
            _v__meta = { raw: _s };
          }
        }
        if (typeof _v__meta !== "object" || _v__meta === null || Array.isArray(_v__meta)) {
          return `_meta muss ein Objekt sein (z.B. Formattable mit raw: string)`;
        }
        body["_meta"] = _v__meta;
      }
      {
        const _pe = applyParentLink(body, args); if (_pe) return _pe;
      }
      break;

      case "list":
      method = "GET"; path = `/api/v3/work_packages`;
      {
        const _qs = new URLSearchParams();
        if (args.offset !== undefined && args.offset !== null && String(args.offset).trim() !== "") _qs.set("offset", String(args.offset));
        if (args.pageSize !== undefined && args.pageSize !== null && String(args.pageSize).trim() !== "") _qs.set("pageSize", String(args.pageSize));
        if (args.filters !== undefined && args.filters !== null && String(args.filters).trim() !== "") _qs.set("filters", String(args.filters));
        if (args.sortBy !== undefined && args.sortBy !== null && String(args.sortBy).trim() !== "") _qs.set("sortBy", String(args.sortBy));
        if (args.groupBy !== undefined && args.groupBy !== null && String(args.groupBy).trim() !== "") _qs.set("groupBy", String(args.groupBy));
        if (args.showSums !== undefined && args.showSums !== null && String(args.showSums).trim() !== "") _qs.set("showSums", String(args.showSums));
        if (args.select !== undefined && args.select !== null && String(args.select).trim() !== "") _qs.set("select", String(args.select));
        if (args.timestamps !== undefined && args.timestamps !== null && String(args.timestamps).trim() !== "") _qs.set("timestamps", String(args.timestamps));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "create":
      missing = requireArgs(["subject"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und >= 1 sein (got: ${args.id})`;
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
      {
        if (args.position !== undefined && args.position !== null && String(args.position).trim() !== "") {
          const _n = Number(args.position);
          if (!Number.isFinite(_n) || !Number.isInteger(_n)) {
            return `position muss eine ganze Zahl sein (got: ${args.position})`;
          }
        }
      }
      {
        if (args.storyPoints !== undefined && args.storyPoints !== null && String(args.storyPoints).trim() !== "") {
          const _n = Number(args.storyPoints);
          if (!Number.isFinite(_n) || !Number.isInteger(_n)) {
            return `storyPoints muss eine ganze Zahl sein (got: ${args.storyPoints})`;
          }
        }
      }
      {
        if (args.percentageDone !== undefined && args.percentageDone !== null && String(args.percentageDone).trim() !== "") {
          const _n = Number(args.percentageDone);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 0) {
            return `percentageDone muss eine ganze Zahl und >= 0 sein (got: ${args.percentageDone})`;
          }
        }
      }
      {
        if (args.derivedPercentageDone !== undefined && args.derivedPercentageDone !== null && String(args.derivedPercentageDone).trim() !== "") {
          const _n = Number(args.derivedPercentageDone);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 0) {
            return `derivedPercentageDone muss eine ganze Zahl und >= 0 sein (got: ${args.derivedPercentageDone})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/work_packages`;
      {
        const _qs = new URLSearchParams();
        if (args.notify !== undefined && args.notify !== null && String(args.notify).trim() !== "") _qs.set("notify", String(args.notify));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "offset", "pageSize", "filters", "sortBy", "groupBy", "showSums", "select", "notify", "displayId", "lockVersion", "subject", "_type", "description", "scheduleManually", "readonly", "hasProjectAttributes", "startDate", "dueDate", "date", "derivedStartDate", "derivedDueDate", "duration", "estimatedTime", "derivedEstimatedTime", "ignoreNonWorkingDays", "position", "spentTime", "storyPoints", "percentageDone", "derivedPercentageDone", "createdAt", "updatedAt", "_meta", "timestamps", "identifier", "comment", "internal", "query", "type", "_embedded", "user", "user_id", "work_package_id", "remindAt", "note", "parent_id", "parent", "category_id", "category"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
        {
          const _n = Number(args.id);
          body["id"] = Number.isNaN(_n) ? args.id : _n;
        }
      }
      if (args.displayId !== undefined && args.displayId !== null && String(args.displayId).trim() !== "") {
        body["displayId"] = args.displayId;
      }
      if (args.lockVersion !== undefined && args.lockVersion !== null && String(args.lockVersion).trim() !== "") {
        {
          const _n = Number(args.lockVersion);
          body["lockVersion"] = Number.isNaN(_n) ? args.lockVersion : _n;
        }
      }
      if (args.subject !== undefined && args.subject !== null && String(args.subject).trim() !== "") {
        body["subject"] = args.subject;
      }
      if (args._type !== undefined && args._type !== null && String(args._type).trim() !== "") {
        {
          const _allowed = ["WorkPackage"];
          if (!_allowed.includes(String(args._type))) {
            return `_type muss einer von: ${_allowed.join(", ")} sein (got: ${args._type})`;
          }
        }
        body["_type"] = args._type;
      }
      if (args.description !== undefined && args.description !== null && String(args.description).trim() !== "") {
        body["description"] = args.description;
      }
      if (args.scheduleManually !== undefined && args.scheduleManually !== null && String(args.scheduleManually).trim() !== "") {
        {
          const _raw = args.scheduleManually;
          if (typeof _raw === "boolean") {
            body["scheduleManually"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `scheduleManually muss boolean sein (got: ${args.scheduleManually})`;
            }
            body["scheduleManually"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.readonly !== undefined && args.readonly !== null && String(args.readonly).trim() !== "") {
        {
          const _raw = args.readonly;
          if (typeof _raw === "boolean") {
            body["readonly"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `readonly muss boolean sein (got: ${args.readonly})`;
            }
            body["readonly"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.hasProjectAttributes !== undefined && args.hasProjectAttributes !== null && String(args.hasProjectAttributes).trim() !== "") {
        {
          const _raw = args.hasProjectAttributes;
          if (typeof _raw === "boolean") {
            body["hasProjectAttributes"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `hasProjectAttributes muss boolean sein (got: ${args.hasProjectAttributes})`;
            }
            body["hasProjectAttributes"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.startDate !== undefined && args.startDate !== null && String(args.startDate).trim() !== "") {
        body["startDate"] = args.startDate;
      }
      if (args.dueDate !== undefined && args.dueDate !== null && String(args.dueDate).trim() !== "") {
        body["dueDate"] = args.dueDate;
      }
      if (args.date !== undefined && args.date !== null && String(args.date).trim() !== "") {
        body["date"] = args.date;
      }
      if (args.derivedStartDate !== undefined && args.derivedStartDate !== null && String(args.derivedStartDate).trim() !== "") {
        body["derivedStartDate"] = args.derivedStartDate;
      }
      if (args.derivedDueDate !== undefined && args.derivedDueDate !== null && String(args.derivedDueDate).trim() !== "") {
        body["derivedDueDate"] = args.derivedDueDate;
      }
      if (args.duration !== undefined && args.duration !== null && String(args.duration).trim() !== "") {
        body["duration"] = args.duration;
      }
      if (args.estimatedTime !== undefined && args.estimatedTime !== null && String(args.estimatedTime).trim() !== "") {
        body["estimatedTime"] = args.estimatedTime;
      }
      if (args.derivedEstimatedTime !== undefined && args.derivedEstimatedTime !== null && String(args.derivedEstimatedTime).trim() !== "") {
        body["derivedEstimatedTime"] = args.derivedEstimatedTime;
      }
      if (args.ignoreNonWorkingDays !== undefined && args.ignoreNonWorkingDays !== null && String(args.ignoreNonWorkingDays).trim() !== "") {
        {
          const _raw = args.ignoreNonWorkingDays;
          if (typeof _raw === "boolean") {
            body["ignoreNonWorkingDays"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `ignoreNonWorkingDays muss boolean sein (got: ${args.ignoreNonWorkingDays})`;
            }
            body["ignoreNonWorkingDays"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.position !== undefined && args.position !== null && String(args.position).trim() !== "") {
        {
          const _n = Number(args.position);
          body["position"] = Number.isNaN(_n) ? args.position : _n;
        }
      }
      if (args.spentTime !== undefined && args.spentTime !== null && String(args.spentTime).trim() !== "") {
        body["spentTime"] = args.spentTime;
      }
      if (args.storyPoints !== undefined && args.storyPoints !== null && String(args.storyPoints).trim() !== "") {
        {
          const _n = Number(args.storyPoints);
          body["storyPoints"] = Number.isNaN(_n) ? args.storyPoints : _n;
        }
      }
      if (args.percentageDone !== undefined && args.percentageDone !== null && String(args.percentageDone).trim() !== "") {
        {
          const _n = Number(args.percentageDone);
          body["percentageDone"] = Number.isNaN(_n) ? args.percentageDone : _n;
        }
      }
      if (args.derivedPercentageDone !== undefined && args.derivedPercentageDone !== null && String(args.derivedPercentageDone).trim() !== "") {
        {
          const _n = Number(args.derivedPercentageDone);
          body["derivedPercentageDone"] = Number.isNaN(_n) ? args.derivedPercentageDone : _n;
        }
      }
      if (args.createdAt !== undefined && args.createdAt !== null && String(args.createdAt).trim() !== "") {
        body["createdAt"] = args.createdAt;
      }
      if (args.updatedAt !== undefined && args.updatedAt !== null && String(args.updatedAt).trim() !== "") {
        body["updatedAt"] = args.updatedAt;
      }
      {
        const _pe = applyParentLink(body, args); if (_pe) return _pe;
      }
      break;

      case "form_create":
      method = "POST"; path = `/api/v3/work_packages/form`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "offset", "pageSize", "filters", "sortBy", "groupBy", "showSums", "select", "notify", "displayId", "lockVersion", "subject", "_type", "description", "scheduleManually", "readonly", "hasProjectAttributes", "startDate", "dueDate", "date", "derivedStartDate", "derivedDueDate", "duration", "estimatedTime", "derivedEstimatedTime", "ignoreNonWorkingDays", "position", "spentTime", "storyPoints", "percentageDone", "derivedPercentageDone", "createdAt", "updatedAt", "_meta", "timestamps", "identifier", "comment", "internal", "query", "type", "_embedded", "user", "user_id", "work_package_id", "remindAt", "note", "parent_id", "parent", "category_id", "category"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.subject !== undefined && args.subject !== null && String(args.subject).trim() !== "") {
        body["subject"] = args.subject;
      }
      if (args.description !== undefined && args.description !== null && String(args.description).trim() !== "") {
        body["description"] = args.description;
      }
      if (args.scheduleManually !== undefined && args.scheduleManually !== null && String(args.scheduleManually).trim() !== "") {
        {
          const _raw = args.scheduleManually;
          if (typeof _raw === "boolean") {
            body["scheduleManually"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `scheduleManually muss boolean sein (got: ${args.scheduleManually})`;
            }
            body["scheduleManually"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.startDate !== undefined && args.startDate !== null && String(args.startDate).trim() !== "") {
        body["startDate"] = args.startDate;
      }
      if (args.dueDate !== undefined && args.dueDate !== null && String(args.dueDate).trim() !== "") {
        body["dueDate"] = args.dueDate;
      }
      if (args.estimatedTime !== undefined && args.estimatedTime !== null && String(args.estimatedTime).trim() !== "") {
        body["estimatedTime"] = args.estimatedTime;
      }
      if (args.duration !== undefined && args.duration !== null && String(args.duration).trim() !== "") {
        body["duration"] = args.duration;
      }
      if (args.ignoreNonWorkingDays !== undefined && args.ignoreNonWorkingDays !== null && String(args.ignoreNonWorkingDays).trim() !== "") {
        {
          const _raw = args.ignoreNonWorkingDays;
          if (typeof _raw === "boolean") {
            body["ignoreNonWorkingDays"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `ignoreNonWorkingDays muss boolean sein (got: ${args.ignoreNonWorkingDays})`;
            }
            body["ignoreNonWorkingDays"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args._meta !== undefined && args._meta !== null && String(args._meta).trim() !== "") {
        let _v__meta = args._meta;
        if (typeof _v__meta === "string") {
          const _s = String(_v__meta).trim();
          if (_s.startsWith("{") || _s.startsWith("[")) {
            try { _v__meta = JSON.parse(_s); }
            catch (e) { _v__meta = { raw: _s }; }
          } else {
            _v__meta = { raw: _s };
          }
        }
        if (typeof _v__meta !== "object" || _v__meta === null || Array.isArray(_v__meta)) {
          return `_meta muss ein Objekt sein (z.B. Formattable mit raw: string)`;
        }
        body["_meta"] = _v__meta;
      }
      break;

      case "list_schemas":
      missing = requireArgs(["filters"]); if (missing) return missing;
      method = "GET"; path = `/api/v3/work_packages/schemas`;
      {
        const _qs = new URLSearchParams();
        if (args.filters !== undefined && args.filters !== null && String(args.filters).trim() !== "") _qs.set("filters", String(args.filters));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "get_schema":
      missing = requireArgs(["identifier"]); if (missing) return missing;
      method = "GET"; path = `/api/v3/work_packages/schemas/${encodeURIComponent(args.identifier)}`;
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
      method = "DELETE"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}`;
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
      method = "GET"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}`;
      {
        const _qs = new URLSearchParams();
        if (args.timestamps !== undefined && args.timestamps !== null && String(args.timestamps).trim() !== "") _qs.set("timestamps", String(args.timestamps));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "update":
      missing = requireArgs(["id", "lockVersion"]); if (missing) return missing;
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
      method = "PATCH"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}`;
      {
        const _qs = new URLSearchParams();
        if (args.notify !== undefined && args.notify !== null && String(args.notify).trim() !== "") _qs.set("notify", String(args.notify));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "offset", "pageSize", "filters", "sortBy", "groupBy", "showSums", "select", "notify", "displayId", "lockVersion", "subject", "_type", "description", "scheduleManually", "readonly", "hasProjectAttributes", "startDate", "dueDate", "date", "derivedStartDate", "derivedDueDate", "duration", "estimatedTime", "derivedEstimatedTime", "ignoreNonWorkingDays", "position", "spentTime", "storyPoints", "percentageDone", "derivedPercentageDone", "createdAt", "updatedAt", "_meta", "timestamps", "identifier", "comment", "internal", "query", "type", "_embedded", "user", "user_id", "work_package_id", "remindAt", "note", "parent_id", "parent", "status_id", "status", "category_id", "category", "assignee_id", "assignee"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.subject !== undefined && args.subject !== null && String(args.subject).trim() !== "") {
        body["subject"] = args.subject;
      }
      if (args.description !== undefined && args.description !== null && String(args.description).trim() !== "") {
        body["description"] = args.description;
      }
      if (args.scheduleManually !== undefined && args.scheduleManually !== null && String(args.scheduleManually).trim() !== "") {
        {
          const _raw = args.scheduleManually;
          if (typeof _raw === "boolean") {
            body["scheduleManually"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `scheduleManually muss boolean sein (got: ${args.scheduleManually})`;
            }
            body["scheduleManually"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.startDate !== undefined && args.startDate !== null && String(args.startDate).trim() !== "") {
        body["startDate"] = args.startDate;
      }
      if (args.dueDate !== undefined && args.dueDate !== null && String(args.dueDate).trim() !== "") {
        body["dueDate"] = args.dueDate;
      }
      if (args.estimatedTime !== undefined && args.estimatedTime !== null && String(args.estimatedTime).trim() !== "") {
        body["estimatedTime"] = args.estimatedTime;
      }
      if (args.duration !== undefined && args.duration !== null && String(args.duration).trim() !== "") {
        body["duration"] = args.duration;
      }
      if (args.ignoreNonWorkingDays !== undefined && args.ignoreNonWorkingDays !== null && String(args.ignoreNonWorkingDays).trim() !== "") {
        {
          const _raw = args.ignoreNonWorkingDays;
          if (typeof _raw === "boolean") {
            body["ignoreNonWorkingDays"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `ignoreNonWorkingDays muss boolean sein (got: ${args.ignoreNonWorkingDays})`;
            }
            body["ignoreNonWorkingDays"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args._meta !== undefined && args._meta !== null && String(args._meta).trim() !== "") {
        let _v__meta = args._meta;
        if (typeof _v__meta === "string") {
          const _s = String(_v__meta).trim();
          if (_s.startsWith("{") || _s.startsWith("[")) {
            try { _v__meta = JSON.parse(_s); }
            catch (e) { _v__meta = { raw: _s }; }
          } else {
            _v__meta = { raw: _s };
          }
        }
        if (typeof _v__meta !== "object" || _v__meta === null || Array.isArray(_v__meta)) {
          return `_meta muss ein Objekt sein (z.B. Formattable mit raw: string)`;
        }
        body["_meta"] = _v__meta;
      }
      if (args.lockVersion !== undefined && args.lockVersion !== null && String(args.lockVersion).trim() !== "") {
        {
          const _n = Number(args.lockVersion);
          body["lockVersion"] = Number.isNaN(_n) ? args.lockVersion : _n;
        }
      }
      if (args.percentageDone !== undefined && args.percentageDone !== null && String(args.percentageDone).trim() !== "") {
        const _n = Number(args.percentageDone);
        if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 0) {
          return `percentageDone muss eine ganze Zahl und >= 0 sein (got: ${args.percentageDone})`;
        }
        body["percentageDone"] = _n;
      }
      {
        // ki-basis: status transition via HAL link (status_id or status)
        const statusRaw =
          args.status_id !== undefined && args.status_id !== null && String(args.status_id).trim() !== ""
            ? args.status_id
            : args.status !== undefined && args.status !== null && String(args.status).trim() !== ""
              ? args.status
              : null;
        if (statusRaw != null) {
          const _n = Number(statusRaw);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `status_id muss eine ganze Zahl und > 0 sein (got: ${statusRaw})`;
          }
          body._links = body._links || {};
          body._links.status = { href: `/api/v3/statuses/${_n}` };
        }
      }
      {
        // ki-basis: assignee via HAL link (assignee_id or assignee = user id)
        const assigneeRaw =
          args.assignee_id !== undefined &&
          args.assignee_id !== null &&
          String(args.assignee_id).trim() !== ""
            ? args.assignee_id
            : args.assignee !== undefined &&
                args.assignee !== null &&
                String(args.assignee).trim() !== "" &&
                /^\d+$/.test(String(args.assignee).trim())
              ? args.assignee
              : null;
        if (assigneeRaw != null) {
          const _n = Number(assigneeRaw);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `assignee_id muss eine ganze Zahl und > 0 sein (got: ${assigneeRaw})`;
          }
          body._links = body._links || {};
          body._links.assignee = { href: `/api/v3/users/${_n}` };
        }
      }
      {
        const _pe = applyParentLink(body, args); if (_pe) return _pe;
      }
      break;

      case "list_activities":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/activities`;
      break;

      case "comment":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/activities`;
      {
        const _qs = new URLSearchParams();
        if (args.notify !== undefined && args.notify !== null && String(args.notify).trim() !== "") _qs.set("notify", String(args.notify));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "offset", "pageSize", "filters", "sortBy", "groupBy", "showSums", "select", "notify", "displayId", "lockVersion", "subject", "_type", "description", "scheduleManually", "readonly", "hasProjectAttributes", "startDate", "dueDate", "date", "derivedStartDate", "derivedDueDate", "duration", "estimatedTime", "derivedEstimatedTime", "ignoreNonWorkingDays", "position", "spentTime", "storyPoints", "percentageDone", "derivedPercentageDone", "createdAt", "updatedAt", "_meta", "timestamps", "identifier", "comment", "internal", "query", "type", "_embedded", "user", "user_id", "work_package_id", "remindAt", "note", "parent_id", "parent", "category_id", "category"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.comment !== undefined && args.comment !== null && String(args.comment).trim() !== "") {
        let _v_comment = args.comment;
        if (typeof _v_comment === "string") {
          const _s = String(_v_comment).trim();
          if (_s.startsWith("{") || _s.startsWith("[")) {
            try { _v_comment = JSON.parse(_s); }
            catch (e) { _v_comment = { raw: _s }; }
          } else {
            _v_comment = { raw: _s };
          }
        }
        if (typeof _v_comment !== "object" || _v_comment === null || Array.isArray(_v_comment)) {
          return `comment muss ein Objekt sein (z.B. Formattable mit raw: string)`;
        }
        if (_v_comment.raw !== undefined && _v_comment.raw !== null && typeof _v_comment.raw !== "string") {
          return `comment.raw muss ein string sein`;
        }
        body["comment"] = _v_comment;
      }
      if (args.internal !== undefined && args.internal !== null && String(args.internal).trim() !== "") {
        {
          const _raw = args.internal;
          if (typeof _raw === "boolean") {
            body["internal"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `internal muss boolean sein (got: ${args.internal})`;
            }
            body["internal"] = (_s === "true" || _s === "1");
          }
        }
      }
      break;

      case "list_activities_emoji_reactions":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/activities_emoji_reactions`;
      break;

      case "available_assignees":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/available_assignees`;
      break;

      case "available_projects_for":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/available_projects`;
      break;

      case "list_available_relation_candidates":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/available_relation_candidates`;
      {
        const _qs = new URLSearchParams();
        if (args.pageSize !== undefined && args.pageSize !== null && String(args.pageSize).trim() !== "") _qs.set("pageSize", String(args.pageSize));
        if (args.filters !== undefined && args.filters !== null && String(args.filters).trim() !== "") _qs.set("filters", String(args.filters));
        if (args.query !== undefined && args.query !== null && String(args.query).trim() !== "") _qs.set("query", String(args.query));
        if (args.type !== undefined && args.type !== null && String(args.type).trim() !== "") _qs.set("type", String(args.type));
        if (args.sortBy !== undefined && args.sortBy !== null && String(args.sortBy).trim() !== "") _qs.set("sortBy", String(args.sortBy));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "available_watchers":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/available_watchers`;
      break;

      case "list_file_links":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/file_links`;
      {
        const _qs = new URLSearchParams();
        if (args.filters !== undefined && args.filters !== null && String(args.filters).trim() !== "") _qs.set("filters", String(args.filters));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "create_file_link":
      missing = requireArgs(["id", "_embedded"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/file_links`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "offset", "pageSize", "filters", "sortBy", "groupBy", "showSums", "select", "notify", "displayId", "lockVersion", "subject", "_type", "description", "scheduleManually", "readonly", "hasProjectAttributes", "startDate", "dueDate", "date", "derivedStartDate", "derivedDueDate", "duration", "estimatedTime", "derivedEstimatedTime", "ignoreNonWorkingDays", "position", "spentTime", "storyPoints", "percentageDone", "derivedPercentageDone", "createdAt", "updatedAt", "_meta", "timestamps", "identifier", "comment", "internal", "query", "type", "_embedded", "user", "user_id", "work_package_id", "remindAt", "note", "parent_id", "parent", "category_id", "category"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args._embedded !== undefined && args._embedded !== null && String(args._embedded).trim() !== "") {
        let _v__embedded = args._embedded;
        if (typeof _v__embedded === "string") {
          const _s = String(_v__embedded).trim();
          if (_s.startsWith("{") || _s.startsWith("[")) {
            try { _v__embedded = JSON.parse(_s); }
            catch (e) { _v__embedded = { raw: _s }; }
          } else {
            _v__embedded = { raw: _s };
          }
        }
        if (typeof _v__embedded !== "object" || _v__embedded === null || Array.isArray(_v__embedded)) {
          return `_embedded muss ein Objekt sein (z.B. Formattable mit raw: string)`;
        }
        body["_embedded"] = _v__embedded;
      }
      break;

      case "form_edit":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/form`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "offset", "pageSize", "filters", "sortBy", "groupBy", "showSums", "select", "notify", "displayId", "lockVersion", "subject", "_type", "description", "scheduleManually", "readonly", "hasProjectAttributes", "startDate", "dueDate", "date", "derivedStartDate", "derivedDueDate", "duration", "estimatedTime", "derivedEstimatedTime", "ignoreNonWorkingDays", "position", "spentTime", "storyPoints", "percentageDone", "derivedPercentageDone", "createdAt", "updatedAt", "_meta", "timestamps", "identifier", "comment", "internal", "query", "type", "_embedded", "user", "user_id", "work_package_id", "remindAt", "note", "parent_id", "parent", "category_id", "category"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.subject !== undefined && args.subject !== null && String(args.subject).trim() !== "") {
        body["subject"] = args.subject;
      }
      if (args.description !== undefined && args.description !== null && String(args.description).trim() !== "") {
        body["description"] = args.description;
      }
      if (args.scheduleManually !== undefined && args.scheduleManually !== null && String(args.scheduleManually).trim() !== "") {
        {
          const _raw = args.scheduleManually;
          if (typeof _raw === "boolean") {
            body["scheduleManually"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `scheduleManually muss boolean sein (got: ${args.scheduleManually})`;
            }
            body["scheduleManually"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.startDate !== undefined && args.startDate !== null && String(args.startDate).trim() !== "") {
        body["startDate"] = args.startDate;
      }
      if (args.dueDate !== undefined && args.dueDate !== null && String(args.dueDate).trim() !== "") {
        body["dueDate"] = args.dueDate;
      }
      if (args.estimatedTime !== undefined && args.estimatedTime !== null && String(args.estimatedTime).trim() !== "") {
        body["estimatedTime"] = args.estimatedTime;
      }
      if (args.duration !== undefined && args.duration !== null && String(args.duration).trim() !== "") {
        body["duration"] = args.duration;
      }
      if (args.ignoreNonWorkingDays !== undefined && args.ignoreNonWorkingDays !== null && String(args.ignoreNonWorkingDays).trim() !== "") {
        {
          const _raw = args.ignoreNonWorkingDays;
          if (typeof _raw === "boolean") {
            body["ignoreNonWorkingDays"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `ignoreNonWorkingDays muss boolean sein (got: ${args.ignoreNonWorkingDays})`;
            }
            body["ignoreNonWorkingDays"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args._meta !== undefined && args._meta !== null && String(args._meta).trim() !== "") {
        let _v__meta = args._meta;
        if (typeof _v__meta === "string") {
          const _s = String(_v__meta).trim();
          if (_s.startsWith("{") || _s.startsWith("[")) {
            try { _v__meta = JSON.parse(_s); }
            catch (e) { _v__meta = { raw: _s }; }
          } else {
            _v__meta = { raw: _s };
          }
        }
        if (typeof _v__meta !== "object" || _v__meta === null || Array.isArray(_v__meta)) {
          return `_meta muss ein Objekt sein (z.B. Formattable mit raw: string)`;
        }
        body["_meta"] = _v__meta;
      }
      break;

      case "revisions":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/revisions`;
      break;

      case "list_watchers":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/watchers`;
      break;

      case "add_watcher":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/watchers`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "offset", "pageSize", "filters", "sortBy", "groupBy", "showSums", "select", "notify", "displayId", "lockVersion", "subject", "_type", "description", "scheduleManually", "readonly", "hasProjectAttributes", "startDate", "dueDate", "date", "derivedStartDate", "derivedDueDate", "duration", "estimatedTime", "derivedEstimatedTime", "ignoreNonWorkingDays", "position", "spentTime", "storyPoints", "percentageDone", "derivedPercentageDone", "createdAt", "updatedAt", "_meta", "timestamps", "identifier", "comment", "internal", "query", "type", "_embedded", "user", "user_id", "work_package_id", "remindAt", "note", "parent_id", "parent", "category_id", "category"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.user !== undefined && args.user !== null && String(args.user).trim() !== "") {
        let _v_user = args.user;
        if (typeof _v_user === "string") {
          const _s = String(_v_user).trim();
          if (_s.startsWith("{") || _s.startsWith("[")) {
            try { _v_user = JSON.parse(_s); }
            catch (e) { _v_user = { raw: _s }; }
          } else {
            _v_user = { raw: _s };
          }
        }
        if (typeof _v_user !== "object" || _v_user === null || Array.isArray(_v_user)) {
          return `user muss ein Objekt sein (z.B. Formattable mit raw: string)`;
        }
        if (_v_user.href !== undefined && _v_user.href !== null && typeof _v_user.href !== "string") {
          return `user.href muss ein string sein`;
        }
        body["user"] = _v_user;
      }
      break;

      case "delete_watcher":
      missing = requireArgs(["id", "user_id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      {
        if (args.user_id !== undefined && args.user_id !== null && String(args.user_id).trim() !== "") {
          const _n = Number(args.user_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `user_id muss eine ganze Zahl und > 0 sein (got: ${args.user_id})`;
          }
        }
      }
      method = "DELETE"; path = `/api/v3/work_packages/${encodeURIComponent(args.id)}/watchers/${encodeURIComponent(args.user_id)}`;
      break;

      case "list_reminders":
      missing = requireArgs(["work_package_id"]); if (missing) return missing;
      {
        if (args.work_package_id !== undefined && args.work_package_id !== null && String(args.work_package_id).trim() !== "") {
          const _n = Number(args.work_package_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `work_package_id muss eine ganze Zahl und > 0 sein (got: ${args.work_package_id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/work_packages/${encodeURIComponent(args.work_package_id)}/reminders`;
      break;

      case "create_reminder":
      missing = requireArgs(["work_package_id", "remindAt"]); if (missing) return missing;
      {
        if (args.work_package_id !== undefined && args.work_package_id !== null && String(args.work_package_id).trim() !== "") {
          const _n = Number(args.work_package_id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `work_package_id muss eine ganze Zahl und > 0 sein (got: ${args.work_package_id})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/work_packages/${encodeURIComponent(args.work_package_id)}/reminders`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "offset", "pageSize", "filters", "sortBy", "groupBy", "showSums", "select", "notify", "displayId", "lockVersion", "subject", "_type", "description", "scheduleManually", "readonly", "hasProjectAttributes", "startDate", "dueDate", "date", "derivedStartDate", "derivedDueDate", "duration", "estimatedTime", "derivedEstimatedTime", "ignoreNonWorkingDays", "position", "spentTime", "storyPoints", "percentageDone", "derivedPercentageDone", "createdAt", "updatedAt", "_meta", "timestamps", "identifier", "comment", "internal", "query", "type", "_embedded", "user", "user_id", "work_package_id", "remindAt", "note", "parent_id", "parent", "category_id", "category"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.remindAt !== undefined && args.remindAt !== null && String(args.remindAt).trim() !== "") {
        body["remindAt"] = args.remindAt;
      }
      if (args.note !== undefined && args.note !== null && String(args.note).trim() !== "") {
        body["note"] = args.note;
      }
      break;

      case "workspace_available_assignees":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/workspaces/${encodeURIComponent(args.id)}/available_assignees`;
      break;

      case "get_workspace_collection":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "GET"; path = `/api/v3/workspaces/${encodeURIComponent(args.id)}/work_packages`;
      {
        const _qs = new URLSearchParams();
        if (args.offset !== undefined && args.offset !== null && String(args.offset).trim() !== "") _qs.set("offset", String(args.offset));
        if (args.pageSize !== undefined && args.pageSize !== null && String(args.pageSize).trim() !== "") _qs.set("pageSize", String(args.pageSize));
        if (args.filters !== undefined && args.filters !== null && String(args.filters).trim() !== "") _qs.set("filters", String(args.filters));
        if (args.sortBy !== undefined && args.sortBy !== null && String(args.sortBy).trim() !== "") _qs.set("sortBy", String(args.sortBy));
        if (args.groupBy !== undefined && args.groupBy !== null && String(args.groupBy).trim() !== "") _qs.set("groupBy", String(args.groupBy));
        if (args.showSums !== undefined && args.showSums !== null && String(args.showSums).trim() !== "") _qs.set("showSums", String(args.showSums));
        if (args.select !== undefined && args.select !== null && String(args.select).trim() !== "") _qs.set("select", String(args.select));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      break;

      case "create_workspace":
      missing = requireArgs(["id", "subject"]); if (missing) return missing;
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
      {
        if (args.position !== undefined && args.position !== null && String(args.position).trim() !== "") {
          const _n = Number(args.position);
          if (!Number.isFinite(_n) || !Number.isInteger(_n)) {
            return `position muss eine ganze Zahl sein (got: ${args.position})`;
          }
        }
      }
      {
        if (args.storyPoints !== undefined && args.storyPoints !== null && String(args.storyPoints).trim() !== "") {
          const _n = Number(args.storyPoints);
          if (!Number.isFinite(_n) || !Number.isInteger(_n)) {
            return `storyPoints muss eine ganze Zahl sein (got: ${args.storyPoints})`;
          }
        }
      }
      {
        if (args.percentageDone !== undefined && args.percentageDone !== null && String(args.percentageDone).trim() !== "") {
          const _n = Number(args.percentageDone);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 0) {
            return `percentageDone muss eine ganze Zahl und >= 0 sein (got: ${args.percentageDone})`;
          }
        }
      }
      {
        if (args.derivedPercentageDone !== undefined && args.derivedPercentageDone !== null && String(args.derivedPercentageDone).trim() !== "") {
          const _n = Number(args.derivedPercentageDone);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 0) {
            return `derivedPercentageDone muss eine ganze Zahl und >= 0 sein (got: ${args.derivedPercentageDone})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/workspaces/${encodeURIComponent(args.id)}/work_packages`;
      {
        const _qs = new URLSearchParams();
        if (args.notify !== undefined && args.notify !== null && String(args.notify).trim() !== "") _qs.set("notify", String(args.notify));
        const _q = _qs.toString() ? `?${_qs.toString()}` : "";
        path = path + _q;
      }
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "offset", "pageSize", "filters", "sortBy", "groupBy", "showSums", "select", "notify", "displayId", "lockVersion", "subject", "_type", "description", "scheduleManually", "readonly", "hasProjectAttributes", "startDate", "dueDate", "date", "derivedStartDate", "derivedDueDate", "duration", "estimatedTime", "derivedEstimatedTime", "ignoreNonWorkingDays", "position", "spentTime", "storyPoints", "percentageDone", "derivedPercentageDone", "createdAt", "updatedAt", "_meta", "timestamps", "identifier", "comment", "internal", "query", "type", "_embedded", "user", "user_id", "work_package_id", "remindAt", "note", "parent_id", "parent", "category_id", "category"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.displayId !== undefined && args.displayId !== null && String(args.displayId).trim() !== "") {
        body["displayId"] = args.displayId;
      }
      if (args.lockVersion !== undefined && args.lockVersion !== null && String(args.lockVersion).trim() !== "") {
        {
          const _n = Number(args.lockVersion);
          body["lockVersion"] = Number.isNaN(_n) ? args.lockVersion : _n;
        }
      }
      if (args.subject !== undefined && args.subject !== null && String(args.subject).trim() !== "") {
        body["subject"] = args.subject;
      }
      if (args._type !== undefined && args._type !== null && String(args._type).trim() !== "") {
        {
          const _allowed = ["WorkPackage"];
          if (!_allowed.includes(String(args._type))) {
            return `_type muss einer von: ${_allowed.join(", ")} sein (got: ${args._type})`;
          }
        }
        body["_type"] = args._type;
      }
      if (args.description !== undefined && args.description !== null && String(args.description).trim() !== "") {
        body["description"] = args.description;
      }
      if (args.scheduleManually !== undefined && args.scheduleManually !== null && String(args.scheduleManually).trim() !== "") {
        {
          const _raw = args.scheduleManually;
          if (typeof _raw === "boolean") {
            body["scheduleManually"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `scheduleManually muss boolean sein (got: ${args.scheduleManually})`;
            }
            body["scheduleManually"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.readonly !== undefined && args.readonly !== null && String(args.readonly).trim() !== "") {
        {
          const _raw = args.readonly;
          if (typeof _raw === "boolean") {
            body["readonly"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `readonly muss boolean sein (got: ${args.readonly})`;
            }
            body["readonly"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.hasProjectAttributes !== undefined && args.hasProjectAttributes !== null && String(args.hasProjectAttributes).trim() !== "") {
        {
          const _raw = args.hasProjectAttributes;
          if (typeof _raw === "boolean") {
            body["hasProjectAttributes"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `hasProjectAttributes muss boolean sein (got: ${args.hasProjectAttributes})`;
            }
            body["hasProjectAttributes"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.startDate !== undefined && args.startDate !== null && String(args.startDate).trim() !== "") {
        body["startDate"] = args.startDate;
      }
      if (args.dueDate !== undefined && args.dueDate !== null && String(args.dueDate).trim() !== "") {
        body["dueDate"] = args.dueDate;
      }
      if (args.date !== undefined && args.date !== null && String(args.date).trim() !== "") {
        body["date"] = args.date;
      }
      if (args.derivedStartDate !== undefined && args.derivedStartDate !== null && String(args.derivedStartDate).trim() !== "") {
        body["derivedStartDate"] = args.derivedStartDate;
      }
      if (args.derivedDueDate !== undefined && args.derivedDueDate !== null && String(args.derivedDueDate).trim() !== "") {
        body["derivedDueDate"] = args.derivedDueDate;
      }
      if (args.duration !== undefined && args.duration !== null && String(args.duration).trim() !== "") {
        body["duration"] = args.duration;
      }
      if (args.estimatedTime !== undefined && args.estimatedTime !== null && String(args.estimatedTime).trim() !== "") {
        body["estimatedTime"] = args.estimatedTime;
      }
      if (args.derivedEstimatedTime !== undefined && args.derivedEstimatedTime !== null && String(args.derivedEstimatedTime).trim() !== "") {
        body["derivedEstimatedTime"] = args.derivedEstimatedTime;
      }
      if (args.ignoreNonWorkingDays !== undefined && args.ignoreNonWorkingDays !== null && String(args.ignoreNonWorkingDays).trim() !== "") {
        {
          const _raw = args.ignoreNonWorkingDays;
          if (typeof _raw === "boolean") {
            body["ignoreNonWorkingDays"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `ignoreNonWorkingDays muss boolean sein (got: ${args.ignoreNonWorkingDays})`;
            }
            body["ignoreNonWorkingDays"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.position !== undefined && args.position !== null && String(args.position).trim() !== "") {
        {
          const _n = Number(args.position);
          body["position"] = Number.isNaN(_n) ? args.position : _n;
        }
      }
      if (args.spentTime !== undefined && args.spentTime !== null && String(args.spentTime).trim() !== "") {
        body["spentTime"] = args.spentTime;
      }
      if (args.storyPoints !== undefined && args.storyPoints !== null && String(args.storyPoints).trim() !== "") {
        {
          const _n = Number(args.storyPoints);
          body["storyPoints"] = Number.isNaN(_n) ? args.storyPoints : _n;
        }
      }
      if (args.percentageDone !== undefined && args.percentageDone !== null && String(args.percentageDone).trim() !== "") {
        {
          const _n = Number(args.percentageDone);
          body["percentageDone"] = Number.isNaN(_n) ? args.percentageDone : _n;
        }
      }
      if (args.derivedPercentageDone !== undefined && args.derivedPercentageDone !== null && String(args.derivedPercentageDone).trim() !== "") {
        {
          const _n = Number(args.derivedPercentageDone);
          body["derivedPercentageDone"] = Number.isNaN(_n) ? args.derivedPercentageDone : _n;
        }
      }
      if (args.createdAt !== undefined && args.createdAt !== null && String(args.createdAt).trim() !== "") {
        body["createdAt"] = args.createdAt;
      }
      if (args.updatedAt !== undefined && args.updatedAt !== null && String(args.updatedAt).trim() !== "") {
        body["updatedAt"] = args.updatedAt;
      }
      break;

      case "form_create_in_workspace":
      missing = requireArgs(["id"]); if (missing) return missing;
      {
        if (args.id !== undefined && args.id !== null && String(args.id).trim() !== "") {
          const _n = Number(args.id);
          if (!Number.isFinite(_n) || !Number.isInteger(_n) || _n < 1) {
            return `id muss eine ganze Zahl und > 0 sein (got: ${args.id})`;
          }
        }
      }
      method = "POST"; path = `/api/v3/workspaces/${encodeURIComponent(args.id)}/work_packages/form`;
      {
        const knownArgs = new Set(["operation", "confirmed", "id", "offset", "pageSize", "filters", "sortBy", "groupBy", "showSums", "select", "notify", "displayId", "lockVersion", "subject", "_type", "description", "scheduleManually", "readonly", "hasProjectAttributes", "startDate", "dueDate", "date", "derivedStartDate", "derivedDueDate", "duration", "estimatedTime", "derivedEstimatedTime", "ignoreNonWorkingDays", "position", "spentTime", "storyPoints", "percentageDone", "derivedPercentageDone", "createdAt", "updatedAt", "_meta", "timestamps", "identifier", "comment", "internal", "query", "type", "_embedded", "user", "user_id", "work_package_id", "remindAt", "note", "parent_id", "parent", "category_id", "category"]);
        for (const key of Object.keys(args)) {
          if (knownArgs.has(key)) continue;
          if (args[key] === undefined || args[key] === null || String(args[key]).trim() === "") continue;
          return `Unbekanntes Feld für operation=${operation}: ${key}`;
        }
      }
      body = {};
      if (args.subject !== undefined && args.subject !== null && String(args.subject).trim() !== "") {
        body["subject"] = args.subject;
      }
      if (args.description !== undefined && args.description !== null && String(args.description).trim() !== "") {
        body["description"] = args.description;
      }
      if (args.scheduleManually !== undefined && args.scheduleManually !== null && String(args.scheduleManually).trim() !== "") {
        {
          const _raw = args.scheduleManually;
          if (typeof _raw === "boolean") {
            body["scheduleManually"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `scheduleManually muss boolean sein (got: ${args.scheduleManually})`;
            }
            body["scheduleManually"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args.startDate !== undefined && args.startDate !== null && String(args.startDate).trim() !== "") {
        body["startDate"] = args.startDate;
      }
      if (args.dueDate !== undefined && args.dueDate !== null && String(args.dueDate).trim() !== "") {
        body["dueDate"] = args.dueDate;
      }
      if (args.estimatedTime !== undefined && args.estimatedTime !== null && String(args.estimatedTime).trim() !== "") {
        body["estimatedTime"] = args.estimatedTime;
      }
      if (args.duration !== undefined && args.duration !== null && String(args.duration).trim() !== "") {
        body["duration"] = args.duration;
      }
      if (args.ignoreNonWorkingDays !== undefined && args.ignoreNonWorkingDays !== null && String(args.ignoreNonWorkingDays).trim() !== "") {
        {
          const _raw = args.ignoreNonWorkingDays;
          if (typeof _raw === "boolean") {
            body["ignoreNonWorkingDays"] = _raw;
          } else {
            const _s = String(_raw).trim().toLowerCase();
            if (_s !== "true" && _s !== "false" && _s !== "1" && _s !== "0") {
              return `ignoreNonWorkingDays muss boolean sein (got: ${args.ignoreNonWorkingDays})`;
            }
            body["ignoreNonWorkingDays"] = (_s === "true" || _s === "1");
          }
        }
      }
      if (args._meta !== undefined && args._meta !== null && String(args._meta).trim() !== "") {
        let _v__meta = args._meta;
        if (typeof _v__meta === "string") {
          const _s = String(_v__meta).trim();
          if (_s.startsWith("{") || _s.startsWith("[")) {
            try { _v__meta = JSON.parse(_s); }
            catch (e) { _v__meta = { raw: _s }; }
          } else {
            _v__meta = { raw: _s };
          }
        }
        if (typeof _v__meta !== "object" || _v__meta === null || Array.isArray(_v__meta)) {
          return `_meta muss ein Objekt sein (z.B. Formattable mit raw: string)`;
        }
        body["_meta"] = _v__meta;
      }
      break;
      default:
        return `Unbekannte operation: ${operation}`;
    }

    // Category / Tag / Label: resolve name→id; list must be project-scoped
    // (global /work_packages?filters=category crashes on this OP build).
    if (operation === "list" || operation === "get_project_collection") {
      let filters = parseFiltersArg(args.filters);
      const catIdx = filters.findIndex((f) => f && f.category);
      if (catIdx >= 0) {
        let projectId = String(args.projectId || "").trim();
        if (!projectId && operation === "get_project_collection") {
          projectId = String(args.id || "").trim();
        }
        if (!projectId) {
          const proj = filters.find((f) => f && f.project);
          const vals = proj && proj.project && proj.project.values;
          if (Array.isArray(vals) && vals[0] != null) projectId = String(vals[0]).trim();
        }
        if (!projectId) {
          return "Ask: In welchem Projekt soll nach Tag/Label (Kategorie) gefiltert werden?";
        }
        const catVal =
          filters[catIdx].category &&
          Array.isArray(filters[catIdx].category.values) &&
          filters[catIdx].category.values[0] != null
            ? String(filters[catIdx].category.values[0]).trim()
            : "";
        const resolved = await resolveCategoryInProject(projectId, catVal);
        if (resolved && resolved.error) return resolved.error;
        if (resolved && resolved.id) {
          filters[catIdx] = {
            category: {
              operator: filters[catIdx].category.operator || "=",
              values: [resolved.id],
            },
          };
        }
        // Drop project filter when path is project-scoped
        filters = filters.filter((f) => !(f && f.project));
        args = { ...args, filters: JSON.stringify(filters) };
        if (operation === "list") {
          const _qs = new URLSearchParams();
          if (args.offset != null && String(args.offset).trim() !== "") _qs.set("offset", String(args.offset));
          if (args.pageSize != null && String(args.pageSize).trim() !== "") _qs.set("pageSize", String(args.pageSize));
          if (args.filters != null && String(args.filters).trim() !== "") _qs.set("filters", String(args.filters));
          if (args.sortBy != null && String(args.sortBy).trim() !== "") _qs.set("sortBy", String(args.sortBy));
          if (args.groupBy != null && String(args.groupBy).trim() !== "") _qs.set("groupBy", String(args.groupBy));
          if (args.showSums != null && String(args.showSums).trim() !== "") _qs.set("showSums", String(args.showSums));
          if (args.select != null && String(args.select).trim() !== "") _qs.set("select", String(args.select));
          if (args.timestamps != null && String(args.timestamps).trim() !== "") _qs.set("timestamps", String(args.timestamps));
          const _q = _qs.toString() ? `?${_qs.toString()}` : "";
          path = `/api/v3/projects/${encodeURIComponent(projectId)}/work_packages` + _q;
        } else {
          // get_project_collection: rebuild query with resolved filters
          const _qs = new URLSearchParams();
          if (args.offset != null && String(args.offset).trim() !== "") _qs.set("offset", String(args.offset));
          if (args.pageSize != null && String(args.pageSize).trim() !== "") _qs.set("pageSize", String(args.pageSize));
          if (args.filters != null && String(args.filters).trim() !== "") _qs.set("filters", String(args.filters));
          if (args.sortBy != null && String(args.sortBy).trim() !== "") _qs.set("sortBy", String(args.sortBy));
          if (args.groupBy != null && String(args.groupBy).trim() !== "") _qs.set("groupBy", String(args.groupBy));
          if (args.showSums != null && String(args.showSums).trim() !== "") _qs.set("showSums", String(args.showSums));
          if (args.select != null && String(args.select).trim() !== "") _qs.set("select", String(args.select));
          const _q = _qs.toString() ? `?${_qs.toString()}` : "";
          path = `/api/v3/projects/${encodeURIComponent(args.id)}/work_packages` + _q;
        }
      }
    }

    if (
      body &&
      (operation === "create_project" ||
        operation === "create" ||
        operation === "update" ||
        operation === "create_workspace")
    ) {
      const _ce = await applyCategoryLink(
        body,
        args,
        operation === "create_project" || operation === "create_workspace"
          ? args.id
          : args.projectId
      );
      if (_ce) return _ce;
    }

    const confirmBlock = confirmOrNull({
      hubId: "openproject-work-packages",
      operation,
      method,
      args,
    });
    if (confirmBlock) return confirmBlock;

    const wantsFetchAll = (() => {
      const fa = String(args.fetchAll || "").trim().toLowerCase();
      if (fa === "1" || fa === "true" || fa === "yes" || fa === "all") return true;
      return String(args.pageSize || "").trim().toLowerCase() === "all";
    })();

    /**
     * Transparently load the full list collection when fetchAll is set.
     * This OP build often omits HAL `_links.next` even when total > pageSize;
     * offset is a 1-based page index (not an element offset). Prefer one high
     * pageSize request; if more remain, advance offset=2,3,… internally.
     * Safety cap only: if hit, report how many were omitted — never “next page”.
     */
    const fetchOpCollection = async (startPath) => {
      const maxPages = Math.max(
        1,
        Number(process.env.OPENPROJECT_LIST_MAX_PAGES || 40) || 40
      );
      const maxItems = Math.max(
        1,
        Number(process.env.OPENPROJECT_LIST_MAX_ITEMS || 500) || 500
      );
      let cursorPath = startPath;
      let total = null;
      const elements = [];
      let pages = 0;
      let truncated = false;
      let pageIndex = 1;
      while (pages < maxPages) {
        pages += 1;
        const res = await fetch(`${base}${cursorPath}`, {
          method: "GET",
          headers,
        });
        if (!res.ok) {
          return {
            error: `OpenProject-Fehler ${res.status}: ${await res.text()}`,
          };
        }
        const _raw = await res.text();
        if (!_raw || !String(_raw).trim()) {
          return { error: `(leer, HTTP ${res.status})` };
        }
        let page;
        try {
          page = JSON.parse(_raw);
        } catch (e) {
          return { error: `Fehler beim Aufruf von OpenProject: ${e.message}` };
        }
        if (page && page.total != null) total = page.total;
        const els =
          page && page._embedded && Array.isArray(page._embedded.elements)
            ? page._embedded.elements
            : [];
        for (const el of els) {
          if (elements.length >= maxItems) {
            truncated = true;
            break;
          }
          elements.push(el);
        }
        if (truncated) break;
        const nextHref =
          page && page._links && page._links.next && page._links.next.href;
        if (nextHref) {
          if (String(nextHref).startsWith("http")) {
            try {
              const u = new URL(nextHref);
              cursorPath = `${u.pathname}${u.search}`;
            } catch {
              break;
            }
          } else {
            cursorPath = String(nextHref);
          }
        } else if (
          total != null &&
          els.length > 0 &&
          elements.length < Number(total)
        ) {
          // No HAL next: advance 1-based page offset.
          const qIdx = String(cursorPath).indexOf("?");
          const pathOnly = qIdx >= 0 ? cursorPath.slice(0, qIdx) : cursorPath;
          const qs = new URLSearchParams(
            qIdx >= 0 ? cursorPath.slice(qIdx + 1) : ""
          );
          const curPage = Number(qs.get("offset") || pageIndex) || pageIndex;
          pageIndex = curPage + 1;
          qs.set("offset", String(pageIndex));
          cursorPath = `${pathOnly}?${qs.toString()}`;
        } else {
          break;
        }
        if (els.length === 0) break;
      }
      if (pages >= maxPages && total != null && elements.length < Number(total)) {
        truncated = true;
      }
      return {
        item: {
          _type: "Collection",
          total: total != null ? total : elements.length,
          count: elements.length,
          _embedded: { elements },
          _meta: {
            fetchAll: true,
            pages,
            truncated,
            maxItems,
          },
        },
      };
    };

    try {
      let item;
      if (wantsFetchAll && String(method).toUpperCase() === "GET" && operation === "list") {
        // Prefer one large page (this OP accepts pageSize=500+); loop by page offset if needed.
        const chunk = Math.max(
          1,
          Number(process.env.OPENPROJECT_LIST_CHUNK_SIZE || 500) || 500
        );
        const qIdx = String(path).indexOf("?");
        const pathOnly = qIdx >= 0 ? path.slice(0, qIdx) : path;
        const qs = new URLSearchParams(qIdx >= 0 ? path.slice(qIdx + 1) : "");
        qs.delete("offset");
        qs.set("pageSize", String(chunk));
        const listPath = `${pathOnly}?${qs.toString()}`;
        const paged = await fetchOpCollection(listPath);
        if (paged.error) return paged.error;
        item = paged.item;
      } else {
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
        try { item = JSON.parse(_raw); }
        catch (e) { return `Fehler beim Aufruf von OpenProject: ${e.message}`; }
      }
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
      // Local post-filters when OP lacks an operator (e.g. non-empty description).
      // Applied only after server-side filters + optional fetchAll narrowing.
      const postFilter = String(args.postFilter || "").trim();
      if (
        postFilter &&
        item &&
        item._type &&
        (item._type === "Collection" || String(item._type).endsWith("Collection"))
      ) {
        const elsIn =
          item._embedded && Array.isArray(item._embedded.elements)
            ? item._embedded.elements
            : [];
        const hasDesc = (el) => {
          if (!el || typeof el !== "object") return false;
          const desc = el.description;
          if (desc == null) return false;
          if (typeof desc === "string") return desc.trim().length > 0;
          if (typeof desc === "object") {
            const raw = String(desc.raw || "").trim();
            if (raw) return true;
            const html = String(desc.html || "").trim();
            if (!html) return false;
            const text = html
              .replace(/<[^>]+>/g, " ")
              .replace(/&nbsp;/gi, " ")
              .replace(/\s+/g, " ")
              .trim();
            return text.length > 0;
          }
          return false;
        };
        let filtered = elsIn;
        if (postFilter === "nonEmptyDescription") {
          filtered = elsIn.filter(hasDesc);
        }
        if (filtered !== elsIn) {
          item = {
            ...item,
            total: filtered.length,
            count: filtered.length,
            _embedded: { ...(item._embedded || {}), elements: filtered },
            _meta: {
              ...(item._meta || {}),
              postFilter,
              prePostFilterTotal:
                item.total != null ? item.total : elsIn.length,
              prePostFilterCount: elsIn.length,
            },
          };
        }
      }
      if (item && item._type && (item._type === "Collection" || String(item._type).endsWith("Collection"))) {
        const els = (item._embedded && item._embedded.elements) ? item._embedded.elements : [];
        const fullFetch = item._meta && item._meta.fetchAll;
        let out;
        if (fullFetch) {
          // No page-oriented header: count only, or “n von total” when safety-capped.
          if (!els.length) {
            out = ui.empty(item.total ?? 0);
          } else {
            const head =
              item._meta.truncated && item.total != null && Number(item.total) > els.length
                ? locale === "en"
                  ? `Entries (${els.length} of ${item.total})`
                  : `Einträge (${els.length} von ${item.total})`
                : locale === "en"
                  ? `Entries (${els.length})`
                  : `Einträge (${els.length})`;
            // Rebuild table body via collectionTable then replace first line
            const table = collectionTable(els, item.total);
            const lines = table.split("\n");
            lines[0] = head;
            out = lines.join("\n");
          }
          if (item._meta.truncated && item.total != null) {
            const omitted = Math.max(0, Number(item.total) - els.length);
            out +=
              locale === "en"
                ? `\n\n_Safety limit: ${els.length} shown, ${omitted} omitted._`
                : `\n\n_Sicherheitslimit: ${els.length} angezeigt, ${omitted} weggelassen._`;
          }
        } else {
          out = collectionTable(els, item.total);
        }
        return out;
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
