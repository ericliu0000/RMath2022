from manim import *
from constants import *

class OptimalPlacement(Scene):
    def construct(self):
        # Create barbell graph
        graph = Graph(OptimalPlacementConstants.VERTICES, 
                OptimalPlacementConstants.EDGES, 
                layout=OptimalPlacementConstants.LAYOUT)

        # Initialize hare and fox objects
        hare = SVGMobject(HARE_FILE_NAME)
        hare.scale(FOX_SCALE)
        hare.move_to(graph.vertices[4])

        fox = SVGMobject(FOX_FILE_NAME)
        fox.scale(HARE_SCALE)
        fox.move_to(graph.vertices[1])

        # Initialize text objects
        text1_1 = MarkupText(f"The optimal positions favor the hare,", color=TEXT_COLOR)
        text1_2 = MarkupText(f"allowing it to best delay or escape loss.", color=TEXT_COLOR)
        text1_1.next_to(graph, DOWN, buff=TOP_TEXT_BUFFER)
        text1_2.next_to(text1_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text2_1 = MarkupText(f"Therefore, the hare will select a vertex", color=TEXT_COLOR)
        text2_2 = MarkupText(f"in the greatest fox number subgraph.", color=TEXT_COLOR)
        text2_1.next_to(graph, DOWN, buff=TOP_TEXT_BUFFER)
        text2_2.next_to(text2_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text3_1 = MarkupText(f"In this case, the hare will select any", color=TEXT_COLOR)
        text3_2 = MarkupText(f"vertex in the sub-4-cycle graph.", color=TEXT_COLOR)
        text3_1.next_to(graph, DOWN, buff=TOP_TEXT_BUFFER)
        text3_2.next_to(text3_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text4_1 = MarkupText(f"Furthermore, the hare will start on", color=TEXT_COLOR)
        text4_2 = MarkupText(f"the vertex with the greatest degree.", color=TEXT_COLOR)
        text4_1.next_to(graph, DOWN, buff=TOP_TEXT_BUFFER)
        text4_2.next_to(text4_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text5_1 = MarkupText(f"This maximizes the hare's movement", color=TEXT_COLOR)
        text5_2 = MarkupText(f"options, alleviating being cornered.", color=TEXT_COLOR)
        text5_1.next_to(graph, DOWN, buff=TOP_TEXT_BUFFER)
        text5_2.next_to(text5_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        # Create graph objects
        self.play(Create(graph))
        self.wait(PAUSE_TIME)

        # Cycle text, begin truncated pause section
        self.play(Create(text1_1), Create(text1_2))
        self.wait(PAUSE_TIME)

        self.play(ReplacementTransform(text1_1, text2_1),
                ReplacementTransform(text1_2, text2_2))
        self.wait(PAUSE_TIME)

        self.play(ReplacementTransform(text2_1, text3_1),
            ReplacementTransform(text2_2, text3_2))
        self.wait(PAUSE_TIME)

        # Indicate vertices
        self.play(*bulk_indicate_points(graph, [4, 5, 6, 7]),
            run_time=ANIMATION_TIME)
        self.wait(PAUSE_TIME)

        self.play(ReplacementTransform(text3_1, text4_1),
            ReplacementTransform(text3_2, text4_2))
        self.wait(PAUSE_TIME)

        self.play(ReplacementTransform(text4_1, text5_1),
            ReplacementTransform(text4_2, text5_2))
        self.wait(PAUSE_TIME)

        # Indicate best point
        self.play(Indicate(graph.vertices[4], scale_factor=2, 
            color=OptimalPlacementConstants.INDICATION_COLOR))
        self.wait(PAUSE_TIME)

        # Make hare show up
        self.play(Create(hare))


        # End truncated pause section


        self.play(Uncreate(graph))
        self.wait(PAUSE_TIME)
