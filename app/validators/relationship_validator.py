from app.models.architecture import CanonicalArchitectureModel
from .base import ValidationResult

def validate_relationships(model: CanonicalArchitectureModel) -> ValidationResult:
    result = ValidationResult()
    ids = {e.id for e in model.elements}
    relationship_ids = set()

    for rel in model.relationships:
        if rel.id in relationship_ids:
            result.add("DUPLICATE_RELATIONSHIP_ID", "error", f"Duplicate relationship ID: {rel.id}", rel.id)
        relationship_ids.add(rel.id)

        if rel.source not in ids:
            result.add("UNKNOWN_RELATIONSHIP_SOURCE", "error", f"Unknown source {rel.source}", rel.id)
        if rel.target not in ids:
            result.add("UNKNOWN_RELATIONSHIP_TARGET", "error", f"Unknown target {rel.target}", rel.id)
        if rel.source == rel.target:
            result.add("SELF_RELATIONSHIP", "error", "Relationship cannot connect an element to itself", rel.id)

    return result
