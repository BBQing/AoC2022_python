from itertools import zip_longest


def read_file(PATH):
    with open(PATH, 'r') as file:
        yield from file.read().strip().split("\n\n")


def parse_packets(packets):
    a, b = packets.split("\n")
    a = eval(a)
    b = eval(b)
    return a, b


def compare_packets(a, b):
    return compare(a, b)


def compare(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return compare_ints(left, right)
    if isinstance(left, list) and isinstance(right, list):
        return compare_lists(left, right)
    if isinstance(left, int) and isinstance(right, list):
        return compare_lists(listify(left), right)
    if isinstance(left, list) and isinstance(right, int):
        return compare_lists(left, listify(right))


def compare_ints(a, b):
    if a < b:
        return True
    if a > b:
        return False


def compare_lists(a, b):
    for left, right in zip_longest(a, b):
        if left is None:
            return True
        if right is None:
            return False
        if (n := compare(left, right)) is not None:
            return n


def listify(a):
    aa = list()
    aa.append(a)
    return aa


def distress_signal(PATH):
    for ind, packets in enumerate(read_file(PATH), 1):
        a, b = parse_packets(packets)
        if compare(a, b):
            yield ind


if __name__ == '__main__':
    PATH = 'day13/data.txt'
    # PATH = 'day13/test.txt'

    print(sum(distress_signal(PATH)))
