# Phase 3.2 - Adaptive Enterprise Layout Engine

This release preserves the existing extraction, validation, enterprise intelligence and renderer pipeline while replacing fixed layout selection with an adaptive composition pipeline.

## Pipeline
Prompt -> Canonical Model -> Enterprise Intelligence -> Topology Analysis -> Candidate Layouts -> Layout Scoring -> Viewport Optimization -> Renderer

## Topologies
- linear
- layered
- fan_in
- fan_out
- hub_spoke
- domain_flow
- hybrid

## Layout strategies
- linear_horizontal
- linear_vertical
- layered_horizontal
- layered_vertical
- branching_horizontal
- branching_vertical
- domain_horizontal
- hybrid_horizontal

## New modules
- app/layout/topology_analyzer.py
- app/layout/candidate_generator.py
- app/layout/layout_scorer.py
- app/layout/viewport_optimizer.py

## Key behavior
The engine no longer forces all architectures into a single top-to-bottom layout. It selects a layout based on graph topology, domains, layers and branching degree, then sends viewport guidance to the renderer.

## Validation
30 pytest tests pass.
