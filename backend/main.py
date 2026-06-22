import os
import uuid
import shutil
from typing import Optional, List
from fastapi import FastAPI, HTTPException, UploadFile, File, Form, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import database
import agent

app = FastAPI(title="Prompt to Design Diagram Generator API")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure directories exist
UPLOAD_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "icons")
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Initialize database
database.init_db()

# Request schemas
class GenerateRequest(BaseModel):
    prompt: str

class RefineRequest(BaseModel):
    prompt: str
    current_diagram: dict

class ProjectCreateRequest(BaseModel):
    name: str

class DiagramSaveRequest(BaseModel):
    id: str
    project_id: str
    topology_json: dict
    version: int

# API Endpoints

@app.get("/api/projects")
def get_projects():
    return database.get_projects()

@app.post("/api/projects")
def create_project(req: ProjectCreateRequest):
    project_id = str(uuid.uuid4())
    database.create_project(project_id, req.name)
    return {"id": project_id, "name": req.name}

@app.get("/api/projects/{project_id}/diagrams")
def get_project_diagrams(project_id: str):
    return database.get_project_diagrams(project_id)

@app.post("/api/diagrams")
def save_diagram(req: DiagramSaveRequest):
    import json
    topology_str = json.dumps(req.topology_json)
    database.save_diagram(req.id, req.project_id, topology_str, req.version)
    return {"status": "success"}

@app.get("/api/diagrams/{diagram_id}")
def get_diagram(diagram_id: str):
    import json
    diag = database.get_diagram(diagram_id)
    if not diag:
        raise HTTPException(status_code=404, detail="Diagram not found")
    # Parse topology_json back to dict
    diag_dict = dict(diag)
    diag_dict["topology_json"] = json.loads(diag_dict["topology_json"])
    return diag_dict

@app.post("/api/generate")
def generate_diagram(req: GenerateRequest, x_gemini_key: Optional[str] = Header(None)):
    custom_icons = database.get_custom_icons()
    try:
        diagram_data = agent.generate_diagram(req.prompt, custom_icons, x_gemini_key)
        return diagram_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/refine")
def refine_diagram(req: RefineRequest, x_gemini_key: Optional[str] = Header(None)):
    custom_icons = database.get_custom_icons()
    try:
        refined_data = agent.refine_diagram(req.prompt, req.current_diagram, custom_icons, x_gemini_key)
        return refined_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/icons")
def get_custom_icons():
    icons = database.get_custom_icons()
    # Add public URL path
    for icon in icons:
        icon["url"] = f"/static/icons/{icon['filename']}"
    return icons

@app.post("/api/icons/upload")
async def upload_custom_icon(
    tag: str = Form(...),
    description: str = Form(...),
    file: UploadFile = File(...)
):
    if not file.filename.lower().endswith(".svg"):
        raise HTTPException(status_code=400, detail="Only SVG files are supported.")
        
    icon_id = str(uuid.uuid4())
    # Save file locally
    filename = f"{icon_id}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    database.save_custom_icon(icon_id, tag, description, filename)
    return {"id": icon_id, "tag": tag, "url": f"/static/icons/{filename}"}

@app.delete("/api/icons/{icon_id}")
def delete_custom_icon(icon_id: str):
    filename = database.delete_custom_icon(icon_id)
    if filename:
        file_path = os.path.join(UPLOAD_DIR, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
        return {"status": "success"}
    raise HTTPException(status_code=404, detail="Icon not found")

# Serve Frontend static assets
static_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
if os.path.exists(static_path):
    app.mount("/static", StaticFiles(directory=static_path), name="static")
    
    # Mount index.html at root
    @app.get("/")
    def read_index():
        from fastapi.responses import FileResponse
        return FileResponse(os.path.join(static_path, "index.html"))
else:
    @app.get("/")
    def read_root():
        return {"message": "Server running, static files folder not found. Please create 'static' folder."}
