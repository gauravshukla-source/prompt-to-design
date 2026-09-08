from app.models.architecture import CanonicalArchitectureModel
from app.models.enterprise import CompositionPlan, CompositionContainer
from app.models.enums import Viewpoint
from app.tools.diagram_rules import get_layout_strategy

class CompositionPlanner:
    def plan(self,model:CanonicalArchitectureModel,viewpoint:Viewpoint):
        containers=[]
        for d in model.domains:
            ids=[e.id for e in model.elements if e.domain_id==d.id]
            if ids: containers.append(CompositionContainer(id=d.id,name=d.name,kind='domain',element_ids=ids,parent_id=d.parent_id))
        return CompositionPlan(
            layout_strategy=get_layout_strategy(viewpoint), containers=containers,
            boundaries=model.boundaries,
            metadata={'layers':{e.id:e.layer for e in model.elements},'enterprise':True}
        )
