import os
import json
from typing import List, Optional, Dict
from pydantic import BaseModel, Field
from google import genai
from google.genai import types

# Pydantic models for Structured Output
class NodeData(BaseModel):
    label: str
    icon: Optional[str] = Field(None, description="Standard icon slug (e.g., 'aws-api-gateway', 'aws-rds', 'aws-ecs', 'aws-s3', 'aws-lambda', 'azure-sql', 'azure-app-service', 'azure-vm', 'active-directory', 'kubernetes', 'gcp-cloud-run', 'gcp-gcs') or a custom icon tag")
    category: Optional[str] = Field(None, description="e.g., 'compute', 'database', 'network', 'security', 'integration', 'general'")
    description: Optional[str] = Field(None, description="Brief description of node function")
    properties: Optional[Dict[str, str]] = Field(None, description="Key-value pairs for node properties (e.g., instance size, multi-az)")

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
You are an expert Enterprise Integration and Cloud Solutions Architect. Your job is to design professional, business-accurate architecture diagrams, integration flows, and business flowcharts based on user requests.

Guidelines for Architecture:
1. Use logical boundaries (VPCs, Subnets, Kubernetes Clusters, Resource Groups) to group resources.
2. Ensure database instances (like RDS or Azure SQL) are properly isolated.
3. Include standard connectors like API Gateways, Load Balancers, and ESBs/Message Brokers (Kafka, ActiveMQ, RabbitMQ) for integration points.
4. If Active Directory (AD) or Azure AD is requested, place it in an identity boundary.
5. Use correct protocols on connection lines (edges) e.g., REST, LDAP, AMQP, gRPC.

Icon Library Context:
You have a set of built-in standard icons:
- Cloud/SaaS: 'aws-api-gateway', 'aws-rds', 'aws-ecs', 'aws-s3', 'aws-lambda', 'azure-sql', 'azure-app-service', 'azure-vm', 'active-directory', 'kubernetes', 'gcp-cloud-run', 'gcp-gcs'
- Integration/General: 'kafka', 'rabbitmq', 'database', 'server', 'client', 'user', 'dns', 'router', 'firewall', 'cog'
{custom_icons_context}

Output format:
Return a JSON object that strictly adheres to the requested DiagramSchema.
"""

def generate_diagram(prompt: str, custom_icons: list = None, api_key: str = None) -> dict:
    key = api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise ValueError("Gemini API Key is missing. Please set it in settings or environment.")
        
    client = genai.Client(api_key=key)
    
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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Generate a diagram for the following prompt:\n{prompt}",
        config=config
    )

    return json.loads(response.text)

def refine_diagram(prompt: str, current_diagram: dict, custom_icons: list = None, api_key: str = None) -> dict:
    key = api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not key:
        raise ValueError("Gemini API Key is missing.")

    client = genai.Client(api_key=key)
    
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

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Apply the following modifications: {prompt}",
        config=config
    )

    return json.loads(response.text)
