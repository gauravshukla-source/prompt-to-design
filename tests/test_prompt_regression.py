import json
from pathlib import Path
from app.agents.orchestrator import ArchitectureOrchestrator

CASES = json.loads(
    (Path(__file__).parent / "prompts" / "cases.json").read_text()
)

def test_prompt_regressions():
    orchestrator = ArchitectureOrchestrator()

    for case in CASES:
        model, analysis = orchestrator.generate(case["prompt"])
        assert model.architecture.type.value == case["expected_type"], case["id"]
        assert len(model.elements) >= case["minimum_elements"], case["id"]
        assert analysis["validation"]["valid"], case["id"]
