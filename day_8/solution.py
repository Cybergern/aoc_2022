from functools import reduce

input_file = "day_8/input.data"

def get_tree(x, y, matrix):
    return matrix[y-1][x-1]

def get_row(rownum, matrix):
    return matrix[rownum-1]

def get_column(colnum, matrix):
    return [x[colnum-1] for x in matrix]

def get_directions(x, y, matrix):
    col = get_column(x, matrix)
    row = get_row(y, matrix)
    return {"north": col[:y-1][::-1], "south": col[y:], "west": row[:x-1][::-1], "east": row[x:]}

def is_visible(height, directions):
    if any([len(x) == 0 for x in directions.values()]):
        return True
    elif any([all([x < height for x in d]) for d in directions.values()]):
        return True
    else:
        return False

def trees_visible(base, heights):
    sum = 0
    for x in heights:
        sum += 1
        if x >= base:
            break
    return sum

def count_visible(matrix):
    sum = 0
    for y in range(1, len(matrix) + 1):
        for x in range(1, len(matrix[0]) + 1):
            directions = get_directions(x, y, matrix)
            if (is_visible(get_tree(x, y, matrix), directions)):
                sum += 1
    return sum

def get_scenic_score(x, y, matrix):
    base = get_tree(x, y, matrix)
    directions = get_directions(x, y, matrix)
    return reduce((lambda score, other_score: score * other_score), [trees_visible(base, x) for x in directions.values()])

def get_best_scenic_score(matrix):
    best = 0
    for y in range(1, len(matrix) + 1):
        for x in range(1, len(matrix[0]) + 1):
            score = get_scenic_score(x, y, matrix)
            if score > best:
                best = score
    return best


with open(input_file, "r") as file:
    matrix = []
    for l in file.readlines():
        matrix.append([int(d) for d in l.strip()])
    print(count_visible(matrix))
    print(get_best_scenic_score(matrix))
