from app.models.architecture import CanonicalArchitectureModel
from .base import ValidationResult
from .architecture_validator import validate_architecture
from .relationship_validator import validate_relationships
from .semantic_validator import validate_semantics

def validate_model(model: CanonicalArchitectureModel) -> ValidationResult:
    result = ValidationResult()
    for validator in (
        validate_architecture,
        validate_relationships,
        validate_semantics,
    ):
        result.extend(validator(model))
    return result
