def read_file(PATH):
    with open(PATH, 'r') as file:
        for line in file.readlines():
            yield [parse_vertex(vertex) for vertex in line.strip().split(" -> ")]


def parse_vertex(vertex):
    x, y = vertex.split(",")
    return int(x), int(y)


class Maze:

    def __init__(self, walls) -> None:
        self.data = set()
        for wall in walls:
            self.insert_wall(wall)
        self.bottom_limit = max(self.data, key=lambda x: x[1])[1]
        self.sand_start = (500, 0)
        self.counter = 0

    def insert_wall(self, wall):
        for i in range(len(wall) - 1):
            x0, y0 = wall[i]
            x1, y1 = wall[i+1]
            if x0 == x1:
                if y0 > y1:
                    for y in range(y1, y0 + 1):
                        self.data.add((x0, y))
                else:
                    for y in range(y0, y1 + 1):
                        self.data.add((x0, y))
            elif y0 == y1:
                if x0 > x1:
                    for x in range(x1, x0 + 1):
                        self.data.add((x, y0))
                else:
                    for x in range(x0, x1 + 1):
                        self.data.add((x, y0))
    
    def sand_fall(self):
        if self.sand_start in self.data:
            return True
        sand_x, sand_y = self.sand_start
        

        while sand_y <= self.bottom_limit:
            if (sand_x, sand_y + 1) not in self.data:
                sand_y += 1
            elif (sand_x - 1, sand_y + 1) not in self.data:
                sand_y += 1
                sand_x -= 1
            elif (sand_x + 1, sand_y + 1) not in self.data:
                sand_y += 1
                sand_x += 1
            else:
                break
        self.data.add((sand_x, sand_y))
        return False

    def __call__(self):
        state = self.sand_fall()
        if not state:
            self.counter += 1
        return state





if __name__ == '__main__':
    PATH = 'day14/data.txt'
    # PATH = 'day14/test.txt'

    maze = Maze(read_file(PATH))
    for i in iter(maze, True):
        pass
    print(maze.counter)
