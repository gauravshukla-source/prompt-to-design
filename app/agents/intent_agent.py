from dataclasses import dataclass
from app.models.enums import ArchitectureType, Viewpoint

@dataclass
class IntentResult:
    architecture_type: ArchitectureType
    viewpoint: Viewpoint
    complexity: str
    required_concepts: list[str]
    excluded_concepts: list[str]
    primary_goal: str

class IntentAgent:
    def analyze(self, prompt: str) -> IntentResult:
        p = prompt.lower()

        if any(x in p for x in [
            "active directory", "active directive", "entra", "saviynt", "eic",
            "identity", "iga", "pam", "okta", "ldap", "cyberark", "sso", "scim",
            "provision", "governance", "directory"
        ]):
            architecture_type = ArchitectureType.IAM
            viewpoint = Viewpoint.IAM
            concepts = ["user", "identity", "target_system"]
        elif any(x in p for x in ["zero trust", "firewall", "siem", "security", "waf"]):
            architecture_type = ArchitectureType.SECURITY
            viewpoint = Viewpoint.SECURITY
            concepts = ["user", "security", "application"]
        elif any(x in p for x in ["kafka", "event", "publish", "consume", "broker", "rabbitmq"]):
            architecture_type = ArchitectureType.EVENT_DRIVEN
            viewpoint = Viewpoint.INTEGRATION
            concepts = ["producer", "broker", "consumer"]
        elif any(x in p for x in ["microservice", "microservices", "kubernetes", "k8s", "container"]):
            architecture_type = ArchitectureType.MICROSERVICES
            viewpoint = Viewpoint.DEPLOYMENT
            concepts = ["client", "gateway", "service"]
        elif any(x in p for x in ["vpn", "on-prem", "on premise", "on-premises", "hybrid cloud", "expressroute"]):
            architecture_type = ArchitectureType.HYBRID_CLOUD
            viewpoint = Viewpoint.DEPLOYMENT
            concepts = ["on_premises", "vpn", "cloud"]
        elif any(x in p for x in ["aws", "azure", "gcp", "cloud"]):
            architecture_type = ArchitectureType.CLOUD
            viewpoint = Viewpoint.DEPLOYMENT
            concepts = ["cloud", "application"]
        else:
            architecture_type = ArchitectureType.GENERIC
            viewpoint = Viewpoint.CONCEPTUAL
            concepts = []

        complexity = "simple" if len(prompt.split()) < 25 else "medium"
        return IntentResult(
            architecture_type=architecture_type,
            viewpoint=viewpoint,
            complexity=complexity,
            required_concepts=concepts,
            excluded_concepts=[],
            primary_goal="Generate an enterprise architecture that models the systems and interactions described in the prompt.",
        )
