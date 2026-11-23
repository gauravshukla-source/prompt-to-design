import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from app.api.architecture import router as architecture_router

BASE_DIR   = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"

app = FastAPI(
    title="Enterprise Architecture Generator 4.0",
    version="4.0.0",
    description="Canonical-model-first enterprise architecture generation.",
)

app.include_router(architecture_router)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def index():
    return FileResponse(STATIC_DIR / "index.html")


@app.get("/health")
def health():
    return {"status": "ok", "version": "4.0.0"}


@app.get("/api/llm-status")
def llm_status():
    """Returns whether LLM is configured and which model/provider is active."""
    provider = os.getenv("LLM_PROVIDER", "vertex_ai").strip()
    model    = os.getenv("GEMINI_MODEL", "gemini-1.5-flash").strip()
    project  = os.getenv("GOOGLE_CLOUD_PROJECT", "").strip()

    if provider == "vertex_ai" and not project:
        return {"available": False, "reason": "GOOGLE_CLOUD_PROJECT not set", "provider": provider}
    if provider == "gemini_api" and not os.getenv("GEMINI_API_KEY", "").strip():
        return {"available": False, "reason": "GEMINI_API_KEY not set", "provider": provider}

    return {
        "available": True,
        "provider": provider,
        "model": model,
        "project": project or None,
    }
