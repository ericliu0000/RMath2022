from manim import *
from constants import *

class Subgraph(Scene):
    def construct(self):
        graph = Graph(SubgraphConstants.VERTICES, 
                SubgraphConstants.EDGES, 
                layout=SubgraphConstants.FULL_LAYOUT)

        self.play(Create(graph))
        self.wait(2)

        self.play(graph.animate.change_layout(SubgraphConstants.EXPLODED_LAYOUT))
        self.wait(2)