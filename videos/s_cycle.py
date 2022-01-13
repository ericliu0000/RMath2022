from manim import *
from constants import *

class ThreeCycle(Scene):
    def construct(self):
        graph = Graph(ThreeCycleGraphConstants.VERTICES,
                    ThreeCycleGraphConstants.EDGES,
                    layout=ThreeCycleGraphConstants.LAYOUT)
        
        # Create fox and hare objects
        fox = SVGMobject(FOX_FILE_NAME)
        fox.scale(FOX_SCALE)
        fox.move_to(graph.vertices[3])

        hare = SVGMobject(HARE_FILE_NAME)
        hare.scale(HARE_SCALE)
        hare.move_to(graph.vertices[1])

        # Make text
        text1_1 = MarkupText(f"No matter the starting positions,", color=TEXT_COLOR)
        text1_2 = MarkupText(f"the hare is immediately cornered.", color=TEXT_COLOR)
        text1_1.shift(ThreeCycleGraphConstants.TEXT_SHIFT)
        text1_2.next_to(text1_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text2_1 = MarkupText(f"As all vertices are interconnected,", color=TEXT_COLOR)
        text2_2 = MarkupText(f"the fox can move anywhere and win.", color=TEXT_COLOR)
        text2_1.shift(ThreeCycleGraphConstants.TEXT_SHIFT)
        text2_2.next_to(text2_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text3_1 = MarkupText(f"The hare is deceased", color=TEXT_COLOR)
        text3_1.shift(ThreeCycleGraphConstants.TEXT_SHIFT)

        # Make graph and pause
        self.play(Create(graph))
        self.wait(PAUSE_TIME)

        # Add fox and hare
        self.play(Create(fox), Create(hare))
        self.wait(PAUSE_TIME)

        # Cycle through text and movements
        self.play(Create(text1_1), Create(text1_2))
        self.wait(LONG_PAUSE_TIME)

        self.play(ReplacementTransform(text1_1, text2_1),
                    ReplacementTransform(text1_2, text2_2),
                    fox.animate.move_to(graph.vertices[1]))
        self.wait(LONG_PAUSE_TIME)

        self.play(ReplacementTransform(text2_1, text3_1), Uncreate(text2_2))
        self.wait(PAUSE_TIME)
        self.play(Uncreate(hare))

        # Remove objects
        self.wait(PAUSE_TIME)
        self.play(Uncreate(text3_1), Uncreate(fox), Uncreate(graph))
        self.wait(PAUSE_TIME)

