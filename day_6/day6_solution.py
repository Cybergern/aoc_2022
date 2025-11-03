def all_different(list) -> bool:
    return sum([list.count(x) for x in list]) == len(list)

def find_first_different(line: str, size: int) -> int:
    for i in range(0, len(line) - size):
        if all_different(line[i:i+size]):
            return i+size

def get_start_of_packet_marker(input_file: str, length: int) -> int:
    with open(input_file, "r") as file:
        line = file.readlines()[0]
    return find_first_different(line, length)
    
