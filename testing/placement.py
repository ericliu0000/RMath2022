from manim import *
from constants import *

class OptimalPlacement(Scene):
    def construct(self):
        graph = Graph(OptimalPlacementConstants.VERTICES, 
                OptimalPlacementConstants.EDGES, 
                layout=OptimalPlacementConstants.LAYOUT)

        self.play(Create(graph))
        self.wait(LONG_PAUSE_TIME)

        self.play(Uncreate(graph))
        self.wait(PAUSE_TIME)
