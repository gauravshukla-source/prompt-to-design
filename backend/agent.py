import os
import json
from typing import List, Optional
from pydantic import BaseModel, Field
from google import genai
from google.genai import types
import google.auth

class NodeProperty(BaseModel):
    key: str
    value: str

class NodeData(BaseModel):
    label: str
    icon: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    properties: Optional[List[NodeProperty]] = None
    layer: Optional[int] = Field(None, ge=0, le=10)
    provider: Optional[str] = None
    role: Optional[str] = Field(None, description="Architecture role: external_actor, edge_entry, traffic_router, primary_component, peer_service, infrastructure_container, integration, event_backbone, identity_provider, security_control, transactional_data, data_store, cache, observability, target_application")
    peerGroup: Optional[str] = Field(None, description="Stable peer group name for services that must render side-by-side")
    importance: Optional[str] = Field("normal", description="primary, normal, or supporting")

class Node(BaseModel):
    id: str
    type: str
    parentId: Optional[str] = None
    data: NodeData

class EdgeData(BaseModel):
    protocol: Optional[str] = None
    encrypted: Optional[bool] = None
    direction: Optional[str] = "forward"
    kind: Optional[str] = "sync"
    importance: Optional[str] = "normal"

class Edge(BaseModel):
    id: str
    source: str
    target: str
    label: Optional[str] = None
    data: Optional[EdgeData] = None

class Group(BaseModel):
    id: str
    label: str
    type: str
    parentId: Optional[str] = None
    role: Optional[str] = None

class DiagramSchema(BaseModel):
    diagramType: str
    pattern: Optional[str] = Field("generic", description="three_tier, microservices, event_driven, iam, hybrid_cloud, zero_trust, data_pipeline, generic")
    groups: List[Group]
    nodes: List[Node]
    edges: List[Edge]

SYSTEM_PROMPT = """
You are a principal Enterprise Solutions Architect. Produce publication-quality architecture specifications inspired by official AWS Architecture Center, Microsoft Azure Architecture Center, and Google Cloud reference architectures. The renderer owns coordinates; you own semantic architecture and containment.

PHASE 5.1 COMPOSITION RULES:
1. First classify pattern as exactly one of: three_tier, microservices, event_driven, iam, hybrid_cloud, zero_trust, data_pipeline, generic.
2. Give every node category, provider, role, importance, and layer. Roles drive visual composition.
3. Build a PRIMARY FLOW spine using only true end-to-end request/identity/event/data flow. Do NOT create edges merely because two components are in the same architecture.
4. Peer services must share peerGroup and layer and must NOT be chained unless the prompt explicitly says service A calls service B.
5. Infrastructure containers (ECS cluster, Kubernetes cluster) are boundaries/groups when they contain workloads; do not collapse all workloads into one generic infrastructure node if named workloads are requested.
6. Containment must be real and hierarchical. Example AWS: AWS Cloud -> VPC -> Public/Private Subnet -> workload/container. Use Group.parentId for nested boundaries.
7. Edge/Internet services may be placed outside the workload boundary when that improves readability. Never force Route 53/CloudFront/WAF into a VPC unless explicitly required.
8. Data peers (RDS, DynamoDB, cache) are peers by default. Connect only from actual consumers to actual data resources.
9. IAM default composition: Actors -> Identity Source/IdP -> Primary IGA/IAM Component -> Target Applications. The IGA/IAM orchestrator is importance=primary.
10. Event composition: Producers -> Event Backbone -> Consumers. Event edges kind=async and dashed.
11. Hybrid composition: On-Prem boundary and Cloud boundary are peers connected through one explicit connectivity bridge.
12. Edge semantics: kind is sync, async, auth, data, control. direction is forward or bidirectional. importance is primary, normal, supporting.
13. Generate 5-24 nodes. Use whitespace and hierarchy instead of decorative boxes. Do not create empty groups.
14. Use ONLY approved icon slugs or supplied custom icon tags. Never invent slugs.

Approved icon slugs:
AWS: aws-api-gateway | aws-rds | aws-ecs | aws-s3 | aws-lambda | aws-ec2 | aws-alb | aws-cloudfront
Azure: azure-sql | azure-app-service | azure-vm | azure-api-management | azure-active-directory | azure-functions | azure-service-bus
GCP: gcp-cloud-run | gcp-gcs | gcp-bigquery | gcp-pubsub
Identity: active-directory | azure-active-directory | okta | ldap | saviynt-iga | microsoft-graph
Messaging: kafka | rabbitmq | azure-service-bus
Infra: kubernetes | load-balancer | firewall | router | dns
Generic: database | server | client | user | cog
Group types: cloud | vpc | subnet | trustZone | onprem | saas | securityGroup | azureResourceGroup | kubernetesCluster | ecsCluster | generic
Return ONLY valid JSON conforming to DiagramSchema. No markdown.
{custom_icons_context}
"""

VALID_ICONS = {
    "aws-api-gateway","aws-rds","aws-ecs","aws-s3","aws-lambda","aws-ec2","aws-alb","aws-cloudfront",
    "azure-sql","azure-app-service","azure-vm","azure-api-management","azure-active-directory","azure-functions","azure-service-bus",
    "gcp-cloud-run","gcp-gcs","gcp-bigquery","gcp-pubsub","active-directory","okta","ldap","saviynt-iga","microsoft-graph",
    "kafka","rabbitmq","kubernetes","load-balancer","firewall","router","dns","database","server","client","user","cog"
}
CATEGORY_LAYER = {"external":0,"user":0,"edge":1,"network":1,"security":1,"identity":1,"compute":2,"application":2,"general":2,"integration":3,"messaging":3,"data":4,"database":4,"storage":4,"observability":5}
ROLE_LAYER = {"external_actor":0,"edge_entry":1,"security_control":1,"identity_provider":1,"traffic_router":2,"primary_component":2,"infrastructure_container":2,"peer_service":3,"integration":3,"event_backbone":3,"transactional_data":4,"data_store":4,"cache":4,"target_application":5,"observability":5}
ROLE_BY_ICON = {"aws-cloudfront":"edge_entry","aws-api-gateway":"edge_entry","dns":"edge_entry","aws-alb":"traffic_router","load-balancer":"traffic_router","saviynt-iga":"primary_component","kafka":"event_backbone","rabbitmq":"event_backbone","aws-rds":"transactional_data","azure-sql":"transactional_data","database":"data_store","active-directory":"identity_provider","azure-active-directory":"identity_provider","okta":"identity_provider"}

def check_auth_status() -> dict:
    project = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GCP_PROJECT_ID", "architecture-diagram-500204")
    location = os.environ.get("GCP_LOCATION", "us-central1")
    model = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
    try:
        creds, resolved = google.auth.default()
        return {"authenticated": True, "auth_mode":"Vertex AI (ADC)", "project":resolved or project, "location":location, "model":model, "message":"Connected via Application Default Credentials (ADC)"}
    except Exception as e:
        return {"authenticated": False, "auth_mode":"Vertex AI (ADC)", "project":project, "location":location, "model":model, "message":f"ADC not detected: {e}"}

def get_gemini_client() -> genai.Client:
    project = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GCP_PROJECT_ID", "architecture-diagram-500204")
    location = os.environ.get("GCP_LOCATION", "us-central1")
    try:
        return genai.Client(vertexai=True, project=project, location=location)
    except Exception as e:
        raise RuntimeError(f"Vertex AI (ADC) initialization failed: {e}. Ensure Cloud Run service account permissions or Application Default Credentials are configured.")

def _generate_with_model_fallback(client, contents, config):
    preferred = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")
    candidates=[]
    for model in [preferred, "gemini-2.5-flash", "gemini-2.5-pro"]:
        if model not in candidates: candidates.append(model)
    last=None
    for model in candidates:
        try:
            return client.models.generate_content(model=model, contents=contents, config=config)
        except Exception as e:
            last=e
            if any(x in str(e).lower() for x in ["404","not_found","not found","unsupported model"]):
                continue
            raise
    raise last

def infer_pattern(prompt: str, diagram: dict) -> str:
    text=(prompt + " " + " ".join(n.get("data",{}).get("label","") + " " + n.get("data",{}).get("icon","") for n in diagram.get("nodes",[]))).lower()
    if any(x in text for x in ["saviynt","iga","iam","identity governance","provisioning","scim"]): return "iam"
    if any(x in text for x in ["kafka","rabbitmq","event-driven","event driven","topic","consumer group"]): return "event_driven"
    if any(x in text for x in ["on-prem","on prem","hybrid cloud","direct connect","expressroute","vpn"]): return "hybrid_cloud"
    if any(x in text for x in ["microservice","kubernetes","ecs service","api gateway"]): return "microservices"
    if any(x in text for x in ["ingestion","warehouse","data lake","etl","analytics pipeline"]): return "data_pipeline"
    if any(x in text for x in ["web tier","application tier","three-tier","3-tier"]): return "three_tier"
    return diagram.get("pattern") or "generic"

def normalize_diagram(diagram: dict, prompt: str = "") -> dict:
    custom={i.get("tag") for i in diagram.get("custom_icons",[])}
    diagram["pattern"] = infer_pattern(prompt, diagram)
    for n in diagram.get("nodes",[]):
        d=n.setdefault("data",{})
        d["category"]=(d.get("category") or "general").lower()
        icon=d.get("icon") or "server"
        if icon not in VALID_ICONS and icon not in custom: icon="server"
        d["icon"]=icon
        role=d.get("role") or ROLE_BY_ICON.get(icon)
        label=d.get("label","").lower()
        if not role:
            if any(x in label for x in ["user","employee","admin","browser"]): role="external_actor"
            elif "service" in label: role="peer_service"
            elif any(x in label for x in ["redis","cache","elasticache"]): role="cache"
            elif any(x in label for x in ["rds","sql","database","dynamodb"]): role="transactional_data"
            else: role="primary_component" if d.get("importance")=="primary" else "peer_service" if d["category"]=="application" else "data_store" if d["category"] in ["data","database","storage"] else "infrastructure_container" if d["category"]=="compute" else "integration"
        d["role"]=role
        d["importance"]=d.get("importance") or ("primary" if role=="primary_component" else "normal")
        d["layer"]=ROLE_LAYER.get(role, CATEGORY_LAYER.get(d["category"],2))
        if role=="peer_service" and not d.get("peerGroup"): d["peerGroup"]="application-services"
        if not d.get("provider"):
            d["provider"]="aws" if icon.startswith("aws-") else "azure" if icon.startswith("azure-") else "gcp" if icon.startswith("gcp-") else "generic"
    ids={n.get("id") for n in diagram.get("nodes",[])}
    seen=set(); edges=[]
    for e in diagram.get("edges",[]):
        if e.get("source") not in ids or e.get("target") not in ids or e.get("source")==e.get("target"): continue
        key=(e.get("source"),e.get("target"),e.get("label") or e.get("data",{}).get("protocol", ""))
        if key in seen: continue
        seen.add(key); d=e.setdefault("data",{})
        d.setdefault("direction","forward"); d.setdefault("kind","sync"); d.setdefault("importance","normal")
        e["label"]=e.get("label") or d.get("protocol") or ""
        edges.append(e)
    diagram["edges"]=edges
    return diagram

def _custom_context(custom_icons):
    if not custom_icons: return ""
    return "\nCustom icon tags:\n"+"\n".join(f"- {i['tag']}: {i.get('description','')}" for i in custom_icons)

def generate_diagram(prompt: str, custom_icons: list=None) -> dict:
    client=get_gemini_client(); context=_custom_context(custom_icons)
    config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT.format(custom_icons_context=context), response_mime_type="application/json", response_schema=DiagramSchema)
    response=_generate_with_model_fallback(client, f"Generate an enterprise architecture for:\n{prompt}", config)
    return normalize_diagram(json.loads(response.text), prompt)

def refine_diagram(prompt: str, current_diagram: dict, custom_icons: list=None) -> dict:
    client=get_gemini_client(); context=_custom_context(custom_icons)
    instruction=f"""Preserve unchanged IDs. Recompose boundaries, roles, peer groups and semantic edges where needed. Current diagram:\n{json.dumps(current_diagram, indent=2)}\nRequested change:\n{prompt}"""
    config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT.format(custom_icons_context=context)+"\n"+instruction, response_mime_type="application/json", response_schema=DiagramSchema)
    response=_generate_with_model_fallback(client, "Apply the requested enterprise architecture modification.", config)
    return normalize_diagram(json.loads(response.text), prompt)
