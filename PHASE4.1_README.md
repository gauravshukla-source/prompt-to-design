# Phase 4.1 — Smart Graph Layout & Connector Intelligence

## Updated files
- app.js
- main.py
- style.css (retained from Phase 4)
- agent.py (retained from Phase 4)

## What changed
1. Graph-aware layout using semantic layers as the primary architecture direction.
2. Longest weighted request path becomes a centered visual backbone.
3. Barycentric ordering sweeps reduce edge crossings between adjacent layers.
4. Fan-in and fan-out branches are compacted around their primary relationship anchor.
5. Immediate siblings stay together instead of being distributed across the full canvas.
6. Connector lanes are assigned after final positions are known.
7. Boundary styling now reflects nesting depth.
8. Edge labels are larger and have clearer backgrounds.

## Replace
Copy app.js to static/app.js and main.py to backend/main.py.
You may keep the existing Phase 4 agent.py, index.html and style.css unchanged.

## Test
Restart the backend and hard refresh the browser. Re-run the AWS three-tier prompt first.
