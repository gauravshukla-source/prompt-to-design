"""
LLM-powered entity and relationship extractor.
Handles ANY user prompt: brief notes, typos, complex multi-cloud systems, or abstract scenarios.
Synthesizes a complete, standard-compliant enterprise architecture with proper layers.
"""
import logging
from typing import Any

logger = logging.getLogger(__name__)

SYSTEM_INSTRUCTION = """
You are a Principal Enterprise Solutions Architect.
Your task is to take ANY natural language prompt and generate a complete, publication-quality architecture diagram model.

CRITICAL RULES:
1. Handle ANY prompt: even if the prompt is short (e.g. "Saviynt EIC integrates with Active Directive on premise"), has typos (e.g. "Active Directive" -> "Active Directory", "entra" -> "Microsoft Entra ID"), or only names 1 or 2 systems.
2. Always produce a complete, multi-tier enterprise architecture with 4 to 10 components.
3. Automatically infer complementary components if the user only specified part of the system (e.g., if Saviynt EIC and on-prem Active Directory are mentioned, also include: Enterprise Users/Admins, Secure Connector/Gateway/VPN, Target Applications, and Cloud Control Plane).
4. Assign every component a valid "type" from:
   - user
   - application
   - api
   - api_gateway
   - database
   - service
   - message_broker
   - identity_source
   - identity_provider
   - iga
   - pam
   - target_system
   - vpn
   - load_balancer
   - security
   - storage
   - compute
   - generic
5. Define directional relationships between components with realistic enterprise protocols (HTTPS, LDAP, LDAPS, SCIM, REST, SQL, AMQP, OAuth2, SAML, gRPC).
6. Ensure EVERY component has at least one connection. Never leave orphan nodes.
"""

ARCHITECTURE_SYNTHESIS_PROMPT = """{system_instruction}

User Prompt: "{prompt}"

Return a single JSON object with this EXACT structure:
{{
  "architecture_name": "Title of Architecture",
  "components": [
    {{
      "id": "unique-slug-id",
      "name": "Component Display Name",
      "type": "valid_type_from_list",
      "technology": "Specific Technology (e.g. Saviynt, Active Directory, AWS, etc.)",
      "provider": "aws | azure | gcp | on_premises | saas"
    }}
  ],
  "relationships": [
    {{
      "source": "source-component-id",
      "target": "target-component-id",
      "type": "api | authentication | authorization | provisioning | sync | data_access | network | event | generic",
      "protocol": "HTTPS | LDAP | SCIM | REST | SQL | etc.",
      "label": "Action label (e.g. Provision, Sync, Authenticate, HTTPS)"
    }}
  ]
}}

Return ONLY valid JSON. No markdown fences, no explanation.
"""


def extract_architecture(prompt: str) -> dict[str, Any] | None:
    """
    Call LLM to extract full architecture components and relationships for ANY prompt.
    Returns dict with 'components' and 'relationships', or None if unavailable.
    """
    from app.llm.client import generate_json

    formatted = ARCHITECTURE_SYNTHESIS_PROMPT.format(
        system_instruction=SYSTEM_INSTRUCTION,
        prompt=prompt,
    )
    try:
        result = generate_json(formatted)
        if isinstance(result, dict) and "components" in result and len(result["components"]) >= 2:
            return result
    except Exception as exc:
        logger.info("LLM full architecture extraction failed: %s", exc)

    return None


def extract_entities(prompt: str) -> list[dict[str, Any]]:
    """Legacy helper for entity extraction."""
    arch = extract_architecture(prompt)
    if arch and "components" in arch:
        return arch["components"]
    return []


def extract_relationships(prompt: str, elements: list[dict]) -> list[dict[str, Any]]:
    """Legacy helper for relationship extraction."""
    arch = extract_architecture(prompt)
    if arch and "relationships" in arch:
        return arch["relationships"]
    return []
