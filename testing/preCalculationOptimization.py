from manim import *
import numpy as np 

import networkx as nx


class subgraph(Scene):
    def construct(self):    
        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3, 4, 5,6])
        G.add_edges_from([(0, 2), (1,0), (1, 2) , (2,3), (3,4), (4,5), (5,6), (6,4), (6,0)])
        graph = Graph(list(G.nodes), list(G.edges), layout="circular", partitions=[[0, 1]])
        self.play(Create(graph))
        self.wait(2)

        graph2 = graph.copy()
        graph2.change_layout("kamada_kawai")
        graph2.remove_edges((3,4), (6,0))
        graph2.remove_vertices(3)
        self.play(ReplacementTransform(graph,graph2))
        text = MarkupText(str(graph2.edges))
        text.scale(0.5)
        text.move_to(graph2.get_center())
        self.play(FadeIn(text))        
        self.wait(2)
