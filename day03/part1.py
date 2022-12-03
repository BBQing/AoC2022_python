import string

letters = string.ascii_letters

def rucksacks(path):
    with open(path, 'r') as file:
        for line in file.readlines():
            line = line.strip()
            yield line
            

def process_rucksack(rucksack):
    length = len(rucksack) // 2
    rs_a, rs_b = set(rucksack[:length]), set(rucksack[-length:])
    return letters.index(rs_a.intersection(rs_b).pop()) + 1

if __name__ == '__main__':
    PATH = 'day03/data.txt'
    print(sum(map(process_rucksack, rucksacks(PATH))))
   