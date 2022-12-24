from itertools import chain
facings = {
    "<": [0, -1],
    ">": [0, 1],
    "^":  [-1, 0],
    "v": [1, 0],
}


def read_file(PATH):
    with open(PATH, "r") as file:
        for x, line in enumerate(file.readlines()):
            for y, char in enumerate(line.strip()):
                yield x, y, char


class BlizzardField:

    def __init__(self, fields) -> None:
        self.data = dict()
        self.blizzards = []
        self.start = (0, 1)
        self.end = None
        self.walls = set()
        self.x_size = 0
        self.y_size = 0

        self.process_fields(fields)
        self.current_blizzards = set(map(next, self.blizzards))

    def process_fields(self, fields):
        for x, y, char in fields:
            if char == "#":
                self.walls.add((x, y))
            if char in ["v", "^", ">", "<"]:
                self.blizzards.append(self.blizzard(x, y, facings[char]))

        self.x_size = max(x[0] for x in self.walls)
        self.y_size = max(x[1] for x in self.walls)
        self.end = self.x_size, self.y_size - 1

    def blizzard(self, x, y, facing):
        while True:
            yield x, y
            x += facing[0]
            y += facing[1]
            while (x, y) in self.walls:
                x += facing[0]
                x %= self.x_size
                y += facing[1]
                y %= self.y_size

    def next_blizards(self):
        for blizzard in self.blizzards:
            yield next(blizzard)

    def walk(self):
        new_blizzards = set(self.next_blizards())
        candidates = set(self.create_candidates(*self.start))
        # for _ in range(3):
        while self.end not in candidates:
            candidates -= self.walls
            candidates -= new_blizzards
            yield 1
            new_blizzards = set(self.next_blizards())
            candidates = set(chain.from_iterable(
                self.create_candidates(*x) for x in candidates))

    def walk_from_start(self, start, end):
        self.start = start
        self.end = end
        yield from self.walk()

    def create_candidates(self, x, y):
        yield x, y
        for facing in facings.values():
            new_x, new_y = x + facing[0], y + facing[1]
            if new_x >= 0 and new_y >= 0:
                yield new_x, new_y


if __name__ == '__main__':
    PATH = 'day24/data.txt'
    # PATH = 'day24/test.txt'

    blizzard_field = BlizzardField(read_file(PATH))

    print(
        sum(
            sum(blizzard_field.walk_from_start(start, end))+1
            for start, end in [
                [(0, 1), (blizzard_field.x_size, blizzard_field.y_size - 1)],
                [(blizzard_field.x_size, blizzard_field.y_size - 1), (0, 1)],
                [(0, 1), (blizzard_field.x_size, blizzard_field.y_size - 1)]
            ]
        )
    )
