input_file = "day_4/input.data"

def split_line(line):
    sections = []
    ranges = line.strip().split(",")
    for r in ranges:
        parts = r.split("-")
        sections.append([int(x) for x in parts])
    return sections

def either_range_contains_other(ranges):
    first_start, first_end, second_start, second_end = ranges[0][0], ranges[0][1], ranges[1][0], ranges[1][1]
    return ((first_start <= second_start) and (first_end >= second_end)) or ((second_start <= first_start) and (second_end >= first_end))

def either_range_overlaps_other(ranges):
    first_start, first_end, second_start, second_end = ranges[0][0], ranges[0][1], ranges[1][0], ranges[1][1]
    return first_start <= second_end and first_end >= second_start

with open(input_file, "r") as file:
    contains_sum = 0
    overlaps_sum = 0
    for l in file.readlines():
        sections = split_line(l)
        if either_range_contains_other(sections):
            contains_sum += 1
        if either_range_overlaps_other(sections):
            overlaps_sum += 1

print(contains_sum)
print(overlaps_sum)
