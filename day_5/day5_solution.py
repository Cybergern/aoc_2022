def file_split(lines: list[str]) -> tuple[list[str], list[str], list[str]]:
    column_start = 0
    for i in range(0, len(lines)):
        line = lines[i]
        if (line.startswith(" 1")):
            column_start = i
            return lines[:column_start], lines[column_start].strip(), lines[column_start+2:]

def add_stack_values(line: list[str], stacks: dict[str,list[str]]):
    pos = 1
    col = 1
    while(pos < len(line)):
        if line[pos].strip():
            stacks[str(col)].append(line[pos])
        col += 1
        pos += 4

def get_moves(line: str) -> tuple[str, str, str]:
    parts = line.strip().split()
    return parts[1], parts[3], parts[5]

def apply_single_moves(line: str, stacks: dict[str,list[str]]):
    no_of_moves, from_stack, to_stack = get_moves(line)
    for x in range(0, int(no_of_moves)):
        stacks[to_stack].append(stacks[from_stack].pop())

def apply_multiple_moves(line: str, stacks: dict[str,list[str]]):
    no_of_moves, from_stack, to_stack = get_moves(line)
    to_move = stacks[from_stack][-int(no_of_moves):]
    stacks[from_stack] = stacks[from_stack][:-int(no_of_moves)]
    stacks[to_stack].extend(to_move)

def get_last_element(stacks: dict[str,list[str]], key) -> str:
    return stacks[key][len(stacks[key])-1]

def get_top_boxes(stacks: dict[str]) -> list[str]:
    return [get_last_element(stacks, x) for x in stacks.keys()]

def get_stacks_and_moves(input_file: str) -> tuple[dict[str,list[str]], list[str]]:
    with open(input_file, "r") as file:
        stacks = {}
        lines = file.readlines()
        start, columns, moves = file_split(lines)
        for x in columns.strip().split():
            stacks[x] = []
        start.reverse()
        for x in start:
            add_stack_values(x, stacks)
    return stacks, moves

def get_single_crate_move_top_crates(input_file: str) -> str:
    stacks, moves = get_stacks_and_moves(input_file)
    for x in moves:
        apply_single_moves(x, stacks)
    return "".join(get_top_boxes(stacks))

def get_multiple_crate_move_top_crates(input_file: str) -> str:
    stacks, moves = get_stacks_and_moves(input_file)
    for x in moves:
        apply_multiple_moves(x, stacks)
    return "".join(get_top_boxes(stacks))
