from operator import itemgetter
from collections import defaultdict

def read_file(path):
    data = []
    with open(path, 'r') as file:
        for line in file.readlines():
            data.append([int(i) for i in line.strip()])

    return data


def takewhile_with_last(predicate, iterable):
    for i in iterable:
        yield i
        if not predicate(i):
            break


def process_data(data):

    row_count = len(data)
    column_count = len(data[0])
    for i in range(row_count):
        yield from row_scan(data, i)
        yield from row_scan(data, i, True)
    for i in range(column_count):
        yield from column_scan(data, i)
        yield from column_scan(data, i, True)


def row_scan(data, row, reverse=False):

    for column, value in enumerate(data[row]):
        col_slice = slice(None, column) if reverse else slice(column+1, None)
        yield row, column, \
            len(list(takewhile_with_last(lambda x: x < value,
                                         data[row][col_slice] if not reverse else reversed(data[row][col_slice]))))


def column_scan(data, column, reverse=False):
    column_data = list(map(itemgetter(column), data))
    for row, value in enumerate(column_data):
        row_slice = slice(None, row) if reverse else slice(row+1, None)

        yield row, column,  \
            len(list(takewhile_with_last(lambda x: x < value,
                               column_data[row_slice] if not reverse else reversed(column_data[row_slice]))))


def process_data(data):
    row_count = len(data)
    column_count = len(data[0])
    for i in range(row_count):
        yield from row_scan(data, i)
        yield from row_scan(data, i, True)
    for i in range(column_count):
        yield from column_scan(data, i)
        yield from column_scan(data, i, True)


def max_scenic_score(data):
    data_dict = defaultdict(lambda: 1)

    for row, column, value in process_data(data):
        data_dict[(row, column)] *= value

    return max(data_dict.values())


if __name__ == '__main__':
    PATH = 'day08/data.txt'
    # PATH = 'day08/test.txt'

    data = read_file(PATH)
    print(max_scenic_score(data))
