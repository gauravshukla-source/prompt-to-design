# Enterprise Architecture Generator 4.0

A production-oriented foundation for generating enterprise architecture diagrams from natural-language prompts.

## Architecture pipeline

Prompt
-> Intent Analysis
-> Architecture Planning
-> Domain Specialization
-> Canonical Architecture Model (CAM)
-> Validation / Review
-> View Compilation
-> Graph Compilation
-> Frontend Rendering

## Design rules

- AI never owns coordinates.
- AI output is normalized into a strict Canonical Architecture Model.
- Semantic and structural validation run before visualization.
- Test prompts are versioned and executed as regression tests.
- Layout is deterministic.
- Frontend modules are separated; no monolithic app.js.

## Quick start

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

## Run validation and tests

```bash
pytest -q
```

## Test coverage

The project includes:

- Schema validation
- Semantic validation
- Relationship validation
- Boundary/domain validation
- Primary-flow validation
- Orphan-node detection
- Duplicate ID detection
- View compilation tests
- Prompt regression tests
- API tests
- Negative test cases

## Project stages

The current project is a complete Phase 1/2 foundation:
1. Canonical Architecture Model
2. Validation engine
3. Pattern library
4. Deterministic local multi-agent orchestration
5. View compiler
6. Graph compiler
7. API
8. Modular frontend foundation
9. Regression suite

The `app/llm` package is intentionally provider-agnostic. Connect Vertex AI/Gemini only after the model contract and tests are stable.
