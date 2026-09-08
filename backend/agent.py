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
    properties: Optional[List[NodeProperty]] = Field(None, description="Key-value pairs for node properties (e.g., instance size, multi-az)")

class Node(BaseModel):
    id: str
    type: str = Field(..., description="Type of node: 'cloudIcon', 'database', 'group', 'process', 'actor'")
    parentId: Optional[str] = Field(None, description="Parent group ID if nested inside a boundary")
    data: NodeData

class EdgeData(BaseModel):
    protocol: Optional[str] = Field(None, description="Protocol used, e.g., 'HTTPS', 'gRPC', 'AMQP', 'LDAP'")
    encrypted: Optional[bool] = Field(None, description="Whether the connection is encrypted")

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
    diagramType: str = Field(..., description="Type of diagram: 'architecture', 'integration', 'flowchart'")
    groups: List[Group]
    nodes: List[Node]
    edges: List[Edge]

# Base prompts
SYSTEM_PROMPT = """
You are a world-class Enterprise Solutions Architect designing professional, publication-quality architecture diagrams matching the standard of AWS Architecture Center, Microsoft Azure documentation, and Google Cloud reference architectures.

## Structural Layout Rules (CRITICAL)
Organize every diagram as clear left-to-right layers inside named groups:
  - Layer 1 (leftmost group): External Clients / Users / SaaS
  - Layer 2: Edge / Network (CDN, DNS, Firewall, Load Balancer, WAF)
  - Layer 3: Application / Compute (App Services, Lambda, ECS, Cloud Run, VMs)
  - Layer 4: Integration / Messaging (API Gateway, Kafka, Service Bus, ESB)
  - Layer 5: Data / Storage (RDS, SQL, S3, GCS, Blob, Cache)
  - Layer 6 (rightmost): Identity / Security (Active Directory, Okta, IAM, LDAP)

Rules:
1. ALWAYS place every node inside a group — set parentId to the group's id.
2. ALWAYS add a label on every edge showing the protocol: HTTPS, REST, gRPC, AMQP, LDAP, JDBC, OAuth2, etc.
3. Use SPECIFIC icon slugs from the library below — never invent new slugs.
4. Generate 6–14 nodes total. No more than 20. Diagrams must be readable.
5. Connect nodes only between adjacent logical layers — show realistic data flow.

## Icon Slug Library
AWS:     aws-api-gateway | aws-rds | aws-ecs | aws-s3 | aws-lambda | aws-ec2 | aws-alb | aws-cloudfront
Azure:   azure-sql | azure-app-service | azure-vm | azure-api-management | azure-active-directory | azure-functions | azure-service-bus
GCP:     gcp-cloud-run | gcp-gcs | gcp-bigquery | gcp-pubsub
Identity: active-directory | azure-active-directory | okta | ldap | saviynt-iga | microsoft-graph
Messaging: kafka | rabbitmq | azure-service-bus
Infra:   kubernetes | load-balancer | firewall | router | dns
Generic: database | server | client | user | cog

## Group Type Values
Use ONLY these values for group.type:
  vpc | subnet | securityGroup | azureResourceGroup | kubernetesCluster | generic

## Output
Return ONLY a valid JSON object conforming to DiagramSchema. No markdown, no explanation.
{custom_icons_context}
"""

def check_auth_status() -> dict:
    """
    Checks the status of Application Default Credentials (ADC) and Vertex AI configuration.
    Returns diagnostic details for monitoring and UI badge display.
    """
    gcp_project = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GCP_PROJECT_ID", "architecture-diagram-500204")
    gcp_location = os.environ.get("GCP_LOCATION", "us-central1")
    model = os.environ.get("GEMINI_MODEL", "gemini-1.5-flash")

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
    preferred_model = os.environ.get("GEMINI_MODEL", "gemini-1.5-flash")
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

    return json.loads(response.text)

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

    return json.loads(response.text)
