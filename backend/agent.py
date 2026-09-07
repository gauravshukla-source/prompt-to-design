import os
import json
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
    layer: Optional[int] = Field(None, ge=0, le=20)
    provider: Optional[str] = None
    deploymentScope: Optional[str] = None
    role: Optional[str] = None

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
    provider: Optional[str] = None

class DiagramSchema(BaseModel):
    diagramType: str = "architecture"
    title: Optional[str] = None
    groups: List[Group] = []
    nodes: List[Node] = []
    edges: List[Edge] = []

SYSTEM_PROMPT = """
You are a principal Enterprise Solutions Architect producing semantic specifications for a professional architecture renderer inspired by AWS Architecture Center, Microsoft Azure Architecture Center and Google Cloud reference architectures. The renderer owns coordinates and routing; you own semantics, containment and accurate relationships.

RULES:
1. Primary flow left-to-right: External/Users -> Edge/Network -> Security/Identity -> Application/Compute -> Integration/Messaging -> Data. Observability is a supporting lane.
2. Use 4-8 logical layers. Every node needs category, role and layer. Keep peers in the same layer.
3. Boundaries are hierarchical and real. Use Group.parentId. Use immediate containment only.
4. Example containment: AWS Cloud -> VPC -> Public Subnet / Private Subnet -> ECS Cluster. Do not force every node into a group.
5. Never create empty/decorative groups.
6. Accuracy matters: DynamoDB, S3, CloudFront and CloudWatch are managed services and must not be drawn as ordinary resources inside a private subnet unless explicitly requested through a private endpoint/deployment scope.
7. AWS three-tier: Public Subnet contains ALB; Private Subnet contains ECS/compute and applicable private data services; managed services remain outside subnet boundaries but can remain under AWS Cloud.
8. Every edge is a real directional interaction. Avoid decorative, duplicate and transitive edges. Prefer adjacent layers.
9. Labels are short protocol/flow labels: HTTPS, DNS, TLS, REST/HTTPS, gRPC, JDBC, LDAP, SAML, OIDC, OAuth2, SCIM, Event, AMQP, Kafka.
10. kind=async for queues/topics/events; kind=auth for authentication/authorization; direction=forward by default.
11. Generate 5-22 nodes and summarize repeated infrastructure.
12. Use ONLY approved icon slugs or supplied custom icon tags.

APPROVED ICONS
AWS: aws-api-gateway | aws-rds | aws-ecs | aws-s3 | aws-lambda | aws-ec2 | aws-alb | aws-cloudfront
Azure: azure-sql | azure-app-service | azure-vm | azure-api-management | azure-active-directory | azure-functions | azure-service-bus
GCP: gcp-cloud-run | gcp-gcs | gcp-bigquery | gcp-pubsub
Identity: active-directory | azure-active-directory | okta | ldap | saviynt-iga | microsoft-graph
Messaging: kafka | rabbitmq | azure-service-bus
Infra: kubernetes | load-balancer | firewall | router | dns
Generic: database | server | client | user | cog
Return ONLY valid JSON conforming to DiagramSchema.
{custom_icons_context}
"""

CATEGORY_LAYER = {"external":0,"user":0,"dns":1,"edge":1,"network":1,"security":2,"identity":2,"gateway":3,"application":4,"compute":4,"general":4,"integration":5,"messaging":5,"data":6,"database":6,"storage":6,"observability":7}
VALID_ICONS = {"aws-api-gateway","aws-rds","aws-ecs","aws-s3","aws-lambda","aws-ec2","aws-alb","aws-cloudfront","azure-sql","azure-app-service","azure-vm","azure-api-management","azure-active-directory","azure-functions","azure-service-bus","gcp-cloud-run","gcp-gcs","gcp-bigquery","gcp-pubsub","active-directory","okta","ldap","saviynt-iga","microsoft-graph","kafka","rabbitmq","kubernetes","load-balancer","firewall","router","dns","database","server","client","user","cog"}

def _candidates():
    return list(dict.fromkeys([os.environ.get("GEMINI_MODEL", "gemini-3.8-flash"),"gemini-3.8-flash","gemini-3.7-flash","gemini-3.6-flash","gemini-2.5-pro"]))

def check_auth_status():
    project=os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GCP_PROJECT_ID", "architecture-diagram-500204")
    location=os.environ.get("GCP_LOCATION", "us-central1")
    model=os.environ.get("GEMINI_MODEL", "gemini-3.8-flash")
    try:
        _, detected=google.auth.default()
        return {"authenticated":True,"auth_mode":"Vertex AI (ADC)","project":detected or project,"location":location,"model":model,"message":"Connected via Application Default Credentials (ADC)"}
    except Exception as exc:
        return {"authenticated":False,"auth_mode":"Vertex AI (ADC)","project":project,"location":location,"model":model,"message":f"ADC not detected: {exc}"}

def get_gemini_client():
    project=os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GCP_PROJECT_ID", "architecture-diagram-500204")
    location=os.environ.get("GCP_LOCATION", "us-central1")
    return genai.Client(vertexai=True, project=project, location=location)

def _generate(client, contents, config):
    last=None
    for model in _candidates():
        try: return client.models.generate_content(model=model, contents=contents, config=config)
        except Exception as exc:
            last=exc
            if any(x in str(exc).lower() for x in ("404","not_found","not found","model not available")): continue
            raise
    raise RuntimeError(f"No configured Gemini model was available: {last}")

def _provider(icon):
    if icon.startswith("aws-"): return "aws"
    if icon.startswith("azure-"): return "azure"
    if icon.startswith("gcp-"): return "gcp"
    return "generic"

def _scope(node):
    icon=node.get("data",{}).get("icon",""); label=node.get("data",{}).get("label","").lower()
    if icon in {"aws-s3","aws-cloudfront","gcp-gcs","gcp-bigquery","gcp-pubsub"} or "dynamodb" in label or "cloudwatch" in label: return "managed-service"
    if any(x in label for x in ("user","customer","employee")): return "internet"
    return "cloud"

def normalize_diagram(diagram, custom_icons=None):
    custom={i.get("tag") for i in (custom_icons or [])}; groups=diagram.get("groups",[]); gids={g.get("id") for g in groups}
    for g in groups:
        if g.get("parentId") not in gids: g["parentId"]=None
    for n in diagram.get("nodes",[]):
        d=n.setdefault("data",{}); cat=(d.get("category") or "general").lower(); d["category"]=cat; d["layer"]=CATEGORY_LAYER.get(cat,d.get("layer",4))
        icon=d.get("icon") or "server"; d["icon"]=icon if icon in VALID_ICONS or icon in custom else "server"; d.setdefault("provider",_provider(d["icon"])); d.setdefault("deploymentScope",_scope(n))
        if n.get("parentId") not in gids: n["parentId"]=None
    # remove empty boundaries while preserving hierarchy
    changed=True
    while changed:
        keep={n.get("parentId") for n in diagram.get("nodes",[]) if n.get("parentId")} | {g.get("parentId") for g in groups if g.get("parentId")}
        filtered=[g for g in groups if g.get("id") in keep]; changed=len(filtered)!=len(groups); groups=filtered
    diagram["groups"]=groups
    valid={n.get("id") for n in diagram.get("nodes",[])}; seen=set(); edges=[]
    for e in diagram.get("edges",[]):
        if e.get("source") not in valid or e.get("target") not in valid or e.get("source")==e.get("target"): continue
        d=e.setdefault("data",{}); d.setdefault("direction","forward"); d.setdefault("kind","sync"); protocol=d.get("protocol") or e.get("label") or ""; e["label"]=protocol
        key=(e.get("source"),e.get("target"),protocol,d.get("kind"))
        if key not in seen: seen.add(key); edges.append(e)
    diagram["edges"]=edges; diagram.setdefault("diagramType","architecture"); return diagram

def _context(custom_icons):
    if not custom_icons: return ""
    return "\nCustom organization icon tags:\n"+"\n".join(f"- {i['tag']}: {i['description']}" for i in custom_icons)

def _config(context):
    return types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT.format(custom_icons_context=context),response_mime_type="application/json",response_schema=DiagramSchema)

def generate_diagram(prompt, custom_icons=None):
    response=_generate(get_gemini_client(),f"Generate a professional enterprise architecture specification for:\n{prompt}",_config(_context(custom_icons)))
    return normalize_diagram(json.loads(response.text),custom_icons)

def refine_diagram(prompt,current_diagram,custom_icons=None):
    context=_context(custom_icons)
    instruction=SYSTEM_PROMPT.format(custom_icons_context=context)+"\nREFINEMENT: Preserve IDs of unchanged elements, preserve nested containment, remove obsolete edges and avoid duplicates.\nCurrent JSON:\n"+json.dumps(current_diagram,indent=2)
    config=types.GenerateContentConfig(system_instruction=instruction,response_mime_type="application/json",response_schema=DiagramSchema)
    response=_generate(get_gemini_client(),f"Apply this refinement: {prompt}",config)
    return normalize_diagram(json.loads(response.text),custom_icons)
