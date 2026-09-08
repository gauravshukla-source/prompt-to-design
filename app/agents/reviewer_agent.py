from app.models.architecture import CanonicalArchitectureModel
from app.validators.quality import validate_model
from app.validators.prompt_coverage_validator import validate_prompt_coverage
from app.validators.base import ValidationResult

class ReviewerAgent:
    def review(self, model: CanonicalArchitectureModel, prompt: str | None = None) -> ValidationResult:
        result = validate_model(model)
        placeholder={'source','target'}
        if {e.id for e in model.elements} == placeholder:
            result.add('PLACEHOLDER_ARCHITECTURE','error','Placeholder Source/Target architecture is not an acceptable result')
        if prompt:
            result.extend(validate_prompt_coverage(prompt,model))
        return result
