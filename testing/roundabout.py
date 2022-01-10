from manim import *

class CycleGraph(Scene):
    def construct(self):

        timeOfNextText = 6

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
        fox.move_to(g.vertices[6])

        # Make text
        text1 = MarkupText(f"The hare and fox are", color=RED)
        text2 = MarkupText(f"engaging in shennanigans.", color=RED)
        text1.next_to(g.vertices[5], DOWN, buff=0.3)
        text2.next_to(text1, DOWN, buff=0.2)

        # make text that says "the distance between the hare and the fox is always (v/2) - 1"
        text3 = MarkupText(f"The distance between the hare and the fox is always (v/2) - 1.", color=RED)
        text3.scale(0.8)
        text3.next_to(g.vertices[5], DOWN, buff=0.3)

        # where v is the number of vertices in the cycle graph
        text4 = MarkupText(f"Where v is the number of vertices in the cycle graph.", color=RED)
        text4.scale(0.7)
        text4.next_to(text3, DOWN, buff=0.2)

        # because V is greater than or equal to 4 and the distance is always (v/2) - 1
        # the distance between the hare and the fox is always atleast 1 
        text5 = MarkupText(f"Because V is greater than or equal to 4 and the distance is always (v/2) - 1", color=RED)
        text5.scale(0.65)
        text5.next_to(g.vertices[5], DOWN, buff=0.3)
        
        # the distance between the hare and the fox is always atleast 1
        text6 = MarkupText(f"The distance between the hare and the fox is always atleast 1.", color=RED)
        text6.scale(0.65)
        text6.next_to(text5, DOWN, buff=0.2)




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
        for i in range(15):
            self.play(fox.animate(run_time=0.6).move_to(g.vertices[(i+6)%6 + 1]))
            self.play(hare.animate(run_time=0.6).move_to(g.vertices[(i+3)%6 + 1]))

            # fade out the text 
            if i == timeOfNextText:
                self.play(FadeOut(text1), FadeOut(text2))
                self.play(Create(text3))
            if i == timeOfNextText + 1:
                self.play(Create(text4))

            if i == timeOfNextText + 3:
                self.play(FadeOut(text3), FadeOut(text4))
                self.play(Create(text5))
            if i == timeOfNextText + 4:
                self.play(Create(text6))

        self.play(FadeOut(text5), FadeOut(text6))
        self.wait()
        # Fade out everything 
        self.play(FadeOut(hare), FadeOut(fox), Uncreate(g))
        self.wait()