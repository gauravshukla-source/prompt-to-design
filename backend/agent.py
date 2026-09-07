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
    role: Optional[str] = Field(None, description="Semantic architecture role: external_actor, identity_source, identity_provider, primary_component, target_application, traffic_router, peer_service, event_backbone, integration, data_store, cache, security_control, observability")
    peerGroup: Optional[str] = Field(None, description="Name of a peer set that must be rendered together, never sequentially")
    importance: Optional[str] = Field("normal", description="primary, normal, supporting")

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
    type: str = Field(..., description="Type of group boundary: 'vpc', 'subnet', 'securityGroup', 'azureResourceGroup', 'kubernetesCluster', 'generic'")

class DiagramSchema(BaseModel):
    diagramType: str = Field(..., description="Type of diagram: architecture, integration, flowchart")
    pattern: Optional[str] = Field("generic", description="iam, hub_spoke, three_tier, microservices, event_driven, data_pipeline, hybrid_cloud, zero_trust, generic")
    groups: List[Group]
    nodes: List[Node]
    edges: List[Edge]

# Base prompts
SYSTEM_PROMPT = """
You are a principal Enterprise Solutions Architect. Produce clean, publication-quality architecture diagram specifications inspired by AWS Architecture Center, Microsoft Azure Architecture Center, and Google Cloud reference architectures.
The renderer owns coordinates; you own semantic architecture and MUST select the architecture pattern.

ARCHITECTURE PATTERN SELECTION:
- IAM / IGA: identity_source -> identity_provider -> primary_component (IGA hub) -> target_application peers.
- hub_spoke: one central primary component with independent peers around it.
- three_tier: users/edge -> traffic -> application peers -> data peers.
- microservices: entry -> independent peer services -> optional event backbone -> data peers.
- event_driven: producer peers -> event backbone -> consumer peers.
- data_pipeline: source peers -> ingestion -> processing -> storage/analytics.
- hybrid_cloud: on-prem boundary -> connectivity bridge -> cloud boundary.
- zero_trust: user/device -> identity -> security policy -> secure access -> applications.

CRITICAL RULES:
1. Return pattern explicitly in the root object.
2. Assign every node role, layer, importance and category. Use importance=primary only for the architecture hub/backbone.
3. Use peerGroup for services, producers, consumers, target applications, and data stores that must appear as peers. Never make peers sequential unless the prompt explicitly states a dependency.
4. Groups are real boundaries only: cloud/on-prem/SaaS domain, VPC/VNet, resource group, cluster, subnet, namespace, or trust zone. Never create empty groups.
5. Every edge is a real directional interaction source -> target. Do not connect sibling databases or sibling applications merely because they coexist.
6. Edge labels are short: HTTPS, REST/HTTPS, gRPC, AMQP, LDAP, JDBC, OAuth2/OIDC, SCIM, Event.
7. Use kind=auth for authentication/identity, async for events/queues, data for data access, control for governance/control plane, sync otherwise.
8. For IAM/IGA, make the IGA platform primary and visually central; target applications are independent peers.
9. Generate 5-18 nodes. Summarize repeated infrastructure instead of clutter.
10. Use architecture notation (components, boundaries, directional connectors), never a generic flowchart.
11. Use ONLY approved icon slugs or supplied custom icon tags. Never invent slugs.

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
    """Normalize AI output into deterministic Phase 5.2 architecture semantics."""
    valid_icons = {
        "aws-api-gateway","aws-rds","aws-ecs","aws-s3","aws-lambda","aws-ec2","aws-alb","aws-cloudfront",
        "azure-sql","azure-app-service","azure-vm","azure-api-management","azure-active-directory","azure-functions","azure-service-bus",
        "gcp-cloud-run","gcp-gcs","gcp-bigquery","gcp-pubsub","active-directory","okta","ldap","saviynt-iga","microsoft-graph",
        "kafka","rabbitmq","kubernetes","load-balancer","firewall","router","dns","database","server","client","user","cog"
    }
    custom = {i.get("tag") for i in diagram.get("custom_icons", [])}
    text = " ".join(f"{n.get('data',{}).get('label','')} {n.get('data',{}).get('icon','')}" for n in diagram.get("nodes", [])).lower()
    pattern = (diagram.get("pattern") or "generic").lower()
    if pattern == "generic":
        if any(x in text for x in ["saviynt", "identity governance", "iga"]): pattern = "iam"
        elif any(x in text for x in ["kafka", "rabbitmq", "event bus", "pubsub"]): pattern = "event_driven"
        elif any(x in text for x in ["kubernetes", "microservice", "ecs cluster"]): pattern = "microservices"
        elif any(x in text for x in ["data lake", "warehouse", "ingestion", "spark"]): pattern = "data_pipeline"
    diagram["pattern"] = pattern

    def infer_role(label, icon, category):
        t = f"{label} {icon} {category}".lower()
        if any(x in t for x in ["saviynt", "identity governance", " iga"]): return "primary_component"
        if any(x in t for x in ["active directory", "ldap", "identity source"]): return "identity_source"
        if any(x in t for x in ["entra", "okta", "identity provider"]): return "identity_provider"
        if any(x in t for x in ["user", "employee", "admin", "browser", "client"]): return "external_actor"
        if any(x in t for x in ["servicenow", "salesforce", "workday", "aws iam", "target application"]): return "target_application"
        if any(x in t for x in ["kafka", "rabbitmq", "pubsub", "service bus", "event bus"]): return "event_backbone"
        if any(x in t for x in ["rds", "database", "sql", "postgres", "mongo", "dynamodb"]): return "data_store"
        if any(x in t for x in ["redis", "cache", "elasticache"]): return "cache"
        if any(x in t for x in ["alb", "load balancer", "api gateway", "gateway"]): return "traffic_router"
        if any(x in t for x in ["waf", "firewall", "policy", "mfa", "security"]): return "security_control"
        if any(x in t for x in ["monitor", "grafana", "prometheus", "logging"]): return "observability"
        if any(x in t for x in ["integration", "connector", "direct connect", "expressroute"]): return "integration"
        return "peer_service"

    role_layer = {
        "external_actor": 0, "identity_source": 0, "edge_entry": 1, "traffic_router": 1,
        "identity_provider": 1, "security_control": 2, "primary_component": 3,
        "peer_service": 3, "integration": 4, "event_backbone": 4,
        "data_store": 5, "cache": 5, "target_application": 5, "observability": 6
    }
    for n in diagram.get("nodes", []):
        data = n.setdefault("data", {})
        category = (data.get("category") or "general").lower()
        data["category"] = category
        role = data.get("role") or infer_role(data.get("label", ""), data.get("icon", ""), category)
        data["role"] = role
        data["importance"] = "primary" if role in {"primary_component", "event_backbone"} else data.get("importance") or "normal"
        data["layer"] = role_layer.get(role, data.get("layer", 3))
        if role in {"peer_service", "target_application", "data_store", "cache"} and not data.get("peerGroup"):
            data["peerGroup"] = role
        if data.get("icon") not in valid_icons and data.get("icon") not in custom:
            data["icon"] = "server"
        if not data.get("provider"):
            icon = data.get("icon", "")
            data["provider"] = "aws" if icon.startswith("aws-") else "azure" if icon.startswith("azure-") else "gcp" if icon.startswith("gcp-") else "generic"

    seen, cleaned = set(), []
    for e in diagram.get("edges", []):
        key = (e.get("source"), e.get("target"), e.get("label") or e.get("data", {}).get("protocol", ""))
        if not all(key[:2]) or key in seen: continue
        seen.add(key)
        d = e.setdefault("data", {})
        d.setdefault("direction", "forward")
        d.setdefault("kind", "sync")
        protocol = (d.get("protocol") or e.get("label") or "").lower()
        if d["kind"] == "sync":
            if any(x in protocol for x in ["oauth", "oidc", "saml", "ldap", "scim"]): d["kind"] = "auth"
            elif any(x in protocol for x in ["amqp", "event", "kafka", "queue", "topic", "pubsub"]): d["kind"] = "async"
            elif any(x in protocol for x in ["jdbc", "sql"]): d["kind"] = "data"
        if not e.get("label"): e["label"] = d.get("protocol") or ""
        cleaned.append(e)
    diagram["edges"] = cleaned
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
