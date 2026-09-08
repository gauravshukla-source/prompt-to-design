from app.validators.quality import validate_model

def test_quality_gate(make_valid_model):
    result = validate_model(make_valid_model())
    assert result.valid
    assert result.issues == []
