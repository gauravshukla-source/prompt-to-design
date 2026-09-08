from dataclasses import dataclass
from app.models.architecture import CanonicalArchitectureModel, Element
from app.models.enums import ElementType


@dataclass
class CoverageResult:
    expected: list[str]
    matched: list[str]
    missing: list[str]
    score: float
    semantic_matches: list[dict]


@dataclass(frozen=True)
class ConceptSpec:
    canonical: str
    keywords: tuple[str, ...]
    aliases: tuple[str, ...] = ()
    element_types: tuple[ElementType, ...] = ()


class PromptCoverage:
    """
    Prompt coverage is semantic, not literal.

    A prompt concept such as "Web Application" may be represented by
    "React Frontend". Likewise "Database" may be represented by PostgreSQL
    or MongoDB. The validator therefore checks canonical concepts, aliases,
    technology names and element types before declaring a concept missing.
    """

    CONCEPTS = (
        ConceptSpec(
            "React Frontend",
            ("react", "frontend"),
            ("react frontend", "web frontend", "web application", "spa", "single page application"),
            (ElementType.APPLICATION,),
        ),
        ConceptSpec(
            "Web Application",
            ("web application", "web app"),
            ("web application", "web frontend", "frontend", "react frontend", "angular frontend", "vue frontend", "spa"),
            (ElementType.APPLICATION,),
        ),
        ConceptSpec(
            "Backend API",
            ("backend api",),
            ("backend api", "api", "rest api", "graphql api", "service api"),
            (ElementType.API,),
        ),
        ConceptSpec(
            "PostgreSQL Database",
            ("postgresql", "postgres"),
            ("postgresql", "postgres", "database"),
            (ElementType.DATABASE,),
        ),
        ConceptSpec(
            "Database",
            ("database", "databases"),
            ("database", "postgresql", "postgres", "mongodb", "mongo", "mysql", "oracle", "sql server", "cloud database"),
            (ElementType.DATABASE,),
        ),
        ConceptSpec(
            "Mobile Application",
            ("mobile application", "mobile app"),
            ("mobile application", "mobile app", "ios app", "android app"),
            (ElementType.APPLICATION,),
        ),
        ConceptSpec(
            "API Gateway",
            ("api gateway",),
            ("api gateway", "apigee", "kong", "api management", "aws api gateway"),
            (ElementType.API_GATEWAY,),
        ),
        ConceptSpec(
            "Backend Microservices",
            ("backend microservices", "microservices", "microservice"),
            ("backend microservices", "microservices", "microservice", "service"),
            (ElementType.SERVICE,),
        ),
        ConceptSpec(
            "Redis Cache",
            ("redis",),
            ("redis", "redis cache", "cache"),
            (ElementType.STORAGE,),
        ),
        ConceptSpec(
            "MongoDB Database",
            ("mongodb", "mongo"),
            ("mongodb", "mongo", "database"),
            (ElementType.DATABASE,),
        ),
        ConceptSpec(
            "On-Prem Application",
            ("on-prem applications", "on premises applications", "on-prem application"),
            ("on-prem application", "on premises application", "legacy application", "application"),
            (ElementType.APPLICATION,),
        ),
        ConceptSpec(
            "Cloud API",
            ("cloud api", "cloud apis"),
            ("cloud api", "api", "backend api"),
            (ElementType.API,),
        ),
        ConceptSpec(
            "Cloud Database",
            ("cloud database", "cloud databases"),
            ("cloud database", "database", "postgresql", "mongodb", "cloud sql"),
            (ElementType.DATABASE,),
        ),
        ConceptSpec(
            "VPN",
            ("vpn", "site-to-site vpn", "site to site vpn"),
            ("vpn", "private connectivity", "secure connection"),
            (ElementType.VPN, ElementType.CONNECTIVITY),
        ),
        ConceptSpec(
            "Kafka",
            ("kafka",),
            ("kafka", "event broker", "message broker", "event stream"),
            (ElementType.MESSAGE_BROKER,),
        ),
        ConceptSpec(
            "Identity Provider",
            ("identity provider", "idp"),
            ("identity provider", "idp", "entra id", "microsoft entra", "okta", "ping identity"),
            (ElementType.IDENTITY_PROVIDER,),
        ),
        ConceptSpec(
            "Microsoft Entra ID",
            ("entra id", "microsoft entra"),
            ("microsoft entra id", "entra id", "identity provider"),
            (ElementType.IDENTITY_PROVIDER,),
        ),
        ConceptSpec(
            "Active Directory",
            ("active directory",),
            ("active directory", "ad", "directory"),
            (ElementType.IDENTITY_SOURCE,),
        ),
        ConceptSpec(
            "Identity Governance",
            ("identity governance", "iga"),
            ("identity governance", "iga", "saviynt"),
            (ElementType.IGA,),
        ),
        ConceptSpec(
            "Saviynt IGA",
            ("saviynt",),
            ("saviynt", "saviynt iga", "identity governance", "iga"),
            (ElementType.IGA,),
        ),
        ConceptSpec(
            "Privileged Access Management",
            ("privileged access management", "pam"),
            ("privileged access management", "pam", "cyberark"),
            (ElementType.PAM,),
        ),
    )

    def _expected_specs(self, prompt: str) -> list[ConceptSpec]:
        text = prompt.lower()
        expected: list[ConceptSpec] = []
        seen: set[str] = set()

        for spec in self.CONCEPTS:
            if any(keyword in text for keyword in spec.keywords):
                if spec.canonical not in seen:
                    expected.append(spec)
                    seen.add(spec.canonical)
        return expected

    @staticmethod
    def _normalized_element_text(element: Element) -> str:
        return " ".join(
            part for part in (
                element.name,
                element.technology or "",
                element.provider or "",
            ) if part
        ).lower()

    def _match(self, spec: ConceptSpec, element: Element) -> tuple[bool, str]:
        text = self._normalized_element_text(element)
        aliases = {spec.canonical.lower(), *spec.aliases}

        if text in aliases or any(alias in text for alias in aliases):
            return True, "semantic_alias"

        if element.type in spec.element_types:
            return True, "element_type"

        return False, ""

    def evaluate(self, prompt: str, model: CanonicalArchitectureModel) -> CoverageResult:
        specs = self._expected_specs(prompt)

        expected: list[str] = []
        matched: list[str] = []
        missing: list[str] = []
        semantic_matches: list[dict] = []

        for spec in specs:
            expected.append(spec.canonical)
            best_match = None

            for element in model.elements:
                ok, match_kind = self._match(spec, element)
                if ok:
                    best_match = (element, match_kind)
                    break

            if best_match:
                element, match_kind = best_match
                matched.append(spec.canonical)
                semantic_matches.append(
                    {
                        "concept": spec.canonical,
                        "element": element.name,
                        "match_type": match_kind,
                    }
                )
            else:
                missing.append(spec.canonical)

        score = 100.0 if not expected else round(
            100 * len(set(matched)) / len(set(expected)), 2
        )

        return CoverageResult(
            expected=expected,
            matched=matched,
            missing=missing,
            score=score,
            semantic_matches=semantic_matches,
        )
