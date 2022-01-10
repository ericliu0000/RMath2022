from manim import *
from constants import *

class WheelGraph(Scene):
    def construct(self):
        # Create w_7 graph
        g = Graph(WheelGraphConstants.VERTICES,
                    WheelGraphConstants.EDGES,
                    layout = WheelGraphConstants.LAYOUT)
        
        # Initialize hare object
        hare = SVGMobject(HARE_FILE_NAME)
        hare.scale(FOX_SCALE)
        hare.move_to(g.vertices[7])

        # Initialize fox object
        fox = SVGMobject(FOX_FILE_NAME)
        fox.scale(HARE_SCALE)
        fox.move_to(g.vertices[6])

        # Initialize text
        text1_1 = MarkupText(f"Given any wheel graph, the fox and", color=RED)
        text1_2 = MarkupText(f"hare are always adjacent to another.", color=RED)
        text1_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text1_2.next_to(text1_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        # Create graph
        self.play(Create(g))

        # Add hare and fox
        self.play(FadeIn(hare, shift=UP, scale=0.1))
        self.play(FadeIn(fox, shift=UP, scale=0.1))

        # Add text
        self.play(Create(text1_1), Create(text1_2))
    

        self.wait(LONG_PAUSE_TIME)


