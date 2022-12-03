import heapq


def generate_elves(path):

    with open(path, 'r') as file:
        elfs_calories = 0
        for line in file.readlines():
            if line == '\n':
                yield elfs_calories
                elfs_calories = 0
            else:
                elfs_calories += int(line.strip())


def insert_elf(elves, elf):
    if len(elves) < 3:
        heapq.heappush(elves, elf)
    else:
        heapq.heappushpop(elves, elf)


if __name__ == '__main__':
    PATH = 'day01/data.txt'
    elves = []
    for elf in generate_elves(PATH):
        insert_elf(elves, elf)

    print(sum(elves))
