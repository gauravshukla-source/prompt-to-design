from app.agents.orchestrator import ArchitectureOrchestrator
from app.compiler.view_compiler import ViewCompiler

def test_hybrid_architecture_has_deployment_domains_and_boundaries():
    model,analysis=ArchitectureOrchestrator().generate('On-prem applications connect securely through VPN to cloud APIs and databases.')
    assert any(d.type.value=='on_premises' for d in model.domains)
    assert any(d.type.value=='cloud' for d in model.domains)
    assert model.boundaries
    assert analysis['enterprise']['domains'] >= 2

def test_application_architecture_has_layers_and_composition():
    model,_=ArchitectureOrchestrator().generate('Users access a React frontend through the internet. The frontend calls a backend API which stores data in PostgreSQL.')
    assert {e.layer for e in model.elements} >= {'presentation','integration','data'}
    view=ViewCompiler().compile(model)
    assert view.metadata['composition']['containers']

def test_cloud_provider_is_explicit_domain():
    model,_=ArchitectureOrchestrator().generate('Users access a React frontend in AWS that calls a backend API which stores data in PostgreSQL database.')
    assert any(d.provider=='aws' for d in model.domains)
