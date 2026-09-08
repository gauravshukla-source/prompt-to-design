from app.models.architecture import Flow, Relationship
from app.models.enums import FlowType

class FlowBuilder:
    def build(self, relationships: list[Relationship]) -> list[Flow]:
        if not relationships:
            return []
        outgoing = {r.source: r.target for r in relationships if r.source not in {x.target for x in relationships}}
        # Prefer a longest traversable chain; graph may branch.
        start = next(iter(outgoing), relationships[0].source)
        steps=[start]; seen={start}; current=start
        by_source={}
        for r in relationships: by_source.setdefault(r.source, []).append(r.target)
        while current in by_source:
            nxt=next((x for x in by_source[current] if x not in seen), None)
            if not nxt: break
            steps.append(nxt); seen.add(nxt); current=nxt
        if len(steps) < 2: steps=[relationships[0].source, relationships[0].target]
        return [Flow(id='primary-flow', name='Primary Architecture Flow', type=FlowType.PRIMARY, steps=steps, primary=True)]
