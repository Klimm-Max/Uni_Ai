from project.search.graph.graph import Graph
from project.search.graph.node import Node
from project.search.bfs import breadth_first_search
from project.search.dfs import depth_first_search
from project.search.functions import calculate_path

graph = Graph(5, 5)
start = Node(1, 1)
target = Node(3, 2)

came_from_bfs = breadth_first_search(graph, start, target)
path = calculate_path(came_from_bfs, start, target)

print(path, came_from_bfs)

came_from_dfs = depth_first_search(graph, start, target)
path = calculate_path(came_from_dfs, start, target)

print(path, came_from_dfs)