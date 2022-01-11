from manim import *
from manim.utils import tex

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


TEXT_SHIFT_AMOUNT = UP * 2.5

class subgraph(Scene):
    def construct(self):    


        # text that states, we start with a complex graph with many branches
        text = Text("A complex graph with many branches").shift(TEXT_SHIFT_AMOUNT)
        text.scale(0.5)

        # text that states, we can identify branches that end with a degree of one
        text2 = Text("We can identify branches that end with a degree of one").shift(TEXT_SHIFT_AMOUNT)
        text2.scale(0.5)

        # text that says, These are branches that the rabbit should NOT follow 
        text3 = Text("These are branches that the rabbit should NOT follow").shift(TEXT_SHIFT_AMOUNT)
        text3.scale(0.5)


        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7 , 8, 9, 10])
        G.add_edges_from([(0, 2), (1,0), (1, 2), (0,3), (1,4), (2,5), (5,6), (6,7), (1,8), (8,9), (9,10)])
        graph = Graph(list(G.nodes), list(G.edges), layout="kamada_kawai", partitions=[[0, 1]]).scale(1.5)
        self.play(Create(graph), Write(text))
        self.wait(2)


        graph2 = graph.copy()

        graph2.remove_vertices(3,4,5,6,7,8,9,10).scale(2)
        self.play(ReplacementTransform(text, text2))
        self.wait()
        self.play(Indicate(graph.edges[(0,3)], color=RED),
                  Indicate(graph.edges[(1,4)], color=RED),
                  Indicate(graph.edges[(2,5)], color=RED),
                  Indicate(graph.edges[(5,6)], color=RED),
                  Indicate(graph.edges[(6,7)], color=RED), 
                    Indicate(graph.edges[(1,8)], color=RED),
                    Indicate(graph.edges[(8,9)], color=RED),
                    Indicate(graph.edges[(9,10)], color=RED),
                  run_time=3)
        self.wait(2)
        self.play(ReplacementTransform(text2,text3))
        self.wait(2)
        self.play(ReplacementTransform(graph,graph2))
        self.wait()
        self.play(Indicate(graph2))
        self.wait(2)


