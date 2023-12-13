from part_two import parse_input_file


def test_parse_input_file():
    time, distance = parse_input_file('../inputs/example_input.txt')
    assert time == 71530
    assert distance == 940200
