from part_one import is_game_valid


def test_is_game_valid_when_valid():
    assert is_game_valid([{'red': 1, 'green': 23}, {'red': 12, 'green': 4}],
                         {'red': 13, 'blue': 6}) is True


def test_is_game_valid_when_invalid():
    assert is_game_valid([{'red': 0, 'green': 23}, {'red': 12, 'green': 4}],
                         {'red': 11, 'blue': 6}) is False
