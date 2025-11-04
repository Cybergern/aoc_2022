input_file = "day_3/input.data"

# We can calculate priority by simply getting the ascii-value and subtracting 
# the number before the first letter for lowercase and uppercase
def get_priority(item: str) -> int:
    if (item.islower()):
        return ord(item) - 96
    else:
        return ord(item) - 38

def split_line(line: str) -> list[str]:
    half_l = len(line) // 2
    return [line[half_l:].strip(), line[:half_l].strip()]

# Easiest way of finding common items is to make sets out of each letter group 
# and find the intersection of those sets.
def find_intersection(group: list[str]) -> str:
    sets = [set(x) for x in group]
    return set.intersection(*sets).pop()

def calc_prio(items: list[str]) -> int:
    return sum([get_priority(x) for x in items])

def get_common_item_priority_sum(input_file: str) -> int:
    with open(input_file, "r") as file:
        items = []
        group = []
        for l in file.readlines():
            items.append(find_intersection(split_line(l)))
            group.append(l.strip())
    return calc_prio(items)

def get_badges_priority_sum(input_file: str) -> int:
    with open(input_file, "r") as file:
        badges = []
        group = []
        for l in file.readlines():
            group.append(l.strip())
            if len(group) == 3:
                badges.append(find_intersection(group))
                group = []
    return calc_prio(badges)
