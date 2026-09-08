from dataclasses import dataclass
from app.models.architecture import CanonicalArchitectureModel

@dataclass
class CoverageResult:
    expected: list[str]
    matched: list[str]
    missing: list[str]
    score: float

class PromptCoverage:
    CONCEPTS = {
        'react': ['React Frontend'], 'frontend': ['React Frontend'],
        'backend api': ['Backend API'], 'postgresql': ['PostgreSQL Database'],
        'mobile application': ['Mobile Application'], 'web application': ['Web Application'],
        'api gateway': ['API Gateway'], 'microservice': ['Backend Microservices'],
        'redis': ['Redis Cache'], 'mongodb': ['MongoDB Database'],
        'saviynt': ['Saviynt IGA'], 'entra id': ['Microsoft Entra ID'], 'cloud api': ['Cloud API'], 'cloud databases': ['Cloud Database'], 'on-prem applications': ['On-Prem Application'], 'kafka': ['Kafka'], 'vpn': ['VPN'], 'identity provider': ['Identity Provider'],
        'active directory': ['Active Directory'], 'identity governance': ['Identity Governance'],
        'iga': ['Identity Governance'], 'pam': ['Privileged Access Management'],
    }
    def evaluate(self, prompt: str, model: CanonicalArchitectureModel) -> CoverageResult:
        text=prompt.lower(); names={e.name.lower() for e in model.elements}
        expected=[]; matched=[]; missing=[]
        for keyword, targets in self.CONCEPTS.items():
            if keyword in text:
                for target in targets:
                    if target not in expected: expected.append(target)
                    if target.lower() in names: matched.append(target)
                    else: missing.append(target)
        score=100.0 if not expected else round(100*len(set(matched))/len(set(expected)),2)
        return CoverageResult(expected=expected, matched=matched, missing=missing, score=score)
