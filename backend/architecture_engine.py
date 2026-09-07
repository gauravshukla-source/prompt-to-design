"""Phase 3 architecture intelligence engine.
Deterministic normalization, linting and multi-view projection for AI-generated diagrams.
"""
from __future__ import annotations
from collections import defaultdict, deque
from typing import Any

CATEGORY_LAYER = {
    "external": 0, "user": 0, "client": 0, "saas": 0,
    "edge": 1, "network": 1, "gateway": 1,
    "application": 2, "compute": 2, "service": 2, "general": 2,
    "integration": 3, "messaging": 3,
    "data": 4, "database": 4, "storage": 4,
    "identity": 5, "security": 5, "observability": 6,
}
VALID_KINDS = {"sync", "async", "auth", "data", "control", "observability"}
VALID_DIRECTIONS = {"forward", "bidirectional", "response"}
VALID_PORTS = {"north", "south", "east", "west", "auto"}

DEFAULT_ICONS = {
    "aws-api-gateway","aws-rds","aws-ecs","aws-s3","aws-lambda","aws-ec2","aws-alb","aws-cloudfront",
    "azure-sql","azure-app-service","azure-vm","azure-api-management","azure-active-directory","azure-functions","azure-service-bus",
    "gcp-cloud-run","gcp-gcs","gcp-bigquery","gcp-pubsub","active-directory","okta","ldap","saviynt-iga","microsoft-graph",
    "kafka","rabbitmq","kubernetes","load-balancer","firewall","router","dns","database","server","client","user","cog"
}


def _provider(icon: str) -> str:
    if icon.startswith("aws-"): return "aws"
    if icon.startswith("azure-"): return "azure"
    if icon.startswith("gcp-"): return "gcp"
    return "generic"


def _port_for(source_layer: int, target_layer: int, direction: str, side: str) -> str:
    if direction == "bidirectional": return "east" if side == "source" else "west"
    if target_layer > source_layer: return "east" if side == "source" else "west"
    if target_layer < source_layer: return "west" if side == "source" else "east"
    return "south" if side == "source" else "north"


def normalize_diagram(diagram: dict[str, Any], custom_icons: list[dict[str, Any]] | None = None) -> dict[str, Any]:
    diagram = dict(diagram or {})
    diagram.setdefault("diagramType", "architecture")
    diagram.setdefault("groups", [])
    diagram.setdefault("nodes", [])
    diagram.setdefault("edges", [])
    custom_tags = {i.get("tag") for i in (custom_icons or []) if i.get("tag")}
    valid_icons = DEFAULT_ICONS | custom_tags

    clean_groups, group_ids = [], set()
    for g in diagram["groups"]:
        if not g.get("id") or g.get("id") in group_ids: continue
        group_ids.add(g["id"])
        g.setdefault("type", "generic"); g.setdefault("provider", "generic"); g.setdefault("zone", None)
        clean_groups.append(g)
    diagram["groups"] = clean_groups

    node_ids, layers = set(), {}
    clean_nodes = []
    for n in diagram["nodes"]:
        nid = n.get("id")
        if not nid or nid in node_ids: continue
        node_ids.add(nid)
        data = n.setdefault("data", {})
        category = str(data.get("category") or "general").strip().lower()
        data["category"] = category
        try: layer = int(data.get("layer"))
        except (TypeError, ValueError): layer = CATEGORY_LAYER.get(category, 2)
        data["layer"] = max(0, min(10, layer)); layers[nid] = data["layer"]
        icon = str(data.get("icon") or "server")
        data["icon"] = icon if icon in valid_icons else "server"
        data["provider"] = data.get("provider") or _provider(data["icon"])
        data.setdefault("description", "")
        data.setdefault("properties", [])
        if n.get("parentId") not in group_ids: n["parentId"] = None
        clean_nodes.append(n)
    diagram["nodes"] = clean_nodes

    seen, clean_edges = set(), []
    for e in diagram["edges"]:
        s, t = e.get("source"), e.get("target")
        if not s or not t or s == t or s not in node_ids or t not in node_ids: continue
        data = e.setdefault("data", {}) or {}; e["data"] = data
        protocol = str(data.get("protocol") or e.get("label") or "").strip()
        kind = str(data.get("kind") or "sync").lower(); kind = kind if kind in VALID_KINDS else "sync"
        direction = str(data.get("direction") or "forward").lower(); direction = direction if direction in VALID_DIRECTIONS else "forward"
        src_port = str(data.get("sourcePort") or "auto").lower()
        tgt_port = str(data.get("targetPort") or "auto").lower()
        if src_port not in VALID_PORTS: src_port = "auto"
        if tgt_port not in VALID_PORTS: tgt_port = "auto"
        if src_port == "auto": src_port = _port_for(layers[s], layers[t], direction, "source")
        if tgt_port == "auto": tgt_port = _port_for(layers[s], layers[t], direction, "target")
        data.update({"protocol": protocol, "kind": kind, "direction": direction,
                     "encrypted": bool(data.get("encrypted", False)),
                     "sourcePort": src_port, "targetPort": tgt_port})
        e["label"] = e.get("label") or protocol
        key = (s, t, protocol, kind, direction)
        if key in seen: continue
        seen.add(key); clean_edges.append(e)
    diagram["edges"] = clean_edges
    diagram.setdefault("metadata", {})
    diagram["metadata"]["quality"] = {
        "layout": "phase3-layered-sugiyama", "routing": "orthogonal-port-aware",
        "boundaries": len(clean_groups), "nodes": len(clean_nodes), "edges": len(clean_edges)
    }
    return diagram


def _has_cycle(nodes: list[str], edges: list[dict[str, Any]]) -> bool:
    graph = defaultdict(list); indegree = {n: 0 for n in nodes}
    for e in edges:
        if e["data"].get("kind") == "observability": continue
        graph[e["source"]].append(e["target"]); indegree[e["target"]] += 1
    q = deque([n for n, d in indegree.items() if d == 0]); visited = 0
    while q:
        n = q.popleft(); visited += 1
        for m in graph[n]:
            indegree[m] -= 1
            if indegree[m] == 0: q.append(m)
    return visited != len(nodes)


def lint_architecture(diagram: dict[str, Any]) -> dict[str, Any]:
    nodes = diagram.get("nodes", []); edges = diagram.get("edges", [])
    by_id = {n["id"]: n for n in nodes}; findings = []
    score = 100
    def add(severity: str, code: str, message: str, points: int, ids=None):
        nonlocal score
        findings.append({"severity": severity, "code": code, "message": message, "nodeIds": ids or []})
        score -= points
    if len(nodes) > 20: add("warning", "HIGH_NODE_COUNT", "High node count; consider splitting into multiple views.", 8)
    if _has_cycle(list(by_id), edges): add("warning", "CYCLE", "A dependency cycle was detected in the primary architecture graph.", 7)
    fanout = defaultdict(int); fanin = defaultdict(int)
    for e in edges: fanout[e["source"]] += 1; fanin[e["target"]] += 1
    for nid, count in fanout.items():
        if count > 5: add("warning", "EXCESSIVE_FANOUT", f"{by_id[nid]['data']['label']} has {count} direct outbound connections; consider a gateway or broker.", 5, [nid])
    for n in nodes:
        d = n["data"]; category = d.get("category")
        label = d.get("label", "component")
        if category == "database" and d.get("provider") == "generic" and any(x in label.lower() for x in ["public", "internet"]):
            add("error", "PUBLIC_DATABASE", f"{label} appears exposed in a public context.", 15, [n["id"]])
    for e in edges:
        d = e["data"]; s = by_id[e["source"]]; t = by_id[e["target"]]
        if (d.get("protocol") or "").upper() == "HTTP" and not d.get("encrypted"):
            add("warning", "UNENCRYPTED_HTTP", f"HTTP connection from {s['data']['label']} to {t['data']['label']} is not marked encrypted.", 8, [s["id"], t["id"]])
        if s["data"].get("category") == "external" and t["data"].get("category") in {"database", "data", "storage"}:
            add("error", "EXTERNAL_TO_DATA", "External system connects directly to a data component; introduce an application or API boundary.", 12, [s["id"], t["id"]])
    if not any(n["data"].get("category") == "identity" for n in nodes): add("info", "NO_IDENTITY", "No identity component is modeled; add one when authentication or authorization is in scope.", 0)
    if not any(n["data"].get("category") == "observability" for n in nodes): add("info", "NO_OBSERVABILITY", "No observability component is modeled; add logging/metrics when operational architecture is in scope.", 0)
    return {"score": max(0, score), "grade": "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 60 else "D",
            "summary": {"errors": sum(f["severity"] == "error" for f in findings), "warnings": sum(f["severity"] == "warning" for f in findings), "info": sum(f["severity"] == "info" for f in findings)}, "findings": findings}


def project_view(diagram: dict[str, Any], view: str) -> dict[str, Any]:
    view = (view or "logical").lower()
    result = {k: diagram.get(k, []) for k in ("groups", "nodes", "edges")}
    if view == "context":
        keep = {n["id"] for n in result["nodes"] if n["data"].get("category") in {"external", "user", "client", "edge", "application", "compute", "saas"}}
    elif view == "security":
        keep = {n["id"] for n in result["nodes"] if n["data"].get("category") in {"external", "user", "edge", "security", "identity", "application", "compute", "data", "database"}}
    elif view == "data-flow":
        keep = {n["id"] for n in result["nodes"] if n["data"].get("category") not in {"observability", "identity"}}
    elif view == "integration":
        keep = {n["id"] for n in result["nodes"] if n["data"].get("category") in {"external", "saas", "application", "compute", "integration", "messaging", "identity"}}
    else: keep = {n["id"] for n in result["nodes"]}
    result["nodes"] = [n for n in result["nodes"] if n["id"] in keep]
    result["edges"] = [e for e in result["edges"] if e["source"] in keep and e["target"] in keep]
    parents = {n.get("parentId") for n in result["nodes"] if n.get("parentId")}
    result["groups"] = [g for g in result["groups"] if g["id"] in parents]
    result["diagramType"] = view
    result["metadata"] = {"view": view, "generatedBy": "phase3-architecture-engine"}
    return result
