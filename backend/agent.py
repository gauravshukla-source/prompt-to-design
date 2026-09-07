"""
Enterprise Architecture Engine 3.0
----------------------------------

Semantic architecture compiler using:

- Google Vertex AI
- Application Default Credentials (ADC)
- Google Gen AI SDK
- Gemini structured JSON output

No API key is used.

Environment variables:

GOOGLE_CLOUD_PROJECT
    Google Cloud project ID

GOOGLE_CLOUD_LOCATION
    Vertex AI location
    Default: us-central1

GCP_LOCATION
    Legacy fallback for location

GEMINI_MODEL
    Preferred Gemini model
    Default: gemini-2.5-flash
"""

import json
import logging
import os
from typing import List, Optional

import google.auth
from google import genai
from google.genai import types
from pydantic import BaseModel, Field


# =============================================================================
# LOGGING
# =============================================================================

logging.basicConfig(level=os.getenv("LOG_LEVEL", "INFO"))
logger = logging.getLogger(__name__)


# =============================================================================
# GOOGLE CLOUD CONFIGURATION
# =============================================================================

DEFAULT_PROJECT_ID = "architecture-diagram-500204"

PROJECT_ID = (
    os.getenv("GOOGLE_CLOUD_PROJECT")
    or os.getenv("GCP_PROJECT_ID")
    or DEFAULT_PROJECT_ID
)

LOCATION = (
    os.getenv("GOOGLE_CLOUD_LOCATION")
    or os.getenv("GCP_LOCATION")
    or "us-central1"
)

DEFAULT_MODEL = "gemini-2.5-flash"

PREFERRED_MODEL = os.getenv(
    "GEMINI_MODEL",
    DEFAULT_MODEL
).strip()


def get_model_candidates() -> List[str]:
    """
    Return model candidates in priority order.

    IMPORTANT:
    The environment variable GEMINI_MODEL always gets first priority.

    We intentionally use stable Vertex AI model IDs here.

    If your project does not have access to a fallback model,
    the next candidate is attempted.
    """

    candidates = [
        PREFERRED_MODEL,
        "gemini-2.5-flash",
        "gemini-2.5-pro",
        "gemini-2.5-flash-lite",
    ]

    # Remove duplicates while preserving order
    unique_models = []

    for model in candidates:
        if model and model not in unique_models:
            unique_models.append(model)

    return unique_models


MODEL_CANDIDATES = get_model_candidates()


# =============================================================================
# PYDANTIC ARCHITECTURE SCHEMA
# =============================================================================

class Domain(BaseModel):
    id: str
    label: str
    type: str = "enterprise"
    members: List[str] = Field(default_factory=list)


class Boundary(BaseModel):
    id: str
    label: str
    type: str = "boundary"
    members: List[str] = Field(default_factory=list)
    parentId: Optional[str] = None


class NodeData(BaseModel):
    label: str

    icon: Optional[str] = None
    category: Optional[str] = "general"
    description: Optional[str] = None

    provider: Optional[str] = "generic"
    domain: Optional[str] = None

    role: Optional[str] = None

    visualType: Optional[str] = None

    peerGroup: Optional[str] = None

    importance: Optional[str] = "normal"

    layer: Optional[int] = None


class Node(BaseModel):
    id: str

    type: str = "component"

    parentId: Optional[str] = None

    data: NodeData


class EdgeData(BaseModel):
    protocol: Optional[str] = None

    direction: Optional[str] = "forward"

    kind: Optional[str] = "sync"

    encrypted: Optional[bool] = None


class Edge(BaseModel):
    id: str

    source: str

    target: str

    label: Optional[str] = None

    data: EdgeData = Field(default_factory=EdgeData)


class Group(BaseModel):
    id: str

    label: str

    type: str = "boundary"

    parentId: Optional[str] = None

    members: List[str] = Field(default_factory=list)


class DiagramSchema(BaseModel):

    diagramType: str = "architecture"

    title: str = "Enterprise Architecture"

    architectureType: str = "generic"

    viewpoint: str = "logical"

    pattern: str = "generic"

    domains: List[Domain] = Field(default_factory=list)

    boundaries: List[Boundary] = Field(default_factory=list)

    layers: List[str] = Field(default_factory=list)

    groups: List[Group] = Field(default_factory=list)

    nodes: List[Node] = Field(default_factory=list)

    edges: List[Edge] = Field(default_factory=list)

    legend: List[str] = Field(default_factory=list)


# =============================================================================
# APPROVED ICONS
# =============================================================================

APPROVED_ICONS = """
AWS:
aws-api-gateway
aws-rds
aws-ecs
aws-s3
aws-lambda
aws-ec2
aws-alb
aws-cloudfront

Azure:
azure-sql
azure-app-service
azure-vm
azure-api-management
azure-active-directory
azure-functions
azure-service-bus

GCP:
gcp-cloud-run
gcp-gcs
gcp-bigquery
gcp-pubsub

Identity:
active-directory
azure-active-directory
okta
ldap
saviynt-iga
microsoft-graph

Infrastructure:
kubernetes
load-balancer
firewall
router
dns
database
server
client
user
cog
kafka
rabbitmq
"""


# =============================================================================
# SYSTEM PROMPT
# =============================================================================

SYSTEM_PROMPT = f"""
You are a Principal Enterprise Architect and architecture documentation specialist.

You are NOT a generic flowchart generator.

Your responsibility is to build a structured ENTERPRISE ARCHITECTURE MODEL
that can later be compiled into a professional architecture diagram.

Follow professional architecture principles:

- Select one clear architecture viewpoint.
- Use meaningful domains and boundaries.
- Show directional relationships.
- Keep labels concise.
- Avoid unnecessary detail.
- Do not create decorative empty boxes.
- Do not overload a single diagram.
- Do not invent infrastructure that the user did not request.
- Prefer real technology names when explicitly provided.

====================================================================

STEP 1 - CLASSIFY THE ARCHITECTURE

architectureType must be one of:

- cloud
- hybrid_cloud
- application
- data
- identity
- security
- network
- integration
- enterprise
- generic

====================================================================

STEP 2 - SELECT THE VIEWPOINT

viewpoint must be one of:

- context
- logical
- container
- deployment
- security

Do NOT mix logical abstraction and deployment topology unless
explicitly requested.

====================================================================

STEP 3 - IDENTIFY PATTERN

pattern should be one of:

- iam
- microservices
- event_driven
- data_pipeline
- three_tier
- zero_trust
- hybrid_cloud
- hub_spoke
- generic

====================================================================

STEP 4 - IDENTIFY DOMAINS AND BOUNDARIES

Boundaries must represent real architecture scope such as:

- Enterprise
- Organization
- Cloud Provider
- Region
- VPC
- VNet
- Subnet
- Kubernetes Cluster
- Deployment Environment
- Trust Zone
- Security Zone
- Network Zone

Never create empty decorative boundaries.

====================================================================

STEP 5 - IDENTIFY COMPONENTS

Each component should have:

- meaningful ID
- concise label
- role
- visualType
- provider
- icon when applicable
- layer
- peerGroup when appropriate

visualType must be one of:

- actor
- component
- datastore
- event
- external
- security

====================================================================

STEP 6 - IDENTIFY RELATIONSHIPS

Relationships must be directional.

Allowed relationship kinds:

- sync
- async
- auth
- data
- control
- security

Prefer one-way arrows.

Only create reverse relationships when they provide important
architectural information.

Do not create unnecessary sequential connections between peer systems.

====================================================================

VIEWPOINT RULES

CONTEXT:

Show:

- People
- Primary system
- External systems

Avoid:

- Infrastructure
- Subnets
- Databases
- Protocol clutter

------------------------------------------------------------

LOGICAL:

Show:

- Responsibilities
- Major components
- Integration flow
- Technology choices when useful

Avoid:

- Detailed infrastructure topology

------------------------------------------------------------

CONTAINER:

Show:

- Applications
- Services
- Datastores
- Major runtime boundaries

------------------------------------------------------------

DEPLOYMENT:

Show:

- Cloud
- Region
- VPC/VNet
- Subnets
- Clusters
- Compute
- Databases
- Infrastructure

Use nested boundaries where appropriate.

------------------------------------------------------------

SECURITY:

Show:

- Trust boundaries
- Security controls
- Identity
- Authentication
- Authorization
- Network segmentation
- Protected resources

====================================================================

NODE COUNT

Use approximately 5 to 18 nodes.

If the architecture contains many repeated peers,
use peerGroup.

Do not create dozens of nodes unless explicitly requested.

====================================================================

ICON RULES

Only use official provider/service names when explicitly identified.

Approved icon slugs:

{APPROVED_ICONS}

====================================================================

OUTPUT RULES

Return ONLY JSON.

The JSON MUST conform to the provided schema.

Do not include:

- Markdown
- Explanations
- Comments
- Code fences
"""


# =============================================================================
# ADC AUTHENTICATION STATUS
# =============================================================================

def check_auth_status():
    """
    Check whether Application Default Credentials are available.
    """

    try:

        credentials, resolved_project = google.auth.default()

        project = resolved_project or PROJECT_ID

        logger.info(
            "ADC authentication successful | "
            "Project=%s | Location=%s | PreferredModel=%s",
            project,
            LOCATION,
            PREFERRED_MODEL,
        )

        return {
            "authenticated": True,
            "auth_mode": "Vertex AI (ADC)",
            "project": project,
            "location": LOCATION,
            "model": PREFERRED_MODEL,
            "model_candidates": MODEL_CANDIDATES,
            "message": "Connected via Application Default Credentials",
        }

    except Exception as exc:

        logger.exception("ADC authentication failed")

        return {
            "authenticated": False,
            "auth_mode": "Vertex AI (ADC)",
            "project": PROJECT_ID,
            "location": LOCATION,
            "model": PREFERRED_MODEL,
            "model_candidates": MODEL_CANDIDATES,
            "message": f"ADC not detected: {exc}",
        }


# =============================================================================
# GEMINI CLIENT
# =============================================================================

def get_gemini_client():
    """
    Create a Google Gen AI SDK client configured for Vertex AI.

    Authentication:
        Application Default Credentials

    No API key is used.
    """

    logger.info(
        "Creating Vertex AI Gemini client | "
        "Project=%s | Location=%s",
        PROJECT_ID,
        LOCATION,
    )

    return genai.Client(
        vertexai=True,
        project=PROJECT_ID,
        location=LOCATION,
    )


# =============================================================================
# GEMINI MODEL EXECUTION
# =============================================================================

def generate_with_fallback(
    client,
    contents,
    config,
):
    """
    Generate content using the configured model candidates.

    Logs each model attempt so Cloud Run logs clearly show:

    - Model attempted
    - Model selected
    - Failure reason

    This avoids silent failures.
    """

    errors = []

    for model_name in MODEL_CANDIDATES:

        try:

            logger.info(
                "Attempting Gemini model | "
                "Model=%s | Project=%s | Location=%s",
                model_name,
                PROJECT_ID,
                LOCATION,
            )

            response = client.models.generate_content(
                model=model_name,
                contents=contents,
                config=config,
            )

            logger.info(
                "Gemini generation successful | "
                "Model=%s",
                model_name,
            )

            return response

        except Exception as exc:

            error_message = str(exc)

            logger.warning(
                "Gemini model failed | "
                "Model=%s | Error=%s",
                model_name,
                error_message,
            )

            errors.append(
                {
                    "model": model_name,
                    "error": error_message,
                }
            )

    formatted_errors = "\n".join(
        [
            f"- {item['model']}: {item['error']}"
            for item in errors
        ]
    )

    raise RuntimeError(
        "No configured Gemini model succeeded.\n"
        f"Project: {PROJECT_ID}\n"
        f"Location: {LOCATION}\n"
        f"Models attempted:\n{formatted_errors}"
    )


# =============================================================================
# SEMANTIC ROLE INFERENCE
# =============================================================================

def _infer_role(text):
    """
    Infer architecture role and visual type.

    Returns:
        (role, visual_type)
    """

    text = text.lower()

    # -----------------------------------------------------------------
    # ACTORS
    # -----------------------------------------------------------------

    if any(
        item in text
        for item in [
            "employee",
            "user",
            "customer",
            "admin",
            "browser",
            "developer",
        ]
    ):
        return "external_actor", "actor"

    # -----------------------------------------------------------------
    # IDENTITY SOURCES
    # -----------------------------------------------------------------

    if any(
        item in text
        for item in [
            "active directory",
            "ldap",
            "hr source",
            "human resources",
        ]
    ):
        return "identity_source", "component"

    # -----------------------------------------------------------------
    # IDENTITY PROVIDERS
    # -----------------------------------------------------------------

    if any(
        item in text
        for item in [
            "entra",
            "okta",
            "identity provider",
            "idp",
        ]
    ):
        return "identity_provider", "component"

    # -----------------------------------------------------------------
    # IGA
    # -----------------------------------------------------------------

    if any(
        item in text
        for item in [
            "saviynt",
            "sailpoint",
            "identity governance",
            "iga",
        ]
    ):
        return "primary_component", "component"

    # -----------------------------------------------------------------
    # SECURITY
    # -----------------------------------------------------------------

    if any(
        item in text
        for item in [
            "firewall",
            "waf",
            "security control",
            "ztna",
            "casb",
        ]
    ):
        return "security_control", "security"

    # -----------------------------------------------------------------
    # EDGE
    # -----------------------------------------------------------------

    if any(
        item in text
        for item in [
            "api gateway",
            "ingress",
            "cloudfront",
            "cdn",
        ]
    ):
        return "edge_entry", "component"

    # -----------------------------------------------------------------
    # ROUTING
    # -----------------------------------------------------------------

    if any(
        item in text
        for item in [
            "load balancer",
            "alb",
            "router",
        ]
    ):
        return "traffic_router", "component"

    # -----------------------------------------------------------------
    # EVENT SYSTEMS
    # -----------------------------------------------------------------

    if any(
        item in text
        for item in [
            "kafka",
            "rabbitmq",
            "pubsub",
            "service bus",
            "event bus",
            "eventbridge",
        ]
    ):
        return "event_backbone", "event"

    # -----------------------------------------------------------------
    # DATA STORES
    # -----------------------------------------------------------------

    if any(
        item in text
        for item in [
            "database",
            "rds",
            "sql",
            "postgres",
            "mysql",
            "warehouse",
            "storage",
            "s3",
            "gcs",
            "bigquery",
        ]
    ):
        return "data_store", "datastore"

    # -----------------------------------------------------------------
    # EXTERNAL / SAAS
    # -----------------------------------------------------------------

    if any(
        item in text
        for item in [
            "salesforce",
            "servicenow",
            "workday",
            "saas",
        ]
    ):
        return "target_application", "external"

    # -----------------------------------------------------------------
    # DEFAULT
    # -----------------------------------------------------------------

    return "peer_service", "component"


# =============================================================================
# DIAGRAM NORMALIZATION
# =============================================================================

def normalize_diagram(diagram):
    """
    Normalize Gemini output into the canonical architecture model.

    This protects the frontend renderer from inconsistent AI output.
    """

    if not isinstance(diagram, dict):
        raise ValueError(
            "Gemini did not return a valid JSON object."
        )

    # -----------------------------------------------------------------
    # REQUIRED COLLECTIONS
    # -----------------------------------------------------------------

    diagram.setdefault("domains", [])

    diagram.setdefault("boundaries", [])

    diagram.setdefault("groups", [])

    diagram.setdefault("nodes", [])

    diagram.setdefault("edges", [])

    diagram.setdefault("legend", [])

    diagram.setdefault("layers", [])

    # -----------------------------------------------------------------
    # NORMALIZE NODES
    # -----------------------------------------------------------------

    normalized_nodes = []

    seen_node_ids = set()

    for node in diagram["nodes"]:

        if not isinstance(node, dict):
            continue

        node_id = str(
            node.get("id") or ""
        ).strip()

        if not node_id:
            continue

        if node_id in seen_node_ids:
            continue

        seen_node_ids.add(node_id)

        node["id"] = node_id

        node.setdefault(
            "type",
            "component",
        )

        node.setdefault(
            "data",
            {},
        )

        data = node["data"]

        label = str(
            data.get("label")
            or node_id
            or "Component"
        ).strip()

        data["label"] = label

        semantic_text = (
            f"{label} "
            f"{data.get('description', '')} "
            f"{data.get('icon', '')}"
        )

        inferred_role, inferred_visual = (
            _infer_role(semantic_text)
        )

        if not data.get("role"):
            data["role"] = inferred_role

        if not data.get("visualType"):
            data["visualType"] = inferred_visual

        if not data.get("importance"):
            data["importance"] = "normal"

        if data["role"] == "primary_component":
            data["importance"] = "primary"

        if not data.get("peerGroup"):

            if data["role"] == "target_application":

                data["peerGroup"] = (
                    "target_systems"
                )

            elif data["role"] == "peer_service":

                data["peerGroup"] = (
                    "services"
                )

            else:

                data["peerGroup"] = ""

        if data.get("layer") is None:

            layer_mapping = {

                "external_actor": 0,

                "identity_source": 1,

                "identity_provider": 2,

                "edge_entry": 1,

                "traffic_router": 2,

                "primary_component": 3,

                "peer_service": 3,

                "event_backbone": 3,

                "data_store": 4,

                "target_application": 4,

                "security_control": 2,
            }

            data["layer"] = (
                layer_mapping.get(
                    data["role"],
                    2,
                )
            )

        normalized_nodes.append(node)

    diagram["nodes"] = normalized_nodes

    # -----------------------------------------------------------------
    # VALID NODE IDS
    # -----------------------------------------------------------------

    node_ids = {
        node["id"]
        for node in diagram["nodes"]
    }

    # -----------------------------------------------------------------
    # NORMALIZE EDGES
    # -----------------------------------------------------------------

    normalized_edges = []

    seen_edges = set()

    for edge in diagram["edges"]:

        if not isinstance(edge, dict):
            continue

        source = str(
            edge.get("source") or ""
        ).strip()

        target = str(
            edge.get("target") or ""
        ).strip()

        if not source or not target:
            continue

        if source not in node_ids:
            continue

        if target not in node_ids:
            continue

        if source == target:
            continue

        edge["source"] = source

        edge["target"] = target

        edge.setdefault(
            "data",
            {},
        )

        edge_data = edge["data"]

        edge_data.setdefault(
            "kind",
            "sync",
        )

        edge_data.setdefault(
            "direction",
            "forward",
        )

        label = str(
            edge.get("label")
            or edge_data.get("protocol")
            or ""
        ).strip()

        edge["label"] = label

        if not edge.get("id"):

            edge["id"] = (
                f"{source}_to_{target}"
            )

        edge_key = (
            source,
            target,
            label,
            edge_data["kind"],
        )

        if edge_key in seen_edges:
            continue

        seen_edges.add(edge_key)

        normalized_edges.append(edge)

    diagram["edges"] = normalized_edges

    # -----------------------------------------------------------------
    # NORMALIZE GROUP MEMBERSHIP
    # -----------------------------------------------------------------

    def get_members(item):

        members = set()

        for key in [
            "members",
            "nodeIds",
            "node_ids",
            "children",
        ]:

            value = item.get(key)

            if isinstance(value, list):

                members.update(
                    str(member)
                    for member in value
                    if str(member) in node_ids
                )

        return members

    # -----------------------------------------------------------------
    # NORMALIZE GROUPS
    # -----------------------------------------------------------------

    normalized_groups = []

    for group in diagram["groups"]:

        if not isinstance(group, dict):
            continue

        group_id = str(
            group.get("id") or ""
        ).strip()

        if not group_id:
            continue

        members = get_members(group)

        # Support node-side membership
        members.update(
            node["id"]
            for node in diagram["nodes"]
            if node.get("parentId") == group_id
        )

        # IMPORTANT:
        # Remove empty groups.
        if not members:
            continue

        group["id"] = group_id

        group["members"] = sorted(members)

        normalized_groups.append(group)

    diagram["groups"] = normalized_groups

    # -----------------------------------------------------------------
    # NORMALIZE BOUNDARIES
    # -----------------------------------------------------------------

    normalized_boundaries = []

    for boundary in diagram["boundaries"]:

        if not isinstance(boundary, dict):
            continue

        boundary_id = str(
            boundary.get("id") or ""
        ).strip()

        if not boundary_id:
            continue

        members = get_members(boundary)

        # Boundaries without members must not render
        if not members:
            continue

        boundary["id"] = boundary_id

        boundary["members"] = sorted(members)

        normalized_boundaries.append(boundary)

    diagram["boundaries"] = (
        normalized_boundaries
    )

    # -----------------------------------------------------------------
    # NORMALIZE DOMAINS
    # -----------------------------------------------------------------

    normalized_domains = []

    for domain in diagram["domains"]:

        if not isinstance(domain, dict):
            continue

        domain_id = str(
            domain.get("id") or ""
        ).strip()

        if not domain_id:
            continue

        members = get_members(domain)

        if not members:
            continue

        domain["id"] = domain_id

        domain["members"] = sorted(members)

        normalized_domains.append(domain)

    diagram["domains"] = normalized_domains

    # -----------------------------------------------------------------
    # DEFAULT ARCHITECTURE METADATA
    # -----------------------------------------------------------------

    diagram.setdefault(
        "diagramType",
        "architecture",
    )

    diagram.setdefault(
        "title",
        "Enterprise Architecture",
    )

    diagram.setdefault(
        "architectureType",
        "generic",
    )

    diagram.setdefault(
        "viewpoint",
        "logical",
    )

    diagram.setdefault(
        "pattern",
        "generic",
    )

    logger.info(
        "Architecture normalized | "
        "Nodes=%s | Edges=%s | "
        "Domains=%s | Boundaries=%s | "
        "Groups=%s",
        len(diagram["nodes"]),
        len(diagram["edges"]),
        len(diagram["domains"]),
        len(diagram["boundaries"]),
        len(diagram["groups"]),
    )

    return diagram


# =============================================================================
# GENERATE DIAGRAM
# =============================================================================

def generate_diagram(
    prompt: str,
    custom_icons: Optional[list] = None,
):
    """
    Generate a new Enterprise Architecture Model.
    """

    if not prompt or not prompt.strip():

        raise ValueError(
            "Architecture prompt cannot be empty."
        )

    logger.info(
        "Generating enterprise architecture | "
        "PromptLength=%s",
        len(prompt),
    )

    client = get_gemini_client()

    config = types.GenerateContentConfig(

        system_instruction=SYSTEM_PROMPT,

        response_mime_type="application/json",

        response_schema=DiagramSchema,
    )

    user_prompt = (
        "Analyze and design this enterprise architecture.\n\n"
        f"USER REQUEST:\n{prompt.strip()}"
    )

    response = generate_with_fallback(
        client=client,
        contents=user_prompt,
        config=config,
    )

    if not response:
        raise RuntimeError(
            "Gemini returned an empty response."
        )

    response_text = (
        response.text or ""
    ).strip()

    if not response_text:

        raise RuntimeError(
            "Gemini returned an empty response body."
        )

    try:

        diagram = json.loads(
            response_text
        )

    except json.JSONDecodeError as exc:

        logger.error(
            "Invalid Gemini JSON response: %s",
            response_text[:1000],
        )

        raise RuntimeError(
            "Gemini did not return valid architecture JSON."
        ) from exc

    return normalize_diagram(
        diagram
    )


# =============================================================================
# REFINE DIAGRAM
# =============================================================================

def refine_diagram(
    prompt: str,
    current_diagram: dict,
    custom_icons: Optional[list] = None,
):
    """
    Refine an existing Enterprise Architecture Model.

    Existing IDs should be preserved wherever possible
    so the frontend can maintain architecture continuity.
    """

    if not prompt or not prompt.strip():

        raise ValueError(
            "Refinement prompt cannot be empty."
        )

    if not isinstance(
        current_diagram,
        dict,
    ):

        raise ValueError(
            "Current diagram must be a JSON object."
        )

    client = get_gemini_client()

    current_json = json.dumps(
        current_diagram,
        indent=2,
    )

    instruction = f"""
{SYSTEM_PROMPT}

====================================================================

REFINEMENT MODE

You are refining an existing Enterprise Architecture Model.

Rules:

1. Preserve unchanged architecture intent.
2. Preserve existing IDs whenever possible.
3. Do not remove components unless requested.
4. Do not invent unrelated infrastructure.
5. Maintain the selected viewpoint unless explicitly changed.
6. Maintain architecture semantics.
7. Do not create empty boundaries.
8. Return ONLY valid JSON.

CURRENT ARCHITECTURE MODEL:

{current_json}

REQUESTED CHANGE:

{prompt.strip()}
"""

    config = types.GenerateContentConfig(

        system_instruction=instruction,

        response_mime_type="application/json",

        response_schema=DiagramSchema,
    )

    response = generate_with_fallback(
        client=client,
        contents=(
            "Return the revised Enterprise "
            "Architecture Model."
        ),
        config=config,
    )

    if not response:

        raise RuntimeError(
            "Gemini returned an empty response."
        )

    response_text = (
        response.text or ""
    ).strip()

    if not response_text:

        raise RuntimeError(
            "Gemini returned an empty response body."
        )

    try:

        diagram = json.loads(
            response_text
        )

    except json.JSONDecodeError as exc:

        logger.error(
            "Invalid Gemini JSON response: %s",
            response_text[:1000],
        )

        raise RuntimeError(
            "Gemini did not return valid architecture JSON."
        ) from exc

    return normalize_diagram(
        diagram
    )