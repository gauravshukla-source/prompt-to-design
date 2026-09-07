# Phase 5 — Architecture Pattern Intelligence & Template Engine

## What changed
Phase 5 replaces generic graph placement with pattern-aware visual composition.

### Supported patterns
1. three_tier
2. microservices
3. event_driven
4. iam
5. hybrid_cloud
6. zero_trust
7. data_pipeline
8. generic (hybrid fallback)

## Pipeline
Prompt
 -> Gemini semantic architecture
 -> Pattern classification
 -> Template selection
 -> Pattern node placement
 -> Boundary styling
 -> Orthogonal connector routing
 -> Enterprise diagram

## Backend
agent.py:
- Adds pattern and layoutStrategy to structured output.
- Adds deterministic pattern inference when Gemini omits metadata.
- Keeps Vertex AI + ADC authentication.
- Uses GEMINI_MODEL env override, defaulting to gemini-2.5-flash.

## Frontend
app.js:
- Pattern-specific placement for all 8 patterns.
- Microservices and data resources use peer rows, not fake sequential chains.
- IAM uses Users -> IdP -> IGA/IAM -> Targets composition.
- Event-driven uses Producers -> Broker -> Consumers.
- Hybrid uses On-Prem -> Connectivity -> Cloud.
- Connectors are routed after final placement.

## Install
Replace:
- static/app.js
- backend/agent.py
- backend/main.py (included unchanged for synchronized deployment)

Restart the backend and hard refresh with Ctrl+F5.

## Recommended first tests
1. AWS three-tier web application with ECS, RDS and Redis
2. IAM architecture using Saviynt, Entra ID, Active Directory, ServiceNow and SaaS
3. Event-driven microservices using Kafka
4. Hybrid cloud with on-prem AD connected to AWS
