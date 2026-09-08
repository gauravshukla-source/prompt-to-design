from app.agents.orchestrator import ArchitectureOrchestrator
from app.composition.composition_planner import CompositionPlanner
from app.models.enums import Viewpoint


def plan(prompt):
    model, _ = ArchitectureOrchestrator().generate(prompt)
    return CompositionPlanner().plan(model, Viewpoint.CONCEPTUAL)


def test_linear_web_architecture_prefers_horizontal_flow():
    p = plan('Create an architecture where users access a React frontend through the internet. The frontend communicates with a backend API, which stores data in PostgreSQL.')
    assert p.layout_strategy in {'layered_horizontal', 'linear_horizontal'}
    assert p.metadata['topology']['node_count'] >= 4


def test_microservices_branching_prefers_branching_layout():
    p = plan('A mobile application and web application access backend microservices through an API Gateway. The microservices use Redis and MongoDB.')
    assert p.layout_strategy == 'branching_horizontal'
    assert p.metadata['topology']['has_fan_in'] or p.metadata['topology']['has_fan_out']


def test_hybrid_architecture_prefers_hybrid_layout():
    p = plan('On-prem applications connect securely through VPN to cloud APIs and databases.')
    assert p.layout_strategy == 'hybrid_horizontal'
    assert p.metadata['topology']['hybrid'] is True
    assert p.metadata['viewport']['fit'] == 'content'
