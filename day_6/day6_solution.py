# I'm sure there is a more efficient way of checking that all characters are different but
# this method is very simple and easy to understand. If the sum of the count of each character
# in the list is the same as the length of the list, all the characters are unique, otherwise
# the sum would be higher.
def all_different(list) -> bool:
    return sum([list.count(x) for x in list]) == len(list)

# The method here is pretty simple. We want to find the first sequence of a certain length
# where all the characters are different. So we just keep adding characters and for each character
# we check if all the characters are still different. If they're not, we reset the counter and keep going,
# if we reach the desired length we have our answer and return.
def find_first_different(line: str, size: int) -> int:
    for i in range(0, len(line) - size):
        if all_different(line[i:i+size]):
            return i+size

def get_start_of_packet_marker(input_file: str, length: int) -> int:
    with open(input_file, "r") as file:
        line = file.readlines()[0]
    return find_first_different(line, length)
    
