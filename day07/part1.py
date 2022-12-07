class Leaf:

    def __init__(self, name, size, parent=None):
        self.parent = parent
        self.name = name
        self.size = size


class Node:
    def __init__(self, name, parent=None):
        self.children = dict()
        self.name = name
        self.parent = parent
        self._size = None

    @property
    def size(self):
        if self._size is None:
            self._size = sum(child.size for child in self.children.values())
        return self._size

    @property
    def directories(self):
        yield self
        for child in self.children.values():
            if isinstance(child, Node):
                yield from child.directories

class Command:
    pass


class Ls(Command):
    pass


class Cd(Command):

    def __init__(self, dir) -> None:
        self.dir = dir


class FileSystem:

    def __init__(self, lines):
        self.root = None
        self.current_directory = None
        self.populate_filesystem(lines)

    def populate_filesystem(self, lines):
        for line in lines:
            command = parse_line(line)
            if isinstance(command, Cd):
                self.cd(command)
            if isinstance(command, Ls):
                pass
            if isinstance(command, (Leaf, Node)):
                command.parent = self.current_directory
                self.current_directory.children[command.name] = command
            
    def cd(self, command):
        if self.root == None:
            self.root = Node(command.dir)
            self.current_directory = self.root
            return
        if command.dir == '..':
            self.current_directory = self.current_directory.parent
        else:
            self.current_directory = self.current_directory.children[command.dir]

def read_file(path):
    with open(path, 'r') as file:
        for line in file.readlines():
            yield line.strip()


def parse_line(line):
    if line.startswith('$'):
        _, *command = line.split(" ")
        if len(command) == 1:
            return Ls()
        else:
            return Cd(command[1])
    else:
        first, second = line.split(" ")
        if first == 'dir':
            return Node(second)
        else:
            return Leaf(second, int(first))

def get_directory_sizes(fs):
    yield from (dir.size for dir in fs.root.directories if dir.size <= 100_000)

if __name__ == '__main__':
    PATH = 'day07/data.txt'
    # PATH = 'day07/test.txt'
    fs = FileSystem(read_file(PATH))
    # print(fs.root.size)
    print(sum(get_directory_sizes(fs)))