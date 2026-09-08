class CandidateLayoutGenerator:
    def generate(self, topology: dict, model) -> list[str]:
        kind = topology['topology']
        candidates = []
        if kind == 'hybrid':
            candidates += ['hybrid_horizontal', 'domain_horizontal', 'layered_horizontal']
        elif kind in {'fan_in', 'fan_out', 'hub_spoke'}:
            candidates += ['branching_horizontal', 'layered_horizontal', 'branching_vertical']
        elif kind == 'domain_flow':
            candidates += ['domain_horizontal', 'layered_horizontal', 'layered_vertical']
        elif kind == 'layered':
            candidates += ['layered_horizontal', 'layered_vertical', 'domain_horizontal']
        else:
            candidates += ['linear_horizontal', 'linear_vertical', 'layered_horizontal']
        # Preserve order and remove duplicates.
        return list(dict.fromkeys(candidates))
