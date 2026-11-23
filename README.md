# Enterprise Architecture Generator 4.0

A production-grade system for generating publication-quality enterprise architecture diagrams from natural-language prompts.

## Architecture Pipeline

```
Prompt
  │
  ▼
Intent Analysis (Classification & Viewpoint Selection)
  │
  ▼
AI Architecture Extraction (LLM via Vertex AI / Gemini API with Deterministic Fallback)
  │
  ▼
Enterprise Intelligence (Domains, Layers, Boundaries, Flows)
  │
  ▼
Canonical Architecture Model (CAM)
  │
  ▼
Semantic & Structural Validation
  │
  ▼
View Compilation (Layout Strategy & Layer Ordering)
  │
  ▼
Graph Compilation (Technology & Icon Resolution)
  │
  ▼
Frontend SVG Rendering (Directed Orthogonal Connectors, Brand Icons & Group Containers)
```

## AI Configuration

The application uses Google Vertex AI with Application Default Credentials (ADC) by default, or can be configured to use Google Gemini API via API key.

Configure `.env`:
```env
# Google Cloud Vertex AI Configuration (Enterprise ADC Mode - Recommended)
GOOGLE_CLOUD_PROJECT=architecture-diagram-500204
GCP_LOCATION=us-central1
GEMINI_MODEL=gemini-1.5-flash
LLM_PROVIDER=vertex_ai

# Or for local development with an API key:
# LLM_PROVIDER=gemini_api
# GEMINI_API_KEY=your_key_here
```

### Supported & Verified Models
- `gemini-1.5-flash` (Recommended default: fast, structured, supported across regions)
- `gemini-1.5-pro` (Higher reasoning capability)
- `gemini-2.0-flash` (Next-gen fast model)

## Design Rules

1. **AI Never Owns Coordinates**: The LLM extracts components, technologies, and relationships. Deterministic layout engines compute geometry.
2. **Canonical Architecture Model (CAM)**: All inputs are normalized into strict Pydantic schemas before rendering.
3. **Graceful Degradation**: If Vertex AI or network access is unavailable, the system transparently falls back to the deterministic pattern-matching engine.
4. **Rich Icon Resolution**: Icons resolve hierarchically: Technology match (e.g. `Kafka`, `Saviynt`, `PostgreSQL`) → Name match → Component type default → System fallback.
5. **Modern SVG Visualization**: Fully vector-rendered diagrams with orthogonal/curved connectors, directional arrows, protocol badges, domain boundary boxes, and SVG export.

## Quick Start

```bash
# Setup virtual environment
python -m venv .venv
.venv\Scripts\activate   # Windows
# source .venv/bin/activate # Linux / macOS

# Install dependencies
pip install -r requirements.txt

# Start development server
uvicorn app.main:app --reload --port 8080
```

Open in browser:
- App: http://127.0.0.1:8080
- API Docs: http://127.0.0.1:8080/docs
- Health & LLM Status: http://127.0.0.1:8080/api/llm-status

## Cloud Run Deployment

Deploy with Google Cloud SDK:
```bash
bash deploy.sh
```
Or directly:
```bash
gcloud run deploy enterprise-architecture-generator \
  --source . \
  --project architecture-diagram-500204 \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8080
```
