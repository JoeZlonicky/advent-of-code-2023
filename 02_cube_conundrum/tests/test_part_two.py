from part_two import calculate_minimum_cubes_for_game, calculate_power


def test_calculate_minimum_cubes_for_game():
    assert calculate_minimum_cubes_for_game([{'red': 5, 'green': 3}, {'green': 7, 'red': 3, 'blue': 24}]) == {'red': 5,
                                                                                                              'green': 7,
                                                                                                              'blue': 24}


def test_calculate_power():
    assert calculate_power({'red': 3, 'green': 5, 'blue': 4}) == 60


def test_calculate_power_with_zero_values():
    assert calculate_power({'red': 0, 'green': 3}) == 3


def test_calculate_power_with_no_values():
    assert calculate_power({}) == 0
