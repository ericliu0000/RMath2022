from manim import *
from constants import *


class OptimizeGraphs(Scene):
    def construct(self):        
        # Generate first pair of graphs
        simple_graph1 = Graph(OptimizationConstants.GRAPH_1_VERTICES, 
                        OptimizationConstants.GRAPH_1_EDGES,
                        layout="kamada_kawai", partitions=[[0, 1]]).scale(1.5)
        simple_graph2 = simple_graph1.copy()
        simple_graph2.remove_vertices(3, 4, 5, 6, 7, 8, 9, 10).scale(2)

        simple_graph1.shift(OptimizationConstants.GRAPH_SHIFT)
        simple_graph2.shift(OptimizationConstants.GRAPH_SHIFT)

        # Generate second pair of graphs
        graph1 = Graph(OptimizationConstants.GRAPH_2_VERTICES,\
                    OptimizationConstants.GRAPH_2_EDGES,
                    layout="kamada_kawai", partitions=[[0, 1]]).scale(1.5)
        graph2 = graph1.copy()
        graph2.remove_vertices(7, 8, 9, 10, 11, 12, 13)

        graph1.shift(OptimizationConstants.GRAPH_SHIFT)
        graph2.shift(OptimizationConstants.GRAPH_SHIFT)

        # Make text
        text1_1 = MarkupText("We start off with a complex", color=TEXT_COLOR)
        text1_2 = MarkupText("graph with many branches.", color=TEXT_COLOR)
        text1_2.shift(OptimizationConstants.TEXT_SHIFT)
        text1_1.next_to(text1_2, UP, buff=BETWEEN_TEXT_BUFFER)

        text2_1 = MarkupText("To simplify this, we can remove", color=TEXT_COLOR)
        text2_2 = MarkupText("branches that end with a degree of one.", color=TEXT_COLOR)
        text2_2.shift(OptimizationConstants.TEXT_SHIFT)
        text2_1.next_to(text2_2, UP, buff=BETWEEN_TEXT_BUFFER)

        text3_1 = MarkupText("Those are branches that the rabbit would", color=TEXT_COLOR)
        text3_2 = MarkupText("never enter, as it would get cornered.", color=TEXT_COLOR)
        text3_2.shift(OptimizationConstants.TEXT_SHIFT)
        text3_1.next_to(text3_2, UP, buff=BETWEEN_TEXT_BUFFER)

        text4_1 = MarkupText("After simplifying the graph, we can", color=TEXT_COLOR)
        text4_2 = MarkupText("see that this graph has a fox number of 1.", color=TEXT_COLOR)
        text4_2.shift(OptimizationConstants.TEXT_SHIFT)
        text4_1.next_to(text4_2, UP, buff=BETWEEN_TEXT_BUFFER)

        text5_1 = MarkupText("We can also use this in graphs", color=TEXT_COLOR)
        text5_2 = MarkupText("with multiple sub-cycle graphs.", color=TEXT_COLOR)
        text5_2.shift(OptimizationConstants.TEXT_SHIFT)
        text5_1.next_to(text5_2, UP, buff=BETWEEN_TEXT_BUFFER)

        text6_1 = MarkupText("This graph has a fox number of 2,", color=TEXT_COLOR)
        text6_2 = MarkupText("because after cleaning the graph, there", color=TEXT_COLOR)
        text6_3 = MarkupText("there is a cycle with a fox number of 2.", color=TEXT_COLOR)
        text6_3.shift(OptimizationConstants.TEXT_SHIFT - UP)
        text6_2.next_to(text6_3, UP, buff=BETWEEN_TEXT_BUFFER)
        text6_1.next_to(text6_2, UP, buff=BETWEEN_TEXT_BUFFER)

        # Create graph and text
        self.play(Create(simple_graph1), Write(text1_1), Write(text1_2))
        self.wait(LONG_PAUSE_TIME)
        self.play(ReplacementTransform(text1_1, text2_1), 
                ReplacementTransform(text1_2, text2_2))

        # Indicate vestigial structures
        self.wait(PAUSE_TIME)
        self.play(*bulk_indicate(simple_graph1,
                [(0, 3), (1, 4), (2, 5), (5, 6), (6, 7), (1, 8), (8, 9), (9, 10)]),
                *bulk_indicate_points(simple_graph1, [3, 4, 5, 6, 7, 8, 9, 10]),
                run_time=OptimizationConstants.ANIMATION_TIME)
        self.wait(PAUSE_TIME)

        # Cycle text and graph
        self.play(ReplacementTransform(text2_1, text3_1), 
                ReplacementTransform(text2_2, text3_2))
        self.play(ReplacementTransform(simple_graph1, simple_graph2))
        self.wait(PAUSE_TIME)

        # Indicate entire graph and swap text
        self.play(Indicate(simple_graph2), 
                ReplacementTransform(text3_1, text4_1), 
                ReplacementTransform(text3_2, text4_2))
        self.wait(LONG_PAUSE_TIME)

        # Remove graph and text
        self.play(Uncreate(simple_graph2), Uncreate(text4_1), Uncreate(text4_2))
        self.wait(PAUSE_TIME)

        # Introduce second graph and text
        self.play(Create(graph1))
        self.wait(PAUSE_TIME)
        self.play(Write(text5_1), Write(text5_2))

        # Emphasize vestigial structures on second graph
        self.play(*bulk_indicate(graph1,
                [(6, 7), (7, 8), (8, 9), (9, 10), (0, 11), (11, 12), (12, 13)]),
                *bulk_indicate_points(graph1, [7, 8, 9, 10, 11, 12, 13]),
                run_time=OptimizationConstants.ANIMATION_TIME)
        self.wait(PAUSE_TIME)

        # Cycle text
        self.play(ReplacementTransform(graph1, graph2), 
                ReplacementTransform(text5_1, text6_1), 
                ReplacementTransform(text5_2, text6_2),
                Write(text6_3))
        self.wait(PAUSE_TIME)

        # Indicate graph
        self.play(*bulk_indicate(graph2, [(0, 1), (1, 2), (2, 3), (0, 3)]),
                *bulk_indicate_points(graph2, [0, 1, 2, 3]),
                run_time=OptimizationConstants.ANIMATION_TIME)
        self.wait(LONG_PAUSE_TIME)

        # Remove graph and text
        self.play(Uncreate(text6_1), Uncreate(text6_2), Uncreate(text6_3))
        self.play(Uncreate(graph2))
        self.wait(PAUSE_TIME)
