from pydantic import BaseModel, Field

class ValidationIssue(BaseModel):
    code: str
    severity: str
    message: str
    entity_id: str | None = None

class ValidationResult(BaseModel):
    valid: bool = True
    issues: list[ValidationIssue] = Field(default_factory=list)

    def add(self, code: str, severity: str, message: str, entity_id: str | None = None):
        self.issues.append(ValidationIssue(
            code=code, severity=severity, message=message, entity_id=entity_id
        ))
        if severity == "error":
            self.valid = False

    def extend(self, other: "ValidationResult"):
        self.issues.extend(other.issues)
        self.valid = self.valid and other.valid
