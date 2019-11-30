class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'X: ' + str(self.x) + ' Y: ' + str(self.y)

    def __add__(self, other):
        return Node(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y
        return False

    def __hash__(self):
        return hash((self.x, self.y))
