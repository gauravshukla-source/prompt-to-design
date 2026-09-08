import re
from app.models.architecture import Domain, Element
from app.models.enterprise import Boundary

class BoundaryIntelligence:
    def detect(self,prompt:str,domains:list[Domain],elements:list[Element]):
        text=prompt.lower(); out=[]
        for d in domains:
            if d.type.value in {'cloud','on_premises','saas'}:
                out.append(Boundary(id=f'{d.id}-boundary',name=d.name,type='deployment',domain_id=d.id))
        rules=[
            ('trust',r'trust boundary|internet|external'),'network',
        ]
        if re.search(r'\bdmz\b|\bpublic subnet\b',text): out.append(Boundary(id='dmz-boundary',name='DMZ / Public Zone',type='security'))
        if re.search(r'\bprivate subnet\b|\bprivate network\b',text): out.append(Boundary(id='private-boundary',name='Private Network',type='network'))
        if re.search(r'\bvpc\b',text): out.append(Boundary(id='vpc-boundary',name='VPC',type='network'))
        if re.search(r'\btrust boundary\b',text): out.append(Boundary(id='trust-boundary',name='Trust Boundary',type='trust'))
        seen=set(); return [b for b in out if not (b.id in seen or seen.add(b.id))]
