from app.models.architecture import CanonicalArchitectureModel
from .domain_intelligence import DomainIntelligence
from .layer_intelligence import LayerIntelligence
from .boundary_intelligence import BoundaryIntelligence
from .flow_intelligence import FlowIntelligence

class EnterpriseArchitectureIntelligence:
    def __init__(self):
        self.domains=DomainIntelligence(); self.layers=LayerIntelligence(); self.boundaries=BoundaryIntelligence(); self.flows=FlowIntelligence()
    def enrich(self,prompt:str,model:CanonicalArchitectureModel):
        model.domains,model.elements=self.domains.enrich(prompt,model.elements,model.domains)
        model.elements=self.layers.enrich(model.elements)
        model.boundaries=self.boundaries.detect(prompt,model.domains,model.elements)
        model.flow_metadata=self.flows.enrich(model.relationships)
        model.metadata['enterprise_intelligence']={
            'domains':len(model.domains),'layers':sorted({e.layer for e in model.elements if e.layer}),
            'boundaries':len(model.boundaries),'flows':len(model.flow_metadata)
        }
        return model
