# setup a basic manim scene 
from manim import *
from constants import *


class subgraph(Scene):
    def construct(self):
        vertices = [1, 2, 3, 4, 5, 6]

        vertices_2 = [1,2,3]
        verticies_3 = [1,2]

        edges_2 = [(1, 2), (2, 3), (3, 1)]
        edges_3 = [(1, 2), (2, 1)]

        edges = [(1, 2), (2, 3), (1,3), (3, 4), (4, 5), (5, 6), (6,4)]
        combinedGraph = Graph(vertices, edges)
        
        leftThreeCycle  = Graph(vertices_2, edges_2).scale(0.5)
        rightThreeCycle = Graph(vertices_2, edges_2).scale(0.5)
        pathGraph = Graph(verticies_3, edges_3) .scale(0.5)

        leftThreeCycle.move_to(LEFT * 2)
        pathGraph.next_to(leftThreeCycle, RIGHT, buff=0.5)
        rightThreeCycle.next_to(rightThreeCycle, RIGHT, buff=0.5)

        leftThreeCycle.move_to(leftThreeCycle.get_center() + LEFT * 2)

        seperatedGraph = VGroup(leftThreeCycle, pathGraph, rightThreeCycle)

        self.play(Create(seperatedGraph))
        self.wait(0.5)