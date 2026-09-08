class ViewportOptimizer:
    def recommend(self, topology: dict, strategy: str) -> dict:
        n = max(topology.get('node_count', 1), 1)
        branch = max(topology.get('max_in_degree', 1), topology.get('max_out_degree', 1))
        width = max(760, min(1800, 260 + n * 240))
        height = 560
        if strategy.endswith('vertical'):
            width = max(760, min(1200, 420 + branch * 220))
            height = max(560, min(1800, 180 + n * 190))
        elif 'branching' in strategy:
            height = max(560, 280 + branch * 180)
        elif 'hybrid' in strategy or 'domain' in strategy:
            height = max(560, 320 + topology.get('domain_count', 1) * 110)
        return {
            'min_width': width,
            'min_height': height,
            'fit': 'content',
            'padding': 64,
            'compact': strategy in {'linear_horizontal', 'domain_horizontal'},
        }
