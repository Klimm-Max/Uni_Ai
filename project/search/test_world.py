from project.search.graph.graph import Graph
from project.search.graph.node import Node
from project.search.bfs import calculate_path, breadth_first_search

graph = Graph(5, 5)
start = Node(1, 1)
target = Node(3, 2)

came_from = breadth_first_search(graph, start, target)
path = calculate_path(came_from, start, target)

print(path)