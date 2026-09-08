from app.models.enums import RelationshipType
from app.models.architecture import Element, Relationship

class RelationshipExtractor:
    def _id(self, name: str) -> str:
        import re
        return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')

    def extract(self, prompt: str, elements: list[Element]) -> list[Relationship]:
        ids = {e.name.lower(): e.id for e in elements}
        def has(name): return name.lower() in ids
        rels: list[tuple[str,str,RelationshipType,str|None]] = []
        def add(a,b,t,label=None):
            if has(a) and has(b) and ids[a.lower()] != ids[b.lower()]:
                item=(ids[a.lower()],ids[b.lower()],t,label)
                if item not in rels: rels.append(item)

        # Common access path.
        add('Users','React Frontend',RelationshipType.API,'Access')
        add('Users','Web Application',RelationshipType.API,'Access')
        add('Users','Mobile Application',RelationshipType.API,'Access')
        add('Mobile Application','API Gateway',RelationshipType.API,'HTTPS')
        add('Web Application','API Gateway',RelationshipType.API,'HTTPS')
        add('React Frontend','Backend API',RelationshipType.API,'HTTPS')
        add('React Frontend','API Gateway',RelationshipType.API,'HTTPS')
        add('API Gateway','Backend Microservices',RelationshipType.API,'Route')
        add('Backend API','PostgreSQL Database',RelationshipType.DATA_ACCESS,'SQL')
        add('Backend API','Database',RelationshipType.DATA_ACCESS,'Data')
        add('Backend Microservices','Redis Cache',RelationshipType.DATA_ACCESS,'Cache')
        add('Backend Microservices','MongoDB Database',RelationshipType.DATA_ACCESS,'Data')
        add('Backend Microservices','Database',RelationshipType.DATA_ACCESS,'Data')
        add('On-Prem Application','VPN',RelationshipType.NETWORK,'Secure connection')
        add('VPN','Cloud API',RelationshipType.NETWORK,'VPN')
        add('Cloud API','Cloud Database',RelationshipType.DATA_ACCESS,'Data')
        add('Users','Active Directory',RelationshipType.AUTHENTICATION,'Authenticate')
        add('Active Directory','Microsoft Entra ID',RelationshipType.SYNC,'Sync')
        add('Microsoft Entra ID','Saviynt IGA',RelationshipType.PROVISIONING,'Governance')
        add('Saviynt IGA','Target Systems',RelationshipType.PROVISIONING,'Provision')
        add('Application','VPN',RelationshipType.NETWORK,'Secure connection')
        add('VPN','Backend API',RelationshipType.NETWORK,'VPN')
        add('VPN','Database',RelationshipType.NETWORK,'VPN')
        add('Users','Identity Provider',RelationshipType.AUTHENTICATION,'Authenticate')
        add('Identity Provider','Identity Governance',RelationshipType.PROVISIONING,'Governance')
        add('Identity Governance','Active Directory',RelationshipType.PROVISIONING,'Provision')
        add('Identity Governance','Privileged Access Management',RelationshipType.PROVISIONING,'Govern')

        # Event-driven patterns. Named services are connected through the broker.
        if 'kafka' in prompt.lower() or 'event' in prompt.lower():
            broker_id = ids.get('kafka') or ids.get('event broker')
            if broker_id:
                services = [e for e in elements if e.type.value == 'service']
                producer = next((e for e in services if 'order' in e.name.lower()), services[0] if services else None)
                if producer:
                    item=(producer.id, broker_id, RelationshipType.EVENT, 'Publish')
                    if item not in rels: rels.append(item)
                    for e in services:
                        if e.id != producer.id:
                            item=(broker_id, e.id, RelationshipType.EVENT, 'Consume')
                            if item not in rels: rels.append(item)

        return [Relationship(id=f'rel-{i+1}', source=s, target=t, type=typ, label=label)
                for i,(s,t,typ,label) in enumerate(rels)]
