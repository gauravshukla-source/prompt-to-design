from typing import Any
from pydantic import BaseModel, Field
from .enums import Viewpoint

class ViewNode(BaseModel):
    id: str
    label: str
    type: str
    domain_id: str | None = None
    layer: int = 0
    metadata: dict[str, Any] = Field(default_factory=dict)

class ViewEdge(BaseModel):
    id: str
    source: str
    target: str
    label: str | None = None
    type: str = "generic"
    metadata: dict[str, Any] = Field(default_factory=dict)

class ViewModel(BaseModel):
    name: str
    viewpoint: Viewpoint
    domains: list[dict[str, Any]] = Field(default_factory=list)
    nodes: list[ViewNode] = Field(default_factory=list)
    edges: list[ViewEdge] = Field(default_factory=list)
    layout_strategy: str = "layered"
    metadata: dict[str, Any] = Field(default_factory=dict)

class GraphModel(BaseModel):
    nodes: list[dict[str, Any]]
    edges: list[dict[str, Any]]
    groups: list[dict[str, Any]] = Field(default_factory=list)
    constraints: dict[str, Any] = Field(default_factory=dict)
