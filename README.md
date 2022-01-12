# Research in Mathematics 2022 January-Term

### Ben Caunt, Eric Liu, Helen Wu, Ganning Xu

### Animation tools for "Foxes and Hares" problem

## Structure

In the `testing/` directory, there are various files that each create a [Manim](https://www.manim.community/) animation. Various animations create our group's final presentation, which focuses on explaining aspects of the Foxes and Hares problem. 

In a game of Foxes and Hares, the hare begins on an optimal position, and the fox(es) start the farthest away from the hare. The foxes attempt to occupy the same vertex as the hare, and the hare seeks to escape. Assuming all of the foxes and the hare play optimally, the minimum number of foxes required to decisively assure a victory determines the graph's "fox number."

Within this problem, we seek to identify the patterns between the shape of the graph that yield certain fox numbers. Here, we are attempting to visualize patterns observed in cycle sub-graphs within certain graphs, as well as optimizations that can be taken within the graph.

## Usage

All animations were created using Manim Community, and have been tested on [Manim](https://github.com/ManimCommunity/manim) v0.14.0 or later, with Python 3.9. To generate a video file, navigate to the `testing` directory and invoke the command

`manim [file].py`

This will output a file in the `media/videos/` directory. 

You may also render all of the files by using the Render.java program. It may work on Java versions 1.8 or later, but has only been tested on Java 17. The program will animate, using Manim, all of the .py files in the current working directory unless otherwise excluded. It may be run using the command

`java Render.java`

The program will halt after 1000 seconds of runtime, if not finished by then. All of the video files should also be present in `media/videos`
