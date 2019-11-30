from queue import Queue


def breadth_first_search(graph, start, target):
    queue = Queue()
    queue.put(start)
    came_from = {start: None}

    while not queue.empty():
        current = queue.get()

        if current == target:
            break

        for neighbour in graph.neighbours(current):
            if neighbour not in came_from:
                queue.put(neighbour)
                came_from[neighbour] = current

    return came_from


def calculate_path(came_from, start, target):
    if came_from[target] is None:
        return None

    path = [target]
    while target != start:
        target = came_from[target]
        path.append(target)

    return path[::-1]
