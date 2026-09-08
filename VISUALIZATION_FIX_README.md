# Enterprise Architecture Visualization Fix

This package fixes the visualization layer.

## Root cause
The previous `static/js/canvas.js` rendered nodes as a vertical HTML list and relationships as text. It was not a diagram renderer.

## What changed
- SVG-based architecture renderer with directional arrows.
- Automatic DAG/layer-based layout.
- Vertical layered layouts for conceptual/IAM/security/flow views.
- Horizontal layered layouts for executive/integration/deployment strategies.
- Branching support for multiple nodes in the same architecture layer.
- Curved orthogonal-style connectors with relationship labels.
- Domain containers when `domain_id` and graph groups are present.
- Stable fallback placement for disconnected nodes and cyclic graphs.
- Correct static icon paths in the graph contract.
- Regression test for graph compiler render contract.

## Tests
Run:

    python -m pytest -q

Expected:

    24 passed

## Deployment
Deploy the project normally. No Cytoscape dependency is required for this renderer.
