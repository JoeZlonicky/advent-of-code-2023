from part_one import parse_input_file


def test_parse_input_file():
    times, distances = parse_input_file('../inputs/example_input.txt')
    assert times == [7, 15, 30]
    assert distances == [9, 40, 200]
