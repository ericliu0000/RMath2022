from manim import *
import math

# Next text time in cycles
NEXT_TEXT_TIME = 4

# Animation delay time in seconds
ANIMATION_TIME = 1.0

# Fox and hare file names
FOX_FILE_NAME = "assets/foxBased.svg"
HARE_FILE_NAME = "assets/hareBased.svg"

# Fox and hare scales
FOX_SCALE = 0.6
HARE_SCALE = 0.48

# Text buffers in units
TOP_TEXT_BUFFER = 0.4
BETWEEN_TEXT_BUFFER = 0.2

# Animation wait time in seconds
PAUSE_TIME = 1
LONG_PAUSE_TIME = 4

# Text color as a Manim color
TEXT_COLOR = RED
INDICATION_COLOR = YELLOW

# Helper function to generate animations in bulk for indication


def bulk_indicate(graph: Graph, edges: list):
    actions = []

    for edge in edges:
        actions.append(Indicate(graph.edges[edge], color=INDICATION_COLOR))

    return actions


def bulk_indicate_points(graph: Graph, points: list):
    actions = []

    for point in points:
        actions.append(Indicate(graph.vertices[point], color=INDICATION_COLOR))

    return actions


class CycleGraphConstants:
    GRAPH_OFFSET = UP * 0.5

    VERTICES = [1, 2, 3, 4, 5, 6]
    EDGES = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]
    LAYOUT = {1: [-2, 1.3, 0], 2: [0, 2.3, 0], 3: [2, 1.3, 0],
              4: [2, -0.7, 0], 5: [0, -1.7, 0], 6: [-2, -0.7, 0]}

    ONE_FOX_FRAMES = [i for i in range(5, 30, 5)]


class WheelGraphConstants:
    VERTICES = [1, 2, 3, 4, 5, 6, 7]
    EDGES = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1),
             (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7)]
    LAYOUT = {1: [-2, 1.3, 0], 2: [0, 2.3, 0], 3: [2, 1.3, 0],
              4: [2, -0.7, 0], 5: [0, -1.7, 0], 6: [-2, -0.7, 0], 7: [0, 0.3, 0]}


class PathGraphConstants:
    VERTICES = [1, 2, 3]
    EDGES = [(1, 2), (2, 3)]
    LAYOUT = {1: [-2, 0, 0], 2: [0, 0, 0], 3: [2, 0, 0]}

    TEXT_SHIFT = DOWN * 2


class SubgraphConstants:
    TEXT_SHIFT = DOWN * 2.5

    VERTICES = [1, 2, 3, 4, 5, 6, 7, 8, 11, 13, 16, 18]
    EDGES = [(11, 13), (2, 11), (2, 13),
             (1, 3), (3, 4), (4, 5), (5, 6), (6, 8), (8, 1),
             (16, 18), (18, 7), (7, 16)]

    FULL_LAYOUT = {
        1: [-1, 2, 0], 2: [1, 2, 0], 3: [2, 1, 0],
        4: [2, -1, 0], 5: [1, -2, 0], 6: [-1, -2, 0],
        7: [-2, -1, 0], 8: [-2, 1, 0], 11: [-1, 2, 0],
        13: [2, 1, 0], 16: [-1, -2, 0], 18: [-2, 1, 0]
    }

    EXPLODED_LAYOUT = {
        1: [-1, 2, 0], 2: [1, 2.5, 0], 3: [2, 1, 0],
        4: [2, -1, 0], 5: [1, -2, 0], 6: [-1, -2, 0],
        7: [-2.5, -1, 0], 8: [-2, 1, 0], 11: [-1, 2.5, 0],
        13: [2, 1.5, 0], 16: [-1.5, -2, 0], 18: [-2.5, 1, 0]
    }

    MOVES = [(2, 6), (1, 5), (8, 4), (6, 3), (5, 1),
             (4, 8), (3, 6), (1, 5), (8, 4)]


class AltSubgraphConstants:
    VERTICES = [i for i in range(1, 15)] + [i for i in range(101, 111)]
    EDGES = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9),
             (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 1), (101, 102),
             (102, 103), (103, 104), (104, 105), (105, 106), (106, 107),
             (107, 108), (108, 109), (109, 110), (110, 101), (1, 101), (2, 101),
             (2, 102), (3, 102), (4, 102), (4, 103), (5, 103), (6, 103), (6, 104),
             (6, 105), (7, 105), (8, 105), (8, 106), (8, 107), (9, 107), (10, 107),
             (10, 108), (11, 108), (11, 109), (12, 109), (13, 109), (13, 110),
             (14, 110), (1, 110)]

    FULL_LAYOUT = {}

    for i in range(1, 15):
        FULL_LAYOUT[i] = [
            1.5 * math.cos(math.pi * i / 7), 1.5 * math.sin(math.pi * i / 7), 0]

    for i in range(101, 111):
        FULL_LAYOUT[i] = [math.cos(
            (math.pi * i / 5) + math.pi / 40), math.sin((math.pi * i / 5) + math.pi / 40), 0]

    SPLIT_LAYOUT = {}

    for i in range(101, 111):
        SPLIT_LAYOUT[i] = [
            1.5 * math.cos(math.pi * i / 5), 1.5 * math.sin(math.pi * i / 5), 0]


class OptimizationConstants:
    ANIMATION_TIME = 3

    TEXT_SHIFT = UP * 2.5
    GRAPH_SHIFT = DOWN * 1.0

    GRAPH_1_VERTICES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    GRAPH_1_EDGES = [(0, 2), (1, 0), (1, 2), (0, 3), (1, 4), (2, 5),
                     (5, 6), (6, 7), (1, 8), (8, 9), (9, 10)]

    GRAPH_2_VERTICES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    GRAPH_2_EDGES = [(0, 1), (1, 2), (2, 3), (0, 3), (4, 5),
                     (5, 6), (4, 6), (6, 7), (7, 8), (8, 9), (9, 10),
                     (3, 4), (0, 11), (11, 12), (12, 13)]


class OptimalPlacementConstants:
    VERTICES = [1, 2, 3, 4, 5, 6, 7]
    EDGES = [(1, 2), (2, 3), (3, 1), (4, 5), (5, 6), (6, 7), (7, 4), (3, 4)]

    LAYOUT = {1: [-3, -1.5, 0], 2: [-3, 1.5, 0],  3: [-1, 0, 0],
              4: [1, 0, 0], 5: [2.5, 1.5, 0], 6: [4, 0, 0], 7: [2.5, -1.5, 0]}

    TEXT_SHIFT = DOWN * 2.5

    MOVES = [[5, 3], [6, 4], [5, 7], [6, 4], [5, 7], [6, 4], [5, 7]]
