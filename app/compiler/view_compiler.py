from app.models.architecture import CanonicalArchitectureModel
from app.models.enums import Viewpoint
from app.models.view import ViewModel, ViewNode, ViewEdge
from app.composition.composition_planner import CompositionPlanner

LAYER_ORDER={'presentation':0,'identity':1,'network':1,'integration':2,'application':3,'security':3,'data':4,'infrastructure':4}
class ViewCompiler:
    def __init__(self): self.composition=CompositionPlanner()
    def compile(self, model: CanonicalArchitectureModel, viewpoint: Viewpoint | None = None) -> ViewModel:
        viewpoint=viewpoint or model.architecture.viewpoint
        plan=self.composition.plan(model,viewpoint)
        nodes=[ViewNode(id=e.id,label=e.name,type=e.type.value,domain_id=e.domain_id,
            layer=LAYER_ORDER.get(e.layer or 'application',2),metadata={'technology':e.technology,'provider':e.provider,'layer':e.layer}) for e in model.elements]
        edges=[ViewEdge(id=r.id,source=r.source,target=r.target,label=r.label or r.protocol,type=r.type.value,
            metadata={'protocol':r.protocol,'direction':r.direction}) for r in model.relationships]
        domains=[d.model_dump() for d in model.domains]
        return ViewModel(name=f'{model.architecture.name} - {viewpoint.value}',viewpoint=viewpoint,domains=domains,nodes=nodes,edges=edges,
            layout_strategy=plan.layout_strategy,metadata={'composition':plan.model_dump(),'boundaries':[b.model_dump() for b in model.boundaries]})
