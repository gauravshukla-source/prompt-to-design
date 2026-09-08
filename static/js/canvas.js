export function renderGraph(graph) {
  const canvas = document.getElementById("canvas");
  canvas.innerHTML = "";

  const root = document.createElement("div");
  root.className = "graph";

  const nodeMap = new Map();
  for (const node of graph.nodes) {
    nodeMap.set(node.data.id, node);
    const el = document.createElement("div");
    el.className = "node";
    el.dataset.id = node.data.id;
    el.innerHTML = `
      <strong>${escapeHtml(node.data.label)}</strong>
      <div>${escapeHtml(node.data.type)}</div>
      <small>${escapeHtml(node.data.domain_id || "No domain")}</small>
    `;
    root.appendChild(el);
  }

  for (const edge of graph.edges) {
    const el = document.createElement("div");
    el.className = "edge";
    el.textContent = `${edge.data.source} → ${edge.data.target}${edge.data.label ? ` (${edge.data.label})` : ""}`;
    root.appendChild(el);
  }

  canvas.appendChild(root);
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}
