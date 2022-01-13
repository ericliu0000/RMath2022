from manim import *
from constants import *

class TwoFoxCycle(Scene):
    def construct(self):
        # Create 6 cycle graph
        g = Graph(CycleGraphConstants.VERTICES, 
                    CycleGraphConstants.EDGES, 
                    layout=CycleGraphConstants.LAYOUT).shift(
                        CycleGraphConstants.GRAPH_OFFSET)

        # Initialize hare object
        hare = SVGMobject(HARE_FILE_NAME)
        hare.scale(FOX_SCALE)
        hare.move_to(g.vertices[6])

        # Initialize fox object
        fox1 = SVGMobject(FOX_FILE_NAME)
        fox1.scale(HARE_SCALE)
        fox1.move_to(g.vertices[3])
        
        fox2 = SVGMobject(FOX_FILE_NAME)
        fox2.scale(HARE_SCALE)
        fox2.move_to(g.vertices[4])
        
        # Make text
        text1_1 = MarkupText(f"The hare and foxes begin", color=TEXT_COLOR)
        text1_2 = MarkupText(f"opposite from another.", color=TEXT_COLOR)
        text1_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text1_2.next_to(text1_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text2_1 = MarkupText(f"The distance between the hare", color=TEXT_COLOR)
        text2_2 = MarkupText(f"and the fox is floor((n - 1) / 2)", color=TEXT_COLOR)
        text2_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text2_2.next_to(text2_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text3_1 = MarkupText(f"Thus, it takes floor((n - 1) / 2)", color=TEXT_COLOR)
        text3_2 = MarkupText(f"moves for the foxes to reach the hare.", color=TEXT_COLOR)
        text3_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text3_2.next_to(text3_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text4_1 = MarkupText(f"Now, the hare is deceased", color=TEXT_COLOR)
        text4_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)

        # Create graph and wait
        self.play(Create(g))
        self.wait(PAUSE_TIME)
        
        # Add hare and foxes
        self.play(FadeIn(hare, shift=UP, scale=0.1))
        self.play(FadeIn(fox1, shift=UP, scale=0.1), FadeIn(fox2, shift=UP, scale=0.1))

        # Add text1 and pause
        self.play(Create(text1_1), Create(text1_2))
        self.wait(LONG_PAUSE_TIME)

        # Remove text, shift foxes, and add new text
        self.play(ReplacementTransform(text1_1, text2_1), 
                    ReplacementTransform(text1_2, text2_2),
                    fox1.animate(run_time=ANIMATION_TIME).move_to(g.vertices[2]), 
                    fox2.animate(run_time=ANIMATION_TIME).move_to(g.vertices[5]))
        self.wait(LONG_PAUSE_TIME)

        # Cycle text again
        self.play(ReplacementTransform(text2_1, text3_1), 
                    ReplacementTransform(text2_2, text3_2),
                    fox1.animate(run_time=ANIMATION_TIME).move_to(g.vertices[1]), 
                    fox2.animate(run_time=ANIMATION_TIME).move_to(g.vertices[6]))
        self.wait(LONG_PAUSE_TIME)

        # Show final text
        self.play(ReplacementTransform(text3_1, text4_1), FadeOut(text3_2))
        self.play(Uncreate(hare))
        self.wait(LONG_PAUSE_TIME)

        # Remove text and animals
        self.play(Uncreate(text4_1), Uncreate(fox1), Uncreate(fox2))
        self.play(Uncreate(g))
        self.wait(PAUSE_TIME)


