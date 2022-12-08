from operator import itemgetter

def read_file(path):
    data = []
    with open(path, 'r') as file:
        for line in file.readlines():
            data.append(line.strip())

    return data

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
    visibility = -1
    
    it = enumerate(map(int, data[row]))
    if reverse:
        it = reversed(list(it))
    for ind, tree in it:
        if tree > visibility:
            yield row, ind
            visibility = tree
        if visibility == 9:
            break

def column_scan(data, column, reverse=False):
    visibility = -1
    it = enumerate(map(int, map(itemgetter(column), data)))
    if reverse:
        it = reversed(list(it))
    for ind, tree in it:
        if tree > visibility:
            yield ind, column
            visibility = tree
        if visibility == 9:
            break

if __name__ == '__main__':
    PATH = 'day08/data.txt'
    # PATH = 'day08/test.txt'

    data = read_file(PATH)
    print(len(set(process_data(data))))
    # print(data)