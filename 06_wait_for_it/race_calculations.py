import math


def calc_number_of_ways_to_beat_record(race_time, record_distance):
    a = -1
    b = race_time
    c = -record_distance
    rhs = b ** 2 - 4 * a * c
    if rhs < 0:
        return 0

    lhs = -b
    rhs = math.sqrt(rhs)
    s1 = (lhs + rhs) / (2 * a)
    s2 = (lhs - rhs) / (2 * a)

    upper_bound, lower_bound = (s1, s2) if s1 > s2 else (s2, s1)
    upper_bound, lower_bound = math.floor(upper_bound), math.ceil(lower_bound)
    return upper_bound - lower_bound + 1
