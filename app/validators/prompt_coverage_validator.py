from app.models.architecture import CanonicalArchitectureModel
from app.validators.base import ValidationResult
from app.extraction.prompt_coverage import PromptCoverage

def validate_prompt_coverage(prompt: str, model: CanonicalArchitectureModel) -> ValidationResult:
    result=ValidationResult(); coverage=PromptCoverage().evaluate(prompt,model)
    for item in coverage.missing:
        result.add('PROMPT_CONCEPT_MISSING','error',f"Prompt concept '{item}' was not represented in the architecture")
    if coverage.score < 100 and not coverage.missing:
        result.add('LOW_PROMPT_COVERAGE','warning',f'Prompt coverage score is {coverage.score}')
    return result
