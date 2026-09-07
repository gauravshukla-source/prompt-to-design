# AI Enterprise Architecture Designer — Phase 3

## What Phase 3 adds

### 1. Architecture Intelligence Engine
`backend/architecture_engine.py` is the deterministic layer between Gemini and the renderer.

It normalizes:
- architecture categories and layers
- providers and icon slugs
- hierarchy parents and boundaries
- duplicate/dangling edges
- connection semantics
- `sourcePort` and `targetPort`

### 2. Port-aware orthogonal routing
Every connector now receives a semantic port pair:
- left-to-right: `east -> west`
- right-to-left: `west -> east`
- same-layer / side dependency: `south -> north`

The frontend uses these semantics to select horizontal or vertical orthogonal taxi routing. This keeps identity and observability dependencies away from the primary request path.

### 3. Sugiyama-style layered layout
The renderer performs repeated barycentric sweeps to reduce edge crossings while preserving architecture layers. Identity is placed on a top side rail and observability on a bottom side rail.

### 4. Architecture linter and score
New endpoint:
`POST /api/architecture/lint`

Checks include:
- dependency cycles
- excessive fan-out
- unencrypted HTTP
- direct external-to-data connectivity
- likely public database exposure
- missing identity modeling
- missing observability modeling

Returns an explainable score and findings.

### 5. Multiple architecture views
New endpoint:
`POST /api/architecture/view`

Supported views:
- `context`
- `logical`
- `integration`
- `security`
- `data-flow`

The frontend exposes `setArchitectureView(view)`.

### 6. Professional legend
A live legend is automatically added to the canvas and reflects the active architecture view.

### 7. Real SVG export
Phase 3 generates a standalone SVG instead of the previous placeholder message. Export options:
- JSON
- high-resolution PNG
- SVG
- PDF via browser print from generated SVG

### 8. Official-first icon policy
The embedded icons remain local fallbacks. Do not describe them as official vendor artwork.
For production, place vendor-approved assets in:
- `static/icons/aws`
- `static/icons/azure`
- `static/icons/gcp`

Then update the frontend registry to prefer the local approved asset before `SVG_ICONS` fallback.

## New API examples

### Lint
```json
POST /api/architecture/lint
{
  "diagram": { "groups": [], "nodes": [], "edges": [] }
}
```

### View projection
```json
POST /api/architecture/view
{
  "diagram": { "groups": [], "nodes": [], "edges": [] },
  "view": "security"
}
```

## Add these controls to your existing HTML
The JS exposes these functions; add buttons wherever your canvas toolbar is defined:

```html
<button onclick="runArchitectureLint()">Architecture Score</button>
<button onclick="setArchitectureView('context')">Context</button>
<button onclick="setArchitectureView('logical')">Logical</button>
<button onclick="setArchitectureView('integration')">Integration</button>
<button onclick="setArchitectureView('security')">Security</button>
<button onclick="setArchitectureView('data-flow')">Data Flow</button>
<button onclick="exportDiagram('svg')">Export SVG</button>
<button onclick="exportDiagram('pdf')">Export PDF</button>
```

## Replace files in the existing project

```text
existing-project/
├── backend/
│   ├── agent.py                 <- Phase 3
│   ├── architecture_engine.py   <- new
│   ├── database.py              <- existing copy
│   └── main.py                  <- Phase 3
├── static/
│   └── app.js                   <- Phase 3
├── icon_registry.json
└── static/icons/
    ├── aws/
    ├── azure/
    └── gcp/
```

No database schema migration is required for Phase 3.

## Important implementation note
Phase 3 is intentionally layered: AI proposes architecture semantics, the backend validates and lints them, and the frontend owns deterministic placement and visual routing. This prevents a model response from directly deciding the final visual quality.


## Phase 3.1: Gemini Latest + ADC Authentication

This build uses the Google Gen AI SDK against Vertex AI with **Application Default Credentials (ADC) only**. API keys are intentionally not supported.

### Model policy
- Default: `gemini-3.8-flash`
- Override: `GEMINI_MODEL` environment variable
- Compatibility fallback order: newest supported Gemini Flash candidates down to `gemini-2.5-flash`
- The configured model is always attempted first.

### Local development
```bash
gcloud auth application-default login
gcloud config set project YOUR_PROJECT_ID
```
Then set `GOOGLE_CLOUD_PROJECT` (or rely on the ADC-resolved project) and start the app.

### Google Cloud deployment
Use the runtime service account / workload identity as ADC and grant the workload the required Vertex AI permissions (for example, Vertex AI User as appropriate for your organization).

### Security policy
- No `GEMINI_API_KEY` is read.
- No API key is persisted.
- ADC credentials are supplied to the Vertex AI client.
- If ADC is unavailable, generation fails closed instead of falling back to an API key.
