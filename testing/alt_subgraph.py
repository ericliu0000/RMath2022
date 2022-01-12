from manim import *
from constants import *

class AlternateSubgraph(Scene):
    def construct(self):
        g = Graph(AltSubgraphConstants.VERTICES,
                    AltSubgraphConstants.EDGES,
                    layout=AltSubgraphConstants.FULL_LAYOUT)
        
        self.play(Create(g))
        self.wait(LONG_PAUSE_TIME)

        # Indicate the subgraphs
        self.play(*bulk_indicate(g, AltSubgraphConstants.EDGES[14:24]), 
                    run_time=LONG_PAUSE_TIME)
        self.wait(LONG_PAUSE_TIME)

        # Remove edges to expose subgraphs
        for edge in AltSubgraphConstants.EDGES[24:]:
            self.play(g.animate(run_time=0.05).remove_edges(edge))
            self.wait(0.05)
        for (i, edge) in enumerate(AltSubgraphConstants.EDGES[:14]):
            self.play(g.animate(run_time=0.05).remove_edges(edge))
            self.wait(0.05)
        for i in range(1, 15):
            self.play(g.animate(run_time=0.05).remove_vertices(i))

        
        self.wait(LONG_PAUSE_TIME)

        # Change layout of graph
        self.play(g.animate(run_time=ANIMATION_TIME)
                .change_layout(AltSubgraphConstants.SPLIT_LAYOUT))

        # Indicate the subgraphs
        self.play(Indicate(g))
        self.wait(LONG_PAUSE_TIME)

        # Remove all graphs
        self.play(Uncreate(g))
        self.wait(PAUSE_TIME)
