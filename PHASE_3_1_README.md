# Phase 3.1 - Enterprise Architecture Intelligence

This release adds deterministic enterprise architecture enrichment after canonical extraction:

- Domain Intelligence: on-premises, AWS, Azure, GCP, generic cloud, SaaS and logical layers.
- Layer Intelligence: presentation, integration, application, data, identity, security, network and infrastructure.
- Boundary Intelligence: deployment, VPC, private network, DMZ and trust boundaries when present in the prompt.
- Flow Intelligence: relationship flow metadata and protocol/security hints.
- Composition Planner: the renderer receives a composition plan instead of inventing architecture grouping.

The LLM/extraction stage remains responsible for understanding the prompt; deterministic intelligence enriches and validates the canonical model.
