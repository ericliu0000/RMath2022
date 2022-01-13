from manim import *
from constants import *


class OneFoxCycle(Scene):
    def construct(self):
        # Create 6 cycle graph
        g = Graph(CycleGraphConstants.VERTICES, 
                    CycleGraphConstants.EDGES, 
                    layout = CycleGraphConstants.LAYOUT).shift(
                        CycleGraphConstants.GRAPH_OFFSET)

        # Initialize hare object
        hare = SVGMobject(HARE_FILE_NAME)
        hare.scale(FOX_SCALE)
        hare.move_to(g.vertices[3])

        # Initialize fox object
        fox = SVGMobject(FOX_FILE_NAME)
        fox.scale(HARE_SCALE)
        fox.move_to(g.vertices[6])

        # Make text
        text1_1 = MarkupText(f"The hare and fox are", color=TEXT_COLOR)
        text1_2 = MarkupText(f"engaging in shennanigans.", color=TEXT_COLOR)
        text1_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text1_2.next_to(text1_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text2_1 = MarkupText(f"The distance between the hare", color=TEXT_COLOR)
        text2_2 = MarkupText(f"and the fox is always (n/2) - 1,", color=TEXT_COLOR)
        text2_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text2_2.next_to(text2_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text3_1 = MarkupText(f"where n is the number of", color=TEXT_COLOR)
        text3_2 = MarkupText(f"vertices in the cycle graph.", color=TEXT_COLOR)
        text3_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text3_2.next_to(text3_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text4_1 = MarkupText(f"Because n is greater than or equal to 4,", color=TEXT_COLOR)
        text4_2 = MarkupText(f"and the distance is always (n/2) - 1,", color=TEXT_COLOR)
        text4_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text4_2.next_to(text4_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text5_1 = MarkupText(f"the distance between the hare ", color=TEXT_COLOR)
        text5_2 = MarkupText(f"and the fox is always at least 1.", color=TEXT_COLOR)
        text5_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text5_2.next_to(text5_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text6_1 = MarkupText(f"Thus, the hare is not deceased.", color=TEXT_COLOR)
        text6_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)

        # Create graph
        self.play(Create(g))
        self.wait(PAUSE_TIME)

        # Add hare and fox
        self.play(Create(hare))
        self.play(Create(fox))

        # Add text and pause
        self.play(Create(text1_1), Create(text1_2))
        self.wait(PAUSE_TIME)

        # Move animals
        for i in range(25):
            buffer = [hare.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+3) % 6 + 1]), 
                        fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+6) % 6 + 1])]

            if i == CycleGraphConstants.ONE_FOX_FRAMES[0]:
                buffer += [ReplacementTransform(text1_1, text2_1), ReplacementTransform(text1_2, text2_2)]
            elif i == CycleGraphConstants.ONE_FOX_FRAMES[1]:
                buffer += [ReplacementTransform(text2_1, text3_1), ReplacementTransform(text2_2, text3_2)]
            elif i == CycleGraphConstants.ONE_FOX_FRAMES[2]:
                buffer += [ReplacementTransform(text3_1, text4_1), ReplacementTransform(text3_2, text4_2)]
            elif i == CycleGraphConstants.ONE_FOX_FRAMES[3]:
                buffer += [ReplacementTransform(text4_1, text5_1), ReplacementTransform(text4_2, text5_2)]
            elif i == CycleGraphConstants.ONE_FOX_FRAMES[4]:
                buffer += [FadeOut(text5_2), ReplacementTransform(text5_1, text6_1)]

            self.play(*buffer)

        # Fade out text
        self.play(FadeOut(text6_1))

        # Fade out everything
        self.play(Uncreate(hare), Uncreate(fox), Uncreate(g))
        self.wait(PAUSE_TIME)
