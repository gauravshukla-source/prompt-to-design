from app.models.architecture import Domain, Element
from app.models.enums import DomainType, ElementType

class DomainResolver:
    def resolve(self, prompt: str, elements: list[Element]) -> tuple[list[Domain], list[Element]]:
        text = prompt.lower()
        domains: list[Domain] = []
        if any(x in text for x in ['on-prem', 'on premises', 'data center']):
            domains.append(Domain(id='on-premises', name='On-Premises', type=DomainType.ON_PREMISES))
        if any(x in text for x in ['cloud', 'aws', 'azure', 'gcp', 'google cloud']):
            domains.append(Domain(id='cloud', name='Cloud', type=DomainType.CLOUD))
        if not domains:
            app_domain = Domain(id='application-layer', name='Application Layer', type=DomainType.LOGICAL)
            data_domain = Domain(id='data-layer', name='Data Layer', type=DomainType.LOGICAL)
            domains.extend([app_domain, data_domain])
            data_types={ElementType.DATABASE, ElementType.STORAGE}
            for e in elements:
                if e.type in data_types: e.domain_id='data-layer'
                else: e.domain_id='application-layer'
        return domains, elements
