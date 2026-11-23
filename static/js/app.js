import { renderGraph } from "./canvas.js";

const promptEl  = document.getElementById("prompt");
const viewpoint = document.getElementById("viewpoint");
const generate  = document.getElementById("generate");
const genIcon   = document.getElementById("generate-icon");
const statusEl  = document.getElementById("status");
const exportBtn = document.getElementById("export-svg");
const clearBtn  = document.getElementById("clear-btn");
const llmBadge  = document.getElementById("llm-badge");
const genInfo   = document.getElementById("generation-info");

// ── Check LLM Status on Load ────────────────────────────────────
async function checkLLMStatus() {
  try {
    const res  = await fetch("/api/llm-status");
    const data = await res.json();
    if (data.available) {
      llmBadge.textContent = `AI: ${data.model || "Gemini"} (${data.provider || "Vertex"})`;
      llmBadge.className = "badge badge-success";
    } else {
      llmBadge.textContent = "AI: Deterministic Fallback";
      llmBadge.className = "badge badge-warn";
    }
  } catch {
    llmBadge.textContent = "AI: Deterministic";
    llmBadge.className = "badge badge-warn";
  }
}
checkLLMStatus();

// ── Generate Diagram ────────────────────────────────────────────
generate.addEventListener("click", async () => {
  const promptText = promptEl?.value?.trim();
  if (!promptText) {
    statusEl.textContent = "Please enter an architecture prompt.";
    return;
  }

  generate.disabled = true;
  exportBtn.disabled = true;
  if (genIcon) {
    genIcon.textContent = "⟳";
    genIcon.classList.add("spinning");
  }
  statusEl.textContent = "Generating architecture…";
  genInfo.classList.add("hidden");

  try {
    const response = await fetch("/api/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        prompt: promptText,
        viewpoint: viewpoint?.value || null
      }),
    });

    let data;
    try {
      data = await response.json();
    } catch {
      throw new Error(`Server returned an invalid response (HTTP ${response.status})`);
    }

    if (!response.ok) {
      throw new Error(extractMessage(data));
    }

    if (!data?.graph) {
      throw new Error("Generation result does not contain a graph model.");
    }

    renderGraph(data.graph);
    renderInspector(data.analysis || {});

    const extraction = data.analysis?.extraction || {};
    if (extraction.elements_found != null) {
      const parts = [`${extraction.elements_found} components`];
      if (extraction.relationships_found != null) {
        parts.push(`${extraction.relationships_found} connections`);
      }
      if (extraction.coverage_score != null) {
        parts.push(`coverage ${Math.round(extraction.coverage_score * 100)}%`);
      }
      genInfo.textContent = parts.join(" · ");
      genInfo.classList.remove("hidden");
    }

    const valid = data.analysis?.validation?.valid;
    statusEl.textContent = valid === false ? "⚠ Generated with warnings" : "✓ Generated";
    exportBtn.disabled = false;
  } catch (err) {
    statusEl.textContent = `Error: ${err.message}`;
    console.error("Architecture generation error:", err);
  } finally {
    generate.disabled = false;
    if (genIcon) {
      genIcon.textContent = "▶";
      genIcon.classList.remove("spinning");
    }
  }
});

// ── Export SVG ──────────────────────────────────────────────────
exportBtn.addEventListener("click", () => {
  const svg = document.querySelector(".architecture-svg");
  if (!svg) return;
  const serializer = new XMLSerializer();
  const source = '<?xml version="1.0" standalone="no"?>\r\n' + serializer.serializeToString(svg);
  const blob = new Blob([source], { type: "image/svg+xml;charset=utf-8" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "enterprise-architecture.svg";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
});

// ── Clear Canvas & Form ─────────────────────────────────────────
clearBtn.addEventListener("click", () => {
  if (promptEl) promptEl.value = "";
  const canvas = document.getElementById("canvas");
  if (canvas) {
    canvas.innerHTML = `<div class="empty-state" id="empty-hint">Enter an architecture prompt above and click <strong>Generate Diagram</strong> to produce a standard diagram.</div>`;
  }
  const validation = document.getElementById("validation");
  if (validation) {
    validation.innerHTML = `<p class="muted">No diagram generated yet.</p>`;
  }
  exportBtn.disabled = true;
  statusEl.textContent = "Ready";
  genInfo.classList.add("hidden");
});

// ── Render Inspector Sidebar ────────────────────────────────────
function renderInspector(analysis) {
  const container = document.getElementById("validation");
  if (!container) return;
  container.innerHTML = "";

  const intent = analysis.intent || {};
  const extraction = analysis.extraction || {};
  const validation = analysis.validation || {};
  const enterprise = analysis.enterprise || {};

  // Intent section
  if (intent.architecture_type) {
    const s = section("Architecture Intent");
    s.appendChild(pill(`Type: ${intent.architecture_type}`, "info"));
    if (intent.viewpoint) s.appendChild(pill(`View: ${intent.viewpoint}`, "info"));
    if (intent.complexity) s.appendChild(pill(`Complexity: ${intent.complexity}`, "info"));
    container.appendChild(s);
  }

  // Extraction section
  if (extraction.elements_found != null) {
    const s = section("Extracted Components");
    s.appendChild(pill(`${extraction.elements_found} elements`, "ok"));
    if (extraction.relationships_found != null) {
      s.appendChild(pill(`${extraction.relationships_found} relationships`, "ok"));
    }
    if (extraction.coverage_score != null) {
      const pct = Math.round(extraction.coverage_score * 100);
      s.appendChild(pill(`Coverage: ${pct}%`, pct >= 70 ? "ok" : "warn"));
    }
    if (extraction.missing_concepts?.length) {
      extraction.missing_concepts.slice(0, 4).forEach(c => s.appendChild(pill(`Missing: ${c}`, "warn")));
    }
    container.appendChild(s);
  }

  // Enterprise Layers section
  if (enterprise.layers?.length) {
    const s = section("Enterprise Layers");
    enterprise.layers.forEach(l => s.appendChild(pill(l, "info")));
    container.appendChild(s);
  }

  // Validation issues
  if (validation.issues?.length) {
    const s = section("Validation Checks");
    validation.issues.slice(0, 8).forEach(issue => {
      const cls = issue.severity === "error" ? "err" : issue.severity === "warning" ? "warn" : "info";
      s.appendChild(pill(issue.message || issue.code, cls));
    });
    container.appendChild(s);
  } else if (validation.valid != null) {
    const s = section("Validation");
    s.appendChild(pill(validation.valid ? "✓ Standard Compliant" : "Review needed", validation.valid ? "ok" : "warn"));
    container.appendChild(s);
  }
}

function section(title) {
  const div = document.createElement("div");
  div.className = "val-section";
  const h = document.createElement("h3");
  h.textContent = title;
  div.appendChild(h);
  return div;
}

function pill(text, type) {
  const span = document.createElement("span");
  span.className = `val-pill pill-${type}`;
  span.textContent = text;
  return span;
}

function extractMessage(data) {
  if (!data) return "Generation failed";
  if (typeof data.detail === "string") return data.detail;
  if (data.detail?.message) return data.detail.message;
  if (typeof data.message === "string") return data.message;
  try { return JSON.stringify(data.detail || data); } catch { return "Generation failed"; }
}
