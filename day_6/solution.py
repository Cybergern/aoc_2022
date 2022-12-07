input_file = "day_6/input.data"
 
def all_different(list):
    return sum([list.count(x) for x in list]) == len(list)

def find_first_different(line, size):
    for i in range(0, len(line) - size):
        if all_different(line[i:i+size]):
            return i+size

with open(input_file, "r") as file:
    line = file.readlines()[0]
    print([find_first_different(line, x) for x in [4, 14]])
    
