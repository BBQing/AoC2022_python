def generate_elves(path):

    with open(path, 'r') as file:
        elfs_calories = 0
        for line in file.readlines():
            if line == '\n':
                yield elfs_calories
                elfs_calories = 0
            else:
                elfs_calories += int(line.strip())


if __name__ == '__main__':
    PATH = 'day01/data.txt'
    print(max(generate_elves(PATH)))
