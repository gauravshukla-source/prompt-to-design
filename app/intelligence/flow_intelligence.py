from app.models.architecture import Relationship
from app.models.enterprise import FlowMetadata

class FlowIntelligence:
    SECURITY={
        'HTTPS':'TLS','HTTP':'TLS','VPN':'Encrypted Tunnel','SQL':'Database Access',
        'SAML':'Federated Authentication','OAuth 2.0':'Token Security','SCIM':'Provisioning'
    }
    def enrich(self,relationships:list[Relationship]):
        out=[]
        for r in relationships:
            protocol=r.protocol or r.label
            out.append(FlowMetadata(
                relationship_id=r.id, flow_type=r.type.value, protocol=protocol,
                security=self.SECURITY.get(protocol or ''), direction=r.direction,
            ))
        return out
