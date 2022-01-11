from manim import *
from manim.utils import tex
from constants import *
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
        text = Text("A complex graph with many branches").shift(
            TEXT_SHIFT_AMOUNT)
        text.scale(0.5)

        text2 = Text("We can identify branches that end with a degree of one").shift(
            TEXT_SHIFT_AMOUNT)
        text2.scale(0.5)

        text3 = Text("Those are branches that the rabbit should NOT follow").shift(
            TEXT_SHIFT_AMOUNT)
        text3.scale(0.5)

        text4 = Text("After simplifying the graph, we can identify this graph has a fox number of 1.").shift(
            TEXT_SHIFT_AMOUNT)
        text4.scale(0.5)

        text5 = Text("We can repeat the process for graphs with mutliple cycles.").shift(
            TEXT_SHIFT_AMOUNT)
        text5.scale(0.5)

        text6 = MarkupText("We can identify that this graph has a fox number of 2 because after cleaning the graph, \n there is a cycle with a fox number of 2.").shift(
            TEXT_SHIFT_AMOUNT)
        text6.scale(0.5)

        G = nx.Graph()
        G.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        G.add_edges_from([(0, 2), (1, 0), (1, 2), (0, 3), (1, 4),
                         (2, 5), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10)])

        G2 = nx.Graph()

        # 0 - 6 are of the actual cycle graphs, th rest are branches
        G2.add_nodes_from([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
        G2.add_edges_from([(0, 1), (1, 2), (2, 3), (0, 3), (4, 5), 
                        (5, 6), (4, 6), (6, 7), (7, 8), (8, 9), (9, 10), 
                        (3, 4), (0, 11), (11, 12), (12, 13)])

        graph_nu = Graph(list(G2.nodes), list(G2.edges),
                         layout="kamada_kawai", partitions=[[0, 1]]).scale(1.5)

        graph_nu_2 = graph_nu.copy()
        graph_nu_2.remove_vertices(7, 8, 9, 10, 11, 12, 13)

        graph = Graph(list(G.nodes), list(G.edges),
                      layout="kamada_kawai", partitions=[[0, 1]]).scale(1.5)
        graph2 = graph.copy()

        self.play(Create(graph), Write(text))
        self.wait(PAUSE_TIME)
        graph2.remove_vertices(3, 4, 5, 6, 7, 8, 9, 10).scale(2)
        self.play(ReplacementTransform(text, text2))
        self.wait()
        self.play(*self.bulk_indicate(graph,
                [(0, 3), (1, 4), (2, 5), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10)]),
                run_time=OptimizationConstants.ANIMATION_TIME)

        self.wait(PAUSE_TIME)
        self.play(ReplacementTransform(text2, text3))
        self.wait(PAUSE_TIME)
        self.play(ReplacementTransform(graph, graph2))
        self.wait()
        self.play(Indicate(graph2), ReplacementTransform(text3, text4))
        self.wait(LONG_PAUSE_TIME)
        self.play(Uncreate(graph2), Uncreate(text4))
        self.wait()

        self.play(Create(graph_nu))
        self.wait(PAUSE_TIME)
        self.play(Write(text5))

        self.play(*self.bulk_indicate(graph_nu,
                                      [(6, 7), (7, 8), (8, 9), (9, 10), (0, 11), (11, 12), (12, 13)]),
                  run_time=OptimizationConstants.ANIMATION_TIME)

        self.wait(PAUSE_TIME)
        self.play(ReplacementTransform(graph_nu, graph_nu_2))
        self.wait(0.1)
        self.play(ReplacementTransform(text5, text6))
        self.wait(0.1)

        self.play(*self.bulk_indicate(graph_nu_2,
                                [(0, 1), (1, 2), (2, 3), (0, 3)]),
                                run_time=OptimizationConstants.ANIMATION_TIME)

        self.wait(LONG_PAUSE_TIME)

        self.play(Uncreate(graph_nu_2), Uncreate(text6))
        self.wait(PAUSE_TIME)

    def bulk_indicate(self, graph, edges: list):
        actions = []

        for edge in edges:
            actions.append(Indicate(graph.edges[edge], color=RED))

        return actions
