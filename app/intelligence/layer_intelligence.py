from app.models.architecture import Element
from app.models.enums import ElementType

class LayerIntelligence:
    MAP={
        ElementType.USER:'presentation', ElementType.APPLICATION:'presentation',
        ElementType.API:'integration', ElementType.API_GATEWAY:'integration',
        ElementType.SERVICE:'application', ElementType.MESSAGE_BROKER:'integration',
        ElementType.DATABASE:'data', ElementType.STORAGE:'data',
        ElementType.IDENTITY_SOURCE:'identity', ElementType.IDENTITY_PROVIDER:'identity',
        ElementType.IGA:'identity', ElementType.PAM:'security', ElementType.SECURITY:'security',
        ElementType.VPN:'network', ElementType.CONNECTIVITY:'network',
        ElementType.LOAD_BALANCER:'network', ElementType.COMPUTE:'infrastructure',
    }
    def enrich(self,elements:list[Element]):
        for e in elements:
            if not e.layer: e.layer=self.MAP.get(e.type,'application')
        return elements
