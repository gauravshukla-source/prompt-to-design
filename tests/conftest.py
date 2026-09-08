import pytest
from app.models.architecture import (
    ArchitectureMeta, CanonicalArchitectureModel, Element, Relationship, Flow
)
from app.models.enums import ArchitectureType, ElementType, RelationshipType

@pytest.fixture
def make_valid_model():
    def factory():
        return CanonicalArchitectureModel(
            architecture=ArchitectureMeta(
                id="test",
                name="Test",
                type=ArchitectureType.GENERIC,
            ),
            elements=[
                Element(id="a", name="A", type=ElementType.APPLICATION),
                Element(id="b", name="B", type=ElementType.DATABASE),
            ],
            relationships=[
                Relationship(
                    id="r1", source="a", target="b",
                    type=RelationshipType.DATA_ACCESS
                )
            ],
            flows=[
                Flow(id="f1", name="Primary", steps=["a", "b"], primary=True)
            ],
        )
    return factory
