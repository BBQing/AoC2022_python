import re

split_regex = re.compile(r'[-,]')
def assignments(PATH):
    with open(PATH, 'r') as file:
        for line in file.readlines():
            yield parse_line(line)


def parse_line(line):
    return split_regex.split(line.strip())

def contains(line):
    a1, a2, b1, b2 = map(int, line)
    return _contains(a1, a2, b1, b2)

def _contains(a1, a2, b1, b2):
    if (a1 - b1) * (a2 - b2) <= 0:
        return True
    else:
        return False
if __name__ == '__main__':
    PATH = 'day04/data.txt'
    print(sum(map(contains, assignments(PATH))))