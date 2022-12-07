from collections import deque

def part1(path):
    last_signals = deque()
    it = enumerate(stream(path), 1)
    for _ in range(13):
        _, char = next(it)
        last_signals.appendleft(char)
    for ind, char in it:
        last_signals.appendleft(char)
        if len(last_signals) == len(set(last_signals)):
            return ind
        last_signals.pop()
            

    
    return 1

def stream(path):
    with open(path, 'r') as file:
        for char in file.readline().strip():
            yield char

if __name__ == '__main__':
    PATH = 'day06/data.txt'
    import tempfile
    fp = tempfile.mkstemp(text=True)
    with open(fp[1], 'w') as file:
        file.write("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw")
    
    
    # print(part1(fp[1]))
    print(part1(PATH))