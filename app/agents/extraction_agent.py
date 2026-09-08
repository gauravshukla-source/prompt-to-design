import re
from app.models.architecture import ArchitectureMeta, CanonicalArchitectureModel, Element
from app.models.enums import ArchitectureType, ElementType
from app.extraction.entity_extractor import EntityExtractor
from app.extraction.relationship_extractor import RelationshipExtractor
from app.extraction.domain_resolver import DomainResolver
from app.extraction.flow_builder import FlowBuilder
from .intent_agent import IntentResult

class ArchitectureExtractionError(ValueError):
    pass

class ExtractionAgent:
    def __init__(self):
        self.entities=EntityExtractor(); self.relationships=RelationshipExtractor(); self.domains=DomainResolver(); self.flows=FlowBuilder()

    @staticmethod
    def _slug(value: str) -> str:
        return re.sub(r'[^a-z0-9]+','-',value.lower()).strip('-')

    def extract(self, prompt: str, intent: IntentResult) -> CanonicalArchitectureModel:
        extracted=self.entities.extract(prompt)
        if len(extracted) < 2:
            raise ArchitectureExtractionError('Unable to extract at least two architecture components from the prompt')
        elements=[]; used=set()
        for x in extracted:
            eid=self._slug(x.name); base=eid; i=2
            while eid in used: eid=f'{base}-{i}'; i+=1
            used.add(eid)
            elements.append(Element(id=eid,name=x.name,type=x.type,technology=x.technology))
        domains,elements=self.domains.resolve(prompt,elements)
        relationships=self.relationships.extract(prompt,elements)
        if not relationships:
            raise ArchitectureExtractionError('Components were extracted but no meaningful relationships could be derived')
        flows=self.flows.build(relationships)
        return CanonicalArchitectureModel(
            architecture=ArchitectureMeta(id='arch-001',name=f'{intent.architecture_type.value.replace("_"," ").title()} Architecture',type=intent.architecture_type,viewpoint=intent.viewpoint,description=prompt),
            domains=domains,elements=elements,relationships=relationships,flows=flows,
            metadata={'generator':'deterministic-extraction-v1','stage':'canonical'}
        )
