from manim import *
from constants import *

class Funny(Scene):
    def construct(self):
        g1 = Graph(list(range(30)), [(1, 2), (2, 3), (3, 4), (4, 5), (5, 1)], layout="kamada_kawai")
        g1.shift(LEFT * 2)

        g2 = Graph([1, 2], [(1, 2)])
        g2.shift(RIGHT)

        self.play(Create(g1), Create(g2))

        # Create fox and hare objects
        fox = SVGMobject(FOX_FILE_NAME)
        fox.scale(FOX_SCALE)
        fox.move_to(g1.vertices[3])

        hare = SVGMobject(HARE_FILE_NAME)
        hare.scale(HARE_SCALE)
        hare.move_to(g2)

        self.play(Create(fox), Create(hare))

        self.wait(LONG_PAUSE_TIME)

        text = MarkupText(f"global warming", color=TEXT_COLOR)
        text2 = MarkupText(f"they are both deceased", color=TEXT_COLOR)
        text3 = MarkupText(f"hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", color=GREEN).shift(UP)

        self.play(Write(text, run_time=8), fox.animate(run_time=8).shift(RIGHT * 2.3), hare.animate(run_time=8).shift(UP * 0.9))
        self.play(g1.animate.change_layout(layout="random"), g2.animate.change_layout(layout="spring"))

        self.play(Write(text2, run_time=4), fox.animate(run_time=4).shift(UP * 7), hare.animate(run_time=4).shift(DOWN * 7))

        self.wait(PAUSE_TIME)
        self.play(text2.animate.shift(DOWN + RIGHT), Write(text3, run_time=8))
        