import copy


input_file = "day_5/input.data"
 
def file_split(lines):
    column_start = 0
    for i in range(0, len(lines)):
        line = lines[i]
        if (line.startswith(" 1")):
            column_start = i
            break
    return lines[:column_start], lines[column_start].strip(), lines[column_start+2:]

def add_stack_values(line, stacks):
    pos = 1
    col = 1
    while(pos < len(line)):
        if line[pos].strip():
            stacks[str(col)].append(line[pos])
        col += 1
        pos += 4

def get_moves(line):
    parts = line.strip().split()
    return parts[1], parts[3], parts[5]

def apply_single_moves(line, stacks):
    no_of_moves, from_stack, to_stack = get_moves(line)
    for x in range(0, int(no_of_moves)):
        stacks[to_stack].append(stacks[from_stack].pop())

def apply_multiple_moves(line, stacks):
    no_of_moves, from_stack, to_stack = get_moves(line)
    to_move = stacks[from_stack][-int(no_of_moves):]
    stacks[from_stack] = stacks[from_stack][:-int(no_of_moves)]
    stacks[to_stack].extend(to_move)

def get_last_element(stacks, key):
    return stacks[key][len(stacks[key])-1]

def get_top_boxes(stacks):
    return [get_last_element(stacks, x) for x in stacks.keys()]

with open(input_file, "r") as file:
    stacks = {}
    lines = file.readlines()
    start, columns, moves = file_split(lines)
    for x in columns.strip().split():
        stacks[x] = []
    start.reverse()
    for x in start:
        add_stack_values(x, stacks)
    second_stacks = copy.deepcopy(stacks)
    for x in moves:
        apply_single_moves(x, stacks)
        apply_multiple_moves(x, second_stacks)
    print(get_top_boxes(stacks))
    print(get_top_boxes(second_stacks))

        

