input_file = "day_17/input.data"

def get_map_limits(map):
    global RIGHT_WALL
    return (-1, max([x[1] for x in map])), (RIGHT_WALL, -1)

def draw_map(map, block):
    global RIGHT_WALL
    full_map = set(map).union(set(block))
    upper_left, bottom_right = get_map_limits(full_map)
    for y in range(upper_left[1], bottom_right[1] -1, -1):
        line = f"{y}" + " "*(3-len(str(y)))
        for x in range(upper_left[0], bottom_right[0]+1):
            if (x, y) in [(-1, -1), (RIGHT_WALL, -1)]:
                line += "+"            
            elif x == RIGHT_WALL or x == -1:
                line += "|"
            elif (x, y) in map:
                line += "#"
            elif (x, y) in block:
                line += "@"
            elif y == -1:
                line += "-"
            else:
                line += "."
        print(line)

BLOCKS = [[(0,0), (1,0), (2,0), (3,0)], 
          [(1,0), (0,1), (1,1), (2,1), (1,2)], 
          [(0,0), (1,0), (2,0), (2,1), (2,2)], 
          [(0,0), (0,1), (0,2), (0,3)], 
          [(0,0), (0,1), (1,0), (1,1)]]
RIGHT_WALL = 7

block_counter = 0
jets = ""
jets_counter = 0

def get_next_block():
    global block_counter
    next_block = BLOCKS[block_counter % len(BLOCKS)]
    block_counter += 1
    return next_block

def go_left():
    global jets_counter
    next_jet = jets[jets_counter % len(jets)]
    jets_counter += 1
    return next_jet == "<"

def get_highest_block(map):
    if not map:
        return -1
    return max(map, key=lambda item: item[1])[1]

def spawn_block(map):
    y_offset = get_highest_block(map) + 4
    x_offset = 2
    offset_block = move_block(x_offset, y_offset, get_next_block())
    return offset_block

def move_block(x, y, block):
    return [(c[0]+x, c[1]+y) for c in block]

def move_left(block):
    return move_block(-1, 0, block)

def move_right(block):
    return move_block(1, 0, block)

def move_down(block):
    return move_block(0, -1, block)

def blow_block(block):
    if go_left():
        new_block = move_left(block)
        if not in_wall(new_block) and not in_floor_or_block(new_block, map):
            return new_block
        else:
            return block
    else:
        new_block = move_right(block)
        if not in_wall(new_block) and not in_floor_or_block(new_block, map):
            return new_block
        else:
            return block

def in_wall(block):
    global RIGHT_WALL
    for c in block:
        if c[0] < 0:
            return True
        elif c[0] >= RIGHT_WALL:
            return True
    return False

def in_floor_or_block(block, map):
    for c in block:
        if c in map:
            return True
        elif c[1] < 0:
            return True
    return False

def move_block_down(block, map):
    new_block = move_down(block)
    if in_floor_or_block(new_block, map):
        return True, block
    else:
        return False, new_block

def drop_block(map):
    block = spawn_block(map)
    at_rest = False
    while not at_rest:
        block = blow_block(block)
        at_rest, block = move_block_down(block, map)
    return block

def guess_seq_len(seq, verbose=False):
    seq_len = 1
    initial_item = seq[0]
    butfirst_items = seq[1:]
    if initial_item in butfirst_items:
        first_match_idx = butfirst_items.index(initial_item)
        if verbose:
            print(f'"{initial_item}" was found at index 0 and index {first_match_idx}')
        max_seq_len = min(len(seq) - first_match_idx, first_match_idx)
        for seq_len in range(max_seq_len, 0, -1):
            if seq[:seq_len] == seq[first_match_idx:first_match_idx+seq_len]:
                if verbose:
                    print(f'A sequence length of {seq_len} was found at index {first_match_idx}')
                break
    
    return seq_len

with open(input_file, "r") as file:
    map = set()
    jets = file.readline().strip()
    blocks = 0
    last_height = 0
    sequence = ""
    while blocks < 10000:
        map = map.union(set(drop_block(map)))
        blocks += 1
        high_block = get_highest_block(map)
        sequence += str(high_block - last_height)
        last_height = high_block
    print(get_highest_block(map) + 1)
    print(sequence)

    # Bit of an explanation here. I actually didn't solve this one entierely in code.
    # First took the produced sequence for 10000 blocks, put it in a text editor, marked a long
    # sequence from the back of the sequence and searched for it, found it at 1740 column intervals
    # so then we have the size of the sequence. Then used sequence_finder.py to get the actual sequence and the associated sum.
    # Used this to find the size and then sum of the preamble to the repeating sequence. Finally, used modulo to determine
    # how much of the final iteration of the sequence was left at the end of the final sequence and got the sum of that
    # partial sequence to add at the end. Finally added one just because my height is 0-based. Final expression:

    # 2892 + (2759/1740) * (1000000000000 - 1819 - 1101) + 1744 + 1