from typing import Callable
import math


def parse_lines_from_file(file_name):
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        return [line for line in lines if line != '']


def parse_node_from_line(line) -> tuple[str, tuple[str, str]]:
    name, rhs = [section.strip() for section in line.split('=')]
    rhs = rhs.strip('()')
    left, right = [side.strip() for side in rhs.split(',')]
    return name, (left, right)


# Returns instructions string and a dict with node_name : (left, right)
def parse_puzzle_input(input_file_name) -> tuple[str, dict]:
    lines = parse_lines_from_file(input_file_name)

    instructions = lines[0]
    nodes = {}
    for line in lines[1:]:
        name, directions = parse_node_from_line(line)
        nodes[name] = directions

    return instructions, nodes


def count_steps_to_destination(instructions, nodes, start_node, dest_predicate: Callable[[str], bool]) -> int:
    steps = 0
    instruction_i = 0
    instruction_count = len(instructions)
    current_node = start_node

    while not dest_predicate(current_node):
        steps += 1
        instruction = instructions[instruction_i]

        current_node = nodes[current_node][0 if instruction == 'L' else 1]

        instruction_i = (instruction_i + 1) % instruction_count

    return steps


# Assumes ghosts move in a cyclic nature with a constant period between destinations, which is true for all inputs
def count_ghost_steps_to_destination(instructions, nodes, start_letter, dest_letter) -> int:
    start_nodes = {node: node for node in nodes if node[-1] == start_letter}
    steps_to_dest = []
    for node in start_nodes:
        steps = count_steps_to_destination(instructions, nodes, node, lambda x: x[-1] == dest_letter)
        steps_to_dest.append(steps)

    return calc_lcm(steps_to_dest)


def calc_lcm(numbers: list[int]) -> int:
    assert len(numbers) > 0

    lcm = numbers[0]
    if len(numbers) == 1:
        return lcm

    for steps in numbers[1:]:
        lcm = abs(lcm) * (abs(steps) // math.gcd(lcm, steps))
    return lcm
