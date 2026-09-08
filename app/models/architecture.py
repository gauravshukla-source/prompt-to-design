from typing import Any
from pydantic import BaseModel, Field
from .enums import ArchitectureType, DomainType, ElementType, RelationshipType, FlowType, Viewpoint

class ArchitectureMeta(BaseModel):
    id: str
    name: str
    type: ArchitectureType = ArchitectureType.GENERIC
    viewpoint: Viewpoint = Viewpoint.CONCEPTUAL
    description: str = ""

class Domain(BaseModel):
    id: str
    name: str
    type: DomainType = DomainType.LOGICAL
    provider: str | None = None
    parent_id: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)

class Element(BaseModel):
    id: str
    name: str
    type: ElementType = ElementType.GENERIC
    technology: str | None = None
    provider: str | None = None
    domain_id: str | None = None
    layer: str | None = None
    required: bool = True
    metadata: dict[str, Any] = Field(default_factory=dict)

class Relationship(BaseModel):
    id: str
    source: str
    target: str
    type: RelationshipType = RelationshipType.GENERIC
    protocol: str | None = None
    direction: str = "forward"
    label: str | None = None
    required: bool = True
    metadata: dict[str, Any] = Field(default_factory=dict)

class Flow(BaseModel):
    id: str
    name: str
    type: FlowType = FlowType.PRIMARY
    steps: list[str] = Field(min_length=2)
    primary: bool = False
    metadata: dict[str, Any] = Field(default_factory=dict)

class CanonicalArchitectureModel(BaseModel):
    architecture: ArchitectureMeta
    domains: list[Domain] = Field(default_factory=list)
    elements: list[Element] = Field(default_factory=list)
    relationships: list[Relationship] = Field(default_factory=list)
    flows: list[Flow] = Field(default_factory=list)
    security_zones: list[str] = Field(default_factory=list)
    metadata: dict[str, Any] = Field(default_factory=dict)
