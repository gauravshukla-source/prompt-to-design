from app.models.architecture import CanonicalArchitectureModel
from app.models.enums import Viewpoint
from app.models.view import ViewModel, ViewNode, ViewEdge
from app.tools.diagram_rules import get_layout_strategy

class ViewCompiler:
    def compile(self, model: CanonicalArchitectureModel, viewpoint: Viewpoint | None = None) -> ViewModel:
        viewpoint = viewpoint or model.architecture.viewpoint
        nodes = []
        edges = []

        for index, element in enumerate(model.elements):
            nodes.append(ViewNode(
                id=element.id,
                label=element.name,
                type=element.type.value,
                domain_id=element.domain_id,
                layer=index,
                metadata={
                    "technology": element.technology,
                    "provider": element.provider,
                },
            ))

        for relationship in model.relationships:
            edges.append(ViewEdge(
                id=relationship.id,
                source=relationship.source,
                target=relationship.target,
                label=relationship.label or relationship.protocol,
                type=relationship.type.value,
            ))

        return ViewModel(
            name=f"{model.architecture.name} - {viewpoint.value}",
            viewpoint=viewpoint,
            domains=[d.model_dump() for d in model.domains],
            nodes=nodes,
            edges=edges,
            layout_strategy=get_layout_strategy(viewpoint),
        )
