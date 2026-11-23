"""
LLM-powered entity and relationship extractor.
Falls back gracefully to the deterministic extractor if LLM is unavailable.
"""
import logging
from typing import Any

logger = logging.getLogger(__name__)

ENTITY_EXTRACTION_PROMPT = '''
You are an enterprise architecture expert. Extract all architecture components from the following prompt.

Prompt: "{prompt}"

For each component, return an object with:
- "name": display name (e.g. "Microsoft Entra ID", "Kafka", "API Gateway")
- "type": one of: user, application, api, api_gateway, database, service, message_broker, identity_source, identity_provider, iga, pam, target_system, vpn, load_balancer, security, storage, compute, generic
- "technology": specific tech name if known (e.g. "PostgreSQL", "Apache Kafka"), or null
- "provider": cloud provider if known ("aws", "azure", "gcp", "on_premises"), or null

Return a JSON array of these objects. Include 3-12 components. Only include components actually mentioned or strongly implied by the prompt.
'''

RELATIONSHIP_EXTRACTION_PROMPT = '''
You are an enterprise architecture expert. Given these architecture components:
{elements_json}

And this original prompt:
"{prompt}"

Infer all meaningful relationships between components. For each relationship return:
- "source": id of source component (use the "id" field from above)
- "target": id of target component
- "type": one of: api, authentication, authorization, provisioning, sync, data_access, network, event, async, generic
- "protocol": protocol used (e.g. "HTTPS", "LDAP", "AMQP", "SCIM", "SQL", "OAuth2"), or null
- "label": short human-readable label (e.g. "Authenticate", "Provision", "Publish", "HTTPS")

Return a JSON array of relationships. Include only relationships justified by the prompt or standard architecture patterns.
'''


def extract_entities(prompt: str) -> list[dict[str, Any]]:
    """Use LLM to extract architecture entities from a prompt."""
    from app.llm.client import generate_json
    formatted = ENTITY_EXTRACTION_PROMPT.format(prompt=prompt)
    result = generate_json(formatted)
    if isinstance(result, list):
        return result
    if isinstance(result, dict) and "components" in result:
        return result["components"]
    return []


def extract_relationships(prompt: str, elements: list[dict]) -> list[dict[str, Any]]:
    """Use LLM to extract relationships from a prompt given a list of elements."""
    from app.llm.client import generate_json
    import json
    elements_json = json.dumps(elements, indent=2)
    formatted = RELATIONSHIP_EXTRACTION_PROMPT.format(
        elements_json=elements_json,
        prompt=prompt,
    )
    result = generate_json(formatted)
    if isinstance(result, list):
        return result
    if isinstance(result, dict) and "relationships" in result:
        return result["relationships"]
    return []
