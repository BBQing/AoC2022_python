from itertools import zip_longest
from functools import reduce


def read_file(PATH):
    with open(PATH, 'r') as file:
        for line in file.readlines():
            if line != '\n':
                yield parse_packet(line.strip())


def parse_packet(packet):
    return eval(packet)


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

def parse_signal(PATH):
    a_div = [[2]]
    b_div = [[6]]

    for packet in read_file(PATH):
        a_cmp = compare(packet, a_div)
        b_cmp = compare(b_div, packet)
        yield a_cmp, b_cmp, 1


def accumulate(acc, signal):
    before2, after6, total = acc
    b2, a6, t = signal
    return before2 + b2, after6 + a6, total + t 


def decoder_key(PATH):
    before, after, total = reduce(accumulate, parse_signal(PATH))
    print(before+1, total-after)
    return (before+1) * (total - after + 2)
if __name__ == '__main__':
    PATH = 'day13/data.txt'
    # PATH = 'day13/test.txt'

    print(decoder_key(PATH))
