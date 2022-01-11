from manim import *

import networkx as nx


    # automatic_layouts = {
    #     "circular": nx.layout.circular_layout,
    #     "kamada_kawai": nx.layout.kamada_kawai_layout,
    #     "planar": nx.layout.planar_layout,
    #     "random": nx.layout.random_layout,
    #     "shell": nx.layout.shell_layout,
    #     "spectral": nx.layout.spectral_layout,
    #     "partite": nx.layout.multipartite_layout,
    #     "tree": _tree_layout,
    #     "spiral": nx.layout.spiral_layout,
    #     "spring": nx.layout.spring_layout,
    # }


class subgraph(Scene):
    def construct(self):    
        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7 ])
        G.add_edges_from([(0, 2), (1,0), (1, 2), (0,3), (1,4), (2,5), (5,6), (6,7)])
        graph = Graph(list(G.nodes), list(G.edges), layout="spring", partitions=[[0, 1]]).scale(1.5)
        self.play(Create(graph))
        self.wait(2)

        graph2 = graph.copy()

        graph2.remove_vertices(3,4,5,6,7).scale(2)
        self.play(Indicate(graph.edges[(0,3)], color=RED),
                  Indicate(graph.edges[(1,4)], color=RED),
                  Indicate(graph.edges[(2,5)], color=RED),
                  Indicate(graph.edges[(5,6)], color=RED),
                  Indicate(graph.edges[(6,7)], color=RED), run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(graph,graph2))
        self.wait()

