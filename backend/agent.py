import json
import os
from typing import List, Optional

import google.auth
from google import genai
from google.genai import types
from pydantic import BaseModel, Field


class NodeProperty(BaseModel):
    key: str
    value: str


class NodeData(BaseModel):
    label: str
    icon: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    properties: Optional[List[NodeProperty]] = None
    layer: Optional[int] = None
    provider: Optional[str] = None


class Node(BaseModel):
    id: str
    type: str
    parentId: Optional[str] = None
    data: NodeData


class EdgeData(BaseModel):
    protocol: Optional[str] = None
    encrypted: Optional[bool] = None
    kind: Optional[str] = None
    direction: Optional[str] = None
    sourcePort: Optional[str] = None
    targetPort: Optional[str] = None


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


class DiagramSchema(BaseModel):
    diagramType: str = "architecture"
    groups: List[Group] = Field(default_factory=list)
    nodes: List[Node] = Field(default_factory=list)
    edges: List[Edge] = Field(default_factory=list)


DEFAULT_MODEL = "gemini-2.5-flash"
FALLBACK_MODELS = (
    "gemini-2.5-flash",
    "gemini-2.5-pro",
    "gemini-2.5-flash-lite",
)

SYSTEM_PROMPT = """
You are a principal Enterprise Solutions Architect. Produce implementation-quality architecture topology JSON for a professional architecture diagram.

DESIGN PRINCIPLES:
- Model the architecture that the user actually asks for; do not force unrelated cloud, IAM, or data components into every diagram.
- Use clear boundaries for meaningful trust, deployment, network, application, cloud, SaaS, or organizational scopes.
- Use parentId only when a node belongs inside a meaningful boundary.
- Prefer 5-18 nodes. Split overly complex requests into logical components without inventing unnecessary services.
- Preserve directional integration flow and use realistic protocols.
- Use category values from: external,user,client,saas,edge,network,gateway,application,compute,service,integration,messaging,data,database,storage,identity,security,observability,general.
- Assign layer 0-6 when helpful: external=0, edge=1, application=2, integration=3, data=4, identity/security=5, observability=6.
- Every edge must reference existing node IDs and include a concise protocol or interaction label.
- Never create duplicate IDs and never create self-loop edges unless explicitly requested.

ICON LIBRARY:
AWS: aws-api-gateway, aws-rds, aws-ecs, aws-s3, aws-lambda, aws-ec2, aws-alb, aws-cloudfront
Azure: azure-sql, azure-app-service, azure-vm, azure-api-management, azure-active-directory, azure-functions, azure-service-bus
GCP: gcp-cloud-run, gcp-gcs, gcp-bigquery, gcp-pubsub
Identity: active-directory, azure-active-directory, okta, ldap, saviynt-iga, microsoft-graph
Messaging/infra: kafka, rabbitmq, kubernetes, load-balancer, firewall, router, dns
Generic: database, server, client, user, cog

GROUP TYPES:
vpc, subnet, securityGroup, azureResourceGroup, kubernetesCluster, generic

Return only JSON conforming to the requested schema. No markdown or explanation.
{custom_icons_context}
"""


def _project() -> str:
    return (
        os.environ.get("GOOGLE_CLOUD_PROJECT")
        or os.environ.get("GCP_PROJECT_ID")
        or os.environ.get("GOOGLE_CLOUD_PROJECT_ID")
        or "architecture-diagram-500204"
    )


def _location() -> str:
    # Keep configurable. global is safest for model availability; us-central1 remains supported when explicitly configured.
    return os.environ.get("GOOGLE_CLOUD_LOCATION") or os.environ.get("GCP_LOCATION") or "global"


def _model() -> str:
    return os.environ.get("GEMINI_MODEL") or DEFAULT_MODEL


def check_auth_status() -> dict:
    try:
        _, detected_project = google.auth.default()
        return {
            "authenticated": True,
            "auth_mode": "Vertex AI ADC",
            "project": detected_project or _project(),
            "location": _location(),
            "model": _model(),
            "message": "Connected with Application Default Credentials",
        }
    except Exception as exc:
        return {
            "authenticated": False,
            "auth_mode": "Vertex AI ADC",
            "project": _project(),
            "location": _location(),
            "model": _model(),
            "message": f"ADC not detected: {exc}",
        }


def get_gemini_client() -> genai.Client:
    try:
        return genai.Client(
            vertexai=True,
            project=_project(),
            location=_location(),
            http_options=types.HttpOptions(api_version="v1"),
        )
    except Exception as exc:
        raise RuntimeError(
            "Vertex AI initialization failed. Configure ADC for local development or a Cloud Run service account with Vertex AI access. "
            f"Details: {exc}"
        ) from exc


def _model_candidates() -> list[str]:
    candidates = [_model(), *FALLBACK_MODELS]
    unique = []
    for model in candidates:
        if model and model not in unique:
            unique.append(model)
    return unique


def _generate_with_model_fallback(client: genai.Client, contents: str, config: types.GenerateContentConfig):
    failures = []
    for model in _model_candidates():
        try:
            response = client.models.generate_content(model=model, contents=contents, config=config)
            if not getattr(response, "text", None):
                raise RuntimeError("Model returned an empty response")
            return response
        except Exception as exc:
            message = str(exc)
            failures.append(f"{model}: {message}")
            if any(token in message.upper() for token in ("404", "NOT_FOUND", "MODEL_NOT_FOUND", "PERMISSION_DENIED")):
                continue
            # Retry another configured Gemini model for transient/model-specific failures as well.
            continue
    raise RuntimeError("No configured Gemini model succeeded. " + " | ".join(failures))


def _custom_context(custom_icons: Optional[list]) -> str:
    if not custom_icons:
        return ""
    lines = []
    for icon in custom_icons:
        tag = icon.get("tag") if isinstance(icon, dict) else None
        desc = icon.get("description", "") if isinstance(icon, dict) else ""
        if tag:
            lines.append(f"- {tag}: {desc}")
    if not lines:
        return ""
    return "\nOrganization-specific custom icon tags (use only when relevant):\n" + "\n".join(lines)


def _parse_response(response) -> dict:
    try:
        payload = json.loads(response.text)
    except Exception as exc:
        raise RuntimeError(f"Model returned invalid JSON: {exc}") from exc
    return DiagramSchema.model_validate(payload).model_dump()


def generate_diagram(prompt: str, custom_icons: Optional[list] = None) -> dict:
    prompt = (prompt or "").strip()
    if not prompt:
        raise ValueError("Prompt cannot be empty")
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT.format(custom_icons_context=_custom_context(custom_icons)),
        response_mime_type="application/json",
        response_schema=DiagramSchema,
        temperature=0.2,
    )
    response = _generate_with_model_fallback(get_gemini_client(), f"Design this architecture:\n{prompt}", config)
    return _parse_response(response)


def refine_diagram(prompt: str, current_diagram: dict, custom_icons: Optional[list] = None) -> dict:
    prompt = (prompt or "").strip()
    if not prompt:
        raise ValueError("Refinement instruction cannot be empty")
    config = types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT.format(custom_icons_context=_custom_context(custom_icons)),
        response_mime_type="application/json",
        response_schema=DiagramSchema,
        temperature=0.15,
    )
    contents = (
        "Current architecture JSON:\n"
        + json.dumps(current_diagram or {}, ensure_ascii=False)
        + "\n\nApply this refinement. Preserve unchanged IDs and relationships:\n"
        + prompt
    )
    response = _generate_with_model_fallback(get_gemini_client(), contents, config)
    return _parse_response(response)
