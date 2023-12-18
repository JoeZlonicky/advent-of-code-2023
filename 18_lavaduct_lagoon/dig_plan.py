from dataclasses import dataclass

type pos = tuple[int, int]


@dataclass
class Edge:
    start: pos
    end: pos
    color: str


@dataclass
class DigPlan:
    edges: list[Edge]
    top_left: pos
    bottom_right: pos


def parse_dig_plan_from_file(file_path: str) -> DigPlan:
    with open(file_path) as f:
        lines = [line.strip() for line in f]

    instructions = [parse_instruction_from_line(line) for line in lines if line]
    return create_dig_plan_from_instructions(instructions)


def create_dig_plan_from_instructions(instructions: list[tuple[str, int, str]]) -> DigPlan:
    x, y = 0, 0
    top, right = 0, 0
    bottom, left = 0, 0
    edges = []

    for instruction in instructions:
        direction, distance, color = instruction
        start = (x, y)
        if direction == 'U':
            y -= distance
            top = min(y, top)
        elif direction == 'R':
            x += distance
            right = max(x, right)
        elif direction == 'D':
            y += distance
            bottom = max(y, bottom)
        elif direction == 'L':
            x -= distance
            left = min(x, left)
        else:
            assert False

        edges.append(Edge(start, (x, y), color))

    return DigPlan(edges, (left, top), (right, bottom))


def parse_instruction_from_line(line: str) -> tuple[str, int, str]:
    direction, distance, color = line.split()
    distance = int(distance)
    color = color.strip('(#)')
    return direction, distance, color
