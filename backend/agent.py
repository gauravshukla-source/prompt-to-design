"""Enterprise Architecture Engine 3.0 semantic compiler.
Vertex AI + ADC only. Gemini produces architecture intent and model; browser compiles notation/layout.
"""
import os,json
from typing import List,Optional
from pydantic import BaseModel,Field
from google import genai
from google.genai import types
import google.auth

class Domain(BaseModel):
    id:str; label:str; type:str='enterprise'; members:List[str]=Field(default_factory=list)
class Boundary(BaseModel):
    id:str; label:str; type:str='boundary'; members:List[str]=Field(default_factory=list); parentId:Optional[str]=None
class NodeData(BaseModel):
    label:str; icon:Optional[str]=None; category:Optional[str]='general'; description:Optional[str]=None
    provider:Optional[str]='generic'; domain:Optional[str]=None; role:Optional[str]=None; visualType:Optional[str]=None
    peerGroup:Optional[str]=None; importance:Optional[str]='normal'; layer:Optional[int]=None
class Node(BaseModel):
    id:str; type:str='component'; parentId:Optional[str]=None; data:NodeData
class EdgeData(BaseModel):
    protocol:Optional[str]=None; direction:Optional[str]='forward'; kind:Optional[str]='sync'; encrypted:Optional[bool]=None
class Edge(BaseModel):
    id:str; source:str; target:str; label:Optional[str]=None; data:EdgeData=Field(default_factory=EdgeData)
class Group(BaseModel):
    id:str; label:str; type:str='boundary'; parentId:Optional[str]=None; members:List[str]=Field(default_factory=list)
class DiagramSchema(BaseModel):
    diagramType:str='architecture'; title:str='Enterprise Architecture'; architectureType:str='generic'; viewpoint:str='logical'; pattern:str='generic'
    domains:List[Domain]=Field(default_factory=list); boundaries:List[Boundary]=Field(default_factory=list); layers:List[str]=Field(default_factory=list)
    groups:List[Group]=Field(default_factory=list); nodes:List[Node]=Field(default_factory=list); edges:List[Edge]=Field(default_factory=list); legend:List[str]=Field(default_factory=list)

APPROVED='''AWS: aws-api-gateway aws-rds aws-ecs aws-s3 aws-lambda aws-ec2 aws-alb aws-cloudfront
Azure: azure-sql azure-app-service azure-vm azure-api-management azure-active-directory azure-functions azure-service-bus
GCP: gcp-cloud-run gcp-gcs gcp-bigquery gcp-pubsub
Identity: active-directory azure-active-directory okta ldap saviynt-iga microsoft-graph
Infra: kubernetes load-balancer firewall router dns database server client user cog kafka rabbitmq'''
SYSTEM_PROMPT=f'''
You are a principal Enterprise Architect and architecture documentation specialist.
You are NOT a flowchart generator. Build an enterprise architecture MODEL that can be compiled into a professional diagram.
Follow these architecture principles: select one viewpoint appropriate to the audience; use clear boundaries for ownership/deployment/trust/network scope; directional relationships; concise labels; progressive disclosure; do not overload the view.

STEP 1 classify architectureType: cloud, hybrid_cloud, application, data, identity, security, network, integration, enterprise, generic.
STEP 2 select viewpoint: context, logical, container, deployment, security. Never mix deployment topology and logical abstraction unless explicitly requested.
STEP 3 identify domains and boundaries. Boundaries are only real ownership, cloud, network, trust, deployment or organizational scopes. Never create decorative/empty boxes.
STEP 4 identify components and assign role, visualType and layer. visualType is actor, component, datastore, event, external or security.
STEP 5 relationships are directional. kind is sync, async, auth, data, control or security. Prefer one-way arrows; model request/response as separate edges only when useful.
STEP 6 choose pattern: iam, microservices, event_driven, data_pipeline, three_tier, zero_trust, hybrid_cloud, generic.

Important: For context diagrams, show people and systems, not infrastructure/protocol clutter. For logical/container diagrams, show responsibilities and technology choices but avoid deployment-only detail. For deployment diagrams, show nested cloud/network/deployment boundaries and infrastructure nodes. For security diagrams, make trust/security boundaries and controls explicit.

Use 5-18 nodes. Do not invent infrastructure. Collapse repeated peers into peerGroup. Do not connect peers sequentially unless required.
Use official provider/service names and icon slugs only when a technology is explicitly identified. Approved slugs:\n{APPROVED}
Return only JSON conforming to the schema.
'''

def check_auth_status():
    project=os.getenv('GOOGLE_CLOUD_PROJECT') or os.getenv('GCP_PROJECT_ID','architecture-diagram-500204'); location=os.getenv('GCP_LOCATION','global'); model=os.getenv('GEMINI_MODEL','gemini-3.8-flash')
    try:
        _,resolved=google.auth.default();return {'authenticated':True,'auth_mode':'Vertex AI (ADC)','project':resolved or project,'location':location,'model':model,'message':'Connected via ADC'}
    except Exception as e:return {'authenticated':False,'auth_mode':'Vertex AI (ADC)','project':project,'location':location,'model':model,'message':f'ADC not detected: {e}'}

def get_gemini_client():
    project=os.getenv('GOOGLE_CLOUD_PROJECT') or os.getenv('GCP_PROJECT_ID','architecture-diagram-500204');location=os.getenv('GCP_LOCATION','global')
    return genai.Client(vertexai=True,project=project,location=location)

def generate_with_fallback(client,contents,config):
    preferred=os.getenv('GEMINI_MODEL','gemini-3.8-flash');models=[]
    for m in [preferred,'gemini-3.8-flash','gemini-3.7-flash','gemini-3.6-flash']:
        if m not in models:models.append(m)
    last=None
    for m in models:
        try:return client.models.generate_content(model=m,contents=contents,config=config)
        except Exception as e:last=e
    raise RuntimeError(f'No configured Gemini model succeeded: {last}')

def _infer_role(text):
    t=text.lower()
    if any(x in t for x in ['employee','user','customer','admin','browser']):return'external_actor','actor'
    if any(x in t for x in ['active directory','ldap','hr source']):return'identity_source','component'
    if any(x in t for x in ['entra','okta','identity provider','idp']):return'identity_provider','component'
    if any(x in t for x in ['saviynt','sailpoint','identity governance','iga']):return'primary_component','component'
    if any(x in t for x in ['firewall','waf','security control']):return'security_control','security'
    if any(x in t for x in ['api gateway','ingress','cloudfront']):return'edge_entry','component'
    if any(x in t for x in ['load balancer','alb','router']):return'traffic_router','component'
    if any(x in t for x in ['kafka','rabbitmq','pubsub','service bus','event bus']):return'event_backbone','event'
    if any(x in t for x in ['database','rds','sql','postgres','mysql','warehouse','storage','s3','gcs']):return'data_store','datastore'
    if any(x in t for x in ['salesforce','servicenow','workday','saas']):return'target_application','external'
    return'peer_service','component'

def normalize_diagram(diagram):
    diagram.setdefault('domains',[]);diagram.setdefault('boundaries',[]);diagram.setdefault('groups',[]);diagram.setdefault('nodes',[]);diagram.setdefault('edges',[]);diagram.setdefault('legend',[])
    # Canonicalize nodes and semantic notation.
    for n in diagram['nodes']:
        d=n.setdefault('data',{});d['label']=str(d.get('label') or n.get('id') or 'Component');text=d['label']+' '+str(d.get('description',''))+' '+str(d.get('icon',''))
        inferred,visual=_infer_role(text);d['role']=d.get('role') or inferred;d['visualType']=d.get('visualType') or visual;d['importance']='primary' if d['role']=='primary_component' else d.get('importance','normal')
        d['peerGroup']=d.get('peerGroup') or ('target_systems' if d['role']=='target_application' else 'services' if d['role']=='peer_service' else '')
        if d.get('layer') is None:d['layer']={'external_actor':0,'identity_source':1,'identity_provider':2,'edge_entry':1,'traffic_router':2,'primary_component':3,'peer_service':3,'event_backbone':3,'data_store':4,'target_application':4}.get(d['role'],2)
    ids={n['id'] for n in diagram['nodes']};seen=set();clean=[]
    for e in diagram['edges']:
        if e.get('source') not in ids or e.get('target') not in ids or e.get('source')==e.get('target'):continue
        ed=e.setdefault('data',{});ed['kind']=ed.get('kind','sync');ed['direction']=ed.get('direction','forward');e['label']=str(e.get('label') or ed.get('protocol') or '').strip();key=(e['source'],e['target'],e['label'],ed['kind'])
        if key not in seen:seen.add(key);clean.append(e)
    diagram['edges']=clean
    # Remove empty boundaries before renderer sees them.
    for collection in ['groups','boundaries','domains']:
        kept=[]
        for x in diagram[collection]:
            members=set(x.get('members') or x.get('nodeIds') or [])
            if collection=='groups':members.update(n['id'] for n in diagram['nodes'] if n.get('parentId')==x.get('id'))
            if members:kept.append(x)
        diagram[collection]=kept
    return diagram

def generate_diagram(prompt:str,custom_icons:list=None):
    client=get_gemini_client();cfg=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT,response_mime_type='application/json',response_schema=DiagramSchema)
    response=generate_with_fallback(client,f'Analyze and design this enterprise architecture:\n{prompt}',cfg)
    return normalize_diagram(json.loads(response.text))

def refine_diagram(prompt:str,current_diagram:dict,custom_icons:list=None):
    client=get_gemini_client();instruction=SYSTEM_PROMPT+'\nPreserve unchanged IDs and architecture intent. Current model:\n'+json.dumps(current_diagram)+'\nRequested change:\n'+prompt
    cfg=types.GenerateContentConfig(system_instruction=instruction,response_mime_type='application/json',response_schema=DiagramSchema)
    response=generate_with_fallback(client,'Return the revised enterprise architecture model.',cfg)
    return normalize_diagram(json.loads(response.text))
