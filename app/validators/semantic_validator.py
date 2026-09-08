from app.models.architecture import CanonicalArchitectureModel
from .base import ValidationResult

def validate_semantics(model: CanonicalArchitectureModel) -> ValidationResult:
    result = ValidationResult()
    connected = set()

    for rel in model.relationships:
        connected.add(rel.source)
        connected.add(rel.target)

    for element in model.elements:
        if len(model.elements) > 1 and element.required and element.id not in connected:
            result.add(
                "ORPHAN_ELEMENT",
                "warning",
                f"Required element '{element.name}' is not connected",
                element.id
            )

    primary_flows = [flow for flow in model.flows if flow.primary]
    if model.relationships and not primary_flows:
        result.add(
            "NO_PRIMARY_FLOW",
            "warning",
            "Architecture has relationships but no explicitly marked primary flow"
        )

    element_ids = {e.id for e in model.elements}
    for flow in model.flows:
        for step in flow.steps:
            if step not in element_ids:
                result.add(
                    "UNKNOWN_FLOW_STEP",
                    "error",
                    f"Flow '{flow.id}' references unknown element '{step}'",
                    flow.id
                )

    return result
