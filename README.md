# Search Visualization

## About

The Design and Analysis of Algorithms course that I am taking discusses various graph search algorithms. Some examples of these algorithms include BFS (breadth-first search), DFS (depth-first search), Dijkstra's, and Bellman Ford's. I have created programs that visualize these search algorithms on randomly generated graphs, to make it easier to conceptualize what the algorithms do.

<img src="/Users/cara/Downloads/oxford/Trinity2020/search-vis/bfs.gif" alt="BFS Visualization on Randomly Generated Graph" style="zoom:50%;" />

*BFS Visualization Software*

## Usage
This visualization software can be run in Python 3 by calling the `main()` function. There are some additional libraries required, as detailed in the following section.

## Dependencies

This project was built using Python 3 libraries including:

* [Matplotlib](https://matplotlib.org/) for visualization
* [Networkx](https://networkx.github.io/) for graph generation
  * Includes various random graph generators for Erdős-Rényi graphs, Watts–Strogatz small-world graphs, and many others
  * Contains multiple layout/node positioning routines

The variants noted for Networkx are fun and easy to play around with, and I would recommend experimenting with different types of graphs by changing the code in BFS.py.

## ImageMagick (optional)

ImageMagick is a useful tool for converting multiple images / frames into a GIF. I installed it on my Mac using Homebrew:

  `brew install imagemagick`

but it can also be installed on other machines—have a look [here](https://imagemagick.org/script/download.php) for instructions.

**Using the tool**

1. Navigate to the directory where BFS.py is stored on your computer
1. Run BFS.py using the command `python -m BFS`. This will create an animation `test.gif` with the results of running BFS on a random graph.

## Releases

So far, I have only developed visualization software for BFS and DFS, but others should be coming soon!

<img src="/Users/cara/Downloads/oxford/Trinity2020/search-vis/dfs1.gif" alt="DFS Visualization on Randomly Generated Graph" style="zoom:50%;" />
*DFS Visualization Software*

