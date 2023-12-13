from shared_functions import parse_game_from_line


def test_parse_game_from_line():
    assert parse_game_from_line('Game 2: 1 red, 2 green; 3 blue, 4 purple; 23 red') == (
        2, [{'red': 1, 'green': 2}, {'blue': 3, 'purple': 4}, {'red': 23}])
