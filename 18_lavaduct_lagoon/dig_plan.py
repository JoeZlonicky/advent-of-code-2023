from dataclasses import dataclass

type pos = tuple[int, int]


@dataclass
class Edge:
    start: pos
    end: pos


@dataclass
class DigPlan:
    edges: list[Edge]
    top_left: pos
    bottom_right: pos

    def calculate_area(self) -> int:
        area_sum = 0
        for idx, edge in enumerate(self.edges):
            x1, y1 = edge.start
            x2, y2 = edge.end

            area_sum += x1 * y2 - y1 * x2

        return abs(area_sum // 2)

    def calculate_perimeter(self) -> int:
        perimeter = 0
        for edge in self.edges:
            perimeter += abs(edge.end[0] - edge.start[0]) + abs(edge.end[1] - edge.start[1]) + 1

        perimeter -= len(self.edges)  # Remove double-ups
        return perimeter

    def calculate_n_squares(self) -> int:
        return self.calculate_area() + 1 + self.calculate_perimeter() // 2


def parse_dig_plan_from_file(file_path: str, part_2: bool = False) -> DigPlan:
    with open(file_path) as f:
        lines = [line.strip() for line in f]

    if part_2:
        instructions = [parse_instruction_from_line_part_2(line) for line in lines if line]
    else:
        instructions = [parse_instruction_from_line(line) for line in lines if line]
    return create_dig_plan_from_instructions(instructions)


def create_dig_plan_from_instructions(instructions: list[tuple[str, int]]) -> DigPlan:
    x, y = 0, 0
    top, right = 0, 0
    bottom, left = 0, 0
    edges = []

    for instruction in instructions:
        direction, distance = instruction
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

        edges.append(Edge(start, (x, y)))

    return DigPlan(edges, (left, top), (right, bottom))


def parse_instruction_from_line(line: str) -> tuple[str, int]:
    direction, distance, _ = line.split()
    distance = int(distance)
    return direction, distance


def parse_instruction_from_line_part_2(line: str) -> tuple[str, int]:
    _, _, hex_code = line.split()
    hex_code = hex_code.strip('(#)')
    return parse_hex_instruction(hex_code)


def parse_hex_instruction(hex_code: str) -> tuple[str, int]:
    direction_i = int(hex_code[-1])
    direction = ['R', 'D', 'L', 'U'][direction_i]

    distance = int('0x' + hex_code[:-1], 16)
    return direction, distance
