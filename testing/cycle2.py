from manim import *
from constants import *

class TwoFoxCycle(Scene):
    def construct(self):
        next_text_time = 4
        animation_time = 1

        # Create 6 cycle graph
        g = Graph(CycleGraphConstants.VERTICES, 
                    CycleGraphConstants.EDGES, 
                    layout=CycleGraphConstants.LAYOUT)

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
        text1_1 = MarkupText(f"The hare and foxes begin", color=RED)
        text1_2 = MarkupText(f"opposite from another.", color=RED)
        text1_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text1_2.next_to(text1_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text2_1 = MarkupText(f"The distance between the hare", color=RED)
        text2_2 = MarkupText(f"and the fox is floor((n - 1) / 2)", color=RED)
        text2_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text2_2.next_to(text2_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text3_1 = MarkupText(f"Thus, it takes floor((n - 1) / 2)", color=RED)
        text3_2 = MarkupText(f"moves for the foxes to reach the hare.", color=RED)
        text3_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text3_2.next_to(text3_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text4_1 = MarkupText(f"Now, the hare is deceased", color=RED)
        text4_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)

        # Create graph and wait
        self.play(Create(g))
        self.wait(ANIMATION_TIME)
        
        # Add hare and foxes
        self.play(FadeIn(hare, shift=UP, scale=0.1))
        self.play(FadeIn(fox1, shift=UP, scale=0.1), FadeIn(fox2, shift=UP, scale=0.1))

        # Add text1 and pause
        self.play(Create(text1_1), Create(text1_2))
        self.wait(ANIMATION_TIME * 3)

        # Remove text, shift foxes, and add new text
        self.play(FadeOut(text1_1), FadeOut(text1_2))
        self.play(fox1.animate(run_time=ANIMATION_TIME).move_to(g.vertices[2]), fox2.animate(run_time=ANIMATION_TIME).move_to(g.vertices[5]))
        self.play(Create(text2_1), Create(text2_2))
        self.wait(ANIMATION_TIME * 3)

        # Cycle text again
        self.play(FadeOut(text2_1), FadeOut(text2_2))
        self.play(fox1.animate(run_time=ANIMATION_TIME).move_to(g.vertices[1]), fox2.animate(run_time=ANIMATION_TIME).move_to(g.vertices[6]))
        self.play(Create(text3_1), Create(text3_2))
        self.wait(ANIMATION_TIME * 3)

        # Show final text
        self.play(FadeOut(text3_1), FadeOut(text3_2))
        self.play(Create(text4_1))
        self.play(hare.animate(run_time=ANIMATION_TIME).move_to(UP * 10))
        self.wait(ANIMATION_TIME * 3)

        # Remove text and animals
        self.play(Uncreate(text4_1), Uncreate(hare), Uncreate(fox1), Uncreate(fox2))
        self.play(Uncreate(g))
        self.wait(ANIMATION_TIME)

