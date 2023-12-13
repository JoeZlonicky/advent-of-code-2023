import pytest
from functions import parse_lines_from_file, parse_node_from_line, parse_puzzle_input, count_steps_to_destination, \
    count_ghost_steps_to_destination, calc_lcm


@pytest.fixture
def example_setup():
    return parse_puzzle_input('../inputs/example.txt')


@pytest.fixture
def example2_setup():
    return parse_puzzle_input('../inputs/example2.txt')


@pytest.fixture
def example3_setup():
    return parse_puzzle_input('../inputs/example3.txt')


def test_parse_lines_from_file():
    lines = parse_lines_from_file('../inputs/example.txt')
    assert len(lines) == 8
    assert lines[0] == 'RL'
    assert lines[1] == 'AAA = (BBB, CCC)'


def test_parse_node_from_line():
    line = 'AAA = (BBB, CCC)'
    name, directions = parse_node_from_line(line)
    assert name == 'AAA'
    assert directions[0] == 'BBB'
    assert directions[1] == 'CCC'


def test_parse_puzzle_input():
    instructions, nodes = parse_puzzle_input('../inputs/example.txt')
    assert instructions == 'RL'
    assert len(nodes) == 7
    assert nodes['AAA'] == ('BBB', 'CCC')


def test_count_steps_to_destination(example_setup, example2_setup):
    assert count_steps_to_destination(example_setup[0], example_setup[1], 'AAA', lambda x: x == 'ZZZ') == 2
    assert count_steps_to_destination(example2_setup[0], example2_setup[1], 'AAA', lambda x: x == 'ZZZ') == 6


def test_count_ghost_steps_to_destination(example3_setup):
    assert count_ghost_steps_to_destination(example3_setup[0], example3_setup[1], 'A', 'Z') == 6


def test_calc_lcm():
    assert calc_lcm([1, 2, 3]) == 6
    assert calc_lcm([4, 8]) == 8
    assert calc_lcm([9]) == 9
