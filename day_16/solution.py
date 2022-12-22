import math
import re
from itertools import permutations

input_file = "day_16/input.data"

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

with open(input_file, "r") as file:
    all_valves = {}
    for line in file.readlines():
        valve, flow_rate, leads_to = extract_values(line)
        all_valves[valve] = {"flow_rate": flow_rate, "leads_to": leads_to}
    remaining_time = 30
    best_single_path, best_score = get_best_path("AA", 30, [], all_valves, 0, [])
    print(f"{best_single_path}, {best_score}")
    human_path, human_sum = get_best_path("AA", 26, [], all_valves, 0, [])
    elephant_path, elephant_sum = get_best_path("AA", 26, best_single_path, all_valves, 0, [])
    print(elephant_path, elephant_sum, human_path, human_sum, human_sum + elephant_sum)