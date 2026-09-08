const NS = "http://www.w3.org/2000/svg";

const TYPE_STYLE = {
  user: { accent: "#4f8cff", icon: "👤" }, application: { accent: "#3b82f6", icon: "▣" },
  api: { accent: "#f59e0b", icon: "⇄" }, api_gateway: { accent: "#8b5cf6", icon: "◇" },
  database: { accent: "#10b981", icon: "▤" }, vpn: { accent: "#06b6d4", icon: "⌁" },
  connectivity: { accent: "#06b6d4", icon: "⌁" }, identity_source: { accent: "#0ea5e9", icon: "◎" },
  identity_provider: { accent: "#2563eb", icon: "◎" }, iga: { accent: "#2563eb", icon: "◉" },
  pam: { accent: "#ef4444", icon: "◆" }, target_system: { accent: "#64748b", icon: "▦" },
  service: { accent: "#f97316", icon: "◈" }, message_broker: { accent: "#a855f7", icon: "↔" },
  load_balancer: { accent: "#ec4899", icon: "⇆" }, compute: { accent: "#f97316", icon: "▣" },
  storage: { accent: "#14b8a6", icon: "▤" }, security: { accent: "#ef4444", icon: "◇" }, generic: { accent: "#64748b", icon: "◆" },
};

const EDGE_COLORS = {
  authentication: "#38bdf8", authorization: "#818cf8", provisioning: "#f59e0b", sync: "#14b8a6",
  async: "#a855f7", event: "#a855f7", data_access: "#10b981", network: "#06b6d4", api: "#60a5fa", generic: "#64748b",
};

export function renderGraph(graph) {
  const canvas = document.getElementById("canvas");
  if (!canvas) throw new Error("Canvas element was not found.");
  canvas.replaceChildren();
  const nodes = Array.isArray(graph?.nodes) ? graph.nodes : [];
  const edges = Array.isArray(graph?.edges) ? graph.edges : [];
  const groups = Array.isArray(graph?.groups) ? graph.groups : [];
  if (!nodes.length) { canvas.appendChild(emptyState("No architecture nodes were generated.")); return; }

  const layout = buildLayout(nodes, edges, groups, graph?.constraints || {});
  const svg = svgEl("svg", { class: "architecture-svg", viewBox: `0 0 ${layout.width} ${layout.height}`, role: "img", "aria-label": "Generated enterprise architecture diagram" });
  const defs = svgEl("defs");
  defs.appendChild(marker("arrow-default", "#64748b"));
  Object.entries(EDGE_COLORS).forEach(([type, color]) => defs.appendChild(marker(`arrow-${type}`, color)));
  svg.appendChild(defs);
  const groupLayer = svgEl("g", { class: "domain-layer" }); layout.groupBoxes.forEach(box => drawGroup(groupLayer, box)); svg.appendChild(groupLayer);
  const edgeLayer = svgEl("g", { class: "edge-layer" }); edges.forEach(edge => drawEdge(edgeLayer, edge.data || edge, layout.positions)); svg.appendChild(edgeLayer);
  const nodeLayer = svgEl("g", { class: "node-layer" }); layout.orderedNodes.forEach(node => drawNode(nodeLayer, node.data || node, layout.positions.get((node.data || node).id))); svg.appendChild(nodeLayer);
  canvas.appendChild(svg);
}

function buildLayout(nodes, edges, groups, constraints) {
  const nodeData = nodes.map(n => n.data || n);
  const edgeData = edges.map(e => e.data || e).filter(e => e.source && e.target);
  const strategy = constraints.layout_strategy || "linear_horizontal";
  const composition = constraints.composition || {};
  const viewport = composition?.metadata?.viewport || {};
  const topology = composition?.metadata?.topology || {};
  const nodeWidth = 190, nodeHeight = 92, margin = Number(viewport.padding || 64);
  const gapX = strategy.includes("compact") ? 100 : 135;
  const gapY = strategy.includes("branching") ? 95 : 70;
  const positions = new Map();
  let orderedNodes = [];

  if (strategy === "branching_vertical") {
    placeVertical(nodeData, edgeData, positions, margin, nodeWidth, nodeHeight, gapX, gapY);
  } else {
    // All enterprise horizontal strategies share a rank-based left-to-right flow.
    // This deliberately avoids the old sparse top-to-bottom composition.
    placeHorizontal(nodeData, edgeData, positions, margin, nodeWidth, nodeHeight, gapX, gapY, strategy, topology);
  }
  orderedNodes = [...nodeData].sort((a, b) => {
    const pa = positions.get(a.id), pb = positions.get(b.id);
    return (pa.x - pb.x) || (pa.y - pb.y) || String(a.label).localeCompare(String(b.label));
  });

  const groupBoxes = buildGroupBoxes(groups, nodeData, positions);
  const bounds = calculateBounds(positions, margin);
  const groupMaxX = Math.max(0, ...groupBoxes.map(g => g.x + g.width));
  const groupMaxY = Math.max(0, ...groupBoxes.map(g => g.y + g.height));
  const width = Math.max(Number(viewport.min_width || 0), bounds.width + margin, groupMaxX + margin, 760);
  const height = Math.max(Number(viewport.min_height || 0), bounds.height + margin, groupMaxY + margin, 420);
  return { positions, orderedNodes, groupBoxes, width, height };
}

function placeHorizontal(nodes, edges, positions, margin, w, h, gapX, gapY, strategy, topology) {
  const ranks = computeRanks(nodes, edges);
  const buckets = bucketByRank(nodes, ranks);
  const orderedRanks = [...buckets.keys()].sort((a,b)=>a-b);
  const widest = Math.max(1, ...[...buckets.values()].map(b=>b.length));
  orderedRanks.forEach((rank, rankIndex) => {
    const bucket = orderBucket(buckets.get(rank), nodes, edges);
    const totalHeight = bucket.length * h + Math.max(0, bucket.length - 1) * gapY;
    const centerOffset = Math.max(0, (widest * h + (widest - 1) * gapY - totalHeight) / 2);
    bucket.forEach((node, i) => positions.set(node.id, { x: margin + rankIndex * (w + gapX), y: margin + centerOffset + i * (h + gapY), width:w, height:h, rank:rankIndex }));
  });

  // Domain strategy: keep independent domain members together without creating huge bands.
  if (strategy === "domain_horizontal" && topology.domain_count > 1) {
    compactDomainColumns(nodes, positions, edges, margin, w, h, gapX, gapY);
  }
}

function compactDomainColumns(nodes, positions, edges, margin, w, h, gapX, gapY) {
  const domains = [...new Set(nodes.map(n => n.domain_id || "__none__"))];
  if (domains.length <= 1) return;
  const domainOrder = orderDomains(nodes, edges, domains);
  let x = margin;
  domainOrder.forEach(domainId => {
    const members = nodes.filter(n => (n.domain_id || "__none__") === domainId).sort((a,b)=>{
      const pa=positions.get(a.id), pb=positions.get(b.id); return pa.y-pb.y || String(a.label).localeCompare(String(b.label));
    });
    members.forEach((node, i) => positions.set(node.id, { ...positions.get(node.id), x, y: margin + i * (h + gapY) }));
    x += w + gapX;
  });
}

function orderDomains(nodes, edges, domains) {
  const index = new Map(domains.map((d,i)=>[d,i]));
  const score = new Map(domains.map(d=>[d,0]));
  const byId = new Map(nodes.map(n=>[n.id,n]));
  edges.forEach(e=>{
    const s=byId.get(e.source), t=byId.get(e.target); if (!s || !t) return;
    const sd=s.domain_id||"__none__", td=t.domain_id||"__none__";
    if (sd!==td) score.set(td,(score.get(td)||0)+1);
  });
  return [...domains].sort((a,b)=>(score.get(a)-score.get(b)) || (index.get(a)-index.get(b)));
}

function placeVertical(nodes, edges, positions, margin, w, h, gapX, gapY) {
  const ranks = computeRanks(nodes, edges); const buckets = bucketByRank(nodes, ranks);
  const orderedRanks = [...buckets.keys()].sort((a,b)=>a-b);
  const widest = Math.max(1,...[...buckets.values()].map(b=>b.length));
  orderedRanks.forEach((rank, rankIndex)=>{
    const bucket = orderBucket(buckets.get(rank), nodes, edges);
    const totalWidth=bucket.length*w+Math.max(0,bucket.length-1)*gapX;
    const offset=Math.max(0,(widest*w+(widest-1)*gapX-totalWidth)/2);
    bucket.forEach((node,i)=>positions.set(node.id,{x:margin+offset+i*(w+gapX),y:margin+rankIndex*(h+gapY+80),width:w,height:h,rank:rankIndex}));
  });
}

function bucketByRank(nodes, ranks) { const buckets=new Map(); nodes.forEach(n=>{const r=ranks.get(n.id)||0;if(!buckets.has(r))buckets.set(r,[]);buckets.get(r).push(n);}); return buckets; }
function orderBucket(bucket, nodes, edges) {
  const degree=new Map(nodes.map(n=>[n.id,0])); edges.forEach(e=>{degree.set(e.source,(degree.get(e.source)||0)+1);degree.set(e.target,(degree.get(e.target)||0)+1);});
  return [...bucket].sort((a,b)=>(degree.get(b.id)-degree.get(a.id)) || String(a.label||a.id).localeCompare(String(b.label||b.id)));
}

function computeRanks(nodes, edges) {
  const ids=new Set(nodes.map(n=>n.id)), incoming=new Map(nodes.map(n=>[n.id,0])), outgoing=new Map(nodes.map(n=>[n.id,[]]));
  edges.forEach(e=>{if(!ids.has(e.source)||!ids.has(e.target)||e.source===e.target)return;incoming.set(e.target,(incoming.get(e.target)||0)+1);outgoing.get(e.source).push(e.target);});
  const queue=nodes.filter(n=>incoming.get(n.id)===0).map(n=>n.id), rank=new Map(queue.map(id=>[id,0])), visited=new Set();
  while(queue.length){const id=queue.shift();visited.add(id);const current=rank.get(id)||0;(outgoing.get(id)||[]).forEach(target=>{rank.set(target,Math.max(rank.get(target)||0,current+1));incoming.set(target,incoming.get(target)-1);if(incoming.get(target)===0)queue.push(target);});}
  let fallback=Math.max(...rank.values(),-1)+1;nodes.forEach((n,i)=>{if(!rank.has(n.id))rank.set(n.id,fallback+i);});return rank;
}

function calculateBounds(positions, margin) { let maxX=margin,maxY=margin;positions.forEach(p=>{maxX=Math.max(maxX,p.x+p.width);maxY=Math.max(maxY,p.y+p.height);});return {width:maxX,height:maxY}; }
function buildGroupBoxes(groups,nodes,positions) { const map=new Map(groups.map(g=>[g.id,g]));return [...map.values()].flatMap(group=>{const members=nodes.filter(n=>n.domain_id===group.id&&positions.has(n.id));if(!members.length)return [];const points=members.map(n=>positions.get(n.id)),pad=28,minX=Math.min(...points.map(p=>p.x))-pad,minY=Math.min(...points.map(p=>p.y))-44,maxX=Math.max(...points.map(p=>p.x+p.width))+pad,maxY=Math.max(...points.map(p=>p.y+p.height))+pad;return [{id:group.id,label:group.label||group.id,type:group.type,x:minX,y:minY,width:maxX-minX,height:maxY-minY}];}); }
function drawGroup(layer,box){layer.appendChild(svgEl("rect",{x:box.x,y:box.y,width:box.width,height:box.height,rx:14,class:"domain-box"}));layer.appendChild(textEl(box.label,box.x+16,box.y+24,"domain-label"));}
function drawEdge(layer,edge,positions){const source=positions.get(edge.source),target=positions.get(edge.target);if(!source||!target)return;const dx=target.x-source.x,dy=target.y-source.y;let sx,sy,tx,ty,d;if(Math.abs(dx)>=Math.abs(dy)){sx=source.x+(dx>=0?source.width:0);sy=source.y+source.height/2;tx=target.x+(dx>=0?0:target.width);ty=target.y+target.height/2;const mx=(sx+tx)/2;d=`M ${sx} ${sy} C ${mx} ${sy}, ${mx} ${ty}, ${tx} ${ty}`;}else{sx=source.x+source.width/2;sy=source.y+(dy>=0?source.height:0);tx=target.x+target.width/2;ty=target.y+(dy>=0?0:target.height);const my=(sy+ty)/2;d=`M ${sx} ${sy} C ${sx} ${my}, ${tx} ${my}, ${tx} ${ty}`;}const type=edge.type||"generic",color=EDGE_COLORS[type]||EDGE_COLORS.generic;layer.appendChild(svgEl("path",{d,fill:"none",stroke:color,"stroke-width":2,"marker-end":`url(#arrow-${EDGE_COLORS[type]?type:"default"})`,class:`edge-path edge-${type}`}));if(edge.label){const lx=(sx+tx)/2,ly=(sy+ty)/2-8,label=textEl(edge.label,lx,ly,"edge-label","middle"),width=Math.max(42,String(edge.label).length*6.5+14);layer.appendChild(svgEl("rect",{x:lx-width/2,y:ly-13,width,height:19,rx:4,class:"edge-label-bg"}));layer.appendChild(label);}}
function drawNode(layer,node,position){if(!position)return;const style=TYPE_STYLE[node.type]||TYPE_STYLE.generic,group=svgEl("g",{class:"architecture-node",transform:`translate(${position.x} ${position.y})`});group.appendChild(svgEl("rect",{width:position.width,height:position.height,rx:12,class:"node-card",stroke:style.accent}));group.appendChild(svgEl("rect",{x:14,y:17,width:40,height:40,rx:10,fill:style.accent,opacity:.18}));group.appendChild(textEl(style.icon,34,44,"node-glyph","middle"));const lines=wrapText(node.label||node.id,18,116,2);lines.forEach((line,i)=>group.appendChild(textEl(line,66,35+i*18,"node-title")));group.appendChild(textEl(formatType(node.type),66,72,"node-type"));layer.appendChild(group);}
function marker(id,color){const m=svgEl("marker",{id,markerWidth:8,markerHeight:8,refX:7,refY:4,orient:"auto",markerUnits:"strokeWidth"});m.appendChild(svgEl("path",{d:"M 0 0 L 8 4 L 0 8 z",fill:color}));return m;}
function svgEl(name,attrs={}){const el=document.createElementNS(NS,name);Object.entries(attrs).forEach(([k,v])=>el.setAttribute(k,String(v)));return el;}
function textEl(value,x,y,className,anchor="start"){const el=svgEl("text",{x,y,class:className,"text-anchor":anchor});el.textContent=String(value);return el;}
function wrapText(value,maxChars,maxWidth,maxLines){const words=String(value).split(/\s+/).filter(Boolean),lines=[];let current="";words.forEach(word=>{const next=current?`${current} ${word}`:word;if(next.length<=maxChars||!current)current=next;else{lines.push(current);current=word;}});if(current)lines.push(current);if(lines.length>maxLines){lines.length=maxLines;lines[maxLines-1]=`${lines[maxLines-1].slice(0,Math.max(1,maxChars-1))}…`;}return lines;}
function formatType(type){return String(type||"generic").replaceAll("_"," ").replace(/\b\w/g,c=>c.toUpperCase());}
function emptyState(message){const el=document.createElement("div");el.className="empty-state";el.textContent=message;return el;}
