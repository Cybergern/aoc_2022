def split_line(line: str) -> list[int]:
    sections = []
    ranges = line.strip().split(",")
    for r in ranges:
        parts = r.split("-")
        sections.append([int(x) for x in parts])
    return sections

def either_range_contains_other(ranges: list[str]) -> bool:
    first_start, first_end, second_start, second_end = ranges[0][0], ranges[0][1], ranges[1][0], ranges[1][1]
    return ((first_start <= second_start) and (first_end >= second_end)) or ((second_start <= first_start) and (second_end >= first_end))

def either_range_overlaps_other(ranges: list[str]) -> bool:
    first_start, first_end, second_start, second_end = ranges[0][0], ranges[0][1], ranges[1][0], ranges[1][1]
    return first_start <= second_end and first_end >= second_start

def get_fully_contained_pairs(input_file: str) -> int:
    contains_count = 0
    with open(input_file, "r") as file:
        for l in file.readlines():
            sections = split_line(l)
            if either_range_contains_other(sections):
                contains_count += 1
    return contains_count

def get_overlapping_pairs(input_file: str) -> int:
    overlaps_count = 0
    with open(input_file, "r") as file:
        for l in file.readlines():
            sections = split_line(l)
            if either_range_overlaps_other(sections):
                overlaps_count += 1
    return overlaps_count
