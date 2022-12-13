from math import floor
import math

input_file = "day_12/input.data"

TRANSFORMS = {"S": "a", "E": "z"}

def get_height(x, y, map):
    height = map[y][x]
    return TRANSFORMS[height] if height in TRANSFORMS.keys() else height

def get_all_with_heights(height_list, map):
    found = []
    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            if map[y][x] in height_list:
                found.append((x, y))
    return found

def get_start(map):
    return get_unique("S", map)

def get_finish(map):
    return get_unique("E", map)

def get_unique(value, map):
    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            if map[y][x] == value:
                return x, y

def is_available(prev_height, x, y, map, reverse):
    if y < 0 or x < 0 or y >= len(map) or x >= len(map[0]):
        return False
    new_height = get_height(x, y, map)
    if new_height in ["E", "S"]:
        new_height = TRANSFORMS[new_height]
    if ord(new_height) - ord(prev_height) <= 1 and reverse == False:
        return True
    elif ord(prev_height) - ord(new_height) <= 1 and reverse == True:
        return True
    else:
        return False

def get_available_steps(pos, reverse):
    pos_mods = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pos_height = get_height(pos[0], pos[1], map)
    available_steps = []
    for pm in pos_mods:
        new_pos = (pos[0] + pm[0], pos[1] + pm[1])
        if is_available(pos_height, *new_pos, map, reverse):
            available_steps.append(new_pos)
    return available_steps

def dijkstras(source, map, reverse=False):
    distances = {}
    visited = {}
    queue = []
    for y in range(0, len(map)):
        for x in range(0, len(map[0])):
            pos = (x, y)
            distances[pos] = math.inf
            visited[pos] = None
            queue.append(pos)
    distances[source] = 0

    while len(queue) > 0:
        current = min(queue, key=distances.get)
        queue.remove(current)

        for neighbour in [x for x in get_available_steps(current, reverse) if x in queue]:
            new_dist = distances[current] + 1
            if new_dist < distances[neighbour]:
                distances[neighbour] = new_dist
                visited[neighbour] = current
    return distances, visited

with open(input_file, "r") as file:
    map = []
    for line in file.readlines():
        map.append(line.strip())
    
    #print(len(follow_path(get_start(map), map, [])))
    distances, visited = dijkstras(get_start(map), map)
    print(distances[get_finish(map)])
    all_a_starts = get_all_with_heights(["a", "S"], map)
    distances, visited = dijkstras(get_finish(map), map, reverse=True)
    print(min([distances[x] for x in all_a_starts]))
    