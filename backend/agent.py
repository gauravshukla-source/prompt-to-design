import os
import json
from typing import List, Optional
from architecture_engine import normalize_diagram as phase3_normalize
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

class Node(BaseModel):
    id: str
    type: str = Field(..., description="Type of node: 'cloudIcon', 'database', 'group', 'process', 'actor'")
    parentId: Optional[str] = Field(None, description="Parent group ID if nested inside a boundary")
    data: NodeData

class EdgeData(BaseModel):
    protocol: Optional[str] = Field(None, description="Protocol used, e.g., 'HTTPS', 'gRPC', 'AMQP', 'LDAP'")
    encrypted: Optional[bool] = Field(None, description="Whether the connection is encrypted")
    direction: Optional[str] = Field("forward", description="forward, bidirectional, or response")
    kind: Optional[str] = Field("sync", description="sync, async, auth, data, control, or observability")
    sourcePort: Optional[str] = Field("auto", description="auto, north, south, east, west")
    targetPort: Optional[str] = Field("auto", description="auto, north, south, east, west")

class Edge(BaseModel):
    id: str
    source: str
    target: str
    label: Optional[str] = Field(None, description="Label for the edge showing integration flow")
    data: Optional[EdgeData] = None

class Group(BaseModel):
    id: str
    label: str
    type: str = Field(..., description="Boundary type: cloud, awsAccount, azureSubscription, gcpProject, vpc, vnet, subnet, securityGroup, trustZone, kubernetesCluster, onPrem, saas, azureResourceGroup, generic")
    provider: Optional[str] = Field(None, description="aws, azure, gcp, onprem, saas, generic")
    zone: Optional[str] = Field(None, description="internet, dmz, public, private, trusted, restricted")

class DiagramSchema(BaseModel):
    diagramType: str = Field(..., description="architecture is preferred; integration and flowchart only when explicitly requested")
    groups: List[Group]
    nodes: List[Node]
    edges: List[Edge]

# Base prompts
SYSTEM_PROMPT = """
You are a principal Enterprise Solutions Architect. Produce clean, publication-quality architecture diagram specifications inspired by AWS Architecture Center, Microsoft Azure Architecture Center, and Google Cloud reference architectures.
The renderer owns coordinates; you own semantic architecture.
CRITICAL RULES:
1. Organize architecture left-to-right into 4-7 logical layers: External/Users -> Edge/Network -> Application/Compute -> Integration/Messaging -> Data -> Identity/Security/Observability.
2. Assign every node a category and layer. Keep peers in the same layer.
3. Use groups only for real boundaries: cloud/on-prem/SaaS domain, VPC/VNet/resource group, cluster, subnet, or trust zone.
4. Every edge is a real directional interaction source -> target. Prefer adjacent layers and avoid decorative/duplicate edges.
5. Edge labels are short protocol/flow labels only: HTTPS, REST/HTTPS, gRPC, AMQP, LDAP, JDBC, OAuth2/OIDC, Event.
6. Use direction="bidirectional" only for genuine two-way relationships; use kind="async" for queues/topics/events.
7. Generate 5-18 nodes. Summarize repeated infrastructure instead of creating clutter.
8. Use architecture notation (components, boundaries, directional connectors), not a generic flowchart.
9. Use ONLY approved icon slugs or supplied custom icon tags. Never invent slugs.
10. Do not create empty/decorative groups.
11. Model boundaries hierarchically: provider/cloud -> account/subscription/project -> VPC/VNet -> subnet/trust zone -> workload when relevant. Do not force every boundary level.
12. Keep connectivity readable: fan-in/fan-out through gateways or brokers; avoid many-to-many direct lines.
13. For async flows use Event, AMQP, Kafka, Pub/Sub or Service Bus and never draw async flows as request/response.
14. Authentication/identity dependencies should normally be shown as side dependencies, not as the main request path.
15. Prefer one primary left-to-right request path. Secondary identity, logging and control-plane flows may use dashed connectors.
16. Think in ports: each connector must leave/enter a sensible north/south/east/west side. Leave sourcePort/targetPort=auto unless a specific side is architecturally required.
17. Design for multiple views: context, logical, integration, security and data-flow. The logical view is the default full topology.
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
    gcp_project = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GCP_PROJECT_ID")
    gcp_location = os.environ.get("GCP_LOCATION", "global")
    model = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")

    try:
        creds, proj = google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
        resolved_project = proj or gcp_project
        if not resolved_project:
            raise RuntimeError("No Google Cloud project found in ADC or GOOGLE_CLOUD_PROJECT")
        return {
            "authenticated": True,
            "auth_mode": "Vertex AI (ADC)",
            "project": resolved_project,
            "location": gcp_location,
            "model": model,
            "message": "Connected via Application Default Credentials (ADC); no API key is used"
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
    Initializes the Google Gen AI SDK for Vertex AI using Application Default Credentials only.

    Credential precedence is entirely ADC-controlled (local gcloud ADC, workload identity,
    service account attached to Cloud Run/GKE/Compute Engine, etc.). API keys are never read.
    """
    env_project = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GCP_PROJECT_ID")
    gcp_location = os.environ.get("GCP_LOCATION", "global")

    try:
        credentials, adc_project = google.auth.default(
            scopes=["https://www.googleapis.com/auth/cloud-platform"]
        )
        project = env_project or adc_project
        if not project:
            raise RuntimeError(
                "No Google Cloud project was resolved. Set GOOGLE_CLOUD_PROJECT or configure ADC with a project."
            )
        return genai.Client(
            vertexai=True,
            project=project,
            location=gcp_location,
            credentials=credentials,
        )
    except Exception as e:
        raise RuntimeError(
            f"Vertex AI ADC initialization failed: {e}. "
            "No API-key fallback is enabled. For local development run "
            "'gcloud auth application-default login' and set GOOGLE_CLOUD_PROJECT. "
            "For Cloud Run/GKE/Compute Engine, attach a service account with Vertex AI User permissions."
        ) from e


def get_model_candidates() -> list[str]:
    """Return newest-first Gemini candidates while allowing an explicit enterprise override.

    The configured GEMINI_MODEL is always attempted first. The remaining candidates provide
    graceful compatibility when a model is not yet enabled in a particular Vertex AI project/region.
    """
    preferred = os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")
    newest_first = [
        preferred,
        "gemini-3.8-flash",
        "gemini-3.7-flash",
        "gemini-3.6-flash",
        "gemini-3.5-flash",
        "gemini-2.5-flash",
    ]
    seen = set()
    return [m for m in newest_first if m and not (m in seen or seen.add(m))]

def _generate_with_model_fallback(client: genai.Client, contents: str, config: types.GenerateContentConfig):
    """
    Tries the configured model first, and gracefully falls back to other standard
    Vertex AI Gemini models in the region if a 404 NOT_FOUND occurs.
    """
    candidate_models = get_model_candidates()

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

def normalize_diagram(diagram: dict, custom_icons: list | None = None) -> dict:
    """Compatibility wrapper for the Phase 3 architecture intelligence engine."""
    return phase3_normalize(diagram, custom_icons)

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

    return normalize_diagram(json.loads(response.text), custom_icons)

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

    return normalize_diagram(json.loads(response.text), custom_icons)