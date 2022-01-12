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
        hare.move_to(g.vertices[6])

        # Initialize fox object
        fox = SVGMobject(FOX_FILE_NAME)
        fox.scale(HARE_SCALE)
        fox.move_to(g.vertices[7])

        # Initialize text
        text1_1 = MarkupText(f"Given any wheel graph, the fox and", color=TEXT_COLOR)
        text1_2 = MarkupText(f"hare begin adjacent to another.", color=TEXT_COLOR)
        text1_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text1_2.next_to(text1_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        

        text2_1 = MarkupText(f"Because the fox controls all vertices", color=TEXT_COLOR)
        text2_2 = MarkupText(f"from the middle, the hare loses.", color=TEXT_COLOR)
        text2_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text2_2.next_to(text2_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text3_1 = MarkupText(f"The hare cannot move to any other", color=TEXT_COLOR)
        text3_2 = MarkupText(f"vertices due to the fox's position.", color=TEXT_COLOR)
        text3_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text3_2.next_to(text3_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text4_1 = MarkupText(f"The hare is deceased", color=TEXT_COLOR)
        text4_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)

        # Create graph
        self.play(Create(g))

        # Add hare and fox
        self.play(FadeIn(hare, shift=UP, scale=0.1))
        self.play(FadeIn(fox, shift=UP, scale=0.1))

        # Add text section 1
        self.play(Create(text1_1), Create(text1_2))
        self.wait(LONG_PAUSE_TIME)

        # quickly move the hare to all other vertices
        FAST_SPEED = 0.1

        for i in range(1, len(g.vertices)):
            self.play(hare.animate().move_to(g.vertices[i]), run_time=FAST_SPEED, rate_func=smooth)
            self.wait()

        self.play(ReplacementTransform(text1_1, text2_1), 
                ReplacementTransform(text1_2, text2_2))
        self.wait(LONG_PAUSE_TIME)

        self.play(fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[6]))
        self.wait(PAUSE_TIME)

        # Cycle text section
        self.play(ReplacementTransform(text2_1, text3_1), 
                ReplacementTransform(text2_2, text3_2))
        self.wait(LONG_PAUSE_TIME)

        self.play(Uncreate(hare))
        self.wait(PAUSE_TIME)

        # Last text section
        self.play(ReplacementTransform(text3_1, text4_1), Uncreate(text3_2))
        self.wait(LONG_PAUSE_TIME)

        # Remove all objects
        self.play(Uncreate(g), FadeOut(text4_1), FadeOut(fox))
        self.wait(PAUSE_TIME)

        # uncreate the hare and the grph 
        self.play(Uncreate(hare), Uncreate(g))
        self.wait(PAUSE_TIME)
