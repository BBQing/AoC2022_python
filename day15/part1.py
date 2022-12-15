import re

sensor_regex = re.compile(
    r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")


def read_file(PATH):
    with open(PATH, 'r') as file:
        for line in file.read().strip().split("\n"):
            sensors = sensor_regex.match(line.strip())
            sensor_x = sensors.group(1)
            sensor_y = sensors.group(2)
            beacon_x = sensors.group(3)
            beacon_y = sensors.group(4)
            yield int(sensor_x), int(sensor_y), int(beacon_x), int(beacon_y)


def manhattan_distance(x0, y0, x1, y1):
    return abs(x0 - x1) + abs(y0 - y1)


def manhattan_search_interval(x0, y0, x1, y1, row):
    distance = manhattan_distance(x0, y0, x1, y1)
    if y1 == row:
        yield x1, 'beacon'
    if abs(y0 - row) > distance:
        return None
    lbx = x0 - (distance - abs(y0-row))
    ubx = x0 + (distance - abs(y0-row))

    yield lbx, 'start'
    yield ubx, 'end'


def scan_row_by_sensors(row, sensors):
    intervals = [(x, t)
                 for x0, y0, x1, y1 in sensors
                 for x, t in manhattan_search_interval(x0, y0, x1, y1, row)
                 ]
    beacons = len(set(x for x, t in intervals if t == 'beacon'))

    sorted_intervals = sorted([(x, t) for x, t in intervals if t != 'beacon'], key = lambda x: (x[0], (0 if x[1] == 'start' else 1)) )
    return sum(size_intervals(connect_itervals(sorted_intervals))) - beacons
    



def connect_itervals(intervals):
    level = 0
    for x, t in intervals:
        if t == 'start':
            if level == 0:
                yield x, t
            level += 1
        if t == 'end':
            level -= 1
            if level == 0:
                yield x, t

def size_intervals(intervals):
    it = iter(intervals)
    while True:
        try:
            x0 = next(it)[0]
            x1 = next(it)[0]
            yield x1 - x0 + 1
        except StopIteration:
            break

if __name__ == '__main__':
    PATH = 'day15/data.txt'
    ROW = 2_000_000
    # PATH = 'day15/test.txt'
    # ROW = 10

    print(scan_row_by_sensors(ROW, read_file(PATH)))
   