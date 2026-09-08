from app.models.architecture import CanonicalArchitectureModel
from app.validators.quality import validate_model
from app.validators.base import ValidationResult

class ReviewerAgent:
    def review(self, model: CanonicalArchitectureModel) -> ValidationResult:
        return validate_model(model)
