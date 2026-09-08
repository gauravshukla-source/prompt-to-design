from app.models.architecture import CanonicalArchitectureModel
from app.models.enterprise import CompositionPlan, CompositionContainer
from app.models.enums import Viewpoint
from app.layout.topology_analyzer import TopologyAnalyzer
from app.layout.candidate_generator import CandidateLayoutGenerator
from app.layout.layout_scorer import LayoutScorer
from app.layout.viewport_optimizer import ViewportOptimizer


class CompositionPlanner:
    def __init__(self):
        self.topology = TopologyAnalyzer()
        self.candidates = CandidateLayoutGenerator()
        self.scorer = LayoutScorer()
        self.viewport = ViewportOptimizer()

    def plan(self, model: CanonicalArchitectureModel, viewpoint: Viewpoint):
        containers = []
        for d in model.domains:
            ids = [e.id for e in model.elements if e.domain_id == d.id]
            if ids:
                containers.append(
                    CompositionContainer(
                        id=d.id,
                        name=d.name,
                        kind='domain',
                        element_ids=ids,
                        parent_id=d.parent_id,
                    )
                )

        topology = self.topology.analyze(model)
        candidates = self.candidates.generate(topology, model)
        selected, scores = self.scorer.select(candidates, topology, model)
        viewport = self.viewport.recommend(topology, selected)

        return CompositionPlan(
            layout_strategy=selected,
            containers=containers,
            boundaries=model.boundaries,
            metadata={
                'layers': {e.id: e.layer for e in model.elements},
                'enterprise': True,
                'topology': topology,
                'layout_candidates': scores,
                'selected_layout': selected,
                'viewport': viewport,
            },
        )
