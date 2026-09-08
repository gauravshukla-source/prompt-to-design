from app.models.architecture import CanonicalArchitectureModel
from .base import ValidationResult

def validate_architecture(model: CanonicalArchitectureModel) -> ValidationResult:
    result = ValidationResult()

    ids = [d.id for d in model.domains] + [e.id for e in model.elements]
    duplicates = {x for x in ids if ids.count(x) > 1}
    for duplicate in duplicates:
        result.add("DUPLICATE_ID", "error", f"Duplicate ID: {duplicate}", duplicate)

    domain_ids = {d.id for d in model.domains}
    element_ids = {e.id for e in model.elements}

    for domain in model.domains:
        if domain.parent_id and domain.parent_id not in domain_ids:
            result.add(
                "UNKNOWN_PARENT_DOMAIN", "error",
                f"Domain {domain.id} references unknown parent {domain.parent_id}",
                domain.id
            )

    for element in model.elements:
        if element.domain_id and element.domain_id not in domain_ids:
            result.add(
                "UNKNOWN_DOMAIN", "error",
                f"Element {element.id} references unknown domain {element.domain_id}",
                element.id
            )

    if not model.elements:
        result.add("NO_ELEMENTS", "error", "Architecture contains no elements")

    return result
