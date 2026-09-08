from collections import defaultdict
from app.models.architecture import CanonicalArchitectureModel


class TopologyAnalyzer:
    """Classifies graph shape without relying on prompt-specific templates."""

    def analyze(self, model: CanonicalArchitectureModel) -> dict:
        ids = {e.id for e in model.elements}
        incoming = defaultdict(int)
        outgoing = defaultdict(int)
        adjacency = defaultdict(list)
        for r in model.relationships:
            if r.source in ids and r.target in ids and r.source != r.target:
                outgoing[r.source] += 1
                incoming[r.target] += 1
                adjacency[r.source].append(r.target)

        node_count = len(ids)
        edge_count = sum(outgoing.values())
        roots = [i for i in ids if incoming[i] == 0]
        leaves = [i for i in ids if outgoing[i] == 0]
        max_in = max(incoming.values(), default=0)
        max_out = max(outgoing.values(), default=0)
        domains = {e.domain_id for e in model.elements if e.domain_id}
        layers = {e.layer for e in model.elements if e.layer}
        physical_domains = [d for d in model.domains if str(d.type.value if hasattr(d.type, 'value') else d.type) != 'logical']

        has_branch_in = max_in >= 2
        has_branch_out = max_out >= 2
        hybrid = any('on-prem' in (d.name or '').lower() for d in model.domains) and any(
            'cloud' in (d.name or '').lower() or str(getattr(d, 'type', '')).lower().endswith('cloud')
            for d in model.domains
        )

        if hybrid:
            topology = 'hybrid'
        elif has_branch_in and has_branch_out:
            topology = 'hub_spoke'
        elif has_branch_in:
            topology = 'fan_in'
        elif has_branch_out:
            topology = 'fan_out'
        elif len(physical_domains) >= 2:
            topology = 'domain_flow'
        elif node_count > 1 and len(layers) >= 3:
            topology = 'layered'
        else:
            topology = 'linear'

        return {
            'topology': topology,
            'node_count': node_count,
            'edge_count': edge_count,
            'roots': roots,
            'leaves': leaves,
            'max_in_degree': max_in,
            'max_out_degree': max_out,
            'domain_count': len(domains),
            'layer_count': len(layers),
            'hybrid': hybrid,
            'has_fan_in': has_branch_in,
            'has_fan_out': has_branch_out,
        }
