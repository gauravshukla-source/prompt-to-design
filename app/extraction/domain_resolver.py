from app.models.architecture import Domain, Element
from app.intelligence.domain_intelligence import DomainIntelligence

class DomainResolver:
    def __init__(self): self.engine=DomainIntelligence()
    def resolve(self,prompt:str,elements:list[Element])->tuple[list[Domain],list[Element]]:
        return self.engine.enrich(prompt,elements,[])
