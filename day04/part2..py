import re

split_regex = re.compile(r'[-,]')
def assignments(PATH):
    with open(PATH, 'r') as file:
        for line in file.readlines():
            yield parse_line(line)


def parse_line(line):
    return split_regex.split(line.strip())

def overlaps(line):
    a1, a2, b1, b2 = map(int, line)
    return _overlaps(a1, a2, b1, b2)

def _overlaps(a1, a2, b1, b2):
    if (a1 <= b2 and a1 >= b1) or (b1 <= a2 and b1 >= a1):
        return True
    else:
        return False 
if __name__ == '__main__':
    PATH = 'day04/data.txt'
    print(sum(map(overlaps, assignments(PATH))))