from app.validators.relationship_validator import validate_relationships
from app.models.architecture import Relationship
from app.models.enums import RelationshipType

def test_unknown_source(make_valid_model):
    model = make_valid_model()
    model.relationships[0].source = "unknown"
    result = validate_relationships(model)
    assert not result.valid
    assert any(x.code == "UNKNOWN_RELATIONSHIP_SOURCE" for x in result.issues)

def test_self_relationship(make_valid_model):
    model = make_valid_model()
    model.relationships[0].target = "a"
    result = validate_relationships(model)
    assert not result.valid
    assert any(x.code == "SELF_RELATIONSHIP" for x in result.issues)

def test_duplicate_relationship_id(make_valid_model):
    model = make_valid_model()
    model.relationships.append(
        Relationship(id="r1", source="a", target="b", type=RelationshipType.API)
    )
    result = validate_relationships(model)
    assert not result.valid
