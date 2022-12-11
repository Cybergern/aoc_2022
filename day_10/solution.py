input_file = "day_10/input.data"

class Processor:
    def __init__(self, queue, save_cycles) -> None:
        self.queue = queue
        self.current = ""
        self.time_left = 0
        self.cycle = 0
        self.x = 1
        self.save_cycles = save_cycles

    def tick(self):
        self.cycle += 1
        if self.current == "":
            self.current = self.queue.pop(0)
            if self.current.startswith("noop"):
                self.time_left = 0
            else:
                self.time_left = 1
        else:
            self.time_left -= 1
        if self.current.startswith("noop"):
            self.noop()
        elif self.current.startswith("addx") and self.time_left == 0:
            value = int(self.current.split()[1])
            self.addx(value)
                
    def reset(self):
        self.current = ""

    def noop(self):
        self.reset()

    def addx(self, value):
        self.x += value
        self.reset()
    
    def row_num(self, value):
        return (value % 40)

    def get_sprite(self):
        return [x for x in range(self.x - 1, self.x + 2)]

    def run(self):
        signal_strengths = []
        pixels = []
        while(self.queue or self.current != ""):
            if self.cycle in self.save_cycles:
                signal_strengths.append(self.x * self.cycle)
            if self.row_num(self.cycle) in self.get_sprite():
                pixels.append(self.cycle)
            self.tick()
        return signal_strengths, pixels

with open(input_file, "r") as file:
    instructions = []
    for line in file.readlines():
        instructions.append(line.strip())
    proc = Processor(instructions, [20, 60, 100, 140, 180, 220])
    signal_strengths, pixels = proc.run()
    print(sum(signal_strengths))
    pixel_output = ""
    for i in range(0, 240):
        if i in pixels:
            pixel_output += "#"
        else:
            pixel_output += "."
        if i % 40 == 39:
            pixel_output += "\n"
    print(pixel_output)