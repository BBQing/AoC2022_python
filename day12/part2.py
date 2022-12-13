from string import ascii_lowercase

LETTERS = "S" + ascii_lowercase + "E"


def read_file(PATH):
    with open(PATH, 'r') as file:
        for x, line in enumerate(file.readlines()):
            for y, char in enumerate(line.strip()):
                yield x, y, LETTERS.find(char)


class Map:

    def __init__(self, points):
        self.map = dict()
        self.start = None
        self.end = None
        self.counter = 1
        for x, y, ind in points:
            self.map[(x, y)] = ind
            if ind == 0:
                self.start = (x, y)
            if ind == 27:
                self.end = (x, y)
        self.directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        self.map[self.start] = 1
        self.map[self.end] = 26


    def __iter__(self):
        return self.find_the_path()

    def find_the_path(self):
        current_nodes = set()
        visited_nodes = set()
        candidates = set()
        current_nodes = set(node for node, value in self.map.items() if value == 1)
        visited_nodes |= current_nodes
        while self.end not in visited_nodes:
            self.counter += 1
            for node in current_nodes:
                for candidate in self.candidate_nodes(node):
                    if candidate not in visited_nodes:
                        candidates.add(candidate)
            yield 1
            visited_nodes |= current_nodes

            current_nodes = candidates
            if not candidates:
                break
            if self.end in candidates:
                break
            candidates = set()

    def candidate_nodes(self, node):
        x, y = node
        value = self.map.get(node)
        for direction in self.directions:
            a, b = direction
            if (v := self.map.get((cx := x + a, cy := y + b)) ):
                if v - value  <= 1:
                    yield cx, cy
            

if __name__ == '__main__':
    PATH = 'day12/data.txt'
    # PATH = 'day12/test.txt'

    data = Map(read_file(PATH))
    print(sum(data))