from functions import parse_ints_from_file, extrapolate_value_history


def test_parse_ints_from_file():
    values = parse_ints_from_file('../inputs/example.txt')
    assert len(values) == 3
    assert values[0] == [0, 3, 6, 9, 12, 15]


def test_parse_ints_from_file_with_negative_values():
    values = parse_ints_from_file('../inputs/negative_example.txt')
    assert len(values) == 1
    assert values[0] == [0, -3, -6, -9, -12, -15]


def test_extrapolate_value_history():
    assert extrapolate_value_history([0, 3, 6, 9, 12, 15]) == 18
    assert extrapolate_value_history([1, 3, 6, 10, 15, 21]) == 28
    assert extrapolate_value_history([10, 13, 16, 21, 30, 45]) == 68


def test_extrapolate_value_history_backwards():
    assert extrapolate_value_history([0, 3, 6, 9, 12, 15], False) == -3
    assert extrapolate_value_history([1, 3, 6, 10, 15, 21], False) == 0
    assert extrapolate_value_history([10, 13, 16, 21, 30, 45], False) == 5
