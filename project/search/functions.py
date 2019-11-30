def calculate_path(came_from, start, target):
    if came_from[target] is None:
        return None

    path = [target]
    while target != start:
        target = came_from[target]
        path.append(target)

    return path[::-1]
