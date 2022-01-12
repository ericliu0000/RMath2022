from manim import *
from constants import *

class Subgraph(Scene):
    def construct(self):
        graph = Graph(SubgraphConstants.VERTICES, 
                SubgraphConstants.EDGES, 
                layout=SubgraphConstants.FULL_LAYOUT).shift(UP * 0.5)

        # Make fox and hare objects
        hare = SVGMobject(HARE_FILE_NAME)
        hare.scale(FOX_SCALE)
        hare.move_to(graph.vertices[3])

        fox = SVGMobject(FOX_FILE_NAME)
        fox.scale(HARE_SCALE)
        fox.move_to(graph.vertices[7])

        # Make text objects
        text1_1 = MarkupText(f"More complex graphs can be split", color=TEXT_COLOR)
        text1_2 = MarkupText(f"into rudimentary cycle graphs.", color=TEXT_COLOR)
        text1_1.shift(SubgraphConstants.TEXT_SHIFT)
        text1_2.next_to(text1_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text2_1 = MarkupText(f"This 2-fox graph contains three", color=TEXT_COLOR)
        text2_2 = MarkupText(f"sub-cycles: a 5-cycle, and two 3-cycles.", color=TEXT_COLOR)
        text2_1.shift(SubgraphConstants.TEXT_SHIFT)
        text2_2.next_to(text2_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text3_1 = MarkupText(f"The largest fox number sub-cycle", color=TEXT_COLOR)
        text3_2 = MarkupText(f"is the 5-cycle graph, at 2.", color=TEXT_COLOR)
        text3_1.shift(SubgraphConstants.TEXT_SHIFT)
        text3_2.next_to(text3_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text4_1 = MarkupText(f"Thus, the fox number of the", color=TEXT_COLOR)
        text4_2 = MarkupText(f"entire graph is 2.", color=TEXT_COLOR)
        text4_1.shift(SubgraphConstants.TEXT_SHIFT)
        text4_2.next_to(text4_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

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

        self.wait(PAUSE_TIME)
        self.play(graph.animate(run_time=ANIMATION_TIME * 2).change_layout(SubgraphConstants.EXPLODED_LAYOUT))

        # Continue iterating through text
        self.play(ReplacementTransform(text2_1, text3_1),
            ReplacementTransform(text2_2, text3_2))
        self.wait(PAUSE_TIME)

        self.play(ReplacementTransform(text3_1, text4_1),
            ReplacementTransform(text3_2, text4_2))
        self.wait(PAUSE_TIME)

        # Reunite graph, show fox and hare        # End time truncation section
        self.play(graph.animate(run_time=ANIMATION_TIME * 2).change_layout(SubgraphConstants.FULL_LAYOUT))
        self.play(Create(hare), Create(fox))
        self.wait(PAUSE_TIME)

        # Indicate starting positions
        self.play(*bulk_indicate_points(graph, [1]))
        self.wait(PAUSE_TIME)

        # Play game
        for hare_pos, fox_pos in SubgraphConstants.MOVES:
            self.play(fox.animate(run_time=ANIMATION_TIME).move_to(graph.vertices[fox_pos]))
            self.wait(0.1)
            self.play(hare.animate(run_time=ANIMATION_TIME).move_to(graph.vertices[hare_pos]))
            self.wait(PAUSE_TIME / 2)


        self.wait(PAUSE_TIME)

