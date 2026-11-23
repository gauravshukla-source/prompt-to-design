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
        s = re.sub(r'[^a-z0-9]+', '-', value.lower()).strip('-')
        return s or 'component'

    def _llm_extract(self, prompt: str, intent: IntentResult) -> CanonicalArchitectureModel | None:
        """Attempt LLM-powered extraction for ANY prompt. Returns None on failure."""
        try:
            from app.llm.llm_extractor import extract_architecture

            arch = extract_architecture(prompt)
            if not arch or "components" not in arch:
                return None

            raw_entities = arch.get("components", [])
            if not raw_entities or len(raw_entities) < 2:
                return None

            elements: list[Element] = []
            used: set[str] = set()

            for raw in raw_entities:
                name = str(raw.get("name", "")).strip()
                if not name:
                    continue
                eid = raw.get("id") or self._slug(name)
                eid = self._slug(eid)
                base = eid
                i = 2
                while eid in used:
                    eid = f"{base}-{i}"
                    i += 1
                used.add(eid)

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

            if len(elements) < 2:
                return None

            domains, elements = self.domains.resolve(prompt, elements)

            # Build relationships
            raw_rels = arch.get("relationships", [])
            id_set = {e.id for e in elements}
            relationships: list[Relationship] = []

            for i, raw in enumerate(raw_rels or []):
                src = self._slug(str(raw.get("source", "")).strip())
                tgt = self._slug(str(raw.get("target", "")).strip())
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

            # If LLM didn't return relationships, use the universal relationship extractor
            if not relationships:
                relationships = self.relationships.extract(prompt, elements)

            if not relationships:
                return None

            flows = self.flows.build(relationships)
            return CanonicalArchitectureModel(
                architecture=ArchitectureMeta(
                    id="arch-001",
                    name=arch.get("architecture_name") or f"{intent.architecture_type.value.replace('_', ' ').title()} Architecture",
                    type=intent.architecture_type,
                    viewpoint=intent.viewpoint,
                    description=prompt,
                ),
                domains=domains,
                elements=elements,
                relationships=relationships,
                flows=flows,
                metadata={"generator": "llm-architecture-v1", "stage": "canonical"},
            )

        except Exception as exc:
            logger.info("LLM extraction failed (%s); using resilient deterministic extraction", exc)
            return None

    def extract(self, prompt: str, intent: IntentResult) -> CanonicalArchitectureModel:
        # Try LLM first if configured
        llm_result = self._llm_extract(prompt, intent)
        if llm_result is not None:
            logger.info("LLM extraction succeeded with %d elements and %d relationships",
                        len(llm_result.elements), len(llm_result.relationships))
            return llm_result

        # Resilient Deterministic Extractor (guaranteed to succeed on ANY prompt)
        extracted = self.entities.extract(prompt)
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
            elements.append(Element(
                id=eid,
                name=x.name,
                type=x.type,
                technology=x.technology,
                provider=x.provider
            ))

        domains, elements = self.domains.resolve(prompt, elements)
        relationships = self.relationships.extract(prompt, elements)
        flows = self.flows.build(relationships) if relationships else []

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
            metadata={"generator": "deterministic-extraction-v2", "stage": "canonical"},
        )
