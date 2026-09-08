from app.validators.semantic_validator import validate_semantics
from app.models.architecture import Element
from app.models.enums import ElementType

def test_valid_semantics(make_valid_model):
    result = validate_semantics(make_valid_model())
    assert result.valid

def test_orphan_is_warning(make_valid_model):
    model = make_valid_model()
    model.elements.append(Element(id="c", name="C", type=ElementType.SERVICE))
    result = validate_semantics(model)
    assert result.valid
    assert any(x.code == "ORPHAN_ELEMENT" for x in result.issues)

def test_unknown_flow_step(make_valid_model):
    model = make_valid_model()
    model.flows[0].steps.append("missing")
    result = validate_semantics(model)
    assert not result.valid
    assert any(x.code == "UNKNOWN_FLOW_STEP" for x in result.issues)
