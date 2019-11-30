from queue import LifoQueue


def depth_first_search(graph, start, target):
    queue = LifoQueue()
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
