import re
import logging
from app.models.architecture import ArchitectureMeta, CanonicalArchitectureModel, Element, Relationship
from app.models.enums import ArchitectureType, ElementType, RelationshipType
from app.extraction.entity_extractor import EntityExtractor
from app.extraction.relationship_extractor import RelationshipExtractor
from app.extraction.domain_resolver import DomainResolver
from app.extraction.flow_builder import FlowBuilder
from .intent_agent import IntentResult

logger = logging.getLogger(__name__)


class ArchitectureExtractionError(ValueError):
    pass


class ExtractionAgent:
    def __init__(self):
        self.entities = EntityExtractor()
        self.relationships = RelationshipExtractor()
        self.domains = DomainResolver()
        self.flows = FlowBuilder()

    @staticmethod
    def _slug(value: str) -> str:
        return re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-')

    def _llm_extract(self, prompt: str, intent: IntentResult) -> CanonicalArchitectureModel | None:
        """Attempt LLM-powered extraction. Returns None on any failure so deterministic fallback runs."""
        try:
            from app.llm.llm_extractor import extract_entities, extract_relationships

            raw_entities = extract_entities(prompt)
            if not raw_entities or len(raw_entities) < 2:
                logger.debug("LLM returned fewer than 2 entities; falling back to deterministic")
                return None

            elements: list[Element] = []
            used: set[str] = set()
            elem_dicts: list[dict] = []

            for raw in raw_entities:
                name = str(raw.get("name", "")).strip()
                if not name:
                    continue
                eid = self._slug(name)
                base = eid
                i = 2
                while eid in used:
                    eid = f"{base}-{i}"
                    i += 1
                used.add(eid)

                # Map LLM type string to ElementType
                type_str = str(raw.get("type", "generic")).lower().replace("-", "_")
                try:
                    etype = ElementType(type_str)
                except ValueError:
                    etype = ElementType.GENERIC

                elem = Element(
                    id=eid,
                    name=name,
                    type=etype,
                    technology=raw.get("technology"),
                    provider=raw.get("provider"),
                )
                elements.append(elem)
                elem_dicts.append({"id": eid, "name": name, "type": type_str})

            if len(elements) < 2:
                return None

            domains, elements = self.domains.resolve(prompt, elements)

            # LLM relationship extraction
            raw_rels = extract_relationships(prompt, elem_dicts)
            id_set = {e.id for e in elements}
            relationships: list[Relationship] = []

            for i, raw in enumerate(raw_rels or []):
                src = str(raw.get("source", "")).strip()
                tgt = str(raw.get("target", "")).strip()
                if src not in id_set or tgt not in id_set or src == tgt:
                    continue
                type_str = str(raw.get("type", "generic")).lower().replace("-", "_")
                try:
                    rtype = RelationshipType(type_str)
                except ValueError:
                    rtype = RelationshipType.GENERIC

                relationships.append(Relationship(
                    id=f"rel-{i + 1}",
                    source=src,
                    target=tgt,
                    type=rtype,
                    protocol=raw.get("protocol"),
                    label=raw.get("label"),
                ))

            # If LLM didn't return relationships, try deterministic relationship extractor on elements
            if not relationships:
                relationships = self.relationships.extract(prompt, elements)

            if not relationships:
                logger.debug("LLM produced no valid relationships; falling back to deterministic")
                return None

            flows = self.flows.build(relationships)
            return CanonicalArchitectureModel(
                architecture=ArchitectureMeta(
                    id="arch-001",
                    name=f"{intent.architecture_type.value.replace('_', ' ').title()} Architecture",
                    type=intent.architecture_type,
                    viewpoint=intent.viewpoint,
                    description=prompt,
                ),
                domains=domains,
                elements=elements,
                relationships=relationships,
                flows=flows,
                metadata={"generator": "llm-extraction-v1", "stage": "canonical"},
            )

        except Exception as exc:
            logger.info("LLM extraction not available or failed (%s); using deterministic extraction", exc)
            return None

    def extract(self, prompt: str, intent: IntentResult) -> CanonicalArchitectureModel:
        # Try LLM first if configured
        llm_result = self._llm_extract(prompt, intent)
        if llm_result is not None:
            logger.info("LLM extraction succeeded (%d elements, %d relationships)",
                        len(llm_result.elements), len(llm_result.relationships))
            return llm_result

        # Deterministic extraction fallback
        extracted = self.entities.extract(prompt)
        if len(extracted) < 2:
            raise ArchitectureExtractionError(
                "Unable to extract at least two architecture components from the prompt"
            )
        elements: list[Element] = []
        used: set[str] = set()
        for x in extracted:
            eid = self._slug(x.name)
            base = eid
            i = 2
            while eid in used:
                eid = f"{base}-{i}"
                i += 1
            used.add(eid)
            elements.append(Element(id=eid, name=x.name, type=x.type, technology=x.technology))
        domains, elements = self.domains.resolve(prompt, elements)
        relationships = self.relationships.extract(prompt, elements)
        if not relationships:
            raise ArchitectureExtractionError(
                "Components were extracted but no meaningful relationships could be derived"
            )
        flows = self.flows.build(relationships)
        return CanonicalArchitectureModel(
            architecture=ArchitectureMeta(
                id="arch-001",
                name=f"{intent.architecture_type.value.replace('_', ' ').title()} Architecture",
                type=intent.architecture_type,
                viewpoint=intent.viewpoint,
                description=prompt,
            ),
            domains=domains,
            elements=elements,
            relationships=relationships,
            flows=flows,
            metadata={"generator": "deterministic-extraction-v1", "stage": "canonical"},
        )
