from app.validators.architecture_validator import validate_architecture
from app.models.architecture import Element
from app.models.enums import ElementType

def test_valid_architecture(make_valid_model):
    result = validate_architecture(make_valid_model())
    assert result.valid

def test_unknown_domain(make_valid_model):
    model = make_valid_model()
    model.elements[0].domain_id = "missing"
    result = validate_architecture(model)
    assert not result.valid
    assert any(x.code == "UNKNOWN_DOMAIN" for x in result.issues)

def test_duplicate_id(make_valid_model):
    model = make_valid_model()
    model.elements.append(Element(id="a", name="Duplicate", type=ElementType.APPLICATION))
    result = validate_architecture(model)
    assert not result.valid
    assert any(x.code == "DUPLICATE_ID" for x in result.issues)
