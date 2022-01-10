# Next text time in cycles
NEXT_TEXT_TIME = 4

# Animation delay time in seconds
ANIMATION_TIME = 1.0

# Fox and hare file names
FOX_FILE_NAME = "assets/fox.png"
HARE_FILE_NAME = "assets/hare.png"

# Fox and hare scales
FOX_SCALE = 0.6
HARE_SCALE = 0.24

# Text buffers in units
TOP_TEXT_BUFFER = 0.3
BETWEEN_TEXT_BUFFER = 0.2

class CycleGraphConstants:
    # Layout of vertices in 6-cycle graph
    VERTICES = [1, 2, 3, 4, 5, 6]
    EDGES = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]
    LAYOUT = {1: [-2, 1, 0], 2: [0, 2, 0], 3: [2, 1, 0],
            4: [2, -1, 0], 5: [0, -2, 0], 6: [-2, -1, 0]}

    # Animation wait time in seconds
    PAUSE_TIME = 0.5

    ONE_FOX_FRAMES = [3, 4, 7, 8, 11, 12, 15, 16, 19, 20]