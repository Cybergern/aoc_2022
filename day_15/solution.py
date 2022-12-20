import re
from time import sleep

input_file = "day_15/input.data"

input_pattern = re.compile('^Sensor at x=([0-9-]+), y=([0-9-]+): closest beacon is at x=([0-9-]+), y=([0-9-]+)')

def get_map_limits(sensor_coverage):
    return (min([k[0] - v for k,v in sensor_coverage.items()]), min([k[1] - v for k,v in sensor_coverage.items()])), (max([k[0] + v for k,v in sensor_coverage.items()]), max([k[1] + v for k,v in sensor_coverage.items()]))

def draw_map(sensor_beacon, sensor_coverage):
    upper_left, bottom_right = get_map_limits(sensor_coverage)
    buffer = " "*len(str(bottom_right[1])) + " "
    for y in range(len(str(bottom_right[1])) - 1, -1, -1):
        line = buffer
        for x in range(upper_left[0], bottom_right[0]+1):
            if x % 5 == 0:
                if len(str(x)) > y:
                    line += str(x)[::-1][y]
                else:
                    line += " "
            else:
                line += " "
        print(line)
        
    for y in range(upper_left[1], bottom_right[1]+1):
        line = f"{y}" + " "*(len(str(bottom_right[1])) - len(str(y))) + " "
        for x in range(upper_left[0], bottom_right[0]+1):
            if (x, y) in sensor_beacon.keys():
                line += "S"
            elif (x, y) in sensor_beacon.values():
                line += "B"
            elif covered_by((x, y), sensor_coverage):
                line += "#"
            else:
                line += "."
        print(line)

def covered_by(pos, coverage):
    for sensor in coverage:
        if abs(sensor[0] - pos[0]) + abs(sensor[1] - pos[1]) <= coverage[sensor]:
            return True
    return False

def extract_sensor_and_beacon(line):
    m = input_pattern.match(line)
    return (int(m.group(1)), int(m.group(2))), (int(m.group(3)), (int(m.group(4))))

def get_sensor_coverage_from_closest_beacon(sensor, beacon):
    reach = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    return reach

def get_tuning_frequency(pos):
    return pos[0] * 4000000 + pos[1]

def get_positive_span(sensor, reach, row, with_limits):
    y_distance = abs(sensor[1] - row)
    if with_limits:
        return max(0, (sensor[0] - reach + y_distance)), min((sensor[0] + reach - y_distance), 4000000)
    else:
        return (sensor[0] - reach + y_distance), (sensor[0] + reach - y_distance)

def covers_span_on_row(row, sensor_coverage, with_limits=False):
    spans = []
    for sensor, reach in sensor_coverage.items():
        y_limits = sensor[1] - reach, sensor[1] + reach
        if row < y_limits[0] or row > y_limits[1]:
            continue
        else:
            spans.append(get_positive_span(sensor, reach, row, with_limits))
    return merge_spans(spans)

def key_func(input):
    return input[0]

def span_sum(spans):
    return sum([x[1]-x[0] for x in spans])

def merge_spans(spans):
    spans.sort(key=key_func)
    result = []
    current_span = spans[0]
    for i in range(1, len(spans)):
        if spans[i][0] > current_span[1]:
            result.append(current_span)
            current_span = spans[i]
        else:
            current_span = (current_span[0], max(spans[i][1], current_span[1]))
    result.append(current_span)
    return result

def find_available_space(sensor_coverage):
    spans = []
    for row in range(0, 4000000):
        spans = covers_span_on_row(row, sensor_coverage, with_limits=True)
        if len(spans) > 1:
            return spans[0][1] + 1, row
    return None

with open(input_file, "r") as file:
    sensor_beacon = {}
    sensor_coverage = {}
    for line in file.readlines():
        sensor, beacon = extract_sensor_and_beacon(line)
        sensor_beacon[sensor] = beacon
    for key in sensor_beacon:
        sensor_coverage[key] = get_sensor_coverage_from_closest_beacon(key, sensor_beacon[key])
    print(span_sum(covers_span_on_row(2000000, sensor_coverage)))
    print(get_tuning_frequency(find_available_space(sensor_coverage)))
