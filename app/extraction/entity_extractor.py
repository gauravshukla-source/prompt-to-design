import re
from dataclasses import dataclass
from app.models.enums import ElementType

@dataclass
class ExtractedEntity:
    name: str
    type: ElementType
    technology: str | None = None
    provider: str | None = None


# Common typos and abbreviations normalization
NORMALIZATION_MAP = [
    (r'\bactive\s+directive\b|\bactive\s+directry\b', 'Active Directory'),
    (r'\bsaviynt\s+eic\b|\beic\b', 'Saviynt EIC'),
    (r'\bentra\s+id\b|\bmicrosoft\s+entra\b|\bazure\s+ad\b', 'Microsoft Entra ID'),
    (r'\bon[- ]prem(?:ises?)?\b', 'On-Premises System'),
    (r'\bk8s?\b', 'Kubernetes'),
    (r'\bpostgres\b', 'PostgreSQL'),
    (r'\bmongo\b', 'MongoDB'),
    (r'\bo365\b|\bm365\b', 'Microsoft 365'),
    (r'\baws\b', 'AWS Cloud'),
    (r'\bgcp\b', 'Google Cloud'),
]


class EntityExtractor:
    # Rich rules catalog ordered from specific technologies to broader components
    RULES = [
        # Users & Clients
        (r'\busers?|customers?|employees?|administrators?|admins?|clients?\b', 'Users', ElementType.USER, None),
        (r'\breact(?:\s+frontend)?\b|\bfrontend\b', 'React Frontend', ElementType.APPLICATION, 'React'),
        (r'\bmobile\s+(?:app|application)\b', 'Mobile Application', ElementType.APPLICATION, 'Mobile'),
        (r'\bweb\s+(?:app|application)\b', 'Web Application', ElementType.APPLICATION, 'Web'),

        # Identity & Access Management (Saviynt, Entra, AD, Okta, etc.)
        (r'\bsaviynt(?:\s+eic|\s+iga)?\b', 'Saviynt IGA', ElementType.IGA, 'Saviynt'),
        (r'\bactive\s+directory\b|\bactive\s+directive\b|\bad\b', 'Active Directory', ElementType.IDENTITY_SOURCE, 'Active Directory'),
        (r'\bentra(?:\s+id)?\b|\bmicrosoft\s+entra\b', 'Microsoft Entra ID', ElementType.IDENTITY_PROVIDER, 'Microsoft Entra ID'),
        (r'\bokta\b', 'Okta Identity Cloud', ElementType.IDENTITY_PROVIDER, 'Okta'),
        (r'\bcyberark\b', 'CyberArk PAM', ElementType.PAM, 'CyberArk'),
        (r'\bprivileged\s+access\s+management\b|\bpam\b', 'Privileged Access Management', ElementType.PAM, None),
        (r'\bidentity\s+governance\b|\biga\b', 'Identity Governance', ElementType.IGA, None),
        (r'\bidentity\s+provider\b|\bidp\b', 'Identity Provider', ElementType.IDENTITY_PROVIDER, None),
        (r'\bldap\b', 'LDAP Directory', ElementType.IDENTITY_SOURCE, 'LDAP'),
        (r'\bsaas\s+applications?\b|\btarget\s+systems?\b|\btarget\s+apps?\b', 'Target Systems', ElementType.TARGET_SYSTEM, 'SaaS'),

        # Integration, Gateways & Message Brokers
        (r'\bapi\s+gateway\b', 'API Gateway', ElementType.API_GATEWAY, None),
        (r'\bapigee\b', 'Apigee API Platform', ElementType.API_GATEWAY, 'Apigee'),
        (r'\bkafka\b|\bapache\s+kafka\b', 'Kafka Event Streaming', ElementType.MESSAGE_BROKER, 'Apache Kafka'),
        (r'\brabbitmq\b', 'RabbitMQ', ElementType.MESSAGE_BROKER, 'RabbitMQ'),
        (r'\bevent\s+broker\b|\bmessage\s+broker\b|\bmessage\s+queue\b', 'Event Broker', ElementType.MESSAGE_BROKER, None),
        (r'\bload\s+balancer\b|\balb\b|\bnlb\b', 'Load Balancer', ElementType.LOAD_BALANCER, None),

        # Security & Networking
        (r'\bweb\s+application\s+firewall\b|\bwaf\b', 'Web Application Firewall', ElementType.SECURITY, 'WAF'),
        (r'\bsite[- ]to[- ]site\s+vpn\b|\bvpn\b|\bvpn\s+gateway\b', 'VPN Gateway', ElementType.VPN, 'VPN'),
        (r'\bfirewall\b', 'Enterprise Firewall', ElementType.SECURITY, 'Firewall'),
        (r'\bzero\s+trust\b', 'Zero Trust Network Access', ElementType.SECURITY, 'Zero Trust'),

        # Compute & Microservices
        (r'\bkubernetes\b|\bk8s\b|\baks\b|\beks\b|\bgke\b', 'Kubernetes Cluster', ElementType.COMPUTE, 'Kubernetes'),
        (r'\bcloud\s+run\b', 'Cloud Run', ElementType.COMPUTE, 'Cloud Run'),
        (r'\blambda\b|\baws\s+lambda\b', 'AWS Lambda', ElementType.COMPUTE, 'AWS Lambda'),
        (r'\bbackend\s+microservices?\b|\bmicroservices?\b', 'Backend Microservices', ElementType.SERVICE, None),
        (r'\bbackend\s+api\b|\bcloud\s+apis?\b|\brest\s+api\b', 'Backend API', ElementType.API, 'REST API'),
        (r'\border\s+service\b', 'Order Service', ElementType.SERVICE, None),
        (r'\bpayment\s+service\b', 'Payment Service', ElementType.SERVICE, None),
        (r'\binventory\s+service\b', 'Inventory Service', ElementType.SERVICE, None),
        (r'\bnotification\s+service\b', 'Notification Service', ElementType.SERVICE, None),
        (r'\banalytics\s+service\b', 'Analytics Service', ElementType.SERVICE, None),
        (r'\bon[- ]prem(?:ise)?\s+applications?\b|\bon[- ]prem(?:ises?)?\b', 'On-Premises Application', ElementType.APPLICATION, 'On-Prem'),

        # Databases & Storage
        (r'\bpostgresql\b|\bpostgres\b', 'PostgreSQL Database', ElementType.DATABASE, 'PostgreSQL'),
        (r'\bmongodb\b|\bmongo\b', 'MongoDB Database', ElementType.DATABASE, 'MongoDB'),
        (r'\bredis\b|\bredis\s+cache\b', 'Redis Cache', ElementType.STORAGE, 'Redis'),
        (r'\bamazon\s+rds\b|\brds\b|\bcloud\s+database\b', 'Cloud Database', ElementType.DATABASE, 'Cloud SQL'),
        (r'\bdatabase\b|\bdb\b', 'Database', ElementType.DATABASE, None),
        (r'\bs3\b|\bblob\s+storage\b|\bcloud\s+storage\b', 'Object Storage', ElementType.STORAGE, 'S3'),
    ]

    def _normalize(self, text: str) -> str:
        res = text
        for pat, repl in NORMALIZATION_MAP:
            res = re.sub(pat, repl, res, flags=re.I)
        return res

    def extract(self, prompt: str) -> list[ExtractedEntity]:
        normalized = self._normalize(prompt)
        text = normalized.lower()
        found: list[ExtractedEntity] = []
        seen = set()

        for item in self.RULES:
            pattern, name, etype = item[0], item[1], item[2]
            tech = item[3] if len(item) > 3 else None
            if re.search(pattern, text, re.I):
                key = (name.lower(), etype.value)
                if key not in seen:
                    seen.add(key)
                    found.append(ExtractedEntity(name=name, type=etype, technology=tech))

        # Contextual recognition: If Saviynt/EIC is mentioned with on-prem, add Connector
        if any(x.name in ('Saviynt IGA', 'Active Directory') for x in found):
            if 'on-prem' in text or 'on premise' in text or 'active directory' in text or 'active directive' in text:
                if not any(x.name == 'Active Directory' for x in found):
                    found.append(ExtractedEntity(name='Active Directory', type=ElementType.IDENTITY_SOURCE, technology='Active Directory'))
                if not any(x.name == 'On-Prem Connector' for x in found):
                    found.append(ExtractedEntity(name='On-Prem Connector', type=ElementType.VPN, technology='Gateway'))
                if not any(x.name == 'Target Systems' for x in found):
                    found.append(ExtractedEntity(name='Target Systems', type=ElementType.TARGET_SYSTEM, technology='SaaS'))

        # If less than 2 entities found, extract capitalized noun phrases / keywords dynamically
        if len(found) < 2:
            words = [w.strip(',.:;"\'()[]') for w in prompt.split() if len(w) > 3]
            for w in words:
                if w.lower() not in ('create', 'architecture', 'diagram', 'where', 'integrates', 'with', 'from', 'into', 'connects', 'through'):
                    key = (w.lower(), 'service')
                    if key not in seen:
                        seen.add(key)
                        found.append(ExtractedEntity(name=w.capitalize(), type=ElementType.SERVICE, technology=w))
                if len(found) >= 3:
                    break

        # Architecture Synthesizer: If still under 3 components, intelligently complete the architecture
        if len(found) == 1:
            single = found[0]
            if single.type in (ElementType.IGA, ElementType.IDENTITY_PROVIDER, ElementType.IDENTITY_SOURCE):
                found.append(ExtractedEntity(name='Enterprise Users', type=ElementType.USER))
                found.append(ExtractedEntity(name='Target Systems', type=ElementType.TARGET_SYSTEM))
            elif single.type in (ElementType.DATABASE, ElementType.STORAGE):
                found.append(ExtractedEntity(name='Application Backend', type=ElementType.SERVICE))
                found.append(ExtractedEntity(name='API Gateway', type=ElementType.API_GATEWAY))
            else:
                found.append(ExtractedEntity(name='Client Application', type=ElementType.APPLICATION))
                found.append(ExtractedEntity(name='Backend API', type=ElementType.API))

        if len(found) == 0:
            found = [
                ExtractedEntity(name='Client Application', type=ElementType.APPLICATION),
                ExtractedEntity(name='API Gateway', type=ElementType.API_GATEWAY),
                ExtractedEntity(name='Core Service', type=ElementType.SERVICE),
                ExtractedEntity(name='Enterprise Database', type=ElementType.DATABASE),
            ]

        return found
