from manim import *
from constants import *

class Path(Scene):
    def construct(self):
        # Create 3 vertex path graph
        g = Graph(PathGraphConstants.VERTICES,
            PathGraphConstants.EDGES, 
            layout=PathGraphConstants.LAYOUT)

        # Initialize hare object
        hare = SVGMobject(HARE_FILE_NAME)
        hare.scale(FOX_SCALE)
        hare.move_to(g.vertices[1])

        # Initialize fox object
        fox = SVGMobject(FOX_FILE_NAME)
        fox.scale(HARE_SCALE)
        fox.move_to(g.vertices[3])

        # Make text
        text1 = MarkupText(f"The hare and fox start at opposite ends.", color=TEXT_COLOR)
        text1.shift(PathGraphConstants.TEXT_SHIFT)

        text2 = MarkupText(f"The hare has nowhere to move.", color=TEXT_COLOR)
        text2.shift(PathGraphConstants.TEXT_SHIFT)

        text3 = MarkupText(f"The hare is deceased", color=TEXT_COLOR)
        text3.shift(PathGraphConstants.TEXT_SHIFT)

        # Create graph
        self.play(Create(g))
        self.wait(PAUSE_TIME)

        # Add hare
        self.play(Create(hare))
        self.play(Create(fox))
        self.play(Create(text1))
        self.wait(PAUSE_TIME)

        # Move fox to the other nodes and cycle text
        self.play(fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[2]))
        self.play(ReplacementTransform(text1, text2))
        self.wait(PAUSE_TIME)

        # Add text and pause
        self.play(fox.animate(run_time=ANIMATION_TIME).move_to(g.vertices[1]))
        self.play(Uncreate(hare), ReplacementTransform(text2, text3))
        self.wait(LONG_PAUSE_TIME)

        # Remove elements
        self.play(Uncreate(text3), Uncreate(fox), Uncreate(g))
        self.wait(PAUSE_TIME)
