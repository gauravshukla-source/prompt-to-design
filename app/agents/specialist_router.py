from app.models.enums import ArchitectureType

SPECIALISTS = {
    ArchitectureType.IAM: "iam",
    ArchitectureType.HYBRID_CLOUD: "cloud",
    ArchitectureType.CLOUD: "cloud",
    ArchitectureType.SECURITY: "security",
    ArchitectureType.MICROSERVICES: "application",
    ArchitectureType.EVENT_DRIVEN: "application",
}

class SpecialistRouter:
    def select(self, architecture_type: ArchitectureType) -> str:
        return SPECIALISTS.get(architecture_type, "general")
