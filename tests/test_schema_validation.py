import pytest
from pydantic import ValidationError
from app.models.architecture import Flow

def test_flow_requires_two_steps():
    with pytest.raises(ValidationError):
        Flow(id="f", name="bad", steps=["only-one"])
