shape_points = {'A' : 1, 'B': 2, 'C': 3}

def result(a_points, b_points):
    return (a_points - b_points) % 3

def games(PATH):
    with open(PATH, 'r') as file:
        for line in file.readlines():
            yield line.strip().split(' ')


    
def points(games):
    game_state = {
        'X' : 2,
        'Y' : 0,
        'Z' : 1
    }
    game_result = {
        'X' : 0,
        'Y' : 3,
        'Z' : 6}
    shape = {
        0: 3,
        1: 1,
        2: 2
    }

    for game in games:
        b_points = shape_points[game[0]]
        a_points = shape[(b_points + game_state[game[1]]) % 3]
        yield game_result[game[1]] + a_points


if __name__ == '__main__':
    PATH = 'day02/data.txt'
    print(sum(points(games(PATH))))