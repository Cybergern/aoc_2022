from time import sleep


input_file = "day_14/input.data"

def make_map(lines):
    map = []
    for line in lines:
        for i in range(0, len(line) - 1):
            map.extend(get_coords_between(line[i], line[i+1]))
    return set(map)
            
def get_numbers_between(first, second):
    if first > second:
        return [x for x in range(second, first+1)]
    else:
        return [x for x in range(first, second+1)]

def get_coords_between(start, end):
    if start[0] == end[0]:
        return [(start[0], y) for y in get_numbers_between(start[1], end[1])]
    else:
        return [(x, start[1]) for x in get_numbers_between(start[0], end[0])]

def get_coord_list(line):
    coord_list = []
    parts = line.strip().split(" -> ")
    for p in parts:
        coord_list.append(tuple([int(x) for x in p.split(",")]))
    return coord_list

def get_map_limits(map):
    return (min([x[0] for x in map]), 0), (max([x[0] for x in map]), max([x[1] for x in map]))

def draw_map(map, sand):
    full_map = map.union(sand)
    upper_left, bottom_right = get_map_limits(full_map)
    for y in range(upper_left[1], bottom_right[1]+1):
        line = f"{y} "
        for x in range(upper_left[0], bottom_right[0]+1):
            if (x, y) == (500, 0):
                line += "+"
            elif (x, y) in map:
                line += "#"
            elif (x, y) in sand:
                line += "o"
            else:
                line += "."
        print(line)

def get_free(sand, map, sand_map, bottom=0):
    straight_down = (sand[0], sand[1] + 1)
    down_left = (sand[0] - 1, sand[1] + 1)
    down_right = (sand[0] + 1, sand[1] + 1)
    if bottom != 0 and sand[1] + 1 == bottom:
        return None
    if straight_down not in map and straight_down not in sand_map:
        return straight_down
    elif down_left not in map and down_left not in sand_map:
        return down_left
    elif down_right not in map and down_right not in sand_map:
        return down_right
    else:
        return None

def drop_sand(map, sand_map, bottom, bottomless=True):
    sand = (500,0)
    new_pos = get_free(sand, map, sand_map)
    while new_pos is not None and sand[1] != bottom:
        sand = new_pos
        if bottomless:
            new_pos = get_free(sand, map, sand_map)
        else:
            new_pos = get_free(sand, map, sand_map, bottom=bottom)
    return sand

with open(input_file, "r") as file:
    lines = []
    for line in file.readlines():
        lines.append(get_coord_list(line))
    map = make_map(lines)
    sand = set()
    current_sand = (500,0)
    upper_left, bottom_right = get_map_limits(map)
    while (current_sand[1] != bottom_right[1]):
        current_sand = drop_sand(map, sand, bottom_right[1])
        sand.add(current_sand)
    draw_map(map, sand)
    print(len(sand) - 1)
    sand = set()
    drop_point = (500, 1)
    while(current_sand != (500, 0)):
        current_sand = drop_sand(map, sand, bottom_right[1] + 2, bottomless=False)
        sand.add(current_sand)
        if len(sand) % 1000 == 0:
            print(len(sand))
            draw_map(map, sand)

    sand.add(current_sand)
    draw_map(map, sand)
    print(len(sand))
