from app.models.architecture import (
    ArchitectureMeta, CanonicalArchitectureModel, Domain, Element, Relationship, Flow
)
from app.models.enums import (
    ArchitectureType, DomainType, ElementType, RelationshipType, FlowType
)
from .intent_agent import IntentResult

class ArchitectAgent:
    def build(self, prompt: str, intent: IntentResult) -> CanonicalArchitectureModel:
        atype = intent.architecture_type
        architecture = ArchitectureMeta(
            id="arch-001",
            name=f"{atype.value.replace('_', ' ').title()} Architecture",
            type=atype,
            viewpoint=intent.viewpoint,
            description=prompt,
        )

        if atype == ArchitectureType.HYBRID_CLOUD:
            return CanonicalArchitectureModel(
                architecture=architecture,
                domains=[
                    Domain(id="onprem", name="On-Premises", type=DomainType.ON_PREMISES),
                    Domain(id="cloud", name="Cloud", type=DomainType.CLOUD),
                ],
                elements=[
                    Element(id="onprem-app", name="On-Prem Application", type=ElementType.APPLICATION, domain_id="onprem"),
                    Element(id="vpn", name="VPN Connection", type=ElementType.VPN),
                    Element(id="api", name="Cloud API", type=ElementType.API, domain_id="cloud"),
                    Element(id="database", name="Cloud Database", type=ElementType.DATABASE, domain_id="cloud"),
                ],
                relationships=[
                    Relationship(id="r1", source="onprem-app", target="vpn", type=RelationshipType.NETWORK, label="Secure tunnel"),
                    Relationship(id="r2", source="vpn", target="api", type=RelationshipType.NETWORK, label="VPN"),
                    Relationship(id="r3", source="api", target="database", type=RelationshipType.DATA_ACCESS),
                ],
                flows=[
                    Flow(id="primary", name="Secure application flow", type=FlowType.PRIMARY,
                         steps=["onprem-app", "vpn", "api", "database"], primary=True)
                ],
            )

        if atype == ArchitectureType.IAM:
            return CanonicalArchitectureModel(
                architecture=architecture,
                domains=[
                    Domain(id="identity", name="Identity & Governance", type=DomainType.LOGICAL),
                    Domain(id="target-systems-domain", name="Target Systems", type=DomainType.LOGICAL),
                ],
                elements=[
                    Element(id="users", name="Users", type=ElementType.USER),
                    Element(id="identity-source", name="Identity Source", type=ElementType.IDENTITY_SOURCE, domain_id="identity"),
                    Element(id="idp", name="Identity Provider", type=ElementType.IDENTITY_PROVIDER, domain_id="identity"),
                    Element(id="iga", name="IGA Platform", type=ElementType.IGA, domain_id="identity"),
                    Element(id="targets", name="Target Systems", type=ElementType.TARGET_SYSTEM, domain_id="target-systems-domain"),
                ],
                relationships=[
                    Relationship(id="r1", source="users", target="identity-source", type=RelationshipType.AUTHENTICATION),
                    Relationship(id="r2", source="identity-source", target="idp", type=RelationshipType.SYNC),
                    Relationship(id="r3", source="idp", target="iga", type=RelationshipType.PROVISIONING),
                    Relationship(id="r4", source="iga", target="targets", type=RelationshipType.PROVISIONING),
                ],
                flows=[
                    Flow(id="primary", name="Identity governance flow", type=FlowType.PRIMARY,
                         steps=["users", "identity-source", "idp", "iga", "targets"], primary=True)
                ],
            )

        if atype == ArchitectureType.EVENT_DRIVEN:
            return CanonicalArchitectureModel(
                architecture=architecture,
                elements=[
                    Element(id="producer", name="Producer Service", type=ElementType.SERVICE),
                    Element(id="broker", name="Event Broker", type=ElementType.MESSAGE_BROKER),
                    Element(id="consumer-a", name="Consumer Service A", type=ElementType.SERVICE),
                    Element(id="consumer-b", name="Consumer Service B", type=ElementType.SERVICE),
                ],
                relationships=[
                    Relationship(id="r1", source="producer", target="broker", type=RelationshipType.EVENT, label="Publish"),
                    Relationship(id="r2", source="broker", target="consumer-a", type=RelationshipType.EVENT, label="Consume"),
                    Relationship(id="r3", source="broker", target="consumer-b", type=RelationshipType.EVENT, label="Consume"),
                ],
                flows=[
                    Flow(id="primary", name="Event flow", type=FlowType.EVENT,
                         steps=["producer", "broker", "consumer-a"], primary=True)
                ],
            )

        return CanonicalArchitectureModel(
            architecture=architecture,
            elements=[
                Element(id="source", name="Source", type=ElementType.APPLICATION),
                Element(id="target", name="Target", type=ElementType.APPLICATION),
            ],
            relationships=[
                Relationship(id="r1", source="source", target="target", type=RelationshipType.GENERIC)
            ],
            flows=[
                Flow(id="primary", name="Primary flow", steps=["source", "target"], primary=True)
            ],
        )
