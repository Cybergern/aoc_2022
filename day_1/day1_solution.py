
# Just go through the list, line by line. If there is a value, add it to the sum.
# Once we get an empty line, the sum is finished so we add it to the list. Keep going
# until we run out of file.
def get_calory_totals(input_file: str) -> list[int]:
    totals = []
    with open(input_file, "r") as file:
        cur = 0
        for l in file.readlines():
            # Empty row means we can summarize calory count gathered so far
            if (l.strip() == ""):
                totals.append(cur)
                cur = 0
            else:
                cur += int(l.strip())
        totals.append(cur)
    totals.sort()
    totals.reverse()
    return totals

def get_top_calory_total(input_file: str) -> int:
    return get_calory_totals(input_file)[0]

def get_top_three_calory_sum(input_file: str) -> int:
    return sum(get_calory_totals(input_file)[0:3])