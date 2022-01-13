from manim import *
from constants import *


class ProblemGraph(Scene):
    def construct(self):
        graph = Graph(ProblemGraphConstants.VERTICES, 
                ProblemGraphConstants.EDGES,
                layout=ProblemGraphConstants.FULL_LAYOUT)

        # Create text
        text1 = MarkupText(f"What is the fox number of this graph?", color=TEXT_COLOR)
        text1.next_to(graph, DOWN, buff=TOP_TEXT_BUFFER*2)

        text2 = MarkupText(f"Step 1: Optimization", color=TEXT_COLOR)
        text2.next_to(graph, DOWN, buff=TOP_TEXT_BUFFER*2)

        text3 = MarkupText(f"Step 2: Subgraphs", color=TEXT_COLOR)
        text3.next_to(graph, DOWN, buff=TOP_TEXT_BUFFER*2)

        text4 = MarkupText(f"This is a 2 fox graph", color=TEXT_COLOR)
        text4.next_to(graph, DOWN, buff=TOP_TEXT_BUFFER*2)

        # Make graph and text
        self.play(Create(graph))
        self.play(Create(text1))
        self.wait(LONG_PAUSE_TIME)

        # Indicate place to optimize
        self.play(ReplacementTransform(text1, text2))
        self.play(*bulk_indicate(graph, [(20, 21), (21, 22), (22, 23), (23, 24)]),
                *bulk_indicate_points(graph, [20, 21, 22, 23, 24]))
        self.wait(PAUSE_TIME)
        self.play(graph.animate.remove_vertices(20, 21, 22, 23, 24))

        self.play(ReplacementTransform(text2, text3))
        self.play(graph.animate.change_layout(ProblemGraphConstants.SPLIT_LAYOUT))
        self.wait(PAUSE_TIME)

        self.play(ReplacementTransform(text3, text4))
        self.play(Indicate(graph, scale_factor=1.2))
        self.wait(PAUSE_TIME)
