
import re
from itertools import islice

cmd_pattern = re.compile(r'addx (-?\d+)')


def read_file(path):

    with open(path, 'r') as file:
        for line in file.readlines():
            cmd = cmd_pattern.match(line.strip())
            if cmd is not None:
                yield int(cmd.group(1))
            else:
                yield None


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


def signal_stength(input):
    ind, X = input
    return ind * X


def signal_strengths(PATH):
    register = Register()
    register_states = enumerate(register.commands(read_file(PATH)), 1)

    return sum(map(signal_stength, islice(register_states, 19, 220, 40)))
    


if __name__ == '__main__':
    PATH = 'day10/data.txt'
    # PATH = 'day10/test.txt'

    

    print(signal_strengths(PATH))
