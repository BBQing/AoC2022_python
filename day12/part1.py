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
        current_nodes.add(self.start)
        visited_nodes.add(self.start)
        while self.end not in visited_nodes:
            # print(f"cycle {self.counter} {current_nodes}")
            if self.end in visited_nodes:
                print("Something")
            self.counter += 1
            for node in current_nodes:
                for candidate in self.candidate_nodes(node):
                    if candidate not in visited_nodes:
                        candidates.add(candidate)
            yield 1
            print(len(visited_nodes), len(current_nodes), len(candidates), set(LETTERS[self.map.get(node)] for node in candidates))
            visited_nodes |= current_nodes

            current_nodes = candidates
            if not candidates:
                break
            if self.end in candidates:
                print("here")
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
    # print(LETTERS)
    # print(data.map)
    # print(data.start)
    # print(data.end)
    # print(LETTERS[19])
    print(sum(data))