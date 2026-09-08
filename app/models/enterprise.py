from typing import Any
from pydantic import BaseModel, Field

class Boundary(BaseModel):
    id: str
    name: str
    type: str = "logical"
    domain_id: str | None = None
    parent_id: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)

class FlowMetadata(BaseModel):
    relationship_id: str
    flow_type: str
    protocol: str | None = None
    security: str | None = None
    direction: str = "forward"
    metadata: dict[str, Any] = Field(default_factory=dict)

class CompositionContainer(BaseModel):
    id: str
    name: str
    kind: str = "domain"
    element_ids: list[str] = Field(default_factory=list)
    parent_id: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)

class CompositionPlan(BaseModel):
    layout_strategy: str = "layered"
    containers: list[CompositionContainer] = Field(default_factory=list)
    boundaries: list[Boundary] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
