const NS = "http://www.w3.org/2000/svg";

const TYPE_STYLE = {
  user: { accent: "#4f8cff", icon: "👤" },
  application: { accent: "#3b82f6", icon: "▣" },
  api: { accent: "#f59e0b", icon: "⇄" },
  api_gateway: { accent: "#8b5cf6", icon: "◇" },
  database: { accent: "#10b981", icon: "▤" },
  vpn: { accent: "#06b6d4", icon: "⌁" },
  connectivity: { accent: "#06b6d4", icon: "⌁" },
  identity_source: { accent: "#0ea5e9", icon: "◎" },
  identity_provider: { accent: "#2563eb", icon: "◎" },
  iga: { accent: "#2563eb", icon: "◉" },
  pam: { accent: "#ef4444", icon: "◆" },
  target_system: { accent: "#64748b", icon: "▦" },
  service: { accent: "#f97316", icon: "◈" },
  message_broker: { accent: "#a855f7", icon: "↔" },
  load_balancer: { accent: "#ec4899", icon: "⇆" },
  compute: { accent: "#f97316", icon: "▣" },
  storage: { accent: "#14b8a6", icon: "▤" },
  security: { accent: "#ef4444", icon: "◇" },
  generic: { accent: "#64748b", icon: "◆" },
};

const EDGE_COLORS = {
  authentication: "#38bdf8",
  authorization: "#818cf8",
  provisioning: "#f59e0b",
  sync: "#14b8a6",
  async: "#a855f7",
  event: "#a855f7",
  data_access: "#10b981",
  network: "#06b6d4",
  api: "#60a5fa",
  generic: "#64748b",
};

export function renderGraph(graph) {
  const canvas = document.getElementById("canvas");
  if (!canvas) throw new Error("Canvas element was not found.");
  canvas.replaceChildren();

  const nodes = Array.isArray(graph?.nodes) ? graph.nodes : [];
  const edges = Array.isArray(graph?.edges) ? graph.edges : [];
  const groups = Array.isArray(graph?.groups) ? graph.groups : [];

  if (!nodes.length) {
    canvas.appendChild(emptyState("No architecture nodes were generated."));
    return;
  }

  const layout = buildLayout(nodes, edges, groups, graph?.constraints || {});
  const svg = svgEl("svg", {
    class: "architecture-svg",
    viewBox: `0 0 ${layout.width} ${layout.height}`,
    width: layout.width,
    height: layout.height,
    role: "img",
    "aria-label": "Generated enterprise architecture diagram",
  });

  const defs = svgEl("defs");
  defs.appendChild(marker("arrow-default", "#64748b"));
  Object.entries(EDGE_COLORS).forEach(([type, color]) => defs.appendChild(marker(`arrow-${type}`, color)));
  svg.appendChild(defs);

  const groupLayer = svgEl("g", { class: "domain-layer" });
  layout.groupBoxes.forEach((box) => drawGroup(groupLayer, box));
  svg.appendChild(groupLayer);

  const edgeLayer = svgEl("g", { class: "edge-layer" });
  edges.forEach((edge) => drawEdge(edgeLayer, edge.data || edge, layout.positions));
  svg.appendChild(edgeLayer);

  const nodeLayer = svgEl("g", { class: "node-layer" });
  layout.orderedNodes.forEach((node) => drawNode(nodeLayer, node.data || node, layout.positions.get((node.data || node).id)));
  svg.appendChild(nodeLayer);

  canvas.appendChild(svg);
}

function buildLayout(nodes, edges, groups, constraints) {
  const nodeData = nodes.map((n) => n.data || n);
  const edgeData = edges.map((e) => e.data || e).filter((e) => e.source && e.target);
  const horizontal = constraints.layout_strategy === "layered_horizontal" || constraints.layout_strategy === "domain_horizontal";
  const nodeWidth = 190;
  const nodeHeight = 92;
  const primaryGap = 150;
  const secondaryGap = 85;
  const margin = 80;

  const ranks = computeRanks(nodeData, edgeData);
  const rankBuckets = new Map();
  nodeData.forEach((node, index) => {
    const rank = ranks.get(node.id) ?? index;
    if (!rankBuckets.has(rank)) rankBuckets.set(rank, []);
    rankBuckets.get(rank).push(node);
  });

  const orderedRanks = [...rankBuckets.keys()].sort((a, b) => a - b);
  const positions = new Map();
  const orderedNodes = [];

  orderedRanks.forEach((rank, rankIndex) => {
    const bucket = rankBuckets.get(rank);
    bucket.sort((a, b) => String(a.label || a.id).localeCompare(String(b.label || b.id)));
    bucket.forEach((node, index) => {
      let x, y;
      if (horizontal) {
        x = margin + rankIndex * (nodeWidth + primaryGap);
        y = margin + index * (nodeHeight + secondaryGap);
      } else {
        x = margin + index * (nodeWidth + secondaryGap);
        y = margin + rankIndex * (nodeHeight + primaryGap);
      }
      positions.set(node.id, { x, y, width: nodeWidth, height: nodeHeight, rank: rankIndex });
      orderedNodes.push(node);
    });
  });

  // Center smaller layers against the widest layer for a professional layered layout.
  const maxSecondary = Math.max(...[...rankBuckets.values()].map((b) => b.length), 1);
  orderedRanks.forEach((rank) => {
    const bucket = rankBuckets.get(rank);
    const offset = ((maxSecondary - bucket.length) * (horizontal ? nodeHeight + secondaryGap : nodeWidth + secondaryGap)) / 2;
    bucket.forEach((node) => {
      const p = positions.get(node.id);
      if (horizontal) p.y += offset;
      else p.x += offset;
    });
  });

  const bounds = calculateBounds(positions, margin);
  const groupBoxes = buildGroupBoxes(groups, nodeData, positions);
  const width = Math.max(bounds.width + margin, ...groupBoxes.map((g) => g.x + g.width + margin), 700);
  const height = Math.max(bounds.height + margin, ...groupBoxes.map((g) => g.y + g.height + margin), 520);

  return { positions, orderedNodes, groupBoxes, width, height };
}

function computeRanks(nodes, edges) {
  const ids = new Set(nodes.map((n) => n.id));
  const incoming = new Map(nodes.map((n) => [n.id, 0]));
  const outgoing = new Map(nodes.map((n) => [n.id, []]));

  edges.forEach((edge) => {
    if (!ids.has(edge.source) || !ids.has(edge.target) || edge.source === edge.target) return;
    incoming.set(edge.target, (incoming.get(edge.target) || 0) + 1);
    outgoing.get(edge.source).push(edge.target);
  });

  const queue = nodes.filter((n) => incoming.get(n.id) === 0).map((n) => n.id);
  const rank = new Map(queue.map((id) => [id, 0]));
  const visited = new Set();

  while (queue.length) {
    const id = queue.shift();
    visited.add(id);
    const currentRank = rank.get(id) || 0;
    (outgoing.get(id) || []).forEach((target) => {
      rank.set(target, Math.max(rank.get(target) || 0, currentRank + 1));
      incoming.set(target, incoming.get(target) - 1);
      if (incoming.get(target) === 0) queue.push(target);
    });
  }

  // Cycles and disconnected components still receive stable positions.
  let fallbackRank = Math.max(...rank.values(), -1) + 1;
  nodes.forEach((node) => {
    if (!visited.has(node.id) && !rank.has(node.id)) rank.set(node.id, fallbackRank++);
  });
  nodes.forEach((node, index) => {
    if (!rank.has(node.id)) rank.set(node.id, index);
  });
  return rank;
}

function calculateBounds(positions, margin) {
  let maxX = margin;
  let maxY = margin;
  positions.forEach((p) => {
    maxX = Math.max(maxX, p.x + p.width);
    maxY = Math.max(maxY, p.y + p.height);
  });
  return { width: maxX, height: maxY };
}

function buildGroupBoxes(groups, nodes, positions) {
  const groupMap = new Map(groups.map((g) => [g.id, g]));
  return [...groupMap.values()].flatMap((group) => {
    const members = nodes.filter((node) => node.domain_id === group.id && positions.has(node.id));
    if (!members.length) return [];
    const points = members.map((node) => positions.get(node.id));
    const pad = 34;
    const minX = Math.min(...points.map((p) => p.x)) - pad;
    const minY = Math.min(...points.map((p) => p.y)) - 42;
    const maxX = Math.max(...points.map((p) => p.x + p.width)) + pad;
    const maxY = Math.max(...points.map((p) => p.y + p.height)) + pad;
    return [{ id: group.id, label: group.label || group.id, type: group.type, x: minX, y: minY, width: maxX - minX, height: maxY - minY }];
  });
}

function drawGroup(layer, box) {
  layer.appendChild(svgEl("rect", { x: box.x, y: box.y, width: box.width, height: box.height, rx: 14, class: "domain-box" }));
  layer.appendChild(textEl(box.label, box.x + 18, box.y + 24, "domain-label"));
}

function drawEdge(layer, edge, positions) {
  const source = positions.get(edge.source);
  const target = positions.get(edge.target);
  if (!source || !target) return;

  const dx = target.x - source.x;
  const dy = target.y - source.y;
  let sx, sy, tx, ty, d;
  if (Math.abs(dx) >= Math.abs(dy)) {
    sx = source.x + (dx >= 0 ? source.width : 0);
    sy = source.y + source.height / 2;
    tx = target.x + (dx >= 0 ? 0 : target.width);
    ty = target.y + target.height / 2;
    const midX = (sx + tx) / 2;
    d = `M ${sx} ${sy} C ${midX} ${sy}, ${midX} ${ty}, ${tx} ${ty}`;
  } else {
    sx = source.x + source.width / 2;
    sy = source.y + (dy >= 0 ? source.height : 0);
    tx = target.x + target.width / 2;
    ty = target.y + (dy >= 0 ? 0 : target.height);
    const midY = (sy + ty) / 2;
    d = `M ${sx} ${sy} C ${sx} ${midY}, ${tx} ${midY}, ${tx} ${ty}`;
  }

  const type = edge.type || "generic";
  const color = EDGE_COLORS[type] || EDGE_COLORS.generic;
  layer.appendChild(svgEl("path", {
    d,
    fill: "none",
    stroke: color,
    "stroke-width": 2,
    "marker-end": `url(#arrow-${EDGE_COLORS[type] ? type : "default"})`,
    class: `edge-path edge-${type}`,
  }));

  if (edge.label) {
    const labelX = (sx + tx) / 2;
    const labelY = (sy + ty) / 2 - 8;
    const label = textEl(edge.label, labelX, labelY, "edge-label", "middle");
    const width = Math.max(42, String(edge.label).length * 6.5 + 14);
    const bg = svgEl("rect", { x: labelX - width / 2, y: labelY - 13, width, height: 19, rx: 4, class: "edge-label-bg" });
    layer.appendChild(bg);
    layer.appendChild(label);
  }
}

function drawNode(layer, node, position) {
  if (!position) return;
  const style = TYPE_STYLE[node.type] || TYPE_STYLE.generic;
  const group = svgEl("g", { class: "architecture-node", transform: `translate(${position.x} ${position.y})` });
  group.appendChild(svgEl("rect", { width: position.width, height: position.height, rx: 12, class: "node-card", stroke: style.accent }));
  group.appendChild(svgEl("rect", { x: 14, y: 17, width: 40, height: 40, rx: 10, fill: style.accent, opacity: 0.18 }));
  group.appendChild(textEl(style.icon, 34, 44, "node-glyph", "middle"));

  const labelLines = wrapText(node.label || node.id, 18, 116, 2);
  labelLines.forEach((line, index) => group.appendChild(textEl(line, 66, 35 + index * 18, "node-title")));
  group.appendChild(textEl(formatType(node.type), 66, 72, "node-type"));
  layer.appendChild(group);
}

function marker(id, color) {
  const m = svgEl("marker", { id, markerWidth: 8, markerHeight: 8, refX: 7, refY: 4, orient: "auto", markerUnits: "strokeWidth" });
  m.appendChild(svgEl("path", { d: "M 0 0 L 8 4 L 0 8 z", fill: color }));
  return m;
}

function svgEl(name, attrs = {}) {
  const el = document.createElementNS(NS, name);
  Object.entries(attrs).forEach(([key, value]) => el.setAttribute(key, String(value)));
  return el;
}

function textEl(value, x, y, className, anchor = "start") {
  const el = svgEl("text", { x, y, class: className, "text-anchor": anchor });
  el.textContent = String(value);
  return el;
}

function wrapText(value, maxChars, maxWidth, maxLines) {
  const words = String(value).split(/\s+/).filter(Boolean);
  const lines = [];
  let current = "";
  words.forEach((word) => {
    const next = current ? `${current} ${word}` : word;
    if (next.length <= maxChars || !current) current = next;
    else {
      lines.push(current);
      current = word;
    }
  });
  if (current) lines.push(current);
  if (lines.length > maxLines) {
    lines.length = maxLines;
    lines[maxLines - 1] = `${lines[maxLines - 1].slice(0, Math.max(1, maxChars - 1))}…`;
  }
  return lines;
}

function formatType(type) {
  return String(type || "generic").replaceAll("_", " ").replace(/\b\w/g, (c) => c.toUpperCase());
}

function emptyState(message) {
  const el = document.createElement("div");
  el.className = "empty-state";
  el.textContent = message;
  return el;
}
