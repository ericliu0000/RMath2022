from manim import *
from constants import *

class Path(Scene):
    def construct(self):
        # Create 3 vertex path graph
        vertices = [1, 2, 3]
        edges = [(1, 2), (2, 3)]
        layout = {1: [-2, 0, 0], 2: [0, 0, 0], 3: [2, 0, 0]}
        g = Graph(vertices, edges, layout=layout)

        # Initialize hare object
        hare = SVGMobject(HARE_FILE_NAME)
        hare.scale(FOX_SCALE)
        hare.next_to(g.vertices[1], UP)

        # Initialize fox object
        fox = SVGMobject(FOX_FILE_NAME)
        fox.scale(HARE_SCALE)
        fox.next_to(g.vertices[2], UP)

        # Make text
        text = MarkupText(f"The hare is deceased", color=RED)
        text.next_to(g, DOWN, buff=1)

        # Create graph
        self.play(Create(g))
        self.wait(PAUSE_TIME)

        # Add hare
        self.play(FadeIn(hare, shift=UP, scale=0.1))
        self.play(FadeIn(fox, shift=UP, scale=0.1))

        # Move hare to the other node
        self.play(fox.animate(run_time=2).next_to(g.vertices[1], UP))

        # Add text and pause
        self.play(FadeOut(hare))
        self.play(Create(text))
        self.wait(LONG_PAUSE_TIME)

        self.play(FadeOut(text), Uncreate(fox), Uncreate(g))
        self.wait(PAUSE_TIME)
