from app.models.architecture import CanonicalArchitectureModel
from .intent_agent import IntentAgent
from .architect_agent import ArchitectAgent
from .specialist_router import SpecialistRouter
from .reviewer_agent import ReviewerAgent

class ArchitectureOrchestrator:
    def __init__(self):
        self.intent_agent = IntentAgent()
        self.architect_agent = ArchitectAgent()
        self.specialist_router = SpecialistRouter()
        self.reviewer_agent = ReviewerAgent()

    def generate(self, prompt: str) -> tuple[CanonicalArchitectureModel, dict]:
        intent = self.intent_agent.analyze(prompt)
        specialist = self.specialist_router.select(intent.architecture_type)
        model = self.architect_agent.build(prompt, intent)
        validation = self.reviewer_agent.review(model)

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
            "validation": validation.model_dump(),
        }
