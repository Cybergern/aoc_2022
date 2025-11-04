# To me, the easiest way of reading the input was to find the line starting with " 1", since this would be
# the line showing the bottom of the columns in order. I would then know that the rows above contained the
# column states and the ones below (except the very next one) contained the moves.
def file_split(lines: list[str]) -> tuple[list[str], list[str], list[str]]:
    column_start = 0
    for i in range(0, len(lines)):
        line = lines[i]
        if (line.startswith(" 1")):
            column_start = i
            return lines[:column_start], lines[column_start].strip(), lines[column_start+2:]

# This is just a complicated looking way of setting up the start values for each column.
# We know that the columns always start at index 1 and each column is separated by three characters
# so for each line, we can just skip through to index 5 for the next column, etc.
# We do need to know how many columns there are though, since the right-most columns can be empty from the start.
def add_stack_starting_values(start: list[list[str]], columns: list[str]) -> dict[str,list[str]]:
    stacks = {}
    for x in columns.strip().split():
        stacks[x] = []
    for line in start:
        pos = 1
        col = 1
        while(pos < len(line)):
            if line[pos].strip():
                stacks[str(col)].append(line[pos])
            col += 1
            pos += 4
    return stacks

# Move format is always "move 1 from 2 to 1", we can ignore the text since it is always the same.
def get_moves(line: str) -> tuple[str, str, str]:
    parts = line.strip().split()
    return parts[1], parts[3], parts[5]

# This is the implementation for the first part of the problem, we can only move one box at a time.
# So we just pop them off one stack and push them on to another for the number of moves required.
# Stacks is edited directly to avoid a bunch of copying.
def apply_single_moves(line: str, stacks: dict[str,list[str]]):
    no_of_moves, from_stack, to_stack = get_moves(line)
    for x in range(0, int(no_of_moves)):
        stacks[to_stack].append(stacks[from_stack].pop())

# This is the implementation for the second part of the problem, we can move multiple boxes at a time.
# This will matter because the order of the boxes moved will stay the same rather than reversing as
# they do when moved one by one.
# Stacks is edited directly to avoid a bunch of copying.
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
        lines = file.readlines()
        start, columns, moves = file_split(lines)
        # The reverse is here because we read the values top to bottom,
        # but we want to add them in the opposite order. Also, the reverse method
        # reverses in place instead of returning a reversed list.
        start.reverse()
        stacks = add_stack_starting_values(start, columns)
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
