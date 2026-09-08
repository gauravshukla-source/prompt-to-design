from app.agents.orchestrator import ArchitectureOrchestrator
from app.compiler.view_compiler import ViewCompiler
from app.compiler.graph_compiler import GraphCompiler
from app.models.enums import Viewpoint

def test_view_and_graph_compilation():
    model, _ = ArchitectureOrchestrator().generate(
        "On-prem applications connect securely through VPN to cloud APIs and databases."
    )
    view = ViewCompiler().compile(model, Viewpoint.DEPLOYMENT)
    graph = GraphCompiler().compile(view)

    assert view.layout_strategy == "hybrid_horizontal"
    assert len(graph.nodes) == len(model.elements)
    assert len(graph.edges) == len(model.relationships)
