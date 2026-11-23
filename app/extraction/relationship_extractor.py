from app.models.enums import RelationshipType, ElementType
from app.models.architecture import Element, Relationship

LAYER_TIER = {
    ElementType.USER: 0,
    ElementType.APPLICATION: 0,
    ElementType.LOAD_BALANCER: 1,
    ElementType.SECURITY: 1,
    ElementType.VPN: 1,
    ElementType.CONNECTIVITY: 1,
    ElementType.API_GATEWAY: 2,
    ElementType.IGA: 2,
    ElementType.PAM: 2,
    ElementType.IDENTITY_PROVIDER: 2,
    ElementType.SERVICE: 3,
    ElementType.COMPUTE: 3,
    ElementType.API: 3,
    ElementType.MESSAGE_BROKER: 3,
    ElementType.DATABASE: 4,
    ElementType.STORAGE: 4,
    ElementType.IDENTITY_SOURCE: 4,
    ElementType.TARGET_SYSTEM: 4,
    ElementType.GENERIC: 3,
}

PROTOCOL_MAP = {
    ElementType.DATABASE: ('SQL', RelationshipType.DATA_ACCESS),
    ElementType.STORAGE: ('S3/Blob', RelationshipType.DATA_ACCESS),
    ElementType.IDENTITY_SOURCE: ('LDAPS', RelationshipType.PROVISIONING),
    ElementType.TARGET_SYSTEM: ('SCIM/REST', RelationshipType.PROVISIONING),
    ElementType.MESSAGE_BROKER: ('AMQP/Event', RelationshipType.EVENT),
    ElementType.API: ('REST/JSON', RelationshipType.API),
    ElementType.API_GATEWAY: ('HTTPS', RelationshipType.NETWORK),
    ElementType.VPN: ('IPsec/TLS', RelationshipType.NETWORK),
    ElementType.IDENTITY_PROVIDER: ('SAML/OIDC', RelationshipType.AUTHENTICATION),
    ElementType.IGA: ('Governance', RelationshipType.PROVISIONING),
}


class RelationshipExtractor:
    def extract(self, prompt: str, elements: list[Element]) -> list[Relationship]:
        if not elements or len(elements) < 2:
            return []

        ids = {e.name.lower(): e.id for e in elements}
        by_id = {e.id: e for e in elements}

        def has(name: str) -> bool:
            return name.lower() in ids

        rels: list[tuple[str, str, RelationshipType, str | None]] = []

        def add(a: str, b: str, t: RelationshipType, label: str | None = None):
            if has(a) and has(b) and ids[a.lower()] != ids[b.lower()]:
                item = (ids[a.lower()], ids[b.lower()], t, label)
                if item not in rels:
                    rels.append(item)

        # ── Known Enterprise & IAM Patterns ─────────────────────────
        # Saviynt & Identity integrations
        add('Users', 'Saviynt IGA', RelationshipType.AUTHENTICATION, 'Access')
        add('Users', 'Active Directory', RelationshipType.AUTHENTICATION, 'Authenticate')
        add('Users', 'Microsoft Entra ID', RelationshipType.AUTHENTICATION, 'SSO / MFA')
        add('Users', 'Okta Identity Cloud', RelationshipType.AUTHENTICATION, 'SSO')
        add('Active Directory', 'Microsoft Entra ID', RelationshipType.SYNC, 'DirSync')
        add('Microsoft Entra ID', 'Saviynt IGA', RelationshipType.PROVISIONING, 'Governance')
        add('Saviynt IGA', 'On-Prem Connector', RelationshipType.NETWORK, 'Secure Channel')
        add('On-Prem Connector', 'Active Directory', RelationshipType.PROVISIONING, 'LDAPS Sync')
        add('Saviynt IGA', 'Active Directory', RelationshipType.PROVISIONING, 'Manage / Provision')
        add('Saviynt IGA', 'Target Systems', RelationshipType.PROVISIONING, 'SCIM Provision')
        add('Saviynt IGA', 'CyberArk PAM', RelationshipType.PROVISIONING, 'PAM Governance')
        add('Identity Provider', 'Identity Governance', RelationshipType.PROVISIONING, 'Governance')
        add('Identity Governance', 'Active Directory', RelationshipType.PROVISIONING, 'Provision')
        add('Identity Governance', 'Privileged Access Management', RelationshipType.PROVISIONING, 'Govern')

        # Web & Microservices patterns
        add('Users', 'React Frontend', RelationshipType.API, 'HTTPS')
        add('Users', 'Web Application', RelationshipType.API, 'HTTPS')
        add('Users', 'Mobile Application', RelationshipType.API, 'HTTPS')
        add('React Frontend', 'API Gateway', RelationshipType.API, 'REST')
        add('React Frontend', 'Backend API', RelationshipType.API, 'REST')
        add('Mobile Application', 'API Gateway', RelationshipType.API, 'REST')
        add('Web Application', 'API Gateway', RelationshipType.API, 'REST')
        add('API Gateway', 'Backend Microservices', RelationshipType.API, 'Route')
        add('Backend Microservices', 'PostgreSQL Database', RelationshipType.DATA_ACCESS, 'SQL')
        add('Backend Microservices', 'MongoDB Database', RelationshipType.DATA_ACCESS, 'NoSQL')
        add('Backend Microservices', 'Redis Cache', RelationshipType.DATA_ACCESS, 'Cache')
        add('Backend API', 'PostgreSQL Database', RelationshipType.DATA_ACCESS, 'SQL')
        add('Backend API', 'Cloud Database', RelationshipType.DATA_ACCESS, 'SQL')
        add('Backend API', 'Database', RelationshipType.DATA_ACCESS, 'SQL')
        add('On-Premises Application', 'VPN Gateway', RelationshipType.NETWORK, 'Secure Tunnel')
        add('VPN Gateway', 'Backend API', RelationshipType.NETWORK, 'VPN')
        add('VPN Gateway', 'Cloud Database', RelationshipType.DATA_ACCESS, 'Direct')

        # Event-driven pattern
        if any(e.type == ElementType.MESSAGE_BROKER for e in elements):
            broker = next(e for e in elements if e.type == ElementType.MESSAGE_BROKER)
            services = [e for e in elements if e.id != broker.id and e.type in (ElementType.SERVICE, ElementType.APPLICATION, ElementType.COMPUTE)]
            if services:
                # First service publishes, others consume
                add(services[0].name, broker.name, RelationshipType.EVENT, 'Publish')
                for s in services[1:]:
                    add(broker.name, s.name, RelationshipType.EVENT, 'Consume')

        # ── Universal Topological Connector (Fallback & Gap Filler) ─
        # Ensure all elements have at least one incoming or outgoing edge
        connected = {r[0] for r in rels} | {r[1] for r in rels}
        unconnected = [e for e in elements if e.id not in connected]

        # If zero relations were created or some elements are disconnected,
        # sort elements by architectural tier and link them sequentially
        sorted_elements = sorted(
            elements,
            key=lambda e: (LAYER_TIER.get(e.type, 3), e.name)
        )

        if not rels and len(sorted_elements) >= 2:
            for i in range(len(sorted_elements) - 1):
                src = sorted_elements[i]
                tgt = sorted_elements[i + 1]
                proto, rtype = PROTOCOL_MAP.get(tgt.type, ('REST/HTTPS', RelationshipType.API))
                rels.append((src.id, tgt.id, rtype, proto))

        elif unconnected:
            # Connect each unconnected element to its closest logical neighbor
            for unconn in unconnected:
                unconn_tier = LAYER_TIER.get(unconn.type, 3)
                # Find potential source with lower or equal tier
                candidates_src = [e for e in elements if e.id != unconn.id and LAYER_TIER.get(e.type, 3) <= unconn_tier]
                candidates_tgt = [e for e in elements if e.id != unconn.id and LAYER_TIER.get(e.type, 3) >= unconn_tier]

                if candidates_src:
                    src = candidates_src[-1]
                    proto, rtype = PROTOCOL_MAP.get(unconn.type, ('HTTPS', RelationshipType.GENERIC))
                    item = (src.id, unconn.id, rtype, proto)
                    if item not in rels:
                        rels.append(item)
                elif candidates_tgt:
                    tgt = candidates_tgt[0]
                    proto, rtype = PROTOCOL_MAP.get(tgt.type, ('HTTPS', RelationshipType.GENERIC))
                    item = (unconn.id, tgt.id, rtype, proto)
                    if item not in rels:
                        rels.append(item)

        return [
            Relationship(id=f'rel-{i + 1}', source=s, target=t, type=typ, label=label)
            for i, (s, t, typ, label) in enumerate(rels)
        ]
