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


def count_steps_to_destination(instructions, nodes, start_node, dest_node) -> int:
    steps = 0
    instruction_i = 0
    instruction_count = len(instructions)
    current_node = start_node

    while current_node != dest_node:
        steps += 1
        instruction = instructions[instruction_i]

        current_node = nodes[current_node][0 if instruction == 'L' else 1]

        instruction_i = (instruction_i + 1) % instruction_count

    return steps


# Assumes ghosts move in a cyclic nature with a constant period between destinations, which is true for all inputs
def count_ghost_steps_to_destination(instructions, nodes, start_letter, dest_letter) -> int:
    steps = 0
    instruction_i = 0
    instruction_count = len(instructions)
    current_nodes = {node: node for node in nodes if node[-1] == start_letter}
    steps_to_dest: dict[str, int] = {}

    while current_nodes:
        steps += 1
        instruction = instructions[instruction_i]

        current_nodes = {node: nodes[current_nodes[node]][0 if instruction == 'L' else 1] for node in current_nodes}
        to_remove = []
        for node in current_nodes:
            current_node = current_nodes[node]
            if current_node[-1] != dest_letter:
                continue

            steps_to_dest[node] = steps
            to_remove.append(node)
        for node in to_remove:
            current_nodes.pop(node)

        instruction_i = (instruction_i + 1) % instruction_count

    start_nodes = list(steps_to_dest.keys())
    lcm = steps_to_dest[start_nodes[0]]
    for other in start_nodes[1:]:
        other_steps = steps_to_dest[other]
        lcm = abs(lcm) * (abs(other_steps) // math.gcd(lcm, other_steps))

    return lcm
