from project.search.graph.node import Node


class Graph:
    def __init__(self, width=20, height=20):
        self.nodes = []
        for x in range(width):
            for y in range(height):
                self.nodes.append(Node(x, y))

    def get_nodes(self):
        return self.nodes

    def neighbours(self, node, allow_diagonal=False):
        directions = [Node(1, 0), Node(-1, 0), Node(0, 1), Node(0, -1)]
        if allow_diagonal:
            directions.extend([Node(1, 1), Node(-1, 1), Node(1, -1), Node(-1, -1)])

        return [direction + node for direction in directions if direction + node in self.nodes]

    def delete_nodes(self, nodes_to_del):
        for node in nodes_to_del:
            if isinstance(node, Node) and node in self.nodes:
                self.nodes.remove(node)
