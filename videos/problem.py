from manim import *
from constants import *


class ProblemGraph(Scene):
    def construct(self):
        graph = Graph(ProblemGraphConstants.VERTICES, 
                ProblemGraphConstants.EDGES,
                layout=ProblemGraphConstants.LAYOUT)

        self.play(Create(graph))
        self.wait(LONG_PAUSE_TIME)