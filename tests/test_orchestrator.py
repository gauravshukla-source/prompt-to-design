from app.agents.orchestrator import ArchitectureOrchestrator

def test_hybrid_prompt():
    model, analysis = ArchitectureOrchestrator().generate(
        "On-prem applications connect securely through VPN to cloud APIs and databases."
    )
    assert model.architecture.type.value == "hybrid_cloud"
    assert analysis["specialist"] == "cloud"
    assert analysis["validation"]["valid"]

def test_iam_prompt():
    model, analysis = ArchitectureOrchestrator().generate(
        "Employees authenticate using Active Directory and Entra ID. Saviynt manages access."
    )
    assert model.architecture.type.value == "iam"
    assert analysis["specialist"] == "iam"

def test_event_prompt():
    model, analysis = ArchitectureOrchestrator().generate(
        "Order service publishes events to Kafka and payment service consumes them."
    )
    assert model.architecture.type.value == "event_driven"
    assert analysis["validation"]["valid"]
