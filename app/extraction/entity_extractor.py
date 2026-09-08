import re
from dataclasses import dataclass
from app.models.enums import ElementType

@dataclass
class ExtractedEntity:
    name: str
    type: ElementType
    technology: str | None = None

class EntityExtractor:
    # Ordered from specific technologies/concepts to generic concepts.
    RULES = [
        (r'\busers?|customers?|employees?|administrators?|admins?\b', 'Users', ElementType.USER),
        (r'\bon-prem applications?\b', 'On-Prem Application', ElementType.APPLICATION),
        (r'\bcloud apis?\b', 'Cloud API', ElementType.API),
        (r'\bcloud databases?\b', 'Cloud Database', ElementType.DATABASE),
        (r'\bentra id\b|\bmicrosoft entra\b', 'Microsoft Entra ID', ElementType.IDENTITY_PROVIDER),
        (r'\bsaviynt\b', 'Saviynt IGA', ElementType.IGA),
        (r'\bsaas applications?\b|\btarget systems?\b', 'Target Systems', ElementType.TARGET_SYSTEM),
        (r'\border service\b', 'Order Service', ElementType.SERVICE),
        (r'\bpayment(?:\s+and\s+inventory)?(?:\s+service|\s+services)?\b', 'Payment Service', ElementType.SERVICE),
        (r'\binventory(?:\s+service|\s+services)?\b', 'Inventory Service', ElementType.SERVICE),
        (r'\bnotification service\b', 'Notification Service', ElementType.SERVICE),
        (r'\banalytics service\b', 'Analytics Service', ElementType.SERVICE),
        (r'\breact(?:\s+frontend)?\b|\bfrontend\b', 'React Frontend', ElementType.APPLICATION),
        (r'\bmobile application\b|\bmobile app\b', 'Mobile Application', ElementType.APPLICATION),
        (r'\bweb application\b|\bweb app\b', 'Web Application', ElementType.APPLICATION),
        (r'\bapi gateway\b', 'API Gateway', ElementType.API_GATEWAY),
        (r'\bbackend microservices?\b|\bmicroservices?\b', 'Backend Microservices', ElementType.SERVICE),
        (r'\bbackend api\b', 'Backend API', ElementType.API),
        (r'\bpostgresql\b|\bpostgres\b', 'PostgreSQL Database', ElementType.DATABASE),
        (r'\bmongodb\b|\bmongo\b', 'MongoDB Database', ElementType.DATABASE),
        (r'\bredis\b', 'Redis Cache', ElementType.STORAGE),
        (r'\bkafka\b', 'Kafka', ElementType.MESSAGE_BROKER),
        (r'\bevent broker\b|\bmessage broker\b', 'Event Broker', ElementType.MESSAGE_BROKER),
        (r'\bidentity provider\b|\bidp\b', 'Identity Provider', ElementType.IDENTITY_PROVIDER),
        (r'\bactive directory\b|\bad\b', 'Active Directory', ElementType.IDENTITY_SOURCE),
        (r'\bidentity governance\b|\biga\b', 'Identity Governance', ElementType.IGA),
        (r'\bprivileged access management\b|\bpam\b', 'Privileged Access Management', ElementType.PAM),
        (r'\bsite[- ]to[- ]site vpn\b|\bvpn\b', 'VPN', ElementType.VPN),
        (r'\bweb application firewall\b|\bwaf\b', 'Web Application Firewall', ElementType.SECURITY),
        (r'\bload balancer\b|\bload balancing\b', 'Load Balancer', ElementType.LOAD_BALANCER),
        (r'\bdatabase\b', 'Database', ElementType.DATABASE),
        (r'\bapplication(?:s)?\b', 'Application', ElementType.APPLICATION),
        (r'\bservice(?:s)?\b', 'Service', ElementType.SERVICE),
    ]

    def extract(self, prompt: str) -> list[ExtractedEntity]:
        text = prompt.lower()
        found: list[ExtractedEntity] = []
        seen = set()
        for pattern, name, etype in self.RULES:
            if re.search(pattern, text, re.I):
                key = (name.lower(), etype.value)
                if key not in seen:
                    seen.add(key)
                    found.append(ExtractedEntity(name=name, type=etype))
        # AWS is a deployment domain by default, not an application component.
        # In IAM prompts AWS can represent a governed target estate.
        if ('aws' in text and any(x in text for x in ['saviynt', 'identity governance', 'iga', 'provision'])):
            if not any(x.name == 'Target Systems' for x in found):
                found.append(ExtractedEntity(name='Target Systems', type=ElementType.TARGET_SYSTEM))
        # Contextual cloud concepts such as 'cloud APIs and databases'.
        current_names={x.name for x in found}
        if 'cloud' in text and re.search(r'\bapis?\b', text) and 'Cloud API' not in current_names:
            found.append(ExtractedEntity(name='Cloud API', type=ElementType.API))
        if 'cloud' in text and re.search(r'\bdatabases?\b', text) and 'Cloud Database' not in current_names:
            found.append(ExtractedEntity(name='Cloud Database', type=ElementType.DATABASE))
        names={x.name for x in found}
        # Suppress broad fallback concepts when a more specific component is present.
        if 'Application' in names and any(x.type == ElementType.APPLICATION and x.name != 'Application' for x in found):
            found=[x for x in found if x.name != 'Application']
        if 'React Frontend' in {x.name for x in found} and 'Web Application' in {x.name for x in found}:
            found=[x for x in found if x.name != 'Web Application']
        if 'Database' in names and any(x.type == ElementType.DATABASE and x.name != 'Database' for x in found):
            found=[x for x in found if x.name != 'Database']
        if 'Service' in names and any(x.type == ElementType.SERVICE and x.name != 'Service' for x in found):
            found=[x for x in found if x.name != 'Service']
        return found
