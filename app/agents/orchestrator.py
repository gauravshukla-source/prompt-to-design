from app.models.architecture import CanonicalArchitectureModel
from app.extraction.prompt_coverage import PromptCoverage
from .intent_agent import IntentAgent
from .extraction_agent import ExtractionAgent
from .specialist_router import SpecialistRouter
from .reviewer_agent import ReviewerAgent
from app.intelligence.enterprise_engine import EnterpriseArchitectureIntelligence


class ArchitectureOrchestrator:
    def __init__(self):
        self.intent_agent = IntentAgent()
        self.extraction_agent = ExtractionAgent()
        self.specialist_router = SpecialistRouter()
        self.reviewer_agent = ReviewerAgent()
        self.coverage = PromptCoverage()
        self.enterprise = EnterpriseArchitectureIntelligence()

    def generate(self, prompt: str) -> tuple[CanonicalArchitectureModel, dict]:
        intent = self.intent_agent.analyze(prompt)
        specialist = self.specialist_router.select(intent.architecture_type)

        model = self.extraction_agent.extract(prompt, intent)
        model = self.enterprise.enrich(prompt, model)
        validation = self.reviewer_agent.review(model, prompt)
        coverage = self.coverage.evaluate(prompt, model)

        # Prompt-coverage findings are advisory, even if an older validator
        # accidentally marks them as errors. Only structural/model errors block
        # generation.
        advisory_codes = {
            "PROMPT_CONCEPT_MISSING",
            "PROMPT_COVERAGE_MISSING",
            "PROMPT_CONCEPT_NOT_REPRESENTED",
        }
        fatal_errors = [
            issue for issue in validation.issues
            if issue.severity == "error" and issue.code not in advisory_codes
        ]

        if fatal_errors:
            raise ValueError(
                "Architecture generation failed validation: "
                + "; ".join(issue.message for issue in fatal_errors)
            )

        return model, {
            "intent": {
                "architecture_type": intent.architecture_type.value,
                "viewpoint": intent.viewpoint.value,
                "complexity": intent.complexity,
                "required_concepts": intent.required_concepts,
                "excluded_concepts": intent.excluded_concepts,
                "primary_goal": intent.primary_goal,
            },
            "specialist": specialist,
            "extraction": {
                "elements_found": len(model.elements),
                "relationships_found": len(model.relationships),
                "coverage_score": coverage.score,
                "expected_concepts": coverage.expected,
                "matched_concepts": coverage.matched,
                "missing_concepts": coverage.missing,
                "semantic_matches": coverage.semantic_matches,
            },
            "enterprise": model.metadata.get("enterprise_intelligence", {}),
            "validation": validation.model_dump(),
        }
