from manim import *

class CycleGraph(Scene):
    def construct(self):
        # Create 6 cycle graph
        vertices = [1, 2, 3, 4, 5, 6]
        edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]
        layout = {1: [-2, 1, 0], 2: [0, 2, 0], 3: [2, 1, 0], 4: [2, -1, 0], 5: [0, -2, 0], 6: [-2, -1, 0]}
        g = Graph(vertices, edges, layout=layout) #, layout=layout)

        # Initialize hare object
        hare = ImageMobject("assets/hare.png")
        hare.scale(0.24)
        hare.move_to(g.vertices[3])

        # Initialize fox object
        fox = ImageMobject("assets/fox.png")
        fox.scale(0.6)
        fox.move_to(g.vertices[1])

        # Make text
        text1 = MarkupText(f"The hare and fox are", color=RED)
        text2 = MarkupText(f"engaging in shennanigans.", color=RED)
        text1.next_to(g.vertices[5], DOWN, buff=0.3)
        text2.next_to(text1, DOWN, buff=0.2)

        # Create graph
        self.play(Create(g))
        self.wait(0.5)

        # Add hare
        self.play(FadeIn(hare, shift=UP, scale=0.1))
        self.play(FadeIn(fox, shift=UP, scale=0.1))

        # Add text and pause
        self.play(Create(text1), Create(text2))
        self.wait(1)

        # Move animals
        for i in range(10):
            self.play(fox.animate(run_time=0.6).move_to(g.vertices[(i+1)%6 + 1]))
            self.play(hare.animate(run_time=0.6).move_to(g.vertices[(i+3)%6 + 1]))

