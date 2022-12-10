
def read_file(path):
    with open(path, 'r') as file:
        for line in file.readlines():
            cmd, n = line.strip().split(" ")
            yield cmd, int(n)
    

class Body:

    def __init__(self, i) -> None:
        self.x = 0
        self.y = 0
        self.i = i
        self.child = None
        self.parent = None

    def update(self, x, y):
        x_diff = x - self.x
        y_diff = y - self.y
        if x_diff in [-2, 2] or y_diff in [-2, 2]:

            self.x = self.x + self.cutoff(x_diff)
            self.y = self.y + self.cutoff(y_diff)
            yield from self.notify()
        

    def notify(self):
        yield from self.child.update(self.x, self.y)
        

    def cutoff(self, diff):
        if diff == 2:
            return 1
        if diff == -2:
            return -1
        return diff
    
    

class Channel:

    def __init__(self) -> None:
        self.begin = None
        self.end = None
        
    def add_body(self, body):
        if self.begin is None:
            self.begin = body
            self.begin.parent = self
            self.end = body
            self.end.child = self
        else:
            body.parent = self.end
            body.child = self
            self.end.child = body
            self.end = body
            
    
    def move(self, cmd):
        if cmd == 'R':
            self.begin.y += 1
        if cmd == 'L':
            self.begin.y -= 1
        if cmd == 'U':
            self.begin.x += 1
        if cmd == 'D':
            self.begin.x -= 1
    
    def run_command(self, cmd, n):
        for _ in range(n):
            self.move(cmd)
            yield from self.begin.notify()

    def run(self, data):
        for cmd, n in data:
            yield from self.run_command(cmd, n)
    
    def update(self, x, y):
        yield x, y

def process_commands(data):
    channel = Channel()
    for i in range(10):
        channel.add_body(Body(i))
    
    return set(channel.run(data))

if __name__ == '__main__':
    PATH = 'day09/data.txt'
    # PATH = 'day09/test2.txt'


    result = process_commands(read_file(PATH))
    print(len(result))
    
