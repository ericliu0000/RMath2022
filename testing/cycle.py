from manim import *
from constants import *


class OneFoxCycle(Scene):
    def construct(self):
        # Create 6 cycle graph
        g = Graph(CycleGraphConstants.VERTICES, 
                    CycleGraphConstants.EDGES, 
                    layout = CycleGraphConstants.LAYOUT)

        # Initialize hare object
        hare = SVGMobject(HARE_FILE_NAME)
        hare.scale(FOX_SCALE)
        hare.move_to(g.vertices[3])

        # Initialize fox object
        fox = SVGMobject(FOX_FILE_NAME)
        fox.scale(HARE_SCALE)
        fox.move_to(g.vertices[6])

        # Make text
        text1_1 = MarkupText(f"The hare and fox are", color=RED)
        text1_2 = MarkupText(f"engaging in shennanigans.", color=RED)
        text1_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text1_2.next_to(text1_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text2_1 = MarkupText(f"The distance between the hare", color=RED)
        text2_2 = MarkupText(f"and the fox is always (n/2) - 1.", color=RED)
        text2_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text2_2.next_to(text2_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text3_1 = MarkupText(f"where n is the number of", color=RED)
        text3_2 = MarkupText(f"vertices in the cycle graph.", color=RED)
        text3_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text3_2.next_to(text3_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text4_1 = MarkupText(f"Because n is greater than or equal to 4,", color=RED)
        text4_2 = MarkupText(f"and the distance is always (n/2) - 1,", color=RED)
        text4_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text4_2.next_to(text4_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text5_1 = MarkupText(f"the distance between the hare ", color=RED)
        text5_2 = MarkupText(f"and the fox is always at least 1.", color=RED)
        text5_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)
        text5_2.next_to(text5_1, DOWN, buff=BETWEEN_TEXT_BUFFER)

        text6_1 = MarkupText(f"Thus, the hare is not deceased.", color=RED)
        text6_1.next_to(g.vertices[5], DOWN, buff=TOP_TEXT_BUFFER)

        # Create graph
        self.play(Create(g))
        self.wait(PAUSE_TIME)

        # Add hare and fox
        self.play(FadeIn(hare, shift=UP, scale=0.1))
        self.play(FadeIn(fox, shift=UP, scale=0.1))

        # Add text and pause
        self.play(Create(text1_1), Create(text1_2))
        self.wait(PAUSE_TIME)

        # Move animals
        for i in range(25):
            buffer = [hare.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+3) % 6 + 1]), 
                        fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+6) % 6 + 1])]

            if i == CycleGraphConstants.ONE_FOX_FRAMES[1]:
                buffer += [ReplacementTransform(text1_1, text2_1), ReplacementTransform(text1_2, text2_2)]
            elif i == CycleGraphConstants.ONE_FOX_FRAMES[3]:
                buffer += [ReplacementTransform(text2_1, text3_1), ReplacementTransform(text2_2, text3_2)]
            elif i == CycleGraphConstants.ONE_FOX_FRAMES[5]:
                buffer += [ReplacementTransform(text3_1, text4_1), ReplacementTransform(text3_2, text4_2)]
            elif i == CycleGraphConstants.ONE_FOX_FRAMES[7]:
                buffer += [ReplacementTransform(text4_1, text5_1), ReplacementTransform(text4_2, text5_2)]
            elif i == CycleGraphConstants.ONE_FOX_FRAMES[9]:
                buffer += [FadeOut(text5_2), ReplacementTransform(text5_1, text6_1)]

            self.play(*buffer)
            # if i == CycleGraphConstants.ONE_FOX_FRAMES[0]:
            #     self.play(FadeOut(text1_1), FadeOut(text1_2), hare.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+6) % 6 + 1]))
            # elif i == CycleGraphConstants.ONE_FOX_FRAMES[1]:
            #     self.play(Create(text2_1), Create(text2_2), hare.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+6) % 6 + 1]))
            # elif i == CycleGraphConstants.ONE_FOX_FRAMES[2]:
            #     self.play(FadeOut(text2_1), FadeOut(text2_2), hare.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+6) % 6 + 1]))
            # elif i == CycleGraphConstants.ONE_FOX_FRAMES[3]:
            #     self.play(Create(text3_1), Create(text3_2), hare.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+6) % 6 + 1]))
            # elif i == CycleGraphConstants.ONE_FOX_FRAMES[4]:
            #     self.play(FadeOut(text3_1), FadeOut(text3_2), hare.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+6) % 6 + 1]))
            # elif i == CycleGraphConstants.ONE_FOX_FRAMES[5]:
            #     self.play(Create(text4_1), Create(text4_2), hare.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+6) % 6 + 1]))
            # elif i == CycleGraphConstants.ONE_FOX_FRAMES[6]:
            #     self.play(FadeOut(text4_1), FadeOut(text4_2), hare.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+6) % 6 + 1]))
            # elif i == CycleGraphConstants.ONE_FOX_FRAMES[7]:
            #     self.play(Create(text5_1), Create(text5_2), hare.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+6) % 6 + 1]))
            # elif i == CycleGraphConstants.ONE_FOX_FRAMES[8]:
            #     self.play(FadeOut(text5_1), FadeOut(text5_2), hare.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+6) % 6 + 1]))
            # elif i == CycleGraphConstants.ONE_FOX_FRAMES[9]:
            #     self.play(Create(text6_1), hare.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+6) % 6 + 1]))
            # else:
            #     self.play(hare.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[(i+6) % 6 + 1]))

        # Fade out text
        self.play(FadeOut(text6_1))
        self.wait(PAUSE_TIME)

        # Fade out everything
        self.play(Uncreate(hare), Uncreate(fox), Uncreate(g))
        self.wait(PAUSE_TIME)
