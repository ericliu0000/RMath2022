from manim import *


class OneFox(Scene):
    def construct(self):
        next_text_time = 4
        animation_time = 1

        # Create 6 cycle graph
        vertices = [1, 2, 3, 4, 5, 6]
        edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]
        layout = {1: [-2, 1, 0], 2: [0, 2, 0], 3: [2, 1, 0],
                  4: [2, -1, 0], 5: [0, -2, 0], 6: [-2, -1, 0]}
        g = Graph(vertices, edges, layout=layout)

        # Initialize hare object
        hare = ImageMobject("assets/hare.png")
        hare.scale(0.24)
        hare.move_to(g.vertices[3])

        # Initialize fox object
        fox = ImageMobject("assets/fox.png")
        fox.scale(0.6)
        fox.move_to(g.vertices[6])

        # Make text
        text1_1 = MarkupText(f"The hare and fox are", color=RED)
        text1_2 = MarkupText(f"engaging in shennanigans.", color=RED)
        text1_1.next_to(g.vertices[5], DOWN, buff=0.3)
        text1_2.next_to(text1_1, DOWN, buff=0.2)

        text2_1 = MarkupText(f"The distance between the hare", color=RED)
        text2_2 = MarkupText(f"and the fox is always (n/2) - 1.", color=RED)
        text2_1.next_to(g.vertices[5], DOWN, buff=0.3)
        text2_2.next_to(text2_1, DOWN, buff=0.2)

        text3_1 = MarkupText(f"where n is the number of", color=RED)
        text3_2 = MarkupText(f"vertices in the cycle graph.", color=RED)
        text3_1.next_to(g.vertices[5], DOWN, buff=0.3)
        text3_2.next_to(text3_1, DOWN, buff=0.2)

        text4_1 = MarkupText(f"Because n is greater than or equal to 4,", color=RED)
        text4_2 = MarkupText(f"and the distance is always (n/2) - 1,", color=RED)
        text4_1.next_to(g.vertices[5], DOWN, buff=0.3)
        text4_2.next_to(text4_1, DOWN, buff=0.2)

        text5_1 = MarkupText(f"the distance between the hare ", color=RED)
        text5_2 = MarkupText(f"and the fox is always at least 1.", color=RED)
        text5_1.next_to(g.vertices[5], DOWN, buff=0.3)
        text5_2.next_to(text5_1, DOWN, buff=0.2)

        text6_1 = MarkupText(f"Thus, the hare is not deceased.", color=RED)
        text6_1.next_to(g.vertices[5], DOWN, buff=0.3)

        # Create graph
        self.play(Create(g))
        self.wait(0.5)

        # Add hare and fox
        self.play(FadeIn(hare, shift=UP, scale=0.1))
        self.play(FadeIn(fox, shift=UP, scale=0.1))

        # Add text and pause
        self.play(Create(text1_1), Create(text1_2))
        self.wait(0.7)

        # Move animals
        for i in range(25):
            if i == next_text_time - 1:
                self.play(FadeOut(text1_1), FadeOut(text1_2), hare.animate(run_time=animation_time).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=animation_time).move_to(g.vertices[(i+6) % 6 + 1]))
            elif i == next_text_time:
                self.play(Create(text2_1), Create(text2_2), hare.animate(run_time=animation_time).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=animation_time).move_to(g.vertices[(i+6) % 6 + 1]))
            elif i == next_text_time + 3:
                self.play(FadeOut(text2_1), FadeOut(text2_2), hare.animate(run_time=animation_time).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=animation_time).move_to(g.vertices[(i+6) % 6 + 1]))
            elif i == next_text_time + 4:
                self.play(Create(text3_1), Create(text3_2), hare.animate(run_time=animation_time).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=animation_time).move_to(g.vertices[(i+6) % 6 + 1]))
            elif i == next_text_time + 7:
                self.play(FadeOut(text3_1), FadeOut(text3_2), hare.animate(run_time=animation_time).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=animation_time).move_to(g.vertices[(i+6) % 6 + 1]))
            elif i == next_text_time + 8:
                self.play(Create(text4_1), Create(text4_2), hare.animate(run_time=animation_time).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=animation_time).move_to(g.vertices[(i+6) % 6 + 1]))
            elif i == next_text_time + 11:
                self.play(FadeOut(text4_1), FadeOut(text4_2), hare.animate(run_time=animation_time).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=animation_time).move_to(g.vertices[(i+6) % 6 + 1]))
            elif i == next_text_time + 12:
                self.play(Create(text5_1), Create(text5_2), hare.animate(run_time=animation_time).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=animation_time).move_to(g.vertices[(i+6) % 6 + 1]))
            elif i == next_text_time + 15:
                self.play(FadeOut(text5_1), FadeOut(text5_2), hare.animate(run_time=animation_time).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=animation_time).move_to(g.vertices[(i+6) % 6 + 1]))
            elif i == next_text_time + 16:
                self.play(Create(text6_1), hare.animate(run_time=animation_time).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=animation_time).move_to(g.vertices[(i+6) % 6 + 1]))
            else:
                self.play(hare.animate(run_time=animation_time).move_to(g.vertices[(i+3) % 6 + 1]), fox.animate(run_time=animation_time).move_to(g.vertices[(i+6) % 6 + 1]))

        # Fade out text
        self.play(FadeOut(text6_1))
        self.wait()

        # Fade out everything
        self.play(FadeOut(hare), FadeOut(fox), Uncreate(g))
        self.wait()

class TwoFox(Scene):
    def construct(self):
        next_text_time = 4
        animation_time = 1

        # Create 6 cycle graph
        vertices = [1, 2, 3, 4, 5, 6]
        edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]
        layout = {1: [-2, 1, 0], 2: [0, 2, 0], 3: [2, 1, 0],
                  4: [2, -1, 0], 5: [0, -2, 0], 6: [-2, -1, 0]}
        g = Graph(vertices, edges, layout=layout)

        # Initialize hare object
        hare = ImageMobject("assets/hare.png")
        hare.scale(0.24)
        hare.move_to(g.vertices[3])

        # Initialize fox object
        fox = ImageMobject("assets/fox.png")
        fox.scale(0.6)
        fox.move_to(g.vertices[6])
