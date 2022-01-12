from manim import *
from constants import *

class Subgraph(Scene):
    def construct(self):
        graph = Graph(SubgraphConstants.VERTICES, 
                SubgraphConstants.EDGES, 
                layout=SubgraphConstants.FULL_LAYOUT)

        # Make text objects
        text1_1 = MarkupText(f"More complex graphs can be split", color=TEXT_COLOR)
        text1_2 = MarkupText(f"into rudimentary cycle graphs.", color=TEXT_COLOR)
        text1_1.shift(SubgraphConstants.TEXT_SHIFT)
        text1_2.next_to(text1_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text2_1 = MarkupText(f"This 2-fox graph contains three:", color=TEXT_COLOR)
        text2_2 = MarkupText(f"sub-cycles: a 5-cycle, and two 3-cycles.", color=TEXT_COLOR)
        text2_1.shift(SubgraphConstants.TEXT_SHIFT)
        text2_2.next_to(text2_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text3_1 = MarkupText(f"The 5-cycle is the largest sub-cycle.", color=TEXT_COLOR)
        text3_1.shift(SubgraphConstants.TEXT_SHIFT)

        # Create graph objects
        self.play(Create(graph))
        self.wait(2)

        # Cycle through text, begin truncated times
        self.play(Write(text1_1), Write(text1_2))
        self.wait(PAUSE_TIME)

        self.play(ReplacementTransform(text1_1, text2_1),
            ReplacementTransform(text1_2, text2_2))
        self.wait(PAUSE_TIME)

        # Indicate subgraphs sequentially
        self.play(*bulk_indicate(graph, [(1, 3), (2, 11), (2, 13)]),
            run_time=ANIMATION_TIME, *bulk_indicate_points(graph, [11, 2, 13]))
        self.wait(PAUSE_TIME / 2)

        self.play(*bulk_indicate(graph, [(16, 18), (18, 7), (7, 16)]),
            *bulk_indicate_points(graph, [16, 18, 7]))
        self.wait(PAUSE_TIME / 2)

        self.play(*bulk_indicate(graph, [(1, 3), (3, 4), (4, 5), (5, 6), 
            (16, 18), (8, 1)]), 
            *bulk_indicate_points(graph, [11, 13, 4, 5, 16, 18]))

        # Continue iterating through text
        self.play(ReplacementTransform(text2_1, text3_1),
            ReplacementTransform(text2_2, text3_1))
        self.wait(PAUSE_TIME)

        self.play(graph.animate(run_time=ANIMATION_TIME * 2).change_layout(SubgraphConstants.EXPLODED_LAYOUT))
        self.wait(2)

