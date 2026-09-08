from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from app.agents.orchestrator import ArchitectureOrchestrator
from app.compiler.view_compiler import ViewCompiler
from app.compiler.graph_compiler import GraphCompiler
from app.models.enums import Viewpoint

router = APIRouter(prefix="/api", tags=["architecture"])

class GenerateRequest(BaseModel):
    prompt: str = Field(min_length=3)
    viewpoint: Viewpoint | None = None

@router.post("/generate")
def generate(request: GenerateRequest):
    try:
        model, analysis = ArchitectureOrchestrator().generate(request.prompt)
        view = ViewCompiler().compile(model, request.viewpoint)
        graph = GraphCompiler().compile(view)
        return {
            "architecture": model.model_dump(),
            "analysis": analysis,
            "view": view.model_dump(),
            "graph": graph.model_dump(),
        }
    except ValueError as exc:
        raise HTTPException(status_code=422, detail={"stage": "architecture_generation", "message": str(exc)})
    except Exception as exc:
        raise HTTPException(status_code=500, detail={"stage": "internal_error", "message": str(exc)})
