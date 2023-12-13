from race_calculations import calc_number_of_ways_to_beat_record


def test_calc_number_of_ways_to_beat_record():
    assert calc_number_of_ways_to_beat_record(7, 9) == 4
    assert calc_number_of_ways_to_beat_record(15, 40) == 8
    assert calc_number_of_ways_to_beat_record(30, 200) == 9
