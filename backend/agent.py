import os
import json
from typing import List, Optional
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
import google.auth


# Pydantic models for Structured Output
class NodeProperty(BaseModel):
    key: str
    value: str

class NodeData(BaseModel):
    label: str
    icon: Optional[str] = Field(None, description="Standard icon slug (e.g., 'aws-api-gateway', 'aws-rds', 'aws-ecs', 'aws-s3', 'aws-lambda', 'azure-sql', 'azure-app-service', 'azure-vm', 'active-directory', 'kubernetes', 'gcp-cloud-run', 'gcp-gcs') or a custom icon tag")
    category: Optional[str] = Field(None, description="e.g., 'compute', 'database', 'network', 'security', 'integration', 'general'")
    description: Optional[str] = Field(None, description="Brief description of node function")
    properties: Optional[List[NodeProperty]] = Field(None, description="Key-value pairs for node properties")
    layer: Optional[int] = Field(None, ge=0, le=10, description="Architecture layer for deterministic layout")
    provider: Optional[str] = Field(None, description="aws, azure, gcp, onprem, saas, generic")
    role: Optional[str] = Field(None, description="Semantic role such as external_actor, identity_source, identity_provider, primary_component, target_application, event_backbone, peer_service")
    peerGroup: Optional[str] = Field(None, description="Name of a peer set that must be laid out as peers, not a sequence")
    importance: Optional[str] = Field("normal", description="primary, normal, or supporting")

class Node(BaseModel):
    id: str
    type: str = Field(..., description="Type of node: 'cloudIcon', 'database', 'group', 'process', 'actor'")
    parentId: Optional[str] = Field(None, description="Parent group ID if nested inside a boundary")
    data: NodeData

class EdgeData(BaseModel):
    protocol: Optional[str] = Field(None, description="Protocol used, e.g., 'HTTPS', 'gRPC', 'AMQP', 'LDAP'")
    encrypted: Optional[bool] = Field(None, description="Whether the connection is encrypted")
    direction: Optional[str] = Field("forward", description="forward, bidirectional, or response")
    kind: Optional[str] = Field("sync", description="sync, async, auth, data, or control")

class Edge(BaseModel):
    id: str
    source: str
    target: str
    label: Optional[str] = Field(None, description="Label for the edge showing integration flow")
    data: Optional[EdgeData] = None

class Group(BaseModel):
    id: str
    label: str
    type: str = Field(..., description="Type of group boundary: 'vpc', 'subnet', 'securityGroup', 'azureResourceGroup', 'kubernetesCluster', 'trustZone', 'generic'")
    parentId: Optional[str] = None
    role: Optional[str] = Field("boundary", description="boundary or trust_zone")

class DiagramSchema(BaseModel):
    diagramType: str = Field(..., description="Type of diagram: 'architecture', 'integration', 'flowchart'")
    pattern: Optional[str] = Field(None, description="iam, event_driven, microservices, data_pipeline, hybrid_cloud, three_tier, zero_trust, or generic")
    groups: List[Group]
    nodes: List[Node]
    edges: List[Edge]

# Base prompts
SYSTEM_PROMPT = """
You are a principal Enterprise Solutions Architect. Produce clean, publication-quality architecture diagram specifications inspired by AWS Architecture Center, Microsoft Azure Architecture Center, and Google Cloud reference architectures.
The renderer owns coordinates; you own semantic architecture.
CRITICAL RULES:
1. First classify the architecture pattern: iam, event_driven, microservices, data_pipeline, hybrid_cloud, three_tier, zero_trust, or generic.
2. Organize semantic architecture into logical layers; the renderer owns final coordinates and may use pattern-specific composition instead of generic left-to-right layout.
3. Assign every node a category, layer, role, peerGroup, and importance. Keep peers in the same peerGroup and never connect peers sequentially unless the prompt explicitly requires it.
4. For IAM/IGA: identity_source -> identity_provider -> primary_component -> target_application. Saviynt is primary_component with importance=primary; Active Directory is identity_source; Entra/Okta is identity_provider; provisioned SaaS/AWS targets are target_application peers.
5. Use groups only for real boundaries: never use groups merely to make a box around every node. A boundary must represent ownership, deployment, trust, network, or organizational scope. cloud/on-prem/SaaS domain, VPC/VNet/resource group, cluster, subnet, or trust zone.
6. Every edge is a real directional interaction source -> target. Prefer adjacent layers and avoid decorative/duplicate edges.
7. Edge labels are short protocol/flow labels only: HTTPS, REST/HTTPS, gRPC, AMQP, LDAP, JDBC, OAuth2/OIDC, Event.
8. Use direction="bidirectional" only for genuine two-way relationships; use kind="async" for queues/topics/events.
9. Generate 5-18 nodes. If the prompt is small, generate fewer rather than inventing infrastructure. If it is large, collapse repeated services into a representative peer group. Summarize repeated infrastructure instead of creating clutter.
10. Use architecture notation (components, boundaries, directional connectors), not a generic flowchart.
11. Use ONLY approved icon slugs or supplied custom icon tags. Never invent slugs.
12. Do not create empty/decorative groups.
Approved icon slugs:
AWS: aws-api-gateway | aws-rds | aws-ecs | aws-s3 | aws-lambda | aws-ec2 | aws-alb | aws-cloudfront
Azure: azure-sql | azure-app-service | azure-vm | azure-api-management | azure-active-directory | azure-functions | azure-service-bus
GCP: gcp-cloud-run | gcp-gcs | gcp-bigquery | gcp-pubsub
Identity: active-directory | azure-active-directory | okta | ldap | saviynt-iga | microsoft-graph
Messaging: kafka | rabbitmq | azure-service-bus
Infra: kubernetes | load-balancer | firewall | router | dns
Generic: database | server | client | user | cog
Group types: vpc | subnet | securityGroup | azureResourceGroup | kubernetesCluster | generic
Return ONLY valid JSON conforming to DiagramSchema. No markdown.
{custom_icons_context}
"""

def check_auth_status() -> dict:
    """
    Checks the status of Application Default Credentials (ADC) and Vertex AI configuration.
    Returns diagnostic details for monitoring and UI badge display.
    """
    gcp_project = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GCP_PROJECT_ID", "architecture-diagram-500204")
    gcp_location = os.environ.get("GCP_LOCATION", "us-central1")
    model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

    try:
        creds, proj = google.auth.default()
        resolved_project = proj or gcp_project
        return {
            "authenticated": True,
            "auth_mode": "Vertex AI (ADC)",
            "project": resolved_project,
            "location": gcp_location,
            "model": model,
            "message": "Connected via Application Default Credentials (ADC)"
        }
    except Exception as e:
        return {
            "authenticated": False,
            "auth_mode": "Vertex AI (ADC)",
            "project": gcp_project,
            "location": gcp_location,
            "model": model,
            "message": f"ADC not detected: {e}"
        }

def get_gemini_client() -> genai.Client:
    """
    Initializes Google GenAI client in Vertex AI mode with Application Default Credentials (ADC).
    Strictly complies with enterprise security policies: zero API keys are accepted or stored.
    """
    gcp_project = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GCP_PROJECT_ID", "architecture-diagram-500204")
    gcp_location = os.environ.get("GCP_LOCATION", "us-central1")

    try:
        # Vertex AI uses ADC (OAuth2) automatically without API keys
        return genai.Client(vertexai=True, project=gcp_project, location=gcp_location)
    except Exception as e:
        raise RuntimeError(
            f"Vertex AI (ADC) initialization failed: {e}. "
            f"Enterprise policy disallows API keys. Please ensure Application Default Credentials (ADC) "
            f"are configured locally via 'gcloud auth application-default login', or that the service account "
            f"is assigned when running on Cloud Run."
        )

def _generate_with_model_fallback(client: genai.Client, contents: str, config: types.GenerateContentConfig):
    """
    Tries the configured model first, and gracefully falls back to other standard
    Vertex AI Gemini models in the region if a 404 NOT_FOUND occurs.
    """
    preferred_model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
    models_to_try = [preferred_model, "gemini-2.5-flash", "gemini-2.5-pro"]
    
    # De-duplicate while preserving priority order
    seen = set()
    candidate_models = [m for m in models_to_try if not (m in seen or seen.add(m))]

    last_error = None
    for candidate in candidate_models:
        try:
            return client.models.generate_content(
                model=candidate,
                contents=contents,
                config=config
            )
        except Exception as err:
            last_error = err
            err_msg = str(err)
            if "404" in err_msg or "NOT_FOUND" in err_msg or "not found" in err_msg:
                continue
            raise err
    raise last_error

def normalize_diagram(diagram: dict) -> dict:
    """Normalize Gemini output into a semantic graph. Coordinates are deliberately not generated here."""
    diagram.setdefault("groups", [])
    diagram.setdefault("nodes", [])
    diagram.setdefault("edges", [])

    icon_aliases = {
        "active directory": "active-directory", "ad": "active-directory", "entra id": "azure-active-directory",
        "azure ad": "azure-active-directory", "azure active directory": "azure-active-directory",
        "saviynt": "saviynt-iga", "api gateway": "aws-api-gateway", "application gateway": "azure-api-management",
        "postgres": "database", "mysql": "database", "oracle": "database", "sql server": "database",
        "sqs": "rabbitmq", "event hub": "azure-service-bus", "event hubs": "azure-service-bus",
        "eks": "kubernetes", "aks": "kubernetes", "gke": "kubernetes",
    }
    valid_icons = {
        "aws-api-gateway","aws-rds","aws-ecs","aws-s3","aws-lambda","aws-ec2","aws-alb","aws-cloudfront",
        "azure-sql","azure-app-service","azure-vm","azure-api-management","azure-active-directory","azure-functions","azure-service-bus",
        "gcp-cloud-run","gcp-gcs","gcp-bigquery","gcp-pubsub","active-directory","okta","ldap","saviynt-iga","microsoft-graph",
        "kafka","rabbitmq","kubernetes","load-balancer","firewall","router","dns","database","server","client","user","cog"
    }
    custom = {str(i.get("tag")) for i in diagram.get("custom_icons", []) if i.get("tag")}

    def all_text(n: dict) -> str:
        d=n.get("data", {})
        return " ".join(str(d.get(k, "")) for k in ("label","description","category","icon","role","provider")).lower()

    corpus=" ".join(all_text(n) for n in diagram["nodes"])
    pattern=str(diagram.get("pattern") or "").lower()
    if pattern in {"", "generic", "unknown"}:
        if any(x in corpus for x in ("saviynt","identity governance","identity lifecycle","active directory","entra id"," okta"," scim"," iam")):
            pattern="iam"
        elif any(x in corpus for x in ("kafka","rabbitmq","pubsub","event bus","event-driven","event driven")):
            pattern="event_driven"
        elif any(x in corpus for x in ("warehouse","etl","ingestion","data pipeline","transform","lakehouse")):
            pattern="data_pipeline"
        elif any(x in corpus for x in ("kubernetes","microservice","service mesh")):
            pattern="microservices"
        elif any(x in corpus for x in ("direct connect","expressroute","on-prem","hybrid cloud","site-to-site vpn")):
            pattern="hybrid_cloud"
        elif any(x in corpus for x in ("load balancer","application gateway","web tier")) and any(x in corpus for x in ("database","rds","sql")):
            pattern="three_tier"
        else:
            pattern="generic"
    diagram["pattern"]=pattern

    def infer_provider(text: str, icon: str) -> str:
        if icon.startswith("aws-") or any(x in text for x in ("aws ","amazon ","rds","ecs","ec2","lambda","cloudfront")): return "aws"
        if icon.startswith("azure-") or any(x in text for x in ("azure ","entra","microsoft")): return "azure"
        if icon.startswith("gcp-") or any(x in text for x in ("google cloud","gcp ","bigquery","cloud run")): return "gcp"
        if any(x in text for x in ("on-prem","on prem","datacenter","data center")): return "onprem"
        if any(x in text for x in ("salesforce","servicenow","workday","saas")): return "saas"
        return "generic"

    def infer_role(text: str, category: str) -> str:
        if any(x in text for x in ("user","employee","customer","administrator","admin","browser","mobile client")): return "external_actor"
        if "saviynt" in text: return "primary_component"
        if any(x in text for x in ("active directory","ldap","identity source","hr source")): return "identity_source"
        if any(x in text for x in ("entra","okta","identity provider","idp")): return "identity_provider"
        if any(x in text for x in ("kafka","rabbitmq","pubsub","service bus","event bus")): return "event_backbone"
        if any(x in text for x in ("api gateway","load balancer","cloudfront","ingress","application gateway")): return "entry_point"
        if any(x in text for x in ("database","rds","sql","warehouse","data lake","storage","s3","gcs")): return "data_store"
        if any(x in text for x in ("queue","topic","event producer")): return "event_producer"
        if any(x in text for x in ("consumer","subscriber")): return "event_consumer"
        if pattern=="iam": return "target_application"
        return "peer_service"

    layer_by_role={"external_actor":0,"identity_source":1,"identity_provider":2,"entry_point":1,"primary_component":3,"event_backbone":2,"data_store":4,"target_application":4,"peer_service":2}
    for n in diagram["nodes"]:
        d=n.setdefault("data", {})
        label=str(d.get("label") or n.get("id") or "Component")
        d["label"]=label
        text=all_text(n)
        icon=str(d.get("icon") or "").strip().lower()
        if icon in icon_aliases: icon=icon_aliases[icon]
        if not icon:
            for needle,slug in icon_aliases.items():
                if needle in text: icon=slug; break
        if icon not in valid_icons and icon not in custom:
            icon="database" if any(x in text for x in ("database","sql","warehouse","storage")) else "server"
        d["icon"]=icon
        category=str(d.get("category") or "general").lower()
        d["category"]=category
        provider=str(d.get("provider") or infer_provider(text,icon)).lower()
        d["provider"]=provider
        role=str(d.get("role") or "").lower()
        inferred=infer_role(text,category)
        if role in {"","peer_service"} or (pattern=="iam" and role not in {"external_actor","identity_source","identity_provider","primary_component","target_application"}): role=inferred
        d["role"]=role
        d["importance"]="primary" if role in {"primary_component","event_backbone"} and (role=="primary_component" or pattern=="event_driven") else str(d.get("importance") or "normal")
        if not d.get("peerGroup"):
            if role=="target_application": d["peerGroup"]="target_applications"
            elif role=="peer_service": d["peerGroup"]="services"
            elif role in {"event_producer","event_consumer"}: d["peerGroup"]=role
            else: d["peerGroup"]=""
        try: d["layer"]=int(d.get("layer"))
        except Exception: d["layer"]=layer_by_role.get(role,2)

    ids={n.get("id") for n in diagram["nodes"]}
    # Remove empty/decorative groups and invalid parents. Keep only explicit deployment/trust boundaries.
    valid_group_types={"vpc","subnet","securityGroup","azureResourceGroup","kubernetesCluster","trustZone","generic"}
    cleaned_groups=[]
    group_ids=set()
    for g in diagram["groups"]:
        gid=str(g.get("id") or "").strip()
        if not gid: continue
        members=[n for n in diagram["nodes"] if n.get("parentId")==gid]
        if not members: continue
        g["type"]=g.get("type") if g.get("type") in valid_group_types else "generic"
        g["role"]=g.get("role") or "boundary"
        cleaned_groups.append(g); group_ids.add(gid)
    for n in diagram["nodes"]:
        if n.get("parentId") not in group_ids: n["parentId"]=None
    diagram["groups"]=cleaned_groups

    seen=set(); cleaned_edges=[]
    for e in diagram["edges"]:
        src,tgt=e.get("source"),e.get("target")
        if src not in ids or tgt not in ids or not src or not tgt or src==tgt: continue
        d=e.setdefault("data", {})
        d["direction"]=d.get("direction") or "forward"
        d["kind"]=d.get("kind") or "sync"
        e["label"]=str(e.get("label") or d.get("protocol") or "").strip()
        key=(src,tgt,e["label"],d["kind"])
        if key in seen: continue
        seen.add(key); cleaned_edges.append(e)
    diagram["edges"]=cleaned_edges
    return diagram

def generate_diagram(prompt: str, custom_icons: list = None) -> dict:
    client = get_gemini_client()

    custom_context_str = ""
    if custom_icons:
        custom_context_str = "\nYou also have access to the following custom-uploaded organization-specific icon tags:\n"
        for icon in custom_icons:
            custom_context_str += f"- Tag: '{icon['tag']}', Description: {icon['description']}\n"
        custom_context_str += "Please map relevant systems in the user prompt to these custom tags if they fit perfectly."

    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT.format(custom_icons_context=custom_context_str),
        response_mime_type="application/json",
        response_schema=DiagramSchema
    )

    response = _generate_with_model_fallback(
        client=client,
        contents=f"Generate a diagram for the following prompt:\n{prompt}",
        config=config
    )

    return normalize_diagram(json.loads(response.text))

def refine_diagram(prompt: str, current_diagram: dict, custom_icons: list = None) -> dict:
    client = get_gemini_client()

    custom_context_str = ""
    if custom_icons:
        custom_context_str = "\nAvailable custom icon tags:\n" + "\n".join([f"- Tag: '{i['tag']}', Desc: {i['description']}" for i in custom_icons])

    refine_instruction = f"""
You are an expert Solutions Architect. You are given a current diagram state (JSON) and a user's instruction to modify it.
Your goal is to apply the requested edits (addition of nodes/edges, removals, grouping, boundary changes) while keeping as much of the existing diagram structure intact as possible.
Do not change IDs of unchanged elements. Only add, remove, or modify elements requested by the user.

Current Diagram State:
{json.dumps(current_diagram, indent=2)}

{custom_context_str}
"""

    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT.format(custom_icons_context=custom_context_str) + refine_instruction,
        response_mime_type="application/json",
        response_schema=DiagramSchema
    )

    response = _generate_with_model_fallback(
        client=client,
        contents=f"Apply the following modifications: {prompt}",
        config=config
    )

    return normalize_diagram(json.loads(response.text))
