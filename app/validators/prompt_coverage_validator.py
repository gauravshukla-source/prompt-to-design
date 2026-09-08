from app.models.architecture import CanonicalArchitectureModel
from app.validators.base import ValidationResult
from app.extraction.prompt_coverage import PromptCoverage


def validate_prompt_coverage(
    prompt: str,
    model: CanonicalArchitectureModel,
) -> ValidationResult:
    """Prompt coverage is advisory and never invalidates a structurally valid graph."""
    result = ValidationResult()
    coverage = PromptCoverage().evaluate(prompt, model)

    for item in coverage.missing:
        result.add(
            "PROMPT_CONCEPT_MISSING",
            "warning",
            f"Prompt concept '{item}' may not be represented in the architecture",
        )

    return result
