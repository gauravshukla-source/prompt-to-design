import re
from app.models.architecture import Domain, Element
from app.models.enums import DomainType, ElementType

class DomainIntelligence:
    CLOUD_PROVIDERS = [
        ("aws", "AWS Cloud", "aws"),
        ("amazon web services", "AWS Cloud", "aws"),
        ("azure", "Microsoft Azure", "azure"),
        ("microsoft azure", "Microsoft Azure", "azure"),
        ("gcp", "Google Cloud", "gcp"),
        ("google cloud", "Google Cloud", "gcp"),
    ]

    def enrich(self, prompt: str, elements: list[Element], domains: list[Domain] | None = None):
        text = prompt.lower()
        domains = list(domains or [])
        by_id = {d.id: d for d in domains}

        def add(id, name, typ, provider=None, parent_id=None):
            if id not in by_id:
                d = Domain(id=id, name=name, type=typ, provider=provider, parent_id=parent_id)
                domains.append(d)
                by_id[id] = d
            return by_id[id]

        # On-premises domain check (matches on-prem, on-premises, on premise, on prem, datacenter)
        if re.search(r'\bon[- ]prem(?:ises?|ise)?\b|\bdata\s*cent(?:er|re)\b', text):
            add('on-premises', 'On-Premises Infrastructure', DomainType.ON_PREMISES)

        # Cloud provider checks
        for key, name, provider in self.CLOUD_PROVIDERS:
            if key in text:
                add(provider, name, DomainType.CLOUD, provider=provider)

        # Generic cloud check
        if 'cloud' in text and not any(d.type == DomainType.CLOUD for d in domains):
            add('cloud', 'Cloud Environment', DomainType.CLOUD)

        # SaaS / Identity Cloud check
        if re.search(r'\bsaviynt\b|\beic\b|\bsalesforce\b|\bservicenow\b|\bworkday\b|\bsaas\b|\bokta\b', text):
            add('saas-identity-cloud', 'SaaS & Identity Cloud', DomainType.SAAS)

        # Logical fallback domains
        if not domains:
            add('presentation-layer', 'Presentation Layer', DomainType.LOGICAL)
            add('application-layer', 'Application Layer', DomainType.LOGICAL)
            add('data-layer', 'Data Layer', DomainType.LOGICAL)

        data_types = {ElementType.DATABASE, ElementType.STORAGE}
        identity_types = {ElementType.IDENTITY_SOURCE, ElementType.IDENTITY_PROVIDER, ElementType.IGA, ElementType.PAM}
        explicit_cloud = next((d.id for d in domains if d.type == DomainType.CLOUD), None)
        explicit_onprem = next((d.id for d in domains if d.type == DomainType.ON_PREMISES), None)
        saas = next((d.id for d in domains if d.type == DomainType.SAAS), None)

        for e in elements:
            if e.domain_id:
                continue
            n = (e.name + ' ' + (e.technology or '')).lower()

            if saas and any(x in n for x in ['saviynt', 'eic', 'salesforce', 'servicenow', 'workday', 'saas', 'okta']):
                e.domain_id = saas
            elif explicit_onprem and ('on-prem' in n or 'active directory' in n or 'active directive' in n or 'legacy' in n or 'ldap' in n):
                e.domain_id = explicit_onprem
            elif explicit_cloud and ('cloud' in n or any(k in text for k, _, __ in self.CLOUD_PROVIDERS) or e.type in data_types):
                e.domain_id = explicit_cloud
            elif saas:
                e.domain_id = saas
            elif not any(d.type in (DomainType.CLOUD, DomainType.ON_PREMISES) for d in domains):
                if e.type in data_types:
                    e.domain_id = 'data-layer'
                elif e.type in {ElementType.USER}:
                    e.domain_id = 'presentation-layer'
                elif e.type in identity_types:
                    add('identity-layer', 'Identity Layer', DomainType.LOGICAL)
                    e.domain_id = 'identity-layer'
                else:
                    e.domain_id = 'application-layer'
            elif explicit_onprem:
                e.domain_id = explicit_onprem
            elif explicit_cloud:
                e.domain_id = explicit_cloud

        return domains, elements
