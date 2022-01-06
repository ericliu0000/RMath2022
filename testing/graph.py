from manim import *

class MovingVertices(Scene):
    def construct(self):
        vertices = [1, 2, 3]
        edges = [(1, 2), (2, 3)]
        layout = {1: [-2, 0, 0], 2: [0, 0, 0], 3: [2, 0, 0]}
        g = Graph(vertices, edges, layout=layout)

        

        hare = ImageMobject("assets/hare.png")
        hare.scale(0.5)
        hare.next_to(g.vertices[1], UP, buff=0.5)

        text = MarkupText(f"{g.vertices}", color=RED)
        text.next_to(g, DOWN, buff=1)

        self.play(Create(g))
        self.wait(1)

        self.play(FadeIn(hare, shift=UP, scale=0.1))

        self.play(Create(text))

        self.wait(2)