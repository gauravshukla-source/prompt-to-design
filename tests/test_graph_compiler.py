from app.compiler.graph_compiler import GraphCompiler
from app.compiler.view_compiler import ViewCompiler
from app.agents.orchestrator import ArchitectureOrchestrator


def test_graph_contains_renderable_node_and_edge_contract():
    model, _ = ArchitectureOrchestrator().generate(
        "Users access a React frontend which calls a backend API and stores data in PostgreSQL database."
    )
    view = ViewCompiler().compile(model)
    graph = GraphCompiler().compile(view)

    assert graph.nodes
    assert graph.edges
    assert all("data" in node and node["data"].get("id") for node in graph.nodes)
    assert all("data" in edge and edge["data"].get("source") and edge["data"].get("target") for edge in graph.edges)
    assert all(node["data"].get("icon", "").startswith("/static/icons/") for node in graph.nodes)
