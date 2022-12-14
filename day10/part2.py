
import re
from itertools import cycle, islice

cmd_pattern = re.compile(r'addx (-?\d+)')


def read_file(path):

    with open(path, 'r') as file:
        for line in file.readlines():
            cmd = cmd_pattern.match(line.strip())
            if cmd is not None:
                yield int(cmd.group(1))
            else:
                yield None

def batched(iterable, n):
    "Batch data into lists of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while (batch := list(islice(it, n))):
        yield batch

class Register:

    def __init__(self) -> None:
        self.X = 1

    def noop(self):
        yield self.X

    def addx(self, x):
        for _ in range(2):
            yield from self.noop()
        self.X += x

    def execute(self, cmd):
        if cmd is None:
            yield from self.noop()
        else:
            yield from self.addx(cmd)

    def commands(self, cmds):
        for cmd in cmds:
            yield from self.execute(cmd)

    def draw_pixel(self, pos):
        if abs(pos - self.X) <= 1:
            return '#'
        else:
            return '.'

    def pixels(self, PATH):
        
        register_states = zip(cycle(range(40)), self.commands(read_file(PATH)))
        for ind, _ in register_states:
            yield self.draw_pixel(ind)
        
    


if __name__ == '__main__':
    PATH = 'day10/data.txt'
    # PATH = 'day10/test.txt'

    register = Register()

    for line in batched(register.pixels(PATH), 40):
        print(''.join(line))
