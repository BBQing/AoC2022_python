import string
from itertools import islice
from functools import reduce

letters = string.ascii_letters

def rucksacks(path):
    with open(path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            yield set(line)


def batched(iterable, n):
    "Batch data into lists of length n. The last batch may be shorter."
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while (batch := list(islice(it, n))):
        yield batch

def badge(group):
    return letters.index(reduce(set.intersection, group).pop()) + 1
    

if __name__ == '__main__':
    PATH = 'day03/data.txt'
    elves = rucksacks(PATH)
    print(sum(map(badge, batched(elves, 3))))
        
    
