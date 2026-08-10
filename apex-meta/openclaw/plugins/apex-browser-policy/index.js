import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";

import { registerApexBrowserPolicy } from "./plugin.js";

export default definePluginEntry({
  id: "apex-browser-policy",
  name: "APEX Browser Policy",
  description: "Fail-closed request-scoped browser containment for apex-executor",
  register: registerApexBrowserPolicy,
});
