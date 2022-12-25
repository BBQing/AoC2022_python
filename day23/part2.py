from collections import defaultdict


def read_file(PATH):
    with open(PATH, "r") as file:

        for x, line in enumerate(file.readlines()):
            for y, char in enumerate(line.strip()):
                if char == "#":
                    yield (x, y)


def north_direction(x, y):
    return [(x-1, y), (x-1, y-1), (x-1, y+1)],  (x - 1, y)


def south_direction(x, y):
    return [(x+1, y), (x+1, y-1), (x+1, y+1)],  (x + 1, y)


def west_direction(x, y):
    return [(x, y-1), (x-1, y-1), (x+1, y-1)],  (x, y - 1)


def east_direction(x, y):
    return [(x, y+1), (x-1, y+1), (x+1, y+1)],  (x, y + 1)


direction_priority = [
    north_direction,
    south_direction,
    west_direction,
    east_direction
]


def find_candidate(elves, elf, n):
    x, y = elf
    if not any(candidate in elves for candidate in [
        (x-1, y), (x-1, y-1), (x-1, y+1),
        (x+1, y), (x+1, y-1), (x+1, y+1),
        (x, y-1),
        (x, y+1),
    ]):
        return None

    for i in range(4):
        direction_function = direction_priority[(n + i) % 4]
        direction_list, direction_result = direction_function(x, y)
        if all(candidate not in elves for candidate in direction_list):
            return direction_result


def make_round(elves, n):
    candidate_dict = {elf: find_candidate(elves, elf, n) for elf in elves}
    return sort_proposals(candidate_dict)


def sort_proposals(candidates):

    sorter = defaultdict(set)

    for k, v in candidates.items():
        if v is None:
            sorter[k].add(k)
        else:
            sorter[v].add(k)

    new_candidates = set(k for k, v in sorter.items() if len(v) == 1)
    new_candidates |= set(cand for v in sorter.values()
                          if len(v) > 1 for cand in v)

    return new_candidates


def empty_ground(PATH):
    elves = set(read_file(PATH))

    i = 0
    while True:
        new_elves = make_round(elves, i)
        i += 1
        if elves == new_elves:
            print(i)
            break
        elves = new_elves
    return elves


if __name__ == '__main__':
    PATH = 'day23/data.txt'
    # PATH = 'day23/test.txt'

    empty_ground(PATH)
