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


def count_ghost_steps_to_destination(instructions, nodes, start_letter, dest_letter) -> int:
    steps = 0
    instruction_i = 0
    instruction_count = len(instructions)
    current_nodes = {node for node in nodes if node[-1] == start_letter}

    while any({node[-1] != 'Z' for node in current_nodes}):
        steps += 1
        instruction = instructions[instruction_i]

        current_nodes = {nodes[node][0 if instruction == 'L' else 1] for node in current_nodes}

        instruction_i = (instruction_i + 1) % instruction_count

    return steps
