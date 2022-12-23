import re

input_file = "day_18/input.data"

input_pattern = re.compile('^([0-9]+),([0-9]+),([0-9]+)')


def extract_values(line):
    m = input_pattern.match(line.strip())
    return int(m.group(1)), int(m.group(2)), int(m.group(3))

def is_neighbour(node, other_node):
    diffs = [abs(node[0] - other_node[0]), abs(node[1] - other_node[1]), abs(node[2] - other_node[2])]
    diffs.sort()
    return diffs == [0, 0, 1]

def max_x(rocks):
    return max([x[0] for x in rocks])

def max_y(rocks):
    return max([x[1] for x in rocks])

def max_z(rocks):
    return max([x[2] for x in rocks])

def get_neighbours(coords, rocks):
    neighbours = set()
    forward = (coords[0], coords[1]+1, coords[2])
    if forward[1] <= (max_y(rocks) + 1) and forward not in rocks:
        neighbours.add(forward)
    right = (coords[0]+1, coords[1], coords[2])
    if right[0] <= (max_x(rocks) + 1) and right not in rocks:
        neighbours.add(right)
    back = (coords[0], coords[1]-1, coords[2])
    if back[1] >= 0  and back not in rocks:
        neighbours.add(back)
    left = (coords[0]-1, coords[1], coords[2])
    if left[0] >= 0 and left not in rocks:
        neighbours.add(left)
    up = (coords[0], coords[1], coords[2]+1)
    if up[2] <= (max_z(rocks) + 1) and up not in rocks:
        neighbours.add(up)
    down = (coords[0], coords[1], coords[2]-1)
    if down[2] >= 0 and down not in rocks:
        neighbours.add(down)
    return neighbours
    
def all_reachable(rocks):
    cur = (0, 0, 0)
    queue = get_neighbours(cur, rocks)
    visited = set()
    visited.add(cur)
    while(len(queue) > 0):
        cur = queue.pop()
        visited.add(cur)
        for x in get_neighbours(cur, rocks):
            if x not in visited:
                queue.add(x)
    return visited

def get_all_air(rocks):
    reachable = all_reachable(rocks)
    air = set()
    for x in range(1, max_x(rocks)+1):
        for y in range(1, max_y(rocks)+1):
            for z in range(1, max_z(rocks)+1):
                if (x, y, z) not in reachable.union(rocks):
                    air.add((x, y, z))
    return air

with open(input_file, "r") as file:
    rocks = set()
    for line in file.readlines():
        rocks.add(extract_values(line))
    exposed_sides = 6 * len(rocks)
    for node in rocks:
        for other_node in rocks:
            if is_neighbour(node, other_node):
                exposed_sides -= 1
    print(exposed_sides)
    air = get_all_air(rocks)
    exposed_insides = 6 * len(air)
    for node in air:
        for other_node in air:
            if is_neighbour(node, other_node):
                exposed_insides -= 1
    print(exposed_sides - exposed_insides)

