# Enterprise Architecture Diagram Generator - Final Fix

## What was fixed
- CytoscapeJS is loaded before `app.js`.
- App initialization now validates the DOM and Cytoscape before using `cy`.
- All canvas operations safely handle an unavailable canvas.
- Removed the unconfigured `dagre` layout dependency and replaced it with deterministic layered layout using built-in Cytoscape positioning.
- Generate/refine cannot call `cy.elements()` before canvas initialization.
- Gemini 1.5 defaults were removed. The backend defaults to `gemini-2.5-flash` and uses Vertex AI ADC with fallback models.
- Generated and refined diagrams are normalized by `architecture_engine.py` before returning to the UI.

## Replace/deploy
Deploy this complete project folder, preserving:
- `backend/`
- `static/`
- `requirements.txt`

For Cloud Run, configure ADC through the service account and ensure Vertex AI API access.
Optional environment variables:
- GOOGLE_CLOUD_PROJECT
- GOOGLE_CLOUD_LOCATION (defaults to global)
- GEMINI_MODEL (defaults to gemini-2.5-flash)

## Important browser dependency
The app intentionally loads Cytoscape before `app.js`:
`https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.33.1/cytoscape.min.js`
If your organization blocks public CDNs, download Cytoscape into `static/vendor/` during your build process and update `index.html` to reference the local file.
