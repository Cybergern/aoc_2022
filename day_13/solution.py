import functools


input_file = "day_13/input.data"

def compare(item1, item2):
    if isinstance(item1, int) and isinstance(item2, int):
        if item1 < item2:
            return -1
        elif item1 == item2:
            return 0
        else:
            return 1
    if isinstance(item1, int):
        item1 = [item1]
    if isinstance(item2, int):
        item2 = [item2]
    if len(item1) == 0 and len(item2) > 0:
        return -1
    if len(item2) == 0 and len(item1) > 0:
        return 1
    else:
        for i in range(0, len(item1)):
            if i == len(item2):
                return 1
            result = compare(item1[i], item2[i])
            if result != 0:
                return result
        if len(item1) == len(item2):
            return 0
        else:
            return -1

def part_1(pairs):
    sum = 0
    print([compare(*x) for x in pairs])
    for i, item in enumerate([compare(*x) for x in pairs]):
        if item == -1:
            sum += (i + 1)
    return sum

def part_2(pairs):
    flat_list = []
    for pair in pairs:
        flat_list.append(pair[0])
        flat_list.append(pair[1])
    flat_list.append([[2]])
    flat_list.append([[6]])
    sorted_list = sorted(flat_list, key=functools.cmp_to_key(compare))
    decoder_key = 1
    for i, item in enumerate(sorted_list):
        if str(item) in ["[[2]]", "[[6]]"]:
            decoder_key *= (i + 1)
    return decoder_key

with open(input_file, "r") as file:
    pairs = []
    pair = []
    for line in file.readlines():
        if line.strip() == "":
            pairs.append((pair[0], pair[1]))
            pair = []
        else:
            pair.append(eval(line.strip()))
    pairs.append((pair[0], pair[1]))
    sum = part_1(pairs)
    print(sum)
    decoder_key = part_2(pairs)
    print(decoder_key)