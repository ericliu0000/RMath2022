from manim import *
from constants import *

class DisconnectedGraph(Scene):
    def construct(self):
        # Create two 3 cycle graphs
        vertices = [1, 2, 3]
        edges = [(1, 2), (2, 3), (3, 1)]
        l = Graph(vertices, edges)
        r = Graph(vertices, edges)

        l.move_to(LEFT * 2)
        r.next_to(l, RIGHT, buff=0.5)

        # Initialize hare object
        hare = SVGMobject(HARE_FILE_NAME)
        hare.scale(FOX_SCALE)
        hare.move_to(l.vertices[1])

        # Initialize fox object
        fox = SVGMobject(FOX_FILE_NAME)
        fox.scale(HARE_SCALE)
        fox.move_to(r.vertices[1])

        # Make text
        text1 = MarkupText(f"what", color=TEXT_COLOR)
        text1.next_to(l, DOWN, buff=0.3)

        # Create graph
        self.play(Create(l), Create(r))
        self.wait(PAUSE_TIME)

        # Add hare
        self.play(FadeIn(hare, shift=UP, scale=0.1))
        self.play(FadeIn(fox, shift=UP, scale=0.1))

        # Add text and pause
        self.play(Create(text1))
        self.wait(PAUSE_TIME)

        # Move animals
        for i in range(10):
            self.play(fox.animate(run_time=0.2).move_to(r.vertices[(i)%3 + 1]),
                    hare.animate(run_time=0.2).move_to(l.vertices[(i)%3 + 1]))
            self.wait(0.2)
