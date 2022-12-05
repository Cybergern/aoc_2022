input_file = "day_3/input.data"

def get_priority(item):
    if (item.islower()):
        return ord(item) - 96
    else:
        return ord(item) - 38

def split_line(line):
    half_l = len(line) // 2
    return [line[half_l:].strip(), line[:half_l].strip()]

def find_intersection(list):
    sets = [set(x) for x in list]
    return set.intersection(*sets).pop()

def calc_prio(items):
    return sum([get_priority(x) for x in items])

with open(input_file, "r") as file:
    items = []
    badges = []
    group = []
    for l in file.readlines():
        items.append(find_intersection(split_line(l)))
        group.append(l.strip())
        if len(group) == 3:
            badges.append(find_intersection(group))
            group = []

print(calc_prio(items))
print(calc_prio(badges))