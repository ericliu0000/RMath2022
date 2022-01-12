from manim import *

# Next text time in cycles
NEXT_TEXT_TIME = 4

# Animation delay time in seconds
ANIMATION_TIME = 1.0

# Fox and hare file names
FOX_FILE_NAME = "assets/foxBased.svg"
HARE_FILE_NAME = "assets/hareBased.svg"

# Fox and hare scales
FOX_SCALE = 0.75
HARE_SCALE = 0.6

# Text buffers in units
TOP_TEXT_BUFFER = 0.4
BETWEEN_TEXT_BUFFER = 0.2

# Animation wait time in seconds
PAUSE_TIME = 1
LONG_PAUSE_TIME = 4

class CycleGraphConstants:
    # Layout of vertices in 6-cycle graph
    VERTICES = [1, 2, 3, 4, 5, 6]
    EDGES = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]
    LAYOUT = {1: [-2, 1.3, 0], 2: [0, 2.3, 0], 3: [2, 1.3, 0],
              4: [2, -0.7, 0], 5: [0, -1.7, 0], 6: [-2, -0.7, 0]}

    ONE_FOX_FRAMES = [i for i in range(4, 21, 4)]

class WheelGraphConstants:
    # Layout of vertices in wheel graph W_7
    VERTICES = [1, 2, 3, 4, 5, 6, 7]
    EDGES = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1),
             (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7)]
    LAYOUT = {1: [-2, 1.3, 0], 2: [0, 2.3, 0], 3: [2, 1.3, 0],
              4: [2, -0.7, 0], 5: [0, -1.7, 0], 6: [-2, -0.7, 0], 7: [0, 0.3, 0]}


class PathGraphConstants:
    # Layout of vertices in path graph P_7
    VERTICES = [1, 2, 3, 4, 5, 6, 7]
    EDGES = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 1)]
    LAYOUT = {1: [-2, 1.3, 0], 2: [0, 2.3, 0], 3: [2, 1.3, 0],
              4: [2, -0.7, 0], 5: [0, -1.7, 0], 6: [-2, -0.7, 0], 7: [0, 0.3, 0]}


class SubgraphConstants:
    VERTICES = [1, 2, 3, 4, 5, 6, 7, 8, 11, 13, 16, 18]
    EDGES = [(11, 13), (2, 11), (2, 13),
             (1, 3), (3, 4), (4, 5), (5, 6), (6, 8), (8, 1),
             (16, 18), (18, 7), (7, 16)]

    FULL_LAYOUT = {
        1: [-0.5, 1, 0], 2: [0.5, 1, 0], 3: [1, 0.5, 0],
        4: [1, -0.5, 0], 5: [0.5, -1, 0], 6: [-0.5, -1, 0],
        7: [-1, -0.5, 0], 8: [-1, 0.5, 0], 11: [-0.5, 1, 0],
        13: [1, 0.5, 0], 16: [-0.5, -1, 0], 18: [-1, 0.5, 0]
    }

    EXPLODED_LAYOUT = {
        1: [0, 0.5, 0], 2: [0.5, 1.5, 0], 3: [1.5, 0, 0],
        4: [1.5, -1, 0], 5: [1, -1.5, 0], 6: [0, -1.5, 0],
        7: [-1.5, -0.5, 0], 8: [-0.5, 0, 0], 11: [-0.5, 1.5, 0],
        13: [1, 1, 0], 16: [-1, -1, 0], 18: [-1.5, 0.5, 0]
    }

class OptimizationConstants:
    # Duration of animation in seconds
    ANIMATION_TIME = 3

    # Amount of space to offset, in units
    TEXT_SHIFT = UP * 2.5
    GRAPH_SHIFT = DOWN * 1.0

    GRAPH_1_VERTICES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    GRAPH_1_EDGES = [(0, 2), (1, 0), (1, 2), (0, 3), (1, 4), (2, 5),
                    (5, 6), (6, 7), (1, 8), (8, 9), (9, 10)]

    GRAPH_2_VERTICES = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    GRAPH_2_EDGES = [(0, 1), (1, 2), (2, 3), (0, 3), (4, 5), 
                    (5, 6), (4, 6), (6, 7), (7, 8), (8, 9), (9, 10), 
                    (3, 4), (0, 11), (11, 12), (12, 13)]
