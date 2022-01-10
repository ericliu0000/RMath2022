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

# For renderAll: files to exclude
EXCLUDE_FILES = ["constants.py"]

class CycleGraphConstants:
    # Layout of vertices in 6-cycle graph
    VERTICES = [1, 2, 3, 4, 5, 6]
    EDGES = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1)]
    LAYOUT = {1: [-2, 1.3, 0], 2: [0, 2.3, 0], 3: [2, 1.3, 0],
            4: [2, -0.7, 0], 5: [0, -1.7, 0], 6: [-2, -0.7, 0]}

    # Animation wait time in seconds
    PAUSE_TIME = 0.5

    ONE_FOX_FRAMES = [3, 4, 7, 8, 11, 12, 15, 16, 19, 20]