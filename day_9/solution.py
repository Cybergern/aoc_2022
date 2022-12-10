input_file = "day_9/input.data"


class SimpleGrid:

    def __init__(self) -> None:
        self.positions = {}
        
    def __repr__(self) -> str:
        max_x = max([x[0] for x in self.positions.values()])
        max_y = max([x[1] for x in self.positions.values()])
        min_x = min([x[0] for x in self.positions.values()])
        min_y = min([x[1] for x in self.positions.values()])
        print(self.positions)
        reverse_pos = {v: k for k, v in self.positions.items()}
        grid = ""
        for y in range(max_y+2, min_y-2, -1):
            line = ""
            for x in range(min_x-2, max_x+2):
                if (x, y) in reverse_pos:
                    line += reverse_pos[(x, y)]
                else:
                    line += "."
            grid += line + "\n"
        return grid

    def __str__(self) -> str:
        return self.__repr__()

    def add(self, x, y, value):
        self.positions[value] = (x, y)

    def remove(self, x, y, value):
        self.positions.pop(value)

    def get(self, x, y):
        values = []
        for value in self.positions.keys():
            if self.positions[value] == (x, y):
                values.append(value)
        return values

    def find(self, value):
        if value in self.positions:
            return self.positions[value]
        else:
            return -1, -1

class MultipleKnotGrid:

    DIRECTIONS = {"U": (0, 1), "R": (1, 0), "D": (0, -1), "L": (-1, 0)}

    def __init__(self, length) -> None:
        self.grid = SimpleGrid()
        self.length = length
        for x in range(0, length):
            self.grid.add(0, 0, str(x))
        pass

    def __repr__(self) -> str:
        return self.grid.__repr__()

    def get_knot(self, knot):
        return self.grid.find(str(knot))

    def _move_thing(self, move, value):
        value = str(value)
        x, y = self.grid.find(value)
        self.grid.remove(x, y, value)
        self.grid.add(x + move[0], y + move[1], value)
    
    def _knot_too_far_away(self, knot):
        head = self.get_knot(knot - 1)
        tail = self.get_knot(knot)
        return any([abs(x) > 1 for x in [head[0] - tail[0], head[1] - tail[1]]])
    
    def move_head(self, direction):
        move = self.DIRECTIONS[direction]
        self._move_thing(move, 0)
        for x in range(1, self.length):
            if self._knot_too_far_away(x):
                self._move_knot(x)
            else:
                break

    def _get_knot_diff(self, knot):
        head = self.get_knot(knot - 1)
        tail = self.get_knot(knot)
        x_diff = head[0] - tail[0]
        y_diff = head[1] - tail[1]
        return x_diff, y_diff
    
    @staticmethod
    def sign(num):
        if num > 0:
            return 1
        elif num == 0:
            return 0
        else:
            return -1

    def _get_needed_move(self, knot):
        x_diff, y_diff = self._get_knot_diff(knot)
        return (self.sign(x_diff), self.sign(y_diff))

    def _move_knot(self, knot):
        moves = self._get_needed_move(knot)
        self._move_thing(moves, knot)

with open(input_file, "r") as file:
    moves = []
    for l in file.readlines():
        moves.append(l.strip().split())
    grid = MultipleKnotGrid(2)
    unique_positions = [grid.get_knot(1)]
    for move in moves:
        for _ in range(0, int(move[1])):
            grid.move_head(move[0])
            if grid.get_knot(1) not in unique_positions:
                unique_positions.append(grid.get_knot(1))
    print(len(unique_positions))

    grid = MultipleKnotGrid(10)
    unique_positions = [grid.get_knot(9)]
    for move in moves:
        for _ in range(0, int(move[1])):
            grid.move_head(move[0])
            if grid.get_knot(9) not in unique_positions:
                unique_positions.append(grid.get_knot(9))
    print(len(unique_positions))
