from manim import *
from constants import *

class TwoFox(Scene):
    def construct(self):
        next_text_time = 4
        animation_time = 1

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
