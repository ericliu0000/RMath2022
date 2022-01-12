from manim import *
from manim.utils import tex
from constants import *
import networkx as nx

class subgraph(Scene):
    def construct(self):    

        g = nx.Graph()
        g.add_nodes_from([0, 1, 2, 3])
        graph = Graph(g)


        # Initialize hare object
        hare = SVGMobject(HARE_FILE_NAME)
        hare.scale(FOX_SCALE)
        hare.move_to(g.vertices[3])

        # Initialize fox object
        fox = SVGMobject(FOX_FILE_NAME)
        fox.scale(HARE_SCALE)
        fox.move_to(g.vertices[6])




