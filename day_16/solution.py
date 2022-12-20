import math
import re
from itertools import permutations

input_file = "day_16/example.data"

input_pattern = re.compile('^Valve ([A-Z]+) has flow rate=([0-9]+); tunnel[s]? lead[s]? to valve[s]? ([A-Z, ]+)')
dijkstra_distances_cache = {}

def extract_values(line):
    m = input_pattern.match(line)
    return m.group(1), int(m.group(2)), [x.strip() for x in m.group(3).split(", ")]

def dijkstras(source, valves, reverse=False):
    if source in dijkstra_distances_cache:
        return dijkstra_distances_cache[source], None
    distances = {}
    visited = {}
    queue = []
    for valve in valves.keys():
        distances[valve] = math.inf
        visited[valve] = None
        queue.append(valve)
    distances[source] = 0

    while len(queue) > 0:
        current = min(queue, key=distances.get)
        queue.remove(current)
        for neighbour in valves[current]["leads_to"]:
            new_dist = distances[current] + 1
            if new_dist < distances[neighbour]:
                distances[neighbour] = new_dist
                visited[neighbour] = current
    dijkstra_distances_cache[source] = distances
    return distances, visited

def get_best_path(current, remaining_time, opened_valves, valves, total, path):
    if (remaining_time <= 2):
        return path, total
    distances, _ = dijkstras(current, valves)
    paths = {}
    for k,v in distances.items():
        if valves[k]["flow_rate"] > 0 and k not in opened_valves:
            time_left = remaining_time - v - 1
            reward = valves[k]["flow_rate"] * time_left
            result = get_best_path(k, time_left, opened_valves + [k], valves, total + reward, path + [k])
            paths[result[1]] = result[0]
    if len(paths) == 0:
        return path, total
    best = max(paths.keys())
    return paths[best], best

def get_complimentary(part, full):
    return [x for x in full if x not in list(part)]

def get_pressure(path, time_left, valves):
    cur = "AA"
    distances, _ = dijkstras(cur, valves)
    sum = 0
    for p in path:
        time_left -= distances[p] + 1
        sum += time_left * valves[p]["flow_rate"]
        distances, _ = dijkstras(p, valves)
    return sum

def calculate_pressure(part, full, time_left, valves):
    other_part = get_complimentary(part, full)
    all_combos = permutations(other_part)
    best_other_part = max([(x, get_pressure(x, time_left, valves)) for x in all_combos], key=lambda combo: (combo[1]))
    return part, best_other_part[0], get_pressure(part, time_left, valves) + best_other_part[1]

with open(input_file, "r") as file:
    valves = {}
    for line in file.readlines():
        valve, flow_rate, leads_to = extract_values(line)
        valves[valve] = {"flow_rate": flow_rate, "leads_to": leads_to}
    remaining_time = 30
    print(get_best_path("AA", 30, [], valves, 0, []))

    useful_valves = [k for k in valves if valves[k]["flow_rate"] > 0]
    all_combos = [calculate_pressure(list(x), useful_valves, 26, valves) for x in permutations(useful_valves, 3)]
    print(max(all_combos, key=lambda combo: (combo[2])))
