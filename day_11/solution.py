from math import floor
import math

input_file = "day_11/input.data"

class Monkey:
    def __init__(self, starting_items, operation, test_divisor, monkeys) -> None:
        self.items = starting_items
        self.operation = operation
        self.test_divisor = test_divisor
        self.monkeys = monkeys
        self.inspections = 0

    def set_lcm(self, lcm):
        self.lcm = lcm

    def inspect(self, old):
        self.inspections += 1
        return int(eval(self.operation))

    def bored(self, item):
        return floor(item / 3)

    def test(self, value):
        return value % self.test_divisor == 0

    def throw(self):
        item = self.items.pop(0)
        item = self.inspect(item)
        item = self.bored(item)
        if self.test(item):
            return item, self.monkeys[0]
        else:
            return item, self.monkeys[1]

    def catch(self, item):
        self.items.append(item)

    def items_left(self):
        return len(self.items) > 0

    def no_of_inspections(self):
        return self.inspections

    def __repr__(self) -> str:
        repr = f"Items: {str(self.items)}\n"
        repr += f"Operation: {self.operation}\n"
        repr += f"Test divisor: {self.test_divisor}\n"
        repr += f"Monkeys: {str(self.monkeys)}\n"
        repr += f"Inspections: {str(self.inspections)}\n"
        return repr

class WorryMonkey(Monkey):
    def bored(self, item):
        return item % self.lcm

def get_remainder(part, text):
    part_end_index = text.index(part) + len(part) - 1
    remainder = text[part_end_index:]
    return remainder.strip()

def make_monkey(info, MonkeyClass):
    starting_items = [int(x.strip()) for x in get_remainder("Starting items: ", info[1]).split(",")]
    operation = get_remainder("Operation: new = ", info[2])
    test_divisor = int(get_remainder("Test: divisible by ", info[3]))
    monkeys = (int(get_remainder("If true: throw to monkey ", info[4])), int(get_remainder("If false: throw to monkey ", info[5])))
    return MonkeyClass(starting_items, operation, test_divisor, monkeys)

def set_lcm(monkeys):
    lcm = math.lcm(*[m.test_divisor for m in monkeys])
    for m in monkeys:
        m.set_lcm(lcm)

def get_two_worst_monkeys(MonkeyClass, rounds, lines):
    monkeys = []
    monkey = []
    for line in lines:
        if line.strip() == "":
            monkeys.append(make_monkey(monkey, MonkeyClass))
            monkey = []
        else:
            monkey.append(line.strip())
    set_lcm(monkeys)
    for _ in range(0, rounds):
        for m in monkeys:
            while(m.items_left()):
                item, receiver = m.throw()
                monkeys[receiver].catch(item)
    inspections = sorted([m.no_of_inspections() for m in monkeys], reverse=True)
    return inspections[0], inspections[1]

with open(input_file, "r") as file:
    lines = file.readlines()
    first_two_monkeys = get_two_worst_monkeys(Monkey, 20, lines)
    print(first_two_monkeys[0] * first_two_monkeys[1])
    second_two_monkeys = get_two_worst_monkeys(WorryMonkey, 10000, lines)
    print(second_two_monkeys[0] * second_two_monkeys[1])
