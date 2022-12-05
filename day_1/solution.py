input_file = "day_1/input.data"

with open(input_file, "r") as file:
    totals = []
    cur = 0
    for l in file.readlines():
        if (l.strip() == ""):
            totals.append(cur)
            cur = 0
        else:
            cur += int(l.strip())

totals.sort()
totals.reverse()
print(totals[0:3])
print(sum(totals[0:3]))