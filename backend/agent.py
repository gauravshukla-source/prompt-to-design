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
5. Use groups only for real boundaries: cloud/on-prem/SaaS domain, VPC/VNet/resource group, cluster, subnet, or trust zone.
6. Every edge is a real directional interaction source -> target. Prefer adjacent layers and avoid decorative/duplicate edges.
7. Edge labels are short protocol/flow labels only: HTTPS, REST/HTTPS, gRPC, AMQP, LDAP, JDBC, OAuth2/OIDC, Event.
8. Use direction="bidirectional" only for genuine two-way relationships; use kind="async" for queues/topics/events.
9. Generate 5-18 nodes. Summarize repeated infrastructure instead of creating clutter.
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
    models_to_try = [preferred_model, "gemini-1.5-flash", "gemini-2.5-flash", "gemini-1.5-pro"]
    
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
    """Apply deterministic architecture semantics so rendering does not depend on model layout quality."""
    category_layer = {
        "external": 0, "user": 0, "edge": 1, "network": 1,
        "compute": 2, "application": 2, "general": 2,
        "integration": 3, "messaging": 3,
        "data": 4, "database": 4, "storage": 4,
        "identity": 5, "security": 5, "observability": 5,
    }
    valid_icons = {
        "aws-api-gateway","aws-rds","aws-ecs","aws-s3","aws-lambda","aws-ec2","aws-alb","aws-cloudfront",
        "azure-sql","azure-app-service","azure-vm","azure-api-management","azure-active-directory","azure-functions","azure-service-bus",
        "gcp-cloud-run","gcp-gcs","gcp-bigquery","gcp-pubsub","active-directory","azure-active-directory","okta","ldap","saviynt-iga","microsoft-graph",
        "kafka","rabbitmq","kubernetes","load-balancer","firewall","router","dns","database","server","client","user","cog"
    }
    custom = {i.get("tag") for i in diagram.get("custom_icons", [])}

    text = " ".join(
        " ".join([str(n.get("data", {}).get(k, "")) for k in ("label", "category", "icon", "role")])
        for n in diagram.get("nodes", [])
    ).lower()
    if not diagram.get("pattern") or diagram.get("pattern") in {"generic", "unknown"}:
        if any(x in text for x in ("saviynt", "identity governance", "active directory", "entra", "okta", " scim")):
            diagram["pattern"] = "iam"
        elif any(x in text for x in ("kafka", "rabbitmq", "pubsub", "event")):
            diagram["pattern"] = "event_driven"
        elif any(x in text for x in ("warehouse", "etl", "ingestion", "pipeline", "transform")):
            diagram["pattern"] = "data_pipeline"
        else:
            diagram["pattern"] = "generic"

    for n in diagram.get("nodes", []):
        data = n.setdefault("data", {})
        label = str(data.get("label", "")).lower()
        category = (data.get("category") or "general").lower()
        data["category"] = category
        data["layer"] = category_layer.get(category, data.get("layer", 2))
        if data.get("icon") not in valid_icons and data.get("icon") not in custom:
            data["icon"] = "server"
        if not data.get("provider"):
            icon = data.get("icon", "")
            data["provider"] = "aws" if icon.startswith("aws-") else "azure" if icon.startswith("azure-") else "gcp" if icon.startswith("gcp-") else "generic"

        # Semantic role normalization. The renderer must not have to guess these from coordinates.
        role = str(data.get("role") or "").lower()
        if diagram["pattern"] == "iam":
            if "saviynt" in label:
                role, data["importance"] = "primary_component", "primary"
                data["peerGroup"] = ""
            elif "active directory" in label or data.get("icon") in {"active-directory", "ldap"}:
                role, data["peerGroup"] = "identity_source", "identity_sources"
            elif any(x in label for x in ("entra", "okta", "identity provider", "azure active directory")):
                role, data["peerGroup"] = "identity_provider", "identity_provider"
            elif any(x in label for x in ("user", "employee", "admin", "browser", "client")):
                role, data["peerGroup"] = "external_actor", "users"
            else:
                role, data["peerGroup"] = "target_application", "target_applications"
        data["role"] = role or "peer_service"
        data.setdefault("importance", "normal")
        data.setdefault("peerGroup", "")

    # Strict IAM boundary ownership: do not put SaaS targets in AWS merely because one target is AWS IAM.
    if diagram["pattern"] == "iam":
        node_by_id = {n.get("id"): n for n in diagram.get("nodes", [])}
        valid_groups = []
        for g in diagram.get("groups", []):
            gid = g.get("id")
            members = [n for n in diagram.get("nodes", []) if n.get("parentId") == gid]
            providers = {n.get("data", {}).get("provider") for n in members}
            label = str(g.get("label", "")).lower()
            if "aws" in label and any(p not in {"aws", "generic", None} for p in providers):
                for n in members:
                    n["parentId"] = None
                continue
            valid_groups.append(g)
        diagram["groups"] = valid_groups

    seen = set(); cleaned = []
    for e in diagram.get("edges", []):
        key = (e.get("source"), e.get("target"), e.get("label") or e.get("data", {}).get("protocol", ""))
        if not all(key[:2]) or key in seen:
            continue
        seen.add(key)
        d = e.setdefault("data", {})
        d.setdefault("direction", "forward")
        d.setdefault("kind", "sync")
        if not e.get("label"):
            e["label"] = d.get("protocol") or ""
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
