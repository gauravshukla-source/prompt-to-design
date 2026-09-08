from app.models.view import ViewModel, GraphModel
from app.tools.icon_registry import get_icon

class GraphCompiler:
    def compile(self, view: ViewModel) -> GraphModel:
        nodes = [
            {
                "data": {
                    "id": node.id,
                    "label": node.label,
                    "type": node.type,
                    "domain_id": node.domain_id,
                    "icon": get_icon(node.type),
                }
            }
            for node in view.nodes
        ]

        edges = [
            {
                "data": {
                    "id": edge.id,
                    "source": edge.source,
                    "target": edge.target,
                    "label": edge.label or "",
                    "type": edge.type,
                }
            }
            for edge in view.edges
        ]

        groups = [
            {
                "id": domain["id"],
                "label": domain["name"],
                "type": domain["type"],
                "parent_id": domain.get("parent_id"),
            }
            for domain in view.domains
        ]

        return GraphModel(
            nodes=nodes,
            edges=edges,
            groups=groups,
            constraints={"layout_strategy": view.layout_strategy},
        )
