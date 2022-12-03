shape_points = {'A' : 1, 'B': 2, 'C': 3}

result_points = {
    0: 3,
    1: 6,
    2: 0
}
def result(a_points, b_points):
    return (a_points - b_points) % 3

def games(PATH):
    with open(PATH, 'r') as file:
        for line in file.readlines():
            yield line.strip().split(' ')

def points(games):
    shape_played = {
        'X' : 'A',
        'Y' : 'B',
        'Z' : 'C'
    }
    for game in games:
        a_points = shape_points[shape_played[game[1]]]
        b_points = shape_points[game[0]]
        yield result_points[result(a_points, b_points)] + a_points


if __name__ == '__main__':
    PATH = 'day02/data.txt'
    print(sum(points(games(PATH))))