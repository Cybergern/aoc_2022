import math
import re

input_file = "day_19/input.data"

input_pattern = re.compile('^Blueprint ([0-9]+): Each ore robot costs ([0-9]+) ore. Each clay robot costs ([0-9]+) ore. Each obsidian robot costs ([0-9]+) ore and ([0-9]+) clay. Each geode robot costs ([0-9]+) ore and ([0-9]+) obsidian.')

TYPES = ["ore", "clay", "obsidian", "geode"]

def extract_values(line):
    m = input_pattern.match(line.strip())
    costs = {}
    costs = {"ore": {}, "clay": {}, "obsidian": {}, "geode": {}}
    costs["ore"]["ore"] = int(m.group(2))
    costs["clay"]["ore"] = int(m.group(3))
    costs["obsidian"]["ore"] = int(m.group(4))
    costs["obsidian"]["clay"] = int(m.group(5))
    costs["geode"]["ore"] = int(m.group(6))
    costs["geode"]["obsidian"] = int(m.group(7))
    return int(m.group(1)), costs

def can_build(costs, materials, robots, limits):
    possible = []
    for robot, rob_mats in costs.items():
        if all([materials[k] >= v for k,v in rob_mats.items()]) and robots[robot] < limits[robot]:
            possible.append(robot)
    return possible

def build_robot(robot_to_build, robots, cost, materials):
    new_materials = materials.copy()
    new_robots = robots.copy()
    for k, v in cost.items():
        new_materials[k] -= v
    new_robots[robot_to_build] += 1
    return new_robots, new_materials

def mine(robots, materials, debug=False):
    new_materials = materials.copy()
    for t in TYPES:
        new_materials[t] += robots[t]
        if robots[t] > 0:
            if debug:
                print(f"{robots[t]} {t}-collecting robot(s) collect {robots[t]} {t}; you now have {new_materials[t]} {t}.")
    return new_materials    

def make_cache_key(goal, remaining_time, materials, robots):
    return f"{goal}|{str(remaining_time)}|{'|'.join([str(x) for x in materials.values()])}|{'|'.join([str(x) for x in robots.values()])}"

cache = {}

def simulate_rec(costs, goal, remaining_time, materials, robots, limits):
    global cache
    if remaining_time == 0:
        return materials["geode"]
    cache_key = make_cache_key(goal, remaining_time, materials, robots)
    if cache_key in cache:
        return cache[cache_key]
    new_max = 0
    while(remaining_time > 0):
        possible = can_build(costs, materials, robots, limits)
        if goal in possible:
            tmpMax = 0
            new_materials = mine(robots, materials)
            new_robots, new_materials = build_robot(goal, robots, costs[goal], new_materials)
            for new_goal in TYPES:
                tmpMax = max(tmpMax, simulate_rec(costs, new_goal, remaining_time-1, new_materials, new_robots, limits))
            new_max = max(new_max, tmpMax)
            cache[cache_key] = new_max
            return new_max
        else:
            materials = mine(robots, materials)
            remaining_time -= 1
            new_max = max(new_max, materials["geode"])
    cache[cache_key] = new_max
    return new_max

def make_limits(costs):
    limits = {"ore": 0, "clay": 0, "obsidian": 0, "geode": math.inf}
    for t in TYPES:
        for k,v in costs[t].items():
            limits[k] = max(v, limits[k])
    return limits

def get_max_geodes(costs):
    global cache
    results = []
    limits = make_limits(costs)
    cache = {}
    for start_goal in TYPES:
        results.append(simulate_rec(costs, start_goal, 24, {"ore": 0, "clay": 0, "obsidian": 0, "geode": 0}, {"ore": 1, "clay": 0, "obsidian": 0, "geode": 0}, limits))
    return max(results)

with open(input_file, "r") as file:
    bp = {}
    for line in file.readlines():
        number, costs = extract_values(line)
        bp[number] = costs
    geode_result = {}
    for k,v in bp.items():
        geodes = get_max_geodes(v)
        geode_result[k] = geodes
        print(f"{k}: {geodes}")
    print(sum([k*v for k,v in geode_result.items()]))