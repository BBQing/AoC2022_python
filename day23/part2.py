from collections import defaultdict


corrects = ["""
..............
..............
.......#......
.....###.#....
...#...#.#....
....#...##....
...#.###......
...##.#.##....
....#..#......
..............
..............
..............
""",
            """
..............
.......#......
.....#...#....
...#..#.#.....
.......#..#...
....#.#.##....
..#..#.#......
..#.#.#.##....
..............
....#..#......
..............
..............
""",
            """
..............
.......#......
....#.....#...
...#..#.#.....
.......#...#..
...#..#.#.....
.#...#.#.#....
..............
..#.#.#.##....
....#..#......
..............
..............
"""
            ]
round10_correct = """
......#.....
..........#.
.#.#..#.....
.....#......
..#.....#..#
#......##...
....##......
.#........#.
...#.#..#...
............
...#..#..#..
"""
round0_correct = """
....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..
"""

round1_correct = """
.....#...
...#...#.
.#..#.#..
.....#..#
..#.#.##.
#..#.#...
#.#.#.##.
.........
..#..#...
"""
"""
.....#..
...#...#
.#..#.#.
.....##.
..#.#.##
#..#.#..
#.#.#.##
........
..#..#..
"""

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


def smallest_rectangle(elves):
    min_x = min(candidate[0] for candidate in elves)
    max_x = max(candidate[0] for candidate in elves)
    min_y = min(candidate[1] for candidate in elves)
    max_y = max(candidate[1] for candidate in elves)

    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)


def draw_field(candidates):
    min_x = min(candidate[0] for candidate in candidates)
    max_x = max(candidate[0] for candidate in candidates)
    min_y = min(candidate[1] for candidate in candidates)
    max_y = max(candidate[1] for candidate in candidates)

    print("\n".join(
        ''.join("." if (i, j)
                not in candidates else "#" for j in range(min_y, max_y + 1)
                )
        for i in range(min_x, max_x+1))
    )
    return "\n".join(
        ''.join("." if (i, j)
                not in candidates else "#" for j in range(min_y, max_y + 1)
                )
        for i in range(min_x, max_x+1)
    )


def compare(elves, correct):
    drawn_elves = draw_field(elves)

    for i, j in zip(drawn_elves.strip(), correct.strip()):
        print(f"Drawn: {i} , correct {j}", i == j)



def elves_from_correct(elves, correct_one):
    min_x = min(candidate[0] for candidate in elves)
    
    min_y = min(candidate[1] for candidate in elves)
    for i, line in enumerate(correct_one.strip().split("\n"), min_x):
        for j, char in enumerate(line, min_y):
            if char == "#":
                yield i, j
if __name__ == '__main__':
    PATH = 'day23/data.txt'
    # PATH = 'day23/test.txt'

    empty_ground(PATH)
