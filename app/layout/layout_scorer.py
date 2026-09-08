class LayoutScorer:
    """Deterministic scoring: semantic fit first, then readability and density."""

    def score(self, candidate: str, topology: dict, model) -> tuple[float, dict]:
        score = 50.0
        kind = topology['topology']
        n = max(topology['node_count'], 1)
        reasons = []

        if kind == 'hybrid' and candidate == 'hybrid_horizontal':
            score += 45; reasons.append('preserves hybrid domain boundaries')
        if kind in {'fan_in', 'fan_out', 'hub_spoke'} and candidate.startswith('branching'):
            score += 42; reasons.append('preserves branching topology')
        if kind == 'domain_flow' and candidate == 'domain_horizontal':
            score += 38; reasons.append('preserves domain-to-domain flow')
        if kind == 'layered' and candidate.startswith('layered'):
            score += 34; reasons.append('preserves architectural layers')
        if kind == 'linear' and candidate == 'linear_horizontal':
            score += 40; reasons.append('minimizes whitespace for linear flow')

        if candidate.endswith('horizontal'):
            score += min(20, n * 3); reasons.append('uses wide viewport efficiently')
        if candidate.endswith('vertical') and n <= 4:
            score -= 8; reasons.append('penalized for tall sparse composition')
        if topology['domain_count'] > 1 and 'domain' in candidate or 'hybrid' in candidate:
            score += 8
        if topology['layer_count'] <= 2 and candidate.startswith('layered_vertical'):
            score -= 12

        return score, {'score': round(score, 2), 'reasons': reasons}

    def select(self, candidates: list[str], topology: dict, model):
        scored = []
        for c in candidates:
            score, details = self.score(c, topology, model)
            scored.append({'strategy': c, **details})
        scored.sort(key=lambda x: x['score'], reverse=True)
        return scored[0]['strategy'], scored
