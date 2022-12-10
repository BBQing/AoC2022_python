
def read_file(path):

    with open(path, 'r') as file:
        for line in file.readlines():
            cmd, n = line.strip().split(" ")
            yield cmd, int(n)


class Head:

    def __init__(self) -> None:
        self.x = 0
        self.y = 0
        self.tail = None

    def add_tail(self, tail):
        self.tail = tail

    def notify(self):
        yield from self.tail.update(self.x, self.y)

    def move(self, cmd):
        if cmd == 'R':
            self.y += 1
        if cmd == 'L':
            self.y -= 1
        if cmd == 'U':
            self.x += 1
        if cmd == 'D':
            self.x -= 1

    def run_command(self, cmd, n):
        for _ in range(n):
            self.move(cmd)
            yield from self.notify()

    def run(self, data):
        for cmd, n in data:
            yield from self.run_command(cmd, n)


class Tail:

    def __init__(self, head):
        self.x = 0
        self.y = 0
        head.add_tail(self)

    def update(self, x, y):
        x_diff = x - self.x
        y_diff = y - self.y
        if x_diff in [-2, 2] or y_diff in [-2, 2]:

            self.x = self.x + self.cutoff(x_diff)
            self.y = self.y + self.cutoff(y_diff)

        yield self.x, self.y

    def cutoff(self, diff):
        if diff == 2:
            return 1
        if diff == -2:
            return -1
        return diff


def process_commands(data):

    head = Head()

    Tail(head)

    return set(head.run(data))


if __name__ == '__main__':
    PATH = 'day09/data.txt'
    PATH = 'day09/test.txt'

    result = process_commands(read_file(PATH))
    print(result)
    print(len(result))
